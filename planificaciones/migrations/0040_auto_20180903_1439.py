from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

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

    Indicador.objects.bulk_create([
        # Física
        Indicador(
            description=(
                "Determina magnitudes cinemáticas escalares como: posición, "
                "desplazamiento, rapidez en el MRU, a partir de tablas y "
                "gráficas. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.1.1.",
            criterio_evaluacion=criterio_fisica_5_1
        ),
        Indicador(
            description=(
                "Obtiene a base de tablas y gráficos las magnitudes "
                "cinemáticas del MRUV como: posición, velocidad, velocidad "
                "media e instantánea, aceleración, aceleración media e "
                "instantánea y desplazamiento. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.1.2.",
            criterio_evaluacion=criterio_fisica_5_1
        ),
        Indicador(
            description=(
                "Obtiene magnitudes cinemáticas del MRUV con un enfoque "
                "vectorial, como: posición, velocidad, velocidad media e "
                "instantánea, aceleración, aceleración media e instantánea y "
                "desplazamiento a base de representaciones gráficas de un "
                "objeto que se mueve en dos dimensiones. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.2.1.",
            criterio_evaluacion=criterio_fisica_5_2
        ),
        Indicador(
            description=(
                "Determina las magnitudes cinemáticas del movimiento "
                "circular uniforme y explica las características del mismo "
                "considerando las aceleraciones normal y centrípeta, a base "
                "de un objeto que gira en torno a un eje. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.3.1.",
            criterio_evaluacion=criterio_fisica_5_3
        ),
        Indicador(
            description=(
                "Resuelve problemas de aplicación de movimiento circular "
                "uniformemente variado y establece analogías entre el MRU y "
                "MCU. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.3.2.",
            criterio_evaluacion=criterio_fisica_5_3
        ),
        Indicador(
            description=(
                "Elabora diagramas de cuerpo libre, resuelve problemas y "
                "reconoce sistemas inerciales y no inerciales, aplicando las "
                "leyes de Newton, cuando el objeto es mucho mayor que una "
                "partícula elemental y se mueve a velocidades inferiores a "
                "la de la luz. (I.2.,I.4.)"
            ),
            codigo="I.CN.F.5.4.1.",
            criterio_evaluacion=criterio_fisica_5_4
        ),
        Indicador(
            description=(
                "Determina, a través de experimentos y ejemplos reales, el "
                "teorema del impulso y la cantidad de movimiento, el "
                "principio de conservación de la cantidad de movimiento "
                "lineal y el centro de masa para un sistema simple de dos "
                "cuerpos. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.4.2.",
            criterio_evaluacion=criterio_fisica_5_4
        ),
        Indicador(
            description=(
                "Determina el peso y analiza el lanzamiento vertical y caída "
                "libre (considerando y sin considerar la resistencia del "
                "aire) de un objeto, en función de la intensidad del campo "
                "gravitatorio. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.5.1.",
            criterio_evaluacion=criterio_fisica_5_5
        ),
        Indicador(
            description=(
                "Analiza la velocidad, ángulo de lanzamiento, aceleración, "
                "alcance, altura máxima, tiempo de vuelo, aceleración normal "
                "y centrípeta en el movimiento de proyectiles, en función de "
                "la naturaleza vectorial de la segunda ley de Newton. (I.2.)"
            ),
            codigo="I.CN.F.5.6.1.",
            criterio_evaluacion=criterio_fisica_5_6
        ),
        Indicador(
            description=(
                "Argumenta desde la experimentación y la observación de "
                "fenómenos la ley de Hooke (fuerza que ejerce un resorte es "
                "proporcional a la deformación que experimenta), "
                "estableciendo su modelo matemático y su importancia para la "
                "vida cotidiana. (I.2., S.4.)"
            ),
            codigo="I.CN.F.5.7.1.",
            criterio_evaluacion=criterio_fisica_5_7
        ),
        Indicador(
            description=(
                "Argumenta, experimentalmente, las magnitudes que "
                "intervienen en el MAS cuando un resorte se comprime o "
                "estira (sin considerar las fuerzas de fricción), a partir "
                "de las fuerzas involucradas en MCU (la fuerza centrífuga es "
                "una fuerza ficticia) y la conservación de la energía "
                "mecánica cuando el resorte está en posición horizontal o "
                "suspendido verticalmente, mediante la identificación de las "
                "energías que intervienen en cada caso. (I.2.)"
            ),
            codigo="I.CN.F.5.8.1.",
            criterio_evaluacion=criterio_fisica_5_8
        ),
        Indicador(
            description=(
                "Determina, experimentalmente, las magnitudes que "
                "intervienen en el MAS cuando un resorte se comprime o "
                "estira (sin considerar las fuerzas de fricción) y la "
                "conservación de la energía mecánica, cuando el resorte está "
                "en posición horizontal o suspendido verticalmente, "
                "identificando las energías que intervienen en cada caso. "
                "(I.2.)"
            ),
            codigo="I.CN.F.5.8.2.",
            criterio_evaluacion=criterio_fisica_5_8
        ),
        Indicador(
            description=(
                "Argumenta, mediante la experimentación y análisis del "
                "modelo de gas de electrones, el origen atómico de la carga "
                "eléctrica, el tipo de materiales según su capacidad de "
                "conducción de carga, la relación de masa entre protón y "
                "electrón e identifica aparatos de uso cotidiano que separan "
                "cargas eléctricas. (I.2.)"
            ),
            codigo="I.CN.F.5.9.1.",
            criterio_evaluacion=criterio_fisica_5_9
        ),
        Indicador(
            description=(
                "Resuelve problemas de aplicación de la ley de Coulomb, "
                "usando el principio de superposición y presencia de un "
                "campo eléctrico alrededor de una carga puntual. (I.2.)"
            ),
            codigo="I.CN.F.5.10.1.",
            criterio_evaluacion=criterio_fisica_5_10
        ),
        Indicador(
            description=(
                "Argumenta los efectos de las líneas de campo en "
                "demostraciones con material concreto, la diferencia de "
                "potencial eléctrico (considerando el trabajo realizado al "
                "mover cargas dentro de un campo eléctrico) y la corriente "
                "eléctrica (en cargas que se mueven a través de "
                "superficies), estableciendo las transformaciones de energía "
                "que pueden darse en un circuito alimentado por una batería "
                "eléctrica. (I.2.)"
            ),
            codigo="I.CN.F.5.10.2.",
            criterio_evaluacion=criterio_fisica_5_10
        ),
        Indicador(
            description=(
                "Demuestra mediante la experimentación el voltaje, la "
                "intensidad de corriente eléctrica, la resistencia "
                "(considerando su origen atómico-molecular) y la potencia "
                "(comprendiendo el calentamiento de Joule), en circuitos "
                "sencillos alimentados por baterías o fuentes de corriente "
                "continua (considerando su resistencia interna). (I.1., "
                "I.2.)"
            ),
            codigo="I.CN.F.5.11.1.",
            criterio_evaluacion=criterio_fisica_5_11
        ),
        Indicador(
            description=(
                "Argumenta experimentalmente la atracción y repulsión de "
                "imanes y las líneas de campo cerradas presentes en un "
                "objeto magnético, y reconoce que las únicas fuentes de "
                "campos magnéticos son los materiales magnéticos y las "
                "corrientes eléctricas. (I.2.)"
            ),
            codigo="I.CN.F.5.12.1.",
            criterio_evaluacion=criterio_fisica_5_12
        ),
        Indicador(
            description=(
                "Explica el funcionamiento de un motor eléctrico, mediante "
                "la acción de fuerzas magnéticas (reconociendo su naturaleza "
                "vectorial) sobre un objeto que lleva corriente ubicada en "
                "el interior de un campo magnético uniforme, la magnitud y "
                "dirección del campo magnético próximo a un conductor "
                "rectilíneo largo y la ley de Ampère. (I.2.)"
            ),
            codigo="I.CN.F.5.12.2.",
            criterio_evaluacion=criterio_fisica_5_12
        ),
        Indicador(
            description=(
                "Determina, mediante ejercicios de aplicación, el trabajo "
                "mecánico con fuerzas constantes, energía mecánica, "
                "conservación de energía, potencia y trabajo negativo "
                "producido por las fuerzas de fricción al mover un objeto a "
                "lo largo de cualquier trayectoria cerrada. (I.2.)"
            ),
            codigo="I.CN.F.5.13.1.",
            criterio_evaluacion=criterio_fisica_5_13
        ),
        Indicador(
            description=(
                "Analiza la temperatura como energía cinética promedio de "
                "sus partículas y experimenta la ley cero de la "
                "termodinámica (usando conceptos de calor especifico, cambio "
                "de estado, calor latente y temperatura de equilibrio), la "
                "transferencia de calor (por conducción, convección y "
                "radiación), el trabajo mecánico producido por la energía "
                "térmica de un sistema y las pérdidas de energía en forma de "
                "calor hacia el ambiente y disminución del orden , que "
                "tienen lugar durante los procesos de transformación de "
                "energía. (I.2.)"
            ),
            codigo="I.CN.F.5.14.1.",
            criterio_evaluacion=criterio_fisica_5_14
        ),
        Indicador(
            description=(
                "Describe con base en un “modelo de ondas mecánicas” los "
                "elementos de una onda, su clasificación en función del "
                "modelo elástico y dirección de propagación y a base de un "
                "“modelo de rayos “ los fenómenos de reflexión, refracción y "
                "la formación de imágenes en lentes y espejos, que cuando un "
                "rayo de luz atraviesa un prisma, esta se descompone en "
                "colores que van desde el infrarrojo hasta el ultravioleta y "
                "el efecto Doppler (por medio del análisis de la variación "
                "en la frecuencia de una onda cuando la fuente y el "
                "observador se encuentran en movimiento relativo). (I.2.)"
            ),
            codigo="I.CN.F.5.15.1.",
            criterio_evaluacion=criterio_fisica_5_15
        ),
        Indicador(
            description=(
                "Establece la dualidad onda partícula de la luz y las "
                "aplicaciones de las ondas en la trasmisión de energía e "
                "información en ondas en los equipos de uso diario. (I.2.)"
            ),
            codigo="I.CN.F.5.15.2.",
            criterio_evaluacion=criterio_fisica_5_15
        ),
        Indicador(
            description=(
                "Explica los campos eléctricos generados en las proximidades "
                "de flujos magnéticos variables, los campos eléctricos "
                "generados en las proximidades de flujos eléctricos "
                "variables, el mecanismo de la radiación electromagnética "
                "por medio de la observación de videos (mostrando el "
                "funcionamiento de aparatos de uso cotidiano), "
                "ejemplificando los avances de la mecatrónica al servicio de "
                "la sociedad. (I.1., I.2.)"
            ),
            codigo="I.CN.F.5.16.1.",
            criterio_evaluacion=criterio_fisica_5_16
        ),
        Indicador(
            description=(
                "Argumenta las tres leyes de Kepler y la ley de gravitación "
                "universal de Newton (a partir de las observaciones de Tycho "
                "Brahe al planeta Marte y el concepto de campo "
                "gravitacional), las semejanzas y diferencias entre el "
                "movimiento de la Luna y los satélites artificiales "
                "(mediante el uso de simuladores). (I.2.)"
            ),
            codigo="I.CN.F.5.17.1.",
            criterio_evaluacion=criterio_fisica_5_17
        ),
        Indicador(
            description=(
                "Explica los límites del Sistema Solar (el cinturón de "
                "Kuiper y la nube de Oort), reconociendo que esta zona "
                "contiene asteroides, cometas y meteoritos y su ubicación "
                "dentro de la Vía Láctea. (I.2.)"
            ),
            codigo="I.CN.F.5.18.1.",
            criterio_evaluacion=criterio_fisica_5_18
        ),
        Indicador(
            description=(
                "Explica los fenómenos de radiación del cuerpo negro, efecto "
                "fotoeléctrico, la radiación electromagnética (considerando "
                "la luz como partículas), el principio de incertidumbre de "
                "Heisenberg, el comportamiento ondulatorio de las partículas "
                "y la dualidad onda partícula a escala atómica. (I.2.)"
            ),
            codigo="I.CN.F.5.19.1.",
            criterio_evaluacion=criterio_fisica_5_19
        ),
        Indicador(
            description=(
                "Argumenta el comportamiento ondulatorio de las partículas y "
                "la dualidad onda partícula a escala atómica (mediante el "
                "experimento de la doble rendija), y la incidencia del "
                "electromagnetismo, la mecánica cuántica y la nanotecnología "
                "en las necesidades de la sociedad contemporánea. (I.2.)"
            ),
            codigo="I.CN.F.5.19.2.",
            criterio_evaluacion=criterio_fisica_5_19
        ),
        Indicador(
            description=(
                "Fundamenta las cuatro fuerzas de la naturaleza: "
                "electromagnética, nuclear fuerte, nuclear débil, "
                "(estableciendo que hay tres formas comunes de "
                "desintegración radiactiva: alfa, beta y gamma) y "
                "gravitacional, valorando los efectos que tiene la "
                "tecnología en la revolución industrial. (I.2.)"
            ),
            codigo="I.CN.F.5.20.1.",
            criterio_evaluacion=criterio_fisica_5_20
        ),
        Indicador(
            description=(
                "Argumenta mediante el modelo estándar, que los protones y "
                "neutrones no son partículas elementales, analizando las "
                "características ( masa, carga, espín) de las partículas "
                "elementales del átomo, distinguiendo partículas reales: "
                "leptones (electrón, neutrino del electrón, muon, neutrino "
                "del muon, tau y neutrino del tau), quarks (up, down, charm, "
                "strange, bottom y top), hadrones (bariones formados por "
                "tres quarks, mesones formados por pares quark-antiquark) y "
                "el efecto de las cuatro fuerzas fundamentales "
                "(electromagnética, nuclear fuerte y débil), mediante "
                "partículas virtuales o “cuantos del campo de fuerza” "
                "(gravitones, fotones, gluones y bosones) distinguiendo en "
                "estos últimos al bosón de Higgs. (I.2.)"
            ),
            codigo="I.CN.F.5.21.1.",
            criterio_evaluacion=criterio_fisica_5_21
        ),
        Indicador(
            description=(
                "Argumenta el modelo estándar “Lambda-CDM” como una "
                "explicación a todo lo observado en el Universo, a excepción "
                "de la gravedad, materia, energía oscura, las "
                "características y los efectos de estas últimas (al tener un "
                "mayor porcentaje de presencia en el Universo). (I.2.)"
            ),
            codigo="I.CN.F.5.22.1.",
            criterio_evaluacion=criterio_fisica_5_22
        ),
        # Biología
        Indicador(
            description=(
                "Explica el origen de la vida desde el sustento científico, "
                "análisis de evidencias y/o la realización de sencillos "
                "experimentos que fundamenten las teorías de la abiogénesis "
                "en la Tierra (refutando la teoría de la generación "
                "espontánea), la identificación de los elementos y "
                "compuestos químicos de la atmósfera de la Tierra primitiva "
                "y los procesos de abiogénesis de las moléculas y "
                "macromoléculas orgánicas. (I.2., S.4.)"
            ),
            codigo="I.CN.B.5.1.1.",
            criterio_evaluacion=criterio_biologia_5_1
        ),
        Indicador(
            description=(
                "Explica la importancia de las biomoléculas a partir de la "
                "sustentación científica y/o la ejecución de experimentos "
                "sencillos sobre los proceso de abiogénesis, características "
                "básicas, estructura, diversidad y función en la materia "
                "viva. (I.3., I.4.)"
            ),
            codigo="I.CN.B.5.1.2.",
            criterio_evaluacion=criterio_biologia_5_1
        ),
        Indicador(
            description=(
                "Explica la importancia de la evolución biológica desde la "
                "sustentación científica de las teorías de la endosimbiosis, "
                "selección natural y sintética de la evolución, la relación "
                "con las diversas formas de vida con el proceso evolutivo y "
                "su repercusión para el mantenimiento de la vida en la "
                "Tierra. (I.2., I.4.)"
            ),
            codigo="I.CN.B.5.2.1.",
            criterio_evaluacion=criterio_biologia_5_2
        ),
        Indicador(
            description=(
                "Argumenta desde la sustentación científica los tipos de "
                "diversidad biológica (a nivel de genes, especies y "
                "ecosistemas) que existen en los biomas del mundo, la "
                "importancia de estos como evidencia de la evolución de la "
                "diversidad y la necesidad de identificar a las especies "
                "según criterios de clasificación taxonómicas (según un "
                "ancestro común y relaciones evolutivas) específicas. (I.2., "
                "J.3.)"
            ),
            codigo="I.CN.B.5.2.2.",
            criterio_evaluacion=criterio_biologia_5_2
        ),
        Indicador(
            description=(
                "Explica desde la fundamentación científica y modelos la "
                "importancia del ADN como portador de la información "
                "genética, transmisor de la herencia, comprendiendo su "
                "estructura, función, proceso de transcripción y traducción "
                "del ARN, las causas y consecuencias de la alteración "
                "genética y cromosómica. (I.2., I.4.)"
            ),
            codigo="I.CN.B.5.3.1.",
            criterio_evaluacion=criterio_biologia_5_3
        ),
        Indicador(
            description=(
                "Explica la trascendencia de la transmisión de la "
                "información genética, desde la sustentación científica y la "
                "ejecución de experimentos; la teoría cromosómica de la "
                "herencia desde la comprensión de los principios no "
                "mendelianos de cruzamiento, y las leyes de Mendel. (I.2., "
                "S.4.)"
            ),
            codigo="I.CN.B.5.4.1.",
            criterio_evaluacion=criterio_biologia_5_4
        ),
        Indicador(
            description=(
                "Analiza patrones de cruzamiento de especies por selección "
                "natural y artificial estableciendo su impacto en la "
                "actualidad, y predice porcentajes genotípicos y fenotípicos "
                "en diferentes generaciones. (J.3., I.2.)"
            ),
            codigo="I.CN.B.5.4.2.",
            criterio_evaluacion=criterio_biologia_5_4
        ),
        Indicador(
            description=(
                "Examina el desarrollo histórico de la genética, desde la "
                "descripción de las leyes de Mendel, el Proyecto Genoma "
                "Humano y la genética de poblaciones, para justificar su "
                "aporte en la salud humana. (I.2., S.1.)"
            ),
            codigo="I.CN.B.5.4.3.",
            criterio_evaluacion=criterio_biologia_5_4
        ),
        Indicador(
            description=(
                "Explica el valor de la biodiversidad, desde la "
                "fundamentación científica de los patrones de evolución de "
                "las especies nativas y endémicas. Reconoce la importancia "
                "social, económica y ambiental y la identificación de los "
                "efectos de las actividades humanas sobre la biodiversidad a "
                "nivel nacional, regional y global. (J.1., J.3.)"
            ),
            codigo="I.CN.B.5.5.1.",
            criterio_evaluacion=criterio_biologia_5_5
        ),
        Indicador(
            description=(
                "Analiza con actitud crítica y reflexiva los modelos de "
                "desarrollo económico, los avances tecnológicos que cubren "
                "las necesidades del crecimiento de la población humana, las "
                "estrategias y políticas nacionales e internacionales "
                "enfocadas al desarrollo sostenible. (J.1., J.2.)"
            ),
            codigo="I.CN.B.5.5.2.",
            criterio_evaluacion=criterio_biologia_5_5
        ),
        Indicador(
            description=(
                "Explica desde la experimentación los tipos de organización "
                "de las células eucariotas (animales y vegetales), la "
                "estructura y función de sus organelos, tipos de membrana y "
                "transporte celular. (I.2., I.4.)"
            ),
            codigo="I.CN.B.5.6.1.",
            criterio_evaluacion=criterio_biologia_5_6
        ),
        Indicador(
            description=(
                "Relaciona los procesos anabólicos y catabólicos "
                "(fotosíntesis y la respiración celular) con la acción "
                "enzimática, los factores que inciden en la velocidad de las "
                "reacciones, los productos y flujos de energía. (I.2., I.4.)"
            ),
            codigo="I.CN.B.5.6.2.",
            criterio_evaluacion=criterio_biologia_5_6
        ),
        Indicador(
            description=(
                "Cuestiona desde la fundamentación científica, social y "
                "ética los efectos del proceso de proliferación celular "
                "alterada, y la influencia de la ingeniería genética en el "
                "área de alimentación y salud de los seres humanos. (I.2., "
                "S.3.)"
            ),
            codigo="I.CN.B.5.6.3.",
            criterio_evaluacion=criterio_biologia_5_6
        ),
        Indicador(
            description=(
                "Explica que en los organismos multicelulares la forma y "
                "función de las células y los tejidos determinan la "
                "organización de órganos, aparatos y sistemas (circulatorio, "
                "respiratorio, digestivo, excretor, nervioso, reproductivo, "
                "endócrino, inmunitario y osteoartomuscular), establece sus "
                "elementos constitutivos (células, tejidos, componentes), "
                "estructura, función en el ser humano y propone medidas para "
                "su cuidado. (I.2., J.3.)"
            ),
            codigo="I.CN.B.5.7.1.",
            criterio_evaluacion=criterio_biologia_5_7
        ),
        Indicador(
            description=(
                "Establece semejanzas y diferencias funcionales (adaptación, "
                "estímulo y respuesta) y estructurales (evolución de órganos "
                "y aparatos) entre los sistemas de diferentes especies, "
                "mediante las cuales puede deducir el grado de complejidad "
                "de los mismos. (J.3., I.4.)"
            ),
            codigo="I.CN.B.5.7.2.",
            criterio_evaluacion=criterio_biologia_5_7
        ),
        Indicador(
            description=(
                "Establece relaciones funcionales entre los diferentes "
                "sistemas (respuesta inmunológica, osmorregulación, "
                "termorregulación, movimiento, estímulo respuesta) de "
                "especies animales, invertebrados y vertebrados. (J.3., "
                "I.4.)"
            ),
            codigo="I.CN.B.5.7.3.",
            criterio_evaluacion=criterio_biologia_5_7
        ),
        Indicador(
            description=(
                "Elabora un plan de salud integral, a partir de la "
                "comprensión de las enfermedades, desórdenes alimenticios y "
                "efectos del consumo de alcohol y las drogras que afectan al "
                "sistema nervioso y endocrino, así como de los problemas "
                "generados por la falta de ejercicio, la exposición a la "
                "contaminación ambiental y el consumo de alimentos "
                "contaminados, reconociendo el valor nutricional de los "
                "alimentos de uso cotidiano. (I.1., I.4.)"
            ),
            codigo="I.CN.B.5.8.1.",
            criterio_evaluacion=criterio_biologia_5_8
        ),
        Indicador(
            description=(
                "Expone, desde la investigación de campo, la importancia de "
                "los programas de salud pública, la accesibilidad a la salud "
                "individual y colectiva, el desarrollo y aplicación de la "
                "Biotecnología al campo de la Medicina y la Agricultura. "
                "(S.1., I.4.)"
            ),
            codigo="I.CN.B.5.8.2.",
            criterio_evaluacion=criterio_biologia_5_8
        ),
        Indicador(
            description=(
                "Explica los procesos que se realizan en las plantas "
                "(transporte, provisión de nutrientes, excreción de "
                "desechos, mecanismos de regulación del crecimiento, "
                "desarrollo vegetal, reproducción) desde la experimentación "
                "y la identificación de sus estructuras, función y factores "
                "que determinan la actividad. (I.2., I.4.)"
            ),
            codigo="I.CN.B.5.9.1.",
            criterio_evaluacion=criterio_biologia_5_9
        ),
        Indicador(
            description=(
                "Argumenta los riesgos de una maternidad/paternidad "
                "prematura, según su proyecto de vida, partiendo del "
                "análisis crítico y reflexivo de la salud sexual y "
                "reproductiva (fecundación, concepción, desarrollo "
                "embrionario y fetal, parto, aborto, formas de promoción, "
                "prevención y protección) y sus implicaciones. (S.1., S.3.)"
            ),
            codigo="I.CN.B.5.10.1.",
            criterio_evaluacion=criterio_biologia_5_10
        ),
        # Química
        Indicador(
            description=(
                "Explica las propiedades y leyes de los gases, reconoce los "
                "gases cotidianos, identifica los procesos físicos y su "
                "incidencia en la salud y el ambiente. (J.3., I.2.)"
            ),
            codigo="I.CN.Q.5.1.1.",
            criterio_evaluacion=criterio_quimica_5_1
        ),
        Indicador(
            description=(
                "Analiza la estructura del átomo comparando las teorías "
                "atómicas de Bohr (explica los espectros de los elementos "
                "químicos), Demócrito, Dalton, Thompson y Rutherford, y "
                "realiza ejercicios de la configuración electrónica desde el "
                "modelo mecánico-cuántico de la materia. (I.2)"
            ),
            codigo="I.CN.Q.5.2.1.",
            criterio_evaluacion=criterio_quimica_5_2
        ),
        Indicador(
            description=(
                "Analiza la estructura electrónica de los átomos a partir de "
                "la posición en la tabla periódica, la variación periódica y "
                "sus propiedades físicas y químicas, por medio de "
                "experimentos sencillos. (I.2.)"
            ),
            codigo="I.CN.Q.5.3.1.",
            criterio_evaluacion=criterio_quimica_5_3
        ),
        Indicador(
            description=(
                "Argumenta con fundamento científico que los átomos se unen "
                "debido a diferentes tipos de enlaces y fuerzas "
                "intermoleculares, y que tienen la capacidad de relacionarse "
                "de acuerdo a sus propiedades al ceder o ganar electrones. "
                "(I.2.)"
            ),
            codigo="I.CN.Q.5.4.1.",
            criterio_evaluacion=criterio_quimica_5_4
        ),
        Indicador(
            description=(
                "Plantea, mediante el trabajo cooperativo, la formación de "
                "posibles compuestos químicos binarios y ternarios (óxidos, "
                "hidróxidos, ácidos, sales e hidruros) de acuerdo a su "
                "afinidad, estructura electrónica, enlace químico, número de "
                "oxidación, composición, formulación y nomenclatura. (I.2., "
                "S.4.)"
            ),
            codigo="I.CN.Q.5.5.1.",
            criterio_evaluacion=criterio_quimica_5_5
        ),
        Indicador(
            description=(
                "Deduce la posibilidad de que se efectúen las reacciones "
                "químicas de acuerdo a la transferencia de energía y a la "
                "presencia de diferentes catalizadores; clasifica los tipos "
                "de reacciones y reconoce los estados de oxidación de los "
                "elementos y compuestos, y la actividad de los metales; y "
                "efectúa la igualación de reacciones químicas con distintos "
                "métodos, cumpliendo con la ley de la conservación de la "
                "masa y la energía para balancear las ecuaciones. (I.2.)"
            ),
            codigo="I.CN.Q.5.6.1.",
            criterio_evaluacion=criterio_quimica_5_6
        ),
        Indicador(
            description=(
                "Argumenta la estructura del átomo de carbono y demuestra "
                "que es un átomo excepcional, que tiene la capacidad de "
                "unirse consigo mismo con diferentes enlaces entre "
                "carbono-carbono, formando así moléculas orgánicas con "
                "propiedades físicas y químicas diversas, que se representan "
                "mediante fórmulas que indican los tipos de enlace que la "
                "conforman. (I.2., I.4.)"
            ),
            codigo="I.CN.Q.5.7.1.",
            criterio_evaluacion=criterio_quimica_5_7
        ),
        Indicador(
            description=(
                "Explica la formación de los hidrocarburos, su estructura y "
                "el tipo de enlace, y los clasifica en alcanos, alquenos, "
                "alquinos y compuestos aromáticos de acuerdo a sus "
                "propiedades físicas y químicas, mediante experimentos "
                "básicos. (I.2., I.3.)"
            ),
            codigo="I.CN.Q.5.8.1.",
            criterio_evaluacion=criterio_quimica_5_8
        ),
        Indicador(
            description=(
                "Clasifica las series homólogas a partir de la estructura de "
                "los compuestos oxigenados: alcoholes, aldehídos, ácidos, "
                "cetonas y éteres y el comportamiento de sus grupos "
                "funcionales. (I.2.)"
            ),
            codigo="I.CN.Q.5.9.1.",
            criterio_evaluacion=criterio_quimica_5_9
        ),
        Indicador(
            description=(
                "Explica las propiedades de los compuestos orgánicos "
                "determinando sus fórmulas empíricas, semidesarrolladas y "
                "desarrolladas; y aplica la nomenclatura de los compuestos "
                "orgánicos analizando las clases de isomerías. (I.2.)"
            ),
            codigo="I.CN.Q.5.9.2.",
            criterio_evaluacion=criterio_quimica_5_9
        ),
        Indicador(
            description=(
                "Justifica desde la experimentación el cumplimiento de las "
                "leyes de transformación de la materia, mediante el cálculo "
                "de la masa molecular, la masa molar (aplicando número de "
                "Avogadro) y la composición porcentual de los compuestos "
                "químicos. (I.2.)"
            ),
            codigo="I.CN.Q.5.10.1.",
            criterio_evaluacion=criterio_quimica_5_10
        ),
        Indicador(
            description=(
                "Explica las características de los sistemas dispersos según "
                "su estado de agregación y compara las disoluciones de "
                "diferente concentración en las soluciones de uso cotidiano, "
                "a través de la realización de experimentos sencillos. "
                "(I.2., I.4.)"
            ),
            codigo="I.CN.Q.5.11.1.",
            criterio_evaluacion=criterio_quimica_5_11
        ),
        Indicador(
            description=(
                "Determina y explica la importancia de las reacciones "
                "ácido-base y de la acidez en la vida cotidiana, y "
                "experimenta con el balance del pH en soluciones comunes y "
                "con la de desalinización del agua. (I.2., J.3.)"
            ),
            codigo="I.CN.Q.5.12.1.",
            criterio_evaluacion=criterio_quimica_5_12
        ),
        Indicador(
            description=(
                "Explica desde la ejecución de sencillos experimentos el "
                "proceso de desalinización y emite su importancia para la "
                "comunidad. (J.3., I.2.)"
            ),
            codigo="I.CN.Q.5.12.2.",
            criterio_evaluacion=criterio_quimica_5_12
        ),
        Indicador(
            description=(
                "Explica la importancia del petróleo y los polímeros en la "
                "creación de materia prima y su aplicabilidad en la vida "
                "diaria; así como identifica los efectos negativos para el "
                "medio ambiente y el ser humano. (I.2., S.1.)"
            ),
            codigo="I.CN.Q.5.13.1.",
            criterio_evaluacion=criterio_quimica_5_13
        ),
        Indicador(
            description=(
                "Argumenta la importancia para el ser humano de los "
                "alcoholes, aldehídos, cetonas, éteres ácidos carboxílicos "
                "grasos y esteres, amidas y aminas, glúcidos, lípidos, "
                "proteínas y aminoácidos (industria y medicina); identifica "
                "los riegos y determina las medidas de seguridad "
                "recomendadas para su manejo; y explica los símbolos que "
                "identifican la presencia de los compuestos aromáticos. "
                "(J.3., S.1.)"
            ),
            codigo="I.CN.Q.5.13.2.",
            criterio_evaluacion=criterio_quimica_5_13
        ),
        Indicador(
            description=(
                "Argumenta la importancia de los biomateriales en la vida "
                "cotidiana, identifica los contaminantes ambientales, los "
                "factores que inciden en la velocidad de la corrosión de los "
                "materiales y comunica métodos y prácticas de prevención "
                "para una mejor calidad de vida. (J.3., S.3.)"
            ),
            codigo="I.CN.Q.5.14.1.",
            criterio_evaluacion=criterio_quimica_5_14
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0039_auto_20180903_1422'),
    ]

    operations = [
        migrations.RunPython(create_indicadores,
                             reverse_code=migrations.RunPython.noop)
    ]
