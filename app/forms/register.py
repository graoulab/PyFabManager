from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models.autre import TypeAdherent
class UserCreateForm(UserCreationForm):
    username = forms.CharField(label=_("Nome D'utilisateur"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nome D'utilisateur"}))
    email = forms.EmailField(required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'email'}))
    password1 = forms.CharField(label=_("Mot de passe"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Mot de passe'}))
    password2 = password1
    
    UserType = forms.ModelChoiceField(queryset=(TypeAdherent.objects.values_list('Nom', flat=True)),
                                           widget=forms.Select(attrs={'class': 'form-control'}), label='Type Membre')
    PhoneNumber = forms.CharField(label=_("Numéro de telephone"),
                                required=True,max_length=15,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Numéro de telephone'}))
                                   
