from celery import shared_task


@shared_task
def my_event_task():
    # Your event logic goes here
    print("Event triggered!")
    # You can perform more complex operations here
