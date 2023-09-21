from celery import Celery 
import datetime

celery = Celery('tasks')
celery.config_from_object('celeryconfig')

@celery.task
def add(x,y):
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%H:%M:%S")
    res = f"New Run at time : {formatted_time}"
    return res

