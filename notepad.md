# stock
from django.test import Client
from django.shortcuts import reverse

from users import views, forms, models
#




response = Client().get(reverse('users:users_register'))

# John goes to his email...
>       email = mail.outbox[0]

Once the form is submitted:
If the fields are vaild:
the user will be created
the user will be set active=false




steps required to create a custom user model:
1. update app settings

we need to test that our user model is our custom user model

from django.conf import settings
settings.AUTH_USER_MODEL == 'users.CustomUser'
TODO read about spiking de-spiking and create branch
to mess with custom user models


