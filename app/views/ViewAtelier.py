from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
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
def ListAtelier(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    nbelement = 10
    data = list(Atelier.objects.values().order_by('-id'))
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
            'app/ListAtelier.html',
            context =
            {
                'title':_('Liste Atelier'),
                'Type':'Atelier',
                'data':data,
                'year':datetime.now().year,
                'nb':paginator.page_range,
            })

def ViewAtelier(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    data = Atelier.objects.filter(id=NbPage)
    DejaInscrit = 0
    if request.user.is_authenticated : 
        DejaInscrit = len(data[0].UtilisateurInscrit.filter(user =request.user))
    return render(
            request,
            'app/DetailAtelier.html',
            context = 
            {
                'title':data[0].Titre,
                'data':data[0],
                'year':datetime.now().year,
                'nbPlace': (data[0].nBplace-data[0].PlaceReserver),
                'inscrit': data[0].UtilisateurInscrit.all(),
                'DejaInscrit': DejaInscrit
            })

@user_passes_test(lambda u: u.is_authenticated)
def InscriptionAtelier(request,Action=1):
    CurrentAtelier = Atelier.objects.filter(id=Action)[0]
    CurentUser = utilisateur.objects.filter(user = request.user.id)[0]
    CurrentAtelier.UtilisateurInscrit.add(CurentUser)
    return HttpResponseRedirect('/ListAtelier/')

@user_passes_test(lambda u: u.is_authenticated)
def DesinscriptionAtelier(request,Action=1):
    CurrentAtelier = Atelier.objects.filter(id=Action)[0]
    CurentUser = utilisateur.objects.filter(user = request.user.id)[0]
    CurrentAtelier.UtilisateurInscrit.remove(CurentUser)
    return HttpResponseRedirect('/ListAtelier/')
    