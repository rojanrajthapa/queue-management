# task3/urls.py

from django.urls import path
from task3 import views

urlpatterns = [
    path('trigger-celery-task/', views.trigger_celery_task, name='trigger_celery_task'),
    # Other URL patterns for your app
]
