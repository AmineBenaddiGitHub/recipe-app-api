"""
Django command to wait for the DB to be available
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for the database"""

    def handle(self, *args, **kwargs):
        """Entrypoint for the command"""
        self.stdout.write('waiting for db ...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('db unavailable, waiting 1 sec ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('db available !'))
