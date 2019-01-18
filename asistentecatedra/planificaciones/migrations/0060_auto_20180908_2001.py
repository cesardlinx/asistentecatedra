from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales
    objetivo1 = ObjetivoGeneral.objects.get(codigo="OG.LL.1.")
    objetivo2 = ObjetivoGeneral.objects.get(codigo="OG.LL.2.")
    objetivo3 = ObjetivoGeneral.objects.get(codigo="OG.LL.3.")
    objetivo4 = ObjetivoGeneral.objects.get(codigo="OG.LL.4.")
    objetivo5 = ObjetivoGeneral.objects.get(codigo="OG.LL.5.")
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.LL.6.")
    objetivo7 = ObjetivoGeneral.objects.get(codigo="OG.LL.7.")
    objetivo8 = ObjetivoGeneral.objects.get(codigo="OG.LL.8.")
    objetivo9 = ObjetivoGeneral.objects.get(codigo="OG.LL.9.")
    objetivo10 = ObjetivoGeneral.objects.get(codigo="OG.LL.10.")
    objetivo11 = ObjetivoGeneral.objects.get(codigo="OG.LL.11.")

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.4.")
    criterio1_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.5.")
    criterio1_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.6.")
    criterio1_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.7.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.6.")
    criterio2_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.7.")
    criterio2_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.8.")
    criterio2_9 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.9.")
    criterio2_10 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.10.")
    criterio2_11 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.11.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.8.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.8.")
    criterio4_9 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.9.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.4.")
    criterio5_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.5.")
    criterio5_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.6.")
    criterio5_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.7.")
    criterio5_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.8.")

    # Destrezas
    destreza1_5_1 = Destreza.objects.get(codigo="LL.1.5.1.")
    destreza1_5_2 = Destreza.objects.get(codigo="LL.1.5.2.")
    destreza1_5_3 = Destreza.objects.get(codigo="LL.1.5.3.")
    destreza1_5_4 = Destreza.objects.get(codigo="LL.1.5.4.")
    destreza1_5_5 = Destreza.objects.get(codigo="LL.1.5.5.")
    destreza1_5_6 = Destreza.objects.get(codigo="LL.1.5.6.")
    destreza1_5_7 = Destreza.objects.get(codigo="LL.1.5.7.")
    destreza1_5_8 = Destreza.objects.get(codigo="LL.1.5.8.")
    destreza1_5_9 = Destreza.objects.get(codigo="LL.1.5.9.")
    destreza1_5_10 = Destreza.objects.get(codigo="LL.1.5.10.")
    destreza1_5_11 = Destreza.objects.get(codigo="LL.1.5.11.")
    destreza1_5_12 = Destreza.objects.get(codigo="LL.1.5.12.")
    destreza1_5_13 = Destreza.objects.get(codigo="LL.1.5.13.")
    destreza1_5_14 = Destreza.objects.get(codigo="LL.1.5.14.")
    destreza1_5_15 = Destreza.objects.get(codigo="LL.1.5.15.")
    destreza1_5_16 = Destreza.objects.get(codigo="LL.1.5.16.")
    destreza1_5_17 = Destreza.objects.get(codigo="LL.1.5.17.")
    destreza1_5_18 = Destreza.objects.get(codigo="LL.1.5.18.")
    destreza1_5_19 = Destreza.objects.get(codigo="LL.1.5.19.")
    destreza1_5_20 = Destreza.objects.get(codigo="LL.1.5.20.")
    destreza1_5_21 = Destreza.objects.get(codigo="LL.1.5.21.")
    destreza1_5_22 = Destreza.objects.get(codigo="LL.1.5.22.")
    destreza2_1_1 = Destreza.objects.get(codigo="LL.2.1.1.")
    destreza2_1_2 = Destreza.objects.get(codigo="LL.2.1.2.")
    destreza2_1_3 = Destreza.objects.get(codigo="LL.2.1.3.")
    destreza2_1_4 = Destreza.objects.get(codigo="LL.2.1.4.")
    destreza2_2_1 = Destreza.objects.get(codigo="LL.2.2.1.")
    destreza2_2_2 = Destreza.objects.get(codigo="LL.2.2.2.")
    destreza2_2_3 = Destreza.objects.get(codigo="LL.2.2.3.")
    destreza2_2_4 = Destreza.objects.get(codigo="LL.2.2.4.")
    destreza2_2_5 = Destreza.objects.get(codigo="LL.2.2.5.")
    destreza2_2_6 = Destreza.objects.get(codigo="LL.2.2.6.")
    destreza2_3_1 = Destreza.objects.get(codigo="LL.2.3.1.")
    destreza2_3_2 = Destreza.objects.get(codigo="LL.2.3.2.")
    destreza2_3_3 = Destreza.objects.get(codigo="LL.2.3.3.")
    destreza2_3_4 = Destreza.objects.get(codigo="LL.2.3.4.")
    destreza2_3_5 = Destreza.objects.get(codigo="LL.2.3.5.")
    destreza2_3_6 = Destreza.objects.get(codigo="LL.2.3.6.")
    destreza2_3_7 = Destreza.objects.get(codigo="LL.2.3.7.")
    destreza2_3_8 = Destreza.objects.get(codigo="LL.2.3.8.")
    destreza2_3_9 = Destreza.objects.get(codigo="LL.2.3.9.")
    destreza2_3_10 = Destreza.objects.get(codigo="LL.2.3.10.")
    destreza2_3_11 = Destreza.objects.get(codigo="LL.2.3.11.")
    destreza2_4_1 = Destreza.objects.get(codigo="LL.2.4.1.")
    destreza2_4_2 = Destreza.objects.get(codigo="LL.2.4.2.")
    destreza2_4_3 = Destreza.objects.get(codigo="LL.2.4.3.")
    destreza2_4_4 = Destreza.objects.get(codigo="LL.2.4.4.")
    destreza2_4_5 = Destreza.objects.get(codigo="LL.2.4.5.")
    destreza2_4_6 = Destreza.objects.get(codigo="LL.2.4.6.")
    destreza2_4_7 = Destreza.objects.get(codigo="LL.2.4.7.")
    destreza2_5_1 = Destreza.objects.get(codigo="LL.2.5.1.")
    destreza2_5_2 = Destreza.objects.get(codigo="LL.2.5.2.")
    destreza2_5_3 = Destreza.objects.get(codigo="LL.2.5.3.")
    destreza2_5_4 = Destreza.objects.get(codigo="LL.2.5.4.")
    destreza2_5_5 = Destreza.objects.get(codigo="LL.2.5.5.")
    destreza3_1_1 = Destreza.objects.get(codigo="LL.3.1.1.")
    destreza3_1_2 = Destreza.objects.get(codigo="LL.3.1.2.")
    destreza3_1_3 = Destreza.objects.get(codigo="LL.3.1.3.")
    destreza3_2_1 = Destreza.objects.get(codigo="LL.3.2.1.")
    destreza3_2_2 = Destreza.objects.get(codigo="LL.3.2.2.")
    destreza3_2_3 = Destreza.objects.get(codigo="LL.3.2.3.")
    destreza3_2_4 = Destreza.objects.get(codigo="LL.3.2.4.")
    destreza3_2_5 = Destreza.objects.get(codigo="LL.3.2.5.")
    destreza3_3_1 = Destreza.objects.get(codigo="LL.3.3.1.")
    destreza3_3_2 = Destreza.objects.get(codigo="LL.3.3.2.")
    destreza3_3_3 = Destreza.objects.get(codigo="LL.3.3.3.")
    destreza3_3_4 = Destreza.objects.get(codigo="LL.3.3.4.")
    destreza3_3_5 = Destreza.objects.get(codigo="LL.3.3.5.")
    destreza3_3_6 = Destreza.objects.get(codigo="LL.3.3.6.")
    destreza3_3_7 = Destreza.objects.get(codigo="LL.3.3.7.")
    destreza3_3_8 = Destreza.objects.get(codigo="LL.3.3.8.")
    destreza3_3_9 = Destreza.objects.get(codigo="LL.3.3.9.")
    destreza3_3_10 = Destreza.objects.get(codigo="LL.3.3.10.")
    destreza3_3_11 = Destreza.objects.get(codigo="LL.3.3.11.")
    destreza3_4_1 = Destreza.objects.get(codigo="LL.3.4.1.")
    destreza3_4_2 = Destreza.objects.get(codigo="LL.3.4.2.")
    destreza3_4_3 = Destreza.objects.get(codigo="LL.3.4.3.")
    destreza3_4_4 = Destreza.objects.get(codigo="LL.3.4.4.")
    destreza3_4_5 = Destreza.objects.get(codigo="LL.3.4.5.")
    destreza3_4_6 = Destreza.objects.get(codigo="LL.3.4.6.")
    destreza3_4_7 = Destreza.objects.get(codigo="LL.3.4.7.")
    destreza3_4_8 = Destreza.objects.get(codigo="LL.3.4.8.")
    destreza3_4_9 = Destreza.objects.get(codigo="LL.3.4.9.")
    destreza3_4_10 = Destreza.objects.get(codigo="LL.3.4.10.")
    destreza3_4_11 = Destreza.objects.get(codigo="LL.3.4.11.")
    destreza3_4_12 = Destreza.objects.get(codigo="LL.3.4.12.")
    destreza3_4_13 = Destreza.objects.get(codigo="LL.3.4.13.")
    destreza3_4_14 = Destreza.objects.get(codigo="LL.3.4.14.")
    destreza3_5_1 = Destreza.objects.get(codigo="LL.3.5.1.")
    destreza3_5_2 = Destreza.objects.get(codigo="LL.3.5.2.")
    destreza3_5_3 = Destreza.objects.get(codigo="LL.3.5.3.")
    destreza3_5_4 = Destreza.objects.get(codigo="LL.3.5.4.")
    destreza3_5_5 = Destreza.objects.get(codigo="LL.3.5.5.")
    destreza3_5_6 = Destreza.objects.get(codigo="LL.3.5.6.")
    destreza4_1_1 = Destreza.objects.get(codigo="LL.4.1.1.")
    destreza4_1_1 = Destreza.objects.get(codigo="LL.4.1.1.")
    destreza4_1_2 = Destreza.objects.get(codigo="LL.4.1.2.")
    destreza4_1_3 = Destreza.objects.get(codigo="LL.4.1.3.")
    destreza4_1_4 = Destreza.objects.get(codigo="LL.4.1.4.")
    destreza4_2_1 = Destreza.objects.get(codigo="LL.4.2.1.")
    destreza4_2_2 = Destreza.objects.get(codigo="LL.4.2.2.")
    destreza4_2_3 = Destreza.objects.get(codigo="LL.4.2.3.")
    destreza4_2_4 = Destreza.objects.get(codigo="LL.4.2.4.")
    destreza4_2_5 = Destreza.objects.get(codigo="LL.4.2.5.")
    destreza4_2_6 = Destreza.objects.get(codigo="LL.4.2.6.")
    destreza4_3_1 = Destreza.objects.get(codigo="LL.4.3.1.")
    destreza4_3_2 = Destreza.objects.get(codigo="LL.4.3.2.")
    destreza4_3_3 = Destreza.objects.get(codigo="LL.4.3.3.")
    destreza4_3_4 = Destreza.objects.get(codigo="LL.4.3.4.")
    destreza4_3_5 = Destreza.objects.get(codigo="LL.4.3.5.")
    destreza4_3_6 = Destreza.objects.get(codigo="LL.4.3.6.")
    destreza4_3_7 = Destreza.objects.get(codigo="LL.4.3.7.")
    destreza4_3_8 = Destreza.objects.get(codigo="LL.4.3.8.")
    destreza4_3_9 = Destreza.objects.get(codigo="LL.4.3.9.")
    destreza4_3_10 = Destreza.objects.get(codigo="LL.4.3.10.")
    destreza4_4_1 = Destreza.objects.get(codigo="LL.4.4.1.")
    destreza4_4_2 = Destreza.objects.get(codigo="LL.4.4.2.")
    destreza4_4_3 = Destreza.objects.get(codigo="LL.4.4.3.")
    destreza4_4_4 = Destreza.objects.get(codigo="LL.4.4.4.")
    destreza4_4_5 = Destreza.objects.get(codigo="LL.4.4.5.")
    destreza4_4_6 = Destreza.objects.get(codigo="LL.4.4.6.")
    destreza4_4_7 = Destreza.objects.get(codigo="LL.4.4.7.")
    destreza4_4_8 = Destreza.objects.get(codigo="LL.4.4.8.")
    destreza4_4_9 = Destreza.objects.get(codigo="LL.4.4.9.")
    destreza4_4_10 = Destreza.objects.get(codigo="LL.4.4.10.")
    destreza4_4_11 = Destreza.objects.get(codigo="LL.4.4.11.")
    destreza4_5_1 = Destreza.objects.get(codigo="LL.4.5.1.")
    destreza4_5_2 = Destreza.objects.get(codigo="LL.4.5.2.")
    destreza4_5_3 = Destreza.objects.get(codigo="LL.4.5.3.")
    destreza4_5_4 = Destreza.objects.get(codigo="LL.4.5.4.")
    destreza4_5_5 = Destreza.objects.get(codigo="LL.4.5.5.")
    destreza4_5_6 = Destreza.objects.get(codigo="LL.4.5.6.")
    destreza4_5_7 = Destreza.objects.get(codigo="LL.4.5.7.")
    destreza5_1_1 = Destreza.objects.get(codigo="LL.5.1.1.")
    destreza5_1_2 = Destreza.objects.get(codigo="LL.5.1.2.")
    destreza5_1_3 = Destreza.objects.get(codigo="LL.5.1.3.")
    destreza5_1_4 = Destreza.objects.get(codigo="LL.5.1.4.")
    destreza5_2_1 = Destreza.objects.get(codigo="LL.5.2.1.")
    destreza5_2_2 = Destreza.objects.get(codigo="LL.5.2.2.")
    destreza5_2_3 = Destreza.objects.get(codigo="LL.5.2.3.")
    destreza5_2_4 = Destreza.objects.get(codigo="LL.5.2.4.")
    destreza5_3_1 = Destreza.objects.get(codigo="LL.5.3.1.")
    destreza5_3_2 = Destreza.objects.get(codigo="LL.5.3.2.")
    destreza5_3_3 = Destreza.objects.get(codigo="LL.5.3.3.")
    destreza5_3_4 = Destreza.objects.get(codigo="LL.5.3.4.")
    destreza5_3_5 = Destreza.objects.get(codigo="LL.5.3.5.")
    destreza5_3_6 = Destreza.objects.get(codigo="LL.5.3.6.")
    destreza5_4_1 = Destreza.objects.get(codigo="LL.5.4.1.")
    destreza5_4_2 = Destreza.objects.get(codigo="LL.5.4.2.")
    destreza5_4_3 = Destreza.objects.get(codigo="LL.5.4.3.")
    destreza5_4_4 = Destreza.objects.get(codigo="LL.5.4.4.")
    destreza5_4_5 = Destreza.objects.get(codigo="LL.5.4.5.")
    destreza5_4_6 = Destreza.objects.get(codigo="LL.5.4.6.")
    destreza5_4_7 = Destreza.objects.get(codigo="LL.5.4.7.")
    destreza5_4_8 = Destreza.objects.get(codigo="LL.5.4.8.")
    destreza5_5_1 = Destreza.objects.get(codigo="LL.5.5.1.")
    destreza5_5_2 = Destreza.objects.get(codigo="LL.5.5.2.")
    destreza5_5_3 = Destreza.objects.get(codigo="LL.5.5.3.")
    destreza5_5_4 = Destreza.objects.get(codigo="LL.5.5.4.")
    destreza5_5_5 = Destreza.objects.get(codigo="LL.5.5.5.")

    # Asignación

    # Preparatoria
    criterio1_1.objetivos_generales.add(
        objetivo1,
    )
    criterio1_1.destrezas.add(
        destreza1_5_1,
        destreza1_5_2,
    )

    criterio1_2.objetivos_generales.add(
        objetivo2,
    )
    criterio1_2.destrezas.add(
        destreza1_5_3,
        destreza1_5_4,
    )

    criterio1_3.objetivos_generales.add(
        objetivo3,
        objetivo4,
    )
    criterio1_3.destrezas.add(
        destreza1_5_5,
        destreza1_5_6,
        destreza1_5_7,
    )

    criterio1_4.objetivos_generales.add(
        objetivo5,
        objetivo6,
    )
    criterio1_4.destrezas.add(
        destreza1_5_8,
        destreza1_5_9,
        destreza1_5_10,
        destreza1_5_11,
        destreza1_5_12,
    )

    criterio1_5.objetivos_generales.add(
        objetivo5,
        objetivo6,
    )
    criterio1_5.destrezas.add(
        destreza1_5_13,
        destreza1_5_14,
        destreza1_5_15,
    )

    criterio1_6.objetivos_generales.add(
        objetivo5,
        objetivo6,
    )
    criterio1_6.destrezas.add(
        destreza1_5_16,
        destreza1_5_17,
        destreza1_5_18,
        destreza1_5_19,
    )

    criterio1_7.objetivos_generales.add(
        objetivo9,
        objetivo10,
        objetivo11,
    )
    criterio1_7.destrezas.add(
        destreza1_5_20,
        destreza1_5_21,
        destreza1_5_22,
    )

    # Media
    criterio2_1.objetivos_generales.add(
        objetivo1,
    )
    criterio2_1.destrezas.add(
        destreza2_1_1,
        destreza2_1_2,
    )

    criterio2_2.objetivos_generales.add(
        objetivo2,
    )
    criterio2_2.destrezas.add(
        destreza2_1_3,
        destreza2_1_4,
    )

    criterio2_3.objetivos_generales.add(
        objetivo3,
    )
    criterio2_3.destrezas.add(
        destreza2_2_1,
        destreza2_2_2,
        destreza2_2_3,
        destreza2_2_4,
    )

    criterio2_4.objetivos_generales.add(
        objetivo4,
    )
    criterio2_4.destrezas.add(
        destreza2_2_5,
        destreza2_2_6,
    )

    criterio2_5.objetivos_generales.add(
        objetivo5,
    )
    criterio2_5.destrezas.add(
        destreza2_3_1,
        destreza2_3_2,
        destreza2_3_3,
        destreza2_3_4,
        destreza2_3_5,
        destreza2_3_6,
    )

    criterio2_6.objetivos_generales.add(
        objetivo5,
    )
    criterio2_6.destrezas.add(
        destreza2_3_8,
        destreza2_3_9,
        destreza2_3_10,
    )

    criterio2_7.objetivos_generales.add(
        objetivo6,
    )
    criterio2_7.destrezas.add(
        destreza2_3_7,
        destreza2_3_11,
    )

    criterio2_8.objetivos_generales.add(
        objetivo7,
    )
    criterio2_8.destrezas.add(
        destreza2_4_1,
        destreza2_4_2,
        destreza2_4_6,
    )

    criterio2_9.objetivos_generales.add(
        objetivo8,
    )
    criterio2_9.destrezas.add(
        destreza2_4_3,
        destreza2_4_4,
        destreza2_4_5,
        destreza2_4_7,
    )

    criterio2_10.objetivos_generales.add(
        objetivo9,
        objetivo10,
    )
    criterio2_10.destrezas.add(
        destreza2_5_1,
        destreza2_5_2,
    )

    criterio2_11.objetivos_generales.add(
        objetivo11,
    )
    criterio2_11.destrezas.add(
        destreza2_5_3,
        destreza2_5_4,
        destreza2_5_5,
    )

    # Media
    criterio3_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
    )
    criterio3_1.destrezas.add(
        destreza3_1_1,
        destreza3_1_2,
        destreza3_1_3,
    )

    criterio3_2.objetivos_generales.add(
        objetivo3,
        objetivo4,
    )
    criterio3_2.destrezas.add(
        destreza3_2_1,
        destreza3_2_2,
        destreza3_2_3,
        destreza3_2_4,
        destreza3_2_5,
    )

    criterio3_3.objetivos_generales.add(
        objetivo5,
    )
    criterio3_3.destrezas.add(
        destreza3_3_1,
        destreza3_3_2,
        destreza3_3_3,
        destreza3_3_4,
        destreza3_3_5,
        destreza3_3_10,
    )

    criterio3_4.objetivos_generales.add(
        objetivo5,
    )
    criterio3_4.destrezas.add(
        destreza3_3_8,
        destreza3_3_11,
    )

    criterio3_5.objetivos_generales.add(
        objetivo6,
    )
    criterio3_5.destrezas.add(
        destreza3_3_6,
        destreza3_3_7,
        destreza3_3_9,
    )

    criterio3_6.objetivos_generales.add(
        objetivo7,
        objetivo8,
    )
    criterio3_6.destrezas.add(
        destreza3_4_1,
        destreza3_4_2,
        destreza3_4_3,
        destreza3_4_4,
        destreza3_4_5,
        destreza3_4_6,
        destreza3_4_7,
        destreza3_4_8,
        destreza3_4_9,
        destreza3_4_10,
        destreza3_4_11,
        destreza3_4_12,
        destreza3_4_13,
        destreza3_4_14,
    )

    criterio3_7.objetivos_generales.add(
        objetivo9,
        objetivo10,
    )
    criterio3_7.destrezas.add(
        destreza3_5_1,
        destreza3_5_2,
        destreza3_5_3,
    )

    criterio3_8.objetivos_generales.add(
        objetivo11,
    )
    criterio3_8.destrezas.add(
        destreza3_5_4,
        destreza3_5_5,
        destreza3_5_6,
    )

    # Superior
    criterio4_1.objetivos_generales.add(
        objetivo1,
    )
    criterio4_1.destrezas.add(
        destreza4_1_1,
        destreza4_1_2,
    )

    criterio4_2.objetivos_generales.add(
        objetivo2,
    )
    criterio4_2.destrezas.add(
        destreza4_1_3,
        destreza4_1_4,
    )

    criterio4_3.objetivos_generales.add(
        objetivo3,
    )
    criterio4_3.destrezas.add(
        destreza4_2_4,
        destreza4_2_6,
    )

    criterio4_4.objetivos_generales.add(
        objetivo4,
    )
    criterio4_4.destrezas.add(
        destreza4_2_1,
        destreza4_2_2,
        destreza4_2_3,
        destreza4_2_5,
    )

    criterio4_5.objetivos_generales.add(
        objetivo5,
    )
    criterio4_5.destrezas.add(
        destreza4_3_1,
        destreza4_3_2,
        destreza4_3_3,
        destreza4_3_4,
        destreza4_3_8,
        destreza4_3_9,
    )

    criterio4_6.objetivos_generales.add(
        objetivo6,
    )
    criterio4_6.destrezas.add(
        destreza4_3_5,
        destreza4_3_6,
        destreza4_3_7,
        destreza4_3_10,
    )

    criterio4_7.objetivos_generales.add(
        objetivo7,
        objetivo8,
    )
    criterio4_7.destrezas.add(
        destreza4_4_1,
        destreza4_4_2,
        destreza4_4_3,
        destreza4_4_4,
        destreza4_4_5,
        destreza4_4_6,
        destreza4_4_7,
        destreza4_4_8,
        destreza4_4_9,
        destreza4_4_10,
        destreza4_4_11,
    )

    criterio4_8.objetivos_generales.add(
        objetivo9,
        objetivo10,
    )
    criterio4_8.destrezas.add(
        destreza4_5_1,
        destreza4_5_2,
        destreza4_5_3,
    )

    criterio4_9.objetivos_generales.add(
        objetivo11,
    )
    criterio4_9.destrezas.add(
        destreza4_5_4,
        destreza4_5_5,
        destreza4_5_6,
        destreza4_5_7,
    )

    # Bachillerato
    criterio5_1.objetivos_generales.add(
        objetivo1,
    )
    criterio5_1.destrezas.add(
        destreza5_1_1,
        destreza5_1_2,
    )

    criterio5_2.objetivos_generales.add(
        objetivo2,
    )
    criterio5_2.destrezas.add(
        destreza5_1_3,
        destreza5_1_4,
    )

    criterio5_3.objetivos_generales.add(
        objetivo3,
        objetivo4,
    )
    criterio5_3.destrezas.add(
        destreza5_2_1,
        destreza5_2_2,
        destreza5_2_3,
        destreza5_2_4,
    )

    criterio5_4.objetivos_generales.add(
        objetivo5,
    )
    criterio5_4.destrezas.add(
        destreza5_3_1,
        destreza5_3_2,
        destreza5_3_3,
        destreza5_3_4,
        destreza5_3_6,
    )

    criterio5_5.objetivos_generales.add(
        objetivo6,
    )
    criterio5_5.destrezas.add(
        destreza5_3_5,
        destreza5_3_6,
    )

    criterio5_6.objetivos_generales.add(
        objetivo7,
        objetivo8,
    )
    criterio5_6.destrezas.add(
        destreza5_4_1,
        destreza5_4_2,
        destreza5_4_3,
        destreza5_4_4,
        destreza5_4_5,
        destreza5_4_6,
        destreza5_4_7,
        destreza5_4_8,
    )

    criterio5_7.objetivos_generales.add(
        objetivo9,
        objetivo10,
    )
    criterio5_7.destrezas.add(
        destreza5_5_1,
        destreza5_5_2,
        destreza5_5_3,
    )

    criterio5_8.objetivos_generales.add(
        objetivo11,
    )
    criterio5_8.destrezas.add(
        destreza5_5_4,
        destreza5_5_5,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0059_auto_20180908_1237'),
    ]

    operations = [
        migrations.RunPython(create_relationships)
    ]
