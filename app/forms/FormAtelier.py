from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models import Atelier
from ..fct import *
from datetime import date
from django.conf import settings
from django.conf import settings
class AtelierForm(forms.ModelForm):
  Titre  = forms.CharField(label=_("Nom de la machine"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nom de l'atelier"}))
  prix = forms.DecimalField(label=_("Cout"),
                                required=True,
                               widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': "Cout"}))
  prixAdh = forms.DecimalField(label=_("Cout adherent"),
                                required=True,
                               widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': "adherent"}))
  Rang = forms.ChoiceField(choices = list(settings.RANG ),
                               widget=forms.Select(attrs={'class': 'form-control'}))

  nBplace = forms.DecimalField(label=_("Nombre de place"),
                                required=True,
                               widget=forms.NumberInput({
                                   'class': 'form-control',
                                   'placeholder': "Nombre de place"}))
  Image = forms.ImageField(required=False,
        label='Choisir une image',widget=forms.FileInput({'class':'file'})
    )
  date = forms.DateTimeField(initial=date.today().replace(day=1), 
                                 widget=forms.widgets.DateTimeInput())
  Descritpion = forms.CharField(label=_("Descritpion"),
                                required=True,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': "Descritpion"}))
  class Meta:
    model = Atelier
    fields = ('Titre','Rang','prix','prixAdh','Image','Descritpion','date','nBplace')
