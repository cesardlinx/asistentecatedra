from django.db import migrations


def create_bloques(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Bloque = apps.get_model('planificaciones', 'BloqueCurricular')

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

    # Bloques
    Bloque.objects.bulk_create([
        # Ciencias naturales
        Bloque(numero_bloque=1,
               name='Seres vivos y su ambiente',
               asignatura=ciencias_naturales),
        Bloque(numero_bloque=2,
               name='Cuerpo humano y salud', asignatura=ciencias_naturales),
        Bloque(numero_bloque=3,
               name='Materia y energía', asignatura=ciencias_naturales),
        Bloque(numero_bloque=4,
               name='La Tierra y el Universo', asignatura=ciencias_naturales),
        Bloque(numero_bloque=5,
               name='Ciencia en acción', asignatura=ciencias_naturales),
        # Biología
        Bloque(numero_bloque=1,
               name='Evolución de los seres vivos', asignatura=biologia),
        Bloque(numero_bloque=2,
               name='Biología celular y molecular', asignatura=biologia),
        Bloque(numero_bloque=3,
               name='Biología animal y vegetal', asignatura=biologia),
        Bloque(numero_bloque=4,
               name='Cuerpo humano y salud', asignatura=biologia),
        Bloque(numero_bloque=5,
               name='Biología en acción', asignatura=biologia),
        # Química
        Bloque(numero_bloque=1,
               name='El mundo de la Química', asignatura=quimica),
        Bloque(numero_bloque=2,
               name='La química y su lenguaje', asignatura=quimica),
        Bloque(numero_bloque=3,
               name='Química en acción', asignatura=quimica),
        # Física
        Bloque(numero_bloque=1, name='Movimiento y fuerza', asignatura=fisica),
        Bloque(numero_bloque=2, name='Energía, conservación y transferencia',
               asignatura=fisica),
        Bloque(numero_bloque=3, name='Ondas y radiación', asignatura=fisica),
        Bloque(numero_bloque=4,
               name='La Tierra y el Universo', asignatura=fisica),
        Bloque(numero_bloque=5, name='La Física de hoy', asignatura=fisica),
        Bloque(numero_bloque=6, name='Física en acción', asignatura=fisica),
        # Estudios Sociales
        Bloque(numero_bloque=1,
               name='Historia e identidad', asignatura=estudios_sociales),
        Bloque(numero_bloque=2,
               name='Los seres humanos en el espacio',
               asignatura=estudios_sociales),
        Bloque(numero_bloque=3,
               name='La convivencia', asignatura=estudios_sociales),

        # Historia
        Bloque(numero_bloque=1,
               name='Los orígenes y las primeras culturas de la humanidad',
               asignatura=historia),
        Bloque(numero_bloque=2,
               name='De la Edad Media a la Modernidad', asignatura=historia),
        Bloque(numero_bloque=3,
               name='América latina: mestizaje y liberación',
               asignatura=historia),
        Bloque(numero_bloque=4, name='Economía: trabajo y sociedad',
               asignatura=historia),
        # Educación para la ciudadanía
        Bloque(numero_bloque=1, name='Ciudadanía y derechos',
               asignatura=educacion_ciudadania),
        Bloque(numero_bloque=2, name='La democracia moderna',
               asignatura=educacion_ciudadania),
        Bloque(numero_bloque=3,
               name=('La democracia y la construcción de un Estado '
                     'plurinacional'),
               asignatura=educacion_ciudadania),
        Bloque(numero_bloque=4,
               name='El Estado y su organización',
               asignatura=educacion_ciudadania),
        # Filosofía
        Bloque(numero_bloque=1,
               name=('El orígen del pensamiento filosófico y su relación '
                     'con la ciudadanía'),
               asignatura=filosofia),
        Bloque(numero_bloque=2,
               name=('La argumentación y la construcción del discurso '
                     'lógico, oral y escrito'),
               asignatura=filosofia),
        Bloque(numero_bloque=3,
               name='Filosofía occidental y filosofía latinoamericana',
               asignatura=filosofia),
        Bloque(numero_bloque=4,
               name=('El individuo y la comunidad: lo ético, '
                     'lo estético, lo hedónico'),
               asignatura=filosofia),
        # Lengua y Literatura
        Bloque(numero_bloque=1,
               name='Lengua y cultura', asignatura=lengua_literatura),
        Bloque(numero_bloque=2,
               name='Comunicación oral', asignatura=lengua_literatura),
        Bloque(numero_bloque=3,
               name='Lectura', asignatura=lengua_literatura),
        Bloque(numero_bloque=4,
               name='Escritura', asignatura=lengua_literatura),
        Bloque(numero_bloque=5,
               name='Literatura', asignatura=lengua_literatura),
        # Matemática
        Bloque(numero_bloque=1,
               name='Álgebra y funciones', asignatura=matematica),
        Bloque(numero_bloque=2,
               name='Geometría y medida', asignatura=matematica),
        Bloque(numero_bloque=3,
               name='Estadística y probabilidad', asignatura=matematica),

        # Emprendimiento
        Bloque(numero_bloque=1,
               name='Planificación y control financiero del emprendimiento',
               asignatura=emprendimiento),
        Bloque(numero_bloque=2,
               name='Responsabilidad legal y social del emprendedor',
               asignatura=emprendimiento),
        Bloque(numero_bloque=3,
               name='Investigación de mercado y estadística aplicada',
               asignatura=emprendimiento),
        Bloque(numero_bloque=4,
               name='Economía para la toma de decisiones',
               asignatura=emprendimiento),
        Bloque(numero_bloque=5,
               name='Formulación del proyecto de emprendimiento',
               asignatura=emprendimiento),
        Bloque(numero_bloque=6,
               name='Evaluación del proyecto de emprendimiento',
               asignatura=emprendimiento),

    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0006_auto_20180727_1415'),
    ]

    operations = [
        migrations.RunPython(
            create_bloques, reverse_code=migrations.RunPython.noop)
    ]
