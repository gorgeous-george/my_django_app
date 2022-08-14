import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# Celery beat configuration
app.conf.beat_schedule = {
    'parse_5_quotes_every_odd_hour': {
        'task': 'test_celery.tasks.parse_5_quotes',
        'schedule': crontab(minute=0, hour="1-23/2"),
    },
}


app.conf.timezone = 'Europe/Kiev'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
