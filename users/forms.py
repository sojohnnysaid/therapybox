from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse, redirect

from . import models

class UsersRegisterForm(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = ['email', 'first_name', 'password1', 'password2']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'