from django.db import migrations


def create_asignaturas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Area = apps.get_model('planificaciones', 'Area')

    # Areas
    lengua_literatura = Area.objects.get(name='Lengua y Literatura')
    matematica = Area.objects.get(name='Matemática')
    ciencias_naturales = Area.objects.get(name='Ciencias Naturales')
    ciencias_sociales = Area.objects.get(name='Ciencias Sociales')
    interdisciplinar = Area.objects.get(name='Interdisciplinar')

    # Asignaturas
    Asignatura.objects.bulk_create([
        Asignatura(
            name='Lengua y Literatura',
            area=lengua_literatura
        ),
        Asignatura(
            name='Matemática',
            area=matematica,
        ),
        Asignatura(
            name='Ciencias Naturales',
            area=ciencias_naturales,
        ),
        Asignatura(
            name='Química',
            area=ciencias_naturales,
        ),
        Asignatura(
            name='Biología',
            area=ciencias_naturales,
        ),
        Asignatura(
            name='Física',
            area=ciencias_naturales,
        ),
        Asignatura(
            name='Estudios Sociales',
            area=ciencias_sociales,
        ),
        Asignatura(
            name='Historia',
            area=ciencias_sociales,
        ),
        Asignatura(
            name='Filosofía',
            area=ciencias_sociales,
        ),
        Asignatura(
            name='Educación para la Ciudadanía',
            area=ciencias_sociales,
        ),
        Asignatura(
            name='Emprendimiento y Gestión',
            area=interdisciplinar,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0005_auto_20180727_1413'),
    ]

    operations = [
        migrations.RunPython(create_asignaturas,
                             reverse_code=migrations.RunPython.noop)
    ]
