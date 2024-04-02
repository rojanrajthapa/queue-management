from celery import shared_task
from .management.commands.run_transactions import Command as RunTransactionsCommand


@shared_task
def run_transactions():
    command = RunTransactionsCommand()
    command.handle()
