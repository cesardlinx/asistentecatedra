from django.db import migrations


def create_unit_relationships(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Curso = apps.get_model('planificaciones', 'Curso')
    Unidad = apps.get_model('planificaciones', 'Unidad')
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Asignaturas
    historia = Asignatura.objects.get(name="Historia")
    filosofia = Asignatura.objects.get(name="Filosofía")
    ciudadania = Asignatura.objects.get(name="Educación para la Ciudadanía")
    gestion = Asignatura.objects.get(name="Emprendimiento y Gestión")

    # Cursos
    primero_bgu = Curso.objects.get(name="1° BGU")
    segundo_bgu = Curso.objects.get(name="2° BGU")
    tercero_bgu = Curso.objects.get(name="3° BGU")

    # Objetivos Historia
    objetivo_historia_5_1 = Objetivo.objects.get(codigo="O.CS.H.5.1.")
    objetivo_historia_5_2 = Objetivo.objects.get(codigo="O.CS.H.5.2.")
    objetivo_historia_5_3 = Objetivo.objects.get(codigo="O.CS.H.5.3.")
    objetivo_historia_5_4 = Objetivo.objects.get(codigo="O.CS.H.5.4.")
    objetivo_historia_5_5 = Objetivo.objects.get(codigo="O.CS.H.5.5.")
    objetivo_historia_5_6 = Objetivo.objects.get(codigo="O.CS.H.5.6.")
    objetivo_historia_5_7 = Objetivo.objects.get(codigo="O.CS.H.5.7.")
    objetivo_historia_5_8 = Objetivo.objects.get(codigo="O.CS.H.5.8.")

    # Objetivos Filosofía
    objetivo_filosofia_5_1 = Objetivo.objects.get(codigo="O.CS.F.5.1.")
    objetivo_filosofia_5_2 = Objetivo.objects.get(codigo="O.CS.F.5.2.")
    objetivo_filosofia_5_3 = Objetivo.objects.get(codigo="O.CS.F.5.3.")
    objetivo_filosofia_5_4 = Objetivo.objects.get(codigo="O.CS.F.5.4.")
    objetivo_filosofia_5_5 = Objetivo.objects.get(codigo="O.CS.F.5.5.")

    # Objetivos Educación para la Ciudadanía
    objetivo_ciudadania_5_1 = Objetivo.objects.get(codigo="O.CS.EC.5.1.")
    objetivo_ciudadania_5_2 = Objetivo.objects.get(codigo="O.CS.EC.5.2.")
    objetivo_ciudadania_5_3 = Objetivo.objects.get(codigo="O.CS.EC.5.3.")
    objetivo_ciudadania_5_4 = Objetivo.objects.get(codigo="O.CS.EC.5.4.")
    objetivo_ciudadania_5_5 = Objetivo.objects.get(codigo="O.CS.EC.5.5.")
    objetivo_ciudadania_5_6 = Objetivo.objects.get(codigo="O.CS.EC.5.6.")

    # Emprendimiento y Gestión
    objetivo_gestion_2 = ObjetivoGeneral.objects.get(codigo="OG.EG.2.")
    objetivo_gestion_3 = ObjetivoGeneral.objects.get(codigo="OG.EG.3.")
    objetivo_gestion_4 = ObjetivoGeneral.objects.get(codigo="OG.EG.4.")
    objetivo_gestion_5 = ObjetivoGeneral.objects.get(codigo="OG.EG.5.")
    objetivo_gestion_6 = ObjetivoGeneral.objects.get(codigo="OG.EG.6.")

    # Unidades Historia
    # 1° BGU
    primero_historia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=historia,
        curso=primero_bgu
    )
    primero_historia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=historia,
        curso=primero_bgu
    )
    primero_historia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=historia,
        curso=primero_bgu
    )
    primero_historia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=historia,
        curso=primero_bgu
    )
    primero_historia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=historia,
        curso=primero_bgu
    )
    primero_historia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=historia,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_historia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=historia,
        curso=segundo_bgu
    )
    segundo_historia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=historia,
        curso=segundo_bgu
    )
    segundo_historia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=historia,
        curso=segundo_bgu
    )
    segundo_historia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=historia,
        curso=segundo_bgu
    )
    segundo_historia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=historia,
        curso=segundo_bgu
    )
    segundo_historia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=historia,
        curso=segundo_bgu
    )
    # 3° BGU
    tercero_historia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=historia,
        curso=tercero_bgu
    )
    tercero_historia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=historia,
        curso=tercero_bgu
    )
    tercero_historia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=historia,
        curso=tercero_bgu
    )
    tercero_historia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=historia,
        curso=tercero_bgu
    )
    tercero_historia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=historia,
        curso=tercero_bgu
    )
    tercero_historia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=historia,
        curso=tercero_bgu
    )

    # Unidades Filosofía
    # 1° BGU
    primero_filosofia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=filosofia,
        curso=primero_bgu
    )
    primero_filosofia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=filosofia,
        curso=primero_bgu
    )
    primero_filosofia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=filosofia,
        curso=primero_bgu
    )
    primero_filosofia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=filosofia,
        curso=primero_bgu
    )
    primero_filosofia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=filosofia,
        curso=primero_bgu
    )
    primero_filosofia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=filosofia,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_filosofia_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=filosofia,
        curso=segundo_bgu
    )
    segundo_filosofia_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=filosofia,
        curso=segundo_bgu
    )
    segundo_filosofia_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=filosofia,
        curso=segundo_bgu
    )
    segundo_filosofia_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=filosofia,
        curso=segundo_bgu
    )
    segundo_filosofia_u5 = Unidad.objects.get(
        numero_unidad=5,
        asignatura=filosofia,
        curso=segundo_bgu
    )
    segundo_filosofia_u6 = Unidad.objects.get(
        numero_unidad=6,
        asignatura=filosofia,
        curso=segundo_bgu
    )

    # Unidades Educación para la Ciudadanía
    # 1° BGU
    primero_ciudadania_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciudadania,
        curso=primero_bgu
    )
    primero_ciudadania_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciudadania,
        curso=primero_bgu
    )
    primero_ciudadania_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciudadania,
        curso=primero_bgu
    )
    primero_ciudadania_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciudadania,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_ciudadania_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=ciudadania,
        curso=segundo_bgu
    )
    segundo_ciudadania_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=ciudadania,
        curso=segundo_bgu
    )
    segundo_ciudadania_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=ciudadania,
        curso=segundo_bgu
    )
    segundo_ciudadania_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=ciudadania,
        curso=segundo_bgu
    )

    # Unidades Emprendimiento
    # 1° BGU
    primero_gestion_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=gestion,
        curso=primero_bgu
    )
    primero_gestion_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=gestion,
        curso=primero_bgu
    )
    primero_gestion_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=gestion,
        curso=primero_bgu
    )
    primero_gestion_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=gestion,
        curso=primero_bgu
    )
    # 2° BGU
    segundo_gestion_u1 = Unidad.objects.get(
        numero_unidad=1,
        asignatura=gestion,
        curso=segundo_bgu
    )
    segundo_gestion_u2 = Unidad.objects.get(
        numero_unidad=2,
        asignatura=gestion,
        curso=segundo_bgu
    )
    segundo_gestion_u3 = Unidad.objects.get(
        numero_unidad=3,
        asignatura=gestion,
        curso=segundo_bgu
    )
    segundo_gestion_u4 = Unidad.objects.get(
        numero_unidad=4,
        asignatura=gestion,
        curso=segundo_bgu
    )

    # Asignación de objetivos a unidades

    # Historia
    objetivo_historia_5_1.unidades.add(
        # Primero
        primero_historia_u3,
        primero_historia_u4,
        primero_historia_u5,
        primero_historia_u6,
        # Tercero
        tercero_historia_u4,
    )
    objetivo_historia_5_2.unidades.add(
        # Primero
        primero_historia_u1,
        primero_historia_u2,
        primero_historia_u3,
        primero_historia_u4,
        primero_historia_u5,
        primero_historia_u6,
        # Tercero
        tercero_historia_u1,
        tercero_historia_u2,
        tercero_historia_u3,
        tercero_historia_u4,
        tercero_historia_u5,
    )
    objetivo_historia_5_3.unidades.add(
        # Primero
        primero_historia_u1,
        primero_historia_u2,
        # Segundo
        segundo_historia_u1,
        segundo_historia_u2,
        segundo_historia_u3,
    )
    objetivo_historia_5_4.unidades.add(
        # Primero
        primero_historia_u3,
        primero_historia_u4,
        primero_historia_u5,
        primero_historia_u6,
        # Segundo
        segundo_historia_u2,
        segundo_historia_u3,
        # Tercero
        tercero_historia_u3,
        tercero_historia_u4,
    )
    objetivo_historia_5_5.unidades.add(
        # Tercero
        tercero_historia_u5,
    )
    objetivo_historia_5_6.unidades.add(
        # Segundo
        segundo_historia_u1,
        segundo_historia_u2,
        segundo_historia_u4,
        segundo_historia_u5,
        segundo_historia_u6,
        # Tercero
        tercero_historia_u6,
    )
    objetivo_historia_5_7.unidades.add(
        # Primero
        primero_historia_u1,
        primero_historia_u2,
        primero_historia_u3,
        primero_historia_u4,
        primero_historia_u5,
        # Segundo
        segundo_historia_u3,
        # Tercero
        tercero_historia_u4,
    )
    objetivo_historia_5_8.unidades.add(
        # Segundo
        segundo_historia_u1,
        segundo_historia_u2,
        segundo_historia_u3,
        segundo_historia_u4,
        segundo_historia_u5,
        segundo_historia_u6,
    )

    # Filosofía
    objetivo_filosofia_5_1.unidades.add(
        # Primero
        primero_filosofia_u1,
        primero_filosofia_u2,
        primero_filosofia_u3,
        primero_filosofia_u4,
        primero_filosofia_u5,
        primero_filosofia_u6,
        # Segundo
        segundo_filosofia_u1,
        segundo_filosofia_u2,
        segundo_filosofia_u3,
        segundo_filosofia_u4,
        segundo_filosofia_u5,
        segundo_filosofia_u6,
    )
    objetivo_filosofia_5_2.unidades.add(
        # Primero
        primero_filosofia_u1,
        primero_filosofia_u2,
        primero_filosofia_u3,
        primero_filosofia_u4,
        primero_filosofia_u5,
        primero_filosofia_u6,
        # Segundo
        segundo_filosofia_u1,
        segundo_filosofia_u2,
        segundo_filosofia_u3,
        segundo_filosofia_u4,
        segundo_filosofia_u5,
        segundo_filosofia_u6,
    )
    objetivo_filosofia_5_3.unidades.add(
        # Primero
        primero_filosofia_u1,
        primero_filosofia_u2,
        primero_filosofia_u3,
        primero_filosofia_u4,
        primero_filosofia_u5,
        primero_filosofia_u6,
        # Segundo
        segundo_filosofia_u1,
        segundo_filosofia_u2,
        segundo_filosofia_u3,
        segundo_filosofia_u4,
        segundo_filosofia_u5,
        segundo_filosofia_u6,
    )
    objetivo_filosofia_5_4.unidades.add(
        # Primero
        primero_filosofia_u1,
        primero_filosofia_u2,
        primero_filosofia_u3,
        primero_filosofia_u4,
        primero_filosofia_u5,
        primero_filosofia_u6,
        # Segundo
        segundo_filosofia_u1,
        segundo_filosofia_u2,
        segundo_filosofia_u3,
        segundo_filosofia_u4,
        segundo_filosofia_u5,
        segundo_filosofia_u6,
    )
    objetivo_filosofia_5_5.unidades.add(
        # Primero
        primero_filosofia_u1,
        primero_filosofia_u2,
        primero_filosofia_u3,
        primero_filosofia_u4,
        primero_filosofia_u5,
        primero_filosofia_u6,
        # Segundo
        segundo_filosofia_u1,
        segundo_filosofia_u2,
        segundo_filosofia_u3,
        segundo_filosofia_u4,
        segundo_filosofia_u5,
        segundo_filosofia_u6,
    )

    # Educación para la Ciudadanía
    # Primero BGU
    primero_ciudadania_u1.objetivos.add(
        objetivo_ciudadania_5_1,
        objetivo_ciudadania_5_2,
    )
    primero_ciudadania_u2.objetivos.add(
        objetivo_ciudadania_5_2,
        objetivo_ciudadania_5_5,
    )
    primero_ciudadania_u3.objetivos.add(
        objetivo_ciudadania_5_5,
        objetivo_ciudadania_5_6,
    )
    primero_ciudadania_u4.objetivos.add(
        objetivo_ciudadania_5_3,
        objetivo_ciudadania_5_6,
    )
    # Segundo BGU
    segundo_ciudadania_u1.objetivos.add(
        objetivo_ciudadania_5_2,
        objetivo_ciudadania_5_3,
        objetivo_ciudadania_5_4,
    )
    segundo_ciudadania_u2.objetivos.add(
        objetivo_ciudadania_5_3,
        objetivo_ciudadania_5_5,
    )
    segundo_ciudadania_u3.objetivos.add(
        objetivo_ciudadania_5_3,
        objetivo_ciudadania_5_5,
    )
    segundo_ciudadania_u4.objetivos.add(
        objetivo_ciudadania_5_2,
        objetivo_ciudadania_5_6,
    )

    # Emprendimiento y Gestión
    # Primero BGU
    primero_gestion_u1.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_3,
    )
    primero_gestion_u2.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_3,
    )
    primero_gestion_u3.objetivos_generales.add(
        objetivo_gestion_4,
    )
    primero_gestion_u4.objetivos_generales.add(
        objetivo_gestion_4,
    )
    # Segundo BGU
    segundo_gestion_u1.objetivos_generales.add(
        objetivo_gestion_5,

    )
    segundo_gestion_u2.objetivos_generales.add(
        objetivo_gestion_5,
    )
    segundo_gestion_u3.objetivos_generales.add(
        objetivo_gestion_6,
    )
    segundo_gestion_u4.objetivos_generales.add(
        objetivo_gestion_6,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0054_auto_20180929_2047'),
    ]

    operations = [
        migrations.RunPython(create_unit_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
