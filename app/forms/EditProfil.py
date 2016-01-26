from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ..models import utilisateur
class EditProfilForm(forms.ModelForm):
    first_name = forms.CharField(label=_("Nom"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Nom"}))
    last_name = forms.CharField(label=_("Prenom"),
                                required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': "Prenom"}))
    email = forms.EmailField(required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'email'}))
    password1 = forms.CharField(label=_("Mot de passe"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Mot de passe'}),required=False)
    password2 = password1
    PhoneNumber = forms.CharField(label=_("Numéro de telephone"),
                                required=True,max_length=15,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Numéro de telephone'}))
    NewsLetter = forms.BooleanField(label="Recevoir la newsletter",widget=forms.CheckboxInput({
                                   'class': 'form-control',
                                   } ) ) 
    class Meta:
      model = utilisateur
      fields = ('first_name','last_name','email','password1','password2','PhoneNumber','NewsLetter')                                   