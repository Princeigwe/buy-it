import os
from celery import Celery

# applying default django settings to the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buy_it.settings')

app = Celery('buy_it')

# loading custom configuration settings in django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# auto discover asynchronous task
app.autodiscover_tasks()