# stock
from django.test import Client
from django.shortcuts import reverse

from users import views, forms, models
#




response = Client().get(reverse('users:users_register'))
alias djshell='python manage.py shell -c "import code;from rich import pretty;pretty.install();from rich import inspect;code.interact(local=locals())"'