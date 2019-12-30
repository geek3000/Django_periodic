from celery import shared_task
from celery.decorators import periodic_task
from datetime import timedelta

@shared_task(name = "addNumbers")
def add(x, y):
    return x + y

@periodic_task(run_every=timedelta(minutes=1))
def scraper_example():
    result = add(2, 1)
    print(result)
