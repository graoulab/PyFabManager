from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from ..models import Config
class MachineForm(forms.ModelForm):
  Titre  = forms.CharField(label=_("Nom de la machine"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nom de la machine"}))
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
  Image = forms.ImageField(required=False,
        label='Choisir une image'
    )
  Descritpion = forms.CharField(label=_("Descritpion"),
                                required=True,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': "Descritpion"}))
  class Meta:
    model = Config
    fields = ('Titre','Cout','CoutAdh','Image','Descritpion')
