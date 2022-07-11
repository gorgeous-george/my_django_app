from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Deletes user(s) by id. Superuser cannot be deleted.'

    def add_arguments(self, parser):
        parser.add_argument('user_ids',
                            nargs='+',
                            type=int,
                            help='list of user_ids to be deleted')

    def handle(self, *args, **options):
        user_ids: object = options['user_ids']
        for user_id in user_ids:
            if User.objects.get(id=user_id).is_superuser:
                raise CommandError(f'Superuser (id = {user_id}) cannot be deleted')
        User.objects.filter(id__in=user_ids).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted users with the following IDs:' " %s " % user_ids))
