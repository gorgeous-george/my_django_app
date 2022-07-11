from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Creates fake user(s)'

    def add_arguments(self, parser):
        parser.add_argument('number',
                            nargs=1,
                            type=int,
                            choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            help='number of users to be created')

    def handle(self, *args, **options):
        number: object = options['number'][0]
        fake = Faker()
        objs = []
        for _ in range(number):
            objs.append(User(username=fake.unique.first_name(),
                             email=fake.ascii_email(),
                             password=make_password(fake.unique.first_name(), salt=None, hasher='default')))
        User.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS('Successfully created' " %s " 'fake user(s)' % number))
