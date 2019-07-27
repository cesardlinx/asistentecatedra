from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales Emprendimiento y Gestión
    objetivo_gestion_1 = ObjetivoGeneral.objects.get(codigo="OG.EG.1.")
    objetivo_gestion_2 = ObjetivoGeneral.objects.get(codigo="OG.EG.2.")
    objetivo_gestion_3 = ObjetivoGeneral.objects.get(codigo="OG.EG.3.")
    objetivo_gestion_4 = ObjetivoGeneral.objects.get(codigo="OG.EG.4.")
    objetivo_gestion_5 = ObjetivoGeneral.objects.get(codigo="OG.EG.5.")
    objetivo_gestion_6 = ObjetivoGeneral.objects.get(codigo="OG.EG.6.")
    objetivo_gestion_7 = ObjetivoGeneral.objects.get(codigo="OG.EG.7.")
    objetivo_gestion_8 = ObjetivoGeneral.objects.get(codigo="OG.EG.8.")

    # criterios de evaluacion Emprendimiento y Gestion
    criterio_gestion_5_1 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.1.")
    criterio_gestion_5_2 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.2.")
    criterio_gestion_5_3 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.3.")
    criterio_gestion_5_4 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.4.")
    criterio_gestion_5_5 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.5.")
    criterio_gestion_5_6 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.6.")
    criterio_gestion_5_7 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.7.")
    criterio_gestion_5_8 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.8.")
    criterio_gestion_5_9 = CriterioEvaluacion.objects.get(codigo="CE.EG.5.9.")
    criterio_gestion_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.10.")
    criterio_gestion_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.11.")

    # Destrezas Gestión
    destreza_gestion_5_1_1 = Destreza.objects.get(codigo="EG.5.1.1.")
    destreza_gestion_5_1_2 = Destreza.objects.get(codigo="EG.5.1.2.")
    destreza_gestion_5_1_3 = Destreza.objects.get(codigo="EG.5.1.3.")
    destreza_gestion_5_1_4 = Destreza.objects.get(codigo="EG.5.1.4.")
    destreza_gestion_5_1_5 = Destreza.objects.get(codigo="EG.5.1.5.")
    destreza_gestion_5_1_6 = Destreza.objects.get(codigo="EG.5.1.6.")
    destreza_gestion_5_1_7 = Destreza.objects.get(codigo="EG.5.1.7.")
    destreza_gestion_5_1_8 = Destreza.objects.get(codigo="EG.5.1.8.")
    destreza_gestion_5_1_9 = Destreza.objects.get(codigo="EG.5.1.9.")
    destreza_gestion_5_1_10 = Destreza.objects.get(codigo="EG.5.1.10.")
    destreza_gestion_5_2_1 = Destreza.objects.get(codigo="EG.5.2.1.")
    destreza_gestion_5_2_2 = Destreza.objects.get(codigo="EG.5.2.2.")
    destreza_gestion_5_2_3 = Destreza.objects.get(codigo="EG.5.2.3.")
    destreza_gestion_5_2_4 = Destreza.objects.get(codigo="EG.5.2.4.")
    destreza_gestion_5_3_1 = Destreza.objects.get(codigo="EG.5.3.1.")
    destreza_gestion_5_3_2 = Destreza.objects.get(codigo="EG.5.3.2.")
    destreza_gestion_5_3_3 = Destreza.objects.get(codigo="EG.5.3.3.")
    destreza_gestion_5_3_4 = Destreza.objects.get(codigo="EG.5.3.4.")
    destreza_gestion_5_3_5 = Destreza.objects.get(codigo="EG.5.3.5.")
    destreza_gestion_5_3_6 = Destreza.objects.get(codigo="EG.5.3.6.")
    destreza_gestion_5_3_7 = Destreza.objects.get(codigo="EG.5.3.7.")
    destreza_gestion_5_3_8 = Destreza.objects.get(codigo="EG.5.3.8.")
    destreza_gestion_5_4_1 = Destreza.objects.get(codigo="EG.5.4.1.")
    destreza_gestion_5_4_2 = Destreza.objects.get(codigo="EG.5.4.2.")
    destreza_gestion_5_4_3 = Destreza.objects.get(codigo="EG.5.4.3.")
    destreza_gestion_5_4_4 = Destreza.objects.get(codigo="EG.5.4.4.")
    destreza_gestion_5_4_5 = Destreza.objects.get(codigo="EG.5.4.5.")
    destreza_gestion_5_4_6 = Destreza.objects.get(codigo="EG.5.4.6.")
    destreza_gestion_5_5_1 = Destreza.objects.get(codigo="EG.5.5.1.")
    destreza_gestion_5_5_2 = Destreza.objects.get(codigo="EG.5.5.2.")
    destreza_gestion_5_5_3 = Destreza.objects.get(codigo="EG.5.5.3.")
    destreza_gestion_5_5_4 = Destreza.objects.get(codigo="EG.5.5.4.")
    destreza_gestion_5_5_4_1 = Destreza.objects.get(codigo="EG.5.5.4.1.")
    destreza_gestion_5_5_5 = Destreza.objects.get(codigo="EG.5.5.5.")
    destreza_gestion_5_5_6 = Destreza.objects.get(codigo="EG.5.5.6.")
    destreza_gestion_5_5_7 = Destreza.objects.get(codigo="EG.5.5.7.")
    destreza_gestion_5_5_8 = Destreza.objects.get(codigo="EG.5.5.8.")
    destreza_gestion_5_5_9 = Destreza.objects.get(codigo="EG.5.5.9.")
    destreza_gestion_5_5_10 = Destreza.objects.get(codigo="EG.5.5.10.")
    destreza_gestion_5_5_11 = Destreza.objects.get(codigo="EG.5.5.11.")
    destreza_gestion_5_5_12 = Destreza.objects.get(codigo="EG.5.5.12.")
    destreza_gestion_5_5_11 = Destreza.objects.get(codigo="EG.5.5.11.")
    destreza_gestion_5_5_12 = Destreza.objects.get(codigo="EG.5.5.12.")
    destreza_gestion_5_5_13 = Destreza.objects.get(codigo="EG.5.5.13.")
    destreza_gestion_5_5_14 = Destreza.objects.get(codigo="EG.5.5.14.")
    destreza_gestion_5_5_15 = Destreza.objects.get(codigo="EG.5.5.15.")
    destreza_gestion_5_5_16 = Destreza.objects.get(codigo="EG.5.5.16.")
    destreza_gestion_5_6_1 = Destreza.objects.get(codigo="EG.5.6.1.")
    destreza_gestion_5_6_1_1 = Destreza.objects.get(codigo="EG.5.6.1.1.")
    destreza_gestion_5_6_2 = Destreza.objects.get(codigo="EG.5.6.2.")

    # Emprendimiento y Gestión
    criterio_gestion_5_1.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_3,
        objetivo_gestion_4,
        objetivo_gestion_8,
    )
    criterio_gestion_5_1.destrezas.add(
        destreza_gestion_5_1_1,
        destreza_gestion_5_1_2,
    )

    criterio_gestion_5_2.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_3,
        objetivo_gestion_4,
        objetivo_gestion_8,
    )
    criterio_gestion_5_2.destrezas.add(
        destreza_gestion_5_1_3,
        destreza_gestion_5_1_4,
        destreza_gestion_5_1_5,
        destreza_gestion_5_1_6,
        destreza_gestion_5_1_7,
        destreza_gestion_5_1_8,
        destreza_gestion_5_1_9,
        destreza_gestion_5_1_10,
    )

    criterio_gestion_5_3.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_4,
    )
    criterio_gestion_5_3.destrezas.add(
        destreza_gestion_5_2_1,
        destreza_gestion_5_2_2,
        destreza_gestion_5_2_3,
        destreza_gestion_5_2_4,
    )

    criterio_gestion_5_4.objetivos_generales.add(
        objetivo_gestion_5,
        objetivo_gestion_7,
        objetivo_gestion_8,
    )
    criterio_gestion_5_4.destrezas.add(
        destreza_gestion_5_3_1,
        destreza_gestion_5_3_2,
        destreza_gestion_5_3_3,
        destreza_gestion_5_3_4,
        destreza_gestion_5_5_1,
        destreza_gestion_5_5_8,
        destreza_gestion_5_6_2,
    )

    criterio_gestion_5_5.objetivos_generales.add(
        objetivo_gestion_1,
        objetivo_gestion_7,
        objetivo_gestion_8,
    )
    criterio_gestion_5_5.destrezas.add(
        destreza_gestion_5_3_5,
        destreza_gestion_5_3_6,
        destreza_gestion_5_3_7,
        destreza_gestion_5_3_8,
    )

    criterio_gestion_5_6.objetivos_generales.add(
        objetivo_gestion_1,
        objetivo_gestion_4,
        objetivo_gestion_6,
        objetivo_gestion_7,
        objetivo_gestion_8,
    )
    criterio_gestion_5_6.destrezas.add(
        destreza_gestion_5_4_1,
        destreza_gestion_5_4_2,
        destreza_gestion_5_4_3,
        destreza_gestion_5_5_3,
    )

    criterio_gestion_5_7.objetivos_generales.add(
        objetivo_gestion_6,
        objetivo_gestion_7,
        objetivo_gestion_8,
    )
    criterio_gestion_5_7.destrezas.add(
        destreza_gestion_5_4_4,
        destreza_gestion_5_4_5,
        destreza_gestion_5_4_6,
    )

    criterio_gestion_5_8.objetivos_generales.add(
        objetivo_gestion_5,
        objetivo_gestion_7,
        objetivo_gestion_8,
    )
    criterio_gestion_5_8.destrezas.add(
        destreza_gestion_5_5_2,
        destreza_gestion_5_5_9,
        destreza_gestion_5_5_10,
    )

    criterio_gestion_5_9.objetivos_generales.add(
        objetivo_gestion_7,
        objetivo_gestion_8,
    )
    criterio_gestion_5_9.destrezas.add(
        destreza_gestion_5_5_4,
        destreza_gestion_5_5_4_1,
        destreza_gestion_5_5_5,
        destreza_gestion_5_5_6,
        destreza_gestion_5_5_7,
    )

    criterio_gestion_5_10.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_3,
        objetivo_gestion_4,
        objetivo_gestion_8,
    )
    criterio_gestion_5_10.destrezas.add(
        destreza_gestion_5_5_11,
        destreza_gestion_5_5_12,
        destreza_gestion_5_5_13,
        destreza_gestion_5_5_14,
        destreza_gestion_5_5_15,
        destreza_gestion_5_5_16,
    )

    criterio_gestion_5_11.objetivos_generales.add(
        objetivo_gestion_2,
        objetivo_gestion_3,
        objetivo_gestion_4,
        objetivo_gestion_8,
    )
    criterio_gestion_5_11.destrezas.add(
        destreza_gestion_5_6_1,
        destreza_gestion_5_6_1_1,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0048_auto_20180908_2013'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
