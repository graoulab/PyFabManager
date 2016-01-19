from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from ..models import Machine
class ConfigSiteForm(forms.ModelForm):
    NomLab = forms.CharField(label=_("Nom du FabLab"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nom du FabLab"}))
    AdresseContact = forms.CharField(label=_("Adresse mail"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Adresse mail"}))
    Rue = forms.CharField(label=_("Rue"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Rue"}))
    ville = forms.CharField(label=_("Ville"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Ville"}))
    CodePostal = forms.CharField(label=_("Code Postal"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Code Postal"}))
    class Meta:
        model = Machine
        fields = ('NomLab', 'AdresseContact','Rue','ville','CodePostal')
