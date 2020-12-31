import os

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
            project_apps = [app.verbose_name.lower() for app in apps.get_app_configs()]
            appname = options['appname']
            feature = options['featurename']
            
            if options['appname'] not in project_apps:
                raise ValidationError('the app you specified does not exist')

            # make folders if they don't exist yet (first feature)
            os.makedirs(f"{appname}/tests/{feature}", exist_ok=False)
            os.makedirs(f"{appname}/tests/{feature}/unit_tests", exist_ok=False)
            os.makedirs(f"{appname}/tests/{feature}/functional_tests", exist_ok=False)

            # read templates and save to variables to use later

            file_template_directory = 'core/management/commands/file_templates/'
            templates = os.listdir(file_template_directory)

            for template in templates:
                with open(f"core/management/commands/file_templates/{template}", 'r') as file:
                    template_text = file.read()
                with open(f"{appname}/tests/{feature}/unit_tests/{template.replace('template_', '')}", 'w') as f:
                    f.write(template_text)
            
             self.stdout.write(self.style.SUCCESS(f"📜 New suite of tests for {feature} has been created in {appname} app! 🎉 Happy testing!"))

        except CommandError as e:
            self.stdout.write(e)

        