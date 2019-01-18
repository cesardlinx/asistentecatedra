from django.db import migrations


def create_unit_relationships(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Curso = apps.get_model('planificaciones', 'Curso')
    Unidad = apps.get_model('planificaciones', 'Unidad')
    Objetivo = apps.get_model('planificaciones', 'Objetivo')

    # Asignatura
    estudios_sociales = Asignatura.objects.get(name="Estudios Sociales")

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
    objetivo2_1 = Objetivo.objects.get(codigo="O.CS.2.1.")
    objetivo2_2 = Objetivo.objects.get(codigo="O.CS.2.2.")
    objetivo2_3 = Objetivo.objects.get(codigo="O.CS.2.3.")
    objetivo2_4 = Objetivo.objects.get(codigo="O.CS.2.4.")
    objetivo2_5 = Objetivo.objects.get(codigo="O.CS.2.5.")
    objetivo2_6 = Objetivo.objects.get(codigo="O.CS.2.6.")
    objetivo2_7 = Objetivo.objects.get(codigo="O.CS.2.7.")
    objetivo3_1 = Objetivo.objects.get(codigo="O.CS.3.1.")
    objetivo3_2 = Objetivo.objects.get(codigo="O.CS.3.2.")
    objetivo3_3 = Objetivo.objects.get(codigo="O.CS.3.3.")
    objetivo3_4 = Objetivo.objects.get(codigo="O.CS.3.4.")
    objetivo3_5 = Objetivo.objects.get(codigo="O.CS.3.5.")
    objetivo3_6 = Objetivo.objects.get(codigo="O.CS.3.6.")
    objetivo3_7 = Objetivo.objects.get(codigo="O.CS.3.7.")
    objetivo4_1 = Objetivo.objects.get(codigo="O.CS.4.1.")
    objetivo4_2 = Objetivo.objects.get(codigo="O.CS.4.2.")
    objetivo4_3 = Objetivo.objects.get(codigo="O.CS.4.3.")
    objetivo4_4 = Objetivo.objects.get(codigo="O.CS.4.4.")
    objetivo4_5 = Objetivo.objects.get(codigo="O.CS.4.5.")
    objetivo4_6 = Objetivo.objects.get(codigo="O.CS.4.6.")
    objetivo4_7 = Objetivo.objects.get(codigo="O.CS.4.7.")
    objetivo4_8 = Objetivo.objects.get(codigo="O.CS.4.8.")

    # Unidades
    # 2° EGB
    segundo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=segundo_egb
    )
    segundo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=segundo_egb
    )
    segundo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=segundo_egb
    )
    segundo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=segundo_egb
    )
    segundo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=segundo_egb
    )
    segundo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=segundo_egb
    )
    # 3° EGB
    tercero_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=tercero_egb
    )
    tercero_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=tercero_egb
    )
    tercero_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=tercero_egb
    )
    tercero_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=tercero_egb
    )
    tercero_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=tercero_egb
    )
    tercero_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=tercero_egb
    )
    # 4° EGB
    cuarto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=cuarto_egb
    )
    cuarto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=cuarto_egb
    )
    cuarto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=cuarto_egb
    )
    cuarto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=cuarto_egb
    )
    cuarto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=cuarto_egb
    )
    cuarto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=cuarto_egb
    )
    # 5° EGB
    quinto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u7 = Unidad.objects.get(
        numero_unidad=7,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    quinto_egb_u8 = Unidad.objects.get(
        numero_unidad=8,
        asignatura=estudios_sociales,
        curso=quinto_egb
    )
    # 6° EGB
    sexto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    sexto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    sexto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    sexto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    sexto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    sexto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    sexto_egb_u7 = Unidad.objects.get(
        numero_unidad=7,
        asignatura=estudios_sociales,
        curso=sexto_egb
    )
    # 7° EGB
    septimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u7 = Unidad.objects.get(
        numero_unidad=7,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    septimo_egb_u8 = Unidad.objects.get(
        numero_unidad=8,
        asignatura=estudios_sociales,
        curso=septimo_egb
    )
    # 8° EGB
    octavo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u7 = Unidad.objects.get(
        numero_unidad=7,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u8 = Unidad.objects.get(
        numero_unidad=8,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    octavo_egb_u9 = Unidad.objects.get(
        numero_unidad=9,
        asignatura=estudios_sociales,
        curso=octavo_egb
    )
    # 9° EGB
    noveno_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u7 = Unidad.objects.get(
        numero_unidad=7,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    noveno_egb_u8 = Unidad.objects.get(
        numero_unidad=8,
        asignatura=estudios_sociales,
        curso=noveno_egb
    )
    # 10° EGB
    decimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u7 = Unidad.objects.get(
        numero_unidad=7,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )
    decimo_egb_u8 = Unidad.objects.get(
        numero_unidad=8,
        asignatura=estudios_sociales,
        curso=decimo_egb
    )

    # Asignación de objetivos a unidades
    # Segundo EGB
    segundo_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    segundo_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    segundo_egb_u3.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    segundo_egb_u4.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    segundo_egb_u5.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    segundo_egb_u6.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    # Tercero EGB
    tercero_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    tercero_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    tercero_egb_u3.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    tercero_egb_u4.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    tercero_egb_u5.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    tercero_egb_u6.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    # Cuarto EGB
    cuarto_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    cuarto_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    cuarto_egb_u3.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    cuarto_egb_u4.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    cuarto_egb_u5.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    cuarto_egb_u6.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
    )
    # Media (Quinto, Sexto, Séptimo)
    objetivo3_1.unidades.add(
        quinto_egb_u1,
        quinto_egb_u2,
        quinto_egb_u3,
        quinto_egb_u4,
    )
    objetivo3_2.unidades.add(
        quinto_egb_u1,
        quinto_egb_u2,
        quinto_egb_u3,
        quinto_egb_u4,
        sexto_egb_u1,
        sexto_egb_u2,
        sexto_egb_u3,
        sexto_egb_u4,
        sexto_egb_u5,
        sexto_egb_u6,
        septimo_egb_u1,
        septimo_egb_u2,
        septimo_egb_u3,
    )
    objetivo3_3.unidades.add(
        quinto_egb_u5,
        quinto_egb_u6,
        septimo_egb_u4,
        septimo_egb_u5,
        septimo_egb_u6,
    )
    objetivo3_4.unidades.add(
        septimo_egb_u4,
        septimo_egb_u5,
        septimo_egb_u6,
    )
    objetivo3_5.unidades.add(
        sexto_egb_u7,
        septimo_egb_u7,
        septimo_egb_u8,
    )
    objetivo3_6.unidades.add(
        quinto_egb_u7,
        quinto_egb_u8,
    )
    objetivo3_7.unidades.add(
        septimo_egb_u7,
        septimo_egb_u8,
    )
    # Superior (Octavo, Noveno y Décimo)
    objetivo4_1.unidades.add(
        octavo_egb_u1,
        octavo_egb_u2,
        octavo_egb_u3,
        octavo_egb_u4,
    )
    objetivo4_2.unidades.add(
        octavo_egb_u1,
        octavo_egb_u2,
        octavo_egb_u3,
        octavo_egb_u4,
        noveno_egb_u1,
        noveno_egb_u2,
        noveno_egb_u3,
        noveno_egb_u4,
    )
    objetivo4_3.unidades.add(
        octavo_egb_u5,
        octavo_egb_u6,
        octavo_egb_u7,
    )
    objetivo4_4.unidades.add(
        noveno_egb_u5,
        noveno_egb_u6,
        decimo_egb_u1,
        decimo_egb_u2,
        decimo_egb_u3,
    )
    objetivo4_5.unidades.add(
        decimo_egb_u1,
        decimo_egb_u2,
        decimo_egb_u3,
        decimo_egb_u4,
        decimo_egb_u5,
        decimo_egb_u6,
    )
    objetivo4_6.unidades.add(
        noveno_egb_u7,
        noveno_egb_u8,
        decimo_egb_u7,
        decimo_egb_u8,
    )
    objetivo4_7.unidades.add(
        octavo_egb_u8,
        octavo_egb_u9,
    )
    objetivo4_8.unidades.add(
        decimo_egb_u7,
        decimo_egb_u8,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0069_auto_20180929_1844'),
    ]

    operations = [
        migrations.RunPython(create_unit_relationships)
    ]
