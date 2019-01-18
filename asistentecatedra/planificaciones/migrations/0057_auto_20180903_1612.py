from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

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
    criterio_gestion_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.1.")
    criterio_gestion_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.2.")
    criterio_gestion_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.3.")
    criterio_gestion_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.4.")
    criterio_gestion_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.5.")
    criterio_gestion_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.6.")
    criterio_gestion_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.7.")
    criterio_gestion_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.8.")
    criterio_gestion_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.9.")
    criterio_gestion_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.10.")
    criterio_gestion_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.11.")

    Indicador.objects.bulk_create([
        # Inglés
        # Preparatoria
        Indicador(
            description=(
                "Learners can understand familiar words, and simple "
                "instructions about their own surroundings (I.3)"
            ),
            codigo="I.EFL.1.1.1.",
            criterio_evaluacion=criterio_ingles_1_1
        ),
        Indicador(
            description=(
                "Learners can recognize and follow simple instructions in "
                "order to act upon them. (J.3.,I.3.,I.4.)"
            ),
            codigo="I.EFL.1.2.1.",
            criterio_evaluacion=criterio_ingles_1_2
        ),
        # Elemental
        Indicador(
            description=(
                "Learners can recognize differences between where people "
                "live and write or talk about their own surroundings, as "
                "well as ask questions about how other people live. (I.2, "
                "S.2)"
            ),
            codigo="I.EFL.2.1.1.",
            criterio_evaluacion=criterio_ingles_2_1
        ),
        Indicador(
            description=(
                "Learners can classify everyday objects and familiar places. "
                "Learners can compare objects from different cultural "
                "contexts. Learners can say and recognize ways to take care "
                "of the"
                "environment and one’s surroundings. (J.3, S.1)"
            ),
            codigo="I.EFL.2.2.1.",
            criterio_evaluacion=criterio_ingles_2_2
        ),
        Indicador(
            description=(
                "Learners can use basic personal information and expressions "
                "of politeness in short dialogues or conversations. (J.2, "
                "J.3)"
            ),
            codigo="I.EFL.2.3.1.",
            criterio_evaluacion=criterio_ingles_2_3
        ),
        Indicador(
            description=(
                "Learners can select pictures and/or short phrases that "
                "relate to collaborating and sharing and express personal "
                "preferences. (J.2, J.3, S.4)"
            ),
            codigo="I.EFL.2.4.1.",
            criterio_evaluacion=criterio_ingles_2_4
        ),
        Indicador(
            description=(
                "Learners can apply turn-taking and ways to express to "
                "others when something is not understood in short "
                "conversations. (J.3, S.1, S.4)"
            ),
            codigo="I.EFL.2.5.1.",
            criterio_evaluacion=criterio_ingles_2_5
        ),
        Indicador(
            description=(
                "Learners can understand the main ideas in short simple "
                "spoken texts and infer who is speaking and what the "
                "situation is, without decoding every word. (I.3)"
            ),
            codigo="I.EFL.2.6.1.",
            criterio_evaluacion=criterio_ingles_2_6
        ),
        Indicador(
            description=(
                "Learners can understand short and simple spoken texts well "
                "enough to be able to pick out key items of information and "
                "record them in writing or drawings, or physically act upon "
                "them. (I.3)"
            ),
            codigo="I.EFL.2.7.1.",
            criterio_evaluacion=criterio_ingles_2_7
        ),
        Indicador(
            description=(
                "Learners can pronounce most familiar vocabulary items "
                "accurately, and can therefore usually be easily understood. "
                "They can also produce some phrases and short sentences "
                "clearly, and may approximate English rhythm and intonation "
                "in longer utterances. (I.3)"
            ),
            codigo="I.EFL.2.8.1.",
            criterio_evaluacion=criterio_ingles_2_8
        ),
        Indicador(
            description=(
                "Learners can express basic ideas, initiate conversations, "
                "and respond to simple questions using appropriate words, "
                "phrases, and short sentences. Responses may be slow though "
                "pauses do not make the interaction tedious or uncomfortable "
                "for participants. (I.3)"
            ),
            codigo="I.EFL.2.9.1.",
            criterio_evaluacion=criterio_ingles_2_9
        ),
        Indicador(
            description=(
                "Learners can interact effectively using a range of basic "
                "functional exponents for interpersonal conversations in "
                "everyday contexts, providing speech is slow and clear. "
                "Learners can request repetition or clarification, and can "
                "react appropriately to responses received. (I.3)"
            ),
            codigo="I.EFL.2.10.1.",
            criterio_evaluacion=criterio_ingles_2_10
        ),
        Indicador(
            description=(
                "Learners can understand familiar words, phrases, and short "
                "simple sentences and can successfully complete the simple "
                "accompanying task. (I.4)"
            ),
            codigo="I.EFL.2.11.1.",
            criterio_evaluacion=criterio_ingles_2_11
        ),
        Indicador(
            description=(
                "Learners can understand a short simple text on an everyday "
                "topic and successfully complete a simple task to show that "
                "they have understood most or some of it. (I.4)"
            ),
            codigo="I.EFL.2.12.1.",
            criterio_evaluacion=criterio_ingles_2_12
        ),
        Indicador(
            description=(
                "Learners can understand a short simple environmental print "
                "text type and successfully complete a simple task. "
                "(Example: a sign, notice, menu, etc.)(I.3)"
            ),
            codigo="I.EFL.2.13.1.",
            criterio_evaluacion=criterio_ingles_2_13
        ),
        Indicador(
            description=(
                "Learners can successfully use simple online and print "
                "learning resources. (Example: flashcards, picture "
                "dictionaries, word lists, etc.) (I.2)"
            ),
            codigo="I.EFL.2.14.1.",
            criterio_evaluacion=criterio_ingles_2_14
        ),
        Indicador(
            description=(
                "Learners can use simple graphic organizers to show that "
                "they can understand a short simple text. (Example: maps, "
                "diagrams, bar charts, Venn diagrams, etc.) (I.4)"
            ),
            codigo="I.EFL.2.15.1.",
            criterio_evaluacion=criterio_ingles_2_15
        ),
        Indicador(
            description=(
                "Learners can understand the main ideas and some basic "
                "details"
                "from a short simple cross-curricular* text and successfully "
                "complete a simple task, as well as acquire subject-specific "
                "lexis. (I.2)"
            ),
            codigo="I.EFL.2.16.1.",
            criterio_evaluacion=criterio_ingles_2_16
        ),
        Indicador(
            description=(
                "Learners can write words, phrases, and short simple "
                "sentences using the correct conventions (spelling, "
                "punctuation, capitalization, and handwriting or typography, "
                "etc.), for making simple learning resources. (I.3)"
            ),
            codigo="I.EFL.2.17.1.",
            criterio_evaluacion=criterio_ingles_2_17
        ),
        Indicador(
            description=(
                "Learners can write short simple phrases and sentences to "
                "show that they know how to use simple grammar or vocabulary "
                "items. (I.3, I.4)"
            ),
            codigo="I.EFL.2.18.1.",
            criterio_evaluacion=criterio_ingles_2_18
        ),
        Indicador(
            description=(
                "Learners can produce a short simple sentence and a "
                "paragraph – with ample support - on a variety of topics, "
                "and some learners can do so with only limited support. "
                "(I.3)"
            ),
            codigo="I.EFL.2.19.1.",
            criterio_evaluacion=criterio_ingles_2_19
        ),
        Indicador(
            description=(
                "Learners can write information in a simple survey form or "
                "questionnaire, and can type or write some simple digital "
                "text-types, such as a URL and an email address. (I.3)"
            ),
            codigo="I.EFL.2.20.1.",
            criterio_evaluacion=criterio_ingles_2_20
        ),
        Indicador(
            description=(
                "Learners can recognize, through pictures or other media "
                "such as ICT, key aspects of a story or literary text (both "
                "oral and written). (J.1, I.2)"
            ),
            codigo="I.EFL.2.21.1.",
            criterio_evaluacion=criterio_ingles_2_21
        ),
        Indicador(
            description=(
                "Learners can report emotions and compose short responses to "
                "literary texts through words and images, or other media "
                "(video, audio). Learners can generate and expand on "
                "personal opinions and responses to oral and written texts "
                "through TPR, playground games, and songs. (I.3, S.3)"
            ),
            codigo="I.EFL.2.22.1.",
            criterio_evaluacion=criterio_ingles_2_22
        ),
        Indicador(
            description=(
                "Learners can demonstrate an affinity for a variety of "
                "literary texts by responding within a range of physical, "
                "cognitive, and attitudinal manners and adapt elements of a "
                "literary text to create a new text. (I.1, I.4)"
            ),
            codigo="I.EFL.2.23.1.",
            criterio_evaluacion=criterio_ingles_2_23
        ),
        Indicador(
            description=(
                "Learners can communicate thoughts, feelings, and/or "
                "personal experiences and create short original texts "
                "through a range of resources and other media, including "
                "ICT. (I.2, I.3, I.4)"
            ),
            codigo="I.EFL.2.24.1.",
            criterio_evaluacion=criterio_ingles_2_24
        ),
        Indicador(
            description=(
                "Learners can utilize a range of creative thinking skills to "
                "show a respect for sharing and accepting different ideas "
                "while working in pairs and through brainstorms.(J.3, S.4)"
            ),
            codigo="I.EFL.2.25.1.",
            criterio_evaluacion=criterio_ingles_2_25
        ),
        # Emprendimiento y gestión
        Indicador(
            description=(
                "Determina proyecciones financieras y el capital de trabajo "
                "de un emprendimiento basándose en conceptos financieros "
                "básicos. (I.1., I.4.)"
            ),
            codigo="I.EG.5.1.1.",
            criterio_evaluacion=criterio_gestion_5_1
        ),
        Indicador(
            description=(
                "Ordena las cuentas contables de acuerdo con la naturaleza "
                "de la función de los asientos contables en aquellos "
                "emprendimientos obligados a llevar contabilidad, tomando en "
                "cuenta las normas tributarias establecidas por la autoridad "
                "competente. (I.4., J.2.)"
            ),
            codigo="I.EG.5.2.1.",
            criterio_evaluacion=criterio_gestion_5_2
        ),
        Indicador(
            description=(
                "Registra transacciones en las cuentas contables bajo el "
                "principio de partida doble, según la normativa contable "
                "vigente. (J.2., I.4.)"
            ),
            codigo="I.EG.5.2.2.",
            criterio_evaluacion=criterio_gestion_5_2
        ),
        Indicador(
            description=(
                "Construye estados financieros (balance general y estado de "
                "pérdidas y ganancias) aplicando técnicas contables y la "
                "normativa vigente. (I.4., J.3.)"
            ),
            codigo="I.EG.5.2.3.",
            criterio_evaluacion=criterio_gestion_5_2
        ),
        Indicador(
            description=(
                "Comprende la importancia de generar una cultura tanto "
                "tributaria como de responsabilidad legal en cualquier "
                "emprendimiento, para validar sus operaciones en el mercado. "
                "(S.1., I.1.)"
            ),
            codigo="I.EG.5.3.1.",
            criterio_evaluacion=criterio_gestion_5_3
        ),
        Indicador(
            description=(
                "Determina, en una zona geográfica, la necesidad de un "
                "determinado bien o servicio para convertirla en su cliente "
                "frecuente. (S.4., S.1.)"
            ),
            codigo="I.EG.5.4.1.",
            criterio_evaluacion=criterio_gestion_5_4
        ),
        Indicador(
            description=(
                "Ejecuta investigaciones de campo y diseña instrumentos de "
                "investigación para seleccionar las ideas de emprendimiento "
                "que presenten mayor factibilidad en el mercado. (I.1., "
                "S.2.)"
            ),
            codigo="I.EG.5.4.2.",
            criterio_evaluacion=criterio_gestion_5_4
        ),
        Indicador(
            description=(
                "Presenta la información de mercado (oferta y demanda) a "
                "través de la representación gráfica de los datos "
                "procesados, en tablas, gráficas, histogramas, cálculo de "
                "frecuencias, diagramas, y estudios de medidas de tendencia "
                "central (media, mediana, moda), así como la información "
                "obtenida en la investigación de campo de forma resumida y "
                "concisa, de tal manera que se facilite la toma de "
                "decisiones. (I.2., I.4.)"
            ),
            codigo="I.EG.5.5.1.",
            criterio_evaluacion=criterio_gestion_5_5
        ),
        Indicador(
            description=(
                "Valora, de acuerdo con un criterio administrativo, la "
                "responsabilidad social en la planificación de los recursos "
                "humanos (estructura organizacional, proceso de "
                "contratación, capacitación, deberes y derechos laborales, "
                "despido) y diagrama una estructura organizacional óptima "
                "para un emprendimiento. (I.4, S.3.)"
            ),
            codigo="I.EG.5.6.1.",
            criterio_evaluacion=criterio_gestion_5_6
        ),
        Indicador(
            description=(
                "Comprueba la rentabilidad de un emprendimiento a partir del "
                "análisis de indicadores económicos (inflación, oferta, "
                "demanda, mercado, empleo, etc.), para favorecer la toma de "
                "decisiones. (I.2., I.1.)"
            ),
            codigo="I.EG.5.7.1.",
            criterio_evaluacion=criterio_gestion_5_7
        ),
        Indicador(
            description=(
                "Analiza la rentabilidad de un emprendimiento a partir de "
                "sus costos marginales (costos hundidos). (I.2., S.3.)"
            ),
            codigo="I.EG.5.7.2.",
            criterio_evaluacion=criterio_gestion_5_7
        ),
        Indicador(
            description=(
                "Realiza una mezcla adecuada de las variables de mercado "
                "(producto, precio, plaza, promoción y personalización) para "
                "un bien o servicio nuevo que presenta a un segmento de "
                "mercado específico mediante mecanismos de comunicación "
                "eficaces. (I.3., S.1.)"
            ),
            codigo="I.EG.5.8.1.",
            criterio_evaluacion=criterio_gestion_5_8
        ),
        Indicador(
            description=(
                "Especifica detalladamente las actividades de la "
                "planificación de producción (recursos humanos y materiales) "
                "para que un emprendimiento sea de calidad y productivo. "
                "(I.1., S.1.)"
            ),
            codigo="I.EG.5.9.1.",
            criterio_evaluacion=criterio_gestion_5_9
        ),
        Indicador(
            description=(
                "Determina la cantidad de bienes o servicios que se debe "
                "producir debido a la proporción de los costos de producción "
                "(c ostos fijos, variables, directos e indirectos) y los "
                "gastos incurridos, para que el emprendimiento sea "
                "productivo. (I.1., S.1.)"
            ),
            codigo="I.EG.5.9.2.",
            criterio_evaluacion=criterio_gestion_5_9
        ),
        Indicador(
            description=(
                "Aplica las TIC para proyectar costos y gastos, calcular el "
                "punto de equilibrio del emprendimiento y el margen de "
                "contribución del producto o servicio ofertado. (I.3.,I.1.)"
            ),
            codigo="I.EG.5.10.1.",
            criterio_evaluacion=criterio_gestion_5_10
        ),
        Indicador(
            description=(
                "Aplica las TIC en proyecciones de efectivo con experiencia "
                "en incrementos paulatinos y ciclicidad del mercado "
                "(considerando las unidades vendidas y los precios de "
                "venta), para establecer el monto de ingresos futuros del "
                "emprendimiento. (I.3., I.2.)"
            ),
            codigo="I.EG.5.10.2.",
            criterio_evaluacion=criterio_gestion_5_10
        ),
        Indicador(
            description=(
                "Elige el proyecto de emprendimiento con menor riesgo "
                "financiero después de analizar la rentabilidad, periodo de "
                "recuperación, tasa interna de retorno y valor actual neto. "
                "(I.1., I.2.)"
            ),
            codigo="I.EG.5.11.1.",
            criterio_evaluacion=criterio_gestion_5_11
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0056_auto_20180903_1534'),
    ]

    operations = [
        migrations.RunPython(create_indicadores)
    ]
