from django.db import migrations


def create_books(model, nivel, asignatura, todos_cursos):
    """Función para crear los libros"""
    Libro = model

    cursos_egb = todos_cursos[:-3]
    cursos_bgu = todos_cursos[-3:]

    asignaturas_especiales = [
        'Emprendimiento y Gestión',
        'Filosofía',
        'Educación para la Ciudadanía'
    ]

    if nivel == 'EGB':
        cursos = cursos_egb
    elif nivel == 'BGU':
        cursos = cursos_bgu

    if asignatura.name in asignaturas_especiales:
        cursos = cursos[:-1]

    if asignatura.name == 'Educación para la Ciudadanía':
        nombre = 'Ciudadanía'
    elif asignatura.name == 'Emprendimiento y Gestión':
        nombre = 'Emprendimiento'
    else:
        nombre = asignatura.name

    for index, curso in enumerate(cursos):
        if nivel == 'EGB':
            numero_curso = index + 2
        elif nivel == 'BGU':
            numero_curso = index + 1

        Libro.objects.create(
            name="{0} {1}{2}".format(nombre, numero_curso, nivel),
            archivo="libros/{} {}{}.pdf".format(nombre, numero_curso, nivel),
            curso=curso,
            asignatura=asignatura
        )


def add_books(apps, schema_editor):
    """Función para añadir los libros de las materias"""
    Libro = apps.get_model('asistente', 'Libro')
    Curso = apps.get_model('planificaciones', 'Curso')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')

    # Cursos
    segundo_egb = Curso.objects.get(name="2° EGB")
    tercero_egb = Curso.objects.get(name="3° EGB")
    cuarto_egb = Curso.objects.get(name="4° EGB")
    quinto_egb = Curso.objects.get(name="5° EGB")
    sexto_egb = Curso.objects.get(name="6° EGB")
    septimo_egb = Curso.objects.get(name="7° EGB")
    octavo_egb = Curso.objects.get(name="8° EGB")
    noveno_egb = Curso.objects.get(name="9° EGB")
    decimo_egb = Curso.objects.get(name="10° EGB")
    primero_bgu = Curso.objects.get(name="1° BGU")
    tercero_bgu = Curso.objects.get(name="2° BGU")
    segundo_bgu = Curso.objects.get(name="3° BGU")

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

    # Asignaturas
    lengua_literatura = Asignatura.objects.get(
        name="Lengua y Literatura"
    )
    matematica = Asignatura.objects.get(name="Matemática")
    ciencias_naturales = Asignatura.objects.get(
        name="Ciencias Naturales"
    )
    biologia = Asignatura.objects.get(name="Biología")
    quimica = Asignatura.objects.get(name="Química")
    fisica = Asignatura.objects.get(name="Física")
    estudios_sociales = Asignatura.objects.get(
        name="Estudios Sociales"
    )
    historia = Asignatura.objects.get(name="Historia")
    filosofia = Asignatura.objects.get(name="Filosofía")
    educacion_ciudadania = Asignatura.objects.get(
        name="Educación para la Ciudadanía"
    )
    emprendimiento = Asignatura.objects.get(
        name="Emprendimiento y Gestión"
    )

    create_books(Libro, 'EGB', matematica, todos_cursos)
    create_books(Libro, 'BGU', matematica, todos_cursos)

    create_books(Libro, 'EGB', lengua_literatura, todos_cursos)
    create_books(Libro, 'BGU', lengua_literatura, todos_cursos)

    create_books(Libro, 'EGB', ciencias_naturales, todos_cursos)
    create_books(Libro, 'EGB', estudios_sociales, todos_cursos)

    create_books(Libro, 'BGU', biologia, todos_cursos)
    create_books(Libro, 'BGU', quimica, todos_cursos)
    create_books(Libro, 'BGU', fisica, todos_cursos)

    create_books(Libro, 'BGU', historia, todos_cursos)
    create_books(Libro, 'BGU', educacion_ciudadania, todos_cursos)
    create_books(Libro, 'BGU', filosofia, todos_cursos)

    create_books(Libro, 'BGU', emprendimiento, todos_cursos)


class Migration(migrations.Migration):

    dependencies = [
        ('asistente', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_books, reverse_code=migrations.RunPython.noop)
    ]
