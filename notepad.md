# stock
from django.test import Client
from django.shortcuts import reverse

from users import views, forms, models
#




response = Client().get(reverse('users:users_register'))