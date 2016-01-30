from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserCreateForm(UserCreationForm):
    Nom = forms.CharField(label=_("Nom"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _("Nom")}))
    Prenom = forms.CharField(label=_("Prenom"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _("Prenom")}))
    username = forms.CharField(label=_("Nom D'utilisateur"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _("Nom D'utilisateur")}))
    email = forms.EmailField(required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'email'}))
    password1 = forms.CharField(label=_("Mot de passe"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':_('Mot de passe')}),required=True)
    password2 = password1
    PhoneNumber = forms.CharField(label=_("Numéro de telephone"),
                                required=True,max_length=15,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Numéro de telephone'}))
    NewsLetter = forms.BooleanField(label=_("Recevoir la newsletter"),widget=forms.CheckboxInput({
                                   'class': 'form-control',
                                   } ) )
                                   
