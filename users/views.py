from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import models

from .models import test


# Create your views here.
class UsersRegisterView(CreateView):
    fields = []
    model = test
    template_name = 'users/users_register.html'
    success_url = reverse_lazy('users_register_form_submitted')



class UsersRegisterFormSubmittedView(TemplateView):
    template_name = 'users/users_register_form_submitted.html'