from django.db import migrations


def create_niveles(apps, schema_editor):
    Nivel = apps.get_model('planificaciones', 'Nivel')
    Nivel.objects.bulk_create([
        Nivel(name="Educación General Básica"),
        Nivel(name="Bachillerato General Unificado"),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0002_auto_20180727_1409'),
    ]

    operations = [
        migrations.RunPython(create_niveles)
    ]
