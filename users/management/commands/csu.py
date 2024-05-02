import os
from django.core.management import BaseCommand
from dotenv import load_dotenv
from config.settings import BASE_DIR
from users.models import User

dotenv_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
            first_name='Admin',
            last_name='Roots',
            is_staff=True,
            is_superuser=True
        )
        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()
