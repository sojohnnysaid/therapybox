from django.core.management.base import BaseCommand
 
import subprocess
from sys import stdout, stdin, stderr
import time, os, signal
 
 
class Command(BaseCommand):
    help = 'Run all commands'
    commands = [
        'python manage.py migrate',
        'python manage.py addsuperuser',
        'python manage.py dummydata',
    ]
 
    def handle(self, *args, **options):
        for command in self.commands:
            words = command.split()
            subprocess.run([words[0], words[1], words[2]])