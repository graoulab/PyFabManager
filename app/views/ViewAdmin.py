from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest , HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from ..forms.register import UserCreateForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import logout
from ..forms.MailList import MailForm
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from django import template
from ..models import *
from ..fct import *

@user_passes_test(lambda u: u.is_superuser)
def EnvoieMail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data['Rang']
            Temp = utilisateur.objects.filter(NewsLetter = True , Rang = form.cleaned_data['Rang'])
            ListAdress = []
            for i in Temp :
                ListAdress.append(i.user.email)
            subject = form.cleaned_data['Sujet']
            from_email = settings.ADRESSECONTACT
            text_content =  ''
            msg = EmailMultiAlternatives(subject, text_content, from_email, ListAdress)
            msg.attach_alternative(form.cleaned_data['Descritpion'], "text/html")
            msg.send()
            return HttpResponseRedirect(reverse('home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MailForm()
    return render(
    request, 
    'admin/mail.html', 
    context = 
        {
            'title':_('Envoie Mail'),
            'year':datetime.now().year,
            'form': form,
        })
