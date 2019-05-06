from django.db import migrations


def create_cursos(apps, schema_editor):
    Curso = apps.get_model('planificaciones', 'Curso')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    # Cursos
    Curso.objects.bulk_create([
        Curso(name='1° EGB', subnivel=preparatoria),
        Curso(name='2° EGB', subnivel=elemental),
        Curso(name='3° EGB', subnivel=elemental),
        Curso(name='4° EGB', subnivel=elemental),
        Curso(name='5° EGB', subnivel=media),
        Curso(name='6° EGB', subnivel=media),
        Curso(name='7° EGB', subnivel=media),
        Curso(name='8° EGB', subnivel=superior),
        Curso(name='9° EGB', subnivel=superior),
        Curso(name='10° EGB', subnivel=superior),
        Curso(name='1° BGU', subnivel=bachillerato),
        Curso(name='2° BGU', subnivel=bachillerato),
        Curso(name='3° BGU', subnivel=bachillerato),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0004_auto_20180727_1411'),
    ]

    operations = [
        migrations.RunPython(
            create_cursos, reverse_code=migrations.RunPython.noop)
    ]
