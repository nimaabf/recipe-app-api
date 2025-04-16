# django command to wait for database to be available

from django.core.management.base import BaseCommand

import time

from psycopg2 import OperationalError as psycopg2_error
from django.db.utils import OperationalError


class Command(BaseCommand):
    # command for wait for db

    def handle(self, *args, **options):
        # Command Entery Point
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2_error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
