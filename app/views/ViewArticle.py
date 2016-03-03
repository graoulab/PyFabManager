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
from datetime import datetime
from django import template
from ..models import *
from ..fct import *

def ListArticle(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    nbelement = 10
    if request.user.is_authenticated() :
        data = list(Article.objects.filter(Rang=utilisateur.objects.filter(user = request.user.id)[0].Rang).order_by('-id'))
    else : 
        data = list(Article.objects.filter(Rang=0).order_by('-id'))
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
            'app/ListArticle.html',
            context =
            {
                'title':_('Liste Article'),
                'Type':'Atelier',
                'data':data,
                'year':datetime.now().year,
                'nb':paginator.page_range,
            })

def ViewArticle(request, NbPage=1):
    """Renders the view page.
    list of 3d page and possibility to tree by categorie
    """
    assert isinstance(request, HttpRequest)
    data = Article.objects.filter(id=NbPage)
    return render(
            request,
            'app/DetailArticle.html',
            context = 
            {
                'title':data[0].Titre,
                'data':data[0],
                'year':datetime.now().year,
            })
