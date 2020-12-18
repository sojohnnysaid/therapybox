from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse
from django.db import models


class test(models.Model):
    pass

# Create your views here.
class UsersRegisterView(CreateView):
    fields = []
    model = test
    template_name = 'users/users_register.html'
    