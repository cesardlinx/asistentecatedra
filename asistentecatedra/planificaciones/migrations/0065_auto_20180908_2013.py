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
    objetivo6 = ObjetivoGeneral.objects.get(codigo="OG.CS.6.")
    objetivo7 = ObjetivoGeneral.objects.get(codigo="OG.CS.7.")
    objetivo8 = ObjetivoGeneral.objects.get(codigo="OG.CS.8.")
    objetivo9 = ObjetivoGeneral.objects.get(codigo="OG.CS.9.")
    objetivo10 = ObjetivoGeneral.objects.get(codigo="OG.CS.10.")

    # Criterios de evaluación
    criterio_historia_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.1.")
    criterio_historia_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.2.")
    criterio_historia_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.3.")
    criterio_historia_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.4.")
    criterio_historia_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.5.")
    criterio_historia_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.6.")
    criterio_historia_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.7.")
    criterio_historia_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.8.")
    criterio_historia_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.9.")
    criterio_historia_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.10.")
    criterio_historia_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.11.")
    criterio_historia_5_12 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.12.")
    criterio_historia_5_13 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.13.")
    criterio_historia_5_14 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.14.")
    criterio_historia_5_15 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.15.")
    criterio_historia_5_16 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.16.")
    criterio_historia_5_17 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.17.")
    criterio_historia_5_18 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.18.")
    criterio_historia_5_19 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.19.")
    criterio_historia_5_20 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.20.")
    criterio_historia_5_21 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.21.")
    criterio_ciudadania_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.1.")
    criterio_ciudadania_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.2.")
    criterio_ciudadania_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.3.")
    criterio_ciudadania_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.4.")
    criterio_ciudadania_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.5.")
    criterio_ciudadania_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.6.")
    criterio_ciudadania_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.7.")
    criterio_ciudadania_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.8.")
    criterio_ciudadania_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.9.")
    criterio_ciudadania_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.10.")
    criterio_filosofia_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.1.")
    criterio_filosofia_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.2.")
    criterio_filosofia_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.3.")
    criterio_filosofia_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.4.")
    criterio_filosofia_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.5.")
    criterio_filosofia_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.6.")
    criterio_filosofia_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.7.")

    # Destrezas Historia
    destreza_historia_5_1_1 = Destreza.objects.get(codigo="CS.H.5.1.1.")
    destreza_historia_5_1_2 = Destreza.objects.get(codigo="CS.H.5.1.2.")
    destreza_historia_5_1_3 = Destreza.objects.get(codigo="CS.H.5.1.3.")
    destreza_historia_5_1_4 = Destreza.objects.get(codigo="CS.H.5.1.4.")
    destreza_historia_5_1_5 = Destreza.objects.get(codigo="CS.H.5.1.5.")
    destreza_historia_5_1_6 = Destreza.objects.get(codigo="CS.H.5.1.6.")
    destreza_historia_5_1_7 = Destreza.objects.get(codigo="CS.H.5.1.7.")
    destreza_historia_5_1_8 = Destreza.objects.get(codigo="CS.H.5.1.8.")
    destreza_historia_5_1_9 = Destreza.objects.get(codigo="CS.H.5.1.9.")
    destreza_historia_5_1_10 = Destreza.objects.get(codigo="CS.H.5.1.10.")
    destreza_historia_5_1_11 = Destreza.objects.get(codigo="CS.H.5.1.11.")
    destreza_historia_5_1_12 = Destreza.objects.get(codigo="CS.H.5.1.12.")
    destreza_historia_5_1_13 = Destreza.objects.get(codigo="CS.H.5.1.13.")
    destreza_historia_5_1_14 = Destreza.objects.get(codigo="CS.H.5.1.14.")
    destreza_historia_5_1_15 = Destreza.objects.get(codigo="CS.H.5.1.15.")
    destreza_historia_5_1_16 = Destreza.objects.get(codigo="CS.H.5.1.16.")
    destreza_historia_5_1_17 = Destreza.objects.get(codigo="CS.H.5.1.17.")
    destreza_historia_5_1_18 = Destreza.objects.get(codigo="CS.H.5.1.18.")
    destreza_historia_5_1_19 = Destreza.objects.get(codigo="CS.H.5.1.19.")
    destreza_historia_5_1_20 = Destreza.objects.get(codigo="CS.H.5.1.20.")
    destreza_historia_5_1_21 = Destreza.objects.get(codigo="CS.H.5.1.21.")
    destreza_historia_5_1_22 = Destreza.objects.get(codigo="CS.H.5.1.22.")
    destreza_historia_5_1_23 = Destreza.objects.get(codigo="CS.H.5.1.23.")
    destreza_historia_5_1_24 = Destreza.objects.get(codigo="CS.H.5.1.24.")
    destreza_historia_5_1_25 = Destreza.objects.get(codigo="CS.H.5.1.25.")
    destreza_historia_5_1_26 = Destreza.objects.get(codigo="CS.H.5.1.26.")
    destreza_historia_5_1_27 = Destreza.objects.get(codigo="CS.H.5.1.27.")
    destreza_historia_5_1_28 = Destreza.objects.get(codigo="CS.H.5.1.28.")
    destreza_historia_5_1_29 = Destreza.objects.get(codigo="CS.H.5.1.29.")
    destreza_historia_5_1_30 = Destreza.objects.get(codigo="CS.H.5.1.30.")
    destreza_historia_5_1_31 = Destreza.objects.get(codigo="CS.H.5.1.31.")
    destreza_historia_5_1_32 = Destreza.objects.get(codigo="CS.H.5.1.32.")
    destreza_historia_5_1_33 = Destreza.objects.get(codigo="CS.H.5.1.33.")
    destreza_historia_5_2_1 = Destreza.objects.get(codigo="CS.H.5.2.1.")
    destreza_historia_5_2_2 = Destreza.objects.get(codigo="CS.H.5.2.2.")
    destreza_historia_5_2_3 = Destreza.objects.get(codigo="CS.H.5.2.3.")
    destreza_historia_5_2_4 = Destreza.objects.get(codigo="CS.H.5.2.4.")
    destreza_historia_5_2_5 = Destreza.objects.get(codigo="CS.H.5.2.5.")
    destreza_historia_5_2_6 = Destreza.objects.get(codigo="CS.H.5.2.6.")
    destreza_historia_5_2_7 = Destreza.objects.get(codigo="CS.H.5.2.7.")
    destreza_historia_5_2_8 = Destreza.objects.get(codigo="CS.H.5.2.8.")
    destreza_historia_5_2_9 = Destreza.objects.get(codigo="CS.H.5.2.9.")
    destreza_historia_5_2_10 = Destreza.objects.get(codigo="CS.H.5.2.10.")
    destreza_historia_5_2_11 = Destreza.objects.get(codigo="CS.H.5.2.11.")
    destreza_historia_5_2_12 = Destreza.objects.get(codigo="CS.H.5.2.12.")
    destreza_historia_5_2_13 = Destreza.objects.get(codigo="CS.H.5.2.13.")
    destreza_historia_5_2_14 = Destreza.objects.get(codigo="CS.H.5.2.14.")
    destreza_historia_5_2_15 = Destreza.objects.get(codigo="CS.H.5.2.15.")
    destreza_historia_5_2_16 = Destreza.objects.get(codigo="CS.H.5.2.16.")
    destreza_historia_5_2_17 = Destreza.objects.get(codigo="CS.H.5.2.17.")
    destreza_historia_5_2_18 = Destreza.objects.get(codigo="CS.H.5.2.18.")
    destreza_historia_5_2_19 = Destreza.objects.get(codigo="CS.H.5.2.19.")
    destreza_historia_5_2_20 = Destreza.objects.get(codigo="CS.H.5.2.20.")
    destreza_historia_5_2_21 = Destreza.objects.get(codigo="CS.H.5.2.21.")
    destreza_historia_5_2_22 = Destreza.objects.get(codigo="CS.H.5.2.22.")
    destreza_historia_5_2_23 = Destreza.objects.get(codigo="CS.H.5.2.23.")
    destreza_historia_5_2_24 = Destreza.objects.get(codigo="CS.H.5.2.24.")
    destreza_historia_5_2_25 = Destreza.objects.get(codigo="CS.H.5.2.25.")
    destreza_historia_5_2_26 = Destreza.objects.get(codigo="CS.H.5.2.26.")
    destreza_historia_5_2_27 = Destreza.objects.get(codigo="CS.H.5.2.27.")
    destreza_historia_5_2_28 = Destreza.objects.get(codigo="CS.H.5.2.28.")
    destreza_historia_5_2_29 = Destreza.objects.get(codigo="CS.H.5.2.29.")
    destreza_historia_5_2_30 = Destreza.objects.get(codigo="CS.H.5.2.30.")
    destreza_historia_5_2_31 = Destreza.objects.get(codigo="CS.H.5.2.31.")
    destreza_historia_5_2_32 = Destreza.objects.get(codigo="CS.H.5.2.32.")
    destreza_historia_5_2_33 = Destreza.objects.get(codigo="CS.H.5.2.33.")
    destreza_historia_5_2_34 = Destreza.objects.get(codigo="CS.H.5.2.34.")
    destreza_historia_5_3_1 = Destreza.objects.get(codigo="CS.H.5.3.1.")
    destreza_historia_5_3_2 = Destreza.objects.get(codigo="CS.H.5.3.2.")
    destreza_historia_5_3_3 = Destreza.objects.get(codigo="CS.H.5.3.3.")
    destreza_historia_5_3_4 = Destreza.objects.get(codigo="CS.H.5.3.4.")
    destreza_historia_5_3_5 = Destreza.objects.get(codigo="CS.H.5.3.5.")
    destreza_historia_5_3_6 = Destreza.objects.get(codigo="CS.H.5.3.6.")
    destreza_historia_5_3_7 = Destreza.objects.get(codigo="CS.H.5.3.7.")
    destreza_historia_5_3_8 = Destreza.objects.get(codigo="CS.H.5.3.8.")
    destreza_historia_5_3_9 = Destreza.objects.get(codigo="CS.H.5.3.9.")
    destreza_historia_5_3_10 = Destreza.objects.get(codigo="CS.H.5.3.10.")
    destreza_historia_5_3_11 = Destreza.objects.get(codigo="CS.H.5.3.11.")
    destreza_historia_5_3_12 = Destreza.objects.get(codigo="CS.H.5.3.12.")
    destreza_historia_5_3_13 = Destreza.objects.get(codigo="CS.H.5.3.13.")
    destreza_historia_5_3_14 = Destreza.objects.get(codigo="CS.H.5.3.14.")
    destreza_historia_5_3_15 = Destreza.objects.get(codigo="CS.H.5.3.15.")
    destreza_historia_5_3_16 = Destreza.objects.get(codigo="CS.H.5.3.16.")
    destreza_historia_5_3_17 = Destreza.objects.get(codigo="CS.H.5.3.17.")
    destreza_historia_5_3_18 = Destreza.objects.get(codigo="CS.H.5.3.18.")
    destreza_historia_5_3_19 = Destreza.objects.get(codigo="CS.H.5.3.19.")
    destreza_historia_5_3_20 = Destreza.objects.get(codigo="CS.H.5.3.20.")
    destreza_historia_5_3_21 = Destreza.objects.get(codigo="CS.H.5.3.21.")
    destreza_historia_5_3_22 = Destreza.objects.get(codigo="CS.H.5.3.22.")
    destreza_historia_5_3_23 = Destreza.objects.get(codigo="CS.H.5.3.23.")
    destreza_historia_5_3_24 = Destreza.objects.get(codigo="CS.H.5.3.24.")
    destreza_historia_5_3_25 = Destreza.objects.get(codigo="CS.H.5.3.25.")
    destreza_historia_5_3_26 = Destreza.objects.get(codigo="CS.H.5.3.26.")
    destreza_historia_5_3_27 = Destreza.objects.get(codigo="CS.H.5.3.27.")
    destreza_historia_5_3_28 = Destreza.objects.get(codigo="CS.H.5.3.28.")
    destreza_historia_5_3_29 = Destreza.objects.get(codigo="CS.H.5.3.29.")
    destreza_historia_5_3_30 = Destreza.objects.get(codigo="CS.H.5.3.30.")
    destreza_historia_5_3_31 = Destreza.objects.get(codigo="CS.H.5.3.31.")
    destreza_historia_5_3_32 = Destreza.objects.get(codigo="CS.H.5.3.32.")
    destreza_historia_5_3_33 = Destreza.objects.get(codigo="CS.H.5.3.33.")
    destreza_historia_5_3_34 = Destreza.objects.get(codigo="CS.H.5.3.34.")
    destreza_historia_5_3_35 = Destreza.objects.get(codigo="CS.H.5.3.35.")
    destreza_historia_5_3_36 = Destreza.objects.get(codigo="CS.H.5.3.36.")
    destreza_historia_5_3_37 = Destreza.objects.get(codigo="CS.H.5.3.37.")
    destreza_historia_5_3_38 = Destreza.objects.get(codigo="CS.H.5.3.38.")
    destreza_historia_5_3_39 = Destreza.objects.get(codigo="CS.H.5.3.39.")
    destreza_historia_5_3_40 = Destreza.objects.get(codigo="CS.H.5.3.40.")
    destreza_historia_5_3_41 = Destreza.objects.get(codigo="CS.H.5.3.41.")
    destreza_historia_5_3_42 = Destreza.objects.get(codigo="CS.H.5.3.42.")
    destreza_historia_5_3_43 = Destreza.objects.get(codigo="CS.H.5.3.43.")
    destreza_historia_5_3_44 = Destreza.objects.get(codigo="CS.H.5.3.44.")
    destreza_historia_5_3_45 = Destreza.objects.get(codigo="CS.H.5.3.45.")
    destreza_historia_5_3_46 = Destreza.objects.get(codigo="CS.H.5.3.46.")
    destreza_historia_5_3_47 = Destreza.objects.get(codigo="CS.H.5.3.47.")
    destreza_historia_5_3_48 = Destreza.objects.get(codigo="CS.H.5.3.48.")
    destreza_historia_5_3_49 = Destreza.objects.get(codigo="CS.H.5.3.49.")
    destreza_historia_5_3_50 = Destreza.objects.get(codigo="CS.H.5.3.50.")
    destreza_historia_5_3_51 = Destreza.objects.get(codigo="CS.H.5.3.51.")
    destreza_historia_5_3_52 = Destreza.objects.get(codigo="CS.H.5.3.52.")
    destreza_historia_5_3_53 = Destreza.objects.get(codigo="CS.H.5.3.53.")
    destreza_historia_5_4_1 = Destreza.objects.get(codigo="CS.H.5.4.1.")
    destreza_historia_5_4_2 = Destreza.objects.get(codigo="CS.H.5.4.2.")
    destreza_historia_5_4_3 = Destreza.objects.get(codigo="CS.H.5.4.3.")
    destreza_historia_5_4_4 = Destreza.objects.get(codigo="CS.H.5.4.4.")
    destreza_historia_5_4_5 = Destreza.objects.get(codigo="CS.H.5.4.5.")
    destreza_historia_5_4_6 = Destreza.objects.get(codigo="CS.H.5.4.6.")
    destreza_historia_5_4_7 = Destreza.objects.get(codigo="CS.H.5.4.7.")
    destreza_historia_5_4_8 = Destreza.objects.get(codigo="CS.H.5.4.8.")
    destreza_historia_5_4_9 = Destreza.objects.get(codigo="CS.H.5.4.9.")
    destreza_historia_5_4_10 = Destreza.objects.get(codigo="CS.H.5.4.10.")
    destreza_historia_5_4_11 = Destreza.objects.get(codigo="CS.H.5.4.11.")
    destreza_historia_5_4_12 = Destreza.objects.get(codigo="CS.H.5.4.12.")
    destreza_historia_5_4_13 = Destreza.objects.get(codigo="CS.H.5.4.13.")
    destreza_historia_5_4_14 = Destreza.objects.get(codigo="CS.H.5.4.14.")
    destreza_historia_5_4_15 = Destreza.objects.get(codigo="CS.H.5.4.15.")
    destreza_historia_5_4_16 = Destreza.objects.get(codigo="CS.H.5.4.16.")
    destreza_historia_5_4_17 = Destreza.objects.get(codigo="CS.H.5.4.17.")
    destreza_historia_5_4_18 = Destreza.objects.get(codigo="CS.H.5.4.18.")
    destreza_historia_5_4_19 = Destreza.objects.get(codigo="CS.H.5.4.19.")
    destreza_historia_5_4_20 = Destreza.objects.get(codigo="CS.H.5.4.20.")
    destreza_historia_5_4_21 = Destreza.objects.get(codigo="CS.H.5.4.21.")
    destreza_historia_5_4_22 = Destreza.objects.get(codigo="CS.H.5.4.22.")
    destreza_historia_5_4_23 = Destreza.objects.get(codigo="CS.H.5.4.23.")
    destreza_historia_5_4_24 = Destreza.objects.get(codigo="CS.H.5.4.24.")
    destreza_historia_5_4_25 = Destreza.objects.get(codigo="CS.H.5.4.25.")
    destreza_historia_5_4_26 = Destreza.objects.get(codigo="CS.H.5.4.26.")
    destreza_historia_5_4_27 = Destreza.objects.get(codigo="CS.H.5.4.27.")
    destreza_historia_5_4_28 = Destreza.objects.get(codigo="CS.H.5.4.28.")
    destreza_historia_5_4_29 = Destreza.objects.get(codigo="CS.H.5.4.29.")
    destreza_historia_5_4_30 = Destreza.objects.get(codigo="CS.H.5.4.30.")
    destreza_historia_5_4_31 = Destreza.objects.get(codigo="CS.H.5.4.31.")
    destreza_historia_5_4_32 = Destreza.objects.get(codigo="CS.H.5.4.32.")
    destreza_historia_5_4_33 = Destreza.objects.get(codigo="CS.H.5.4.33.")
    destreza_historia_5_4_34 = Destreza.objects.get(codigo="CS.H.5.4.34.")
    destreza_historia_5_4_35 = Destreza.objects.get(codigo="CS.H.5.4.35.")
    destreza_historia_5_4_36 = Destreza.objects.get(codigo="CS.H.5.4.36.")
    destreza_historia_5_4_37 = Destreza.objects.get(codigo="CS.H.5.4.37.")
    destreza_historia_5_4_38 = Destreza.objects.get(codigo="CS.H.5.4.38.")
    destreza_historia_5_4_39 = Destreza.objects.get(codigo="CS.H.5.4.39.")
    destreza_historia_5_4_40 = Destreza.objects.get(codigo="CS.H.5.4.40.")
    destreza_historia_5_4_41 = Destreza.objects.get(codigo="CS.H.5.4.41.")

    # Destrezas Educacion para la Ciudadanía
    destreza_ciudadania_5_1_1 = Destreza.objects.get(codigo="CS.EC.5.1.1.")
    destreza_ciudadania_5_1_2 = Destreza.objects.get(codigo="CS.EC.5.1.2.")
    destreza_ciudadania_5_1_3 = Destreza.objects.get(codigo="CS.EC.5.1.3.")
    destreza_ciudadania_5_1_4 = Destreza.objects.get(codigo="CS.EC.5.1.4.")
    destreza_ciudadania_5_1_5 = Destreza.objects.get(codigo="CS.EC.5.1.5.")
    destreza_ciudadania_5_1_6 = Destreza.objects.get(codigo="CS.EC.5.1.6.")
    destreza_ciudadania_5_1_7 = Destreza.objects.get(codigo="CS.EC.5.1.7.")
    destreza_ciudadania_5_1_8 = Destreza.objects.get(codigo="CS.EC.5.1.8.")
    destreza_ciudadania_5_1_9 = Destreza.objects.get(codigo="CS.EC.5.1.9.")
    destreza_ciudadania_5_1_10 = Destreza.objects.get(codigo="CS.EC.5.1.10.")
    destreza_ciudadania_5_1_11 = Destreza.objects.get(codigo="CS.EC.5.1.11.")
    destreza_ciudadania_5_1_12 = Destreza.objects.get(codigo="CS.EC.5.1.12.")
    destreza_ciudadania_5_1_13 = Destreza.objects.get(codigo="CS.EC.5.1.13.")
    destreza_ciudadania_5_2_1 = Destreza.objects.get(codigo="CS.EC.5.2.1.")
    destreza_ciudadania_5_2_2 = Destreza.objects.get(codigo="CS.EC.5.2.2.")
    destreza_ciudadania_5_2_3 = Destreza.objects.get(codigo="CS.EC.5.2.3.")
    destreza_ciudadania_5_2_4 = Destreza.objects.get(codigo="CS.EC.5.2.4.")
    destreza_ciudadania_5_2_5 = Destreza.objects.get(codigo="CS.EC.5.2.5.")
    destreza_ciudadania_5_2_6 = Destreza.objects.get(codigo="CS.EC.5.2.6.")
    destreza_ciudadania_5_2_7 = Destreza.objects.get(codigo="CS.EC.5.2.7.")
    destreza_ciudadania_5_2_8 = Destreza.objects.get(codigo="CS.EC.5.2.8.")
    destreza_ciudadania_5_2_9 = Destreza.objects.get(codigo="CS.EC.5.2.9.")
    destreza_ciudadania_5_2_10 = Destreza.objects.get(codigo="CS.EC.5.2.10.")
    destreza_ciudadania_5_2_11 = Destreza.objects.get(codigo="CS.EC.5.2.11.")
    destreza_ciudadania_5_2_12 = Destreza.objects.get(codigo="CS.EC.5.2.12.")
    destreza_ciudadania_5_2_13 = Destreza.objects.get(codigo="CS.EC.5.2.13.")
    destreza_ciudadania_5_2_14 = Destreza.objects.get(codigo="CS.EC.5.2.14.")
    destreza_ciudadania_5_2_15 = Destreza.objects.get(codigo="CS.EC.5.2.15.")
    destreza_ciudadania_5_2_16 = Destreza.objects.get(codigo="CS.EC.5.2.16.")
    destreza_ciudadania_5_2_17 = Destreza.objects.get(codigo="CS.EC.5.2.17.")
    destreza_ciudadania_5_2_18 = Destreza.objects.get(codigo="CS.EC.5.2.18.")
    destreza_ciudadania_5_2_19 = Destreza.objects.get(codigo="CS.EC.5.2.19.")
    destreza_ciudadania_5_2_20 = Destreza.objects.get(codigo="CS.EC.5.2.20.")
    destreza_ciudadania_5_2_21 = Destreza.objects.get(codigo="CS.EC.5.2.21.")
    destreza_ciudadania_5_3_1 = Destreza.objects.get(codigo="CS.EC.5.3.1.")
    destreza_ciudadania_5_3_2 = Destreza.objects.get(codigo="CS.EC.5.3.2.")
    destreza_ciudadania_5_3_3 = Destreza.objects.get(codigo="CS.EC.5.3.3.")
    destreza_ciudadania_5_3_4 = Destreza.objects.get(codigo="CS.EC.5.3.4.")
    destreza_ciudadania_5_3_5 = Destreza.objects.get(codigo="CS.EC.5.3.5.")
    destreza_ciudadania_5_3_6 = Destreza.objects.get(codigo="CS.EC.5.3.6.")
    destreza_ciudadania_5_3_7 = Destreza.objects.get(codigo="CS.EC.5.3.7.")
    destreza_ciudadania_5_3_8 = Destreza.objects.get(codigo="CS.EC.5.3.8.")
    destreza_ciudadania_5_3_9 = Destreza.objects.get(codigo="CS.EC.5.3.9.")
    destreza_ciudadania_5_4_1 = Destreza.objects.get(codigo="CS.EC.5.4.1.")
    destreza_ciudadania_5_4_2 = Destreza.objects.get(codigo="CS.EC.5.4.2.")
    destreza_ciudadania_5_4_3 = Destreza.objects.get(codigo="CS.EC.5.4.3.")
    destreza_ciudadania_5_4_4 = Destreza.objects.get(codigo="CS.EC.5.4.4.")
    destreza_ciudadania_5_4_5 = Destreza.objects.get(codigo="CS.EC.5.4.5.")
    destreza_ciudadania_5_4_6 = Destreza.objects.get(codigo="CS.EC.5.4.6.")
    destreza_ciudadania_5_4_7 = Destreza.objects.get(codigo="CS.EC.5.4.7.")
    destreza_ciudadania_5_4_8 = Destreza.objects.get(codigo="CS.EC.5.4.8.")
    destreza_ciudadania_5_4_9 = Destreza.objects.get(codigo="CS.EC.5.4.9.")
    destreza_ciudadania_5_4_10 = Destreza.objects.get(codigo="CS.EC.5.4.10.")
    destreza_ciudadania_5_4_11 = Destreza.objects.get(codigo="CS.EC.5.4.11.")
    destreza_ciudadania_5_4_12 = Destreza.objects.get(codigo="CS.EC.5.4.12.")

    # Destrezas Filosofía
    destreza_filosofia_5_1_1 = Destreza.objects.get(codigo="CS.F.5.1.1.")
    destreza_filosofia_5_1_2 = Destreza.objects.get(codigo="CS.F.5.1.2.")
    destreza_filosofia_5_1_3 = Destreza.objects.get(codigo="CS.F.5.1.3.")
    destreza_filosofia_5_1_4 = Destreza.objects.get(codigo="CS.F.5.1.4.")
    destreza_filosofia_5_1_5 = Destreza.objects.get(codigo="CS.F.5.1.5.")
    destreza_filosofia_5_1_6 = Destreza.objects.get(codigo="CS.F.5.1.6.")
    destreza_filosofia_5_1_7 = Destreza.objects.get(codigo="CS.F.5.1.7.")
    destreza_filosofia_5_1_8 = Destreza.objects.get(codigo="CS.F.5.1.8.")
    destreza_filosofia_5_1_9 = Destreza.objects.get(codigo="CS.F.5.1.9.")
    destreza_filosofia_5_1_10 = Destreza.objects.get(codigo="CS.F.5.1.10.")
    destreza_filosofia_5_1_11 = Destreza.objects.get(codigo="CS.F.5.1.11.")
    destreza_filosofia_5_1_12 = Destreza.objects.get(codigo="CS.F.5.1.12.")
    destreza_filosofia_5_2_1 = Destreza.objects.get(codigo="CS.F.5.2.1.")
    destreza_filosofia_5_2_2 = Destreza.objects.get(codigo="CS.F.5.2.2.")
    destreza_filosofia_5_2_3 = Destreza.objects.get(codigo="CS.F.5.2.3.")
    destreza_filosofia_5_2_4 = Destreza.objects.get(codigo="CS.F.5.2.4.")
    destreza_filosofia_5_2_5 = Destreza.objects.get(codigo="CS.F.5.2.5.")
    destreza_filosofia_5_2_6 = Destreza.objects.get(codigo="CS.F.5.2.6.")
    destreza_filosofia_5_2_7 = Destreza.objects.get(codigo="CS.F.5.2.7.")
    destreza_filosofia_5_2_8 = Destreza.objects.get(codigo="CS.F.5.2.8.")
    destreza_filosofia_5_2_9 = Destreza.objects.get(codigo="CS.F.5.2.9.")
    destreza_filosofia_5_2_10 = Destreza.objects.get(codigo="CS.F.5.2.10.")
    destreza_filosofia_5_2_11 = Destreza.objects.get(codigo="CS.F.5.2.11.")
    destreza_filosofia_5_2_12 = Destreza.objects.get(codigo="CS.F.5.2.12.")
    destreza_filosofia_5_2_13 = Destreza.objects.get(codigo="CS.F.5.2.13.")
    destreza_filosofia_5_2_14 = Destreza.objects.get(codigo="CS.F.5.2.14.")
    destreza_filosofia_5_2_15 = Destreza.objects.get(codigo="CS.F.5.2.15.")
    destreza_filosofia_5_2_16 = Destreza.objects.get(codigo="CS.F.5.2.16.")
    destreza_filosofia_5_2_17 = Destreza.objects.get(codigo="CS.F.5.2.17.")
    destreza_filosofia_5_2_18 = Destreza.objects.get(codigo="CS.F.5.2.18.")
    destreza_filosofia_5_3_1 = Destreza.objects.get(codigo="CS.F.5.3.1.")
    destreza_filosofia_5_3_2 = Destreza.objects.get(codigo="CS.F.5.3.2.")
    destreza_filosofia_5_3_3 = Destreza.objects.get(codigo="CS.F.5.3.3.")
    destreza_filosofia_5_3_4 = Destreza.objects.get(codigo="CS.F.5.3.4.")
    destreza_filosofia_5_3_5 = Destreza.objects.get(codigo="CS.F.5.3.5.")
    destreza_filosofia_5_3_6 = Destreza.objects.get(codigo="CS.F.5.3.6.")
    destreza_filosofia_5_3_7 = Destreza.objects.get(codigo="CS.F.5.3.7.")
    destreza_filosofia_5_3_8 = Destreza.objects.get(codigo="CS.F.5.3.8.")
    destreza_filosofia_5_3_9 = Destreza.objects.get(codigo="CS.F.5.3.9.")
    destreza_filosofia_5_3_10 = Destreza.objects.get(codigo="CS.F.5.3.10.")
    destreza_filosofia_5_4_1 = Destreza.objects.get(codigo="CS.F.5.4.1.")
    destreza_filosofia_5_4_2 = Destreza.objects.get(codigo="CS.F.5.4.2.")
    destreza_filosofia_5_4_3 = Destreza.objects.get(codigo="CS.F.5.4.3.")
    destreza_filosofia_5_4_4 = Destreza.objects.get(codigo="CS.F.5.4.4.")
    destreza_filosofia_5_4_5 = Destreza.objects.get(codigo="CS.F.5.4.5.")
    destreza_filosofia_5_4_6 = Destreza.objects.get(codigo="CS.F.5.4.6.")
    destreza_filosofia_5_4_7 = Destreza.objects.get(codigo="CS.F.5.4.7.")
    destreza_filosofia_5_4_8 = Destreza.objects.get(codigo="CS.F.5.4.8.")
    destreza_filosofia_5_4_9 = Destreza.objects.get(codigo="CS.F.5.4.9.")
    destreza_filosofia_5_4_10 = Destreza.objects.get(codigo="CS.F.5.4.10.")
    destreza_filosofia_5_4_11 = Destreza.objects.get(codigo="CS.F.5.4.11.")
    destreza_filosofia_5_4_12 = Destreza.objects.get(codigo="CS.F.5.4.12.")
    destreza_filosofia_5_4_13 = Destreza.objects.get(codigo="CS.F.5.4.13.")

    # Historia
    criterio_historia_5_1.objetivos_generales.add(
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_1.destrezas.add(
        destreza_historia_5_1_1,
        destreza_historia_5_1_2,
        destreza_historia_5_1_5,
        destreza_historia_5_1_6,
    )

    criterio_historia_5_2.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_2.destrezas.add(
        destreza_historia_5_1_3,
        destreza_historia_5_1_7,
        destreza_historia_5_1_8,
        destreza_historia_5_1_9,
        destreza_historia_5_1_10,
        destreza_historia_5_1_11,
        destreza_historia_5_4_1,
        destreza_historia_5_4_2,
    )

    criterio_historia_5_3.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo7,
    )
    criterio_historia_5_3.destrezas.add(
        destreza_historia_5_1_4,
        destreza_historia_5_1_12,
        destreza_historia_5_1_13,
        destreza_historia_5_1_15,
        destreza_historia_5_1_19,
        destreza_historia_5_4_3,
        destreza_historia_5_4_4,
    )

    criterio_historia_5_4.objetivos_generales.add(
        objetivo3,
        objetivo6,
        objetivo7,
        objetivo8,
    )
    criterio_historia_5_4.destrezas.add(
        destreza_historia_5_1_14,
        destreza_historia_5_1_22,
        destreza_historia_5_1_27,
        destreza_historia_5_1_28,
        destreza_historia_5_1_31,
        destreza_historia_5_2_6,
        destreza_historia_5_2_8,
        destreza_historia_5_2_17,
        destreza_historia_5_2_29,
        destreza_historia_5_3_28,
    )

    criterio_historia_5_5.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo7,
    )
    criterio_historia_5_5.destrezas.add(
        destreza_historia_5_1_16,
        destreza_historia_5_1_17,
        destreza_historia_5_1_18,
        destreza_historia_5_1_20,
        destreza_historia_5_1_21,
    )

    criterio_historia_5_6.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_6.destrezas.add(
        destreza_historia_5_1_24,
        destreza_historia_5_1_25,
        destreza_historia_5_1_26,
        destreza_historia_5_1_29,
        destreza_historia_5_1_30,
        destreza_historia_5_1_32,
        destreza_historia_5_2_1,
        destreza_historia_5_2_2,
    )

    criterio_historia_5_7.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_7.destrezas.add(
        destreza_historia_5_2_3,
        destreza_historia_5_2_4,
        destreza_historia_5_2_5,
        destreza_historia_5_2_7,
        destreza_historia_5_2_9,
        destreza_historia_5_2_10,
        destreza_historia_5_2_11,
        destreza_historia_5_2_12,
    )

    criterio_historia_5_8.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_8.destrezas.add(
        destreza_historia_5_1_23,
        destreza_historia_5_1_33,
        destreza_historia_5_2_13,
        destreza_historia_5_2_14,
        destreza_historia_5_2_15,
        destreza_historia_5_2_16,
        destreza_historia_5_2_18,
    )

    criterio_historia_5_9.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_9.destrezas.add(
        destreza_historia_5_2_19,
        destreza_historia_5_2_20,
        destreza_historia_5_2_21,
        destreza_historia_5_2_22,
        destreza_historia_5_2_23,
        destreza_historia_5_2_24,
        destreza_historia_5_2_25,
        destreza_historia_5_2_26,
    )

    criterio_historia_5_10.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_10.destrezas.add(
        destreza_historia_5_2_27,
        destreza_historia_5_2_28,
        destreza_historia_5_2_30,
        destreza_historia_5_2_31,
        destreza_historia_5_2_32,
        destreza_historia_5_2_33,
        destreza_historia_5_2_34,
    )

    criterio_historia_5_11.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_11.destrezas.add(
        destreza_historia_5_3_1,
        destreza_historia_5_3_2,
        destreza_historia_5_3_3,
        destreza_historia_5_3_4,
        destreza_historia_5_3_5,
        destreza_historia_5_3_6,
        destreza_historia_5_3_7,
        destreza_historia_5_3_8,
        destreza_historia_5_3_9,
    )

    criterio_historia_5_12.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo7,
        objetivo10,
    )
    criterio_historia_5_12.destrezas.add(
        destreza_historia_5_3_10,
        destreza_historia_5_3_11,
        destreza_historia_5_3_12,
        destreza_historia_5_3_13,
        destreza_historia_5_3_14,
        destreza_historia_5_3_15,
        destreza_historia_5_3_16,
        destreza_historia_5_3_17,
        destreza_historia_5_3_18,
        destreza_historia_5_3_30,
        destreza_historia_5_3_31,
    )

    criterio_historia_5_13.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_13.destrezas.add(
        destreza_historia_5_3_19,
        destreza_historia_5_3_20,
        destreza_historia_5_3_21,
        destreza_historia_5_3_22,
        destreza_historia_5_3_23,
    )

    criterio_historia_5_14.objetivos_generales.add(
        objetivo3,
        objetivo7,
        objetivo10,
    )
    criterio_historia_5_14.destrezas.add(
        destreza_historia_5_3_24,
        destreza_historia_5_3_25,
        destreza_historia_5_3_26,
        destreza_historia_5_3_27,
        destreza_historia_5_3_29,
    )

    criterio_historia_5_15.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_15.destrezas.add(
        destreza_historia_5_3_32,
        destreza_historia_5_3_33,
        destreza_historia_5_3_34,
        destreza_historia_5_3_35,
        destreza_historia_5_3_40,
        destreza_historia_5_3_41,
        destreza_historia_5_3_42,
        destreza_historia_5_3_45,
        destreza_historia_5_3_46,
        destreza_historia_5_3_47,
    )

    criterio_historia_5_16.objetivos_generales.add(
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_16.destrezas.add(
        destreza_historia_5_3_36,
        destreza_historia_5_3_37,
        destreza_historia_5_3_38,
        destreza_historia_5_3_39,
        destreza_historia_5_3_43,
        destreza_historia_5_3_44,
    )

    criterio_historia_5_17.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_17.destrezas.add(
        destreza_historia_5_3_48,
        destreza_historia_5_3_49,
        destreza_historia_5_3_50,
        destreza_historia_5_3_51,
        destreza_historia_5_3_52,
        destreza_historia_5_3_53,
    )

    criterio_historia_5_18.objetivos_generales.add(
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_18.destrezas.add(
        destreza_historia_5_4_5,
        destreza_historia_5_4_6,
        destreza_historia_5_4_7,
        destreza_historia_5_4_8,
        destreza_historia_5_4_9,
        destreza_historia_5_4_10,
        destreza_historia_5_4_11,
        destreza_historia_5_4_12,
    )

    criterio_historia_5_19.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_19.destrezas.add(
        destreza_historia_5_4_13,
        destreza_historia_5_4_14,
        destreza_historia_5_4_15,
        destreza_historia_5_4_16,
        destreza_historia_5_4_17,
        destreza_historia_5_4_18,
        destreza_historia_5_4_19,
        destreza_historia_5_4_20,
    )

    criterio_historia_5_20.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo10,
    )
    criterio_historia_5_20.destrezas.add(
        destreza_historia_5_4_21,
        destreza_historia_5_4_22,
        destreza_historia_5_4_23,
        destreza_historia_5_4_24,
        destreza_historia_5_4_25,
        destreza_historia_5_4_26,
        destreza_historia_5_4_27,
        destreza_historia_5_4_28,
        destreza_historia_5_4_29,
        destreza_historia_5_4_30,
        destreza_historia_5_4_31,
        destreza_historia_5_4_32,
    )

    criterio_historia_5_21.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo7,
        objetivo10,
    )
    criterio_historia_5_21.destrezas.add(
        destreza_historia_5_4_33,
        destreza_historia_5_4_34,
        destreza_historia_5_4_35,
        destreza_historia_5_4_36,
        destreza_historia_5_4_37,
        destreza_historia_5_4_38,
        destreza_historia_5_4_39,
        destreza_historia_5_4_40,
        destreza_historia_5_4_41,
    )

    # Educación para la ciudadanía
    criterio_ciudadania_5_1.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
    )
    criterio_ciudadania_5_1.destrezas.add(
        destreza_ciudadania_5_1_1,
        destreza_ciudadania_5_1_2,
        destreza_ciudadania_5_1_3,
        destreza_ciudadania_5_1_4,
        destreza_ciudadania_5_1_5,
        destreza_ciudadania_5_1_7,
        destreza_ciudadania_5_1_11,
    )

    criterio_ciudadania_5_2.objetivos_generales.add(
        objetivo1,
        objetivo6,
    )
    criterio_ciudadania_5_2.destrezas.add(
        destreza_ciudadania_5_1_6,
        destreza_ciudadania_5_1_8,
        destreza_ciudadania_5_1_9,
        destreza_ciudadania_5_1_10,
        destreza_ciudadania_5_1_12,
        destreza_ciudadania_5_1_13,
    )

    criterio_ciudadania_5_3.objetivos_generales.add(
        objetivo1,
        objetivo6,
        objetivo7,
    )
    criterio_ciudadania_5_3.destrezas.add(
        destreza_ciudadania_5_2_1,
        destreza_ciudadania_5_2_2,
        destreza_ciudadania_5_2_3,
        destreza_ciudadania_5_2_4,
        destreza_ciudadania_5_2_5,
        destreza_ciudadania_5_2_10,
        destreza_ciudadania_5_2_13,
        destreza_ciudadania_5_3_7,
    )

    criterio_ciudadania_5_4.objetivos_generales.add(
        objetivo1,
        objetivo6,
    )
    criterio_ciudadania_5_4.destrezas.add(
        destreza_ciudadania_5_2_6,
        destreza_ciudadania_5_2_7,
        destreza_ciudadania_5_2_9,
        destreza_ciudadania_5_2_11,
        destreza_ciudadania_5_2_12,
        destreza_ciudadania_5_2_14,
        destreza_ciudadania_5_2_15,
        destreza_ciudadania_5_2_16,
        destreza_ciudadania_5_2_17,
    )

    criterio_ciudadania_5_5.objetivos_generales.add(
        objetivo1,
        objetivo6,
    )
    criterio_ciudadania_5_5.destrezas.add(
        destreza_ciudadania_5_2_18,
        destreza_ciudadania_5_2_19,
        destreza_ciudadania_5_2_20,
        destreza_ciudadania_5_2_21,
    )

    criterio_ciudadania_5_6.objetivos_generales.add(
        objetivo2,
        objetivo3,
        objetivo6,
    )
    criterio_ciudadania_5_6.destrezas.add(
        destreza_ciudadania_5_3_1,
        destreza_ciudadania_5_3_5,
        destreza_ciudadania_5_3_6,
        destreza_ciudadania_5_3_9,
    )

    criterio_ciudadania_5_7.objetivos_generales.add(
        objetivo1,
        objetivo8,
        objetivo9,
    )
    criterio_ciudadania_5_7.destrezas.add(
        destreza_ciudadania_5_3_2,
        destreza_ciudadania_5_3_3,
        destreza_ciudadania_5_3_4,
        destreza_ciudadania_5_3_8,
    )

    criterio_ciudadania_5_8.objetivos_generales.add(
        objetivo1,
        objetivo8,
        objetivo9,
    )
    criterio_ciudadania_5_8.destrezas.add(
        destreza_ciudadania_5_4_1,
        destreza_ciudadania_5_4_2,
        destreza_ciudadania_5_4_3,
        destreza_ciudadania_5_4_12,
    )

    criterio_ciudadania_5_9.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
    )
    criterio_ciudadania_5_9.destrezas.add(
        destreza_ciudadania_5_4_4,
        destreza_ciudadania_5_4_5,
        destreza_ciudadania_5_4_6,
        destreza_ciudadania_5_4_7,
        destreza_ciudadania_5_4_8,
        destreza_ciudadania_5_4_11,
    )

    criterio_ciudadania_5_10.objetivos_generales.add(
        objetivo1,
        objetivo9,
    )
    criterio_ciudadania_5_10.destrezas.add(
        destreza_ciudadania_5_2_8,
        destreza_ciudadania_5_4_9,
        destreza_ciudadania_5_4_10,
    )

    # Filosofía
    criterio_filosofia_5_1.objetivos_generales.add(
        objetivo9,
        objetivo10,
    )
    criterio_filosofia_5_1.destrezas.add(
        destreza_filosofia_5_1_1,
        destreza_filosofia_5_1_2,
        destreza_filosofia_5_1_3,
        destreza_filosofia_5_1_4,
        destreza_filosofia_5_2_12,
        destreza_filosofia_5_3_2,
        destreza_filosofia_5_3_7,
        destreza_filosofia_5_4_5,
    )

    criterio_filosofia_5_2.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo10,
    )
    criterio_filosofia_5_2.destrezas.add(
        destreza_filosofia_5_1_5,
        destreza_filosofia_5_1_6,
        destreza_filosofia_5_1_7,
        destreza_filosofia_5_1_8,
        destreza_filosofia_5_1_9,
        destreza_filosofia_5_1_10,
        destreza_filosofia_5_1_11,
        destreza_filosofia_5_1_12,
        destreza_filosofia_5_3_8,
    )

    criterio_filosofia_5_3.objetivos_generales.add(
        objetivo10,
    )
    criterio_filosofia_5_3.destrezas.add(
        destreza_filosofia_5_2_1,
        destreza_filosofia_5_2_2,
        destreza_filosofia_5_2_10,
        destreza_filosofia_5_2_11,
    )

    criterio_filosofia_5_4.objetivos_generales.add(
        objetivo10,
    )
    criterio_filosofia_5_4.destrezas.add(
        destreza_filosofia_5_2_3,
        destreza_filosofia_5_2_4,
        destreza_filosofia_5_2_5,
        destreza_filosofia_5_2_6,
        destreza_filosofia_5_2_7,
        destreza_filosofia_5_2_8,
        destreza_filosofia_5_2_9,
        destreza_filosofia_5_2_16,
    )

    criterio_filosofia_5_5.objetivos_generales.add(
        objetivo3,
        objetivo8,
        objetivo9,
    )
    criterio_filosofia_5_5.destrezas.add(
        destreza_filosofia_5_2_13,
        destreza_filosofia_5_2_14,
        destreza_filosofia_5_2_15,
        destreza_filosofia_5_2_17,
        destreza_filosofia_5_2_18,
        destreza_filosofia_5_3_1,
        destreza_filosofia_5_3_3,
        destreza_filosofia_5_3_4,
        destreza_filosofia_5_3_5,
        destreza_filosofia_5_3_6,
        destreza_filosofia_5_3_9,
        destreza_filosofia_5_3_10,
    )

    criterio_filosofia_5_6.objetivos_generales.add(
        objetivo10,
    )
    criterio_filosofia_5_6.destrezas.add(
        destreza_filosofia_5_4_1,
        destreza_filosofia_5_4_2,
        destreza_filosofia_5_4_3,
        destreza_filosofia_5_4_4,
        destreza_filosofia_5_4_6,
        destreza_filosofia_5_4_7,
        destreza_filosofia_5_4_8,
        destreza_filosofia_5_4_9,
    )

    criterio_filosofia_5_7.objetivos_generales.add(
        objetivo3,
        objetivo10,
    )
    criterio_filosofia_5_7.destrezas.add(
        destreza_filosofia_5_4_10,
        destreza_filosofia_5_4_11,
        destreza_filosofia_5_4_12,
        destreza_filosofia_5_4_13,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0064_auto_20180908_2011'),
    ]

    operations = [
        migrations.RunPython(create_relationships,
                             reverse_code=migrations.RunPython.noop)
    ]
