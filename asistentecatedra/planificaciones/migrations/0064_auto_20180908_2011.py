from django.db import migrations


def create_relationships(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

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
    criterio_fisica_5_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.1.")
    criterio_fisica_5_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.2.")
    criterio_fisica_5_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.3.")
    criterio_fisica_5_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.4.")
    criterio_fisica_5_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.5.")
    criterio_fisica_5_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.6.")
    criterio_fisica_5_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.7.")
    criterio_fisica_5_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.8.")
    criterio_fisica_5_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.F.5.9.")
    criterio_fisica_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.10.")
    criterio_fisica_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.11.")
    criterio_fisica_5_12 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.12.")
    criterio_fisica_5_13 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.13.")
    criterio_fisica_5_14 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.14.")
    criterio_fisica_5_15 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.15.")
    criterio_fisica_5_16 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.16.")
    criterio_fisica_5_17 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.17.")
    criterio_fisica_5_18 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.18.")
    criterio_fisica_5_19 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.19.")
    criterio_fisica_5_20 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.20.")
    criterio_fisica_5_21 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.21.")
    criterio_fisica_5_22 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.F.5.22.")
    criterio_biologia_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.1.")
    criterio_biologia_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.2.")
    criterio_biologia_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.3.")
    criterio_biologia_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.4.")
    criterio_biologia_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.5.")
    criterio_biologia_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.6.")
    criterio_biologia_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.7.")
    criterio_biologia_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.8.")
    criterio_biologia_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.9.")
    criterio_biologia_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.B.5.10.")
    criterio_quimica_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.1.")
    criterio_quimica_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.2.")
    criterio_quimica_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.3.")
    criterio_quimica_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.4.")
    criterio_quimica_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.5.")
    criterio_quimica_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.6.")
    criterio_quimica_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.7.")
    criterio_quimica_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.8.")
    criterio_quimica_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.9.")
    criterio_quimica_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.10.")
    criterio_quimica_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.11.")
    criterio_quimica_5_12 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.12.")
    criterio_quimica_5_13 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.13.")
    criterio_quimica_5_14 = CriterioEvaluacion.objects.get(
        codigo="CE.CN.Q.5.14.")

    # Destrezas Física
    destreza_fisica_5_1_1 = Destreza.objects.get(codigo="CN.F.5.1.1.")
    destreza_fisica_5_1_2 = Destreza.objects.get(codigo="CN.F.5.1.2.")
    destreza_fisica_5_1_3 = Destreza.objects.get(codigo="CN.F.5.1.3.")
    destreza_fisica_5_1_4 = Destreza.objects.get(codigo="CN.F.5.1.4.")
    destreza_fisica_5_1_5 = Destreza.objects.get(codigo="CN.F.5.1.5.")
    destreza_fisica_5_1_6 = Destreza.objects.get(codigo="CN.F.5.1.6.")
    destreza_fisica_5_1_7 = Destreza.objects.get(codigo="CN.F.5.1.7.")
    destreza_fisica_5_1_8 = Destreza.objects.get(codigo="CN.F.5.1.8.")
    destreza_fisica_5_1_9 = Destreza.objects.get(codigo="CN.F.5.1.9.")
    destreza_fisica_5_1_10 = Destreza.objects.get(codigo="CN.F.5.1.10.")
    destreza_fisica_5_1_11 = Destreza.objects.get(codigo="CN.F.5.1.11.")
    destreza_fisica_5_1_12 = Destreza.objects.get(codigo="CN.F.5.1.12.")
    destreza_fisica_5_1_13 = Destreza.objects.get(codigo="CN.F.5.1.13.")
    destreza_fisica_5_1_14 = Destreza.objects.get(codigo="CN.F.5.1.14.")
    destreza_fisica_5_1_15 = Destreza.objects.get(codigo="CN.F.5.1.15.")
    destreza_fisica_5_1_16 = Destreza.objects.get(codigo="CN.F.5.1.16.")
    destreza_fisica_5_1_17 = Destreza.objects.get(codigo="CN.F.5.1.17.")
    destreza_fisica_5_1_18 = Destreza.objects.get(codigo="CN.F.5.1.18.")
    destreza_fisica_5_1_19 = Destreza.objects.get(codigo="CN.F.5.1.19.")
    destreza_fisica_5_1_20 = Destreza.objects.get(codigo="CN.F.5.1.20.")
    destreza_fisica_5_1_21 = Destreza.objects.get(codigo="CN.F.5.1.21.")
    destreza_fisica_5_1_22 = Destreza.objects.get(codigo="CN.F.5.1.22.")
    destreza_fisica_5_1_23 = Destreza.objects.get(codigo="CN.F.5.1.23.")
    destreza_fisica_5_1_24 = Destreza.objects.get(codigo="CN.F.5.1.24.")
    destreza_fisica_5_1_25 = Destreza.objects.get(codigo="CN.F.5.1.25.")
    destreza_fisica_5_1_26 = Destreza.objects.get(codigo="CN.F.5.1.26.")
    destreza_fisica_5_1_27 = Destreza.objects.get(codigo="CN.F.5.1.27.")
    destreza_fisica_5_1_28 = Destreza.objects.get(codigo="CN.F.5.1.28.")
    destreza_fisica_5_1_29 = Destreza.objects.get(codigo="CN.F.5.1.29.")
    destreza_fisica_5_1_30 = Destreza.objects.get(codigo="CN.F.5.1.30.")
    destreza_fisica_5_1_31 = Destreza.objects.get(codigo="CN.F.5.1.31.")
    destreza_fisica_5_1_32 = Destreza.objects.get(codigo="CN.F.5.1.32.")
    destreza_fisica_5_1_33 = Destreza.objects.get(codigo="CN.F.5.1.33.")
    destreza_fisica_5_1_34 = Destreza.objects.get(codigo="CN.F.5.1.34.")
    destreza_fisica_5_1_35 = Destreza.objects.get(codigo="CN.F.5.1.35.")
    destreza_fisica_5_1_36 = Destreza.objects.get(codigo="CN.F.5.1.36.")
    destreza_fisica_5_1_37 = Destreza.objects.get(codigo="CN.F.5.1.37.")
    destreza_fisica_5_1_38 = Destreza.objects.get(codigo="CN.F.5.1.38.")
    destreza_fisica_5_1_39 = Destreza.objects.get(codigo="CN.F.5.1.39.")
    destreza_fisica_5_1_40 = Destreza.objects.get(codigo="CN.F.5.1.40.")
    destreza_fisica_5_1_41 = Destreza.objects.get(codigo="CN.F.5.1.41.")
    destreza_fisica_5_1_42 = Destreza.objects.get(codigo="CN.F.5.1.42.")
    destreza_fisica_5_1_43 = Destreza.objects.get(codigo="CN.F.5.1.43.")
    destreza_fisica_5_1_44 = Destreza.objects.get(codigo="CN.F.5.1.44.")
    destreza_fisica_5_1_45 = Destreza.objects.get(codigo="CN.F.5.1.45.")
    destreza_fisica_5_1_46 = Destreza.objects.get(codigo="CN.F.5.1.46.")
    destreza_fisica_5_1_47 = Destreza.objects.get(codigo="CN.F.5.1.47.")
    destreza_fisica_5_1_48 = Destreza.objects.get(codigo="CN.F.5.1.48.")
    destreza_fisica_5_1_49 = Destreza.objects.get(codigo="CN.F.5.1.49.")
    destreza_fisica_5_1_50 = Destreza.objects.get(codigo="CN.F.5.1.50.")
    destreza_fisica_5_1_51 = Destreza.objects.get(codigo="CN.F.5.1.51.")
    destreza_fisica_5_1_52 = Destreza.objects.get(codigo="CN.F.5.1.52.")
    destreza_fisica_5_1_53 = Destreza.objects.get(codigo="CN.F.5.1.53.")
    destreza_fisica_5_1_54 = Destreza.objects.get(codigo="CN.F.5.1.54.")
    destreza_fisica_5_1_55 = Destreza.objects.get(codigo="CN.F.5.1.55.")
    destreza_fisica_5_1_56 = Destreza.objects.get(codigo="CN.F.5.1.56.")
    destreza_fisica_5_1_57 = Destreza.objects.get(codigo="CN.F.5.1.57.")
    destreza_fisica_5_2_1 = Destreza.objects.get(codigo="CN.F.5.2.1.")
    destreza_fisica_5_2_2 = Destreza.objects.get(codigo="CN.F.5.2.2.")
    destreza_fisica_5_2_3 = Destreza.objects.get(codigo="CN.F.5.2.3.")
    destreza_fisica_5_2_4 = Destreza.objects.get(codigo="CN.F.5.2.4.")
    destreza_fisica_5_2_5 = Destreza.objects.get(codigo="CN.F.5.2.5.")
    destreza_fisica_5_2_6 = Destreza.objects.get(codigo="CN.F.5.2.6.")
    destreza_fisica_5_2_7 = Destreza.objects.get(codigo="CN.F.5.2.7.")
    destreza_fisica_5_2_8 = Destreza.objects.get(codigo="CN.F.5.2.8.")
    destreza_fisica_5_2_9 = Destreza.objects.get(codigo="CN.F.5.2.9.")
    destreza_fisica_5_2_10 = Destreza.objects.get(codigo="CN.F.5.2.10.")
    destreza_fisica_5_2_11 = Destreza.objects.get(codigo="CN.F.5.2.11.")
    destreza_fisica_5_3_1 = Destreza.objects.get(codigo="CN.F.5.3.1.")
    destreza_fisica_5_3_2 = Destreza.objects.get(codigo="CN.F.5.3.2.")
    destreza_fisica_5_3_3 = Destreza.objects.get(codigo="CN.F.5.3.3.")
    destreza_fisica_5_3_4 = Destreza.objects.get(codigo="CN.F.5.3.4.")
    destreza_fisica_5_3_5 = Destreza.objects.get(codigo="CN.F.5.3.5.")
    destreza_fisica_5_3_6 = Destreza.objects.get(codigo="CN.F.5.3.6.")
    destreza_fisica_5_3_7 = Destreza.objects.get(codigo="CN.F.5.3.7.")
    destreza_fisica_5_3_8 = Destreza.objects.get(codigo="CN.F.5.3.8.")
    destreza_fisica_5_4_1 = Destreza.objects.get(codigo="CN.F.5.4.1.")
    destreza_fisica_5_4_2 = Destreza.objects.get(codigo="CN.F.5.4.2.")
    destreza_fisica_5_4_3 = Destreza.objects.get(codigo="CN.F.5.4.3.")
    destreza_fisica_5_4_4 = Destreza.objects.get(codigo="CN.F.5.4.4.")
    destreza_fisica_5_5_1 = Destreza.objects.get(codigo="CN.F.5.5.1.")
    destreza_fisica_5_5_2 = Destreza.objects.get(codigo="CN.F.5.5.2.")
    destreza_fisica_5_5_3 = Destreza.objects.get(codigo="CN.F.5.5.3.")
    destreza_fisica_5_5_4 = Destreza.objects.get(codigo="CN.F.5.5.4.")
    destreza_fisica_5_5_5 = Destreza.objects.get(codigo="CN.F.5.5.5.")
    destreza_fisica_5_5_6 = Destreza.objects.get(codigo="CN.F.5.5.6.")
    destreza_fisica_5_5_7 = Destreza.objects.get(codigo="CN.F.5.5.7.")
    destreza_fisica_5_5_8 = Destreza.objects.get(codigo="CN.F.5.5.8.")
    destreza_fisica_5_5_9 = Destreza.objects.get(codigo="CN.F.5.5.9.")
    destreza_fisica_5_5_10 = Destreza.objects.get(codigo="CN.F.5.5.10.")
    destreza_fisica_5_5_11 = Destreza.objects.get(codigo="CN.F.5.5.11.")
    destreza_fisica_5_5_12 = Destreza.objects.get(codigo="CN.F.5.5.12.")
    destreza_fisica_5_5_13 = Destreza.objects.get(codigo="CN.F.5.5.13.")
    destreza_fisica_5_5_14 = Destreza.objects.get(codigo="CN.F.5.5.14.")
    destreza_fisica_5_5_15 = Destreza.objects.get(codigo="CN.F.5.5.15.")
    destreza_fisica_5_6_1 = Destreza.objects.get(codigo="CN.F.5.6.1.")
    destreza_fisica_5_6_2 = Destreza.objects.get(codigo="CN.F.5.6.2.")
    destreza_fisica_5_6_3 = Destreza.objects.get(codigo="CN.F.5.6.3.")
    destreza_fisica_5_6_4 = Destreza.objects.get(codigo="CN.F.5.6.4.")
    destreza_fisica_5_6_5 = Destreza.objects.get(codigo="CN.F.5.6.5.")

    # Destrezas Biologia
    destreza_biologia_5_1_1 = Destreza.objects.get(codigo="CN.B.5.1.1.")
    destreza_biologia_5_1_2 = Destreza.objects.get(codigo="CN.B.5.1.2.")
    destreza_biologia_5_1_3 = Destreza.objects.get(codigo="CN.B.5.1.3.")
    destreza_biologia_5_1_4 = Destreza.objects.get(codigo="CN.B.5.1.4.")
    destreza_biologia_5_1_5 = Destreza.objects.get(codigo="CN.B.5.1.5.")
    destreza_biologia_5_1_6 = Destreza.objects.get(codigo="CN.B.5.1.6.")
    destreza_biologia_5_1_7 = Destreza.objects.get(codigo="CN.B.5.1.7.")
    destreza_biologia_5_1_8 = Destreza.objects.get(codigo="CN.B.5.1.8.")
    destreza_biologia_5_1_9 = Destreza.objects.get(codigo="CN.B.5.1.9.")
    destreza_biologia_5_1_10 = Destreza.objects.get(codigo="CN.B.5.1.10.")
    destreza_biologia_5_1_11 = Destreza.objects.get(codigo="CN.B.5.1.11.")
    destreza_biologia_5_1_12 = Destreza.objects.get(codigo="CN.B.5.1.12.")
    destreza_biologia_5_1_13 = Destreza.objects.get(codigo="CN.B.5.1.13.")
    destreza_biologia_5_1_14 = Destreza.objects.get(codigo="CN.B.5.1.14.")
    destreza_biologia_5_1_15 = Destreza.objects.get(codigo="CN.B.5.1.15.")
    destreza_biologia_5_1_16 = Destreza.objects.get(codigo="CN.B.5.1.16.")
    destreza_biologia_5_1_17 = Destreza.objects.get(codigo="CN.B.5.1.17.")
    destreza_biologia_5_1_18 = Destreza.objects.get(codigo="CN.B.5.1.18.")
    destreza_biologia_5_1_19 = Destreza.objects.get(codigo="CN.B.5.1.19.")
    destreza_biologia_5_1_20 = Destreza.objects.get(codigo="CN.B.5.1.20.")
    destreza_biologia_5_1_21 = Destreza.objects.get(codigo="CN.B.5.1.21.")
    destreza_biologia_5_1_22 = Destreza.objects.get(codigo="CN.B.5.1.22.")
    destreza_biologia_5_2_1 = Destreza.objects.get(codigo="CN.B.5.2.1.")
    destreza_biologia_5_2_2 = Destreza.objects.get(codigo="CN.B.5.2.2.")
    destreza_biologia_5_2_3 = Destreza.objects.get(codigo="CN.B.5.2.3.")
    destreza_biologia_5_2_4 = Destreza.objects.get(codigo="CN.B.5.2.4.")
    destreza_biologia_5_2_5 = Destreza.objects.get(codigo="CN.B.5.2.5.")
    destreza_biologia_5_2_6 = Destreza.objects.get(codigo="CN.B.5.2.6.")
    destreza_biologia_5_3_1 = Destreza.objects.get(codigo="CN.B.5.3.1.")
    destreza_biologia_5_3_2 = Destreza.objects.get(codigo="CN.B.5.3.2.")
    destreza_biologia_5_3_3 = Destreza.objects.get(codigo="CN.B.5.3.3.")
    destreza_biologia_5_3_4 = Destreza.objects.get(codigo="CN.B.5.3.4.")
    destreza_biologia_5_3_5 = Destreza.objects.get(codigo="CN.B.5.3.5.")
    destreza_biologia_5_3_6 = Destreza.objects.get(codigo="CN.B.5.3.6.")
    destreza_biologia_5_3_7 = Destreza.objects.get(codigo="CN.B.5.3.7.")
    destreza_biologia_5_3_8 = Destreza.objects.get(codigo="CN.B.5.3.8.")
    destreza_biologia_5_3_9 = Destreza.objects.get(codigo="CN.B.5.3.9.")
    destreza_biologia_5_4_1 = Destreza.objects.get(codigo="CN.B.5.4.1.")
    destreza_biologia_5_4_2 = Destreza.objects.get(codigo="CN.B.5.4.2.")
    destreza_biologia_5_4_3 = Destreza.objects.get(codigo="CN.B.5.4.3.")
    destreza_biologia_5_4_4 = Destreza.objects.get(codigo="CN.B.5.4.4.")
    destreza_biologia_5_4_5 = Destreza.objects.get(codigo="CN.B.5.4.5.")
    destreza_biologia_5_4_6 = Destreza.objects.get(codigo="CN.B.5.4.6.")
    destreza_biologia_5_4_7 = Destreza.objects.get(codigo="CN.B.5.4.7.")
    destreza_biologia_5_4_8 = Destreza.objects.get(codigo="CN.B.5.4.8.")
    destreza_biologia_5_4_9 = Destreza.objects.get(codigo="CN.B.5.4.9.")
    destreza_biologia_5_4_10 = Destreza.objects.get(codigo="CN.B.5.4.10.")
    destreza_biologia_5_4_11 = Destreza.objects.get(codigo="CN.B.5.4.11.")
    destreza_biologia_5_4_12 = Destreza.objects.get(codigo="CN.B.5.4.12.")
    destreza_biologia_5_4_13 = Destreza.objects.get(codigo="CN.B.5.4.13.")
    destreza_biologia_5_4_14 = Destreza.objects.get(codigo="CN.B.5.4.14.")
    destreza_biologia_5_5_1 = Destreza.objects.get(codigo="CN.B.5.5.1.")
    destreza_biologia_5_5_2 = Destreza.objects.get(codigo="CN.B.5.5.2.")
    destreza_biologia_5_5_3 = Destreza.objects.get(codigo="CN.B.5.5.3.")
    destreza_biologia_5_5_4 = Destreza.objects.get(codigo="CN.B.5.5.4.")
    destreza_biologia_5_5_5 = Destreza.objects.get(codigo="CN.B.5.5.5.")
    destreza_biologia_5_5_6 = Destreza.objects.get(codigo="CN.B.5.5.6.")
    destreza_biologia_5_5_7 = Destreza.objects.get(codigo="CN.B.5.5.7.")
    destreza_biologia_5_5_8 = Destreza.objects.get(codigo="CN.B.5.5.8.")
    destreza_biologia_5_5_9 = Destreza.objects.get(codigo="CN.B.5.5.9.")
    destreza_biologia_5_5_10 = Destreza.objects.get(codigo="CN.B.5.5.10.")
    destreza_biologia_5_5_11 = Destreza.objects.get(codigo="CN.B.5.5.11.")

    # Destrezas Química
    destreza_quimica_5_1_1 = Destreza.objects.get(codigo="CN.Q.5.1.1.")
    destreza_quimica_5_1_2 = Destreza.objects.get(codigo="CN.Q.5.1.2.")
    destreza_quimica_5_1_3 = Destreza.objects.get(codigo="CN.Q.5.1.3.")
    destreza_quimica_5_1_4 = Destreza.objects.get(codigo="CN.Q.5.1.4.")
    destreza_quimica_5_1_5 = Destreza.objects.get(codigo="CN.Q.5.1.5.")
    destreza_quimica_5_1_6 = Destreza.objects.get(codigo="CN.Q.5.1.6.")
    destreza_quimica_5_1_7 = Destreza.objects.get(codigo="CN.Q.5.1.7.")
    destreza_quimica_5_1_8 = Destreza.objects.get(codigo="CN.Q.5.1.8.")
    destreza_quimica_5_1_9 = Destreza.objects.get(codigo="CN.Q.5.1.9.")
    destreza_quimica_5_1_10 = Destreza.objects.get(codigo="CN.Q.5.1.10.")
    destreza_quimica_5_1_11 = Destreza.objects.get(codigo="CN.Q.5.1.11.")
    destreza_quimica_5_1_12 = Destreza.objects.get(codigo="CN.Q.5.1.12.")
    destreza_quimica_5_1_13 = Destreza.objects.get(codigo="CN.Q.5.1.13.")
    destreza_quimica_5_1_14 = Destreza.objects.get(codigo="CN.Q.5.1.14.")
    destreza_quimica_5_1_15 = Destreza.objects.get(codigo="CN.Q.5.1.15.")
    destreza_quimica_5_1_16 = Destreza.objects.get(codigo="CN.Q.5.1.16.")
    destreza_quimica_5_1_17 = Destreza.objects.get(codigo="CN.Q.5.1.17.")
    destreza_quimica_5_1_18 = Destreza.objects.get(codigo="CN.Q.5.1.18.")
    destreza_quimica_5_1_19 = Destreza.objects.get(codigo="CN.Q.5.1.19.")
    destreza_quimica_5_1_20 = Destreza.objects.get(codigo="CN.Q.5.1.20.")
    destreza_quimica_5_1_21 = Destreza.objects.get(codigo="CN.Q.5.1.21.")
    destreza_quimica_5_1_22 = Destreza.objects.get(codigo="CN.Q.5.1.22.")
    destreza_quimica_5_1_23 = Destreza.objects.get(codigo="CN.Q.5.1.23.")
    destreza_quimica_5_1_24 = Destreza.objects.get(codigo="CN.Q.5.1.24.")
    destreza_quimica_5_1_25 = Destreza.objects.get(codigo="CN.Q.5.1.25.")
    destreza_quimica_5_1_26 = Destreza.objects.get(codigo="CN.Q.5.1.26.")
    destreza_quimica_5_1_27 = Destreza.objects.get(codigo="CN.Q.5.1.27.")
    destreza_quimica_5_1_28 = Destreza.objects.get(codigo="CN.Q.5.1.28.")
    destreza_quimica_5_1_29 = Destreza.objects.get(codigo="CN.Q.5.1.29.")
    destreza_quimica_5_2_1 = Destreza.objects.get(codigo="CN.Q.5.2.1.")
    destreza_quimica_5_2_2 = Destreza.objects.get(codigo="CN.Q.5.2.2.")
    destreza_quimica_5_2_3 = Destreza.objects.get(codigo="CN.Q.5.2.3.")
    destreza_quimica_5_2_4 = Destreza.objects.get(codigo="CN.Q.5.2.4.")
    destreza_quimica_5_2_5 = Destreza.objects.get(codigo="CN.Q.5.2.5.")
    destreza_quimica_5_2_6 = Destreza.objects.get(codigo="CN.Q.5.2.6.")
    destreza_quimica_5_2_7 = Destreza.objects.get(codigo="CN.Q.5.2.7.")
    destreza_quimica_5_2_8 = Destreza.objects.get(codigo="CN.Q.5.2.8.")
    destreza_quimica_5_2_9 = Destreza.objects.get(codigo="CN.Q.5.2.9.")
    destreza_quimica_5_2_10 = Destreza.objects.get(codigo="CN.Q.5.2.10.")
    destreza_quimica_5_2_11 = Destreza.objects.get(codigo="CN.Q.5.2.11.")
    destreza_quimica_5_2_12 = Destreza.objects.get(codigo="CN.Q.5.2.12.")
    destreza_quimica_5_2_13 = Destreza.objects.get(codigo="CN.Q.5.2.13.")
    destreza_quimica_5_2_14 = Destreza.objects.get(codigo="CN.Q.5.2.14.")
    destreza_quimica_5_2_15 = Destreza.objects.get(codigo="CN.Q.5.2.15.")
    destreza_quimica_5_2_16 = Destreza.objects.get(codigo="CN.Q.5.2.16.")
    destreza_quimica_5_2_17 = Destreza.objects.get(codigo="CN.Q.5.2.17.")
    destreza_quimica_5_3_1 = Destreza.objects.get(codigo="CN.Q.5.3.1.")
    destreza_quimica_5_3_2 = Destreza.objects.get(codigo="CN.Q.5.3.2.")
    destreza_quimica_5_3_3 = Destreza.objects.get(codigo="CN.Q.5.3.3.")
    destreza_quimica_5_3_4 = Destreza.objects.get(codigo="CN.Q.5.3.4.")
    destreza_quimica_5_3_5 = Destreza.objects.get(codigo="CN.Q.5.3.5.")
    destreza_quimica_5_3_6 = Destreza.objects.get(codigo="CN.Q.5.3.6.")
    destreza_quimica_5_3_7 = Destreza.objects.get(codigo="CN.Q.5.3.7.")
    destreza_quimica_5_3_8 = Destreza.objects.get(codigo="CN.Q.5.3.8.")
    destreza_quimica_5_3_9 = Destreza.objects.get(codigo="CN.Q.5.3.9.")
    destreza_quimica_5_3_10 = Destreza.objects.get(codigo="CN.Q.5.3.10.")
    destreza_quimica_5_3_11 = Destreza.objects.get(codigo="CN.Q.5.3.11.")
    destreza_quimica_5_3_12 = Destreza.objects.get(codigo="CN.Q.5.3.12.")
    destreza_quimica_5_3_13 = Destreza.objects.get(codigo="CN.Q.5.3.13.")
    destreza_quimica_5_3_14 = Destreza.objects.get(codigo="CN.Q.5.3.14.")

    # Física
    criterio_fisica_5_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_1.destrezas.add(
        destreza_fisica_5_1_1,
        destreza_fisica_5_1_2,
        destreza_fisica_5_1_3,
        destreza_fisica_5_1_4,
    )

    criterio_fisica_5_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_2.destrezas.add(
        destreza_fisica_5_1_5,
        destreza_fisica_5_1_6,
        destreza_fisica_5_1_7,
        destreza_fisica_5_1_8,
        destreza_fisica_5_1_9,
        destreza_fisica_5_1_10,
        destreza_fisica_5_1_11,
    )

    criterio_fisica_5_3.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_3.destrezas.add(
        destreza_fisica_5_1_12,
        destreza_fisica_5_1_13,
        destreza_fisica_5_1_14,
        destreza_fisica_5_1_15,
    )

    criterio_fisica_5_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_4.destrezas.add(
        destreza_fisica_5_1_16,
        destreza_fisica_5_1_17,
        destreza_fisica_5_1_18,
        destreza_fisica_5_1_19,
        destreza_fisica_5_1_20,
        destreza_fisica_5_1_21,
        destreza_fisica_5_1_22,
        destreza_fisica_5_1_23,
        destreza_fisica_5_1_24,
    )

    criterio_fisica_5_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_5.destrezas.add(
        destreza_fisica_5_1_25,
        destreza_fisica_5_1_26,
        destreza_fisica_5_1_27,
    )

    criterio_fisica_5_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_6.destrezas.add(
        destreza_fisica_5_1_28,
        destreza_fisica_5_1_29,
    )

    criterio_fisica_5_7.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_7.destrezas.add(
        destreza_fisica_5_1_30,
        destreza_fisica_5_1_31,
    )

    criterio_fisica_5_8.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_8.destrezas.add(
        destreza_fisica_5_1_32,
        destreza_fisica_5_1_33,
        destreza_fisica_5_1_34,
        destreza_fisica_5_1_35,
        destreza_fisica_5_1_36,
        destreza_fisica_5_1_37,
    )

    criterio_fisica_5_9.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_9.destrezas.add(
        destreza_fisica_5_1_38,
        destreza_fisica_5_1_39,
        destreza_fisica_5_1_40,
        destreza_fisica_5_1_41,
        destreza_fisica_5_1_42,
    )

    criterio_fisica_5_10.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_10.destrezas.add(
        destreza_fisica_5_1_43,
        destreza_fisica_5_1_44,
        destreza_fisica_5_1_45,
        destreza_fisica_5_1_46,
        destreza_fisica_5_1_47,
    )

    criterio_fisica_5_11.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_11.destrezas.add(
        destreza_fisica_5_1_48,
        destreza_fisica_5_1_49,
        destreza_fisica_5_1_50,
        destreza_fisica_5_1_51,
    )

    criterio_fisica_5_12.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_12.destrezas.add(
        destreza_fisica_5_1_52,
        destreza_fisica_5_1_53,
        destreza_fisica_5_1_54,
        destreza_fisica_5_1_55,
        destreza_fisica_5_1_56,
        destreza_fisica_5_1_57,
    )

    criterio_fisica_5_13.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_13.destrezas.add(
        destreza_fisica_5_2_1,
        destreza_fisica_5_2_2,
        destreza_fisica_5_2_3,
        destreza_fisica_5_2_4,
    )

    criterio_fisica_5_14.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_14.destrezas.add(
        destreza_fisica_5_2_5,
        destreza_fisica_5_2_6,
        destreza_fisica_5_2_7,
        destreza_fisica_5_2_8,
        destreza_fisica_5_2_9,
        destreza_fisica_5_2_10,
        destreza_fisica_5_2_11,
    )

    criterio_fisica_5_15.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_15.destrezas.add(
        destreza_fisica_5_3_1,
        destreza_fisica_5_3_2,
        destreza_fisica_5_3_3,
        destreza_fisica_5_3_4,
        destreza_fisica_5_3_5,
        destreza_fisica_5_3_6,
        destreza_fisica_5_6_1,
    )

    criterio_fisica_5_16.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_16.destrezas.add(
        destreza_fisica_5_3_7,
        destreza_fisica_5_3_8,
        destreza_fisica_5_6_2,
    )

    criterio_fisica_5_17.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_17.destrezas.add(
        destreza_fisica_5_4_1,
        destreza_fisica_5_4_2,
        destreza_fisica_5_6_3,
    )

    criterio_fisica_5_18.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_18.destrezas.add(
        destreza_fisica_5_4_3,
        destreza_fisica_5_4_4,
    )

    criterio_fisica_5_19.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_19.destrezas.add(
        destreza_fisica_5_5_1,
        destreza_fisica_5_5_2,
        destreza_fisica_5_5_3,
        destreza_fisica_5_5_4,
        destreza_fisica_5_5_5,
        destreza_fisica_5_6_4,
    )

    criterio_fisica_5_20.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_20.destrezas.add(
        destreza_fisica_5_5_6,
        destreza_fisica_5_5_7,
        destreza_fisica_5_5_8,
        destreza_fisica_5_6_5,
    )

    criterio_fisica_5_21.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_21.destrezas.add(
        destreza_fisica_5_5_9,
        destreza_fisica_5_5_10,
        destreza_fisica_5_5_11,
        destreza_fisica_5_5_12,
        destreza_fisica_5_5_13,
    )

    criterio_fisica_5_21.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_fisica_5_22.destrezas.add(
        destreza_fisica_5_5_14,
        destreza_fisica_5_5_15,
    )

    # Biología
    criterio_biologia_5_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo5,
        objetivo7,
    )
    criterio_biologia_5_1.destrezas.add(
        destreza_biologia_5_1_1,
        destreza_biologia_5_1_2,
        destreza_biologia_5_1_3,
        destreza_biologia_5_1_4,
        destreza_biologia_5_1_5,
        destreza_biologia_5_5_1,
    )

    criterio_biologia_5_2.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo8,
        objetivo9,
    )
    criterio_biologia_5_2.destrezas.add(
        destreza_biologia_5_1_6,
        destreza_biologia_5_1_7,
        destreza_biologia_5_1_8,
        destreza_biologia_5_1_9,
        destreza_biologia_5_1_10,
        destreza_biologia_5_1_18,
        destreza_biologia_5_2_1,
        destreza_biologia_5_5_2,
    )

    criterio_biologia_5_3.objetivos_generales.add(
        objetivo2,
        objetivo5,
        objetivo6,
        objetivo7,
    )
    criterio_biologia_5_3.destrezas.add(
        destreza_biologia_5_1_11,
        destreza_biologia_5_1_12,
        destreza_biologia_5_1_17,
    )

    criterio_biologia_5_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo9,
    )
    criterio_biologia_5_4.destrezas.add(
        destreza_biologia_5_1_13,
        destreza_biologia_5_1_14,
        destreza_biologia_5_1_15,
        destreza_biologia_5_1_16,
        destreza_biologia_5_5_3,
        destreza_biologia_5_5_5,
        destreza_biologia_5_5_6,
    )

    criterio_biologia_5_5.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo5,
        objetivo6,
    )
    criterio_biologia_5_5.destrezas.add(
        destreza_biologia_5_1_19,
        destreza_biologia_5_1_20,
        destreza_biologia_5_1_21,
        destreza_biologia_5_1_22,
        destreza_biologia_5_5_10,
        destreza_biologia_5_5_11,
    )

    criterio_biologia_5_6.objetivos_generales.add(
        objetivo2,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo10,
    )
    criterio_biologia_5_6.destrezas.add(
        destreza_biologia_5_2_2,
        destreza_biologia_5_2_3,
        destreza_biologia_5_2_4,
        destreza_biologia_5_2_5,
        destreza_biologia_5_2_6,
        destreza_biologia_5_5_7,
        destreza_biologia_5_5_8,
    )

    criterio_biologia_5_7.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo7,
    )
    criterio_biologia_5_7.destrezas.add(
        destreza_biologia_5_3_1,
        destreza_biologia_5_3_2,
        destreza_biologia_5_3_3,
        destreza_biologia_5_3_4,
        destreza_biologia_5_3_5,
        destreza_biologia_5_3_6,
        destreza_biologia_5_4_1,
        destreza_biologia_5_4_5,
        destreza_biologia_5_4_7,
        destreza_biologia_5_4_8,
        destreza_biologia_5_4_11,
    )

    criterio_biologia_5_8.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
        objetivo8,
        objetivo9,
        objetivo10,
    )
    criterio_biologia_5_8.destrezas.add(
        destreza_biologia_5_4_2,
        destreza_biologia_5_4_3,
        destreza_biologia_5_4_4,
        destreza_biologia_5_4_6,
        destreza_biologia_5_4_9,
        destreza_biologia_5_4_10,
        destreza_biologia_5_5_4,
        destreza_biologia_5_5_9,
    )

    criterio_biologia_5_9.objetivos_generales.add(
        objetivo2,
        objetivo5,
    )
    criterio_biologia_5_9.destrezas.add(
        destreza_biologia_5_3_7,
        destreza_biologia_5_3_8,
        destreza_biologia_5_3_9,
    )

    criterio_biologia_5_10.objetivos_generales.add(
        objetivo2,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo7,
    )
    criterio_biologia_5_10.destrezas.add(
        destreza_biologia_5_4_12,
        destreza_biologia_5_4_13,
        destreza_biologia_5_4_14,
    )

    # Quimica
    criterio_quimica_5_1.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo7,
        objetivo8,
        objetivo9,
    )
    criterio_quimica_5_1.destrezas.add(
        destreza_quimica_5_1_1,
        destreza_quimica_5_1_2,
    )

    criterio_quimica_5_2.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_2.destrezas.add(
        destreza_quimica_5_1_3,
        destreza_quimica_5_1_4,
        destreza_quimica_5_1_5,
    )

    criterio_quimica_5_3.objetivos_generales.add(
        objetivo1,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_3.destrezas.add(
        destreza_quimica_5_1_6,
        destreza_quimica_5_1_7,
    )

    criterio_quimica_5_4.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_4.destrezas.add(
        destreza_quimica_5_1_8,
        destreza_quimica_5_1_9,
        destreza_quimica_5_1_10,
        destreza_quimica_5_1_11,
    )

    criterio_quimica_5_5.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_5.destrezas.add(
        destreza_quimica_5_1_12,
        destreza_quimica_5_2_1,
        destreza_quimica_5_2_2,
        destreza_quimica_5_2_3,
        destreza_quimica_5_2_4,
        destreza_quimica_5_2_5,
        destreza_quimica_5_2_6,
        destreza_quimica_5_2_7,
    )

    criterio_quimica_5_6.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_6.destrezas.add(
        destreza_quimica_5_1_13,
        destreza_quimica_5_1_14,
        destreza_quimica_5_1_24,
        destreza_quimica_5_1_25,
        destreza_quimica_5_1_26,
        destreza_quimica_5_1_27,
        destreza_quimica_5_1_28,
        destreza_quimica_5_1_29,
        destreza_quimica_5_2_8,
        destreza_quimica_5_2_13,
    )

    criterio_quimica_5_7.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo5,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_7.destrezas.add(
        destreza_quimica_5_1_15,
        destreza_quimica_5_1_16,
        destreza_quimica_5_1_17,
    )

    criterio_quimica_5_8.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_8.destrezas.add(
        destreza_quimica_5_1_18,
        destreza_quimica_5_1_19,
        destreza_quimica_5_1_20,
        destreza_quimica_5_1_21,
    )

    criterio_quimica_5_9.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_9.destrezas.add(
        destreza_quimica_5_1_22,
        destreza_quimica_5_1_23,
        destreza_quimica_5_2_14,
        destreza_quimica_5_2_15,
        destreza_quimica_5_2_16,
        destreza_quimica_5_2_17,
    )

    criterio_quimica_5_10.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_10.destrezas.add(
        destreza_quimica_5_2_9,
        destreza_quimica_5_2_10,
        destreza_quimica_5_2_11,
        destreza_quimica_5_2_12,
    )

    criterio_quimica_5_11.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo5,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_11.destrezas.add(
        destreza_quimica_5_3_1,
        destreza_quimica_5_3_2,
    )

    criterio_quimica_5_12.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_12.destrezas.add(
        destreza_quimica_5_3_3,
        destreza_quimica_5_3_4,
        destreza_quimica_5_3_5,
        destreza_quimica_5_3_6,
    )

    criterio_quimica_5_13.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo3,
        objetivo4,
        objetivo6,
        objetivo9,
        objetivo10,
    )
    criterio_quimica_5_13.destrezas.add(
        destreza_quimica_5_3_7,
        destreza_quimica_5_3_8,
        destreza_quimica_5_3_9,
        destreza_quimica_5_3_10,
        destreza_quimica_5_3_11,
    )

    criterio_quimica_5_14.objetivos_generales.add(
        objetivo1,
        objetivo2,
        objetivo4,
    )
    criterio_quimica_5_14.destrezas.add(
        destreza_quimica_5_3_12,
        destreza_quimica_5_3_13,
        destreza_quimica_5_3_14,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0063_auto_20180908_2009'),
    ]

    operations = [
        migrations.RunPython(create_relationships)
    ]
