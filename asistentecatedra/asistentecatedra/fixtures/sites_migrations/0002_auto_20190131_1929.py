# Generated by Django 2.0.7 on 2019-02-01 00:29

from django.db import migrations
from django.contrib.sites.models import Site
from django.conf import settings


def create_site(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    Site.objects.all().delete()

    # Register SITE_ID = 1
    Site.objects.create(
        domain=settings.DOMAIN,
        name='Asistente de Cátedra'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_site,
                             reverse_code=migrations.RunPython.noop)
    ]
