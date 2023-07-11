from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]