from django.db import migrations


def create_areas(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    Area.objects.bulk_create([
        Area(name="Lengua y Literatura"),
        Area(name="Matemática"),
        Area(name="Ciencias Naturales"),
        Area(name="Ciencias Sociales"),
        Area(name="Interdisciplinar"),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_areas, reverse_code=migrations.RunPython.noop)
    ]
