from django.db import migrations


def create_unit_relationships(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Curso = apps.get_model('planificaciones', 'Curso')
    Unidad = apps.get_model('planificaciones', 'Unidad')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')
    Objetivo = apps.get_model('planificaciones', 'Objetivo')

    # Asignatura
    literatura = Asignatura.objects.get(name="Lengua y Literatura")

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
    objetivo2_1 = Objetivo.objects.get(codigo="O.LL.2.1.")
    objetivo2_2 = Objetivo.objects.get(codigo="O.LL.2.2.")
    objetivo2_3 = Objetivo.objects.get(codigo="O.LL.2.3.")
    objetivo2_4 = Objetivo.objects.get(codigo="O.LL.2.4.")
    objetivo2_5 = Objetivo.objects.get(codigo="O.LL.2.5.")
    objetivo2_6 = Objetivo.objects.get(codigo="O.LL.2.6.")
    objetivo2_7 = Objetivo.objects.get(codigo="O.LL.2.7.")
    objetivo2_8 = Objetivo.objects.get(codigo="O.LL.2.8.")
    objetivo2_9 = Objetivo.objects.get(codigo="O.LL.2.9.")
    objetivo2_10 = Objetivo.objects.get(codigo="O.LL.2.10.")
    objetivo2_11 = Objetivo.objects.get(codigo="O.LL.2.11.")
    objetivo2_12 = Objetivo.objects.get(codigo="O.LL.2.12.")
    objetivo3_1 = Objetivo.objects.get(codigo="O.LL.3.1.")
    objetivo3_2 = Objetivo.objects.get(codigo="O.LL.3.2.")
    objetivo3_3 = Objetivo.objects.get(codigo="O.LL.3.3.")
    objetivo3_4 = Objetivo.objects.get(codigo="O.LL.3.4.")
    objetivo3_5 = Objetivo.objects.get(codigo="O.LL.3.5.")
    objetivo3_6 = Objetivo.objects.get(codigo="O.LL.3.6.")
    objetivo3_7 = Objetivo.objects.get(codigo="O.LL.3.7.")
    objetivo3_8 = Objetivo.objects.get(codigo="O.LL.3.8.")
    objetivo3_9 = Objetivo.objects.get(codigo="O.LL.3.9.")
    objetivo3_10 = Objetivo.objects.get(codigo="O.LL.3.10.")
    objetivo3_11 = Objetivo.objects.get(codigo="O.LL.3.11.")
    objetivo3_12 = Objetivo.objects.get(codigo="O.LL.3.12.")
    objetivo4_1 = Objetivo.objects.get(codigo="O.LL.4.1.")
    objetivo4_2 = Objetivo.objects.get(codigo="O.LL.4.2.")
    objetivo4_3 = Objetivo.objects.get(codigo="O.LL.4.3.")
    objetivo4_4 = Objetivo.objects.get(codigo="O.LL.4.4.")
    objetivo4_5 = Objetivo.objects.get(codigo="O.LL.4.5.")
    objetivo4_6 = Objetivo.objects.get(codigo="O.LL.4.6.")
    objetivo4_7 = Objetivo.objects.get(codigo="O.LL.4.7.")
    objetivo4_8 = Objetivo.objects.get(codigo="O.LL.4.8.")
    objetivo4_9 = Objetivo.objects.get(codigo="O.LL.4.9.")
    objetivo4_10 = Objetivo.objects.get(codigo="O.LL.4.10.")
    objetivo4_11 = Objetivo.objects.get(codigo="O.LL.4.11.")
    objetivo4_12 = Objetivo.objects.get(codigo="O.LL.4.12.")

    # Objetivos generales
    objetivo_general_1 = ObjetivoGeneral.objects.get(codigo="OG.LL.1.")
    objetivo_general_2 = ObjetivoGeneral.objects.get(codigo="OG.LL.2.")
    objetivo_general_3 = ObjetivoGeneral.objects.get(codigo="OG.LL.3.")
    objetivo_general_4 = ObjetivoGeneral.objects.get(codigo="OG.LL.4.")
    objetivo_general_5 = ObjetivoGeneral.objects.get(codigo="OG.LL.5.")
    objetivo_general_6 = ObjetivoGeneral.objects.get(codigo="OG.LL.6.")
    objetivo_general_7 = ObjetivoGeneral.objects.get(codigo="OG.LL.7.")
    objetivo_general_8 = ObjetivoGeneral.objects.get(codigo="OG.LL.8.")
    objetivo_general_9 = ObjetivoGeneral.objects.get(codigo="OG.LL.9.")
    objetivo_general_10 = ObjetivoGeneral.objects.get(codigo="OG.LL.10.")
    objetivo_general_11 = ObjetivoGeneral.objects.get(codigo="OG.LL.11.")

    # Unidades
    # 2° EGB
    segundo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=segundo_egb
    )
    segundo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=segundo_egb
    )
    segundo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=segundo_egb
    )
    segundo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=segundo_egb
    )
    # 3° EGB
    tercero_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=tercero_egb
    )
    tercero_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=tercero_egb
    )
    tercero_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=tercero_egb
    )
    tercero_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=tercero_egb
    )
    # 4° EGB
    cuarto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=cuarto_egb
    )
    cuarto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=cuarto_egb
    )
    cuarto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=cuarto_egb
    )
    cuarto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=cuarto_egb
    )
    # 5° EGB
    quinto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=quinto_egb
    )
    quinto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=quinto_egb
    )
    quinto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=quinto_egb
    )
    quinto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=quinto_egb
    )
    # 6° EGB
    sexto_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=sexto_egb
    )
    sexto_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=sexto_egb
    )
    sexto_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=sexto_egb
    )
    sexto_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=sexto_egb
    )
    # 7° EGB
    septimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=septimo_egb
    )
    septimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=septimo_egb
    )
    septimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=septimo_egb
    )
    septimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=septimo_egb
    )
    # 8° EGB
    octavo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=octavo_egb
    )
    octavo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=octavo_egb
    )
    octavo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=octavo_egb
    )
    octavo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=octavo_egb
    )
    # 9° EGB
    noveno_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=noveno_egb
    )
    noveno_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=noveno_egb
    )
    noveno_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=noveno_egb
    )
    noveno_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=noveno_egb
    )
    # 10° EGB
    decimo_egb_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=decimo_egb
    )
    decimo_egb_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=decimo_egb
    )
    decimo_egb_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=decimo_egb
    )
    decimo_egb_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=decimo_egb
    )
    # 1° BGU
    primero_bgu_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=primero_bgu
    )
    primero_bgu_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=primero_bgu
    )
    primero_bgu_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=primero_bgu
    )
    primero_bgu_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=primero_bgu
    )
    primero_bgu_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=literatura,
        curso=primero_bgu
    )
    primero_bgu_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=literatura,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_bgu_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=segundo_bgu
    )
    segundo_bgu_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=segundo_bgu
    )
    segundo_bgu_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=segundo_bgu
    )
    segundo_bgu_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=segundo_bgu
    )
    segundo_bgu_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=literatura,
        curso=segundo_bgu
    )
    segundo_bgu_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=literatura,
        curso=segundo_bgu
    )
    # 3° BGU
    tercero_bgu_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=literatura,
        curso=tercero_bgu
    )
    tercero_bgu_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=literatura,
        curso=tercero_bgu
    )
    tercero_bgu_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=literatura,
        curso=tercero_bgu
    )
    tercero_bgu_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=literatura,
        curso=tercero_bgu
    )
    tercero_bgu_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=literatura,
        curso=tercero_bgu
    )
    tercero_bgu_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=literatura,
        curso=tercero_bgu
    )

    # Asignación de objetivos a unidades
    # Segundo EGB
    segundo_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_10,
        objetivo2_11,
    )
    segundo_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_10,
        objetivo2_11,
        objetivo2_12,
    )
    segundo_egb_u3.objetivos.add(
        objetivo2_2,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_10,
        objetivo2_11,
    )
    segundo_egb_u4.objetivos.add(
        objetivo2_2,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_10,
        objetivo2_11,
    )
    # Tercero EGB
    tercero_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_9,
        objetivo2_11,
    )
    tercero_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_9,
        objetivo2_11,
        objetivo2_12,
    )
    tercero_egb_u3.objetivos.add(
        objetivo2_2,
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
        objetivo2_8,
        objetivo2_9,
        objetivo2_10,
        objetivo2_11,
        objetivo2_12,
    )
    tercero_egb_u4.objetivos.add(
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_9,
        objetivo2_11,
        objetivo2_12,
    )
    # Cuarto EGB
    cuarto_egb_u1.objetivos.add(
        objetivo2_1,
        objetivo2_3,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_9,
        objetivo2_11,
    )
    cuarto_egb_u2.objetivos.add(
        objetivo2_1,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_9,
        objetivo2_11,
    )
    cuarto_egb_u3.objetivos.add(
        objetivo2_2,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_8,
        objetivo2_11,
    )
    cuarto_egb_u4.objetivos.add(
        objetivo2_2,
        objetivo2_3,
        objetivo2_4,
        objetivo2_5,
        objetivo2_6,
        objetivo2_7,
        objetivo2_8,
        objetivo2_11,
    )
    # Quinto EGB
    quinto_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_4,
        objetivo3_6,
        objetivo3_8,
        objetivo3_10,
        objetivo3_11,
    )
    quinto_egb_u2.objetivos.add(
        objetivo3_1,
        objetivo3_4,
        objetivo3_6,
        objetivo3_8,
        objetivo3_10,
        objetivo3_11,
    )
    quinto_egb_u3.objetivos.add(
        objetivo3_1,
        objetivo3_4,
        objetivo3_6,
        objetivo3_8,
        objetivo3_10,
        objetivo3_11,
    )
    quinto_egb_u4.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_4,
        objetivo3_6,
        objetivo3_8,
        objetivo3_10,
        objetivo3_11,
    )
    # Sexto EGB
    sexto_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_2,
        objetivo3_3,
        objetivo3_4,
        objetivo3_6,
        objetivo3_7,
        objetivo3_8,
        objetivo3_9,
        objetivo3_10,
        objetivo3_11,
        objetivo3_12,
    )
    sexto_egb_u2.objetivos.add(
        objetivo3_1,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_7,
        objetivo3_8,
        objetivo3_9,
        objetivo3_10,
        objetivo3_11,
        objetivo3_12,
    )
    sexto_egb_u3.objetivos.add(
        objetivo3_1,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_7,
        objetivo3_8,
        objetivo3_9,
        objetivo3_10,
        objetivo3_11,
        objetivo3_12,
    )
    sexto_egb_u4.objetivos.add(
        objetivo3_1,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_7,
        objetivo3_8,
        objetivo3_9,
        objetivo3_10,
        objetivo3_11,
    )
    # Séptimo EGB
    septimo_egb_u1.objetivos.add(
        objetivo3_1,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_8,
        objetivo3_10,
        objetivo3_11,
        objetivo3_12,
    )
    septimo_egb_u2.objetivos.add(
        objetivo3_2,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_8,
        objetivo3_10,
        objetivo3_11,
        objetivo3_12,
    )
    septimo_egb_u3.objetivos.add(
        objetivo3_1,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_7,
        objetivo3_8,
        objetivo3_9,
        objetivo3_10,
        objetivo3_11,
        objetivo3_12,
    )
    septimo_egb_u4.objetivos.add(
        objetivo3_1,
        objetivo3_3,
        objetivo3_4,
        objetivo3_5,
        objetivo3_6,
        objetivo3_8,
        objetivo3_9,
        objetivo3_10,
        objetivo3_11,
    )
    # Octavo
    octavo_egb_u1.objetivos.add(
        objetivo4_1,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_8,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    octavo_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_8,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    octavo_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_8,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    octavo_egb_u4.objetivos.add(
        objetivo4_2,
        objetivo4_3,
        objetivo4_6,
        objetivo4_8,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    # Noveno EGB
    noveno_egb_u1.objetivos.add(
        objetivo4_1,
        objetivo4_4,
        objetivo4_6,
        objetivo4_8,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    noveno_egb_u2.objetivos.add(
        objetivo4_1,
        objetivo4_4,
        objetivo4_6,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    noveno_egb_u3.objetivos.add(
        objetivo4_1,
        objetivo4_4,
        objetivo4_6,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    noveno_egb_u4.objetivos.add(
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_6,
        objetivo4_8,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    # Décimo EGB
    decimo_egb_u1.objetivos.add(
        objetivo4_1,
        objetivo4_2,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
        objetivo4_11,
    )
    decimo_egb_u2.objetivos.add(
        objetivo4_2,
        objetivo4_4,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_11,
        objetivo4_12,
    )
    decimo_egb_u3.objetivos.add(
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_6,
        objetivo4_7,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    decimo_egb_u4.objetivos.add(
        objetivo4_2,
        objetivo4_3,
        objetivo4_4,
        objetivo4_5,
        objetivo4_6,
        objetivo4_8,
        objetivo4_9,
        objetivo4_10,
        objetivo4_11,
        objetivo4_12,
    )
    # Bachillerato
    objetivo_general_1.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_2.unidades.add(
        # Primero
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_3.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_4.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_5.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_6.unidades.add(
        # Primero
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_7.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_8.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_9.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_10.unidades.add(
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )
    objetivo_general_11.unidades.add(
        # Primero
        primero_bgu_u1,
        primero_bgu_u2,
        primero_bgu_u3,
        primero_bgu_u4,
        primero_bgu_u5,
        primero_bgu_u6,
        # Segundo
        segundo_bgu_u1,
        segundo_bgu_u2,
        segundo_bgu_u3,
        segundo_bgu_u4,
        segundo_bgu_u5,
        segundo_bgu_u6,
        # Tercero
        tercero_bgu_u1,
        tercero_bgu_u2,
        tercero_bgu_u3,
        tercero_bgu_u4,
        tercero_bgu_u5,
        tercero_bgu_u6,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0066_auto_20180908_2016'),
    ]

    operations = [
        migrations.RunPython(create_unit_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
