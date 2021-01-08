import os
import errno

from django.core.management.base import BaseCommand
from django.apps import apps
from pathlib import Path
from django.contrib.auth import get_user_model
from factories.factories import TherapyBoxTemplateFactory, TherapyBoxUserFactory

class Command(BaseCommand):
    help = 'creates dummy data'

    def handle(self, *args, **options):
        TherapyBoxTemplateFactory.create_batch(10)
        TherapyBoxUserFactory.create_batch(10)
        print('Dummy data added!')