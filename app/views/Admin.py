from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django import template
from datetime import datetime
from django.utils.html import escape
from ..forms.register import UserCreateForm
from ..forms.Config import ConfigSiteForm
from ..forms.Machine import MachineForm
from ..forms.FormAtelier import AtelierForm
from ..models import *
from ..fct import *

@user_passes_test(lambda u: u.is_superuser)
def AdminIndex(request):
    return render(
    request, 
    'app/Admin.html', 
    context = 
        {
            'title':'Admin',
            'year':datetime.now().year,
        })

@user_passes_test(lambda u: u.is_superuser)
def ConfigWebView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConfigSiteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            NewConfig = Config(NomLab = form.cleaned_data['NomLab'],AdresseContact = form.cleaned_data['AdresseContact'],
                Rue = form.cleaned_data['Rue'],
                ville = form.cleaned_data['ville'],CodePostal= form.cleaned_data['CodePostal'])
            NewConfig.id = 1
            NewConfig.save()
            return HttpResponseRedirect('/Admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = Config.objects.all().last()
        form = ConfigSiteForm(instance = conf)

    return render(
    request, 
    'app/register.html', 
    context = 
        {
            'title':'Modif LAB',
            'year':datetime.now().year,
            'form': form,
        })

@user_passes_test(lambda u: u.is_superuser)
def ListMateriaux(request):
    return render(
    request, 
    'app/List.html', 
    context = 
        {
            'title':'List Des Matiere Disponible',
            'type': 'Matiere',
            'data' : Matiere.objects.all(),
            'year':datetime.now().year,
        })

@user_passes_test(lambda u: u.is_superuser)
def ModifLicence(request , Action ):
    if request.method == 'POST':
        if Action == 'Suppr':
            Licences.objects.filter(Nom=request.POST.get('Nom')).delete()
        else :
            NewLicences = Licences(Nom = request.POST.get('Nom'))
            NewLicences.save()
        return HttpResponseRedirect('/Admin/ListLicence/')

@user_passes_test(lambda u: u.is_superuser)
def ModifMateriaux(request , Action):
    if request.method == 'POST':
        if Action == 'Suppr':
            Matiere.objects.filter(Nom=request.POST.get('Nom')).delete()
        else :
            NewMatier = Matiere(Nom = request.POST.get('Nom'))
            NewMatier.save()
        return HttpResponseRedirect('/Admin/ListMateriaux/')

@user_passes_test(lambda u: u.is_superuser)
def ListLicence(request):
    return render(
    request, 
    'app/List.html', 
    context = 
        {
            'title':'List Des Licences Disponible',
            'type': 'Licences',
            'data' : Licences.objects.all(),
            'year':datetime.now().year,
        })

@user_passes_test(lambda u: u.is_superuser)
def ListUser(request,NbPage=1):
    #
    assert isinstance(request, HttpRequest)
    nbelement = 10
    data = list(utilisateur.objects.all())
    paginator = Paginator(data, nbelement)
    try:
        contacts = paginator.page(NbPage)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    data = contacts
    return render(
            request,
            'app/ListUser.html',
            context =
            {
                'title':'List Des utilisateur',
                'type': 'Licences',
                'data':data,
                'year':datetime.now().year,
                'nb':paginator.page_range,
            })

@user_passes_test(lambda u: u.is_superuser)
def GestionUser(request,Action,NbPage=1):
    if Action == 'Supp':
        NewUtilisateur = utilisateur.objects.filter(id=NbPage)
        User.objects.filter(id=NewUtilisateur[0].user.id).delete()
        NewUtilisateur.delete()
    if Action == 'Admin':
        NewUtilisateur = User.objects.filter(id= utilisateur.objects.filter(id=NbPage)[0].user.id)[0]
        if NewUtilisateur.is_superuser :
            NewUtilisateur.is_superuser = False
        else :
           NewUtilisateur.is_superuser = True
        NewUtilisateur.save()
    return HttpResponseRedirect('/Admin/ListUser/')

@user_passes_test(lambda u: u.is_superuser)
def DeleteMachine(request,NbPage=1):
    Machine.objects.filter(id=NbPage).delete()
    return HttpResponseRedirect('/ListMachine/')

@user_passes_test(lambda u: u.is_superuser)
def GestionMachine(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MachineForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            NewMachine = Machine(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                Descritpion = form.cleaned_data['Descritpion'],Cout= form.cleaned_data['Cout'])
            NewMachine.save()
            return HttpResponseRedirect('/Admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MachineForm()

    return render(
    request, 
    'app/Machine.html', 
    context = 
        {
            'title':'Modif LAB',
            'year':datetime.now().year,
            'form': form,
        })

@user_passes_test(lambda u: u.is_superuser)
def EditMachine(request, NbPage=1):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MachineForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            if form.cleaned_data['Image'] :  
                NewMachine = Machine(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                    Descritpion = form.cleaned_data['Descritpion'],
                    Cout= form.cleaned_data['Cout'],CoutAdh= form.cleaned_data['CoutAdh'])
            else : 
                NewMachine = Machine(Titre = form.cleaned_data['Titre'],Image = Machine.objects.filter(id=NbPage)[0].Image,
                    Descritpion = form.cleaned_data['Descritpion'],
                    Cout= form.cleaned_data['Cout'],CoutAdh= form.cleaned_data['CoutAdh'])
            NewMachine.id = NbPage
            NewMachine.save()
            
            return HttpResponseRedirect('/Admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = Machine.objects.filter(id =NbPage)[0]
        form = MachineForm(instance = conf)

    return render(
    request, 
    'app/Machine.html', 
    context = 
        {
            'title':'Modif LAB',
            'year':datetime.now().year,
            'form': form,
        })    

@user_passes_test(lambda u: u.is_superuser)
def CreationAtelier(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = AtelierForm(request.POST, request.FILES)
        # check whether it's valid:
        print(form.errors.as_json())
        if form.is_valid():
            NewMAtelier = Atelier(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                Descritpion = form.cleaned_data['Descritpion'],prix= form.cleaned_data['Cout'],
                nBplace=form.cleaned_data['NombredePlace'],
                prixAdh= form.cleaned_data['CoutAdh'],date =form.cleaned_data['Date'])
            NewMAtelier.save()
            return HttpResponseRedirect('/Admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AtelierForm()

    return render(
    request, 
    'app/AddAtelier.html', 
    context = 
        {
            'title':'Modif LAB',
            'year':datetime.now().year,
            'form': form,
        })