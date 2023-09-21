from celery import Celery 
from celery.schedules import crontab

BROKER_URL ='amqp://guest:guest@localhost:5672/'

CELERYBEAT_SCHEDULE = {
    'every-minute':{
        'task':'tasks.add',
        'schedule':crontab(minute='*/1'),
        'args':(25,36),
    },
}