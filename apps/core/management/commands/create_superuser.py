from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        USER = get_user_model()
        if not USER.objects.filter(is_superuser=True).exists():
            USER.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin"
            )
            self.stdout.write(self.style.SUCCESS('Admin user has created'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))
