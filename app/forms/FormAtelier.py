from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models import Atelier
from ..fct import *
from datetime import date
from django.conf import settings
def validate_datetime(data, **kwargs):
    """Validate that /data/ is of type datetime.
  
    Used to validate DateTime form fields, to ensure that user select
    a valid date, thus a date that can be converted to a datetime
    obj. Example of invalid date is 'Sept 31 2012'.
  
    """
  
    if not isinstance(data, datetime.datetime):
        raise 
    return data
class AtelierForm(forms.ModelForm):
  Titre  = forms.CharField(label=_("Nom de la machine"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nom de l'atelier"}))
  Cout = forms.DecimalField(label=_("Cout"),
                                required=True,
                               widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': "Cout"}))
  CoutAdh = forms.DecimalField(label=_("Cout adherent"),
                                required=True,
                               widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': "adherent"}))
  NombredePlace = forms.DecimalField(label=_("Nombre de place"),
                                required=True,
                               widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': "Nombre de place"}))
  Image = forms.ImageField(required=False,
        label='Choisir une image'
    )
  Date = forms.DateTimeField(initial=date.today().replace(day=1), 
                                 widget=forms.widgets.DateTimeInput())
  Descritpion = forms.CharField(label=_("Descritpion"),
                                required=True,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': "Descritpion"}))
  class Meta:
    model = Atelier
    fields = ('Titre','Cout','CoutAdh','Image','Descritpion','Date','NombredePlace')
