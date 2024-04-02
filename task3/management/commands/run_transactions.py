import logging
from django.core.management.base import BaseCommand
from django.db import transaction
from random import choice, randint
from task3.models import User
from task3.transaction_utils import deposit, save_transaction, withdraw, transfer

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Runs 50 asynchronous transactions (deposits, withdrawals, transfers)'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                for _ in range(50):
                    operation = choice(['deposit', 'withdraw', 'transfer'])
                    if operation == 'deposit':
                        user = choice(User.objects.all())
                        amount = randint(100, 1000)
                        deposit(user.id, amount)
                        save_transaction('DEPOSIT', amount, user.id, user.id)
                    elif operation == 'withdraw':
                        user = choice(User.objects.all())
                        amount = randint(50, 500)
                        withdraw(user.id, amount)
                        save_transaction('WITHDRAW', amount, user.id, user.id)
                    elif operation == 'transfer':
                        from_user = choice(User.objects.all())
                        to_user = choice(User.objects.exclude(pk=from_user.pk))
                        amount = randint(100, 1000)
                        transfer(from_user.id, to_user.id, amount)
                        save_transaction('TRANSFER', amount, from_user.id, to_user.id)
            logger.info('All transactions completed successfully.')
        except Exception as e:
            logger.error(f'Error occurred: {e}')
            with transaction.atomic():
                transaction.set_rollback(True)
                logger.info('Transactions rolled back due to error.')
