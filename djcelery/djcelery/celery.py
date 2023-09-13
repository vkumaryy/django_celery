import os

from celery import Celery
from time import sleep
from datetime import timedelta
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings')

app = Celery('djcelery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

@app.task(name="addition_task")
def add(x, y):
    return x + y

##Method 2
# app.conf.beat_schedule = {
#     'every-10-seconds':{
#         'task':'celeryapp.tasks.clear_session_cache',
#         'schedule':10,
#         'args':('111111',)
#     }
# #     #Add more periodic task as needde
# }

#using timedelta
# app.conf.beat_schedule = {
#     'every-10-seconds':{
#         'task':'celeryapp.tasks.clear_session_cache',
#         'schedule':timedelta(seconds=10),
#         'args':('111111',)
#     }
# #     #Add more periodic task as needde
# }

# using crontab
app.conf.beat_schedule = {
    'every-10-seconds':{
        'task':'celeryapp.tasks.clear_session_cache',
        'schedule':crontab(minute='*/1'),
        'args':('111111',)
    }
#     #Add more periodic task as needde
}