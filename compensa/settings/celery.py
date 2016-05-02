# -*- coding: utf-8 -*-
from __future__ import absolute_import

import djcelery
#djcelery.setup_loader()

#BROKER_URL = "amqp://guest:guest@localhost:5672//"
#CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'

# CELERY CONFIG
BROKER_URL = 'redis://localhost:6379'
# Results to Redis
#CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# Results to Django DB
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

CELERY_SEND_EVENTS = True
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'