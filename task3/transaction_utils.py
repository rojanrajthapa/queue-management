from celery import shared_task
from django.db import transaction
from .models import Transaction, User

@shared_task
def deposit(user_id, amount):
    try:
        with transaction.atomic():
            user = User.objects.get(pk=user_id)
            user.balance += amount
            user.save()
    except Exception as e:
        with transaction.atomic():
            transaction.set_rollback(True)

@shared_task
def withdraw(user_id, amount):
    try:
        with transaction.atomic():
            user = User.objects.get(pk=user_id)
            if user.balance >= amount:
                user.balance -= amount
                user.save()
            else:
                raise ValueError("Insufficient balance")
    except Exception as e:
        with transaction.atomic():
            transaction.set_rollback(True)

@shared_task
def transfer(from_user_id, to_user_id, amount):
    try:
        with transaction.atomic():
            from_user = User.objects.get(pk=from_user_id)
            to_user = User.objects.get(pk=to_user_id)
            if from_user.balance >= amount:
                from_user.balance -= amount
                to_user.balance += amount
                from_user.save()
                to_user.save()
            else:
                raise ValueError("Insufficient balance")
    except Exception as e:
        with transaction.atomic():
            transaction.set_rollback(True)

@shared_task
def save_transaction(type, amount, sender_id, receiver_id):
    try:
        with transaction.atomic():
            sender = User.objects.get(pk=sender_id)
            receiver = User.objects.get(pk=receiver_id)
            Transaction.objects.create(
                type=type,
                amount=amount,
                sender_id=sender,
                receiver_id=receiver,
            )
    except Exception as e:
        with transaction.atomic():
            transaction.set_rollback(True)
