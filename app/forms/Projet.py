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
  Categorie = forms.ModelChoiceField(queryset=(Categorie.objects.values_list('Nom', flat=True)),
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Materiaux'
                                      )
  Licence = forms.ModelChoiceField(queryset=(Licences.objects.values_list('Nom', flat=True)),
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Materiaux'
                                      )
  Machine = forms.ModelChoiceField(queryset=(Machine.objects.values_list('Titre', flat=True)),
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Materiaux'
                                      )
  Materiaux = forms.ModelChoiceField(queryset=(Matiere.objects.values_list('Nom', flat=True)),
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Materiaux'
                                      )
  Contenue = forms.CharField(label=_("Descritpion"),
                                required=True,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': "Descritpion"}))
  class Meta:
    model = Projet
    fields = ('titre','fichier','Categorie','Image','Licence','Machine','Materiaux','Contenue')
