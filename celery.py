import os
from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'callslack.settings')

app = Celery('callslack')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_slack_message_every_six_hours': {
        'task': 'core.tasks.send_slack_message',
        'schedule': crontab(hour='*/6'),  # Run every 6 hours
    },
}
