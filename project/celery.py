from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django applications.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    
app.conf.beat_schedule = {
    #Scheduler Name
    'print-message-five-mins': {
        # Task Name (Name Specified in Decorator)
        'task': "update_db_with_new_data",  
        # Schedule  5 mins which is 300sec    
        'schedule': 300.0,
    }} 