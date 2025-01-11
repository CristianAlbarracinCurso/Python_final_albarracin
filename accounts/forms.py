# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales que quieras agregar pueden ir aquí
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'avatar', 'biography', 'link', 'birthday']
