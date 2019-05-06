from django.db import migrations


def create_unit_relationships(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Curso = apps.get_model('planificaciones', 'Curso')
    Unidad = apps.get_model('planificaciones', 'Unidad')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')
    Objetivo = apps.get_model('planificaciones', 'Objetivo')

    # Asignatura
    matematica = Asignatura.objects.get(name="Matemática")

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

    # Objetivos
    objetivo2_1 = Objetivo.objects.get(codigo="O.M.2.1.")
    objetivo2_2 = Objetivo.objects.get(codigo="O.M.2.2.")
    objetivo2_3 = Objetivo.objects.get(codigo="O.M.2.3.")
    objetivo2_4 = Objetivo.objects.get(codigo="O.M.2.4.")
    objetivo2_5 = Objetivo.objects.get(codigo="O.M.2.5.")
    objetivo2_6 = Objetivo.objects.get(codigo="O.M.2.6.")
    objetivo2_7 = Objetivo.objects.get(codigo="O.M.2.7.")
    objetivo3_1 = Objetivo.objects.get(codigo="O.M.3.1.")
    objetivo3_2 = Objetivo.objects.get(codigo="O.M.3.2.")
    objetivo3_3 = Objetivo.objects.get(codigo="O.M.3.3.")
    objetivo3_4 = Objetivo.objects.get(codigo="O.M.3.4.")
    objetivo3_5 = Objetivo.objects.get(codigo="O.M.3.5.")
    objetivo4_1 = Objetivo.objects.get(codigo="O.M.4.1.")
    objetivo4_2 = Objetivo.objects.get(codigo="O.M.4.2.")
    objetivo4_3 = Objetivo.objects.get(codigo="O.M.4.3.")
    objetivo4_4 = Objetivo.objects.get(codigo="O.M.4.4.")
    objetivo4_5 = Objetivo.objects.get(codigo="O.M.4.5.")
    objetivo4_6 = Objetivo.objects.get(codigo="O.M.4.6.")
    objetivo4_7 = Objetivo.objects.get(codigo="O.M.4.7.")

    # Objetivos generales
    objetivo_general_1 = ObjetivoGeneral.objects.get(codigo="OG.M.1.")
    objetivo_general_2 = ObjetivoGeneral.objects.get(codigo="OG.M.2.")
    objetivo_general_3 = ObjetivoGeneral.objects.get(codigo="OG.M.3.")
    objetivo_general_4 = ObjetivoGeneral.objects.get(codigo="OG.M.4.")
    objetivo_general_5 = ObjetivoGeneral.objects.get(codigo="OG.M.5.")
    objetivo_general_6 = ObjetivoGeneral.objects.get(codigo="OG.M.6.")

    # Unidades
    # 2° EGB
    segundo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=segundo_egb
    )
    segundo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=segundo_egb
    )
    segundo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=segundo_egb
    )
    segundo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=segundo_egb
    )
    segundo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=segundo_egb
    )
    segundo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=segundo_egb
    )
    # 3° EGB
    tercero_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=tercero_egb
    )
    tercero_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=tercero_egb
    )
    tercero_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=tercero_egb
    )
    tercero_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=tercero_egb
    )
    tercero_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=tercero_egb
    )
    tercero_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=tercero_egb
    )
    # 4° EGB
    cuarto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=cuarto_egb
    )
    cuarto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=cuarto_egb
    )
    cuarto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=cuarto_egb
    )
    cuarto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=cuarto_egb
    )
    cuarto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=cuarto_egb
    )
    cuarto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=cuarto_egb
    )
    # 5° EGB
    quinto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=quinto_egb
    )
    quinto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=quinto_egb
    )
    quinto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=quinto_egb
    )
    quinto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=quinto_egb
    )
    quinto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=quinto_egb
    )
    quinto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=quinto_egb
    )
    # 6° EGB
    sexto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=sexto_egb
    )
    sexto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=sexto_egb
    )
    sexto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=sexto_egb
    )
    sexto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=sexto_egb
    )
    sexto_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=sexto_egb
    )
    sexto_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=sexto_egb
    )
    # 7° EGB
    septimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=septimo_egb
    )
    septimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=septimo_egb
    )
    septimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=septimo_egb
    )
    septimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=septimo_egb
    )
    septimo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=septimo_egb
    )
    septimo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=septimo_egb
    )
    # 8° EGB
    octavo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=octavo_egb
    )
    octavo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=octavo_egb
    )
    octavo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=octavo_egb
    )
    octavo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=octavo_egb
    )
    octavo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=octavo_egb
    )
    octavo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=octavo_egb
    )
    # 9° EGB
    noveno_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=noveno_egb
    )
    noveno_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=noveno_egb
    )
    noveno_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=noveno_egb
    )
    noveno_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=noveno_egb
    )
    noveno_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=noveno_egb
    )
    noveno_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=noveno_egb
    )
    # 10° EGB
    decimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=decimo_egb
    )
    decimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=decimo_egb
    )
    decimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=decimo_egb
    )
    decimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=decimo_egb
    )
    decimo_egb_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=decimo_egb
    )
    decimo_egb_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=decimo_egb
    )
    # 1° BGU
    primero_bgu_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=primero_bgu
    )
    primero_bgu_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=primero_bgu
    )
    primero_bgu_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=primero_bgu
    )
    primero_bgu_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=primero_bgu
    )
    primero_bgu_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=primero_bgu
    )
    primero_bgu_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_bgu_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=segundo_bgu
    )
    segundo_bgu_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=segundo_bgu
    )
    segundo_bgu_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=segundo_bgu
    )
    segundo_bgu_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=segundo_bgu
    )
    segundo_bgu_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=segundo_bgu
    )
    segundo_bgu_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=segundo_bgu
    )
    # 3° BGU
    tercero_bgu_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=matematica,
        curso=tercero_bgu
    )
    tercero_bgu_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=matematica,
        curso=tercero_bgu
    )
    tercero_bgu_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=matematica,
        curso=tercero_bgu
    )
    tercero_bgu_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=matematica,
        curso=tercero_bgu
    )
    tercero_bgu_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=matematica,
        curso=tercero_bgu
    )
    tercero_bgu_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=matematica,
        curso=tercero_bgu
    )

    # Asignación de objetivos a unidades
    # Segundo EGB
    segundo_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
    )
    segundo_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_6,
    )
    segundo_egb_u3.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
    )
    segundo_egb_u4.objetivos.add(
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_6,
    )
    segundo_egb_u5.objetivos.add(
        objetivo2_2,
        objetivo2_3,
        objetivo2_6,
    )
    segundo_egb_u6.objetivos.add(
        objetivo2_4,
        objetivo2_6,
        objetivo2_7,
    )
    # Tercero EGB
    tercero_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_5,
        objetivo2_7,
    )
    tercero_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
    )
    tercero_egb_u3.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
    )
    tercero_egb_u4.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
    )
    tercero_egb_u5.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
    )
    tercero_egb_u6.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
        objetivo2_7,
    )
    # Cuarto EGB
    cuarto_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_2,
        objetivo2_5,
    )
    cuarto_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_6,
        objetivo2_7,
    )
    cuarto_egb_u3.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
    )
    cuarto_egb_u4.objetivos.add(
        objetivo2_3,
        objetivo2_4,
        objetivo2_6,
    )
    cuarto_egb_u5.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_5,
        objetivo2_7,
    )
    cuarto_egb_u6.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
    )
    # Quinto EGB
    quinto_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_3,
    )
    quinto_egb_u2.objetivos.add(
        objetivo3_2,
        objetivo3_3,
    )
    quinto_egb_u3.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_4,
    )
    quinto_egb_u4.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_5,
    )
    quinto_egb_u5.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_4,
    )
    quinto_egb_u6.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
    )
    # Sexto EGB
    sexto_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_3,
    )
    sexto_egb_u2.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_3,
    )
    sexto_egb_u3.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_3,
    )
    sexto_egb_u4.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_3,
        objetivo3_5,
    )
    sexto_egb_u5.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_5,
    )
    sexto_egb_u6.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_5,
    )
    # Séptimo EGB
    septimo_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_4,
    )
    septimo_egb_u2.objetivos.add(
        objetivo3_2,
        objetivo3_4,
    )
    septimo_egb_u3.objetivos.add(
        objetivo3_2,
        objetivo3_3,
    )
    septimo_egb_u4.objetivos.add(
        objetivo3_1,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
    )
    septimo_egb_u5.objetivos.add(
        objetivo3_2,
        objetivo3_3,
    )
    septimo_egb_u6.objetivos.add(
        objetivo3_2,
        objetivo3_5,
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
    )
    octavo_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    octavo_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    octavo_egb_u4.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    octavo_egb_u5.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    octavo_egb_u6.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
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
    )
    noveno_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    noveno_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    noveno_egb_u4.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    noveno_egb_u5.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    noveno_egb_u6.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
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
    )
    decimo_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    decimo_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    decimo_egb_u4.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    decimo_egb_u5.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    decimo_egb_u6.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
    )
    # Primero BGU
    primero_bgu_u1.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_4,
    )
    primero_bgu_u2.objetivos_generales.add(
        objetivo_general_5,
        objetivo_general_6,
    )
    primero_bgu_u3.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_3,
    )
    primero_bgu_u4.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_3,
    )
    primero_bgu_u5.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_6,
    )
    primero_bgu_u6.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_6,
    )
    # Segundo BGU
    segundo_bgu_u1.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_3,
        objetivo_general_4,
    )
    segundo_bgu_u2.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_6,
    )
    segundo_bgu_u3.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_2,
        objetivo_general_6,
    )
    segundo_bgu_u4.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_6,
    )
    segundo_bgu_u5.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_6,
    )
    segundo_bgu_u6.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_5,
    )
    # Tercero BGU
    tercero_bgu_u1.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_3,
    )
    tercero_bgu_u2.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_3,
    )
    tercero_bgu_u3.objetivos_generales.add(
        objetivo_general_1,
        objetivo_general_3,
    )
    tercero_bgu_u4.objetivos_generales.add(
        objetivo_general_2,
        objetivo_general_4,
    )
    tercero_bgu_u5.objetivos_generales.add(
        objetivo_general_5,
        objetivo_general_6,
    )
    tercero_bgu_u6.objetivos_generales.add(
        objetivo_general_5,
        objetivo_general_6,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0067_auto_20180927_2058'),
    ]

    operations = [
        migrations.RunPython(create_unit_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
