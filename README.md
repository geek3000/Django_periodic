# Sample periodic async task for a django application

Follow this [tutorial](https://github.com/geek3000/async_task_django) to create a Django app and configure celery and redis-server


## Create a periodic task
First import package (Add those lines in [task.py]() file
```python
from celery.decorators import periodic_task
from datetime import timedelta
```
After create the periodic task function (In [task.py]())
```python
@periodic_task(run_every=timedelta(minutes=1))
def add_periodic():
    r=add(7, 7)
    print(r)
```
Go to [setting.py]() file configure timezone
```python
timezone = 'UTC'
```
## Run Time
```bash
redis-server C:/Python36/scripts/redis.conf
```
Then launch worker
```bash
python manage.py celery -A async  worker -l info
```
Finally beat shedule
```bash
python manage.py celery -A async beat -l info
```
## Learn more
[Tutorial1](https://djangopy.org/how-to/handle-asynchronous-tasks-with-celery-and-django#periodic-tasks)
[Tutorial1]([Tutorial1](https://djangopy.org/how-to/handle-asynchronous-tasks-with-celery-and-django#periodic-tasks)
)
