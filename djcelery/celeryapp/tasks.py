from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task
def sub(x, y):
    sleep(10)
    return x - y


@shared_task
def clear_session_cache(id):
    print(f"Session Cache cleared: {id}")
    return id



@shared_task
def clear_redis_data(key):
    print(f"Redis Cache cleared: {key}")
    return key

@shared_task
def clear_rabbitmq_data(key):
    print(f"RabbitMq data cleared: {key}")
    return key

#create schedule every 30 second
schedule , create = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)

#schedule the periodiv task pragrammatically
PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='celeryapp.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(["helloRedis"]) #pass the arguments to the task as json-encoded list
)

