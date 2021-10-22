from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

Numerics = ['0', '1', '2', '3', '4', '5', '6', '7', '9']

def name_validation(name):
    if name[0] in Numerics: raise forms.ValidationError("Names' first characters can't be Numeric.")

def email_validation(email):
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("This email is aleady in use.")

class UserSignup(UserCreationForm):
    email = forms.EmailField(validators=[email_validation])
    username = forms.CharField(validators=[name_validation])
    first_name = forms.CharField(required=True, validators=[name_validation])
    last_name = forms.CharField(required=True, validators=[name_validation])
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserSignin(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        
