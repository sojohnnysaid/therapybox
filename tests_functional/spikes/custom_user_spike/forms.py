from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models

class UsersRegisterForm(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = ['email', 'first_name', 'password1', 'password2'] # model fields you want in the form go in here
        # widgets = {
        #     'first_name': widgets.TextInput(attrs={
        #         'placeholder': 'first name'
        #     }),
        #     'email': widgets.EmailInput(attrs={
        #         'placeholder': 'email'
        #     })
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # this does the widget code above on each field
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'