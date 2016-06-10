# coding: utf-8 
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from ..models import Atelier
from datetime import date
from django import forms

class MailForm(forms.Form):
    Sujet = forms.CharField(label=_("Sujet"),
                                required=True,max_length=254,
                                widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Sujet"}))
    Descritpion = forms.CharField(label=_("Corp"),
                                required=True,
                                widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': "Corp"}))
    Rang = forms.ChoiceField(choices = list(settings.RANG ),
                                widget=forms.Select(attrs={'class': 'form-control'}))