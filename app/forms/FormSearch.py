from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from ..models import *
class SearchForm(forms.ModelForm):
    Categorie = forms.ModelChoiceField(queryset=(Categorie.objects.all()),
                                      widget=forms.Select(attrs={'class': 'form-control'})
                                      )
    Machine = forms.ModelChoiceField(queryset=(Machine.objects.all()),
      widget=forms.Select(attrs={'class': 'form-control'}))
    Materiaux = forms.ModelChoiceField(queryset=(Matiere.objects.all()),
      widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Projet
        fields = ('Categorie','Materiaux','Machine')
