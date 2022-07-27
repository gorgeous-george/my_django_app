from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'fill db using prepared fixture.json'

    def handle(self, *args, **options):
        call_command('loaddata', 'fixture.json', app_label='aggregation')


