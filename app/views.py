"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django import template
from datetime import datetime
from .forms.register import UserCreateForm
from .forms.Config import ConfigSiteForm
from .models import *
register = template.Library()
@register.simple_tag
def SiteName():
    return Config.objects.all().last().NomLab
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context = 
        {
            'LastProject': Projet.objects.all().last(),
            'LastEvent': Atelier.objects.all().last(),
            'LastMachine':Machine.objects.all().last(),
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context = 
        {
            'contact':  Config.objects.all().last().AdresseContact,
            'ville':    Config.objects.all().last().ville ,
            'adresse':  Config.objects.all().last().Rue,
            'codepostal':Config.objects.all().last().CodePostal,
            'title':'Contact',
            'message':'Pour nous contacter.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context = 
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = User.objects.create_user(username= form.cleaned_data['username'],email= form.cleaned_data['email'],password = form.cleaned_data['password1'],
            first_name = form.cleaned_data['Nom'] , last_name = form.cleaned_data['Prenom'])
            user.save()
            PhoneNumber = form.cleaned_data['PhoneNumber']
            p = utilisateur(PhoneNumber=PhoneNumber,user =user)
            p.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCreateForm()

    return render(
    request, 
    'app/register.html', 
    context = 
        {
            'title':'Inscription',
            'year':datetime.now().year,
            'form': form,
        })
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')
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
            NewConfig = Config(NomLab = form.cleaned_data['Nom'],AdresseContact = form.cleaned_data['AddresseDeContact'],Rue = form.cleaned_data['Rue'],
                ville = form.cleaned_data['Ville'],CodePostal= form.cleaned_data['CodePostal'])
            NewConfig.id = 1
            NewConfig.save()
            return HttpResponseRedirect('/Admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConfigSiteForm()

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
def ModifMateriaux(request , Action , Nom):
    if Action == 'Suppr':
        Matiere.objects.filter(Nom=Nom).delete()
    else :
        NewMatier = Matiere(Nom = Nom)
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
def ListUser(request):
    return render(
    request, 
    'app/ListUser.html', 
    context = 
        {
            'title':'List Des utilisateur',
            'type': 'Licences',
            'data' : utilisateur.objects.all(),
            'year':datetime.now().year,
        })
@user_passes_test(lambda u: u.is_superuser)
def ModifLicence(request , Action , Nom):
    if Action == 'Suppr':
        Licences.objects.filter(Nom=Nom).delete()
    else :
        NewLicences = Licences(Nom = Nom)
        NewLicences.save()
    return HttpResponseRedirect('/Admin/ListLicence/')