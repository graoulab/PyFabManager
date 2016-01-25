from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from ..models import *
class ProjetForm(forms.ModelForm):
  titre  = forms.CharField(label=_("Nom de la machine"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nom de la machine"})
                               )
  Image = forms.ImageField(required=False,
        label='Choisir une image'
    )
  fichier = forms.FileField(required=False,
        label='Choisir un Fichier'
    )
  Categorie = forms.ModelChoiceField(queryset=(Categorie.objects.all()),
                                      widget=forms.Select(attrs={'class': 'form-control'})
                                      )
  Licence = forms.ModelChoiceField(queryset=(Licences.objects.all()),
                                      widget=forms.Select(attrs={'class': 'form-control'})
                                      )
  Machine = forms.ModelMultipleChoiceField(queryset=(Machine.objects.all()),)
  Materiaux = forms.ModelMultipleChoiceField(queryset=(Matiere.objects.all()),)
  Contenue = forms.CharField(label=_("Descritpion"),
                                required=True,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': "Descritpion"}))
  class Meta:
    model = Projet
    fields = ('titre','fichier','Categorie','Image','Licence','Machine','Materiaux','Contenue')
