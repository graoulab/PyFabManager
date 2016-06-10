# coding: utf-8 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest , HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from ..forms.register import UserCreateForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import render
from django.utils import timezone
from ..forms.FormSearch import *
from datetime import datetime
from ..forms.Projet import *
from django import template
from ..models import *
from ..fct import *

def ListProjet(request, NbPage=1):
    assert isinstance(request, HttpRequest)
    nbelement = 10
    Temp = Projet.objects.all()
    if request.GET.get('Categorie'):
         Temp = Temp.filter(Categorie = request.GET['Categorie'] )
    if request.GET.get('Matiere'):
        Temp = Temp.filter(Matiere = request.GET['Matiere'] )
    if request.GET.get('Machine') :
        Temp = Temp.filter(Machine =request.GET['Machine'])
    data = list(Temp.order_by('-id'))
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
    form = SearchForm()
    return render(
            request,
            'app/ListProjet.html',
            context =
            {
                'title':_('Liste Projet'),
                'Type':'Projet',
                'form' : form,
                'data':data,
                'year':datetime.now().year,
                'nb':paginator.page_range,
            })

@user_passes_test(lambda u: u.is_authenticated)
def CreationProjet(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjetForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            NewMachine = Projet(titre = form.cleaned_data['titre'],Image = form.cleaned_data['Image'],
                Contenue = form.cleaned_data['Contenue'],fichier = form.cleaned_data['fichier'],
                Date = datetime.now())
            NewMachine.save()
            NewMachine.Utilisateur.add(utilisateur.objects.filter(user = request.user.id)[0])
            for i in form.cleaned_data['Materiaux'] :
                NewMachine.Materiaux.add(i)
            for i in form.cleaned_data['Machine'] :
                NewMachine.Machine.add(i)
            if form.cleaned_data['Licence'] :
                NewMachine.Licence.add(form.cleaned_data['Licence'])
            if form.cleaned_data['Categorie'] :
                NewMachine.Categorie.add(form.cleaned_data['Categorie']) 
            
            return HttpResponseRedirect(reverse('home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjetForm()
    return render(
    request, 
    'app/AddProjet.html', 
    context = 
        {
            'title':_('Creer Projet'),
            'year':datetime.now().year,
            'form': form,
        })

def ViewProjet(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    data = Projet.objects.filter(id=NbPage)
    return render(
            request,
            'app/DetailProjet.html',
            context = 
            {
                'title':data[0].titre,
                'data':data[0],
                'year':datetime.now().year,
            })

@user_passes_test(lambda u: u.is_authenticated)
def EditProjet(request, NbPage=1):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjetForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            if form.cleaned_data['Image'] :  
                NewMachine = Projet(titre = form.cleaned_data['titre'],Image = form.cleaned_data['Image'],
                Contenue = form.cleaned_data['Contenue'],fichier = form.cleaned_data['fichier'],
                Date = datetime.now()
                )
            else : 
                NewMachine = Projet(titre = form.cleaned_data['titre'],Image = Projet.objects.filter(id=NbPage)[0].Image,
                    Contenue = form.cleaned_data['Contenue'],fichier = form.cleaned_data['fichier'],
                    Date = datetime.now()
                    )
            NewMachine.id = NbPage
            NewMachine.save()
            NewMachine.Materiaux.clear()
            NewMachine.Utilisateur.clear()
            NewMachine.Machine.clear()
            NewMachine.Licence.clear()
            NewMachine.Categorie.clear()
            NewMachine.Utilisateur.add(utilisateur.objects.filter(user = request.user.id)[0])
            for i in form.cleaned_data['Materiaux'] :
                NewMachine.Materiaux.add(i)
            for i in form.cleaned_data['Machine'] :
                NewMachine.Machine.add(i)
            NewMachine.Licence.add(form.cleaned_data['Licence'])
            NewMachine.Categorie.add(form.cleaned_data['Categorie'])
            
            return HttpResponseRedirect(reverse('ViewProjet',kwargs={'NbPage': NbPage
                }))

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = Projet.objects.filter(id =NbPage)[0]
        form = ProjetForm(instance = conf)

    return render(
    request, 
    'app/AddProjet.html', 
    context = 
        {
            'title':_('Modif Projet'),
            'year':datetime.now().year,
            'form': form,
        })    

@user_passes_test(lambda u: u.is_authenticated)
def DeleteProjet(request,NbPage=1):
    Projet.objects.filter(id=NbPage).delete()
    return HttpResponseRedirect(reverse('ListProjet'))
