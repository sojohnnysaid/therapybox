import os
import errno
from halo import Halo

from django.core.management.base import BaseCommand
from django.apps import apps
from pathlib import Path
from django.contrib.auth import get_user_model
from factories.factories import *

class Command(BaseCommand):
    help = 'creates dummy data'

    def handle(self, *args, **options):
        spinner = Halo(text='Loading', spinner='dots')
        spinner.start()
        TherapyBoxUserFactory.create_batch(12)
        TherapyBoxFactory.create_batch(12)
        spinner.stop()
        print('🔥 Dummy data added!')
