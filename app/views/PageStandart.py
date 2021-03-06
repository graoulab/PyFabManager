# coding: utf-8 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest , HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from ..forms.register import UserCreateForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from django import template
from ..models import *
from ..fct import *
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
            'LastArticle':Article.objects.all().order_by('-id')[:3],
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
                password = form.cleaned_data['password1'],is_superuser = superuser,is_staff=superuser,
                first_name = form.cleaned_data['Nom'] , last_name = form.cleaned_data['Prenom'])
            user.save()
            PhoneNumber = form.cleaned_data['PhoneNumber']
            p = utilisateur(PhoneNumber=PhoneNumber,user =user)
            p.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            messages.add_message(request, messages.INFO, (_("Merci pour votre inscription ")+form.cleaned_data['username']))
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
            'NewsLetter' : User[0].NewsLetter,
            'year':datetime.now().year,
            'Projet' : projet,
            'Evenement':Evenement,
        }
    )

@user_passes_test(lambda u: u.is_authenticated)
def EditNewsLetter(request):
    EditUser = utilisateur.objects.filter(user = request.user.id)[0]
    EditUser.NewsLetter = not(EditUser.NewsLetter)
    EditUser.save()
    return HttpResponseRedirect(reverse('Profil'))
   