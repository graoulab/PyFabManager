from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import HttpRequest , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django import template
from datetime import datetime
from ..forms.register import UserCreateForm
from ..forms.Config import ConfigSiteForm
from ..forms.Machine import MachineForm
from ..forms.EditProfil import EditProfilForm
from ..models import *
from ..fct import *
from django.core.urlresolvers import reverse
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
            'title':_('Home Page'),
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
            'title':_('Contact'),
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
            'title':_('About'),
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
            if len( User.objects.all() ) == 0 :
                superuser = True
            else :
                superuser = False
            user = User.objects.create_user(username= form.cleaned_data['username'],email= form.cleaned_data['email'],
                password = form.cleaned_data['password1'],is_superuser = superuser,
                first_name = form.cleaned_data['Nom'] , last_name = form.cleaned_data['Prenom'])
            user.save()
            PhoneNumber = form.cleaned_data['PhoneNumber']
            p = utilisateur(PhoneNumber=PhoneNumber,user =user)
            p.save()
            return HttpResponseRedirect(reverse('home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCreateForm()

    return render(
    request, 
    'app/register.html', 
    context = 
        {
            'title':_('Inscription'),
            'year':datetime.now().year,
            'form': form,
        })
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('home'))

@user_passes_test(lambda u: u.is_authenticated)
def ViewProfil(request):
    User = utilisateur.objects.filter(user = request.user.id)
    Evenement = Atelier.objects.filter(UtilisateurInscrit = User).order_by('-id')[:5]
    projet = Projet.objects.filter(Utilisateur = User).order_by('-id')[:5]
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Profil.html',
        context = 
        {
            'title':_('Profil'),
            'year':datetime.now().year,
            'Projet' : projet,
            'Evenement':Evenement,
        }
    )

@user_passes_test(lambda u: u.is_authenticated)
def EditProfil(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreateForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect(reverse('Profil',kwargs={'NbPage': NbPage
                }))

    # if a GET (or any other method) we'll create a blank form
    else:
        conf = utilisateur.objects.filter(user = request.user.id)[0]
        form = EditProfilForm(initial = {
            'first_name':conf.user.first_name,
            'last_name' :conf.user.last_name,
            'email' :conf.user.email,
            'PhoneNumber' :conf.PhoneNumber,
            'NewsLetter' :conf.NewsLetter,
            })

    return render(
    request, 
    'app/EditProfil.html', 
    context = 
        {
            'title':_('Modif Profil'),
            'year':datetime.now().year,
            'form': form,
        })    