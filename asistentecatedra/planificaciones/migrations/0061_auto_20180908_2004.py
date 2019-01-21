from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales
    objetivo1 = ObjetivoGeneral.objects.get(codigo="OG.M.1.")
    objetivo2 = ObjetivoGeneral.objects.get(codigo="OG.M.2.")
    objetivo3 = ObjetivoGeneral.objects.get(codigo="OG.M.3.")
    objetivo4 = ObjetivoGeneral.objects.get(codigo="OG.M.4.")
    objetivo5 = ObjetivoGeneral.objects.get(codigo="OG.M.5.")
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.M.6.")

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.M.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.M.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.M.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.M.1.4.")
    criterio1_5 = CriterioEvaluacion.objects.get(codigo="CE.M.1.5.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.M.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.M.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.M.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.M.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.M.2.5.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.M.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.M.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.M.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.M.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.M.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.M.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.M.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.M.3.8.")
    criterio3_9 = CriterioEvaluacion.objects.get(codigo="CE.M.3.9.")
    criterio3_10 = CriterioEvaluacion.objects.get(codigo="CE.M.3.10.")
    criterio3_11 = CriterioEvaluacion.objects.get(codigo="CE.M.3.11.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.M.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.M.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.M.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.M.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.M.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.M.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.M.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.M.4.8.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.M.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.M.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.M.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.M.5.4.")
    criterio5_5 = CriterioEvaluacion.objects.get(codigo="CE.M.5.5.")
    criterio5_6 = CriterioEvaluacion.objects.get(codigo="CE.M.5.6.")
    criterio5_7 = CriterioEvaluacion.objects.get(codigo="CE.M.5.7.")
    criterio5_8 = CriterioEvaluacion.objects.get(codigo="CE.M.5.8.")
    criterio5_9 = CriterioEvaluacion.objects.get(codigo="CE.M.5.9.")
    criterio5_10 = CriterioEvaluacion.objects.get(codigo="CE.M.5.10.")
    criterio5_11 = CriterioEvaluacion.objects.get(codigo="CE.M.5.11.")

    # Destrezas
    destreza1_4_1 = Destreza.objects.get(codigo="M.1.4.1.")
    destreza1_4_2 = Destreza.objects.get(codigo="M.1.4.2.")
    destreza1_4_3 = Destreza.objects.get(codigo="M.1.4.3.")
    destreza1_4_4 = Destreza.objects.get(codigo="M.1.4.4.")
    destreza1_4_5 = Destreza.objects.get(codigo="M.1.4.5.")
    destreza1_4_6 = Destreza.objects.get(codigo="M.1.4.6.")
    destreza1_4_7 = Destreza.objects.get(codigo="M.1.4.7.")
    destreza1_4_8 = Destreza.objects.get(codigo="M.1.4.8.")
    destreza1_4_9 = Destreza.objects.get(codigo="M.1.4.9.")
    destreza1_4_10 = Destreza.objects.get(codigo="M.1.4.10.")
    destreza1_4_11 = Destreza.objects.get(codigo="M.1.4.11.")
    destreza1_4_12 = Destreza.objects.get(codigo="M.1.4.12.")
    destreza1_4_13 = Destreza.objects.get(codigo="M.1.4.13.")
    destreza1_4_14 = Destreza.objects.get(codigo="M.1.4.14.")
    destreza1_4_15 = Destreza.objects.get(codigo="M.1.4.15.")
    destreza1_4_16 = Destreza.objects.get(codigo="M.1.4.16.")
    destreza1_4_17 = Destreza.objects.get(codigo="M.1.4.17.")
    destreza1_4_18 = Destreza.objects.get(codigo="M.1.4.18.")
    destreza1_4_19 = Destreza.objects.get(codigo="M.1.4.19.")
    destreza1_4_20 = Destreza.objects.get(codigo="M.1.4.20.")
    destreza1_4_21 = Destreza.objects.get(codigo="M.1.4.21.")
    destreza1_4_22 = Destreza.objects.get(codigo="M.1.4.22.")
    destreza1_4_23 = Destreza.objects.get(codigo="M.1.4.23.")
    destreza1_4_24 = Destreza.objects.get(codigo="M.1.4.24.")
    destreza1_4_25 = Destreza.objects.get(codigo="M.1.4.25.")
    destreza1_4_26 = Destreza.objects.get(codigo="M.1.4.26.")
    destreza1_4_27 = Destreza.objects.get(codigo="M.1.4.27.")
    destreza1_4_28 = Destreza.objects.get(codigo="M.1.4.28.")
    destreza1_4_29 = Destreza.objects.get(codigo="M.1.4.29.")
    destreza1_4_30 = Destreza.objects.get(codigo="M.1.4.30.")
    destreza1_4_31 = Destreza.objects.get(codigo="M.1.4.31.")
    destreza1_4_32 = Destreza.objects.get(codigo="M.1.4.32.")
    destreza1_4_33 = Destreza.objects.get(codigo="M.1.4.33.")
    destreza1_4_34 = Destreza.objects.get(codigo="M.1.4.34.")
    destreza2_1_1 = Destreza.objects.get(codigo="M.2.1.1.")
    destreza2_1_2 = Destreza.objects.get(codigo="M.2.1.2.")
    destreza2_1_3 = Destreza.objects.get(codigo="M.2.1.3.")
    destreza2_1_4 = Destreza.objects.get(codigo="M.2.1.4.")
    destreza2_1_5 = Destreza.objects.get(codigo="M.2.1.5.")
    destreza2_1_6 = Destreza.objects.get(codigo="M.2.1.6.")
    destreza2_1_7 = Destreza.objects.get(codigo="M.2.1.7.")
    destreza2_1_8 = Destreza.objects.get(codigo="M.2.1.8.")
    destreza2_1_9 = Destreza.objects.get(codigo="M.2.1.9.")
    destreza2_1_10 = Destreza.objects.get(codigo="M.2.1.10.")
    destreza2_1_11 = Destreza.objects.get(codigo="M.2.1.11.")
    destreza2_1_12 = Destreza.objects.get(codigo="M.2.1.12.")
    destreza2_1_13 = Destreza.objects.get(codigo="M.2.1.13.")
    destreza2_1_14 = Destreza.objects.get(codigo="M.2.1.14.")
    destreza2_1_15 = Destreza.objects.get(codigo="M.2.1.15.")
    destreza2_1_16 = Destreza.objects.get(codigo="M.2.1.16.")
    destreza2_1_17 = Destreza.objects.get(codigo="M.2.1.17.")
    destreza2_1_18 = Destreza.objects.get(codigo="M.2.1.18.")
    destreza2_1_19 = Destreza.objects.get(codigo="M.2.1.19.")
    destreza2_1_20 = Destreza.objects.get(codigo="M.2.1.20.")
    destreza2_1_21 = Destreza.objects.get(codigo="M.2.1.21.")
    destreza2_1_22 = Destreza.objects.get(codigo="M.2.1.22.")
    destreza2_1_23 = Destreza.objects.get(codigo="M.2.1.23.")
    destreza2_1_24 = Destreza.objects.get(codigo="M.2.1.24.")
    destreza2_1_25 = Destreza.objects.get(codigo="M.2.1.25.")
    destreza2_1_26 = Destreza.objects.get(codigo="M.2.1.26.")
    destreza2_1_27 = Destreza.objects.get(codigo="M.2.1.27.")
    destreza2_1_28 = Destreza.objects.get(codigo="M.2.1.28.")
    destreza2_1_29 = Destreza.objects.get(codigo="M.2.1.29.")
    destreza2_1_30 = Destreza.objects.get(codigo="M.2.1.30.")
    destreza2_1_31 = Destreza.objects.get(codigo="M.2.1.31.")
    destreza2_1_32 = Destreza.objects.get(codigo="M.2.1.32.")
    destreza2_1_33 = Destreza.objects.get(codigo="M.2.1.33.")
    destreza2_2_1 = Destreza.objects.get(codigo="M.2.2.1.")
    destreza2_2_2 = Destreza.objects.get(codigo="M.2.2.2.")
    destreza2_2_3 = Destreza.objects.get(codigo="M.2.2.3.")
    destreza2_2_4 = Destreza.objects.get(codigo="M.2.2.4.")
    destreza2_2_5 = Destreza.objects.get(codigo="M.2.2.5.")
    destreza2_2_6 = Destreza.objects.get(codigo="M.2.2.6.")
    destreza2_2_7 = Destreza.objects.get(codigo="M.2.2.7.")
    destreza2_2_8 = Destreza.objects.get(codigo="M.2.2.8.")
    destreza2_2_9 = Destreza.objects.get(codigo="M.2.2.9.")
    destreza2_2_10 = Destreza.objects.get(codigo="M.2.2.10.")
    destreza2_2_11 = Destreza.objects.get(codigo="M.2.2.11.")
    destreza2_2_12 = Destreza.objects.get(codigo="M.2.2.12.")
    destreza2_2_13 = Destreza.objects.get(codigo="M.2.2.13.")
    destreza2_2_14 = Destreza.objects.get(codigo="M.2.2.14.")
    destreza2_2_15 = Destreza.objects.get(codigo="M.2.2.15.")
    destreza2_2_16 = Destreza.objects.get(codigo="M.2.2.16.")
    destreza2_2_17 = Destreza.objects.get(codigo="M.2.2.17.")
    destreza2_2_18 = Destreza.objects.get(codigo="M.2.2.18.")
    destreza2_2_19 = Destreza.objects.get(codigo="M.2.2.19.")
    destreza2_2_20 = Destreza.objects.get(codigo="M.2.2.20.")
    destreza2_2_21 = Destreza.objects.get(codigo="M.2.2.21.")
    destreza2_2_22 = Destreza.objects.get(codigo="M.2.2.22.")
    destreza2_2_23 = Destreza.objects.get(codigo="M.2.2.23.")
    destreza2_2_24 = Destreza.objects.get(codigo="M.2.2.24.")
    destreza2_2_25 = Destreza.objects.get(codigo="M.2.2.25.")
    destreza2_3_1 = Destreza.objects.get(codigo="M.2.3.1.")
    destreza2_3_2 = Destreza.objects.get(codigo="M.2.3.2.")
    destreza2_3_3 = Destreza.objects.get(codigo="M.2.3.3.")
    destreza3_1_1 = Destreza.objects.get(codigo="M.3.1.1.")
    destreza3_1_2 = Destreza.objects.get(codigo="M.3.1.2.")
    destreza3_1_3 = Destreza.objects.get(codigo="M.3.1.3.")
    destreza3_1_4 = Destreza.objects.get(codigo="M.3.1.4.")
    destreza3_1_5 = Destreza.objects.get(codigo="M.3.1.5.")
    destreza3_1_6 = Destreza.objects.get(codigo="M.3.1.6.")
    destreza3_1_7 = Destreza.objects.get(codigo="M.3.1.7.")
    destreza3_1_8 = Destreza.objects.get(codigo="M.3.1.8.")
    destreza3_1_9 = Destreza.objects.get(codigo="M.3.1.9.")
    destreza3_1_10 = Destreza.objects.get(codigo="M.3.1.10.")
    destreza3_1_11 = Destreza.objects.get(codigo="M.3.1.11.")
    destreza3_1_12 = Destreza.objects.get(codigo="M.3.1.12.")
    destreza3_1_13 = Destreza.objects.get(codigo="M.3.1.13.")
    destreza3_1_14 = Destreza.objects.get(codigo="M.3.1.14.")
    destreza3_1_15 = Destreza.objects.get(codigo="M.3.1.15.")
    destreza3_1_16 = Destreza.objects.get(codigo="M.3.1.16.")
    destreza3_1_17 = Destreza.objects.get(codigo="M.3.1.17.")
    destreza3_1_18 = Destreza.objects.get(codigo="M.3.1.18.")
    destreza3_1_19 = Destreza.objects.get(codigo="M.3.1.19.")
    destreza3_1_20 = Destreza.objects.get(codigo="M.3.1.20.")
    destreza3_1_21 = Destreza.objects.get(codigo="M.3.1.21.")
    destreza3_1_22 = Destreza.objects.get(codigo="M.3.1.22.")
    destreza3_1_23 = Destreza.objects.get(codigo="M.3.1.23.")
    destreza3_1_24 = Destreza.objects.get(codigo="M.3.1.24.")
    destreza3_1_25 = Destreza.objects.get(codigo="M.3.1.25.")
    destreza3_1_26 = Destreza.objects.get(codigo="M.3.1.26.")
    destreza3_1_27 = Destreza.objects.get(codigo="M.3.1.27.")
    destreza3_1_28 = Destreza.objects.get(codigo="M.3.1.28.")
    destreza3_1_29 = Destreza.objects.get(codigo="M.3.1.29.")
    destreza3_1_30 = Destreza.objects.get(codigo="M.3.1.30.")
    destreza3_1_31 = Destreza.objects.get(codigo="M.3.1.31.")
    destreza3_1_32 = Destreza.objects.get(codigo="M.3.1.32.")
    destreza3_1_33 = Destreza.objects.get(codigo="M.3.1.33.")
    destreza3_1_34 = Destreza.objects.get(codigo="M.3.1.34.")
    destreza3_1_35 = Destreza.objects.get(codigo="M.3.1.35.")
    destreza3_1_36 = Destreza.objects.get(codigo="M.3.1.36.")
    destreza3_1_37 = Destreza.objects.get(codigo="M.3.1.37.")
    destreza3_1_38 = Destreza.objects.get(codigo="M.3.1.38.")
    destreza3_1_39 = Destreza.objects.get(codigo="M.3.1.39.")
    destreza3_1_40 = Destreza.objects.get(codigo="M.3.1.40.")
    destreza3_1_41 = Destreza.objects.get(codigo="M.3.1.41.")
    destreza3_1_42 = Destreza.objects.get(codigo="M.3.1.42.")
    destreza3_1_43 = Destreza.objects.get(codigo="M.3.1.43.")
    destreza3_1_44 = Destreza.objects.get(codigo="M.3.1.44.")
    destreza3_1_45 = Destreza.objects.get(codigo="M.3.1.45.")
    destreza3_1_46 = Destreza.objects.get(codigo="M.3.1.46.")
    destreza3_1_47 = Destreza.objects.get(codigo="M.3.1.47.")
    destreza3_1_48 = Destreza.objects.get(codigo="M.3.1.48.")
    destreza3_2_1 = Destreza.objects.get(codigo="M.3.2.1.")
    destreza3_2_2 = Destreza.objects.get(codigo="M.3.2.2.")
    destreza3_2_3 = Destreza.objects.get(codigo="M.3.2.3.")
    destreza3_2_4 = Destreza.objects.get(codigo="M.3.2.4.")
    destreza3_2_5 = Destreza.objects.get(codigo="M.3.2.5.")
    destreza3_2_6 = Destreza.objects.get(codigo="M.3.2.6.")
    destreza3_2_7 = Destreza.objects.get(codigo="M.3.2.7.")
    destreza3_2_8 = Destreza.objects.get(codigo="M.3.2.8.")
    destreza3_2_9 = Destreza.objects.get(codigo="M.3.2.9.")
    destreza3_2_10 = Destreza.objects.get(codigo="M.3.2.10.")
    destreza3_2_11 = Destreza.objects.get(codigo="M.3.2.11.")
    destreza3_2_12 = Destreza.objects.get(codigo="M.3.2.12.")
    destreza3_2_13 = Destreza.objects.get(codigo="M.3.2.13.")
    destreza3_2_14 = Destreza.objects.get(codigo="M.3.2.14.")
    destreza3_2_15 = Destreza.objects.get(codigo="M.3.2.15.")
    destreza3_2_16 = Destreza.objects.get(codigo="M.3.2.16.")
    destreza3_2_17 = Destreza.objects.get(codigo="M.3.2.17.")
    destreza3_2_18 = Destreza.objects.get(codigo="M.3.2.18.")
    destreza3_2_19 = Destreza.objects.get(codigo="M.3.2.19.")
    destreza3_2_20 = Destreza.objects.get(codigo="M.3.2.20.")
    destreza3_2_21 = Destreza.objects.get(codigo="M.3.2.21.")
    destreza3_2_22 = Destreza.objects.get(codigo="M.3.2.22.")
    destreza3_2_23 = Destreza.objects.get(codigo="M.3.2.23.")
    destreza3_3_1 = Destreza.objects.get(codigo="M.3.3.1.")
    destreza3_3_2 = Destreza.objects.get(codigo="M.3.3.2.")
    destreza3_3_3 = Destreza.objects.get(codigo="M.3.3.3.")
    destreza3_3_4 = Destreza.objects.get(codigo="M.3.3.4.")
    destreza3_3_5 = Destreza.objects.get(codigo="M.3.3.5.")
    destreza3_3_6 = Destreza.objects.get(codigo="M.3.3.6.")
    destreza4_1_1 = Destreza.objects.get(codigo="M.4.1.1.")
    destreza4_1_2 = Destreza.objects.get(codigo="M.4.1.2.")
    destreza4_1_3 = Destreza.objects.get(codigo="M.4.1.3.")
    destreza4_1_4 = Destreza.objects.get(codigo="M.4.1.4.")
    destreza4_1_5 = Destreza.objects.get(codigo="M.4.1.5.")
    destreza4_1_6 = Destreza.objects.get(codigo="M.4.1.6.")
    destreza4_1_7 = Destreza.objects.get(codigo="M.4.1.7.")
    destreza4_1_8 = Destreza.objects.get(codigo="M.4.1.8.")
    destreza4_1_9 = Destreza.objects.get(codigo="M.4.1.9.")
    destreza4_1_10 = Destreza.objects.get(codigo="M.4.1.10.")
    destreza4_1_11 = Destreza.objects.get(codigo="M.4.1.11.")
    destreza4_1_12 = Destreza.objects.get(codigo="M.4.1.12.")
    destreza4_1_13 = Destreza.objects.get(codigo="M.4.1.13.")
    destreza4_1_14 = Destreza.objects.get(codigo="M.4.1.14.")
    destreza4_1_15 = Destreza.objects.get(codigo="M.4.1.15.")
    destreza4_1_16 = Destreza.objects.get(codigo="M.4.1.16.")
    destreza4_1_17 = Destreza.objects.get(codigo="M.4.1.17.")
    destreza4_1_18 = Destreza.objects.get(codigo="M.4.1.18.")
    destreza4_1_19 = Destreza.objects.get(codigo="M.4.1.19.")
    destreza4_1_20 = Destreza.objects.get(codigo="M.4.1.20.")
    destreza4_1_21 = Destreza.objects.get(codigo="M.4.1.21.")
    destreza4_1_22 = Destreza.objects.get(codigo="M.4.1.22.")
    destreza4_1_23 = Destreza.objects.get(codigo="M.4.1.23.")
    destreza4_1_24 = Destreza.objects.get(codigo="M.4.1.24.")
    destreza4_1_25 = Destreza.objects.get(codigo="M.4.1.25.")
    destreza4_1_26 = Destreza.objects.get(codigo="M.4.1.26.")
    destreza4_1_27 = Destreza.objects.get(codigo="M.4.1.27.")
    destreza4_1_28 = Destreza.objects.get(codigo="M.4.1.28.")
    destreza4_1_29 = Destreza.objects.get(codigo="M.4.1.29.")
    destreza4_1_30 = Destreza.objects.get(codigo="M.4.1.30.")
    destreza4_1_31 = Destreza.objects.get(codigo="M.4.1.31.")
    destreza4_1_32 = Destreza.objects.get(codigo="M.4.1.32.")
    destreza4_1_33 = Destreza.objects.get(codigo="M.4.1.33.")
    destreza4_1_34 = Destreza.objects.get(codigo="M.4.1.34.")
    destreza4_1_35 = Destreza.objects.get(codigo="M.4.1.35.")
    destreza4_1_36 = Destreza.objects.get(codigo="M.4.1.36.")
    destreza4_1_37 = Destreza.objects.get(codigo="M.4.1.37.")
    destreza4_1_38 = Destreza.objects.get(codigo="M.4.1.38.")
    destreza4_1_39 = Destreza.objects.get(codigo="M.4.1.39.")
    destreza4_1_40 = Destreza.objects.get(codigo="M.4.1.40.")
    destreza4_1_41 = Destreza.objects.get(codigo="M.4.1.41.")
    destreza4_1_42 = Destreza.objects.get(codigo="M.4.1.42.")
    destreza4_1_43 = Destreza.objects.get(codigo="M.4.1.43.")
    destreza4_1_44 = Destreza.objects.get(codigo="M.4.1.44.")
    destreza4_1_45 = Destreza.objects.get(codigo="M.4.1.45.")
    destreza4_1_46 = Destreza.objects.get(codigo="M.4.1.46.")
    destreza4_1_47 = Destreza.objects.get(codigo="M.4.1.47.")
    destreza4_1_48 = Destreza.objects.get(codigo="M.4.1.48.")
    destreza4_1_49 = Destreza.objects.get(codigo="M.4.1.49.")
    destreza4_1_50 = Destreza.objects.get(codigo="M.4.1.50.")
    destreza4_1_51 = Destreza.objects.get(codigo="M.4.1.51.")
    destreza4_1_52 = Destreza.objects.get(codigo="M.4.1.52.")
    destreza4_1_53 = Destreza.objects.get(codigo="M.4.1.53.")
    destreza4_1_54 = Destreza.objects.get(codigo="M.4.1.54.")
    destreza4_1_55 = Destreza.objects.get(codigo="M.4.1.55.")
    destreza4_1_56 = Destreza.objects.get(codigo="M.4.1.56.")
    destreza4_1_57 = Destreza.objects.get(codigo="M.4.1.57.")
    destreza4_1_58 = Destreza.objects.get(codigo="M.4.1.58.")
    destreza4_1_59 = Destreza.objects.get(codigo="M.4.1.59.")
    destreza4_1_60 = Destreza.objects.get(codigo="M.4.1.60.")
    destreza4_1_61 = Destreza.objects.get(codigo="M.4.1.61.")
    destreza4_2_1 = Destreza.objects.get(codigo="M.4.2.1.")
    destreza4_2_2 = Destreza.objects.get(codigo="M.4.2.2.")
    destreza4_2_3 = Destreza.objects.get(codigo="M.4.2.3.")
    destreza4_2_4 = Destreza.objects.get(codigo="M.4.2.4.")
    destreza4_2_5 = Destreza.objects.get(codigo="M.4.2.5.")
    destreza4_2_6 = Destreza.objects.get(codigo="M.4.2.6.")
    destreza4_2_7 = Destreza.objects.get(codigo="M.4.2.7.")
    destreza4_2_8 = Destreza.objects.get(codigo="M.4.2.8.")
    destreza4_2_9 = Destreza.objects.get(codigo="M.4.2.9.")
    destreza4_2_10 = Destreza.objects.get(codigo="M.4.2.10.")
    destreza4_2_11 = Destreza.objects.get(codigo="M.4.2.11.")
    destreza4_2_12 = Destreza.objects.get(codigo="M.4.2.12.")
    destreza4_2_13 = Destreza.objects.get(codigo="M.4.2.13.")
    destreza4_2_14 = Destreza.objects.get(codigo="M.4.2.14.")
    destreza4_2_15 = Destreza.objects.get(codigo="M.4.2.15.")
    destreza4_2_16 = Destreza.objects.get(codigo="M.4.2.16.")
    destreza4_2_17 = Destreza.objects.get(codigo="M.4.2.17.")
    destreza4_2_18 = Destreza.objects.get(codigo="M.4.2.18.")
    destreza4_2_19 = Destreza.objects.get(codigo="M.4.2.19.")
    destreza4_2_20 = Destreza.objects.get(codigo="M.4.2.20.")
    destreza4_2_21 = Destreza.objects.get(codigo="M.4.2.21.")
    destreza4_2_22 = Destreza.objects.get(codigo="M.4.2.22.")
    destreza4_3_1 = Destreza.objects.get(codigo="M.4.3.1.")
    destreza4_3_2 = Destreza.objects.get(codigo="M.4.3.2.")
    destreza4_3_3 = Destreza.objects.get(codigo="M.4.3.3.")
    destreza4_3_4 = Destreza.objects.get(codigo="M.4.3.4.")
    destreza4_3_5 = Destreza.objects.get(codigo="M.4.3.5.")
    destreza4_3_6 = Destreza.objects.get(codigo="M.4.3.6.")
    destreza4_3_7 = Destreza.objects.get(codigo="M.4.3.7.")
    destreza4_3_8 = Destreza.objects.get(codigo="M.4.3.8.")
    destreza4_3_9 = Destreza.objects.get(codigo="M.4.3.9.")
    destreza4_3_10 = Destreza.objects.get(codigo="M.4.3.10.")
    destreza4_3_11 = Destreza.objects.get(codigo="M.4.3.11.")
    destreza4_3_12 = Destreza.objects.get(codigo="M.4.3.12.")
    destreza5_1_1 = Destreza.objects.get(codigo="M.5.1.1.")
    destreza5_1_2 = Destreza.objects.get(codigo="M.5.1.2.")
    destreza5_1_3 = Destreza.objects.get(codigo="M.5.1.3.")
    destreza5_1_4 = Destreza.objects.get(codigo="M.5.1.4.")
    destreza5_1_5 = Destreza.objects.get(codigo="M.5.1.5.")
    destreza5_1_6 = Destreza.objects.get(codigo="M.5.1.6.")
    destreza5_1_7 = Destreza.objects.get(codigo="M.5.1.7.")
    destreza5_1_8 = Destreza.objects.get(codigo="M.5.1.8.")
    destreza5_1_9 = Destreza.objects.get(codigo="M.5.1.9.")
    destreza5_1_10 = Destreza.objects.get(codigo="M.5.1.10.")
    destreza5_1_11 = Destreza.objects.get(codigo="M.5.1.11.")
    destreza5_1_12 = Destreza.objects.get(codigo="M.5.1.12.")
    destreza5_1_13 = Destreza.objects.get(codigo="M.5.1.13.")
    destreza5_1_14 = Destreza.objects.get(codigo="M.5.1.14.")
    destreza5_1_15 = Destreza.objects.get(codigo="M.5.1.15.")
    destreza5_1_16 = Destreza.objects.get(codigo="M.5.1.16.")
    destreza5_1_17 = Destreza.objects.get(codigo="M.5.1.17.")
    destreza5_1_18 = Destreza.objects.get(codigo="M.5.1.18.")
    destreza5_1_19 = Destreza.objects.get(codigo="M.5.1.19.")
    destreza5_1_20 = Destreza.objects.get(codigo="M.5.1.20.")
    destreza5_1_21 = Destreza.objects.get(codigo="M.5.1.21.")
    destreza5_1_22 = Destreza.objects.get(codigo="M.5.1.22.")
    destreza5_1_23 = Destreza.objects.get(codigo="M.5.1.23.")
    destreza5_1_24 = Destreza.objects.get(codigo="M.5.1.24.")
    destreza5_1_25 = Destreza.objects.get(codigo="M.5.1.25.")
    destreza5_1_26 = Destreza.objects.get(codigo="M.5.1.26.")
    destreza5_1_27 = Destreza.objects.get(codigo="M.5.1.27.")
    destreza5_1_28 = Destreza.objects.get(codigo="M.5.1.28.")
    destreza5_1_29 = Destreza.objects.get(codigo="M.5.1.29.")
    destreza5_1_30 = Destreza.objects.get(codigo="M.5.1.30.")
    destreza5_1_31 = Destreza.objects.get(codigo="M.5.1.31.")
    destreza5_1_32 = Destreza.objects.get(codigo="M.5.1.32.")
    destreza5_1_33 = Destreza.objects.get(codigo="M.5.1.33.")
    destreza5_1_34 = Destreza.objects.get(codigo="M.5.1.34.")
    destreza5_1_35 = Destreza.objects.get(codigo="M.5.1.35.")
    destreza5_1_36 = Destreza.objects.get(codigo="M.5.1.36.")
    destreza5_1_37 = Destreza.objects.get(codigo="M.5.1.37.")
    destreza5_1_38 = Destreza.objects.get(codigo="M.5.1.38.")
    destreza5_1_39 = Destreza.objects.get(codigo="M.5.1.39.")
    destreza5_1_40 = Destreza.objects.get(codigo="M.5.1.40.")
    destreza5_1_41 = Destreza.objects.get(codigo="M.5.1.41.")
    destreza5_1_42 = Destreza.objects.get(codigo="M.5.1.42.")
    destreza5_1_43 = Destreza.objects.get(codigo="M.5.1.43.")
    destreza5_1_44 = Destreza.objects.get(codigo="M.5.1.44.")
    destreza5_1_45 = Destreza.objects.get(codigo="M.5.1.45.")
    destreza5_1_46 = Destreza.objects.get(codigo="M.5.1.46.")
    destreza5_1_47 = Destreza.objects.get(codigo="M.5.1.47.")
    destreza5_1_48 = Destreza.objects.get(codigo="M.5.1.48.")
    destreza5_1_49 = Destreza.objects.get(codigo="M.5.1.49.")
    destreza5_1_50 = Destreza.objects.get(codigo="M.5.1.50.")
    destreza5_1_51 = Destreza.objects.get(codigo="M.5.1.51.")
    destreza5_1_52 = Destreza.objects.get(codigo="M.5.1.52.")
    destreza5_1_53 = Destreza.objects.get(codigo="M.5.1.53.")
    destreza5_1_54 = Destreza.objects.get(codigo="M.5.1.54.")
    destreza5_1_55 = Destreza.objects.get(codigo="M.5.1.55.")
    destreza5_1_56 = Destreza.objects.get(codigo="M.5.1.56.")
    destreza5_1_57 = Destreza.objects.get(codigo="M.5.1.57.")
    destreza5_1_58 = Destreza.objects.get(codigo="M.5.1.58.")
    destreza5_1_59 = Destreza.objects.get(codigo="M.5.1.59.")
    destreza5_1_60 = Destreza.objects.get(codigo="M.5.1.60.")
    destreza5_1_61 = Destreza.objects.get(codigo="M.5.1.61.")
    destreza5_1_62 = Destreza.objects.get(codigo="M.5.1.62.")
    destreza5_1_63 = Destreza.objects.get(codigo="M.5.1.63.")
    destreza5_1_64 = Destreza.objects.get(codigo="M.5.1.64.")
    destreza5_1_65 = Destreza.objects.get(codigo="M.5.1.65.")
    destreza5_1_66 = Destreza.objects.get(codigo="M.5.1.66.")
    destreza5_1_67 = Destreza.objects.get(codigo="M.5.1.67.")
    destreza5_1_68 = Destreza.objects.get(codigo="M.5.1.68.")
    destreza5_1_69 = Destreza.objects.get(codigo="M.5.1.69.")
    destreza5_1_70 = Destreza.objects.get(codigo="M.5.1.70.")
    destreza5_1_71 = Destreza.objects.get(codigo="M.5.1.71.")
    destreza5_1_72 = Destreza.objects.get(codigo="M.5.1.72.")
    destreza5_1_73 = Destreza.objects.get(codigo="M.5.1.73.")
    destreza5_1_74 = Destreza.objects.get(codigo="M.5.1.74.")
    destreza5_1_75 = Destreza.objects.get(codigo="M.5.1.75.")
    destreza5_1_76 = Destreza.objects.get(codigo="M.5.1.76.")
    destreza5_1_77 = Destreza.objects.get(codigo="M.5.1.77.")
    destreza5_1_78 = Destreza.objects.get(codigo="M.5.1.78.")
    destreza5_2_1 = Destreza.objects.get(codigo="M.5.2.1.")
    destreza5_2_2 = Destreza.objects.get(codigo="M.5.2.2.")
    destreza5_2_3 = Destreza.objects.get(codigo="M.5.2.3.")
    destreza5_2_4 = Destreza.objects.get(codigo="M.5.2.4.")
    destreza5_2_5 = Destreza.objects.get(codigo="M.5.2.5.")
    destreza5_2_6 = Destreza.objects.get(codigo="M.5.2.6.")
    destreza5_2_7 = Destreza.objects.get(codigo="M.5.2.7.")
    destreza5_2_8 = Destreza.objects.get(codigo="M.5.2.8.")
    destreza5_2_9 = Destreza.objects.get(codigo="M.5.2.9.")
    destreza5_2_10 = Destreza.objects.get(codigo="M.5.2.10.")
    destreza5_2_11 = Destreza.objects.get(codigo="M.5.2.11.")
    destreza5_2_12 = Destreza.objects.get(codigo="M.5.2.12.")
    destreza5_2_13 = Destreza.objects.get(codigo="M.5.2.13.")
    destreza5_2_14 = Destreza.objects.get(codigo="M.5.2.14.")
    destreza5_2_15 = Destreza.objects.get(codigo="M.5.2.15.")
    destreza5_2_16 = Destreza.objects.get(codigo="M.5.2.16.")
    destreza5_2_17 = Destreza.objects.get(codigo="M.5.2.17.")
    destreza5_2_18 = Destreza.objects.get(codigo="M.5.2.18.")
    destreza5_2_19 = Destreza.objects.get(codigo="M.5.2.19.")
    destreza5_2_20 = Destreza.objects.get(codigo="M.5.2.20.")
    destreza5_2_21 = Destreza.objects.get(codigo="M.5.2.21.")
    destreza5_2_22 = Destreza.objects.get(codigo="M.5.2.22.")
    destreza5_2_23 = Destreza.objects.get(codigo="M.5.2.23.")
    destreza5_2_24 = Destreza.objects.get(codigo="M.5.2.24.")
    destreza5_2_25 = Destreza.objects.get(codigo="M.5.2.25.")
    destreza5_2_26 = Destreza.objects.get(codigo="M.5.2.26.")
    destreza5_2_27 = Destreza.objects.get(codigo="M.5.2.27.")
    destreza5_3_1 = Destreza.objects.get(codigo="M.5.3.1.")
    destreza5_3_2 = Destreza.objects.get(codigo="M.5.3.2.")
    destreza5_3_3 = Destreza.objects.get(codigo="M.5.3.3.")
    destreza5_3_4 = Destreza.objects.get(codigo="M.5.3.4.")
    destreza5_3_5 = Destreza.objects.get(codigo="M.5.3.5.")
    destreza5_3_6 = Destreza.objects.get(codigo="M.5.3.6.")
    destreza5_3_7 = Destreza.objects.get(codigo="M.5.3.7.")
    destreza5_3_8 = Destreza.objects.get(codigo="M.5.3.8.")
    destreza5_3_9 = Destreza.objects.get(codigo="M.5.3.9.")
    destreza5_3_10 = Destreza.objects.get(codigo="M.5.3.10.")
    destreza5_3_11 = Destreza.objects.get(codigo="M.5.3.11.")
    destreza5_3_12 = Destreza.objects.get(codigo="M.5.3.12.")
    destreza5_3_13 = Destreza.objects.get(codigo="M.5.3.13.")
    destreza5_3_14 = Destreza.objects.get(codigo="M.5.3.14.")
    destreza5_3_15 = Destreza.objects.get(codigo="M.5.3.15.")
    destreza5_3_16 = Destreza.objects.get(codigo="M.5.3.16.")
    destreza5_3_17 = Destreza.objects.get(codigo="M.5.3.17.")
    destreza5_3_18 = Destreza.objects.get(codigo="M.5.3.18.")
    destreza5_3_19 = Destreza.objects.get(codigo="M.5.3.19.")
    destreza5_3_20 = Destreza.objects.get(codigo="M.5.3.20.")
    destreza5_3_21 = Destreza.objects.get(codigo="M.5.3.21.")
    destreza5_3_22 = Destreza.objects.get(codigo="M.5.3.22.")
    destreza5_3_23 = Destreza.objects.get(codigo="M.5.3.23.")
    destreza5_3_24 = Destreza.objects.get(codigo="M.5.3.24.")
    destreza5_3_25 = Destreza.objects.get(codigo="M.5.3.25.")

    # Asignación

    # Preparatoria
    criterio1_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
    )
    criterio1_1.destrezas.add(
        destreza1_4_1,
        destreza1_4_2,
        destreza1_4_3,
        destreza1_4_4,
        destreza1_4_5,
        destreza1_4_6,
        destreza1_4_7,
        destreza1_4_8,
        destreza1_4_9,
        destreza1_4_10,
    )

    criterio1_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
    )
    criterio1_2.destrezas.add(
        destreza1_4_11,
        destreza1_4_12,
        destreza1_4_13,
        destreza1_4_14,
        destreza1_4_15,
        destreza1_4_16,
        destreza1_4_17,
        destreza1_4_18,
    )

    criterio1_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio1_3.destrezas.add(
        destreza1_4_19,
        destreza1_4_20,
        destreza1_4_21,
        destreza1_4_22,
        destreza1_4_24,
        destreza1_4_25,
        destreza1_4_26,
        destreza1_4_32,
    )

    criterio1_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio1_4.destrezas.add(
        destreza1_4_23,
        destreza1_4_27,
        destreza1_4_28,
        destreza1_4_29,
        destreza1_4_30,
        destreza1_4_31,
    )

    criterio1_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo6,
    )
    criterio1_5.destrezas.add(
        destreza1_4_33,
        destreza1_4_34,
    )

    # Elemental
    criterio2_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio2_1.destrezas.add(
        destreza2_1_1,
        destreza2_1_2,
        destreza2_1_3,
        destreza2_1_4,
        destreza2_1_5,
        destreza2_1_6,
        destreza2_1_7,
        destreza2_1_8,
        destreza2_1_9,
        destreza2_1_10,
        destreza2_1_11,
    )

    criterio2_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio2_2.destrezas.add(
        destreza2_1_12,
        destreza2_1_13,
        destreza2_1_14,
        destreza2_1_15,
        destreza2_1_16,
        destreza2_1_17,
        destreza2_1_18,
        destreza2_1_19,
        destreza2_1_20,
        destreza2_1_21,
        destreza2_1_22,
        destreza2_1_23,
        destreza2_1_24,
        destreza2_1_25,
        destreza2_1_26,
        destreza2_1_27,
        destreza2_1_28,
        destreza2_1_29,
        destreza2_1_30,
        destreza2_1_31,
        destreza2_1_32,
        destreza2_1_33,
    )

    criterio2_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio2_3.destrezas.add(
        destreza2_2_1,
        destreza2_2_2,
        destreza2_2_3,
        destreza2_2_4,
        destreza2_2_5,
        destreza2_2_6,
        destreza2_2_7,
        destreza2_2_8,
        destreza2_2_9,
    )

    criterio2_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio2_4.destrezas.add(
        destreza2_2_10,
        destreza2_2_11,
        destreza2_2_12,
        destreza2_2_13,
        destreza2_2_14,
        destreza2_2_15,
        destreza2_2_16,
        destreza2_2_17,
        destreza2_2_18,
        destreza2_2_19,
        destreza2_2_20,
        destreza2_2_21,
        destreza2_2_22,
        destreza2_2_23,
        destreza2_2_24,
        destreza2_2_25,
    )

    criterio2_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio2_5.destrezas.add(
        destreza2_3_1,
        destreza2_3_2,
        destreza2_3_3,
    )

    # Media
    criterio3_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio3_1.destrezas.add(
        destreza3_1_1,
        destreza3_1_4,
        destreza3_1_7,
        destreza3_1_9,
        destreza3_1_11,
        destreza3_1_12,
        destreza3_1_13,
    )

    criterio3_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio3_2.destrezas.add(
        destreza3_1_5,
        destreza3_1_6,
        destreza3_1_27,
        destreza3_1_37,
        destreza3_1_38,
    )

    criterio3_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio3_3.destrezas.add(
        destreza3_1_14,
        destreza3_1_15,
        destreza3_1_16,
        destreza3_1_17,
        destreza3_1_18,
        destreza3_1_19,
        destreza3_1_20,
        destreza3_1_21,
        destreza3_1_22,
        destreza3_1_23,
        destreza3_1_24,
    )

    criterio3_4.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_4.destrezas.add(
        destreza3_1_25,
        destreza3_1_26,
        destreza3_1_33,
        destreza3_1_34,
        destreza3_1_35,
        destreza3_1_36,
    )

    criterio3_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_5.destrezas.add(
        destreza3_1_8,
        destreza3_1_10,
        destreza3_1_28,
        destreza3_1_29,
        destreza3_1_30,
        destreza3_1_31,
        destreza3_1_32,
        destreza3_1_39,
        destreza3_1_40,
        destreza3_1_41,
        destreza3_1_42,
        destreza3_1_43,
    )

    criterio3_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_6.destrezas.add(
        destreza3_1_2,
        destreza3_1_3,
        destreza3_1_44,
        destreza3_1_45,
        destreza3_1_46,
        destreza3_1_47,
        destreza3_1_48,
    )

    criterio3_7.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_7.destrezas.add(
        destreza3_2_1,
        destreza3_2_2,
        destreza3_2_3,
        destreza3_2_5,
        destreza3_2_7,
        destreza3_2_8,
        destreza3_2_12,
        destreza3_2_13,
        destreza3_2_20,
    )

    criterio3_8.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_8.destrezas.add(
        destreza3_2_4,
        destreza3_2_6,
        destreza3_2_9,
        destreza3_2_10,
        destreza3_2_11,
    )

    criterio3_9.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo6,
    )
    criterio3_9.destrezas.add(
        destreza3_2_14,
        destreza3_2_15,
        destreza3_2_16,
        destreza3_2_17,
        destreza3_2_18,
        destreza3_2_19,
        destreza3_2_21,
        destreza3_2_22,
        destreza3_2_23,
    )

    criterio3_10.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_10.destrezas.add(
        destreza3_3_1,
        destreza3_3_2,
        destreza3_3_3,
    )

    criterio3_11.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio3_11.destrezas.add(
        destreza3_3_4,
        destreza3_3_5,
        destreza3_3_6,
    )

    # Superior
    criterio4_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio4_1.destrezas.add(
        destreza4_1_1,
        destreza4_1_2,
        destreza4_1_3,
        destreza4_1_4,
        destreza4_1_5,
        destreza4_1_6,
        destreza4_1_7,
        destreza4_1_8,
        destreza4_1_9,
        destreza4_1_10,
        destreza4_1_11,
        destreza4_1_12,
        destreza4_1_13,
        destreza4_1_14,
        destreza4_1_15,
        destreza4_1_16,
        destreza4_1_17,
        destreza4_1_18,
        destreza4_1_19,
        destreza4_1_20,
        destreza4_1_21,
        destreza4_1_22,
        destreza4_1_26,
        destreza4_1_27,
    )

    criterio4_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio4_2.destrezas.add(
        destreza4_1_23,
        destreza4_1_24,
        destreza4_1_25,
        destreza4_1_26,
        destreza4_1_27,
        destreza4_1_28,
        destreza4_1_29,
        destreza4_1_30,
        destreza4_1_31,
        destreza4_1_32,
        destreza4_1_33,
        destreza4_1_34,
        destreza4_1_35,
        destreza4_1_36,
        destreza4_1_37,
        destreza4_1_38,
        destreza4_1_39,
        destreza4_1_40,
        destreza4_1_41,
    )

    criterio4_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio4_3.destrezas.add(
        destreza4_1_42,
        destreza4_1_43,
        destreza4_1_44,
        destreza4_1_45,
        destreza4_1_46,
        destreza4_1_47,
        destreza4_1_48,
        destreza4_1_49,
        destreza4_1_50,
        destreza4_1_51,
        destreza4_1_52,
        destreza4_1_53,
        destreza4_1_54,
        destreza4_1_55,
        destreza4_1_56,
        destreza4_1_57,
        destreza4_1_58,
        destreza4_1_59,
        destreza4_1_60,
        destreza4_1_61,
    )

    criterio4_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
    )
    criterio4_4.destrezas.add(
        destreza4_2_1,
        destreza4_2_2,
        destreza4_2_3,
        destreza4_2_4,
    )

    criterio4_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio4_5.destrezas.add(
        destreza4_2_5,
        destreza4_2_6,
        destreza4_2_7,
        destreza4_2_8,
        destreza4_2_9,
        destreza4_2_10,
        destreza4_2_11,
        destreza4_2_12,
        destreza4_2_13,
    )

    criterio4_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
    )
    criterio4_6.destrezas.add(
        destreza4_2_14,
        destreza4_2_15,
        destreza4_2_16,
        destreza4_2_17,
        destreza4_2_18,
        destreza4_2_19,
        destreza4_2_20,
        destreza4_2_21,
        destreza4_2_22,
    )

    criterio4_7.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio4_7.destrezas.add(
        destreza4_3_1,
        destreza4_3_2,
        destreza4_3_3,
    )

    criterio4_8.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio4_8.destrezas.add(
        destreza4_3_4,
        destreza4_3_5,
        destreza4_3_6,
        destreza4_3_7,
        destreza4_3_8,
        destreza4_3_9,
        destreza4_3_10,
        destreza4_3_11,
        destreza4_3_12,
    )

    # Bachillerato
    criterio5_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio5_1.destrezas.add(
        destreza5_1_1,
        destreza5_1_2,
        destreza5_1_3,
        destreza5_1_4,
        destreza5_1_5,
        destreza5_1_6,
        destreza5_1_7,
        destreza5_1_8,
    )

    criterio5_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio5_2.destrezas.add(
        destreza5_1_9,
        destreza5_1_10,
        destreza5_1_11,
        destreza5_1_12,
        destreza5_1_13,
        destreza5_1_14,
        destreza5_1_15,
        destreza5_1_16,
        destreza5_1_17,
        destreza5_1_18,
        destreza5_1_19,
    )

    criterio5_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
    )
    criterio5_3.destrezas.add(
        destreza5_1_20,
        destreza5_1_21,
        destreza5_1_22,
        destreza5_1_23,
        destreza5_1_24,
        destreza5_1_25,
        destreza5_1_26,
        destreza5_1_27,
        destreza5_1_28,
        destreza5_1_29,
        destreza5_1_30,
        destreza5_1_31,
        destreza5_1_32,
        destreza5_1_33,
        destreza5_1_34,
        destreza5_1_35,
        destreza5_1_36,
        destreza5_1_37,
        destreza5_1_38,
        destreza5_1_39,
        destreza5_1_40,
        destreza5_1_41,
        destreza5_1_42,
        destreza5_1_43,
        destreza5_1_44,
        destreza5_1_45,
        destreza5_1_46,
        destreza5_1_70,
        destreza5_1_71,
        destreza5_1_72,
        destreza5_1_73,
        destreza5_1_74,
        destreza5_1_75,
        destreza5_1_76,
        destreza5_1_77,
        destreza5_1_78,
    )

    criterio5_4.objetivos_generales.add(
        objetivo2,
        objetivo6,
    )
    criterio5_4.destrezas.add(
        destreza5_1_53,
        destreza5_1_54,
        destreza5_1_55,
        destreza5_1_56,
        destreza5_1_57,
        destreza5_1_58,
        destreza5_1_59,
        destreza5_1_60,
        destreza5_1_61,
    )

    criterio5_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo6,
    )
    criterio5_5.destrezas.add(
        destreza5_1_47,
        destreza5_1_48,
        destreza5_1_49,
        destreza5_1_50,
        destreza5_1_51,
        destreza5_1_52,
        destreza5_1_62,
        destreza5_1_63,
        destreza5_1_64,
        destreza5_1_65,
        destreza5_1_66,
        destreza5_1_67,
        destreza5_1_68,
        destreza5_1_69,
    )

    criterio5_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio5_6.destrezas.add(
        destreza5_2_1,
        destreza5_2_2,
        destreza5_2_3,
        destreza5_2_4,
        destreza5_2_5,
        destreza5_2_6,
        destreza5_2_7,
        destreza5_2_8,
        destreza5_2_9,
        destreza5_2_10,
        destreza5_2_11,
        destreza5_2_12,
        destreza5_2_13,
        destreza5_2_14,
        destreza5_2_15,
        destreza5_2_16,
        destreza5_2_17,
    )

    criterio5_7.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo6,
    )
    criterio5_7.destrezas.add(
        destreza5_2_18,
        destreza5_2_19,
        destreza5_2_20,
        destreza5_2_21,
        destreza5_2_22,
        destreza5_2_23,
    )

    criterio5_8.objetivos_generales.add(
        objetivo2,
        objetivo6,
    )
    criterio5_8.destrezas.add(
        destreza5_2_24,
        destreza5_2_25,
        destreza5_2_26,
        destreza5_2_27,
    )

    criterio5_9.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio5_9.destrezas.add(
        destreza5_3_1,
        destreza5_3_2,
        destreza5_3_3,
        destreza5_3_4,
        destreza5_3_5,
        destreza5_3_6,
    )

    criterio5_10.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
    )
    criterio5_10.destrezas.add(
        destreza5_3_7,
        destreza5_3_8,
        destreza5_3_9,
        destreza5_3_10,
        destreza5_3_11,
        destreza5_3_12,
        destreza5_3_13,
        destreza5_3_14,
        destreza5_3_15,
        destreza5_3_16,
        destreza5_3_17,
        destreza5_3_18,
        destreza5_3_19,
        destreza5_3_20,
        destreza5_3_21,
    )

    criterio5_11.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo6,
    )
    criterio5_11.destrezas.add(
        destreza5_3_22,
        destreza5_3_23,
        destreza5_3_24,
        destreza5_3_25,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0060_auto_20180908_2001'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
