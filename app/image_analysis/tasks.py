from celery import shared_task


@shared_task
def submit_image_analysis():
    # Your event logic goes here
    print("Event triggered!")
    # You can perform more complex operations here
