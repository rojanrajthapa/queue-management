from django.db import models

from django.db import models

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
        ('TRANSFER', 'Transfer'),
    ]

    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_transactions')

    def __str__(self):
        return f"{self.type} - {self.amount}"
