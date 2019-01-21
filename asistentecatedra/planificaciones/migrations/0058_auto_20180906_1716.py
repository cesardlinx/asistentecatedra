from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales
    objetivo1 = ObjetivoGeneral.objects.get(codigo="OG.ECA.1.")
    objetivo2 = ObjetivoGeneral.objects.get(codigo="OG.ECA.2.")
    objetivo3 = ObjetivoGeneral.objects.get(codigo="OG.ECA.3.")
    objetivo4 = ObjetivoGeneral.objects.get(codigo="OG.ECA.4.")
    objetivo5 = ObjetivoGeneral.objects.get(codigo="OG.ECA.5.")
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.ECA.6.")
    objetivo7 = ObjetivoGeneral.objects.get(codigo="OG.ECA.7.")
    objetivo8 = ObjetivoGeneral.objects.get(codigo="OG.ECA.8.")

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.4.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.6.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.6.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.6.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.4.")

    # Destrezas
    destreza1_1_1 = Destreza.objects.get(codigo="ECA.1.1.1.")
    destreza1_1_2 = Destreza.objects.get(codigo="ECA.1.1.2.")
    destreza1_1_3 = Destreza.objects.get(codigo="ECA.1.1.3.")
    destreza1_1_4 = Destreza.objects.get(codigo="ECA.1.1.4.")
    destreza1_1_5 = Destreza.objects.get(codigo="ECA.1.1.5.")
    destreza1_1_6 = Destreza.objects.get(codigo="ECA.1.1.6.")
    destreza1_1_7 = Destreza.objects.get(codigo="ECA.1.1.7.")
    destreza1_1_8 = Destreza.objects.get(codigo="ECA.1.1.8.")
    destreza1_1_9 = Destreza.objects.get(codigo="ECA.1.1.9.")
    destreza1_2_1 = Destreza.objects.get(codigo="ECA.1.2.1.")
    destreza1_2_2 = Destreza.objects.get(codigo="ECA.1.2.2.")
    destreza1_2_3 = Destreza.objects.get(codigo="ECA.1.2.3.")
    destreza1_2_4 = Destreza.objects.get(codigo="ECA.1.2.4.")
    destreza1_2_5 = Destreza.objects.get(codigo="ECA.1.2.5.")
    destreza1_2_6 = Destreza.objects.get(codigo="ECA.1.2.6.")
    destreza1_2_7 = Destreza.objects.get(codigo="ECA.1.2.7.")
    destreza1_3_1 = Destreza.objects.get(codigo="ECA.1.3.1.")
    destreza1_3_2 = Destreza.objects.get(codigo="ECA.1.3.2.")
    destreza1_3_3 = Destreza.objects.get(codigo="ECA.1.3.3.")
    destreza1_3_4 = Destreza.objects.get(codigo="ECA.1.3.4.")
    destreza1_3_5 = Destreza.objects.get(codigo="ECA.1.3.5.")
    destreza2_1_1 = Destreza.objects.get(codigo="ECA.2.1.1.")
    destreza2_1_2 = Destreza.objects.get(codigo="ECA.2.1.2.")
    destreza2_1_3 = Destreza.objects.get(codigo="ECA.2.1.3.")
    destreza2_1_4 = Destreza.objects.get(codigo="ECA.2.1.4.")
    destreza2_1_5 = Destreza.objects.get(codigo="ECA.2.1.5.")
    destreza2_1_6 = Destreza.objects.get(codigo="ECA.2.1.6.")
    destreza2_1_7 = Destreza.objects.get(codigo="ECA.2.1.7.")
    destreza2_1_8 = Destreza.objects.get(codigo="ECA.2.1.8.")
    destreza2_1_9 = Destreza.objects.get(codigo="ECA.2.1.9.")
    destreza2_1_10 = Destreza.objects.get(codigo="ECA.2.1.10.")
    destreza2_2_1 = Destreza.objects.get(codigo="ECA.2.2.1.")
    destreza2_2_2 = Destreza.objects.get(codigo="ECA.2.2.2.")
    destreza2_2_3 = Destreza.objects.get(codigo="ECA.2.2.3.")
    destreza2_2_4 = Destreza.objects.get(codigo="ECA.2.2.4.")
    destreza2_2_5 = Destreza.objects.get(codigo="ECA.2.2.5.")
    destreza2_2_6 = Destreza.objects.get(codigo="ECA.2.2.6.")
    destreza2_2_7 = Destreza.objects.get(codigo="ECA.2.2.7.")
    destreza2_2_8 = Destreza.objects.get(codigo="ECA.2.2.8.")
    destreza2_2_9 = Destreza.objects.get(codigo="ECA.2.2.9.")
    destreza2_2_10 = Destreza.objects.get(codigo="ECA.2.2.10.")
    destreza2_2_11 = Destreza.objects.get(codigo="ECA.2.2.11.")
    destreza2_2_12 = Destreza.objects.get(codigo="ECA.2.2.12.")
    destreza2_2_13 = Destreza.objects.get(codigo="ECA.2.2.13.")
    destreza2_3_1 = Destreza.objects.get(codigo="ECA.2.3.1.")
    destreza2_3_2 = Destreza.objects.get(codigo="ECA.2.3.2.")
    destreza2_3_3 = Destreza.objects.get(codigo="ECA.2.3.3.")
    destreza2_3_4 = Destreza.objects.get(codigo="ECA.2.3.4.")
    destreza2_3_5 = Destreza.objects.get(codigo="ECA.2.3.5.")
    destreza2_3_6 = Destreza.objects.get(codigo="ECA.2.3.6.")
    destreza2_3_7 = Destreza.objects.get(codigo="ECA.2.3.7.")
    destreza2_3_8 = Destreza.objects.get(codigo="ECA.2.3.8.")
    destreza2_3_9 = Destreza.objects.get(codigo="ECA.2.3.9.")
    destreza2_3_10 = Destreza.objects.get(codigo="ECA.2.3.10.")
    destreza2_3_11 = Destreza.objects.get(codigo="ECA.2.3.11.")
    destreza2_3_12 = Destreza.objects.get(codigo="ECA.2.3.12.")
    destreza2_3_13 = Destreza.objects.get(codigo="ECA.2.3.13.")
    destreza2_3_14 = Destreza.objects.get(codigo="ECA.2.3.14.")
    destreza2_3_15 = Destreza.objects.get(codigo="ECA.2.3.15.")
    destreza2_3_16 = Destreza.objects.get(codigo="ECA.2.3.16.")
    destreza2_3_17 = Destreza.objects.get(codigo="ECA.2.3.17.")
    destreza2_3_18 = Destreza.objects.get(codigo="ECA.2.3.18.")
    destreza2_3_19 = Destreza.objects.get(codigo="ECA.2.3.19.")
    destreza3_1_1 = Destreza.objects.get(codigo="ECA.3.1.1.")
    destreza3_1_2 = Destreza.objects.get(codigo="ECA.3.1.2.")
    destreza3_1_3 = Destreza.objects.get(codigo="ECA.3.1.3.")
    destreza3_1_4 = Destreza.objects.get(codigo="ECA.3.1.4.")
    destreza3_1_5 = Destreza.objects.get(codigo="ECA.3.1.5.")
    destreza3_1_6 = Destreza.objects.get(codigo="ECA.3.1.6.")
    destreza3_1_7 = Destreza.objects.get(codigo="ECA.3.1.7.")
    destreza3_1_8 = Destreza.objects.get(codigo="ECA.3.1.8.")
    destreza3_1_9 = Destreza.objects.get(codigo="ECA.3.1.9.")
    destreza3_1_10 = Destreza.objects.get(codigo="ECA.3.1.10.")
    destreza3_1_11 = Destreza.objects.get(codigo="ECA.3.1.11.")
    destreza3_1_12 = Destreza.objects.get(codigo="ECA.3.1.12.")
    destreza3_1_13 = Destreza.objects.get(codigo="ECA.3.1.13.")
    destreza3_1_14 = Destreza.objects.get(codigo="ECA.3.1.14.")
    destreza3_1_15 = Destreza.objects.get(codigo="ECA.3.1.15.")
    destreza3_1_16 = Destreza.objects.get(codigo="ECA.3.1.16.")
    destreza3_2_1 = Destreza.objects.get(codigo="ECA.3.2.1.")
    destreza3_2_2 = Destreza.objects.get(codigo="ECA.3.2.2.")
    destreza3_2_3 = Destreza.objects.get(codigo="ECA.3.2.3.")
    destreza3_2_4 = Destreza.objects.get(codigo="ECA.3.2.4.")
    destreza3_2_5 = Destreza.objects.get(codigo="ECA.3.2.5.")
    destreza3_2_6 = Destreza.objects.get(codigo="ECA.3.2.6.")
    destreza3_2_7 = Destreza.objects.get(codigo="ECA.3.2.7.")
    destreza3_2_8 = Destreza.objects.get(codigo="ECA.3.2.8.")
    destreza3_2_9 = Destreza.objects.get(codigo="ECA.3.2.9.")
    destreza3_2_10 = Destreza.objects.get(codigo="ECA.3.2.10.")
    destreza3_2_11 = Destreza.objects.get(codigo="ECA.3.2.11.")
    destreza3_2_12 = Destreza.objects.get(codigo="ECA.3.2.12.")
    destreza3_2_13 = Destreza.objects.get(codigo="ECA.3.2.13.")
    destreza3_2_14 = Destreza.objects.get(codigo="ECA.3.2.14.")
    destreza3_2_15 = Destreza.objects.get(codigo="ECA.3.2.15.")
    destreza3_2_16 = Destreza.objects.get(codigo="ECA.3.2.16.")
    destreza3_2_17 = Destreza.objects.get(codigo="ECA.3.2.17.")
    destreza3_2_18 = Destreza.objects.get(codigo="ECA.3.2.18.")
    destreza3_2_19 = Destreza.objects.get(codigo="ECA.3.2.19.")
    destreza3_3_1 = Destreza.objects.get(codigo="ECA.3.3.1.")
    destreza3_3_2 = Destreza.objects.get(codigo="ECA.3.3.2.")
    destreza3_3_3 = Destreza.objects.get(codigo="ECA.3.3.3.")
    destreza3_3_4 = Destreza.objects.get(codigo="ECA.3.3.4.")
    destreza3_3_5 = Destreza.objects.get(codigo="ECA.3.3.5.")
    destreza3_3_6 = Destreza.objects.get(codigo="ECA.3.3.6.")
    destreza3_3_7 = Destreza.objects.get(codigo="ECA.3.3.7.")
    destreza3_3_8 = Destreza.objects.get(codigo="ECA.3.3.8.")
    destreza3_3_9 = Destreza.objects.get(codigo="ECA.3.3.9.")
    destreza3_3_10 = Destreza.objects.get(codigo="ECA.3.3.10.")
    destreza4_1_1 = Destreza.objects.get(codigo="ECA.4.1.1.")
    destreza4_1_2 = Destreza.objects.get(codigo="ECA.4.1.2.")
    destreza4_1_3 = Destreza.objects.get(codigo="ECA.4.1.3.")
    destreza4_1_4 = Destreza.objects.get(codigo="ECA.4.1.4.")
    destreza4_1_5 = Destreza.objects.get(codigo="ECA.4.1.5.")
    destreza4_1_6 = Destreza.objects.get(codigo="ECA.4.1.6.")
    destreza4_1_7 = Destreza.objects.get(codigo="ECA.4.1.7.")
    destreza4_1_8 = Destreza.objects.get(codigo="ECA.4.1.8.")
    destreza4_1_9 = Destreza.objects.get(codigo="ECA.4.1.9.")
    destreza4_1_10 = Destreza.objects.get(codigo="ECA.4.1.10.")
    destreza4_1_11 = Destreza.objects.get(codigo="ECA.4.1.11.")
    destreza4_1_12 = Destreza.objects.get(codigo="ECA.4.1.12.")
    destreza4_1_13 = Destreza.objects.get(codigo="ECA.4.1.13.")
    destreza4_1_14 = Destreza.objects.get(codigo="ECA.4.1.14.")
    destreza4_1_15 = Destreza.objects.get(codigo="ECA.4.1.15.")
    destreza4_2_1 = Destreza.objects.get(codigo="ECA.4.2.1.")
    destreza4_2_2 = Destreza.objects.get(codigo="ECA.4.2.2.")
    destreza4_2_3 = Destreza.objects.get(codigo="ECA.4.2.3.")
    destreza4_2_4 = Destreza.objects.get(codigo="ECA.4.2.4.")
    destreza4_2_5 = Destreza.objects.get(codigo="ECA.4.2.5.")
    destreza4_2_6 = Destreza.objects.get(codigo="ECA.4.2.6.")
    destreza4_2_7 = Destreza.objects.get(codigo="ECA.4.2.7.")
    destreza4_2_8 = Destreza.objects.get(codigo="ECA.4.2.8.")
    destreza4_2_9 = Destreza.objects.get(codigo="ECA.4.2.9.")
    destreza4_2_10 = Destreza.objects.get(codigo="ECA.4.2.10.")
    destreza4_2_11 = Destreza.objects.get(codigo="ECA.4.2.11.")
    destreza4_3_1 = Destreza.objects.get(codigo="ECA.4.3.1.")
    destreza4_3_2 = Destreza.objects.get(codigo="ECA.4.3.2.")
    destreza4_3_3 = Destreza.objects.get(codigo="ECA.4.3.3.")
    destreza4_3_4 = Destreza.objects.get(codigo="ECA.4.3.4.")
    destreza4_3_5 = Destreza.objects.get(codigo="ECA.4.3.5.")
    destreza4_3_6 = Destreza.objects.get(codigo="ECA.4.3.6.")
    destreza4_3_7 = Destreza.objects.get(codigo="ECA.4.3.7.")
    destreza4_3_8 = Destreza.objects.get(codigo="ECA.4.3.8.")
    destreza4_3_9 = Destreza.objects.get(codigo="ECA.4.3.9.")
    destreza4_3_10 = Destreza.objects.get(codigo="ECA.4.3.10.")
    destreza4_3_11 = Destreza.objects.get(codigo="ECA.4.3.11.")
    destreza4_3_12 = Destreza.objects.get(codigo="ECA.4.3.12.")
    destreza4_3_13 = Destreza.objects.get(codigo="ECA.4.3.13.")
    destreza4_3_14 = Destreza.objects.get(codigo="ECA.4.3.14.")
    destreza4_3_15 = Destreza.objects.get(codigo="ECA.4.3.15.")
    destreza5_1_1 = Destreza.objects.get(codigo="ECA.5.1.1.")
    destreza5_1_2 = Destreza.objects.get(codigo="ECA.5.1.2.")
    destreza5_1_3 = Destreza.objects.get(codigo="ECA.5.1.3.")
    destreza5_1_4 = Destreza.objects.get(codigo="ECA.5.1.4.")
    destreza5_1_5 = Destreza.objects.get(codigo="ECA.5.1.5.")
    destreza5_1_6 = Destreza.objects.get(codigo="ECA.5.1.6.")
    destreza5_1_7 = Destreza.objects.get(codigo="ECA.5.1.7.")
    destreza5_1_8 = Destreza.objects.get(codigo="ECA.5.1.8.")
    destreza5_1_9 = Destreza.objects.get(codigo="ECA.5.1.9.")
    destreza5_2_1 = Destreza.objects.get(codigo="ECA.5.2.1.")
    destreza5_2_2 = Destreza.objects.get(codigo="ECA.5.2.2.")
    destreza5_2_3 = Destreza.objects.get(codigo="ECA.5.2.3.")
    destreza5_2_4 = Destreza.objects.get(codigo="ECA.5.2.4.")
    destreza5_2_5 = Destreza.objects.get(codigo="ECA.5.2.5.")
    destreza5_2_6 = Destreza.objects.get(codigo="ECA.5.2.6.")
    destreza5_2_7 = Destreza.objects.get(codigo="ECA.5.2.7.")
    destreza5_2_8 = Destreza.objects.get(codigo="ECA.5.2.8.")
    destreza5_2_9 = Destreza.objects.get(codigo="ECA.5.2.9.")
    destreza5_2_10 = Destreza.objects.get(codigo="ECA.5.2.10.")
    destreza5_3_1 = Destreza.objects.get(codigo="ECA.5.3.1.")
    destreza5_3_2 = Destreza.objects.get(codigo="ECA.5.3.2.")
    destreza5_3_3 = Destreza.objects.get(codigo="ECA.5.3.3.")
    destreza5_3_4 = Destreza.objects.get(codigo="ECA.5.3.4.")
    destreza5_3_5 = Destreza.objects.get(codigo="ECA.5.3.5.")
    destreza5_3_6 = Destreza.objects.get(codigo="ECA.5.3.6.")
    destreza5_3_7 = Destreza.objects.get(codigo="ECA.5.3.7.")
    destreza5_3_8 = Destreza.objects.get(codigo="ECA.5.3.8.")
    destreza5_3_9 = Destreza.objects.get(codigo="ECA.5.3.9.")
    destreza5_3_10 = Destreza.objects.get(codigo="ECA.5.3.10.")
    destreza5_3_11 = Destreza.objects.get(codigo="ECA.5.3.11.")
    destreza5_3_12 = Destreza.objects.get(codigo="ECA.5.3.12.")

    # Asignación

    # Preparatoria
    criterio1_1.objetivos_generales.add(
        objetivo1,
        objetivo8,
    )
    criterio1_1.destrezas.add(
        destreza1_1_1,
        destreza1_1_3,
        destreza1_1_5,
    )

    criterio1_2.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo8,
    )
    criterio1_2.destrezas.add(
        destreza1_3_2,
        destreza1_3_3,
        destreza1_3_4,
        destreza1_3_5,
    )

    criterio1_3.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo7,
        objetivo8,
    )
    criterio1_3.destrezas.add(
        destreza1_1_2,
        destreza1_1_4,
        destreza1_1_6,
        destreza1_1_7,
        destreza1_1_8,
        destreza1_1_9,
    )

    criterio1_4.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio1_4.destrezas.add(
        destreza1_2_1,
        destreza1_2_2,
        destreza1_2_3,
        destreza1_2_4,
        destreza1_2_5,
        destreza1_2_6,
        destreza1_2_7,
        destreza1_3_1,
    )

    # Elemental
    criterio2_1.objetivos_generales.add(
        objetivo5,
        objetivo7
    )
    criterio2_1.destrezas.add(
        destreza2_1_1,
        destreza2_1_2,
        destreza2_1_3,
        destreza2_1_6,
        destreza2_3_1,
        destreza2_3_2,
    )

    criterio2_2.objetivos_generales.add(
        objetivo1,
        objetivo8,
    )
    criterio2_2.destrezas.add(
        destreza2_1_4,
        destreza2_1_5,
        destreza2_1_7,
        destreza2_1_8,
        destreza2_1_9,
    )

    criterio2_3.objetivos_generales.add(
        objetivo1,
        objetivo4,
    )
    criterio2_3.destrezas.add(
        destreza2_1_10,
        destreza2_2_4,
        destreza2_2_5,
        destreza2_2_6,
        destreza2_2_7,
        destreza2_3_8,
        destreza2_3_13,
    )

    criterio2_4.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo7,
        objetivo8,
    )
    criterio2_4.destrezas.add(
        destreza2_2_1,
        destreza2_2_2,
        destreza2_2_3,
        destreza2_2_8,
        destreza2_2_9,
        destreza2_2_10,
        destreza2_2_12,
        destreza2_2_13,
        destreza2_3_12,
    )

    criterio2_5.objetivos_generales.add(
        objetivo2,
        objetivo5,
        objetivo6,
    )
    criterio2_5.destrezas.add(
        destreza2_3_3,
        destreza2_3_4,
        destreza2_3_5,
        destreza2_3_6,
        destreza2_3_7,
        destreza2_3_9,
        destreza2_3_10,
        destreza2_3_11,
        destreza2_3_14,
        destreza2_3_15,
    )

    criterio2_6.objetivos_generales.add(
        objetivo2,
        objetivo6,
    )
    criterio2_6.destrezas.add(
        destreza2_2_11,
        destreza2_3_16,
        destreza2_3_17,
        destreza2_3_18,
        destreza2_3_19,
    )

    # Media
    criterio3_1.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
        objetivo8,
    )
    criterio3_1.destrezas.add(
        destreza3_1_1,
        destreza3_1_2,
        destreza3_1_3,
        destreza3_1_4,
        destreza3_1_5,
        destreza3_1_6,
        destreza3_1_7,
        destreza3_2_1,
        destreza3_2_2,
        destreza3_2_3,
        destreza3_2_4,
    )

    criterio3_2.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio3_2.destrezas.add(
        destreza3_1_8,
        destreza3_1_9,
        destreza3_1_10,
        destreza3_1_11,
        destreza3_2_10,
        destreza3_2_11,
        destreza3_3_4,
        destreza3_3_5,
        destreza3_3_6,
    )

    criterio3_3.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo4,
    )
    criterio3_3.destrezas.add(
        destreza3_1_12,
        destreza3_1_13,
        destreza3_1_14,
        destreza3_1_15,
        destreza3_1_16,
    )

    criterio3_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
    )
    criterio3_4.destrezas.add(
        destreza3_2_5,
        destreza3_2_6,
        destreza3_2_7,
        destreza3_2_8,
        destreza3_2_9,
    )

    criterio3_5.objetivos_generales.add(
        objetivo2,
        objetivo5,
        objetivo6,
    )
    criterio3_5.destrezas.add(
        destreza3_2_12,
        destreza3_2_13,
        destreza3_2_14,
        destreza3_2_15,
    )

    criterio3_6.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo4,
    )
    criterio3_6.destrezas.add(
        destreza3_2_16,
        destreza3_2_17,
        destreza3_2_18,
        destreza3_2_19,
        destreza3_3_1,
        destreza3_3_2,
        destreza3_3_3,
        destreza3_3_7,
        destreza3_3_8,
        destreza3_3_9,
        destreza3_3_10,
    )

    # Superior
    criterio4_1.objetivos_generales.add(
        objetivo2,
        objetivo5,
    )
    criterio4_1.destrezas.add(
        destreza4_1_1,
        destreza4_1_5,
        destreza4_2_3,
        destreza4_2_10,
    )

    criterio4_2.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo8,
    )
    criterio4_2.destrezas.add(
        destreza4_1_6,
        destreza4_1_15,
        destreza4_2_11,
        destreza4_3_1,
        destreza4_3_2,
        destreza4_3_3,
        destreza4_3_5,
        destreza4_3_6,
        destreza4_3_11,
        destreza4_3_13,
        destreza4_3_14,
        destreza4_3_15,
    )

    criterio4_3.objetivos_generales.add(
        objetivo4,
        objetivo5,
        objetivo7,
    )
    criterio4_3.destrezas.add(
        destreza4_1_9,
        destreza4_1_10,
        destreza4_2_7,
        destreza4_2_8,
        destreza4_3_7,
        destreza4_3_8,
    )

    criterio4_4.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo7,
        objetivo8,
    )
    criterio4_4.destrezas.add(
        destreza4_1_2,
        destreza4_1_3,
        destreza4_1_4,
        destreza4_1_8,
        destreza4_1_14,
        destreza4_2_1,
        destreza4_2_2,
        destreza4_3_12,
    )

    criterio4_5.objetivos_generales.add(
        objetivo2,
        objetivo4,
    )
    criterio4_5.destrezas.add(
        destreza4_1_7,
        destreza4_2_4,
        destreza4_2_5,
    )

    criterio4_6.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio4_6.destrezas.add(
        destreza4_1_11,
        destreza4_1_12,
        destreza4_1_13,
        destreza4_2_6,
        destreza4_2_9,
        destreza4_3_4,
        destreza4_3_9,
        destreza4_3_10,
    )

    # Bachillerato
    criterio5_1.objetivos_generales.add(
        objetivo2,
        objetivo5,
        objetivo8,
    )
    criterio5_1.destrezas.add(
        destreza5_1_3,
        destreza5_1_4,
        destreza5_2_8,
        destreza5_3_2,
        destreza5_3_3,
        destreza5_3_4,
        destreza5_3_5,
        destreza5_3_6,
        destreza5_3_7,
        destreza5_3_8,
        destreza5_3_9,
    )

    criterio5_2.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo7,
    )
    criterio5_2.destrezas.add(
        destreza5_1_5,
        destreza5_2_7,
        destreza5_2_9,
        destreza5_3_1,
    )

    criterio5_3.objetivos_generales.add(
        objetivo1,
        objetivo4,
        objetivo7,
        objetivo8,
    )
    criterio5_3.destrezas.add(
        destreza5_1_1,
        destreza5_1_2,
        destreza5_1_6,
        destreza5_1_7,
        destreza5_2_1,
        destreza5_2_2,
        destreza5_2_3,
        destreza5_2_4,
        destreza5_2_5,
        destreza5_2_6,
        destreza5_2_10,
        destreza5_3_10,
    )

    criterio5_4.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio5_4.destrezas.add(
        destreza5_1_8,
        destreza5_1_9,
        destreza5_3_11,
        destreza5_3_12,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0057_auto_20180903_1612'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
