from django.db import migrations


def create_unit_relationships(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Curso = apps.get_model('planificaciones', 'Curso')
    Unidad = apps.get_model('planificaciones', 'Unidad')
    Objetivo = apps.get_model('planificaciones', 'Objetivo')

    # Asignatura
    ciencias_naturales = Asignatura.objects.get(name="Ciencias Naturales")

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

    # Objetivos
    objetivo2_1 = Objetivo.objects.get(codigo="O.CN.2.1.")
    objetivo2_2 = Objetivo.objects.get(codigo="O.CN.2.2.")
    objetivo2_3 = Objetivo.objects.get(codigo="O.CN.2.3.")
    objetivo2_4 = Objetivo.objects.get(codigo="O.CN.2.4.")
    objetivo2_5 = Objetivo.objects.get(codigo="O.CN.2.5.")
    objetivo2_6 = Objetivo.objects.get(codigo="O.CN.2.6.")
    objetivo2_7 = Objetivo.objects.get(codigo="O.CN.2.7.")
    objetivo2_8 = Objetivo.objects.get(codigo="O.CN.2.8.")
    objetivo2_9 = Objetivo.objects.get(codigo="O.CN.2.9.")
    objetivo2_10 = Objetivo.objects.get(codigo="O.CN.2.10.")
    objetivo2_11 = Objetivo.objects.get(codigo="O.CN.2.11.")
    objetivo3_1 = Objetivo.objects.get(codigo="O.CN.3.1.")
    objetivo3_2 = Objetivo.objects.get(codigo="O.CN.3.2.")
    objetivo3_3 = Objetivo.objects.get(codigo="O.CN.3.3.")
    objetivo3_4 = Objetivo.objects.get(codigo="O.CN.3.4.")
    objetivo3_5 = Objetivo.objects.get(codigo="O.CN.3.5.")
    objetivo3_6 = Objetivo.objects.get(codigo="O.CN.3.6.")
    objetivo3_7 = Objetivo.objects.get(codigo="O.CN.3.7.")
    objetivo3_8 = Objetivo.objects.get(codigo="O.CN.3.8.")
    objetivo3_9 = Objetivo.objects.get(codigo="O.CN.3.9.")
    objetivo3_10 = Objetivo.objects.get(codigo="O.CN.3.10.")
    objetivo4_1 = Objetivo.objects.get(codigo="O.CN.4.1.")
    objetivo4_2 = Objetivo.objects.get(codigo="O.CN.4.2.")
    objetivo4_3 = Objetivo.objects.get(codigo="O.CN.4.3.")
    objetivo4_4 = Objetivo.objects.get(codigo="O.CN.4.4.")
    objetivo4_5 = Objetivo.objects.get(codigo="O.CN.4.5.")
    objetivo4_6 = Objetivo.objects.get(codigo="O.CN.4.6.")
    objetivo4_7 = Objetivo.objects.get(codigo="O.CN.4.7.")
    objetivo4_8 = Objetivo.objects.get(codigo="O.CN.4.8.")
    objetivo4_9 = Objetivo.objects.get(codigo="O.CN.4.9.")
    objetivo4_10 = Objetivo.objects.get(codigo="O.CN.4.10.")

    # Unidades
    # 2° EGB
    segundo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=segundo_egb
    )
    segundo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=segundo_egb
    )
    segundo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=segundo_egb
    )
    segundo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=segundo_egb
    )
    # 3° EGB
    tercero_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=tercero_egb
    )
    tercero_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=tercero_egb
    )
    tercero_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=tercero_egb
    )
    tercero_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=tercero_egb
    )
    # 4° EGB
    cuarto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=cuarto_egb
    )
    cuarto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=cuarto_egb
    )
    cuarto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=cuarto_egb
    )
    cuarto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=cuarto_egb
    )
    cuarto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=cuarto_egb
    )
    cuarto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=cuarto_egb
    )
    # 5° EGB
    quinto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=quinto_egb
    )
    quinto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=quinto_egb
    )
    quinto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=quinto_egb
    )
    quinto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=quinto_egb
    )
    quinto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=quinto_egb
    )
    quinto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=quinto_egb
    )
    # 6° EGB
    sexto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=sexto_egb
    )
    sexto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=sexto_egb
    )
    sexto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=sexto_egb
    )
    sexto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=sexto_egb
    )
    sexto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=sexto_egb
    )
    sexto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=sexto_egb
    )
    # 7° EGB
    septimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=septimo_egb
    )
    septimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=septimo_egb
    )
    septimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=septimo_egb
    )
    septimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=septimo_egb
    )
    septimo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=septimo_egb
    )
    septimo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=septimo_egb
    )
    # 8° EGB
    octavo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=octavo_egb
    )
    octavo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=octavo_egb
    )
    octavo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=octavo_egb
    )
    octavo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=octavo_egb
    )
    octavo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=octavo_egb
    )
    octavo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=octavo_egb
    )
    # 9° EGB
    noveno_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=noveno_egb
    )
    noveno_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=noveno_egb
    )
    noveno_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=noveno_egb
    )
    noveno_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=noveno_egb
    )
    noveno_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=noveno_egb
    )
    noveno_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=noveno_egb
    )
    # 10° EGB
    decimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciencias_naturales,
        curso=decimo_egb
    )
    decimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciencias_naturales,
        curso=decimo_egb
    )
    decimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciencias_naturales,
        curso=decimo_egb
    )
    decimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciencias_naturales,
        curso=decimo_egb
    )
    decimo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=ciencias_naturales,
        curso=decimo_egb
    )
    decimo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=ciencias_naturales,
        curso=decimo_egb
    )

    # Asignación de objetivos a unidades
    # Segundo EGB
    segundo_egb_u1.objetivos.add(
        objetivo2_3,
        objetivo2_4,
    )
    segundo_egb_u2.objetivos.add(
        objetivo2_2,
        objetivo2_5,
        objetivo2_6,
    )
    segundo_egb_u3.objetivos.add(
        objetivo2_1,
    )
    segundo_egb_u4.objetivos.add(
        objetivo2_8,
        objetivo2_10,
        objetivo2_11,
    )
    # Tercero EGB
    tercero_egb_u1.objetivos.add(
        objetivo2_8,
    )
    tercero_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_10,
    )
    tercero_egb_u3.objetivos.add(
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
    )
    tercero_egb_u4.objetivos.add(
        objetivo2_8,
    )
    # Cuarto EGB
    cuarto_egb_u1.objetivos.add(
        objetivo2_5,
        objetivo2_6,
        objetivo2_9,
    )
    cuarto_egb_u2.objetivos.add(
        objetivo2_7,
    )
    cuarto_egb_u3.objetivos.add(
        objetivo2_2,
    )
    cuarto_egb_u4.objetivos.add(
        objetivo2_10,
        objetivo2_11,
    )
    cuarto_egb_u5.objetivos.add(
        objetivo2_1,
    )
    cuarto_egb_u6.objetivos.add(
        objetivo2_3,
    )
    # Quinto EGB
    quinto_egb_u1.objetivos.add(
        objetivo3_2,
    )
    quinto_egb_u2.objetivos.add(
        objetivo3_4,
        objetivo3_5,
    )
    quinto_egb_u3.objetivos.add(
        objetivo3_1,
        objetivo3_3,
    )
    quinto_egb_u4.objetivos.add(
        objetivo3_9,
    )
    quinto_egb_u5.objetivos.add(
        objetivo3_8,
    )
    quinto_egb_u6.objetivos.add(
        objetivo3_7,
        objetivo3_10,
    )
    # Sexto EGB
    sexto_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_2,
    )
    sexto_egb_u2.objetivos.add(
        objetivo3_4,
        objetivo3_5,
    )
    sexto_egb_u3.objetivos.add(
        objetivo3_8,
        objetivo3_9,
    )
    sexto_egb_u4.objetivos.add(
        objetivo3_3,
        objetivo3_10,
    )
    sexto_egb_u5.objetivos.add(
        objetivo3_7,
    )
    sexto_egb_u6.objetivos.add(
        objetivo3_6,
    )
    # Séptimo EGB
    septimo_egb_u1.objetivos.add(
        objetivo3_1,
    )
    septimo_egb_u2.objetivos.add(
        objetivo3_4,
    )
    septimo_egb_u3.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_8,
    )
    septimo_egb_u4.objetivos.add(
        objetivo3_7,
        objetivo3_8,
        objetivo3_10,
    )
    septimo_egb_u5.objetivos.add(
        objetivo3_6,
        objetivo3_7,
        objetivo3_10,
    )
    septimo_egb_u6.objetivos.add(
        objetivo3_6,
        objetivo3_9,
        objetivo3_10,
    )
    # Octavo EGB
    octavo_egb_u1.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    octavo_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    octavo_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    octavo_egb_u4.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    octavo_egb_u5.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    octavo_egb_u6.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    # Noveno EGB
    noveno_egb_u1.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    noveno_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    noveno_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    noveno_egb_u4.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    noveno_egb_u5.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    noveno_egb_u6.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    # Décimo EGB
    decimo_egb_u1.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    decimo_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    decimo_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    decimo_egb_u4.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    decimo_egb_u5.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )
    decimo_egb_u6.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0051_auto_20180929_1625'),
    ]

    operations = [
        migrations.RunPython(create_unit_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
