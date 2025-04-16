# django command to wait for database to be available

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # command for wait for db

    def handle(self, *args, **options):
        pass
