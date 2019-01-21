from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales
    objetivo1 = ObjetivoGeneral.objects.get(codigo="OG.EF.1.")
    objetivo2 = ObjetivoGeneral.objects.get(codigo="OG.EF.2.")
    objetivo3 = ObjetivoGeneral.objects.get(codigo="OG.EF.3.")
    objetivo4 = ObjetivoGeneral.objects.get(codigo="OG.EF.4.")
    objetivo5 = ObjetivoGeneral.objects.get(codigo="OG.EF.5.")
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.EF.6.")
    objetivo7 = ObjetivoGeneral.objects.get(codigo="OG.EF.7.")
    objetivo8 = ObjetivoGeneral.objects.get(codigo="OG.EF.8.")
    objetivo9 = ObjetivoGeneral.objects.get(codigo="OG.EF.9.")

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.EF.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.EF.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.EF.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.EF.1.4.")
    criterio1_5 = CriterioEvaluacion.objects.get(codigo="CE.EF.1.5.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.6.")
    criterio2_7 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.7.")
    criterio2_8 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.8.")
    criterio2_9 = CriterioEvaluacion.objects.get(codigo="CE.EF.2.9.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.EF.3.7.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.EF.4.8.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.4.")
    criterio5_5 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.5.")
    criterio5_6 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.6.")
    criterio5_7 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.7.")
    criterio5_8 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.8.")
    criterio5_9 = CriterioEvaluacion.objects.get(codigo="CE.EF.5.9.")

    # Destrezas
    destreza1_1_1 = Destreza.objects.get(codigo="EF.1.1.1.")
    destreza1_1_2 = Destreza.objects.get(codigo="EF.1.1.2.")
    destreza1_1_3 = Destreza.objects.get(codigo="EF.1.1.3.")
    destreza1_1_4 = Destreza.objects.get(codigo="EF.1.1.4.")
    destreza1_1_5 = Destreza.objects.get(codigo="EF.1.1.5.")
    destreza1_1_6 = Destreza.objects.get(codigo="EF.1.1.6.")
    destreza1_2_1 = Destreza.objects.get(codigo="EF.1.2.1.")
    destreza1_2_2 = Destreza.objects.get(codigo="EF.1.2.2.")
    destreza1_2_3 = Destreza.objects.get(codigo="EF.1.2.3.")
    destreza1_2_4 = Destreza.objects.get(codigo="EF.1.2.4.")
    destreza1_2_5 = Destreza.objects.get(codigo="EF.1.2.5.")
    destreza1_2_6 = Destreza.objects.get(codigo="EF.1.2.6.")
    destreza1_3_1 = Destreza.objects.get(codigo="EF.1.3.1.")
    destreza1_3_2 = Destreza.objects.get(codigo="EF.1.3.2.")
    destreza1_3_3 = Destreza.objects.get(codigo="EF.1.3.3.")
    destreza1_3_4 = Destreza.objects.get(codigo="EF.1.3.4.")
    destreza1_3_5 = Destreza.objects.get(codigo="EF.1.3.5.")
    destreza1_3_6 = Destreza.objects.get(codigo="EF.1.3.6.")
    destreza1_3_7 = Destreza.objects.get(codigo="EF.1.3.7.")
    destreza1_5_1 = Destreza.objects.get(codigo="EF.1.5.1.")
    destreza1_5_2 = Destreza.objects.get(codigo="EF.1.5.2.")
    destreza1_5_3 = Destreza.objects.get(codigo="EF.1.5.3.")
    destreza1_5_4 = Destreza.objects.get(codigo="EF.1.5.4.")
    destreza1_6_1 = Destreza.objects.get(codigo="EF.1.6.1.")
    destreza1_6_2 = Destreza.objects.get(codigo="EF.1.6.2.")
    destreza2_1_1 = Destreza.objects.get(codigo="EF.2.1.1.")
    destreza2_1_2 = Destreza.objects.get(codigo="EF.2.1.2.")
    destreza2_1_3 = Destreza.objects.get(codigo="EF.2.1.3.")
    destreza2_1_4 = Destreza.objects.get(codigo="EF.2.1.4.")
    destreza2_1_5 = Destreza.objects.get(codigo="EF.2.1.5.")
    destreza2_1_6 = Destreza.objects.get(codigo="EF.2.1.6.")
    destreza2_1_7 = Destreza.objects.get(codigo="EF.2.1.7.")
    destreza2_1_8 = Destreza.objects.get(codigo="EF.2.1.8.")
    destreza2_1_9 = Destreza.objects.get(codigo="EF.2.1.9.")
    destreza2_1_10 = Destreza.objects.get(codigo="EF.2.1.10.")
    destreza2_2_1 = Destreza.objects.get(codigo="EF.2.2.1.")
    destreza2_2_2 = Destreza.objects.get(codigo="EF.2.2.2.")
    destreza2_2_3 = Destreza.objects.get(codigo="EF.2.2.3.")
    destreza2_2_4 = Destreza.objects.get(codigo="EF.2.2.4.")
    destreza2_2_5 = Destreza.objects.get(codigo="EF.2.2.5.")
    destreza2_2_6 = Destreza.objects.get(codigo="EF.2.2.6.")
    destreza2_2_7 = Destreza.objects.get(codigo="EF.2.2.7.")
    destreza2_3_1 = Destreza.objects.get(codigo="EF.2.3.1.")
    destreza2_3_2 = Destreza.objects.get(codigo="EF.2.3.2.")
    destreza2_3_3 = Destreza.objects.get(codigo="EF.2.3.3.")
    destreza2_3_4 = Destreza.objects.get(codigo="EF.2.3.4.")
    destreza2_3_5 = Destreza.objects.get(codigo="EF.2.3.5.")
    destreza2_3_6 = Destreza.objects.get(codigo="EF.2.3.6.")
    destreza2_3_7 = Destreza.objects.get(codigo="EF.2.3.7.")
    destreza2_3_8 = Destreza.objects.get(codigo="EF.2.3.8.")
    destreza2_3_9 = Destreza.objects.get(codigo="EF.2.3.9.")
    destreza2_5_1 = Destreza.objects.get(codigo="EF.2.5.1.")
    destreza2_5_2 = Destreza.objects.get(codigo="EF.2.5.2.")
    destreza2_5_3 = Destreza.objects.get(codigo="EF.2.5.3.")
    destreza2_5_4 = Destreza.objects.get(codigo="EF.2.5.4.")
    destreza2_5_5 = Destreza.objects.get(codigo="EF.2.5.5.")
    destreza2_5_6 = Destreza.objects.get(codigo="EF.2.5.6.")
    destreza2_5_7 = Destreza.objects.get(codigo="EF.2.5.7.")
    destreza2_6_1 = Destreza.objects.get(codigo="EF.2.6.1.")
    destreza2_6_2 = Destreza.objects.get(codigo="EF.2.6.2.")
    destreza2_6_3 = Destreza.objects.get(codigo="EF.2.6.3.")
    destreza2_6_4 = Destreza.objects.get(codigo="EF.2.6.4.")
    destreza2_6_5 = Destreza.objects.get(codigo="EF.2.6.5.")
    destreza2_6_6 = Destreza.objects.get(codigo="EF.2.6.6.")
    destreza3_1_1 = Destreza.objects.get(codigo="EF.3.1.1.")
    destreza3_1_2 = Destreza.objects.get(codigo="EF.3.1.2.")
    destreza3_1_3 = Destreza.objects.get(codigo="EF.3.1.3.")
    destreza3_1_4 = Destreza.objects.get(codigo="EF.3.1.4.")
    destreza3_1_5 = Destreza.objects.get(codigo="EF.3.1.5.")
    destreza3_1_6 = Destreza.objects.get(codigo="EF.3.1.6.")
    destreza3_1_7 = Destreza.objects.get(codigo="EF.3.1.7.")
    destreza3_1_8 = Destreza.objects.get(codigo="EF.3.1.8.")
    destreza3_1_9 = Destreza.objects.get(codigo="EF.3.1.9.")
    destreza3_1_10 = Destreza.objects.get(codigo="EF.3.1.10.")
    destreza3_2_1 = Destreza.objects.get(codigo="EF.3.2.1.")
    destreza3_2_2 = Destreza.objects.get(codigo="EF.3.2.2.")
    destreza3_2_3 = Destreza.objects.get(codigo="EF.3.2.3.")
    destreza3_2_4 = Destreza.objects.get(codigo="EF.3.2.4.")
    destreza3_2_5 = Destreza.objects.get(codigo="EF.3.2.5.")
    destreza3_2_6 = Destreza.objects.get(codigo="EF.3.2.6.")
    destreza3_2_7 = Destreza.objects.get(codigo="EF.3.2.7.")
    destreza3_3_1 = Destreza.objects.get(codigo="EF.3.3.1.")
    destreza3_3_2 = Destreza.objects.get(codigo="EF.3.3.2.")
    destreza3_3_3 = Destreza.objects.get(codigo="EF.3.3.3.")
    destreza3_3_4 = Destreza.objects.get(codigo="EF.3.3.4.")
    destreza3_3_5 = Destreza.objects.get(codigo="EF.3.3.5.")
    destreza3_3_6 = Destreza.objects.get(codigo="EF.3.3.6.")
    destreza3_4_1 = Destreza.objects.get(codigo="EF.3.4.1.")
    destreza3_4_2 = Destreza.objects.get(codigo="EF.3.4.2.")
    destreza3_4_3 = Destreza.objects.get(codigo="EF.3.4.3.")
    destreza3_4_4 = Destreza.objects.get(codigo="EF.3.4.4.")
    destreza3_4_5 = Destreza.objects.get(codigo="EF.3.4.5.")
    destreza3_4_6 = Destreza.objects.get(codigo="EF.3.4.6.")
    destreza3_4_7 = Destreza.objects.get(codigo="EF.3.4.7.")
    destreza3_5_1 = Destreza.objects.get(codigo="EF.3.5.1.")
    destreza3_5_2 = Destreza.objects.get(codigo="EF.3.5.2.")
    destreza3_5_3 = Destreza.objects.get(codigo="EF.3.5.3.")
    destreza3_5_4 = Destreza.objects.get(codigo="EF.3.5.4.")
    destreza3_5_5 = Destreza.objects.get(codigo="EF.3.5.5.")
    destreza3_6_1 = Destreza.objects.get(codigo="EF.3.6.1.")
    destreza3_6_2 = Destreza.objects.get(codigo="EF.3.6.2.")
    destreza3_6_3 = Destreza.objects.get(codigo="EF.3.6.3.")
    destreza3_6_4 = Destreza.objects.get(codigo="EF.3.6.4.")
    destreza3_6_5 = Destreza.objects.get(codigo="EF.3.6.5.")
    destreza4_1_1 = Destreza.objects.get(codigo="EF.4.1.1.")
    destreza4_1_2 = Destreza.objects.get(codigo="EF.4.1.2.")
    destreza4_1_3 = Destreza.objects.get(codigo="EF.4.1.3.")
    destreza4_1_4 = Destreza.objects.get(codigo="EF.4.1.4.")
    destreza4_1_5 = Destreza.objects.get(codigo="EF.4.1.5.")
    destreza4_1_6 = Destreza.objects.get(codigo="EF.4.1.6.")
    destreza4_1_7 = Destreza.objects.get(codigo="EF.4.1.7.")
    destreza4_1_8 = Destreza.objects.get(codigo="EF.4.1.8.")
    destreza4_1_9 = Destreza.objects.get(codigo="EF.4.1.9.")
    destreza4_2_1 = Destreza.objects.get(codigo="EF.4.2.1.")
    destreza4_2_2 = Destreza.objects.get(codigo="EF.4.2.2.")
    destreza4_2_3 = Destreza.objects.get(codigo="EF.4.2.3.")
    destreza4_2_4 = Destreza.objects.get(codigo="EF.4.2.4.")
    destreza4_2_5 = Destreza.objects.get(codigo="EF.4.2.5.")
    destreza4_3_1 = Destreza.objects.get(codigo="EF.4.3.1.")
    destreza4_3_2 = Destreza.objects.get(codigo="EF.4.3.2.")
    destreza4_3_3 = Destreza.objects.get(codigo="EF.4.3.3.")
    destreza4_3_4 = Destreza.objects.get(codigo="EF.4.3.4.")
    destreza4_3_5 = Destreza.objects.get(codigo="EF.4.3.5.")
    destreza4_3_6 = Destreza.objects.get(codigo="EF.4.3.6.")
    destreza4_3_7 = Destreza.objects.get(codigo="EF.4.3.7.")
    destreza4_3_8 = Destreza.objects.get(codigo="EF.4.3.8.")
    destreza4_4_1 = Destreza.objects.get(codigo="EF.4.4.1.")
    destreza4_4_2 = Destreza.objects.get(codigo="EF.4.4.2.")
    destreza4_4_3 = Destreza.objects.get(codigo="EF.4.4.3.")
    destreza4_4_4 = Destreza.objects.get(codigo="EF.4.4.4.")
    destreza4_4_5 = Destreza.objects.get(codigo="EF.4.4.5.")
    destreza4_4_6 = Destreza.objects.get(codigo="EF.4.4.6.")
    destreza4_4_7 = Destreza.objects.get(codigo="EF.4.4.7.")
    destreza4_5_1 = Destreza.objects.get(codigo="EF.4.5.1.")
    destreza4_5_2 = Destreza.objects.get(codigo="EF.4.5.2.")
    destreza4_5_3 = Destreza.objects.get(codigo="EF.4.5.3.")
    destreza4_5_4 = Destreza.objects.get(codigo="EF.4.5.4.")
    destreza4_6_1 = Destreza.objects.get(codigo="EF.4.6.1.")
    destreza4_6_2 = Destreza.objects.get(codigo="EF.4.6.2.")
    destreza4_6_3 = Destreza.objects.get(codigo="EF.4.6.3.")
    destreza4_6_4 = Destreza.objects.get(codigo="EF.4.6.4.")
    destreza4_6_5 = Destreza.objects.get(codigo="EF.4.6.5.")
    destreza4_6_6 = Destreza.objects.get(codigo="EF.4.6.6.")
    destreza5_1_1 = Destreza.objects.get(codigo="EF.5.1.1.")
    destreza5_1_2 = Destreza.objects.get(codigo="EF.5.1.2.")
    destreza5_1_3 = Destreza.objects.get(codigo="EF.5.1.3.")
    destreza5_1_4 = Destreza.objects.get(codigo="EF.5.1.4.")
    destreza5_1_5 = Destreza.objects.get(codigo="EF.5.1.5.")
    destreza5_2_1 = Destreza.objects.get(codigo="EF.5.2.1.")
    destreza5_2_2 = Destreza.objects.get(codigo="EF.5.2.2.")
    destreza5_2_3 = Destreza.objects.get(codigo="EF.5.2.3.")
    destreza5_2_4 = Destreza.objects.get(codigo="EF.5.2.4.")
    destreza5_2_5 = Destreza.objects.get(codigo="EF.5.2.5.")
    destreza5_3_1 = Destreza.objects.get(codigo="EF.5.3.1.")
    destreza5_3_2 = Destreza.objects.get(codigo="EF.5.3.2.")
    destreza5_3_3 = Destreza.objects.get(codigo="EF.5.3.3.")
    destreza5_3_4 = Destreza.objects.get(codigo="EF.5.3.4.")
    destreza5_3_5 = Destreza.objects.get(codigo="EF.5.3.5.")
    destreza5_3_6 = Destreza.objects.get(codigo="EF.5.3.6.")
    destreza5_4_1 = Destreza.objects.get(codigo="EF.5.4.1.")
    destreza5_4_2 = Destreza.objects.get(codigo="EF.5.4.2.")
    destreza5_4_3 = Destreza.objects.get(codigo="EF.5.4.3.")
    destreza5_4_4 = Destreza.objects.get(codigo="EF.5.4.4.")
    destreza5_4_5 = Destreza.objects.get(codigo="EF.5.4.5.")
    destreza5_4_6 = Destreza.objects.get(codigo="EF.5.4.6.")
    destreza5_4_7 = Destreza.objects.get(codigo="EF.5.4.7.")
    destreza5_4_8 = Destreza.objects.get(codigo="EF.5.4.8.")
    destreza5_4_9 = Destreza.objects.get(codigo="EF.5.4.9.")
    destreza5_5_1 = Destreza.objects.get(codigo="EF.5.5.1.")
    destreza5_5_2 = Destreza.objects.get(codigo="EF.5.5.2.")
    destreza5_5_3 = Destreza.objects.get(codigo="EF.5.5.3.")
    destreza5_5_4 = Destreza.objects.get(codigo="EF.5.5.4.")
    destreza5_5_5 = Destreza.objects.get(codigo="EF.5.5.5.")
    destreza5_5_6 = Destreza.objects.get(codigo="EF.5.5.6.")
    destreza5_6_1 = Destreza.objects.get(codigo="EF.5.6.1.")
    destreza5_6_2 = Destreza.objects.get(codigo="EF.5.6.2.")
    destreza5_6_3 = Destreza.objects.get(codigo="EF.5.6.3.")
    destreza5_6_4 = Destreza.objects.get(codigo="EF.5.6.4.")
    destreza5_6_5 = Destreza.objects.get(codigo="EF.5.6.5.")
    destreza5_6_6 = Destreza.objects.get(codigo="EF.5.6.6.")
    destreza5_6_7 = Destreza.objects.get(codigo="EF.5.6.7.")

    # Asignación

    # Preparatoria
    criterio1_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo7,
        objetivo8,
    )
    criterio1_1.destrezas.add(
        destreza1_1_1,
        destreza1_1_2,
        destreza1_1_3,
        destreza1_1_4,
        destreza1_1_5,
        destreza1_1_6,
        destreza1_5_2,
        destreza1_5_4,
        destreza1_6_1,
        destreza1_6_2,
    )

    criterio1_2.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio1_2.destrezas.add(
        destreza1_2_1,
        destreza1_2_2,
        destreza1_2_3,
        destreza1_2_4,
        destreza1_2_5,
        destreza1_2_6,
        destreza1_5_1,
        destreza1_5_2,
        destreza1_5_4,
        destreza1_6_1,
        destreza1_6_2,
    )

    criterio1_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio1_3.destrezas.add(
        destreza1_3_1,
        destreza1_3_2,
        destreza1_3_3,
        destreza1_3_4,
        destreza1_3_5,
        destreza1_3_6,
        destreza1_3_7,
        destreza1_5_1,
        destreza1_5_2,
        destreza1_5_3,
        destreza1_6_1,
        destreza1_6_2,
    )

    criterio1_4.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
    )
    criterio1_4.destrezas.add(
        destreza1_5_1,
        destreza1_5_2,
        destreza1_5_3,
        destreza1_5_4,
    )

    criterio1_5.objetivos_generales.add(
        objetivo1,
        objetivo6,
        objetivo8,
    )
    criterio1_5.destrezas.add(
        destreza1_6_1,
        destreza1_6_2,
    )

    # Elemental
    criterio2_1.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio2_1.destrezas.add(
        destreza2_1_1,
        destreza2_1_2,
        destreza2_1_3,
        destreza2_1_8,
        destreza2_1_9,
        destreza2_1_10,
        destreza2_5_5,
        destreza2_5_7,
        destreza2_6_1,
        destreza2_6_5,
    )

    criterio2_2.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio2_2.destrezas.add(
        destreza2_1_4,
        destreza2_1_5,
        destreza2_1_6,
        destreza2_1_7,
        destreza2_5_6,
        destreza2_5_7,
        destreza2_6_5,
        destreza2_6_6,
    )

    criterio2_3.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio2_3.destrezas.add(
        destreza2_2_1,
        destreza2_2_4,
        destreza2_2_6,
        destreza2_2_7,
        destreza2_5_3,
        destreza2_5_4,
        destreza2_5_5,
        destreza2_5_6,
        destreza2_5_7,
        destreza2_6_1,
        destreza2_6_4,
        destreza2_6_5,
    )

    criterio2_4.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio2_4.destrezas.add(
        destreza2_2_2,
        destreza2_2_3,
        destreza2_2_5,
        destreza2_5_1,
        destreza2_5_3,
        destreza2_6_4,
        destreza2_6_5,
    )

    criterio2_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio2_5.destrezas.add(
        destreza2_3_1,
        destreza2_3_2,
        destreza2_3_5,
        destreza2_3_6,
        destreza2_3_8,
        destreza2_3_9,
        destreza2_5_2,
        destreza2_5_3,
        destreza2_5_5,
        destreza2_6_1,
        destreza2_6_5,
    )

    criterio2_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo7,
        objetivo9,
    )
    criterio2_6.destrezas.add(
        destreza2_3_3,
        destreza2_3_4,
        destreza2_3_7,
        destreza2_5_5,
        destreza2_5_7,
    )

    criterio2_7.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
    )
    criterio2_7.destrezas.add(
        destreza2_5_1,
        destreza2_5_2,
        destreza2_5_3,
        destreza2_5_4,
    )

    criterio2_8.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio2_8.destrezas.add(
        destreza2_5_5,
        destreza2_5_6,
        destreza2_5_7,
    )

    criterio2_9.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio2_9.destrezas.add(
        destreza2_6_1,
        destreza2_6_2,
        destreza2_6_3,
        destreza2_6_4,
        destreza2_6_5,
        destreza2_6_6,
    )

    # Media
    criterio3_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio3_1.destrezas.add(
        destreza3_1_1,
        destreza3_1_2,
        destreza3_1_3,
        destreza3_1_4,
        destreza3_1_5,
        destreza3_1_9,
        destreza3_6_4,
    )

    criterio3_2.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio3_2.destrezas.add(
        destreza3_1_6,
        destreza3_1_7,
        destreza3_1_8,
        destreza3_1_10,
        destreza3_5_1,
        destreza3_5_2,
        destreza3_5_4,
        destreza3_6_1,
        destreza3_6_4,
    )

    criterio3_3.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio3_3.destrezas.add(
        destreza3_2_1,
        destreza3_2_2,
        destreza3_2_3,
        destreza3_2_4,
        destreza3_2_5,
        destreza3_2_6,
        destreza3_2_7,
        destreza3_5_1,
        destreza3_5_3,
        destreza3_6_2,
        destreza3_6_3,
        destreza3_6_4,
    )

    criterio3_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio3_4.destrezas.add(
        destreza3_3_1,
        destreza3_3_2,
        destreza3_3_3,
        destreza3_3_4,
        destreza3_3_5,
        destreza3_3_6,
        destreza3_5_2,
        destreza3_5_3,
        destreza3_6_1,
        destreza3_6_4,
    )

    criterio3_5.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio3_5.destrezas.add(
        destreza3_4_1,
        destreza3_4_2,
        destreza3_4_3,
        destreza3_4_4,
        destreza3_4_5,
        destreza3_4_6,
        destreza3_4_7,
        destreza3_5_3,
        destreza3_5_4,
        destreza3_6_1,
        destreza3_6_2,
        destreza3_6_3,
        destreza3_6_4,
    )

    criterio3_6.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio3_6.destrezas.add(
        destreza3_5_1,
        destreza3_5_2,
        destreza3_5_3,
        destreza3_5_4,
        destreza3_5_5,
    )

    criterio3_7.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio3_7.destrezas.add(
        destreza3_6_1,
        destreza3_6_2,
        destreza3_6_3,
        destreza3_6_4,
        destreza3_6_5,
    )

    # Superior
    criterio4_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio4_1.destrezas.add(
        destreza4_1_1,
        destreza4_1_3,
        destreza4_1_4,
        destreza4_1_8,
        destreza4_1_9,
        destreza4_5_2,
        destreza4_6_1,
        destreza4_6_6,
    )

    criterio4_2.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio4_2.destrezas.add(
        destreza4_1_2,
        destreza4_1_5,
        destreza4_1_6,
        destreza4_1_7,
        destreza4_5_4,
        destreza4_6_1,
    )

    criterio4_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio4_3.destrezas.add(
        destreza4_2_1,
        destreza4_2_2,
        destreza4_2_3,
        destreza4_2_4,
        destreza4_2_5,
        destreza4_5_1,
        destreza4_6_4,
        destreza4_6_6,
    )

    criterio4_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio4_4.destrezas.add(
        destreza4_3_1,
        destreza4_3_2,
        destreza4_3_4,
        destreza4_3_5,
        destreza4_5_1,
        destreza4_5_2,
        destreza4_6_1,
    )

    criterio4_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio4_5.destrezas.add(
        destreza4_3_3,
        destreza4_3_6,
        destreza4_3_7,
        destreza4_3_8,
        destreza4_5_1,
        destreza4_5_2,
        destreza4_6_2,
    )

    criterio4_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio4_5.destrezas.add(
        destreza4_3_3,
        destreza4_3_6,
        destreza4_3_7,
        destreza4_3_8,
        destreza4_5_1,
        destreza4_5_2,
        destreza4_6_2,
    )

    criterio4_6.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
    )
    criterio4_6.destrezas.add(
        destreza4_4_1,
        destreza4_4_2,
        destreza4_4_3,
        destreza4_4_4,
        destreza4_4_5,
        destreza4_4_6,
        destreza4_4_7,
        destreza4_5_1,
        destreza4_6_1,
        destreza4_6_4,
        destreza4_6_6,
    )

    criterio4_7.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio4_7.destrezas.add(
        destreza4_5_1,
        destreza4_5_2,
        destreza4_5_3,
        destreza4_5_4,
    )

    criterio4_8.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio4_8.destrezas.add(
        destreza4_6_1,
        destreza4_6_2,
        destreza4_6_3,
        destreza4_6_4,
        destreza4_6_5,
        destreza4_6_6,
    )

    # Bachillerato
    criterio5_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo8,
        objetivo9,
    )
    criterio5_1.destrezas.add(
        destreza5_1_1,
        destreza5_1_2,
        destreza5_1_3,
        destreza5_1_4,
        destreza5_1_5,
        destreza5_5_2,
        destreza5_5_4,
        destreza5_6_4,
    )

    criterio5_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio5_2.destrezas.add(
        destreza5_2_1,
        destreza5_2_2,
        destreza5_2_3,
        destreza5_2_4,
        destreza5_2_5,
        destreza5_5_1,
        destreza5_5_3,
        destreza5_6_1,
        destreza5_6_6,
    )

    criterio5_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
        objetivo9,
    )
    criterio5_3.destrezas.add(
        destreza5_3_1,
        destreza5_3_3,
        destreza5_3_4,
        destreza5_5_5,
        destreza5_6_1,
    )

    criterio5_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio5_4.destrezas.add(
        destreza5_3_2,
        destreza5_3_5,
        destreza5_3_6,
        destreza5_5_5,
        destreza5_6_1,
    )

    criterio5_5.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
        objetivo9,
    )
    criterio5_5.destrezas.add(
        destreza5_4_1,
        destreza5_4_2,
        destreza5_4_3,
        destreza5_4_4,
        destreza5_4_5,
        destreza5_4_6,
        destreza5_4_7,
        destreza5_4_8,
        destreza5_4_9,
        destreza5_5_2,
        destreza5_5_3,
        destreza5_6_1,
        destreza5_6_3,
    )

    criterio5_6.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
    )
    criterio5_6.destrezas.add(
        destreza5_5_1,
        destreza5_5_2,
        destreza5_5_3,
    )

    criterio5_7.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio5_7.destrezas.add(
        destreza5_5_4,
        destreza5_5_5,
        destreza5_5_6,
    )

    criterio5_8.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo8,
    )
    criterio5_8.destrezas.add(
        destreza5_6_1,
        destreza5_6_2,
        destreza5_6_3,
        destreza5_6_7,
    )

    criterio5_9.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo8,
    )
    criterio5_9.destrezas.add(
        destreza5_6_4,
        destreza5_6_5,
        destreza5_6_6,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0058_auto_20180906_1716'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
