from django.db import migrations


def create_unidades(apps, schema_editor):
    Unidad = apps.get_model('planificaciones', 'Unidad')
    Curso = apps.get_model('planificaciones', 'Curso')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')

    # Cursos
    segundo_egb = Curso.objects.get(pk=2)
    tercero_egb = Curso.objects.get(pk=3)
    cuarto_egb = Curso.objects.get(pk=4)
    quinto_egb = Curso.objects.get(pk=5)
    sexto_egb = Curso.objects.get(pk=6)
    septimo_egb = Curso.objects.get(pk=7)
    octavo_egb = Curso.objects.get(pk=8)
    noveno_egb = Curso.objects.get(pk=9)
    decimo_egb = Curso.objects.get(pk=10)
    primero_bgu = Curso.objects.get(pk=11)
    segundo_bgu = Curso.objects.get(pk=12)
    tercero_bgu = Curso.objects.get(pk=13)

    # Listas de cursos
    todos_cursos = [
        segundo_egb,
        tercero_egb,
        cuarto_egb,
        quinto_egb,
        sexto_egb,
        septimo_egb,
        octavo_egb,
        noveno_egb,
        decimo_egb,
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    ]
    cursos_egb = todos_cursos[:-3]
    cursos_bgu = todos_cursos[-3:]
    cursos_bgu2 = todos_cursos[-3:-1]
    cursos_elemental = todos_cursos[:3]
    cursos_elemental2 = todos_cursos[:2]
    cursos_medio_superior = todos_cursos[2:]

    # Asignaturas
    lengua_literatura = Asignatura.objects.get(
        name="Lengua y Literatura")
    matematica = Asignatura.objects.get(name="Matemática")
    ciencias_naturales = Asignatura.objects.get(
        name="Ciencias Naturales")
    biologia = Asignatura.objects.get(name="Biología")
    quimica = Asignatura.objects.get(name="Química")
    fisica = Asignatura.objects.get(name="Física")
    estudios_sociales = Asignatura.objects.get(
        name="Estudios Sociales")
    historia = Asignatura.objects.get(name="Historia")
    filosofia = Asignatura.objects.get(name="Filosofía")
    educacion_ciudadania = Asignatura.objects.get(
        name="Educación para la Ciudadanía")
    emprendimiento_gestion = Asignatura.objects.get(
        name="Emprendimiento y Gestión"
    )

    for unidad in range(1, 5):
        for curso in cursos_egb:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=lengua_literatura
            )

        for curso in cursos_elemental2:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=ciencias_naturales
            )

        for curso in cursos_bgu2:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=educacion_ciudadania
            )
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=emprendimiento_gestion
            )

    for unidad in range(1, 7):
        for curso in cursos_egb:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=matematica
            )

        for curso in cursos_medio_superior:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=ciencias_naturales
            )
        for curso in cursos_elemental:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=estudios_sociales
            )

        for curso in cursos_bgu2:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=filosofia
            )

        for curso in cursos_bgu:
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=lengua_literatura
            )
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=matematica
            )
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=historia
            )
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=biologia
            )
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=quimica
            )
            Unidad.objects.create(
                numero_unidad=unidad,
                curso=curso,
                asignatura=fisica
            )

    for unidad in range(1, 8):
        Unidad.objects.create(
            numero_unidad=unidad,
            curso=sexto_egb,
            asignatura=estudios_sociales
        )

    for unidad in range(1, 9):
        Unidad.objects.create(
            numero_unidad=unidad,
            curso=quinto_egb,
            asignatura=estudios_sociales
        )
        Unidad.objects.create(
            numero_unidad=unidad,
            curso=septimo_egb,
            asignatura=estudios_sociales
        )
        Unidad.objects.create(
            numero_unidad=unidad,
            curso=noveno_egb,
            asignatura=estudios_sociales
        )
        Unidad.objects.create(
            numero_unidad=unidad,
            curso=decimo_egb,
            asignatura=estudios_sociales
        )

    for unidad in range(1, 10):
        Unidad.objects.create(
            numero_unidad=unidad,
            curso=octavo_egb,
            asignatura=estudios_sociales
        )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0015_auto_20180727_2105'),
    ]

    operations = [
        migrations.RunPython(create_unidades)
    ]
