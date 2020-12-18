from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.db.models import QuerySet
from django.db import models

class test(models.Model):
    pass

# Create your views here.
class UsersRegisterView(CreateView):
    fields = []
    model = test
    template_name = 'users/users_register.html'
    