import os
import errno

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from pathlib import Path
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'creates a super user admin@gmail.com with the password "password"'

    def handle(self, *args, **options):
        if get_user_model().objects.filter(email='admin@gmail.com').exists():
            print('Super user already created!')
        else:
            get_user_model().objects.create_superuser(email='admin@gmail.com', password='password')
            print('Super user created!')