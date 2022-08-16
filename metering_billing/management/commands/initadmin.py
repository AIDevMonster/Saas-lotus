from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from metering_billing.models import User, Organization, APIToken
from django.core.management import call_command
from dotenv import load_dotenv
from django.db import connection
import os

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):

        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not User.objects.filter(username=username).exists():
            print("Creating account for %s (%s)" % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )

            org = Organization.objects.create(company_name="Lotus Default")
            org.save()

            org.users.add(admin)
        else:
            print("Admin account has already been initialized.")
