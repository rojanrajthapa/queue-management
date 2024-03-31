from celery import shared_task
from .models import Transaction, User

@shared_task
def deposit(user_id, amount):
    user = User.objects.get(pk=user_id)
    user.balance += amount
    user.save()

@shared_task
def withdraw(user_id, amount):
    user = User.objects.get(pk=user_id)
    if user.balance >= amount:
        user.balance -= amount
        user.save()

@shared_task
def transfer(from_user_id, to_user_id, amount):
    withdraw.delay(from_user_id, amount)
    deposit.delay(to_user_id, amount)

@shared_task
def save_transaction(type, amount, sender_id, receiver_id):
    Transaction.objects.create(
        type=type,
        amount=amount,
        sender_id=User.objects.get(pk=sender_id),
        receiver_id=User.objects.get(pk=receiver_id),
    )
    