from django.db.models.base import Model
from django.forms import ModelForm

from . import models

class UsersRegisterForm(ModelForm):
    class Meta:
        model = models.TestModel
        fields = ['first_name', 'email'] # model fields you want in the form go in here