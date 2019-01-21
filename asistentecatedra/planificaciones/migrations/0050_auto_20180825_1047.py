from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

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

    Indicador.objects.bulk_create([
        # Preparatoria
        Indicador(
            description=(
                "Ajusta sus acciones motrices en función de sus estados "
                "corporales, ritmos internos y objetivos de los juegos. "
                "(S.3.)"
            ),
            codigo="I.EF.1.1.1.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Comprende la necesidad de respetar reglas, roles y acuerdos "
                "simples para el cuidado de sí mismo, sus pares y el "
                "ambiente de aprendizaje antes, durante y después de su "
                "participación en diferentes juegos. (J.3., I.4.)"
            ),
            codigo="I.EF.1.1.2.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Identifica lógicas de los juegos, las habilidades motrices "
                "básicas que se requieren, los objetivos que hay que lograr "
                "y los materiales necesarios para la construcción de "
                "implementos. (I.2., S.3.)"
            ),
            codigo="I.EF.1.1.3.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Experimenta las mejores maneras de practicar habilidades "
                "motrices básicas, destrezas y acrobacias a partir de "
                "identificar los factores que favorecen u obstaculizan la "
                "práctica. (J.4., S.3.)"
            ),
            codigo="I.EF.1.2.1.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Realiza acuerdos necesarios para el cuidado de sí mismo, de "
                "sus pares y el ambiente de aprendizaje. (J.3., S.4.)"
            ),
            codigo="I.EF.1.2.2.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Construye y comunica mensajes (convencionales y/o "
                "espontáneos) utilizando diferentes recursos expresivos "
                "(gestos, ritmos, posturas, tipos de movimiento en el tiempo "
                "y el espacio, otros). (I.3.)"
            ),
            codigo="I.EF.1.3.1.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Reconoce sus ritmos internos, sus estados corporales y de "
                "ánimo, sus posibilidades de interpretación y traducción de "
                "mensajes corporales propios y de pares a otros lenguajes. "
                "(I.3.)"
            ),
            codigo="I.EF.1.3.2.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Establece acuerdos colectivos que favorezcan la "
                "participación y el cuidado de sí mismo, sus pares y el "
                "ambiente de aprendizaje, en diferentes prácticas corporales "
                "expresivo-comunicativas.(J.3., S.4.)"
            ),
            codigo="I.EF.1.3.3.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales, reconociendo "
                "sus estados corporales en reposo y durante la acción y las "
                "asocia a sus modos de participación en las mismas. (J.4., "
                "S.3.)"
            ),
            codigo="I.EF.1.4.1.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales, reconociendo "
                "su ubicación en el tiempo y el espacio de manera estática y "
                "dinámica, las características y posibilidades de movimiento "
                "de sus partes y segmentos corporales. (I.4.)"
            ),
            codigo="I.EF.1.4.2.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Reconoce la necesidad de utilizar los cuidados básicos de "
                "higiene personal y del ambiente durante su participación en "
                "prácticas corporales. (J.3., I.2)"
            ),
            codigo="I.EF.1.5.1.",
            criterio_evaluacion=criterio1_5
        ),
        # Elemental
        Indicador(
            description=(
                "Participa con pares en diferentes juegos propios de la "
                "región, identificando características, objetivos, roles de "
                "los jugadores, demandas y construyendo los implementos "
                "necesarios. (S.2., I.2.)"
            ),
            codigo="I.EF.2.1.1.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Mejora su desempeño de modo seguro en juegos propios de la "
                "región, construyendo con sus pares modos "
                "cooperativos/colaborativos, posibilidades de participación, "
                "de acuerdo a las necesidades del grupo. (J.3., S.4.)"
            ),
            codigo="I.EF.2.1.2.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Acuerda pautas de trabajo para participar de manera segura, "
                "reconociendo posibles riesgos que presentan los juegos en "
                "diferentes ambientes. (J.3., S.4.)"
            ),
            codigo="I.EF.2.2.1.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Participa en diferentes juegos colectivos, reconociendo las "
                "características, objetivos, demandas y la necesidad de "
                "cooperar con pares y tomar las precauciones necesarias "
                "antes y durante su participación. (J.3., S.4.)"
            ),
            codigo="I.EF.2.2.2.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Realiza diferentes acrobacias, destrezas y/o habilidades "
                "motrices básicas, percibiendo las posiciones de su cuerpo "
                "en el tiempo y el espacio e identificando las acciones que "
                "debe mejorar de modo seguro. (J.4., S.3.)"
            ),
            codigo="I.EF.2.3.1.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Construye con pares acuerdos de seguridad, identificando "
                "posibles riesgos antes y durante la realización de "
                "combinaciones, de acrobacias, destrezas y/o habilidades "
                "motrices básicas, en el marco de una práctica gimnástica "
                "segura, basada en su disposición y en la construcción de "
                "confianza entre pares (I.4., J.2.)"
            ),
            codigo="I.EF.2.3.2.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Reconoce y percibe durante la realización de posiciones "
                "invertidas, destrezas y acrobacias la alineación de sus "
                "articulaciones, las posiciones, apoyos, tomas, agarres y "
                "posturas adecuadas, contracciones, relajaciones y contactos "
                "del cuerpo involucrados en la práctica segura de las "
                "mismas. (J.4., S.3.)"
            ),
            codigo="I.EF.2.4.1.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Utiliza diferentes recursos expresivos durante su "
                "participación en prácticas corporales "
                "expresivo-comunicativas, ajustando rítmicamente las "
                "posibilidades expresivas de sus movimientos en el espacio y "
                "el tiempo. (I.3., S.1.)"
            ),
            codigo="I.EF.2.5.1.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Construye colectivamente composiciones "
                "expresivo-comunicativas en un ambiente de confianza y "
                "seguridad. (S.4., I.1.)"
            ),
            codigo="I.EF.2.5.2.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales "
                "expresivo-comunicativas, reconociendo el valor cultural "
                "otorgado a las mismas por el propio contexto. (J.1., S.2.)"
            ),
            codigo="I.EF.2.6.1.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Construye con pares diferentes posibilidades de "
                "participación en prácticas corporales "
                "expresivo-comunicativas propias de la región. (J.1., S.2.)"
            ),
            codigo="I.EF.2.6.2.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Percibe sus músculos, articulaciones (formas y "
                "posibilidades de movimiento), ritmos, estados corporales y "
                "las diferentes posiciones que adopta su cuerpo en el tiempo "
                "y el espacio, durante su participación en diferentes "
                "prácticas corporales. (S.3.)"
            ),
            codigo="I.EF.2.7.1.",
            criterio_evaluacion=criterio2_7
        ),
        Indicador(
            description=(
                "Regula sus acciones motrices en función de sus ritmos y "
                "estados corporales, mejorando su participación en relación "
                "con los objetivos y las características de las prácticas "
                "corporales que realiza. (J.4., I.4.)"
            ),
            codigo="I.EF.2.7.2.",
            criterio_evaluacion=criterio2_7
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales colectivas, "
                "comunicando sus condiciones y disposiciones y valorando la "
                "de sus compañeros y compañeras en la construcción de "
                "posibilidades de participación. (I.3., S.4.)"
            ),
            codigo="I.EF.2.8.1.",
            criterio_evaluacion=criterio2_8
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales de forma "
                "segura reconociendo posturas favorables, adecuadas y menos "
                "lesivas en función de las características del propio cuerpo "
                "y las maneras saludables y beneficiosas de realizarlas. "
                "(J.3., S.3.)"
            ),
            codigo="I.EF.2.9.1.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Identifica riesgos, acordando los cuidados necesarios para "
                "sí, para las demás personas y el entorno, en el desarrollo "
                "de prácticas corporales. (S.1., J.3., I.1.)"
            ),
            codigo="I.EF.2.9.2.",
            criterio_evaluacion=criterio2_9
        ),
        # Media
        Indicador(
            description=(
                "Participa en juegos creados y de otras regiones de manera "
                "colectiva, segura y democrática, reconociéndolos como "
                "producciones culturales con influencia en su identidad "
                "corporal. (J.1.)"
            ),
            codigo="I.EF.3.1.1.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Reconoce las características, objetivos y proveniencias de "
                "diferentes juegos y elige participar o jugar en ellos, "
                "acordando reglas y pautas de trabajo colectivo seguras. "
                "(J.1., I.4.)"
            ),
            codigo="I.EF.3.1.2.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Construye con pares a partir del trabajo en equipo, "
                "diferentes formas de resolver de manera segura los "
                "desafíos, situaciones problemáticas y lógicas particulares "
                "que presentan los juegos, desde sus experiencias corporales "
                "previas. (S.4.)"
            ),
            codigo="I.EF.3.2.1.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Participa en diversos juegos reconociendo su propio "
                "desempeño (posibilidades y dificultades de acción), "
                "mejorándolo de manera segura individual y colectiva y "
                "estableciendo diferencias entre los juegos y los deportes a "
                "partir de las características, reglas, demandas, roles y "
                "situaciones de juego en cada uno. (I.2.)"
            ),
            codigo="I.EF.3.2.2.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Construye colectivamente secuencias gimnásticas "
                "individuales y grupales, realizando el acondicionamiento "
                "corporal necesario, utilizando variantes de destrezas y "
                "acrobacias, percibiendo el tiempo y espacio y reconociendo "
                "las capacidades motoras a mejorar durante su participación "
                "en las mismas. (J.4., S.4.)"
            ),
            codigo="I.EF.3.3.1.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Construye con pares acuerdos de seguridad y trabajo en "
                "equipo, facilitando la confianza en la realización de "
                "secuencias gimnásticas grupales. (J.1., I.3.)"
            ),
            codigo="I.EF.3.3.2.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Construye composiciones expresivo comunicativas "
                "individuales y colectivas de manera segura y colaborativa, "
                "utilizando y compartiendo con sus pares diferentes recursos "
                "(emociones, sensaciones, estados de ánimo, movimientos, "
                "experiencias previas, otros), ajustándolos rítmicamente (al "
                "ritmo musical y de pares) durante la interpretación de "
                "mensajes y/o historias reales o ficticias. (I.3., S.4.)"
            ),
            codigo="I.EF.3.4.1.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Participa y presenta ante diferentes públicos "
                "manifestaciones expresivo-comunicativas de la propia región "
                "y de otras, reconociendo el objetivo de las mismas y "
                "valorando su aporte cultural a la riqueza nacional. (J.1., "
                "S.2.)"
            ),
            codigo="I.EF.3.4.2.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Participa y/o juega de manera segura en juegos de "
                "iniciación deportiva individual y colectiva, identificando "
                "las lógicas, características, objetivos y demandas de cada "
                "uno, construyendo con sus pares diferentes respuestas "
                "técnicas, tácticas y estratégicas, y diferenciándolos de "
                "los deportes. (I.2., S.4.)"
            ),
            codigo="I.EF.3.5.1.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Mejora su desempeño de manera segura y con ayuda de sus "
                "pares en diferentes juegos de iniciación deportiva, a "
                "partir del reconocimiento de su condición física de partida "
                "y la posibilidad que le brindan las reglas de ser acordadas "
                "y modificadas, según sus intereses y necesidades. (J.4., "
                "S.3.)"
            ),
            codigo="I.EF.3.5.2.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Reconoce sus facilidades y dificultades de participar en "
                "diferentes prácticas corporales y las mejora con ayuda de "
                "sus pares, a partir del conocimiento de su cuerpo, las "
                "posibilidades de acción (contracción, relajación muscular y "
                "posibilidades de movimientos articulares) y la confianza en "
                "sí mismo y en los demás. (J.4., S.3.)"
            ),
            codigo="I.EF.3.6.1.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Reconoce los efectos de las representaciones sociales "
                "(propias y del entorno) sobre las prácticas corporales, en "
                "relación con sus conocimientos y experiencias corporales. "
                "(J.1., I.2.)"
            ),
            codigo="I.EF.3.6.2.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Participa de manera segura, saludable y placentera en "
                "prácticas corporales, reconociendo las dificultades propias "
                "y de sus pares para alcanzar los objetivos de las mismas. "
                "(J.4., I.1.)"
            ),
            codigo="I.EF.3.7.1.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Alcanza de manera segura, saludable y placentera los "
                "objetivos y exigencias de diferentes prácticas corporales, "
                "reconociendo su condición física de partida y realizando el "
                "acondicionamiento corporal previo y posterior, evitando "
                "lesiones durante su participación. (J.3., S.3.)"
            ),
            codigo="I.EF.3.7.2.",
            criterio_evaluacion=criterio3_7
        ),
        # Superior
        Indicador(
            description=(
                "Participa individualmente y con pares en diferentes "
                "categorías de juegos, reconociendo lógicas, "
                "características, orígenes, demandas y conocimientos "
                "corporales que le permitan mejorar cooperativamente y de "
                "manera segura las posibilidades de resolución de tácticas y "
                "estrategias colectivas. (J.1., S.4.)"
            ),
            codigo="I.EF.4.1.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Participa en diferentes juegos identificando situaciones de "
                "riesgo y llevando a cabo las acciones individuales y "
                "colectivas necesarias, durante la construcción del material "
                "y acondicionamiento del espacio antes y durante su "
                "participación en diferentes juegos. (J.3.)"
            ),
            codigo="I.EF.4.1.2.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Crea diferentes juegos estableciendo individual y "
                "colectivamente características, objetivos, reglas y pautas "
                "de trabajo seguras, reconociendo aquellos aspectos que "
                "motivan su práctica. (J.2., I.1.)"
            ),
            codigo="I.EF.4.2.1.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Recrea diferentes juegos, modificando individualmente y con "
                "sus pares objetivos, reglas, roles de juego y pautas de "
                "seguridad en función del entorno y las necesidades "
                "identificadas por los participantes. (J.1., S.4.)"
            ),
            codigo="I.EF.4.2.2.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Construye tácticas y estrategias individuales y colectivas "
                "que le permitan, a partir del reconocimiento del entorno y "
                "de las diferencias entre participantes, alcanzar "
                "eficazmente y de manera segura el objetivo del juego, "
                "(I.4.,S.1.)"
            ),
            codigo="I.EF.4.2.3.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Asume diferentes roles antes y durante su participación, de "
                "manera segura, en función del entorno y las demandas que "
                "cada juego le presenta. (J.4., S.4.)"
            ),
            codigo="I.EF.4.2.4.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Reconoce las estrategias de juego adversarias y las "
                "contrarresta asumiendo los roles de juego, en función de la "
                "identificación de las propias posibilidades de acción y las "
                "de sus pares. (J.4., S.1.)"
            ),
            codigo="I.EF.4.2.5.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Establece diferencias entre habilidades motrices básicas de "
                "ejercicios construidos, que le permiten tranferir a otras "
                "prácticas corporales de manera eficaz y segura, ejercicios, "
                "destrezas y acrobacias gimnásticas. (I.1., S.3.)"
            ),
            codigo="I.EF.4.3.1.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Construye con pares, de manera segura, eficaz y placentera "
                "composiciones y coreografías gimnásticas, asociando "
                "habilidades motrices básicas, desplazamientos y enlaces "
                "gimnásticos, acuerdos y cuidados colectivos en función del "
                "entorno. (J.1., I.2.)"
            ),
            codigo="I.EF.4.3.2.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Identifica posibles cambios corporales producidos por la "
                "realización de prácticas gimnásticas, reconociendo y "
                "teniendo en cuenta su condición física de partida. (S.3.)"
            ),
            codigo="I.EF.4.3.3.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Crea diversas prácticas corporales expresivo-comunicativas, "
                "expresando y comunicando percepciones, sensaciones y "
                "estados de ánimos en escenarios individuales y grupales, "
                "identificando recursos necesarios y elementos que favorecen "
                "y obstaculizan su participación, otorgándole sentidos y "
                "significados a su creación. (J.4., I.1.)."
            ),
            codigo="I.EF.4.4.1.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Recrea diferentes prácticas corporales "
                "expresivo-comunicativas, utilizando diferentes recursos y "
                "reconociendo la pertenencia cultural de las mismas a sus "
                "contextos de origen (grupos, regiones, etc.). (I.3., S.2.)"
            ),
            codigo="I.EF.4.4.2.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Construye espacios escénicos individuales y colectivos en "
                "los que pueda vincular saberes de otras áreas, utilizando "
                "diferentes recursos expresivos (percepciones, sensaciones, "
                "estados de ánimo, música, vestuarios, entre otras), "
                "reconociendo los beneficios y las posibilidades que ofrecen "
                "la realización de improvisaciones, ensayos, coreografías y "
                "composiciones. (I.3., S.4.)"
            ),
            codigo="I.EF.4.5.1.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Construye con pares espacios de confianza, respeto, "
                "colaboración y seguridad antes y durante la presentación, "
                "frente a un público, de diferentes prácticas corporales "
                "expresivo-comunicativas. (J.2., S.1.)"
            ),
            codigo="I.EF.4.5.2.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Participa de manera colaborativa y segura en diversas "
                "prácticas deportivas, identificando las características que "
                "las diferencian de los juegos (reglas, lógicas, objetivos, "
                "entre otros) y la necesidad del trabajo en equipo y el "
                "juego limpio. (I.4., S.4.)"
            ),
            codigo="I.EF.4.6.1.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Construye estrategias individuales y colectivas empleando "
                "las técnicas y tácticas más efectivas, en la resolución de "
                "las situaciones problemas que presentan los deportes y los "
                "juegos. (I.1., S.3.)"
            ),
            codigo="I.EF.4.6.2.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales individuales "
                "y/o colectivas de manera segura, identificando las razones "
                "que le permiten elegirlas, valorando y respetando las "
                "diferencias sociales y personales en la práctica de las "
                "mismas. (I.3., S.3.)"
            ),
            codigo="I.EF.4.7.1.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Reconoce la influencia de las etiquetas y representaciones "
                "sociales sobre el cuerpo (cuerpo como organismo biológico "
                "y/o construcción social, etiquetas sociales), en su "
                "participación en diferentes prácticas corporales en "
                "interacción con pares. (I.2., S.2.)"
            ),
            codigo="I.EF.4.7.2.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Reconoce las ejercitaciones, beneficios y conocimientos "
                "(corporales y de la práctica) necesarios para alcanzar sus "
                "objetivos personales de manera placentera y confortable. "
                "(J.4., S.3.)"
            ),
            codigo="I.EF.4.8.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Identifica los cambios y malestares corporales, beneficios "
                "y riesgos que se producen durante y después de la "
                "realización de la práctica corporal. (J.4., S.3.)"
            ),
            codigo="I.EF.4.8.2.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas corporales realizando el "
                "acondicionamiento corporal previo a la realización de las "
                "mismas, reconociendo los beneficios a corto y largo plazo "
                "del mismo, en la construcción de maneras de estar y "
                "permanecer saludable. (S.3.)"
            ),
            codigo="I.EF.4.8.3.",
            criterio_evaluacion=criterio4_8
        ),
        # Bachillerato
        Indicador(
            description=(
                "Establece relaciones entre diferentes juegos, sus contextos "
                "de origen, los sentidos y significados que le otorgan los "
                "participantes durante su participación y el impacto en la "
                "construcción de la identidad corporal y las dimensiones "
                "social, cognitiva, motriz y afectiva de los sujetos. (J.1., "
                "S.2.)"
            ),
            codigo="I.EF.5.1.1.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Participa en diferentes juegos reconociendo las diferencias "
                "individuales, su competencia motriz y la necesidad de "
                "cooperar con pares, identificando las dificultades y "
                "posibilidades que representa trabajar en equipo. (J.4., "
                "I.4.)"
            ),
            codigo="I.EF.5.1.2.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Elabora estrategias y tácticas colectivas que le permitan "
                "alcanzar el objetivo del juego antes que su adversario y "
                "reconocer el valor del trabajo en equipo antes y durante su "
                "participación en juegos, a partir del reconocimiento de las "
                "diferencias individuales. (I.4.)"
            ),
            codigo="I.EF.5.1.3.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Mejora su condición física de manera segura, sistemática y "
                "consciente a partir de la construcción de ejercicios y "
                "planes básicos, en función de los objetivos a alcanzar. "
                "(I.2., S.3.)"
            ),
            codigo="I.EF.5.2.1.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Construye ejercicios, ejecuta movimientos, maneja objetos y "
                "optimiza su respiración y posturas, a partir del "
                "reconocimiento de su dominio corporal. (J.4., I.4.)"
            ),
            codigo="I.EF.5.2.2.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Establece diferencias entre las prácticas gimnasticas y las "
                "prácticas deportivas, reconociendo las demandas de las "
                "mismas y la necesidad de mejorar su condición física para "
                "participar en ellas de manera segura, placentera y "
                "consciente. (J.3., S.3.)"
            ),
            codigo="I.EF.5.2.3.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Combina prácticas corporales expresivo-comunicativas "
                "reconociendo las demandas, los sentidos y significados para "
                "los protagonistas, durante la comunicación e intercambio de "
                "mensajes corporales. (I.1., S.2.)"
            ),
            codigo="I.EF.5.3.1.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Participa en la construcción de creaciones escénicas "
                "colectivas, reconociendo a las prácticas corporales "
                "expresivo-comunicativas como producciones valiosas para la "
                "cultura, los contextos y los sujetos. (J.1., S.2.)"
            ),
            codigo="I.EF.5.3.2.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Construye colectivamente espacios de trabajo respetuosos "
                "que le posicionen como protagonista y/o espectador y que "
                "favorezcan la creación de manifestaciones no estereotipadas "
                "ni hegemónicas, mediante el lenguaje corporal. (J.2., S.1.)"
            ),
            codigo="I.EF.5.4.1.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Crea nuevas formas de danzar, utilizando acciones y "
                "secuencias con intencionalidad expresiva, y las diferencia "
                "de las danzas convencionales, a partir de las demandas que "
                "le generan cada una. (I.2., S.3.)"
            ),
            codigo="I.EF.5.4.2.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas deportivas, de manera "
                "segura, eficaz y colaborativa, comprendiendo la lógica "
                "interna de cada una y las posibilidades de acción que "
                "permiten los reglamentos. (J.2., I.4.)"
            ),
            codigo="I.EF.5.5.1.",
            criterio_evaluacion=criterio5_5
        ),
        Indicador(
            description=(
                "Participa en diferentes prácticas deportivas, realizando "
                "ajustes individuales, colectivos y contextuales (técnicos, "
                "tácticos, estratégicos y corporales) necesarios en el "
                "trabajo de equipo, percibiendo las sensaciones que le "
                "favorecen u obstaculizan el alcance de los objetivos. "
                "(J.4., S.4.)"
            ),
            codigo="I.EF.5.5.2.",
            criterio_evaluacion=criterio5_5
        ),
        Indicador(
            description=(
                "Realiza prácticas deportivas reconociendo los beneficios "
                "que pueden aportar a su salud y a su condición física, "
                "valorando el juego limpio y percibiendo las sensaciones que "
                "favorecen u obstaculizan su desempeño y participación "
                "dentro y fuera de la institución educativa. (J.2., S.3.)"
            ),
            codigo="I.EF.5.5.3.",
            criterio_evaluacion=criterio5_5
        ),
        Indicador(
            description=(
                "Mejora su participación consciente y construye competencia "
                "motriz en diferentes prácticas corporales, a partir de "
                "percibir su estado corporal en movimiento y/o en reposo. "
                "(J.4., S.3.)"
            ),
            codigo="I.EF.5.6.1.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Explicita las percepciones y sensaciones (dolor, fatiga, "
                "entusiasmo, placer, entre otras) que favorecen u "
                "obstaculizan su deseo de moverse y la construcción de su "
                "competencia motriz, influyendo en la toma de decisiones "
                "sobre su participación en prácticas corporales individuales "
                "y colectivas. (J.4., S.3.)"
            ),
            codigo="I.EF.5.6.2.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Establece relaciones entre las percepciones propias y de "
                "las demás personas sobre el propio desempeño y las "
                "diferencias personales y sociales, en la construcción de la "
                "competencia motriz. (J.3., I.3.)"
            ),
            codigo="I.EF.5.7.1.",
            criterio_evaluacion=criterio5_7
        ),
        Indicador(
            description=(
                "Explicita la influencia que las etiquetas sociales, los "
                "modelos estéticos, las percepciones sobre la propia imagen "
                "y los movimientos estereotipados tienen sobre la "
                "singularidad de los sujetos y la construcción de su "
                "identidad corporal. (J.3., S.3.)"
            ),
            codigo="I.EF.5.7.2.",
            criterio_evaluacion=criterio5_7
        ),
        Indicador(
            description=(
                "Identifica las demandas de las prácticas corporales y las "
                "relaciona con el impacto en la salud, asumiendo una actitud "
                "crítica y reflexiva sobre sus propias prácticas cuidando de "
                "sí, de pares y del ambiente. (J.3., S.3.)"
            ),
            codigo="I.EF.5.8.1.",
            criterio_evaluacion=criterio5_8
        ),
        Indicador(
            description=(
                "Plantea objetivos personales de mejora de su condición "
                "física, a partir de la identificación de los beneficios "
                "que, una determinada actividad física realizada "
                "pertinentemente, suponen para su salud. (I.2., S.3.)"
            ),
            codigo="I.EF.5.8.2.",
            criterio_evaluacion=criterio5_8
        ),
        Indicador(
            description=(
                "Realiza prácticas corporales de manera sistemática, "
                "saludable y reflexiva, tomando en consideración las "
                "diferencias individuales y los controles médicos. (J.3., "
                "S.3.)"
            ),
            codigo="I.EF.5.9.1.",
            criterio_evaluacion=criterio5_9
        ),
        Indicador(
            description=(
                "Construye planes de trabajo físico básicos, teniendo en "
                "cuenta los resultados de los controles médicos. (J.4., "
                "I.4.)"
            ),
            codigo="I.EF.5.9.2.",
            criterio_evaluacion=criterio5_9
        ),

    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0049_auto_20180817_2144'),
    ]

    operations = [
        migrations.RunPython(create_indicadores,
                             reverse_code=migrations.RunPython.noop)
    ]
