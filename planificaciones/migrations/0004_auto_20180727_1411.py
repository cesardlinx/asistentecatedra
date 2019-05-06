from django.db import migrations


def create_subniveles(apps, schema_editor):
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    Nivel = apps.get_model('planificaciones', 'Nivel')

    # Niveles
    EGB = Nivel.objects.get(name='Educación General Básica')
    BGU = Nivel.objects.get(name='Bachillerato General Unificado')

    # Subniveles
    Subnivel.objects.bulk_create([
        Subnivel(name="Básica Preparatoria", nivel=EGB),
        Subnivel(name="Básica Elemental", nivel=EGB),
        Subnivel(name="Básica Media", nivel=EGB),
        Subnivel(name="Básica Superior", nivel=EGB),
        Subnivel(name="Bachillerato General Unificado", nivel=BGU)
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0003_auto_20180727_1411'),
    ]

    operations = [
        migrations.RunPython(
            create_subniveles, reverse_code=migrations.RunPython.noop)
    ]
