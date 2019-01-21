from django.db import migrations


def create_unit_relationships(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Curso = apps.get_model('planificaciones', 'Curso')
    Unidad = apps.get_model('planificaciones', 'Unidad')
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Asignaturas
    fisica = Asignatura.objects.get(name="Física")
    quimica = Asignatura.objects.get(name="Química")
    biologia = Asignatura.objects.get(name="Biología")

    # Cursos
    primero_bgu = Curso.objects.get(name="1° BGU")
    tercero_bgu = Curso.objects.get(name="2° BGU")
    segundo_bgu = Curso.objects.get(name="3° BGU")

    # Objetivos Física
    objetivo_fisica_5_1 = Objetivo.objects.get(codigo="O.CN.F.5.1.")
    objetivo_fisica_5_2 = Objetivo.objects.get(codigo="O.CN.F.5.2.")
    objetivo_fisica_5_3 = Objetivo.objects.get(codigo="O.CN.F.5.3.")
    objetivo_fisica_5_4 = Objetivo.objects.get(codigo="O.CN.F.5.4.")
    objetivo_fisica_5_5 = Objetivo.objects.get(codigo="O.CN.F.5.5.")
    objetivo_fisica_5_6 = Objetivo.objects.get(codigo="O.CN.F.5.6.")
    objetivo_fisica_5_7 = Objetivo.objects.get(codigo="O.CN.F.5.7.")
    objetivo_fisica_5_8 = Objetivo.objects.get(codigo="O.CN.F.5.8.")
    objetivo_fisica_5_9 = Objetivo.objects.get(codigo="O.CN.F.5.9.")

    # Objetivos Biología
    objetivo_biologia_5_1 = Objetivo.objects.get(codigo="O.CN.B.5.1.")
    objetivo_biologia_5_3 = Objetivo.objects.get(codigo="O.CN.B.5.3.")
    objetivo_biologia_5_4 = Objetivo.objects.get(codigo="O.CN.B.5.4.")
    objetivo_biologia_5_5 = Objetivo.objects.get(codigo="O.CN.B.5.5.")
    objetivo_biologia_5_6 = Objetivo.objects.get(codigo="O.CN.B.5.6.")
    objetivo_biologia_5_8 = Objetivo.objects.get(codigo="O.CN.B.5.8.")
    objetivo_biologia_5_10 = Objetivo.objects.get(codigo="O.CN.B.5.10.")
    objetivo_biologia_5_11 = Objetivo.objects.get(codigo="O.CN.B.5.11.")

    # Objetivos Química
    objetivo_quimica_5_2 = Objetivo.objects.get(codigo="O.CN.Q.5.2.")
    objetivo_quimica_5_3 = Objetivo.objects.get(codigo="O.CN.Q.5.3.")
    objetivo_quimica_5_4 = Objetivo.objects.get(codigo="O.CN.Q.5.4.")
    objetivo_quimica_5_5 = Objetivo.objects.get(codigo="O.CN.Q.5.5.")
    objetivo_quimica_5_6 = Objetivo.objects.get(codigo="O.CN.Q.5.6.")
    objetivo_quimica_5_7 = Objetivo.objects.get(codigo="O.CN.Q.5.7.")
    objetivo_quimica_5_8 = Objetivo.objects.get(codigo="O.CN.Q.5.8.")
    objetivo_quimica_5_9 = Objetivo.objects.get(codigo="O.CN.Q.5.9.")
    objetivo_quimica_5_10 = Objetivo.objects.get(codigo="O.CN.Q.5.10.")
    objetivo_quimica_5_11 = Objetivo.objects.get(codigo="O.CN.Q.5.11.")

    # Objetivos generales
    objetivo_general_1 = ObjetivoGeneral.objects.get(codigo="OG.CN.1.")
    objetivo_general_2 = ObjetivoGeneral.objects.get(codigo="OG.CN.2.")
    objetivo_general_3 = ObjetivoGeneral.objects.get(codigo="OG.CN.3.")
    objetivo_general_4 = ObjetivoGeneral.objects.get(codigo="OG.CN.4.")
    objetivo_general_5 = ObjetivoGeneral.objects.get(codigo="OG.CN.5.")
    objetivo_general_6 = ObjetivoGeneral.objects.get(codigo="OG.CN.6.")
    objetivo_general_7 = ObjetivoGeneral.objects.get(codigo="OG.CN.7.")
    objetivo_general_8 = ObjetivoGeneral.objects.get(codigo="OG.CN.8.")
    objetivo_general_9 = ObjetivoGeneral.objects.get(codigo="OG.CN.9.")
    objetivo_general_10 = ObjetivoGeneral.objects.get(codigo="OG.CN.10.")

    # Unidades Física
    # 1° BGU
    primero_fisica_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=fisica,
        curso=primero_bgu
    )
    primero_fisica_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=fisica,
        curso=primero_bgu
    )
    primero_fisica_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=fisica,
        curso=primero_bgu
    )
    primero_fisica_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=fisica,
        curso=primero_bgu
    )
    primero_fisica_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=fisica,
        curso=primero_bgu
    )
    primero_fisica_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=fisica,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_fisica_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=fisica,
        curso=segundo_bgu
    )
    segundo_fisica_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=fisica,
        curso=segundo_bgu
    )
    segundo_fisica_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=fisica,
        curso=segundo_bgu
    )
    segundo_fisica_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=fisica,
        curso=segundo_bgu
    )
    segundo_fisica_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=fisica,
        curso=segundo_bgu
    )
    segundo_fisica_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=fisica,
        curso=segundo_bgu
    )
    # 3° BGU
    tercero_fisica_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=fisica,
        curso=tercero_bgu
    )
    tercero_fisica_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=fisica,
        curso=tercero_bgu
    )
    tercero_fisica_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=fisica,
        curso=tercero_bgu
    )
    tercero_fisica_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=fisica,
        curso=tercero_bgu
    )
    tercero_fisica_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=fisica,
        curso=tercero_bgu
    )
    tercero_fisica_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=fisica,
        curso=tercero_bgu
    )
    # Unidades Biología
    # 1° BGU
    primero_biologia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=biologia,
        curso=primero_bgu
    )
    primero_biologia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=biologia,
        curso=primero_bgu
    )
    primero_biologia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=biologia,
        curso=primero_bgu
    )
    primero_biologia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=biologia,
        curso=primero_bgu
    )
    primero_biologia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=biologia,
        curso=primero_bgu
    )
    primero_biologia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=biologia,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_biologia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=biologia,
        curso=segundo_bgu
    )
    segundo_biologia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=biologia,
        curso=segundo_bgu
    )
    segundo_biologia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=biologia,
        curso=segundo_bgu
    )
    segundo_biologia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=biologia,
        curso=segundo_bgu
    )
    segundo_biologia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=biologia,
        curso=segundo_bgu
    )
    segundo_biologia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=biologia,
        curso=segundo_bgu
    )
    # 3° BGU
    tercero_biologia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=biologia,
        curso=tercero_bgu
    )
    tercero_biologia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=biologia,
        curso=tercero_bgu
    )
    tercero_biologia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=biologia,
        curso=tercero_bgu
    )
    tercero_biologia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=biologia,
        curso=tercero_bgu
    )
    tercero_biologia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=biologia,
        curso=tercero_bgu
    )
    tercero_biologia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=biologia,
        curso=tercero_bgu
    )
    # Unidades Química
    # 1° BGU
    primero_quimica_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=quimica,
        curso=primero_bgu
    )
    primero_quimica_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=quimica,
        curso=primero_bgu
    )
    primero_quimica_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=quimica,
        curso=primero_bgu
    )
    primero_quimica_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=quimica,
        curso=primero_bgu
    )
    primero_quimica_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=quimica,
        curso=primero_bgu
    )
    primero_quimica_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=quimica,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_quimica_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=quimica,
        curso=segundo_bgu
    )
    segundo_quimica_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=quimica,
        curso=segundo_bgu
    )
    segundo_quimica_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=quimica,
        curso=segundo_bgu
    )
    segundo_quimica_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=quimica,
        curso=segundo_bgu
    )
    segundo_quimica_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=quimica,
        curso=segundo_bgu
    )
    segundo_quimica_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=quimica,
        curso=segundo_bgu
    )
    # 3° BGU
    tercero_quimica_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=quimica,
        curso=tercero_bgu
    )
    tercero_quimica_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=quimica,
        curso=tercero_bgu
    )
    tercero_quimica_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=quimica,
        curso=tercero_bgu
    )
    tercero_quimica_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=quimica,
        curso=tercero_bgu
    )
    tercero_quimica_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=quimica,
        curso=tercero_bgu
    )
    tercero_quimica_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=quimica,
        curso=tercero_bgu
    )

    # Asignación de objetivos a unidades

    # Física
    # Primero BGU
    primero_fisica_u1.objetivos.add(
        objetivo_fisica_5_1,
        objetivo_fisica_5_2,
        objetivo_fisica_5_4,
    )
    primero_fisica_u2.objetivos.add(
        objetivo_fisica_5_5,
        objetivo_fisica_5_6,
    )
    primero_fisica_u3.objetivos.add(
        objetivo_fisica_5_3,
        objetivo_fisica_5_7,
        objetivo_fisica_5_9,
    )
    primero_fisica_u4.objetivos.add(
        objetivo_fisica_5_5,
    )
    primero_fisica_u5.objetivos.add(
        objetivo_fisica_5_2,
        objetivo_fisica_5_7,
    )
    primero_fisica_u6.objetivos.add(
        objetivo_fisica_5_3,
        objetivo_fisica_5_4,
        objetivo_fisica_5_9,
    )
    # Segundo BGU
    segundo_fisica_u1.objetivos.add(
        objetivo_fisica_5_1,
        objetivo_fisica_5_2,
        objetivo_fisica_5_4,
    )
    segundo_fisica_u2.objetivos.add(
        objetivo_fisica_5_5,
        objetivo_fisica_5_6,
    )
    segundo_fisica_u3.objetivos.add(
        objetivo_fisica_5_5,
        objetivo_fisica_5_9,
    )
    segundo_fisica_u4.objetivos.add(
        objetivo_fisica_5_5,
    )
    segundo_fisica_u5.objetivos.add(
        objetivo_fisica_5_3,
        objetivo_fisica_5_7,
        objetivo_fisica_5_9,
    )
    segundo_fisica_u6.objetivos.add(
        objetivo_fisica_5_3,
        objetivo_fisica_5_4,
        objetivo_fisica_5_9,
    )
    # Tercero BGU
    tercero_fisica_u1.objetivos.add(
        objetivo_fisica_5_2,
        objetivo_fisica_5_4,
        objetivo_fisica_5_5,
    )
    tercero_fisica_u2.objetivos.add(
        objetivo_fisica_5_5,
        objetivo_fisica_5_6,
    )
    tercero_fisica_u3.objetivos.add(
        objetivo_fisica_5_3,
        objetivo_fisica_5_7,
    )
    tercero_fisica_u4.objetivos.add(
        objetivo_fisica_5_5,
    )
    tercero_fisica_u5.objetivos.add(
        objetivo_fisica_5_6,
        objetivo_fisica_5_8,
    )
    tercero_fisica_u6.objetivos.add(
        objetivo_fisica_5_3,
        objetivo_fisica_5_8,
    )

    # Biología
    objetivo_biologia_5_1.unidades.add(
        # Tercero BGU
        tercero_biologia_u1,
        tercero_biologia_u2,
        tercero_biologia_u5,
        tercero_biologia_u6,
    )
    objetivo_biologia_5_3.unidades.add(
        # Segundo BGU
        segundo_biologia_u3,
        # Tercero BGU
        tercero_biologia_u1,
        tercero_biologia_u2,
    )
    objetivo_biologia_5_4.unidades.add(
        # Primero BGU
        primero_biologia_u3,
        primero_biologia_u4,
        # Segundo BGU
        segundo_biologia_u5,
        segundo_biologia_u6,
        # Tercero BGU
        tercero_biologia_u3,
        tercero_biologia_u4,
    )
    objetivo_biologia_5_5.unidades.add(
        # Segundo BGU
        segundo_biologia_u2,
        segundo_biologia_u3,
        # Tercero BGU
        tercero_biologia_u6,
    )
    objetivo_biologia_5_6.unidades.add(
        # Tercero BGU
        tercero_biologia_u6,
    )
    objetivo_biologia_5_8.unidades.add(
        # Primero BGU
        primero_biologia_u4,
        # Tercero BGU
        tercero_biologia_u4,
    )
    objetivo_biologia_5_10.unidades.add(
        # Tercero BGU
        tercero_biologia_u1,
        tercero_biologia_u2,
        tercero_biologia_u4,
    )
    objetivo_biologia_5_11.unidades.add(
        # Tercero BGU
        tercero_biologia_u1,
        tercero_biologia_u2,
        tercero_biologia_u6,
    )

    # Química
    objetivo_quimica_5_2.unidades.add(
        primero_quimica_u1,
    )
    objetivo_quimica_5_3.unidades.add(
        primero_quimica_u1,
    )
    objetivo_quimica_5_4.unidades.add(
        primero_quimica_u5,
    )
    objetivo_quimica_5_5.unidades.add(
        primero_quimica_u4,
    )
    objetivo_quimica_5_6.unidades.add(
        primero_quimica_u2,
    )
    objetivo_quimica_5_7.unidades.add(
        primero_quimica_u3,
        segundo_quimica_u5,
        segundo_quimica_u6,
    )
    objetivo_quimica_5_8.unidades.add(
        primero_quimica_u5,
    )
    objetivo_quimica_5_9.unidades.add(
        primero_quimica_u6,
    )
    objetivo_quimica_5_10.unidades.add(
        primero_quimica_u2,
    )
    objetivo_quimica_5_11.unidades.add(
        primero_quimica_u4,
    )

    # Objetivos Generales (Biología y Química)
    objetivo_general_1.unidades.add(
        # Primero BGU
        primero_biologia_u1,
        primero_biologia_u2,
        primero_biologia_u3,
        primero_biologia_u6,
        primero_quimica_u1,
        primero_quimica_u2,
        primero_quimica_u3,
        primero_quimica_u4,
        primero_quimica_u5,
        # Segundo BGU
        segundo_biologia_u1,
        segundo_biologia_u2,
        segundo_quimica_u1,
        segundo_quimica_u2,
        segundo_quimica_u3,
        segundo_quimica_u4,
        segundo_quimica_u5,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_quimica_u1,
        tercero_quimica_u2,
        tercero_quimica_u3,
        tercero_quimica_u4,
        tercero_quimica_u5,
        tercero_quimica_u6,

    )
    objetivo_general_2.unidades.add(
        # Primero BGU
        primero_biologia_u1,
        primero_biologia_u2,
        primero_biologia_u3,
        primero_biologia_u5,
        primero_biologia_u6,
        primero_quimica_u3,
        primero_quimica_u4,
        primero_quimica_u5,
        # Segundo BGU
        segundo_biologia_u1,
        segundo_biologia_u2,
        segundo_biologia_u3,
        segundo_biologia_u4,
        segundo_biologia_u5,
        segundo_biologia_u6,
        segundo_quimica_u1,
        segundo_quimica_u2,
        segundo_quimica_u3,
        segundo_quimica_u4,
        segundo_quimica_u5,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_biologia_u1,
        tercero_quimica_u2,
        tercero_quimica_u3,
        tercero_quimica_u5,
        tercero_quimica_u6,
    )
    objetivo_general_3.unidades.add(
        # Primero BGU
        primero_quimica_u1,
        primero_quimica_u2,
        primero_quimica_u3,
        primero_quimica_u4,
        primero_quimica_u5,
        # Segundo BGU
        segundo_quimica_u1,
        segundo_quimica_u2,
        segundo_quimica_u3,
        segundo_quimica_u4,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_quimica_u1,
        tercero_quimica_u2,
        tercero_quimica_u4,
        tercero_quimica_u5,
    )
    objetivo_general_4.unidades.add(
        # Primero BGU
        primero_biologia_u3,
        primero_biologia_u5,
        primero_quimica_u6,
        # Segundo BGU
        segundo_biologia_u5,
        segundo_biologia_u6,
        segundo_quimica_u4,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_biologia_u3,
        tercero_biologia_u5,
        tercero_quimica_u1,
        tercero_quimica_u6,
    )
    objetivo_general_5.unidades.add(
        # Primero BGU
        primero_biologia_u1,
        primero_biologia_u2,
        primero_biologia_u3,
        primero_biologia_u5,
        primero_biologia_u6,
        primero_quimica_u4,
        # Segundo BGU
        segundo_biologia_u3,
        segundo_biologia_u5,
        segundo_biologia_u6,
        segundo_quimica_u3,
        # Tercero BGU
        tercero_biologia_u3,
        tercero_biologia_u5,
        tercero_quimica_u1,
    )
    objetivo_general_6.unidades.add(
        # Primero BGU
        primero_biologia_u2,
        primero_biologia_u3,
        primero_biologia_u4,
        primero_biologia_u5,
        primero_biologia_u6,
        primero_quimica_u1,
        primero_quimica_u2,
        primero_quimica_u3,
        primero_quimica_u4,
        primero_quimica_u5,
        primero_quimica_u6,
        # Segundo BGU
        segundo_biologia_u3,
        segundo_quimica_u1,
        segundo_quimica_u2,
        segundo_quimica_u3,
        segundo_quimica_u4,
        segundo_quimica_u5,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_biologia_u2,
        tercero_biologia_u3,
        tercero_biologia_u5,
        tercero_biologia_u6,
        tercero_quimica_u1,
        tercero_quimica_u2,
        tercero_quimica_u4,
        tercero_quimica_u5,
        tercero_quimica_u6,
    )
    objetivo_general_7.unidades.add(
        # Primero BGU
        primero_biologia_u1,
        primero_biologia_u2,
        primero_biologia_u3,
        primero_biologia_u5,
        primero_biologia_u6,
        # Segundo BGU
        segundo_biologia_u1,
        segundo_biologia_u2,
        segundo_biologia_u3,
        segundo_biologia_u5,
        segundo_biologia_u6,
        # Tercero BGU
        tercero_biologia_u3,
        tercero_biologia_u5,
    )
    objetivo_general_8.unidades.add(
        # Primero BGU
        primero_biologia_u3,
        primero_biologia_u4,
        primero_biologia_u5,
        # Segundo BGU
        segundo_biologia_u1,
        segundo_biologia_u2,
        # Tercero BGU
        tercero_biologia_u3,
        tercero_biologia_u5,
    )
    objetivo_general_9.unidades.add(
        # Primero BGU
        primero_biologia_u3,
        primero_biologia_u4,
        primero_quimica_u1,
        primero_quimica_u2,
        primero_quimica_u3,
        primero_quimica_u4,
        primero_quimica_u5,
        # Segundo BGU
        segundo_quimica_u1,
        segundo_quimica_u2,
        segundo_quimica_u3,
        segundo_quimica_u4,
        segundo_quimica_u5,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_biologia_u1,
        tercero_biologia_u3,
        tercero_biologia_u6,
        tercero_quimica_u1,
        tercero_quimica_u5,
        tercero_quimica_u6,
    )
    objetivo_general_10.unidades.add(
        # Primero BGU
        primero_biologia_u5,
        primero_quimica_u1,
        primero_quimica_u2,
        primero_quimica_u3,
        primero_quimica_u4,
        # Segundo BGU
        segundo_biologia_u3,
        segundo_quimica_u1,
        segundo_quimica_u2,
        segundo_quimica_u3,
        segundo_quimica_u4,
        segundo_quimica_u5,
        segundo_quimica_u6,
        # Tercero BGU
        tercero_biologia_u1,
        tercero_biologia_u3,
        tercero_quimica_u1,
        tercero_quimica_u2,
        tercero_quimica_u3,
        tercero_quimica_u4,
        tercero_quimica_u5,
        tercero_quimica_u6,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0070_auto_20180929_1939'),
    ]

    operations = [
        migrations.RunPython(create_unit_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
