import os
import errno

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from pathlib import Path
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'creates a new feature folder named [featurename] inside of [appname] with test files'

    def add_arguments(self, parser):
        parser.add_argument('featurename', type=str, help='name of the feature folder')
        parser.add_argument('appname', type=str, help='name of app where folder will be created')

    def handle(self, *args, **options):
        try:
            appname = options['appname']
            feature = 'test_' + options['featurename']
            
            project_apps = [app.verbose_name.lower() for app in apps.get_app_configs()]
            if options['appname'] not in project_apps:
                raise ValidationError('the app you specified does not exist')

            # make folders if they don't exist yet (first feature)
            os.makedirs(f"{appname}/tests/{feature}", exist_ok=False)
            os.makedirs(f"{appname}/tests/{feature}/tests_unit", exist_ok=False)
            os.makedirs(f"{appname}/tests/{feature}/notes", exist_ok=False)

            app_directory = 'administration'

            # create unit test files from templates
            file_template_directory = f'{app_directory}/management/commands/file_templates/unit'
            templates = os.listdir(file_template_directory)

            for template in templates:
                with open(f"{file_template_directory}/{template}", 'r') as file:
                    template_text = file.read()
                with open(f"{appname}/tests/{feature}/tests_unit/{template.replace('template_', '')}", 'w') as f:
                    f.write(template_text)

            # create functional test files from templates
            file_template_directory = f'{app_directory}/management/commands/file_templates/functional'
            templates = os.listdir(file_template_directory)

            for template in templates:
                with open(f"{file_template_directory}/{template}", 'r') as file:
                    template_text = file.read()
                with open(f"{appname}/tests/{feature}/{template.replace('template_', '')}", 'w') as f:
                    f.write(template_text)

            
            # create notes from templates
            file_template_directory = f'{app_directory}/management/commands/file_templates/notes'
            templates = os.listdir(file_template_directory)

            for template in templates:
                with open(f"{file_template_directory}/{template}", 'r') as file:
                    template_text = file.read()
                with open(f"{appname}/tests/{feature}/notes/{template.replace('template_', '')}", 'w') as f:
                    f.write(template_text)

            
            # create __init__.py files - allows us to use the same test file names in different folders
            # file_exists = os.path.exists(f"{appname}/tests/__init__.py")
            # if not file_exists:
            #     with open(f"{appname}/tests/__init__.py", 'w') as f:
            #         f.write('')
            
            file_exists = os.path.exists(f"{appname}/tests/{feature}/__init__.py")
            if not file_exists:
                with open(f"{appname}/tests/{feature}/__init__.py", 'w') as f:
                    f.write('')

            file_exists = os.path.exists(f"{appname}/tests/{feature}/tests_unit/__init__.py")
            if not file_exists:
                with open(f"{appname}/tests/{feature}/tests_unit/__init__.py", 'w') as f:
                    f.write('')

            
            self.stdout.write(self.style.SUCCESS(f"📜 New suite of tests for {feature} has been created in {appname} app! 🎉 Happy testing!"))

        except OSError as e:
            if e.strerror:
                self.stdout.write(f"Oops! This test suite has already been created! Error message: {e.strerror}")
            else:
                self.stdout.write(e)