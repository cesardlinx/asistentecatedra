from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Objetivos Generales
    objetivo1 = ObjetivoGeneral.objects.get(codigo="OG.CS.1.")
    objetivo2 = ObjetivoGeneral.objects.get(codigo="OG.CS.2.")
    objetivo3 = ObjetivoGeneral.objects.get(codigo="OG.CS.3.")
    objetivo4 = ObjetivoGeneral.objects.get(codigo="OG.CS.4.")
    objetivo5 = ObjetivoGeneral.objects.get(codigo="OG.CS.5.")
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.CS.6.")
    objetivo7 = ObjetivoGeneral.objects.get(codigo="OG.CS.7.")
    objetivo8 = ObjetivoGeneral.objects.get(codigo="OG.CS.8.")
    objetivo9 = ObjetivoGeneral.objects.get(codigo="OG.CS.9.")
    objetivo10 = ObjetivoGeneral.objects.get(codigo="OG.CS.10.")

    # Criterios de evaluación
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.6.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.8.")
    criterio3_9 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.9.")
    criterio3_10 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.10.")
    criterio3_11 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.11.")
    criterio3_12 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.12.")
    criterio3_13 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.13.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.8.")
    criterio4_9 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.9.")
    criterio4_10 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.10.")
    criterio4_11 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.11.")

    # Destrezas
    destreza2_1_1 = Destreza.objects.get(codigo="CS.2.1.1.")
    destreza2_1_2 = Destreza.objects.get(codigo="CS.2.1.2.")
    destreza2_1_3 = Destreza.objects.get(codigo="CS.2.1.3.")
    destreza2_1_4 = Destreza.objects.get(codigo="CS.2.1.4.")
    destreza2_1_5 = Destreza.objects.get(codigo="CS.2.1.5.")
    destreza2_1_6 = Destreza.objects.get(codigo="CS.2.1.6.")
    destreza2_1_7 = Destreza.objects.get(codigo="CS.2.1.7.")
    destreza2_1_8 = Destreza.objects.get(codigo="CS.2.1.8.")
    destreza2_1_9 = Destreza.objects.get(codigo="CS.2.1.9.")
    destreza2_1_10 = Destreza.objects.get(codigo="CS.2.1.10.")
    destreza2_1_11 = Destreza.objects.get(codigo="CS.2.1.11.")
    destreza2_1_12 = Destreza.objects.get(codigo="CS.2.1.12.")
    destreza2_2_1 = Destreza.objects.get(codigo="CS.2.2.1.")
    destreza2_2_2 = Destreza.objects.get(codigo="CS.2.2.2.")
    destreza2_2_3 = Destreza.objects.get(codigo="CS.2.2.3.")
    destreza2_2_4 = Destreza.objects.get(codigo="CS.2.2.4.")
    destreza2_2_5 = Destreza.objects.get(codigo="CS.2.2.5.")
    destreza2_2_6 = Destreza.objects.get(codigo="CS.2.2.6.")
    destreza2_2_7 = Destreza.objects.get(codigo="CS.2.2.7.")
    destreza2_2_8 = Destreza.objects.get(codigo="CS.2.2.8.")
    destreza2_2_9 = Destreza.objects.get(codigo="CS.2.2.9.")
    destreza2_2_10 = Destreza.objects.get(codigo="CS.2.2.10.")
    destreza2_2_11 = Destreza.objects.get(codigo="CS.2.2.11.")
    destreza2_2_12 = Destreza.objects.get(codigo="CS.2.2.12.")
    destreza2_2_13 = Destreza.objects.get(codigo="CS.2.2.13.")
    destreza2_2_14 = Destreza.objects.get(codigo="CS.2.2.14.")
    destreza2_2_15 = Destreza.objects.get(codigo="CS.2.2.15.")
    destreza2_2_16 = Destreza.objects.get(codigo="CS.2.2.16.")
    destreza2_2_17 = Destreza.objects.get(codigo="CS.2.2.17.")
    destreza2_2_18 = Destreza.objects.get(codigo="CS.2.2.18.")
    destreza2_2_19 = Destreza.objects.get(codigo="CS.2.2.19.")
    destreza2_3_1 = Destreza.objects.get(codigo="CS.2.3.1.")
    destreza2_3_2 = Destreza.objects.get(codigo="CS.2.3.2.")
    destreza2_3_3 = Destreza.objects.get(codigo="CS.2.3.3.")
    destreza2_3_4 = Destreza.objects.get(codigo="CS.2.3.4.")
    destreza2_3_5 = Destreza.objects.get(codigo="CS.2.3.5.")
    destreza2_3_6 = Destreza.objects.get(codigo="CS.2.3.6.")
    destreza2_3_7 = Destreza.objects.get(codigo="CS.2.3.7.")
    destreza2_3_8 = Destreza.objects.get(codigo="CS.2.3.8.")
    destreza2_3_9 = Destreza.objects.get(codigo="CS.2.3.9.")
    destreza2_3_10 = Destreza.objects.get(codigo="CS.2.3.10.")
    destreza2_3_11 = Destreza.objects.get(codigo="CS.2.3.11.")
    destreza2_3_12 = Destreza.objects.get(codigo="CS.2.3.12.")
    destreza2_3_13 = Destreza.objects.get(codigo="CS.2.3.13.")
    destreza3_1_1 = Destreza.objects.get(codigo="CS.3.1.1.")
    destreza3_1_2 = Destreza.objects.get(codigo="CS.3.1.2.")
    destreza3_1_3 = Destreza.objects.get(codigo="CS.3.1.3.")
    destreza3_1_4 = Destreza.objects.get(codigo="CS.3.1.4.")
    destreza3_1_5 = Destreza.objects.get(codigo="CS.3.1.5.")
    destreza3_1_6 = Destreza.objects.get(codigo="CS.3.1.6.")
    destreza3_1_7 = Destreza.objects.get(codigo="CS.3.1.7.")
    destreza3_1_8 = Destreza.objects.get(codigo="CS.3.1.8.")
    destreza3_1_9 = Destreza.objects.get(codigo="CS.3.1.9.")
    destreza3_1_10 = Destreza.objects.get(codigo="CS.3.1.10.")
    destreza3_1_11 = Destreza.objects.get(codigo="CS.3.1.11.")
    destreza3_1_12 = Destreza.objects.get(codigo="CS.3.1.12.")
    destreza3_1_13 = Destreza.objects.get(codigo="CS.3.1.13.")
    destreza3_1_14 = Destreza.objects.get(codigo="CS.3.1.14.")
    destreza3_1_15 = Destreza.objects.get(codigo="CS.3.1.15.")
    destreza3_1_16 = Destreza.objects.get(codigo="CS.3.1.16.")
    destreza3_1_17 = Destreza.objects.get(codigo="CS.3.1.17.")
    destreza3_1_18 = Destreza.objects.get(codigo="CS.3.1.18.")
    destreza3_1_19 = Destreza.objects.get(codigo="CS.3.1.19.")
    destreza3_1_20 = Destreza.objects.get(codigo="CS.3.1.20.")
    destreza3_1_21 = Destreza.objects.get(codigo="CS.3.1.21.")
    destreza3_1_22 = Destreza.objects.get(codigo="CS.3.1.22.")
    destreza3_1_23 = Destreza.objects.get(codigo="CS.3.1.23.")
    destreza3_1_24 = Destreza.objects.get(codigo="CS.3.1.24.")
    destreza3_1_25 = Destreza.objects.get(codigo="CS.3.1.25.")
    destreza3_1_26 = Destreza.objects.get(codigo="CS.3.1.26.")
    destreza3_1_27 = Destreza.objects.get(codigo="CS.3.1.27.")
    destreza3_1_28 = Destreza.objects.get(codigo="CS.3.1.28.")
    destreza3_1_29 = Destreza.objects.get(codigo="CS.3.1.29.")
    destreza3_1_30 = Destreza.objects.get(codigo="CS.3.1.30.")
    destreza3_1_31 = Destreza.objects.get(codigo="CS.3.1.31.")
    destreza3_1_32 = Destreza.objects.get(codigo="CS.3.1.32.")
    destreza3_1_33 = Destreza.objects.get(codigo="CS.3.1.33.")
    destreza3_1_34 = Destreza.objects.get(codigo="CS.3.1.34.")
    destreza3_1_35 = Destreza.objects.get(codigo="CS.3.1.35.")
    destreza3_1_36 = Destreza.objects.get(codigo="CS.3.1.36.")
    destreza3_1_37 = Destreza.objects.get(codigo="CS.3.1.37.")
    destreza3_1_38 = Destreza.objects.get(codigo="CS.3.1.38.")
    destreza3_1_39 = Destreza.objects.get(codigo="CS.3.1.39.")
    destreza3_1_40 = Destreza.objects.get(codigo="CS.3.1.40.")
    destreza3_1_41 = Destreza.objects.get(codigo="CS.3.1.41.")
    destreza3_1_42 = Destreza.objects.get(codigo="CS.3.1.42.")
    destreza3_1_43 = Destreza.objects.get(codigo="CS.3.1.43.")
    destreza3_1_44 = Destreza.objects.get(codigo="CS.3.1.44.")
    destreza3_1_45 = Destreza.objects.get(codigo="CS.3.1.45.")
    destreza3_1_46 = Destreza.objects.get(codigo="CS.3.1.46.")
    destreza3_1_47 = Destreza.objects.get(codigo="CS.3.1.47.")
    destreza3_1_48 = Destreza.objects.get(codigo="CS.3.1.48.")
    destreza3_1_49 = Destreza.objects.get(codigo="CS.3.1.49.")
    destreza3_1_50 = Destreza.objects.get(codigo="CS.3.1.50.")
    destreza3_1_51 = Destreza.objects.get(codigo="CS.3.1.51.")
    destreza3_1_52 = Destreza.objects.get(codigo="CS.3.1.52.")
    destreza3_1_53 = Destreza.objects.get(codigo="CS.3.1.53.")
    destreza3_1_54 = Destreza.objects.get(codigo="CS.3.1.54.")
    destreza3_1_55 = Destreza.objects.get(codigo="CS.3.1.55.")
    destreza3_1_56 = Destreza.objects.get(codigo="CS.3.1.56.")
    destreza3_1_57 = Destreza.objects.get(codigo="CS.3.1.57.")
    destreza3_1_58 = Destreza.objects.get(codigo="CS.3.1.58.")
    destreza3_1_59 = Destreza.objects.get(codigo="CS.3.1.59.")
    destreza3_1_60 = Destreza.objects.get(codigo="CS.3.1.60.")
    destreza3_1_61 = Destreza.objects.get(codigo="CS.3.1.61.")
    destreza3_1_62 = Destreza.objects.get(codigo="CS.3.1.62.")
    destreza3_1_63 = Destreza.objects.get(codigo="CS.3.1.63.")
    destreza3_1_64 = Destreza.objects.get(codigo="CS.3.1.64.")
    destreza3_1_65 = Destreza.objects.get(codigo="CS.3.1.65.")
    destreza3_1_66 = Destreza.objects.get(codigo="CS.3.1.66.")
    destreza3_2_1 = Destreza.objects.get(codigo="CS.3.2.1.")
    destreza3_2_2 = Destreza.objects.get(codigo="CS.3.2.2.")
    destreza3_2_3 = Destreza.objects.get(codigo="CS.3.2.3.")
    destreza3_2_4 = Destreza.objects.get(codigo="CS.3.2.4.")
    destreza3_2_5 = Destreza.objects.get(codigo="CS.3.2.5.")
    destreza3_2_6 = Destreza.objects.get(codigo="CS.3.2.6.")
    destreza3_2_7 = Destreza.objects.get(codigo="CS.3.2.7.")
    destreza3_2_8 = Destreza.objects.get(codigo="CS.3.2.8.")
    destreza3_2_9 = Destreza.objects.get(codigo="CS.3.2.9.")
    destreza3_2_10 = Destreza.objects.get(codigo="CS.3.2.10.")
    destreza3_2_11 = Destreza.objects.get(codigo="CS.3.2.11.")
    destreza3_2_12 = Destreza.objects.get(codigo="CS.3.2.12.")
    destreza3_2_13 = Destreza.objects.get(codigo="CS.3.2.13.")
    destreza3_2_14 = Destreza.objects.get(codigo="CS.3.2.14.")
    destreza3_2_15 = Destreza.objects.get(codigo="CS.3.2.15.")
    destreza3_2_16 = Destreza.objects.get(codigo="CS.3.2.16.")
    destreza3_2_17 = Destreza.objects.get(codigo="CS.3.2.17.")
    destreza3_2_18 = Destreza.objects.get(codigo="CS.3.2.18.")
    destreza3_2_19 = Destreza.objects.get(codigo="CS.3.2.19.")
    destreza3_2_20 = Destreza.objects.get(codigo="CS.3.2.20.")
    destreza3_2_21 = Destreza.objects.get(codigo="CS.3.2.21.")
    destreza3_2_22 = Destreza.objects.get(codigo="CS.3.2.22.")
    destreza3_2_23 = Destreza.objects.get(codigo="CS.3.2.23.")
    destreza3_2_24 = Destreza.objects.get(codigo="CS.3.2.24.")
    destreza3_2_25 = Destreza.objects.get(codigo="CS.3.2.25.")
    destreza3_2_26 = Destreza.objects.get(codigo="CS.3.2.26.")
    destreza3_3_1 = Destreza.objects.get(codigo="CS.3.3.1.")
    destreza3_3_2 = Destreza.objects.get(codigo="CS.3.3.2.")
    destreza3_3_3 = Destreza.objects.get(codigo="CS.3.3.3.")
    destreza3_3_4 = Destreza.objects.get(codigo="CS.3.3.4.")
    destreza3_3_5 = Destreza.objects.get(codigo="CS.3.3.5.")
    destreza3_3_6 = Destreza.objects.get(codigo="CS.3.3.6.")
    destreza3_3_7 = Destreza.objects.get(codigo="CS.3.3.7.")
    destreza3_3_8 = Destreza.objects.get(codigo="CS.3.3.8.")
    destreza3_3_9 = Destreza.objects.get(codigo="CS.3.3.9.")
    destreza3_3_10 = Destreza.objects.get(codigo="CS.3.3.10.")
    destreza3_3_11 = Destreza.objects.get(codigo="CS.3.3.11.")
    destreza3_3_12 = Destreza.objects.get(codigo="CS.3.3.12.")
    destreza3_3_13 = Destreza.objects.get(codigo="CS.3.3.13.")
    destreza3_3_14 = Destreza.objects.get(codigo="CS.3.3.14.")
    destreza3_3_15 = Destreza.objects.get(codigo="CS.3.3.15.")
    destreza3_3_16 = Destreza.objects.get(codigo="CS.3.3.16.")
    destreza4_1_1 = Destreza.objects.get(codigo="CS.4.1.1.")
    destreza4_1_2 = Destreza.objects.get(codigo="CS.4.1.2.")
    destreza4_1_3 = Destreza.objects.get(codigo="CS.4.1.3.")
    destreza4_1_4 = Destreza.objects.get(codigo="CS.4.1.4.")
    destreza4_1_5 = Destreza.objects.get(codigo="CS.4.1.5.")
    destreza4_1_6 = Destreza.objects.get(codigo="CS.4.1.6.")
    destreza4_1_7 = Destreza.objects.get(codigo="CS.4.1.7.")
    destreza4_1_8 = Destreza.objects.get(codigo="CS.4.1.8.")
    destreza4_1_9 = Destreza.objects.get(codigo="CS.4.1.9.")
    destreza4_1_10 = Destreza.objects.get(codigo="CS.4.1.10.")
    destreza4_1_11 = Destreza.objects.get(codigo="CS.4.1.11.")
    destreza4_1_12 = Destreza.objects.get(codigo="CS.4.1.12.")
    destreza4_1_13 = Destreza.objects.get(codigo="CS.4.1.13.")
    destreza4_1_14 = Destreza.objects.get(codigo="CS.4.1.14.")
    destreza4_1_15 = Destreza.objects.get(codigo="CS.4.1.15.")
    destreza4_1_16 = Destreza.objects.get(codigo="CS.4.1.16.")
    destreza4_1_17 = Destreza.objects.get(codigo="CS.4.1.17.")
    destreza4_1_18 = Destreza.objects.get(codigo="CS.4.1.18.")
    destreza4_1_19 = Destreza.objects.get(codigo="CS.4.1.19.")
    destreza4_1_20 = Destreza.objects.get(codigo="CS.4.1.20.")
    destreza4_1_21 = Destreza.objects.get(codigo="CS.4.1.21.")
    destreza4_1_22 = Destreza.objects.get(codigo="CS.4.1.22.")
    destreza4_1_23 = Destreza.objects.get(codigo="CS.4.1.23.")
    destreza4_1_24 = Destreza.objects.get(codigo="CS.4.1.24.")
    destreza4_1_25 = Destreza.objects.get(codigo="CS.4.1.25.")
    destreza4_1_26 = Destreza.objects.get(codigo="CS.4.1.26.")
    destreza4_1_27 = Destreza.objects.get(codigo="CS.4.1.27.")
    destreza4_1_28 = Destreza.objects.get(codigo="CS.4.1.28.")
    destreza4_1_29 = Destreza.objects.get(codigo="CS.4.1.29.")
    destreza4_1_30 = Destreza.objects.get(codigo="CS.4.1.30.")
    destreza4_1_31 = Destreza.objects.get(codigo="CS.4.1.31.")
    destreza4_1_32 = Destreza.objects.get(codigo="CS.4.1.32.")
    destreza4_1_33 = Destreza.objects.get(codigo="CS.4.1.33.")
    destreza4_1_34 = Destreza.objects.get(codigo="CS.4.1.34.")
    destreza4_1_35 = Destreza.objects.get(codigo="CS.4.1.35.")
    destreza4_1_36 = Destreza.objects.get(codigo="CS.4.1.36.")
    destreza4_1_37 = Destreza.objects.get(codigo="CS.4.1.37.")
    destreza4_1_38 = Destreza.objects.get(codigo="CS.4.1.38.")
    destreza4_1_39 = Destreza.objects.get(codigo="CS.4.1.39.")
    destreza4_1_40 = Destreza.objects.get(codigo="CS.4.1.40.")
    destreza4_1_41 = Destreza.objects.get(codigo="CS.4.1.41.")
    destreza4_1_42 = Destreza.objects.get(codigo="CS.4.1.42.")
    destreza4_1_43 = Destreza.objects.get(codigo="CS.4.1.43.")
    destreza4_1_44 = Destreza.objects.get(codigo="CS.4.1.44.")
    destreza4_1_45 = Destreza.objects.get(codigo="CS.4.1.45.")
    destreza4_1_46 = Destreza.objects.get(codigo="CS.4.1.46.")
    destreza4_1_47 = Destreza.objects.get(codigo="CS.4.1.47.")
    destreza4_1_48 = Destreza.objects.get(codigo="CS.4.1.48.")
    destreza4_1_49 = Destreza.objects.get(codigo="CS.4.1.49.")
    destreza4_1_50 = Destreza.objects.get(codigo="CS.4.1.50.")
    destreza4_1_51 = Destreza.objects.get(codigo="CS.4.1.51.")
    destreza4_1_52 = Destreza.objects.get(codigo="CS.4.1.52.")
    destreza4_1_53 = Destreza.objects.get(codigo="CS.4.1.53.")
    destreza4_1_54 = Destreza.objects.get(codigo="CS.4.1.54.")
    destreza4_1_55 = Destreza.objects.get(codigo="CS.4.1.55.")
    destreza4_1_56 = Destreza.objects.get(codigo="CS.4.1.56.")
    destreza4_1_57 = Destreza.objects.get(codigo="CS.4.1.57.")
    destreza4_1_58 = Destreza.objects.get(codigo="CS.4.1.58.")
    destreza4_1_59 = Destreza.objects.get(codigo="CS.4.1.59.")
    destreza4_1_60 = Destreza.objects.get(codigo="CS.4.1.60.")
    destreza4_2_1 = Destreza.objects.get(codigo="CS.4.2.1.")
    destreza4_2_2 = Destreza.objects.get(codigo="CS.4.2.2.")
    destreza4_2_3 = Destreza.objects.get(codigo="CS.4.2.3.")
    destreza4_2_4 = Destreza.objects.get(codigo="CS.4.2.4.")
    destreza4_2_5 = Destreza.objects.get(codigo="CS.4.2.5.")
    destreza4_2_6 = Destreza.objects.get(codigo="CS.4.2.6.")
    destreza4_2_7 = Destreza.objects.get(codigo="CS.4.2.7.")
    destreza4_2_8 = Destreza.objects.get(codigo="CS.4.2.8.")
    destreza4_2_9 = Destreza.objects.get(codigo="CS.4.2.9.")
    destreza4_2_10 = Destreza.objects.get(codigo="CS.4.2.10.")
    destreza4_2_11 = Destreza.objects.get(codigo="CS.4.2.11.")
    destreza4_2_12 = Destreza.objects.get(codigo="CS.4.2.12.")
    destreza4_2_13 = Destreza.objects.get(codigo="CS.4.2.13.")
    destreza4_2_14 = Destreza.objects.get(codigo="CS.4.2.14.")
    destreza4_2_15 = Destreza.objects.get(codigo="CS.4.2.15.")
    destreza4_2_16 = Destreza.objects.get(codigo="CS.4.2.16.")
    destreza4_2_17 = Destreza.objects.get(codigo="CS.4.2.17.")
    destreza4_2_18 = Destreza.objects.get(codigo="CS.4.2.18.")
    destreza4_2_19 = Destreza.objects.get(codigo="CS.4.2.19.")
    destreza4_2_20 = Destreza.objects.get(codigo="CS.4.2.20.")
    destreza4_2_21 = Destreza.objects.get(codigo="CS.4.2.21.")
    destreza4_2_22 = Destreza.objects.get(codigo="CS.4.2.22.")
    destreza4_2_23 = Destreza.objects.get(codigo="CS.4.2.23.")
    destreza4_2_24 = Destreza.objects.get(codigo="CS.4.2.24.")
    destreza4_2_25 = Destreza.objects.get(codigo="CS.4.2.25.")
    destreza4_2_26 = Destreza.objects.get(codigo="CS.4.2.26.")
    destreza4_2_27 = Destreza.objects.get(codigo="CS.4.2.27.")
    destreza4_2_28 = Destreza.objects.get(codigo="CS.4.2.28.")
    destreza4_2_29 = Destreza.objects.get(codigo="CS.4.2.29.")
    destreza4_2_30 = Destreza.objects.get(codigo="CS.4.2.30.")
    destreza4_2_31 = Destreza.objects.get(codigo="CS.4.2.31.")
    destreza4_2_32 = Destreza.objects.get(codigo="CS.4.2.32.")
    destreza4_2_33 = Destreza.objects.get(codigo="CS.4.2.33.")
    destreza4_2_34 = Destreza.objects.get(codigo="CS.4.2.34.")
    destreza4_2_35 = Destreza.objects.get(codigo="CS.4.2.35.")
    destreza4_2_36 = Destreza.objects.get(codigo="CS.4.2.36.")
    destreza4_2_37 = Destreza.objects.get(codigo="CS.4.2.37.")
    destreza4_2_38 = Destreza.objects.get(codigo="CS.4.2.38.")
    destreza4_2_39 = Destreza.objects.get(codigo="CS.4.2.39.")
    destreza4_2_40 = Destreza.objects.get(codigo="CS.4.2.40.")
    destreza4_2_41 = Destreza.objects.get(codigo="CS.4.2.41.")
    destreza4_3_1 = Destreza.objects.get(codigo="CS.4.3.1.")
    destreza4_3_2 = Destreza.objects.get(codigo="CS.4.3.2.")
    destreza4_3_3 = Destreza.objects.get(codigo="CS.4.3.3.")
    destreza4_3_4 = Destreza.objects.get(codigo="CS.4.3.4.")
    destreza4_3_5 = Destreza.objects.get(codigo="CS.4.3.5.")
    destreza4_3_6 = Destreza.objects.get(codigo="CS.4.3.6.")
    destreza4_3_7 = Destreza.objects.get(codigo="CS.4.3.7.")
    destreza4_3_8 = Destreza.objects.get(codigo="CS.4.3.8.")
    destreza4_3_9 = Destreza.objects.get(codigo="CS.4.3.9.")
    destreza4_3_10 = Destreza.objects.get(codigo="CS.4.3.10.")
    destreza4_3_11 = Destreza.objects.get(codigo="CS.4.3.11.")
    destreza4_3_12 = Destreza.objects.get(codigo="CS.4.3.12.")
    destreza4_3_13 = Destreza.objects.get(codigo="CS.4.3.13.")
    destreza4_3_14 = Destreza.objects.get(codigo="CS.4.3.14.")
    destreza4_3_15 = Destreza.objects.get(codigo="CS.4.3.15.")
    destreza4_3_16 = Destreza.objects.get(codigo="CS.4.3.16.")
    destreza4_3_17 = Destreza.objects.get(codigo="CS.4.3.17.")
    destreza4_3_18 = Destreza.objects.get(codigo="CS.4.3.18.")
    destreza4_3_19 = Destreza.objects.get(codigo="CS.4.3.19.")
    destreza4_3_20 = Destreza.objects.get(codigo="CS.4.3.20.")
    destreza4_3_21 = Destreza.objects.get(codigo="CS.4.3.21.")
    destreza4_3_22 = Destreza.objects.get(codigo="CS.4.3.22.")
    destreza4_3_23 = Destreza.objects.get(codigo="CS.4.3.23.")

    # Asignación

    # Elemental
    criterio2_1.objetivos_generales.add(
        objetivo1,
        objetivo3,
    )
    criterio2_1.destrezas.add(
        destreza2_1_1,
        destreza2_1_2,
        destreza2_1_3,
        destreza2_3_1,
        destreza2_3_4,
    )

    criterio2_2.objetivos_generales.add(
        objetivo1,
        objetivo6,
        objetivo9,
    )
    criterio2_2.destrezas.add(
        destreza2_2_1,
        destreza2_2_2,
        destreza2_2_3,
        destreza2_2_4,
    )

    criterio2_3.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
    )
    criterio2_3.destrezas.add(
        destreza2_1_4,
        destreza2_1_5,
        destreza2_3_2,
        destreza2_3_5,
        destreza2_3_6,
        destreza2_3_13,
    )

    criterio2_4.objetivos_generales.add(
        objetivo1,
        objetivo6,
    )
    criterio2_4.destrezas.add(
        destreza2_1_6,
        destreza2_1_8,
        destreza2_1_9,
        destreza2_1_10,
        destreza2_1_11,
        destreza2_2_5,
        destreza2_2_6,
        destreza2_2_7,
        destreza2_2_9,
        destreza2_2_10,
        destreza2_2_11,
        destreza2_2_15,
        destreza2_3_7,
    )

    criterio2_5.objetivos_generales.add(
        objetivo2,
        objetivo8,
        objetivo10,
    )
    criterio2_5.destrezas.add(
        destreza2_1_7,
        destreza2_2_8,
        destreza2_2_12,
        destreza2_2_13,
        destreza2_2_14,
        destreza2_3_11,
    )

    criterio2_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo10,
    )
    criterio2_6.destrezas.add(
        destreza2_1_12,
        destreza2_2_16,
        destreza2_2_17,
        destreza2_2_18,
        destreza2_2_19,
        destreza2_3_3,
        destreza2_3_8,
        destreza2_3_9,
        destreza2_3_10,
        destreza2_3_12,
    )

    # Media
    criterio3_1.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio3_1.destrezas.add(
        destreza3_1_1,
        destreza3_1_2,
        destreza3_1_3,
        destreza3_1_4,
        destreza3_1_5,
        destreza3_1_6,
        destreza3_1_7,
        destreza3_1_8,
    )

    criterio3_2.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio3_2.destrezas.add(
        destreza3_1_9,
        destreza3_1_10,
        destreza3_1_11,
        destreza3_1_12,
        destreza3_1_13,
        destreza3_1_14,
        destreza3_1_15,
        destreza3_1_16,
        destreza3_1_17,
        destreza3_1_18,
        destreza3_1_19,
    )

    criterio3_3.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio3_3.destrezas.add(
        destreza3_1_20,
        destreza3_1_21,
        destreza3_1_22,
        destreza3_1_23,
        destreza3_1_24,
    )

    criterio3_4.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio3_4.destrezas.add(
        destreza3_1_25,
        destreza3_1_26,
        destreza3_1_27,
        destreza3_1_28,
        destreza3_1_29,
        destreza3_1_30,
        destreza3_1_31,
        destreza3_1_32,
    )

    criterio3_5.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio3_5.destrezas.add(
        destreza3_1_33,
        destreza3_1_34,
        destreza3_1_35,
        destreza3_1_36,
        destreza3_1_37,
        destreza3_1_38,
        destreza3_1_39,
        destreza3_1_40,
        destreza3_1_41,
        destreza3_1_42,
    )

    criterio3_6.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio3_6.destrezas.add(
        destreza3_1_43,
        destreza3_1_44,
        destreza3_1_45,
        destreza3_1_46,
        destreza3_1_47,
        destreza3_1_48,
        destreza3_1_49,
        destreza3_1_50,
    )

    criterio3_7.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo10,
    )
    criterio3_7.destrezas.add(
        destreza3_1_51,
        destreza3_1_52,
        destreza3_1_53,
        destreza3_1_54,
        destreza3_1_55,
        destreza3_1_56,
        destreza3_1_57,
        destreza3_1_58,
        destreza3_1_59,
        destreza3_1_60,
        destreza3_1_61,
        destreza3_1_62,
        destreza3_1_63,
        destreza3_1_64,
        destreza3_1_65,
        destreza3_1_66,
    )

    criterio3_8.objetivos_generales.add(
        objetivo3,
        objetivo9,
        objetivo10,
    )
    criterio3_8.destrezas.add(
        destreza3_2_1,
        destreza3_2_2,
        destreza3_2_3,
        destreza3_2_4,
    )

    criterio3_9.objetivos_generales.add(
        objetivo2,
        objetivo9,
        objetivo10,
    )
    criterio3_9.destrezas.add(
        destreza3_2_5,
        destreza3_2_6,
        destreza3_2_7,
        destreza3_2_8,
        destreza3_2_9,
    )

    criterio3_10.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo7,
    )
    criterio3_10.destrezas.add(
        destreza3_2_10,
        destreza3_2_11,
        destreza3_2_12,
        destreza3_2_13,
        destreza3_2_14,
        destreza3_2_15,
        destreza3_2_16,
        destreza3_2_17,
        destreza3_2_18,
        destreza3_2_23,
    )

    criterio3_11.objetivos_generales.add(
        objetivo1,
        objetivo8,
    )
    criterio3_11.destrezas.add(
        destreza3_2_19,
        destreza3_2_20,
        destreza3_2_21,
        destreza3_2_22,
        destreza3_2_23,
        destreza3_2_24,
        destreza3_2_25,
        destreza3_2_26,
    )

    criterio3_12.objetivos_generales.add(
        objetivo6,
        objetivo9,
    )
    criterio3_12.destrezas.add(
        destreza3_3_1,
        destreza3_3_2,
        destreza3_3_3,
        destreza3_3_4,
        destreza3_3_5,
        destreza3_3_6,
        destreza3_3_7,
    )

    criterio3_13.objetivos_generales.add(
        objetivo6,
        objetivo7,
        objetivo9,
        objetivo10,
    )
    criterio3_13.destrezas.add(
        destreza3_3_8,
        destreza3_3_9,
        destreza3_3_10,
        destreza3_3_11,
        destreza3_3_12,
        destreza3_3_13,
        destreza3_3_14,
        destreza3_3_15,
        destreza3_3_16,
    )

    # Superior
    criterio4_1.objetivos_generales.add(
        objetivo2,
        objetivo10,
    )
    criterio4_1.destrezas.add(
        destreza4_1_1,
        destreza4_1_2,
        destreza4_1_3,
        destreza4_1_4,
        destreza4_1_16,
        destreza4_1_17,
        destreza4_1_18,
        destreza4_1_19,
        destreza4_1_20,
        destreza4_1_21,
        destreza4_1_22,
        destreza4_1_23,
    )

    criterio4_2.objetivos_generales.add(
        objetivo2,
        objetivo10,
    )
    criterio4_2.destrezas.add(
        destreza4_1_5,
        destreza4_1_6,
        destreza4_1_8,
        destreza4_1_10,
        destreza4_1_11,
        destreza4_1_24,
        destreza4_1_25,
        destreza4_1_26,
        destreza4_1_27,
        destreza4_1_28,
        destreza4_1_29,
        destreza4_1_52,
    )

    criterio4_3.objetivos_generales.add(
        objetivo2,
        objetivo10,
    )
    criterio4_3.destrezas.add(
        destreza4_1_7,
        destreza4_1_9,
        destreza4_1_12,
        destreza4_1_13,
        destreza4_1_14,
        destreza4_1_15,
        destreza4_1_30,
        destreza4_1_31,
        destreza4_1_32,
        destreza4_1_34,
    )

    criterio4_4.objetivos_generales.add(
        objetivo2,
        objetivo10,
    )
    criterio4_4.destrezas.add(
        destreza4_1_46,
        destreza4_1_47,
        destreza4_1_48,
        destreza4_1_50,
        destreza4_1_51,
        destreza4_1_53,
        destreza4_1_54,
        destreza4_1_55,
        destreza4_1_56,
    )

    criterio4_5.objetivos_generales.add(
        objetivo2,
        objetivo10,
    )
    criterio4_5.destrezas.add(
        destreza4_1_33,
        destreza4_1_35,
        destreza4_1_36,
        destreza4_1_37,
        destreza4_1_38,
        destreza4_1_39,
        destreza4_1_40,
        destreza4_1_41,
        destreza4_1_42,
        destreza4_1_43,
        destreza4_1_44,
        destreza4_1_45,
        destreza4_1_49,
        destreza4_1_57,
        destreza4_1_58,
        destreza4_1_59,
        destreza4_1_60,
    )

    criterio4_6.objetivos_generales.add(
        objetivo4,
        objetivo5,
        objetivo8,
    )
    criterio4_6.destrezas.add(
        destreza4_2_1,
        destreza4_2_2,
        destreza4_2_3,
        destreza4_2_4,
        destreza4_2_5,
        destreza4_2_6,
        destreza4_2_7,
        destreza4_2_8,
    )

    criterio4_7.objetivos_generales.add(
        objetivo7,
        objetivo10,
    )
    criterio4_7.destrezas.add(
        destreza4_2_9,
        destreza4_2_10,
        destreza4_2_11,
        destreza4_2_12,
        destreza4_2_13,
        destreza4_2_14,
        destreza4_2_15,
        destreza4_2_16,
    )

    criterio4_8.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio4_8.destrezas.add(
        destreza4_2_17,
        destreza4_2_18,
        destreza4_2_19,
        destreza4_2_20,
        destreza4_2_21,
        destreza4_2_22,
        destreza4_2_23,
        destreza4_2_24,
        destreza4_2_25,
    )

    criterio4_9.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio4_9.destrezas.add(
        destreza4_2_26,
        destreza4_2_27,
        destreza4_2_28,
        destreza4_2_29,
        destreza4_2_30,
        destreza4_2_31,
        destreza4_2_32,
        destreza4_2_33,
        destreza4_2_34,
        destreza4_2_35,
        destreza4_2_36,
        destreza4_2_37,
        destreza4_2_38,
        destreza4_2_39,
        destreza4_2_40,
        destreza4_2_41,
        destreza4_3_11,
    )

    criterio4_10.objetivos_generales.add(
        objetivo1,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio4_10.destrezas.add(
        destreza4_3_1,
        destreza4_3_2,
        destreza4_3_3,
        destreza4_3_4,
        destreza4_3_5,
        destreza4_3_6,
        destreza4_3_7,
        destreza4_3_8,
        destreza4_3_9,
        destreza4_3_14,
        destreza4_3_16,
        destreza4_3_19,
    )

    criterio4_11.objetivos_generales.add(
        objetivo1,
        objetivo7,
        objetivo10,
    )
    criterio4_11.destrezas.add(
        destreza4_3_10,
        destreza4_3_12,
        destreza4_3_13,
        destreza4_3_15,
        destreza4_3_17,
        destreza4_3_18,
        destreza4_3_20,
        destreza4_3_21,
        destreza4_3_22,
        destreza4_3_23,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0045_auto_20180908_2006'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
