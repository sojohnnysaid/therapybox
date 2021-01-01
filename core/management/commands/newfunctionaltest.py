import os

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from pathlib import Path
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'creates a new feature folder named [featurename] inside of [appname] with test files'

    def add_arguments(self, parser):
        parser.add_argument('functional_test_name', type=str, help='name of the functional test. Usually the title of a user story')

    def handle(self, *args, **options):
        try:
            functional_test_name = 'tests_functional_' + options['functional_test_name']
            
            file_exists = os.path.exists(f"core/tests_functional/{functional_test_name}.py")
            if file_exists:
                raise ValidationError('Test already exists!')

            project_apps = [app.verbose_name.lower() for app in apps.get_app_configs()]
            if 'core' not in project_apps:
                raise ValidationError('App not found. This command creates the test file into the app called "core." Did you create an app with that name yet?')

            # make folder if it doesn't exist yet (first functional test)
            os.makedirs(f"core/tests_functional", exist_ok=True)

            with open(f"core/management/commands/file_templates/functional/template_tests_functional.py", 'r') as file:
                template_text = file.read()
                
            with open(f"core/tests_functional/{functional_test_name}.py", 'w') as f:
                f.write(template_text)
            
            self.stdout.write(self.style.SUCCESS(f"📜 {options['functional_test_name']} has been created. 🎉 Happy testing! "))

        except (CommandError, OSError, ValidationError) as e:
            self.stdout.write(f"Can not create the test file you've specified! {e.message}")
