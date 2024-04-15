# task3/views.py

from django.http import JsonResponse

from task3.run_transactions import run_transactions


def trigger_celery_task(request):

    run_transactions.delay()
    return JsonResponse({'message': 'Celery task triggered successfully'})
