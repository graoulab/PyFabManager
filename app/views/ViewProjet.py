from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django import template
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..forms.register import UserCreateForm
from ..forms.Config import ConfigSiteForm
from ..forms.Projet import *
from ..models import *
from ..fct import *

def ListProjet(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    nbelement = 10
    data = list(Projet.objects.values().order_by('-id'))
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
            'app/ListProjet.html',
            context =
            {
                'title':_('Liste Projet'),
                'Type':'Projet',
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
            NewMachine = ProjetForm(Titre = form.cleaned_data['Titre'],Image = form.cleaned_data['Image'],
                Descritpion = form.cleaned_data['Descritpion'],Cout= form.cleaned_data['Cout'])
            NewMachine.save()
            return HttpResponseRedirect('/Admin/')

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