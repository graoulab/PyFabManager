from django.shortcuts import render
from django.http import HttpRequest , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django import template
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..forms.register import UserCreateForm
from ..forms.Config import ConfigSiteForm
from ..forms.Machine import MachineForm
from ..models import *
from ..fct import *
def ListMachine(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    nbelement = 10
    data = list(Machine.objects.values().order_by('-id'))
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
            'app/ListMachine.html',
            context =
            {
                'title':'Liste machine',
                'data':data,
                'Type':'Machine',
                'year':datetime.now().year,
                'nb':paginator.page_range,
            })
        
def ViewMachine(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    data = Machine.objects.filter(id=NbPage)
    return render(
            request,
            'app/DetailMachine.html',
            context = 
            {
                'title':data[0].Titre,
                'data':data[0],
                'year':datetime.now().year,
            })
        