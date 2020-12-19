from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from . import forms, models


# Create your views here.
class UsersRegisterView(CreateView):
    model = models.TestModel
    form_class = forms.UsersRegisterForm
    template_name = 'users/users_register.html'
    success_url = reverse_lazy('users:users_register_form_submitted')


class UsersRegisterFormSubmittedView(TemplateView):    
    template_name = 'users/users_register_form_submitted.html'