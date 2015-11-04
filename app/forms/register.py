from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'username'}))
    email = forms.EmailField(required=True,max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'email'}))
    password1 = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    password2 = password1
    
    PhoneNumber = forms.CharField(required=True,max_length=15,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'PhoneNumber'}))