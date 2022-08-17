import lorem, random

from django.core.management.base import BaseCommand

from test_celery.models import Author, Quote


class Command(BaseCommand):
    help = 'fill Quote model with some data'

    def handle(self, *args, **options):
        authors_id_list = Author.objects.all().values_list('id', flat=True)
        for _ in range(1000):
            Quote.objects.create(quote_text=lorem.sentence(), authors_id=random.choice(authors_id_list))

