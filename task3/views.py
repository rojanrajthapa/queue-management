# task3/views.py

from django.http import JsonResponse
from task3.tasks import run_transactions

def trigger_celery_task(request):
    # Trigger the Celery task asynchronously
    run_transactions.delay()
    return JsonResponse({'message': 'Celery task triggered successfully'})
