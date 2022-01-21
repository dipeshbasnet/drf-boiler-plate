import os

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'renames the project'

    def run_from_argv(self, argv):
        print('Starts ... ... ')
        old_project_name = os.path.basename(settings.BASE_DIR)
        if old_project_name == argv[2]:
            print('There is no change in the project name')
        else:
            os.rename(settings.BASE_DIR, os.path.join(os.path.join(os.path.dirname(settings.BASE_DIR), argv[2])))
            print('Project name is changed from {} to {}'.format(old_project_name, argv[2]))
        print('Finished ... ... ')
