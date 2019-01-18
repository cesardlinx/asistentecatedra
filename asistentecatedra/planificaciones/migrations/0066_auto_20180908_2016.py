from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales Lengua Extranjera
    objetivo_ingles_1 = ObjetivoGeneral.objects.get(codigo="OG.EFL.1.")
    objetivo_ingles_2 = ObjetivoGeneral.objects.get(codigo="OG.EFL.2.")
    objetivo_ingles_3 = ObjetivoGeneral.objects.get(codigo="OG.EFL.3.")
    objetivo_ingles_4 = ObjetivoGeneral.objects.get(codigo="OG.EFL.4.")
    objetivo_ingles_5 = ObjetivoGeneral.objects.get(codigo="OG.EFL.5.")
    objetivo_ingles_6 = ObjetivoGeneral.objects.get(codigo="OG.EFL.6.")
    objetivo_ingles_7 = ObjetivoGeneral.objects.get(codigo="OG.EFL.7.")

    # Objetivos Generales Emprendimiento y Gestión
    objetivo_gestion_1 = ObjetivoGeneral.objects.get(codigo="OG.EG.1.")
    objetivo_gestion_2 = ObjetivoGeneral.objects.get(codigo="OG.EG.2.")
    objetivo_gestion_3 = ObjetivoGeneral.objects.get(codigo="OG.EG.3.")
    objetivo_gestion_4 = ObjetivoGeneral.objects.get(codigo="OG.EG.4.")
    objetivo_gestion_5 = ObjetivoGeneral.objects.get(codigo="OG.EG.5.")
    objetivo_gestion_6 = ObjetivoGeneral.objects.get(codigo="OG.EG.6.")
    objetivo_gestion_7 = ObjetivoGeneral.objects.get(codigo="OG.EG.7.")
    objetivo_gestion_8 = ObjetivoGeneral.objects.get(codigo="OG.EG.8.")

    # Criterios de evaluación
    criterio_ingles_1_1 = CriterioEvaluacion.objects.get(codigo="CE.EFL.1.1.")
    criterio_ingles_1_2 = CriterioEvaluacion.objects.get(codigo="CE.EFL.1.2.")
    criterio_ingles_2_1 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.1.")
    criterio_ingles_2_2 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.2.")
    criterio_ingles_2_3 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.3.")
    criterio_ingles_2_4 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.4.")
    criterio_ingles_2_5 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.5.")
    criterio_ingles_2_6 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.6.")
    criterio_ingles_2_7 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.7.")
    criterio_ingles_2_8 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.8.")
    criterio_ingles_2_9 = CriterioEvaluacion.objects.get(codigo="CE.EFL.2.9.")
    criterio_ingles_2_10 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.10.")
    criterio_ingles_2_11 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.11.")
    criterio_ingles_2_12 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.12.")
    criterio_ingles_2_13 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.13.")
    criterio_ingles_2_14 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.14.")
    criterio_ingles_2_15 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.15.")
    criterio_ingles_2_16 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.16.")
    criterio_ingles_2_17 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.17.")
    criterio_ingles_2_18 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.18.")
    criterio_ingles_2_19 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.19.")
    criterio_ingles_2_20 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.20.")
    criterio_ingles_2_21 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.21.")
    criterio_ingles_2_22 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.22.")
    criterio_ingles_2_23 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.23.")
    criterio_ingles_2_24 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.24.")
    criterio_ingles_2_25 = CriterioEvaluacion.objects.get(
        codigo="CE.EFL.2.25.")
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

    # Destrezas Inglés
    destreza_ingles_1_1_1 = Destreza.objects.get(codigo="EFL.1.1.1.")
    destreza_ingles_1_1_2 = Destreza.objects.get(codigo="EFL.1.1.2.")
    destreza_ingles_1_1_3 = Destreza.objects.get(codigo="EFL.1.1.3.")
    destreza_ingles_1_2_1 = Destreza.objects.get(codigo="EFL.1.2.1.")
    destreza_ingles_1_2_2 = Destreza.objects.get(codigo="EFL.1.2.2.")
    destreza_ingles_1_3_1 = Destreza.objects.get(codigo="EFL.1.3.1.")
    destreza_ingles_1_3_2 = Destreza.objects.get(codigo="EFL.1.3.2.")
    destreza_ingles_1_3_3 = Destreza.objects.get(codigo="EFL.1.3.3.")
    destreza_ingles_1_4_1 = Destreza.objects.get(codigo="EFL.1.4.1.")
    destreza_ingles_1_4_2 = Destreza.objects.get(codigo="EFL.1.4.2.")
    destreza_ingles_1_5_1 = Destreza.objects.get(codigo="EFL.1.5.1.")
    destreza_ingles_1_5_2 = Destreza.objects.get(codigo="EFL.1.5.2.")
    destreza_ingles_1_5_3 = Destreza.objects.get(codigo="EFL.1.5.3.")
    destreza_ingles_1_5_4 = Destreza.objects.get(codigo="EFL.1.5.4.")
    destreza_ingles_1_6_1 = Destreza.objects.get(codigo="EFL.1.6.1.")
    destreza_ingles_1_6_2 = Destreza.objects.get(codigo="EFL.1.6.2.")
    destreza_ingles_1_6_3 = Destreza.objects.get(codigo="EFL.1.6.3.")
    destreza_ingles_1_7_1 = Destreza.objects.get(codigo="EFL.1.7.1.")
    destreza_ingles_1_7_2 = Destreza.objects.get(codigo="EFL.1.7.2.")
    destreza_ingles_1_7_3 = Destreza.objects.get(codigo="EFL.1.7.3.")
    destreza_ingles_2_1_1 = Destreza.objects.get(codigo="EFL.2.1.1.")
    destreza_ingles_2_1_2 = Destreza.objects.get(codigo="EFL.2.1.2.")
    destreza_ingles_2_1_3 = Destreza.objects.get(codigo="EFL.2.1.3.")
    destreza_ingles_2_1_4 = Destreza.objects.get(codigo="EFL.2.1.4.")
    destreza_ingles_2_1_5 = Destreza.objects.get(codigo="EFL.2.1.5.")
    destreza_ingles_2_1_6 = Destreza.objects.get(codigo="EFL.2.1.6.")
    destreza_ingles_2_1_7 = Destreza.objects.get(codigo="EFL.2.1.7.")
    destreza_ingles_2_1_8 = Destreza.objects.get(codigo="EFL.2.1.8.")
    destreza_ingles_2_1_9 = Destreza.objects.get(codigo="EFL.2.1.9.")
    destreza_ingles_2_1_10 = Destreza.objects.get(codigo="EFL.2.1.10.")
    destreza_ingles_2_2_1 = Destreza.objects.get(codigo="EFL.2.2.1.")
    destreza_ingles_2_2_2 = Destreza.objects.get(codigo="EFL.2.2.2.")
    destreza_ingles_2_2_3 = Destreza.objects.get(codigo="EFL.2.2.3.")
    destreza_ingles_2_2_4 = Destreza.objects.get(codigo="EFL.2.2.4.")
    destreza_ingles_2_2_5 = Destreza.objects.get(codigo="EFL.2.2.5.")
    destreza_ingles_2_2_6 = Destreza.objects.get(codigo="EFL.2.2.6.")
    destreza_ingles_2_2_7 = Destreza.objects.get(codigo="EFL.2.2.7.")
    destreza_ingles_2_2_8 = Destreza.objects.get(codigo="EFL.2.2.8.")
    destreza_ingles_2_2_9 = Destreza.objects.get(codigo="EFL.2.2.9.")
    destreza_ingles_2_2_10 = Destreza.objects.get(codigo="EFL.2.2.10.")
    destreza_ingles_2_2_11 = Destreza.objects.get(codigo="EFL.2.2.11.")
    destreza_ingles_2_2_12 = Destreza.objects.get(codigo="EFL.2.2.12.")
    destreza_ingles_2_2_13 = Destreza.objects.get(codigo="EFL.2.2.13.")
    destreza_ingles_2_2_14 = Destreza.objects.get(codigo="EFL.2.2.14.")
    destreza_ingles_2_2_15 = Destreza.objects.get(codigo="EFL.2.2.15.")
    destreza_ingles_2_2_16 = Destreza.objects.get(codigo="EFL.2.2.16.")
    destreza_ingles_2_2_17 = Destreza.objects.get(codigo="EFL.2.2.17.")
    destreza_ingles_2_3_1 = Destreza.objects.get(codigo="EFL.2.3.1.")
    destreza_ingles_2_3_2 = Destreza.objects.get(codigo="EFL.2.3.2.")
    destreza_ingles_2_3_3 = Destreza.objects.get(codigo="EFL.2.3.3.")
    destreza_ingles_2_3_4 = Destreza.objects.get(codigo="EFL.2.3.4.")
    destreza_ingles_2_3_5 = Destreza.objects.get(codigo="EFL.2.3.5.")
    destreza_ingles_2_3_6 = Destreza.objects.get(codigo="EFL.2.3.6.")
    destreza_ingles_2_3_7 = Destreza.objects.get(codigo="EFL.2.3.7.")
    destreza_ingles_2_3_8 = Destreza.objects.get(codigo="EFL.2.3.8.")
    destreza_ingles_2_3_9 = Destreza.objects.get(codigo="EFL.2.3.9.")
    destreza_ingles_2_3_10 = Destreza.objects.get(codigo="EFL.2.3.10.")
    destreza_ingles_2_4_1 = Destreza.objects.get(codigo="EFL.2.4.1.")
    destreza_ingles_2_4_2 = Destreza.objects.get(codigo="EFL.2.4.2.")
    destreza_ingles_2_4_3 = Destreza.objects.get(codigo="EFL.2.4.3.")
    destreza_ingles_2_4_4 = Destreza.objects.get(codigo="EFL.2.4.4.")
    destreza_ingles_2_4_5 = Destreza.objects.get(codigo="EFL.2.4.5.")
    destreza_ingles_2_4_6 = Destreza.objects.get(codigo="EFL.2.4.6.")
    destreza_ingles_2_4_7 = Destreza.objects.get(codigo="EFL.2.4.7.")
    destreza_ingles_2_4_8 = Destreza.objects.get(codigo="EFL.2.4.8.")
    destreza_ingles_2_4_9 = Destreza.objects.get(codigo="EFL.2.4.9.")
    destreza_ingles_2_5_1 = Destreza.objects.get(codigo="EFL.2.5.1.")
    destreza_ingles_2_5_2 = Destreza.objects.get(codigo="EFL.2.5.2.")
    destreza_ingles_2_5_3 = Destreza.objects.get(codigo="EFL.2.5.3.")
    destreza_ingles_2_5_4 = Destreza.objects.get(codigo="EFL.2.5.4.")
    destreza_ingles_2_5_5 = Destreza.objects.get(codigo="EFL.2.5.5.")
    destreza_ingles_2_5_6 = Destreza.objects.get(codigo="EFL.2.5.6.")
    destreza_ingles_2_5_7 = Destreza.objects.get(codigo="EFL.2.5.7.")
    destreza_ingles_2_5_8 = Destreza.objects.get(codigo="EFL.2.5.8.")
    destreza_ingles_2_5_9 = Destreza.objects.get(codigo="EFL.2.5.9.")

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

    # Inglés
    # Preparatoria
    criterio_ingles_1_1.objetivos_generales.add(
        objetivo_ingles_3,
    )
    criterio_ingles_1_1.destrezas.add(
        destreza_ingles_1_1_2,
        destreza_ingles_1_2_1,
        destreza_ingles_1_2_2,
        destreza_ingles_1_3_1,
        destreza_ingles_1_3_2,
        destreza_ingles_1_3_3,
        destreza_ingles_1_4_1,
        destreza_ingles_1_4_2,
        destreza_ingles_1_6_1,
        destreza_ingles_1_7_1,
    )

    criterio_ingles_1_2.objetivos_generales.add(
        objetivo_ingles_4,
        objetivo_ingles_6,
    )
    criterio_ingles_1_2.destrezas.add(
        destreza_ingles_1_1_1,
        destreza_ingles_1_1_3,
        destreza_ingles_1_5_1,
        destreza_ingles_1_5_2,
        destreza_ingles_1_5_3,
        destreza_ingles_1_5_4,
        destreza_ingles_1_6_2,
        destreza_ingles_1_6_3,
        destreza_ingles_1_7_2,
        destreza_ingles_1_7_3,
    )

    # Elemental
    criterio_ingles_2_1.objetivos_generales.add(
        objetivo_ingles_2,
    )
    criterio_ingles_2_1.destrezas.add(
        destreza_ingles_2_1_2,
        destreza_ingles_2_1_3,
        destreza_ingles_2_5_4,
    )

    criterio_ingles_2_2.objetivos_generales.add(
        objetivo_ingles_3,
    )
    criterio_ingles_2_2.destrezas.add(
        destreza_ingles_2_1_4,
        destreza_ingles_2_1_5,
    )

    criterio_ingles_2_3.objetivos_generales.add(
        objetivo_ingles_4,
    )
    criterio_ingles_2_3.destrezas.add(
        destreza_ingles_2_1_1,
        destreza_ingles_2_1_6,
    )

    criterio_ingles_2_4.objetivos_generales.add(
        objetivo_ingles_4,
    )
    criterio_ingles_2_4.destrezas.add(
        destreza_ingles_2_1_7,
        destreza_ingles_2_1_8,
    )

    criterio_ingles_2_5.objetivos_generales.add(
        objetivo_ingles_3,
    )
    criterio_ingles_2_5.destrezas.add(
        destreza_ingles_2_1_9,
        destreza_ingles_2_1_10,
    )

    criterio_ingles_2_6.objetivos_generales.add(
        objetivo_ingles_1,
        objetivo_ingles_4,
        objetivo_ingles_5,
    )
    criterio_ingles_2_6.destrezas.add(
        destreza_ingles_2_2_1,
        destreza_ingles_2_2_2,
        destreza_ingles_2_2_6,
        destreza_ingles_2_2_7,
    )

    criterio_ingles_2_7.objetivos_generales.add(
        objetivo_ingles_4,
        objetivo_ingles_7,
    )
    criterio_ingles_2_7.destrezas.add(
        destreza_ingles_2_2_3,
        destreza_ingles_2_2_4,
        destreza_ingles_2_2_5,
    )

    criterio_ingles_2_8.objetivos_generales.add(
        objetivo_ingles_3,
        objetivo_ingles_7,
    )
    criterio_ingles_2_8.destrezas.add(
        destreza_ingles_2_2_8,
        destreza_ingles_2_2_9,
        destreza_ingles_2_2_10,
    )

    criterio_ingles_2_9.objetivos_generales.add(
        objetivo_ingles_6,
        objetivo_ingles_7,
    )
    criterio_ingles_2_9.destrezas.add(
        destreza_ingles_2_2_11,
        destreza_ingles_2_2_12,
    )

    criterio_ingles_2_10.objetivos_generales.add(
        objetivo_ingles_4,
        objetivo_ingles_6,
        objetivo_ingles_7,
    )
    criterio_ingles_2_10.destrezas.add(
        destreza_ingles_2_2_13,
        destreza_ingles_2_2_14,
        destreza_ingles_2_2_15,
        destreza_ingles_2_2_16,
        destreza_ingles_2_2_17,
    )

    criterio_ingles_2_11.objetivos_generales.add(
        objetivo_ingles_3,
        objetivo_ingles_5,
    )
    criterio_ingles_2_11.destrezas.add(
        destreza_ingles_2_3_1,
    )

    criterio_ingles_2_12.objetivos_generales.add(
        objetivo_ingles_3,
        objetivo_ingles_5,
    )
    criterio_ingles_2_12.destrezas.add(
        destreza_ingles_2_3_2,
        destreza_ingles_2_3_3,
    )

    criterio_ingles_2_13.objetivos_generales.add(
        objetivo_ingles_4,
        objetivo_ingles_5,
    )
    criterio_ingles_2_13.destrezas.add(
        destreza_ingles_2_3_4,
    )

    criterio_ingles_2_14.objetivos_generales.add(
        objetivo_ingles_4,
        objetivo_ingles_5,
    )
    criterio_ingles_2_14.destrezas.add(
        destreza_ingles_2_3_5,
    )

    criterio_ingles_2_15.objetivos_generales.add(
        objetivo_ingles_4,
        objetivo_ingles_6,
    )
    criterio_ingles_2_15.destrezas.add(
        destreza_ingles_2_3_6,
    )

    criterio_ingles_2_16.objetivos_generales.add(
        objetivo_ingles_2,
        objetivo_ingles_5,
    )
    criterio_ingles_2_16.destrezas.add(
        destreza_ingles_2_3_7,
        destreza_ingles_2_3_8,
        destreza_ingles_2_3_9,
        destreza_ingles_2_3_10,
    )

    criterio_ingles_2_17.objetivos_generales.add(
        objetivo_ingles_6,
    )
    criterio_ingles_2_17.destrezas.add(
        destreza_ingles_2_4_1,
        destreza_ingles_2_4_2,
        destreza_ingles_2_4_3,
    )

    criterio_ingles_2_18.objetivos_generales.add(
        objetivo_ingles_6,
    )
    criterio_ingles_2_18.destrezas.add(
        destreza_ingles_2_4_3,
        destreza_ingles_2_4_4,
    )

    criterio_ingles_2_19.objetivos_generales.add(
        objetivo_ingles_6,
    )
    criterio_ingles_2_19.destrezas.add(
        destreza_ingles_2_4_5,
        destreza_ingles_2_4_6,
        destreza_ingles_2_4_7,
    )

    criterio_ingles_2_20.objetivos_generales.add(
        objetivo_ingles_5,
    )
    criterio_ingles_2_20.destrezas.add(
        destreza_ingles_2_4_8,
        destreza_ingles_2_4_9,
    )

    criterio_ingles_2_21.objetivos_generales.add(
        objetivo_ingles_1,
    )
    criterio_ingles_2_21.destrezas.add(
        destreza_ingles_2_5_1,
    )

    criterio_ingles_2_22.objetivos_generales.add(
        objetivo_ingles_3,
        objetivo_ingles_5,
    )
    criterio_ingles_2_22.destrezas.add(
        destreza_ingles_2_5_2,
        destreza_ingles_2_5_3,
        destreza_ingles_2_5_6,
    )

    criterio_ingles_2_23.objetivos_generales.add(
        objetivo_ingles_1,
    )
    criterio_ingles_2_23.destrezas.add(
        destreza_ingles_2_5_4,
        destreza_ingles_2_5_7,
    )

    criterio_ingles_2_24.objetivos_generales.add(
        objetivo_ingles_5,
        objetivo_ingles_6,
    )
    criterio_ingles_2_24.destrezas.add(
        destreza_ingles_2_5_5,
        destreza_ingles_2_5_8,
    )

    criterio_ingles_2_25.objetivos_generales.add(
        objetivo_ingles_4,
    )
    criterio_ingles_2_25.destrezas.add(
        destreza_ingles_2_5_9,
    )

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
        ('planificaciones', '0065_auto_20180908_2013'),
    ]

    operations = [
        migrations.RunPython(create_relationships)
    ]
