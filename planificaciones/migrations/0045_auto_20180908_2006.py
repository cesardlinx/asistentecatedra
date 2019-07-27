from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')
    destreza4_1_1 = Destreza.objects.get(codigo="CN.4.1.1.")

    # Objetivos Generales
    objetivo1 = ObjetivoGeneral.objects.get(codigo="OG.CN.1.")
    objetivo2 = ObjetivoGeneral.objects.get(codigo="OG.CN.2.")
    objetivo3 = ObjetivoGeneral.objects.get(codigo="OG.CN.3.")
    objetivo4 = ObjetivoGeneral.objects.get(codigo="OG.CN.4.")
    objetivo5 = ObjetivoGeneral.objects.get(codigo="OG.CN.5.")
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.CN.6.")
    objetivo7 = ObjetivoGeneral.objects.get(codigo="OG.CN.7.")
    objetivo8 = ObjetivoGeneral.objects.get(codigo="OG.CN.8.")
    objetivo9 = ObjetivoGeneral.objects.get(codigo="OG.CN.9.")
    objetivo10 = ObjetivoGeneral.objects.get(codigo="OG.CN.10.")

    # Criterios de evaluación
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.6.")
    criterio2_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.7.")
    criterio2_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.8.")
    criterio2_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.9.")
    criterio2_10 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.10.")
    criterio2_11 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.11.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.8.")
    criterio3_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.9.")
    criterio3_10 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.10.")
    criterio3_11 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.11.")
    criterio3_12 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.12.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.8.")
    criterio4_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.9.")
    criterio4_10 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.10.")
    criterio4_11 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.11.")
    criterio4_12 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.12.")
    criterio4_13 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.13.")
    criterio4_14 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.14.")

    # Destrezas
    destreza2_1_1 = Destreza.objects.get(codigo="CN.2.1.1.")
    destreza2_1_2 = Destreza.objects.get(codigo="CN.2.1.2.")
    destreza2_1_3 = Destreza.objects.get(codigo="CN.2.1.3.")
    destreza2_1_4 = Destreza.objects.get(codigo="CN.2.1.4.")
    destreza2_1_5 = Destreza.objects.get(codigo="CN.2.1.5.")
    destreza2_1_6 = Destreza.objects.get(codigo="CN.2.1.6.")
    destreza2_1_7 = Destreza.objects.get(codigo="CN.2.1.7.")
    destreza2_1_8 = Destreza.objects.get(codigo="CN.2.1.8.")
    destreza2_1_9 = Destreza.objects.get(codigo="CN.2.1.9.")
    destreza2_1_10 = Destreza.objects.get(codigo="CN.2.1.10.")
    destreza2_1_11 = Destreza.objects.get(codigo="CN.2.1.11.")
    destreza2_1_12 = Destreza.objects.get(codigo="CN.2.1.12.")
    destreza2_2_1 = Destreza.objects.get(codigo="CN.2.2.1.")
    destreza2_2_2 = Destreza.objects.get(codigo="CN.2.2.2.")
    destreza2_2_3 = Destreza.objects.get(codigo="CN.2.2.3.")
    destreza2_2_4 = Destreza.objects.get(codigo="CN.2.2.4.")
    destreza2_2_5 = Destreza.objects.get(codigo="CN.2.2.5.")
    destreza2_2_6 = Destreza.objects.get(codigo="CN.2.2.6.")
    destreza2_3_1 = Destreza.objects.get(codigo="CN.2.3.1.")
    destreza2_3_2 = Destreza.objects.get(codigo="CN.2.3.2.")
    destreza2_3_3 = Destreza.objects.get(codigo="CN.2.3.3.")
    destreza2_3_4 = Destreza.objects.get(codigo="CN.2.3.4.")
    destreza2_3_5 = Destreza.objects.get(codigo="CN.2.3.5.")
    destreza2_3_6 = Destreza.objects.get(codigo="CN.2.3.6.")
    destreza2_3_7 = Destreza.objects.get(codigo="CN.2.3.7.")
    destreza2_3_8 = Destreza.objects.get(codigo="CN.2.3.8.")
    destreza2_3_9 = Destreza.objects.get(codigo="CN.2.3.9.")
    destreza2_3_10 = Destreza.objects.get(codigo="CN.2.3.10.")
    destreza2_3_11 = Destreza.objects.get(codigo="CN.2.3.11.")
    destreza2_3_12 = Destreza.objects.get(codigo="CN.2.3.12.")
    destreza2_3_13 = Destreza.objects.get(codigo="CN.2.3.13.")
    destreza2_4_1 = Destreza.objects.get(codigo="CN.2.4.1.")
    destreza2_4_2 = Destreza.objects.get(codigo="CN.2.4.2.")
    destreza2_4_3 = Destreza.objects.get(codigo="CN.2.4.3.")
    destreza2_4_4 = Destreza.objects.get(codigo="CN.2.4.4.")
    destreza2_4_5 = Destreza.objects.get(codigo="CN.2.4.5.")
    destreza2_4_6 = Destreza.objects.get(codigo="CN.2.4.6.")
    destreza2_4_7 = Destreza.objects.get(codigo="CN.2.4.7.")
    destreza2_4_8 = Destreza.objects.get(codigo="CN.2.4.8.")
    destreza2_4_9 = Destreza.objects.get(codigo="CN.2.4.9.")
    destreza2_4_10 = Destreza.objects.get(codigo="CN.2.4.10.")
    destreza2_4_11 = Destreza.objects.get(codigo="CN.2.4.11.")
    destreza2_4_12 = Destreza.objects.get(codigo="CN.2.4.12.")
    destreza2_4_13 = Destreza.objects.get(codigo="CN.2.4.13.")
    destreza2_4_14 = Destreza.objects.get(codigo="CN.2.4.14.")
    destreza2_5_1 = Destreza.objects.get(codigo="CN.2.5.1.")
    destreza2_5_2 = Destreza.objects.get(codigo="CN.2.5.2.")
    destreza2_5_3 = Destreza.objects.get(codigo="CN.2.5.3.")
    destreza2_5_4 = Destreza.objects.get(codigo="CN.2.5.4.")
    destreza2_5_5 = Destreza.objects.get(codigo="CN.2.5.5.")
    destreza2_5_6 = Destreza.objects.get(codigo="CN.2.5.6.")
    destreza2_5_7 = Destreza.objects.get(codigo="CN.2.5.7.")
    destreza2_5_8 = Destreza.objects.get(codigo="CN.2.5.8.")
    destreza2_5_9 = Destreza.objects.get(codigo="CN.2.5.9.")
    destreza3_1_1 = Destreza.objects.get(codigo="CN.3.1.1.")
    destreza3_1_2 = Destreza.objects.get(codigo="CN.3.1.2.")
    destreza3_1_3 = Destreza.objects.get(codigo="CN.3.1.3.")
    destreza3_1_4 = Destreza.objects.get(codigo="CN.3.1.4.")
    destreza3_1_5 = Destreza.objects.get(codigo="CN.3.1.5.")
    destreza3_1_6 = Destreza.objects.get(codigo="CN.3.1.6.")
    destreza3_1_7 = Destreza.objects.get(codigo="CN.3.1.7.")
    destreza3_1_8 = Destreza.objects.get(codigo="CN.3.1.8.")
    destreza3_1_9 = Destreza.objects.get(codigo="CN.3.1.9.")
    destreza3_1_10 = Destreza.objects.get(codigo="CN.3.1.10.")
    destreza3_1_11 = Destreza.objects.get(codigo="CN.3.1.11.")
    destreza3_1_12 = Destreza.objects.get(codigo="CN.3.1.12.")
    destreza3_1_13 = Destreza.objects.get(codigo="CN.3.1.13.")
    destreza3_2_1 = Destreza.objects.get(codigo="CN.3.2.1.")
    destreza3_2_2 = Destreza.objects.get(codigo="CN.3.2.2.")
    destreza3_2_3 = Destreza.objects.get(codigo="CN.3.2.3.")
    destreza3_2_4 = Destreza.objects.get(codigo="CN.3.2.4.")
    destreza3_2_5 = Destreza.objects.get(codigo="CN.3.2.5.")
    destreza3_2_6 = Destreza.objects.get(codigo="CN.3.2.6.")
    destreza3_2_7 = Destreza.objects.get(codigo="CN.3.2.7.")
    destreza3_2_8 = Destreza.objects.get(codigo="CN.3.2.8.")
    destreza3_2_9 = Destreza.objects.get(codigo="CN.3.2.9.")
    destreza3_2_10 = Destreza.objects.get(codigo="CN.3.2.10.")
    destreza3_3_1 = Destreza.objects.get(codigo="CN.3.3.1.")
    destreza3_3_1 = Destreza.objects.get(codigo="CN.3.3.1.")
    destreza3_3_2 = Destreza.objects.get(codigo="CN.3.3.2.")
    destreza3_3_3 = Destreza.objects.get(codigo="CN.3.3.3.")
    destreza3_3_4 = Destreza.objects.get(codigo="CN.3.3.4.")
    destreza3_3_5 = Destreza.objects.get(codigo="CN.3.3.5.")
    destreza3_3_6 = Destreza.objects.get(codigo="CN.3.3.6.")
    destreza3_3_7 = Destreza.objects.get(codigo="CN.3.3.7.")
    destreza3_3_8 = Destreza.objects.get(codigo="CN.3.3.8.")
    destreza3_3_9 = Destreza.objects.get(codigo="CN.3.3.9.")
    destreza3_3_10 = Destreza.objects.get(codigo="CN.3.3.10.")
    destreza3_3_11 = Destreza.objects.get(codigo="CN.3.3.11.")
    destreza3_3_12 = Destreza.objects.get(codigo="CN.3.3.12.")
    destreza3_4_1 = Destreza.objects.get(codigo="CN.3.4.1.")
    destreza3_4_2 = Destreza.objects.get(codigo="CN.3.4.2.")
    destreza3_4_3 = Destreza.objects.get(codigo="CN.3.4.3.")
    destreza3_4_4 = Destreza.objects.get(codigo="CN.3.4.4.")
    destreza3_4_5 = Destreza.objects.get(codigo="CN.3.4.5.")
    destreza3_4_6 = Destreza.objects.get(codigo="CN.3.4.6.")
    destreza3_4_7 = Destreza.objects.get(codigo="CN.3.4.7.")
    destreza3_4_8 = Destreza.objects.get(codigo="CN.3.4.8.")
    destreza3_4_9 = Destreza.objects.get(codigo="CN.3.4.9.")
    destreza3_4_10 = Destreza.objects.get(codigo="CN.3.4.10.")
    destreza3_4_11 = Destreza.objects.get(codigo="CN.3.4.11.")
    destreza3_4_12 = Destreza.objects.get(codigo="CN.3.4.12.")
    destreza3_4_13 = Destreza.objects.get(codigo="CN.3.4.13.")
    destreza3_4_14 = Destreza.objects.get(codigo="CN.3.4.14.")
    destreza3_5_1 = Destreza.objects.get(codigo="CN.3.5.1.")
    destreza3_5_2 = Destreza.objects.get(codigo="CN.3.5.2.")
    destreza3_5_3 = Destreza.objects.get(codigo="CN.3.5.3.")
    destreza3_5_4 = Destreza.objects.get(codigo="CN.3.5.4.")
    destreza3_5_5 = Destreza.objects.get(codigo="CN.3.5.5.")
    destreza3_5_6 = Destreza.objects.get(codigo="CN.3.5.6.")
    destreza3_5_7 = Destreza.objects.get(codigo="CN.3.5.7.")
    destreza3_5_8 = Destreza.objects.get(codigo="CN.3.5.8.")
    destreza3_5_9 = Destreza.objects.get(codigo="CN.3.5.9.")
    destreza4_1_1 = Destreza.objects.get(codigo="CN.4.1.1.")
    destreza4_1_2 = Destreza.objects.get(codigo="CN.4.1.2.")
    destreza4_1_3 = Destreza.objects.get(codigo="CN.4.1.3.")
    destreza4_1_4 = Destreza.objects.get(codigo="CN.4.1.4.")
    destreza4_1_5 = Destreza.objects.get(codigo="CN.4.1.5.")
    destreza4_1_6 = Destreza.objects.get(codigo="CN.4.1.6.")
    destreza4_1_7 = Destreza.objects.get(codigo="CN.4.1.7.")
    destreza4_1_8 = Destreza.objects.get(codigo="CN.4.1.8.")
    destreza4_1_9 = Destreza.objects.get(codigo="CN.4.1.9.")
    destreza4_1_10 = Destreza.objects.get(codigo="CN.4.1.10.")
    destreza4_1_11 = Destreza.objects.get(codigo="CN.4.1.11.")
    destreza4_1_12 = Destreza.objects.get(codigo="CN.4.1.12.")
    destreza4_1_13 = Destreza.objects.get(codigo="CN.4.1.13.")
    destreza4_1_14 = Destreza.objects.get(codigo="CN.4.1.14.")
    destreza4_1_15 = Destreza.objects.get(codigo="CN.4.1.15.")
    destreza4_1_16 = Destreza.objects.get(codigo="CN.4.1.16.")
    destreza4_1_17 = Destreza.objects.get(codigo="CN.4.1.17.")
    destreza4_2_1 = Destreza.objects.get(codigo="CN.4.2.1.")
    destreza4_2_2 = Destreza.objects.get(codigo="CN.4.2.2.")
    destreza4_2_3 = Destreza.objects.get(codigo="CN.4.2.3.")
    destreza4_2_4 = Destreza.objects.get(codigo="CN.4.2.4.")
    destreza4_2_5 = Destreza.objects.get(codigo="CN.4.2.5.")
    destreza4_2_6 = Destreza.objects.get(codigo="CN.4.2.6.")
    destreza4_2_7 = Destreza.objects.get(codigo="CN.4.2.7.")
    destreza4_3_1 = Destreza.objects.get(codigo="CN.4.3.1.")
    destreza4_3_2 = Destreza.objects.get(codigo="CN.4.3.2.")
    destreza4_3_3 = Destreza.objects.get(codigo="CN.4.3.3.")
    destreza4_3_4 = Destreza.objects.get(codigo="CN.4.3.4.")
    destreza4_3_5 = Destreza.objects.get(codigo="CN.4.3.5.")
    destreza4_3_6 = Destreza.objects.get(codigo="CN.4.3.6.")
    destreza4_3_7 = Destreza.objects.get(codigo="CN.4.3.7.")
    destreza4_3_8 = Destreza.objects.get(codigo="CN.4.3.8.")
    destreza4_3_9 = Destreza.objects.get(codigo="CN.4.3.9.")
    destreza4_3_10 = Destreza.objects.get(codigo="CN.4.3.10.")
    destreza4_3_11 = Destreza.objects.get(codigo="CN.4.3.11.")
    destreza4_3_12 = Destreza.objects.get(codigo="CN.4.3.12.")
    destreza4_3_13 = Destreza.objects.get(codigo="CN.4.3.13.")
    destreza4_3_14 = Destreza.objects.get(codigo="CN.4.3.14.")
    destreza4_3_15 = Destreza.objects.get(codigo="CN.4.3.15.")
    destreza4_3_16 = Destreza.objects.get(codigo="CN.4.3.16.")
    destreza4_3_17 = Destreza.objects.get(codigo="CN.4.3.17.")
    destreza4_3_18 = Destreza.objects.get(codigo="CN.4.3.18.")
    destreza4_3_19 = Destreza.objects.get(codigo="CN.4.3.19.")
    destreza4_4_1 = Destreza.objects.get(codigo="CN.4.4.1.")
    destreza4_4_2 = Destreza.objects.get(codigo="CN.4.4.2.")
    destreza4_4_3 = Destreza.objects.get(codigo="CN.4.4.3.")
    destreza4_4_4 = Destreza.objects.get(codigo="CN.4.4.4.")
    destreza4_4_5 = Destreza.objects.get(codigo="CN.4.4.5.")
    destreza4_4_6 = Destreza.objects.get(codigo="CN.4.4.6.")
    destreza4_4_7 = Destreza.objects.get(codigo="CN.4.4.7.")
    destreza4_4_8 = Destreza.objects.get(codigo="CN.4.4.8.")
    destreza4_4_9 = Destreza.objects.get(codigo="CN.4.4.9.")
    destreza4_4_10 = Destreza.objects.get(codigo="CN.4.4.10.")
    destreza4_4_11 = Destreza.objects.get(codigo="CN.4.4.11.")
    destreza4_4_12 = Destreza.objects.get(codigo="CN.4.4.12.")
    destreza4_4_13 = Destreza.objects.get(codigo="CN.4.4.13.")
    destreza4_4_14 = Destreza.objects.get(codigo="CN.4.4.14.")
    destreza4_4_15 = Destreza.objects.get(codigo="CN.4.4.15.")
    destreza4_4_16 = Destreza.objects.get(codigo="CN.4.4.16.")
    destreza4_4_17 = Destreza.objects.get(codigo="CN.4.4.17.")
    destreza4_5_1 = Destreza.objects.get(codigo="CN.4.5.1.")
    destreza4_5_2 = Destreza.objects.get(codigo="CN.4.5.2.")
    destreza4_5_3 = Destreza.objects.get(codigo="CN.4.5.3.")
    destreza4_5_4 = Destreza.objects.get(codigo="CN.4.5.4.")
    destreza4_5_5 = Destreza.objects.get(codigo="CN.4.5.5.")
    destreza4_5_6 = Destreza.objects.get(codigo="CN.4.5.6.")
    destreza4_5_7 = Destreza.objects.get(codigo="CN.4.5.7.")
    destreza4_5_8 = Destreza.objects.get(codigo="CN.4.5.8.")
    destreza4_5_9 = Destreza.objects.get(codigo="CN.4.5.9.")

    # Asignación

    # Elemental
    criterio2_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo8,
        objetivo10,
    )
    criterio2_1.destrezas.add(
        destreza2_1_1,
        destreza2_1_2,
        destreza2_1_3,
    )

    criterio2_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio2_2.destrezas.add(
        destreza2_1_4,
        destreza2_1_5,
        destreza2_1_6,
        destreza2_1_7,
        destreza2_1_8,
        destreza2_5_9,
    )

    criterio2_3.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo9,
    )
    criterio2_3.destrezas.add(
        destreza2_1_9,
        destreza2_1_10,
        destreza2_1_11,
        destreza2_1_12,
    )

    criterio2_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio2_4.destrezas.add(
        destreza2_2_1,
        destreza2_2_2,
        destreza2_2_3,
        destreza2_2_4,
        destreza2_2_5,
        destreza2_2_6,
        destreza2_5_3,
    )

    criterio2_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio2_5.destrezas.add(
        destreza2_3_1,
        destreza2_3_2,
        destreza2_3_3,
        destreza2_3_4,
        destreza2_3_5,
        destreza2_5_6,
    )

    criterio2_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio2_6.destrezas.add(
        destreza2_3_6,
        destreza2_3_7,
        destreza2_3_8,
    )

    criterio2_7.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
    )
    criterio2_7.destrezas.add(
        destreza2_3_9,
        destreza2_3_10,
    )

    criterio2_8.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio2_8.destrezas.add(
        destreza2_3_11,
        destreza2_3_12,
        destreza2_3_13,
    )

    criterio2_9.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio2_9.destrezas.add(
        destreza2_4_1,
        destreza2_4_2,
        destreza2_4_3,
        destreza2_4_4,
        destreza2_4_5,
        destreza2_4_6,
        destreza2_5_1,
        destreza2_5_2,
        destreza2_5_4,
        destreza2_5_5,
        destreza2_5_7,
    )

    criterio2_10.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
    )
    criterio2_10.destrezas.add(
        destreza2_4_7,
        destreza2_4_8,
        destreza2_4_9,
    )

    criterio2_11.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio2_11.destrezas.add(
        destreza2_4_10,
        destreza2_4_11,
        destreza2_4_12,
        destreza2_4_13,
        destreza2_4_14,
        destreza2_5_8,
    )

    # Media
    criterio3_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo5,
        objetivo6,
    )
    criterio3_1.destrezas.add(
        destreza3_1_1,
        destreza3_1_4,
        destreza3_1_6,
        destreza3_1_7,
    )

    criterio3_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo6,
        objetivo10,
    )
    criterio3_2.destrezas.add(
        destreza3_1_2,
        destreza3_1_3,
        destreza3_1_5,
        destreza3_1_8,
    )

    criterio3_3.objetivos_generales.add(
        objetivo2,
        objetivo6,
        objetivo7,
        objetivo10,
    )
    criterio3_3.destrezas.add(
        destreza3_1_9,
        destreza3_1_10,
        destreza3_1_11,
        destreza3_1_12,
        destreza3_1_13,
        destreza3_5_4,
        destreza3_5_5,
    )

    criterio3_4.objetivos_generales.add(
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo10,
    )
    criterio3_4.destrezas.add(
        destreza3_2_1,
        destreza3_2_2,
        destreza3_2_4,
        destreza3_2_5,
        destreza3_2_10,
    )

    criterio3_5.objetivos_generales.add(
        objetivo4,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio3_5.destrezas.add(
        destreza3_2_3,
        destreza3_2_6,
        destreza3_2_7,
        destreza3_2_8,
        destreza3_2_9,
        destreza3_5_1,
        destreza3_5_2,
    )

    criterio3_6.objetivos_generales.add(
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo8,
    )
    criterio3_6.destrezas.add(
        destreza3_3_1,
        destreza3_3_2,
        destreza3_3_3,
        destreza3_3_4,
        destreza3_5_8,
        destreza3_5_9,
    )

    criterio3_7.objetivos_generales.add(
        objetivo3,
        objetivo5,
        objetivo8,
        objetivo10,
    )
    criterio3_7.destrezas.add(
        destreza3_3_5,
        destreza3_3_6,
    )

    criterio3_8.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo5,
        objetivo10,
    )
    criterio3_8.destrezas.add(
        destreza3_3_7,
        destreza3_3_8,
    )

    criterio3_9.objetivos_generales.add(
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo10,
    )
    criterio3_9.destrezas.add(
        destreza3_3_9,
        destreza3_3_10,
        destreza3_3_11,
        destreza3_3_12,
        destreza3_5_6,
    )

    criterio3_10.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo8,
        objetivo9,
    )
    criterio3_10.destrezas.add(
        destreza3_4_2,
        destreza3_4_3,
        destreza3_4_4,
        destreza3_4_5,
        destreza3_4_6,
        destreza3_5_7,
    )

    criterio3_11.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
    )
    criterio3_11.destrezas.add(
        destreza3_4_1,
        destreza3_4_7,
        destreza3_4_8,
    )

    criterio3_12.objetivos_generales.add(
        objetivo2,
        objetivo5,
        objetivo7,
        objetivo10,
    )
    criterio3_12.destrezas.add(
        destreza3_4_9,
        destreza3_4_10,
        destreza3_4_11,
        destreza3_4_12,
        destreza3_4_13,
        destreza3_4_14,
        destreza3_5_3,
    )

    # Superior
    criterio4_1.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
        objetivo7,
    )
    criterio4_1.destrezas.add(
        destreza4_1_1,
        destreza4_1_2,
        destreza4_1_7,
    )

    criterio4_2.objetivos_generales.add(
        objetivo3,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio4_2.destrezas.add(
        destreza4_1_3,
        destreza4_1_4,
        destreza4_1_5,
        destreza4_1_6,
        destreza4_1_8,
        destreza4_1_9,
        destreza4_5_1,
    )

    criterio4_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo8,
        objetivo9,
    )
    criterio4_3.destrezas.add(
        destreza4_1_10,
        destreza4_1_11,
        destreza4_1_12,
        destreza4_4_7,
        destreza4_5_8,
        destreza4_5_9,
    )

    criterio4_4.objetivos_generales.add(
        objetivo4,
        objetivo9,
    )
    criterio4_4.destrezas.add(
        destreza4_1_13,
        destreza4_1_17,
        destreza4_4_12,
        destreza4_4_13,
        destreza4_5_5,
    )

    criterio4_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo8,
        objetivo9,
    )
    criterio4_5.destrezas.add(
        destreza4_1_14,
        destreza4_1_15,
        destreza4_1_16,
        destreza4_4_14,
        destreza4_4_15,
        destreza4_5_3,
    )

    criterio4_6.objetivos_generales.add(
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
    )
    criterio4_6.destrezas.add(
        destreza4_2_1,
        destreza4_2_4,
        destreza4_2_5,
        destreza4_5_6,
    )

    criterio4_7.objetivos_generales.add(
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio4_7.destrezas.add(
        destreza4_2_2,
        destreza4_2_3,
        destreza4_2_6,
        destreza4_2_7,
    )

    criterio4_8.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo8,
    )
    criterio4_8.destrezas.add(
        destreza4_3_1,
        destreza4_3_2,
        destreza4_3_3,
        destreza4_3_4,
        destreza4_3_5,
        destreza4_3_6,
        destreza4_3_7,
        destreza4_3_8,
    )

    criterio4_9.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo8,
    )
    criterio4_9.destrezas.add(
        destreza4_3_9,
        destreza4_3_10,
        destreza4_3_11,
        destreza4_3_12,
        destreza4_3_13,
    )

    criterio4_10.objetivos_generales.add(
        objetivo1,
        objetivo3,
    )
    criterio4_10.destrezas.add(
        destreza4_3_14,
        destreza4_3_15,
        destreza4_5_4,
    )

    criterio4_11.objetivos_generales.add(
        objetivo1,
        objetivo7,
        objetivo9,
    )
    criterio4_11.destrezas.add(
        destreza4_3_16,
        destreza4_3_17,
        destreza4_3_18,
        destreza4_3_19,
    )

    criterio4_12.objetivos_generales.add(
        objetivo8,
        objetivo9,
    )
    criterio4_12.destrezas.add(
        destreza4_4_1,
        destreza4_4_2,
        destreza4_4_3,
        destreza4_4_4,
        destreza4_4_5,
        destreza4_4_6,
        destreza4_5_2,
    )

    criterio4_13.objetivos_generales.add(
        objetivo8,
        objetivo9,
    )
    criterio4_13.destrezas.add(
        destreza4_4_8,
        destreza4_4_9,
        destreza4_4_10,
        destreza4_4_11,
    )

    criterio4_14.objetivos_generales.add(
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio4_14.destrezas.add(
        destreza4_4_16,
        destreza4_4_17,
        destreza4_5_7,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0044_auto_20180908_2004'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
