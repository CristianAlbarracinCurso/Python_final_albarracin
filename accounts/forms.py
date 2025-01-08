# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales que quieras agregar pueden ir aquí
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
