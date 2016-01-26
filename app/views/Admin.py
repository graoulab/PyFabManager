from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import HttpRequest , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.utils.html import escape
from ..forms.register import UserCreateForm
from ..forms.Config import ConfigSiteForm
from ..forms.Machine import MachineForm
from ..forms.FormAtelier import AtelierForm
from ..models import *
from ..fct import *
from django.core.urlresolvers import reverse

@user_passes_test(lambda u: u.is_superuser)
def AdminIndex(request):
    return render(
    request, 
    'app/Admin.html', 
    context = 
        {
            'title':_('Admin'),
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
            return HttpResponseRedirect(reverse('admin'))

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = Config.objects.all().last()
        form = ConfigSiteForm(instance = conf)

    return render(
    request, 
    'app/register.html', 
    context = 
        {
            'title':_('Modif LAB'),
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
            'title':_('List Des Matiere Disponible'),
            'type': 'Matiere',
            'data' : Matiere.objects.all(),
            'year':datetime.now().year,
        })

@user_passes_test(lambda u: u.is_superuser)
def ModifMateriaux(request , Action):
    print(request.method)
    if request.method == 'POST':
        if Action == 'Suppr':
            Matiere.objects.filter(Nom=request.POST.get('Nom')).delete()
        else :
            NewMatier = Matiere(Nom = request.POST.get('Nom'))
            NewMatier.save()
    return HttpResponseRedirect(reverse('ListMateriaux'))

@user_passes_test(lambda u: u.is_superuser)
def ListLicence(request):
    return render(
    request, 
    'app/List.html', 
    context = 
        {
            'title':_('List Des Licences Disponible'),
            'type': 'Licences',
            'data' : Licences.objects.all(),
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
        return HttpResponseRedirect(reverse('ListLicence'))

@user_passes_test(lambda u: u.is_superuser)
def ListCategorie(request):
    return render(
    request, 
    'app/List.html', 
    context = 
        {
            'title':_('List Des Licences Disponible'),
            'type': 'Categorie',
            'data' : Categorie.objects.all(),
            'year':datetime.now().year,
        })

@user_passes_test(lambda u: u.is_superuser)
def ModifCategorie(request , Action ):
    if request.method == 'POST':
        if Action == 'Suppr':
            Categorie.objects.filter(Nom=request.POST.get('Nom')).delete()
        else :
            NewLicences = Categorie(Nom = request.POST.get('Nom'))
            NewLicences.save()
        return HttpResponseRedirect(reverse('ListCategorie'))

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
                'title':_('List Des utilisateur'),
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
    return HttpResponseRedirect(reverse('ListUser'))

@user_passes_test(lambda u: u.is_superuser)
def DeleteMachine(request,NbPage=1):
    Machine.objects.filter(id=NbPage).delete()
    return HttpResponseRedirect(reverse('ListMachine'))

@user_passes_test(lambda u: u.is_superuser)
def CreationMachine(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MachineForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            NewMachine = Machine(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                Descritpion = form.cleaned_data['Descritpion'],Cout= form.cleaned_data['Cout'],CoutAdh= form.cleaned_data['CoutAdh']
                ,fichier = form.cleaned_data['fichier'])
            NewMachine.save()
            return HttpResponseRedirect(reverse('admin'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MachineForm()

    return render(
    request, 
    'app/AddMachine.html', 
    context = 
        {
            'title':_('Creer Machine'),
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
                    Descritpion = form.cleaned_data['Descritpion'],fichier = form.cleaned_data['fichier'],
                    Cout= form.cleaned_data['Cout'],CoutAdh= form.cleaned_data['CoutAdh'])
            else : 
                NewMachine = Machine(Titre = form.cleaned_data['Titre'],Image = Machine.objects.filter(id=NbPage)[0].Image,
                    Descritpion = form.cleaned_data['Descritpion'],fichier = form.cleaned_data['fichier'],
                    Cout= form.cleaned_data['Cout'],CoutAdh= form.cleaned_data['CoutAdh'])
            NewMachine.id = NbPage
            NewMachine.save()
            
            return HttpResponseRedirect(reverse('admin'))

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = Machine.objects.filter(id =NbPage)[0]
        form = MachineForm(instance = conf)

    return render(
    request, 
    'app/AddMachine.html', 
    context = 
        {
            'title':_('Modif Machine'),
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
        if form.is_valid():
            print('Rang ' + str(form.cleaned_data['Rang']))
            NewMAtelier = Atelier(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                    Descritpion = form.cleaned_data['Descritpion'],nBplace=form.cleaned_data['nBplace'],
                    prix= form.cleaned_data['prix'],prixAdh= form.cleaned_data['prixAdh'],
                    date =form.cleaned_data['date'],Rang =form.cleaned_data['Rang'])
            NewMAtelier.save()
            return HttpResponseRedirect(reverse('admin'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AtelierForm()

    return render(
    request, 
    'app/AddAtelier.html', 
    context = 
        {
            'title':_('Modif LAB'),
            'year':datetime.now().year,
            'form': form,
        })

@user_passes_test(lambda u: u.is_superuser)
def EditAtelier(request, NbPage=1):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AtelierForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            if form.cleaned_data['Image'] :  
                NewMachine = Atelier(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                    Descritpion = form.cleaned_data['Descritpion'],nBplace=form.cleaned_data['nBplace'],
                    prix= form.cleaned_data['prix'],prixAdh= form.cleaned_data['prixAdh'],
                    date =form.cleaned_data['date'],Rang =form.cleaned_data['Rang'])
            else : 
                NewMachine = Atelier(Titre = form.cleaned_data['Titre'],Image = Atelier.objects.filter(id=NbPage)[0].Image,
                    Descritpion = form.cleaned_data['Descritpion'],nBplace=form.cleaned_data['nBplace'],
                    prix= form.cleaned_data['prix'],prixAdh= form.cleaned_data['prixAdh'],
                    date =form.cleaned_data['date'],Rang =form.cleaned_data['Rang'])
            NewMachine.id = NbPage
            NewMachine.save()
            
            return HttpResponseRedirect(reverse('admin'))

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = Atelier.objects.filter(id =NbPage)[0]
        form = AtelierForm(instance = conf)

    return render(
    request, 
    'app/AddAtelier.html', 
    context = 
        {
            'title':_('Modif Atelier'),
            'year':datetime.now().year,
            'form': form,
        })    

@user_passes_test(lambda u: u.is_superuser)
def DeleteAtelier(request,NbPage=1):
    Atelier.objects.filter(id=NbPage).delete()
    return HttpResponseRedirect(reverse('ListAtelier'))