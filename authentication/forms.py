from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from authentication.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=256, widget=forms.EmailInput)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
