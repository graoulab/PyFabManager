"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from datetime import datetime
from .forms.register import UserCreateForm
from .models import *
def home(request):
    """Renders the home page."""
    LastProjet = Projet.objects.all().last()
    LastAtelier = Atelier.objects.all().last()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context = 
        {
            'LastProject': LastProjet,
            'LastEvent': LastAtelier,
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
            'title':'Contact',
            'message':'Your contact page.',
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
            'message':'Your application description page.',
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
            user = User(username= form.cleaned_data['username'],email= form.cleaned_data['email'],password = form.cleaned_data['password1'],
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