from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from app.models import Car, Photo
from .models import *

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


class UserSignin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def is_valid(self):
        super(UserSignin, self).is_valid()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        return True
                    else:
                        self._errors["username"] = ["User is not active"]
                        return False
                else:
                    print("okok")
                    self._errors["username"] = ["Invalid username or password"]
                    return False
            else:
                self._errors["username"] = ["User doesn't exists"]
                return False
        except:
            self._errors["username"] = ["Invalid username or password"]
            self._errors["password"] = ["Invalid username or password"]
            return False

    def save(self, request):
        username = self.cleaned_data.get('username')
        user = User.objects.get(username=username)
        login(request, user)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'location', 'image']