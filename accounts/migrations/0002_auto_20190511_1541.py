from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import migrations

User = get_user_model()


def create_superuser(apps, schema_editor):
    email = settings.SUPERUSER_EMAIL
    password = settings.SUPERUSER_PASSWORD
    first_name = settings.SUPERUSER_FIRSTNAME
    last_name = settings.SUPERUSER_LASTNAME
    User.objects.create_superuser(
        email,
        password,
        first_name=first_name,
        last_name=last_name
    )


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser,
                             reverse_code=migrations.RunPython.noop)
    ]
