import logging
from celery import shared_task
from django.db import transaction
from random import choice

from task3.models import User
from task3.transaction_utils import deposit, save_transaction, withdraw


logger = logging.getLogger(__name__)

@shared_task
def run_transactions():
    try:
        with transaction.atomic():
            user = choice(User.objects.all())
            deposit(user.id, 1000)
            save_transaction('DEPOSIT', 1000, user.id, user.id)

            withdraw(user.id, 1000)
            save_transaction('WITHDRAW', 1000, user.id, user.id)

        logger.info('All transactions completed successfully.')
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        with transaction.atomic():
            transaction.set_rollback(True)
            logger.info('Transactions rolled back due to error.')
