from django.forms import ModelForm, widgets

from . import models

class UsersRegisterForm(ModelForm):
    class Meta:
        model = models.TestModel
        fields = ['first_name', 'email'] # model fields you want in the form go in here
        widgets = {
            'first_name': widgets.TextInput(attrs={'id': 'user-registration-form-first-name-field'})
        } #needs test!