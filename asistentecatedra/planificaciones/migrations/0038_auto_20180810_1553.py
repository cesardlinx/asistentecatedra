from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    educacion_fisica = Asignatura.objects.get(name="Educación Física")

    # Bloques
    bloque1 = BloqueCurricular.objects.get(
        name="Prácticas lúdicas: los juegos y el jugar"
    )
    bloque2 = BloqueCurricular.objects.get(name="Prácticas gimnásticas")
    bloque3 = BloqueCurricular.objects.get(
        name="Prácticas corporales expreso-comunicativas"
    )
    bloque4 = BloqueCurricular.objects.get(name="Prácticas deportivas")
    bloque5 = BloqueCurricular.objects.get(
        name="Construcción de la identidad corporal"
    )
    bloque6 = BloqueCurricular.objects.get(
        name="Relaciones entre prácticas corporales y salud"
    )

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')

    Destreza.objects.bulk_create([
        # Preparatoria
        # Bloque 1
        Destreza(
            description=(
                "Identificar las características básicas de diferentes tipos "
                "de juegos (de persecución, con elementos, rondas, "
                "ancestrales, en ambientes naturales, individuales y "
                "colectivos, etc.) presentes en el entorno cercano para "
                "participar y disfrutar de ellos."
            ),
            codigo="EF.1.1.1.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Comprender la necesidad de reglas y roles para poder jugar "
                "con otros, estableciendo y respetando acuerdos simples con "
                "sus pares."
            ),
            codigo="EF.1.1.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Comprender la importancia del cuidado de sí y de los pares "
                "como requisito para jugar los juegos de manera segura y "
                "placentera."
            ),
            codigo="EF.1.1.3.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar en los juegos ajustando las propias acciones y "
                "decisiones en relación con otros para no dañarse, ni dañar "
                "a otros."
            ),
            codigo="EF.1.1.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar posibles materiales para construir implementos "
                "para diferentes juegos y construirlos de manera segura (por "
                "ejemplo, pelotas de medias, de papel, zancos con latas y "
                "cuerdas, entre otros)."
            ),
            codigo="EF.1.1.5.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer, diferenciar y practicar diferentes maneras de "
                "realizar las acciones motrices que se necesitan para "
                "participar de manera segura en diferentes juegos "
                "individuales y colectivos."
            ),
            codigo="EF.1.1.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Identificar y nombrar las diferentes partes del cuerpo, "
                "vivenciar las distintas posiciones que adopta (sentado, "
                "arrodillado, cuadrupedia, parado, de cúbico dorsal —boca "
                "arriba—, ventral —boca abajo— y lateral) y las "
                "posibilidades de movimiento que tienen (por ejemplo, los "
                "movimientos que se pueden hacer con los dedos de las manos "
                "y los pies) durante la realización de prácticas "
                "gimnásticas."
            ),
            codigo="EF.1.2.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Explorar sus capacidades de coordinación, flexibilidad, "
                "velocidad, resistencia, fuerza, durante la realización de "
                "prácticas gimnásticas (ejercicios, destrezas y acrobacias)."
            ),
            codigo="EF.1.2.2.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Vivenciar distintas habilidades motrices básicas (correr, "
                "saltar, lanzar, trepar, rodar, rolar, empujar, traccionar, "
                "girar, entre otras), acrobacias y destrezas, identificando "
                "los modos en que las realiza y sus posibles combinaciones, "
                "—qué acciones realizan las diferentes partes del cuerpo—, "
                "reconociendo las diferencias entre ellas (por ejemplo, "
                "entre correr y rolar)."
            ),
            codigo="EF.1.2.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Tener disposición para autosuperarse en la práctica de "
                "habilidades motrices básicas, acrobacias y destrezas."
            ),
            codigo="EF.1.2.4.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del cuidado de sí y de los pares "
                "como requisito para realizar todas las tareas y actividades "
                "de manera segura."
            ),
            codigo="EF.1.2.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Tener disposición para trabajar con otros y respetar "
                "acuerdos de seguridad simples (por ejemplo, ubicación en el "
                "espacio para no interferir con las acciones de los otros), "
                "durante la realización de todos los ejercicios y tareas en "
                "las prácticas gimnásticas."
            ),
            codigo="EF.1.2.6.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Reconocer estados de ánimo, sensaciones y emociones "
                "(alegría, tristeza, aburrimiento, enojo, frío, calor, entre "
                "otras) para crear, expresar y comunicar mensajes corporales "
                "(gestuales convencionales y/o espontáneos)."
            ),
            codigo="EF.1.3.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Usar gestos convencionales y/o espontáneos, habilidades "
                "motrices básicas, posturas, ritmos y tipos de movimiento "
                "(lento, rápido, continuo, discontinuo, fuerte, suave, entre "
                "otros) como recursos expresivos para comunicar los mensajes "
                "producidos."
            ),
            codigo="EF.1.3.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Tener disposición para interpretar mensajes corporales "
                "producidos por otros, respetando las diferentes formas en "
                "que se expresen."
            ),
            codigo="EF.1.3.3.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Traducir a lenguaje oral y/o gráfico los mensajes "
                "corporales producidos."
            ),
            codigo="EF.1.3.4.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear, expresar, comunicar e interpretar mensajes "
                "corporales individuales y con otros, de manera espontánea."
            ),
            codigo="EF.1.3.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Establecer acuerdos con otros que les permitan participar "
                "en prácticas corporales expresivo-comunicativas."
            ),
            codigo="EF.1.3.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Cuidar de sí y de los otros cuando participa en prácticas "
                "corporales expresivo-comunicativas."
            ),
            codigo="EF.1.3.7.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        # Bloque 5
        Destreza(
            description=(
                "Reconocer y explorar las diferentes características y "
                "posibilidades de movimiento de las partes y segmentos del "
                "propio cuerpo, durante la realización de diversas prácticas "
                "corporales."
            ),
            codigo="EF.1.5.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Percibir, registrar y expresar sus estados corporales "
                "(fatiga, agitación, excitación, tensión, relajación, entre "
                "otros) y ritmos internos (cardíaco y respiratorio) en "
                "reposo y durante la realización de diferentes prácticas "
                "corporales, en diversos entornos cercanos."
            ),
            codigo="EF.1.5.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer las nociones espaciales (cerca, lejos, dentro, "
                "fuera, arriba, abajo, a los lados, adelante y atrás) y "
                "temporales (lento, rápido, al mismo tiempo, en diferente "
                "tiempo) en relación a sí mismo de manera estática y "
                "dinámica, durante la realización de prácticas corporales."
            ),
            codigo="EF.1.5.3.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Asociar sus estados corporales y ritmos internos (cardíaco "
                "y respiratorio) con sus modos de participar en prácticas "
                "corporales."
            ),
            codigo="EF.1.5.4.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque5,
        ),
        # Bloque 6
        Destreza(
            description=(
                "Reconocer la necesidad de hacer uso de los cuidados básicos "
                "de higiene personal antes, durante y después de su "
                "participación en toda práctica corporal."
            ),
            codigo="EF.1.6.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la importancia de cuidar el ambiente de "
                "aprendizaje, contribuyendo a su higiene y preservación "
                "antes, durante y luego de la realización de diferentes "
                "prácticas corporales."
            ),
            codigo="EF.1.6.2.",
            asignatura=educacion_fisica,
            subnivel=preparatoria,
            bloque=bloque6,
        ),
        # Elemental
        # BLoque 1
        Destreza(
            description=(
                "Identificar las características, objetivos y roles de los "
                "participantes en diferentes tipos de juegos (de "
                "persecución, de cooperación, de relevos, con elementos, "
                "populares, ancestrales, de percepción, entre otros) como "
                "elementos necesarios para mejorar el desempeño motriz en "
                "ellos."
            ),
            codigo="EF.2.1.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer las demandas (motoras, conceptuales, "
                "actitudinales, entre otras) que presentan los juegos y "
                "explorar distintos modos de responder a ellas, para mejorar "
                "el propio desempeño en diferentes juegos."
            ),
            codigo="EF.2.1.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar posibles modos de optimizar las acciones "
                "motrices necesarias para participar en cada juego, según "
                "los objetivos a alcanzar (por ejemplo, saltar lejos, correr "
                "rápido, lanzar lejos, entre otras)."
            ),
            codigo="EF.2.1.3.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar placenteramente de diferentes tipos de juego a "
                "partir del reconocimiento de las características, objetivos "
                "y demandas que presentan dichas prácticas."
            ),
            codigo="EF.2.1.4.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer la necesidad de construir, acordar, respetar y "
                "modificar las reglas propuestas colectivamente, para "
                "participar de diferentes juegos, pudiendo acondicionarlos "
                "al contexto."
            ),
            codigo="EF.2.1.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer la necesidad de acordar pautas para jugar y "
                "cooperar con otros, de manera segura, en el logro de los "
                "objetivos de diferentes juegos."
            ),
            codigo="EF.2.1.6.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar previamente posibles situaciones de riesgo "
                "presentes en el contexto, para participar de manera segura "
                "en todas las situaciones de juego."
            ),
            codigo="EF.2.1.7.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer y participar/jugar en diferentes juegos propios "
                "de la región."
            ),
            codigo="EF.2.1.8.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar posibles maneras de organizar por categorías "
                "diferentes tipos de juegos, según sus características, "
                "(objetivos, cantidad de jugadores, lógicas, recursos, entre "
                "otras)."
            ),
            codigo="EF.2.1.9.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Construir implementos con materiales reciclables o del "
                "entorno, que le permita participar/jugar en diferentes "
                "juegos."
            ),
            codigo="EF.2.1.10.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque1,
        ),
        # BLoque 2
        Destreza(
            description=(
                "Identificar, diferenciar y practicar diferentes tipos de "
                "destrezas y acrobacias (rol adelante, rol atrás, pirámides, "
                "estáticas y dinámicas) individuales y con otros, de manera "
                "segura."
            ),
            codigo="EF.2.2.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer cuáles son las capacidades (coordinativas y "
                "condicionales: flexibilidad, velocidad, resistencia y "
                "fuerza) que demandan las destrezas y acrobacias e "
                "identificar cuáles predominan en relación con el tipo de "
                "ejercicio que realiza."
            ),
            codigo="EF.2.2.2.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Identificar cuáles son las articulaciones que deben "
                "alinearse cuando se trabajan posiciones invertidas y "
                "percibir contracciones y movimientos que favorecen la "
                "elevación del centro de gravedad en diferentes situaciones."
            ),
            codigo="EF.2.2.3.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar combinaciones de destrezas y habilidades motrices "
                "básicas (por ejemplo, desplazarse y rolar o combinar roles "
                "con saltos y enlazar las destrezas con diferentes "
                "desplazamientos o giros), que le permitan mejorar su "
                "desempeño en la práctica gimnástica."
            ),
            codigo="EF.2.2.4.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Identificar y hacer consciente las posiciones, apoyos, "
                "contracciones, relajaciones, tomas, agarres y contactos del "
                "cuerpo durante la realización de destrezas y acrobacias, "
                "para adoptar las maneras más seguras de realizarlas según "
                "cada estudiante."
            ),
            codigo="EF.2.2.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Identificar la importancia del cuidado de sí y de sus "
                "pares, para construir acuerdos básicos de seguridad que le "
                "permitan la realización de destrezas y acrobacias."
            ),
            codigo="EF.2.2.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Construir con pares la confianza necesaria para realizar de "
                "manera segura y placentera destrezas y acrobacias grupales."
            ),
            codigo="EF.2.2.7.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Identificar y percibir los diferentes estados de ánimo, "
                "emociones y sensaciones que se pueden expresar en las "
                "prácticas corporales expresivo-comunicativas."
            ),
            codigo="EF.2.3.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer las posibilidades expresivas de los movimientos "
                "(lento, rápido, continuo, discontinuo, fuerte, suave, entre "
                "otros) y utilizar gestos, imitaciones y posturas como "
                "recursos expresivos para comunicar historias, mensajes, "
                "estados de ánimos y sentimientos."
            ),
            codigo="EF.2.3.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer y participar de diferentes prácticas corporales "
                "expresivo - comunicativas vinculadas con las tradiciones de "
                "la propia región."
            ),
            codigo="EF.2.3.3.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer los sentidos identitarios que los contextos "
                "otorgan a las danzas, circos, teatralizaciones, carnavales, "
                "entre otras manifestaciones culturales, para realizarlas de "
                "manera significativa."
            ),
            codigo="EF.2.3.4.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Ajustar las posibilidades expresivas del movimiento a "
                "diferentes ritmos, de acuerdo a las intenciones o sentidos "
                "del mensaje que se quiere expresar y/o comunicar."
            ),
            codigo="EF.2.3.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Construir composiciones expresivo-comunicativas con otras "
                "personas, reconociendo la necesidad de realizar acuerdos y "
                "respetarlos para lograrlo."
            ),
            codigo="EF.2.3.6.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer el valor cultural de las danzas y sus "
                "características principales(por ejemplo, coreografía y "
                "música) como producciones culturales de la propia región y "
                "participar en ellas de modos placenteros."
            ),
            codigo="EF.2.3.7.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer la necesidad del cuidado de sí y de los demás en "
                "la realización de todas las prácticas corporales "
                "expresivo-comunicativas, para tomar las precauciones "
                "acordes en cada caso."
            ),
            codigo="EF.2.3.8.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Construir con pares espacios de confianza que favorezcan la "
                "participación colectiva en diferentes prácticas corporales "
                "expresivo-comunicativas."
            ),
            codigo="EF.2.3.9.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque3,
        ),
        # Bloque 5
        Destreza(
            description=(
                "Identificar, ubicar y percibir mis músculos y "
                "articulaciones, sus formas y posibilidades de movimiento, "
                "para explorar y mejorar mi desempeño motriz en función de "
                "las demandas u objetivos de las prácticas corporales."
            ),
            codigo="EF.2.5.1.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Identificar ritmos y estados corporales (temperatura, tono "
                "muscular, fatiga, entre otros) propios para regular su "
                "participación (antes, durante y después) en prácticas "
                "corporales."
            ),
            codigo="EF.2.5.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Percibir su cuerpo y las diferentes posiciones (sentado, "
                "arrodillado, cuadrupedia, parado, de cúbico dorsal —boca "
                "arriba—, ventral —boca abajo— y lateral) que adopta en el "
                "espacio (cerca, lejos, dentro, fuera, arriba, abajo, a los "
                "lados, adelante y atrás) y el tiempo (simultaneo, "
                "alternado, sincronizado) durante la realización de "
                "diferentes prácticas corporales para optimizar el propio "
                "desempeño."
            ),
            codigo="EF.2.5.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer y hacer conscientes las acciones motrices propias "
                "para mejorarlas en relación con los objetivos y "
                "características de la práctica corporal que se realice."
            ),
            codigo="EF.2.5.4.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Construir con pares diferentes posibilidades de "
                "participación colectiva en distintas prácticas corporales."
            ),
            codigo="EF.2.5.5.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer y comunicar mis condiciones, mis disposiciones y "
                "mis posibilidades (si me gusta la práctica, si conozco lo "
                "que debo hacer, el sentido de la diversión en la práctica, "
                "mis aptitudes, mis dificultades, entre otros) para poder "
                "participar con pares en diferentes prácticas corporales."
            ),
            codigo="EF.2.5.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Construir con pares acuerdos de cooperación y colaboración "
                "para participar colectivamente en diferentes prácticas "
                "corporales según las características del grupo."
            ),
            codigo="EF.2.5.7.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque5,
        ),
        # Bloque 6
        Destreza(
            description=(
                "Identificar riesgos y acordar con otros los cuidados "
                "necesarios para participar en diferentes prácticas "
                "corporales de manera segura."
            ),
            codigo="EF.2.6.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer y analizar las posibles maneras saludables de "
                "participar en diferentes prácticas corporales para ponerlas "
                "en práctica."
            ),
            codigo="EF.2.6.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer posturas favorables en relación con las "
                "características del propio cuerpo y las situaciones en las "
                "que se encuentra al realizar distintas prácticas corporales "
                "para mejorarlas."
            ),
            codigo="EF.2.6.3.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Identificar posturas adecuadas y menos lesivas para evitar "
                "ponerse o poner en riesgo a sus compañeros, ante el deseo "
                "de mejorarel desempeño en diferentes prácticas corporales."
            ),
            codigo="EF.2.6.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del cuidado de sí y de las demás "
                "personas, durante la participación en diferentes prácticas "
                "corporales para tomar las precauciones necesarias en cada "
                "caso (hidratación y alimentación acorde a lo que cada "
                "práctica requiera)."
            ),
            codigo="EF.2.6.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer al medio ambiente como espacio para la "
                "realización de prácticas corporales contribuyendo a su "
                "cuidado dentro y fuera de la institución educativa."
            ),
            codigo="EF.2.6.6.",
            asignatura=educacion_fisica,
            subnivel=elemental,
            bloque=bloque6,
        ),
        # Media
        # Bloque 1
        Destreza(
            description=(
                "Identificar y diferenciar las características, proveniencia "
                "y objetivos de diferentes tipos de juegos (de relevos, con "
                "elementos, cooperativos, acuáticos, populares, en el medio "
                "natural, rondas, entre otros) para participar en ellos y "
                "reconocerlos como producción de la cultura."
            ),
            codigo="EF.3.1.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Crear con sus pares nuevos juegos, estableciendo objetivos, "
                "reglas, características, formas de agruparlos que respondan "
                "a sus intereses y deseos."
            ),
            codigo="EF.3.1.2.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Acordar reglas y pautas de seguridad para poder participar "
                "en juegos colectivos, de manera democrática y segura."
            ),
            codigo="EF.3.1.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer el sentido, la necesidad y las posibilidades de "
                "las reglas de ser modificadas, creadas, recreadas, "
                "acordadas y respetadas para participar/jugar en diferentes "
                "juegos, según sus necesidades e intereses."
            ),
            codigo="EF.3.1.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer si participa o juega en diferentes juegos, para "
                "poder decidir los modos de intervenir en ellos (según las "
                "posibilidades, deseos o potenciales de cada jugador) e "
                "identificar aquellos que se ligan al disfrute para jugarlos "
                "fuera de la escuela."
            ),
            codigo="EF.3.1.5.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar en juegos (cooperativos, de oposición) de manera "
                "segura cuidando de sí mismo y sus pares, identificando las "
                "demandas (motoras, conceptuales, actitudinales, entre "
                "otras) y lógicas particulares para ajustar sus acciones y "
                "decisiones al logro del objetivo de los mismos."
            ),
            codigo="EF.3.1.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer la necesidad del trabajo en equipo para responder "
                "a las demandas y objetivos de los juegos colectivos "
                "(cooperativos o de oposición)."
            ),
            codigo="EF.3.1.7.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Construir con sus pares diferentes estrategias para los "
                "desafíos que presenta cada juego (de dominio técnico y "
                "táctico), reconociendo y asumiendo roles según las "
                "situaciones del juego (ataque y defensa, perseguidor y "
                "perseguido, buscadores y buscados, jugador comodín, entre "
                "otros)."
            ),
            codigo="EF.3.1.8.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar/jugar de diversos juegos de otras regiones "
                "(barrios, parroquias, cantones, ciudades, provincias), "
                "caracterizándolos y diferenciándolos de los de su propio "
                "contexto."
            ),
            codigo="EF.3.1.9.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar semejanzas y diferencias entre los juegos y los "
                "deportes, en sus características, objetivos, reglas, "
                "presencia de los mismos en sus contextos y sobre las "
                "posibilidades de participar y elegir para practicarlos."
            ),
            codigo="EF.3.1.10.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Vivenciar las diferentes variantes de ejecución de las "
                "destrezas (con una mano, piernas separadas, con salto, con "
                "piernas juntas, entre otros) y acrobacias (tomas, agarres, "
                "roles), de manera segura y placentera."
            ),
            codigo="EF.3.2.1.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Crear secuencias gimnásticas individuales y grupales con "
                "diferentes destrezas(y sus variantes), utilizando como "
                "recursos los saltos, giros y desplazamientos para "
                "enlazarlas, entre otros."
            ),
            codigo="EF.3.2.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del trabajo en equipo, la ayuda y "
                "el cuidado de las demás personas, como indispensable para "
                "la realización de los ejercicios, las destrezas y creación "
                "de acrobacias grupales, de modo seguro."
            ),
            codigo="EF.3.2.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Percibir y registrar el uso del espacio (ejemplo: niveles: "
                "alto, medio y bajo. Planos y ejes: sagital, transversal, "
                "longitudinal, profundidad) y el tiempo (velocidades, "
                "simultaneidad, alternancia, entre otras), en la realización "
                "de destrezas, acrobacias y secuencias gimnásticas "
                "individuales y grupales."
            ),
            codigo="EF.3.2.4.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer cuáles son las capacidades motoras (coordinativas "
                "y condicionales: flexibilidad, velocidad, resistencia y "
                "fuerza) que intervienen en la ejecución de diferentes "
                "prácticas gimnásticas e identificar cuáles requieren "
                "mejorarsepara optimizar las posibilidades de realizarlas."
            ),
            codigo="EF.3.2.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Construir y respetar los acuerdos de seguridad para la "
                "realización de las secuencias gimnásticas, destrezas y "
                "acrobacias, reconociendo la importancia del cuidado de sí y "
                "de sus pares, como indispensables."
            ),
            codigo="EF.3.2.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Construir con pares la confianza necesaria para realizar de "
                "manera segura y placentera destrezas y acrobacias grupales."
            ),
            codigo="EF.3.2.7.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Reconocer y analizar la relación entre las emociones de "
                "cada persona y sus modos de participación en diferentes "
                "prácticas expresivo-comunicativas, para mejorar su "
                "desempeño en ellas."
            ),
            codigo="EF.3.3.1.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Realizar el ajuste del ritmo propio al ritmo musical (o "
                "externo) y de las demás personas, en la realización de "
                "diferentes coreografías/composiciones."
            ),
            codigo="EF.3.3.2.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Construir individualmente y con otros diferentes "
                "composiciones expresivo-comunicativas reconociendo, "
                "percibiendoy seleccionando diferentes movimientos, según la "
                "intencionalidad expresiva (lento, rápido, continuo, "
                "discontinuo, fuerte, suave, entre otros) del mensaje a "
                "comunicar."
            ),
            codigo="EF.3.3.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Elaborar, comunicar, reproducir e interpretar mensajes "
                "escénicos que reflejen historias reales o ficticias en "
                "diferentes manifestaciones expresivo- comunicativas (danza, "
                "composiciones, coreografías, prácticas circenses, entre "
                "otras) para ser presentados ante diferentes públicos."
            ),
            codigo="EF.3.3.4.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Vivenciar, reconocer, valorar y respetar las "
                "manifestaciones expresivo-comunicativas propias y de otras "
                "regiones, vinculándolas con sus significados de origen "
                "(música, vestimenta, lenguaje, entre otros) para comprender "
                "los aportes a la riqueza cultural."
            ),
            codigo="EF.3.3.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Tener disposición para ayudar y cuidar de sí y de otros en "
                "las prácticas corporales expresivo-comunicativas para "
                "participar de ellas de modo seguro."
            ),
            codigo="EF.3.3.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque3,
        ),
        # Bloque 4
        Destreza(
            description=(
                "Establecer acuerdos en las reglas y pautas de seguridad "
                "para poder participar en diferentes prácticas deportivas "
                "colectivas de manera democrática y segura."
            ),
            codigo="EF.3.4.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Reconocer los posibles modos de intervenir en diferentes "
                "prácticas deportivas (juegos modificados: de blanco y "
                "diana, de invasión, de cancha dividida, de bate y campo; "
                "juegos atléticos: carreras largas y cortas, carreras de "
                "relevos y con obstáculos, saltos en altura y longitud y "
                "lanzamientos a distancia) para decidir los modos de "
                "participar en ellas (según las posibilidades, deseos o "
                "potenciales de cada jugador) e identificar aquellas "
                "prácticas que se ligan al disfrute para realizarlas fuera "
                "de la escuela."
            ),
            codigo="EF.3.4.2.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Participar en diferentes prácticas deportivas de manera "
                "segura cuidando de sí mismo y sus pares, identificando las "
                "demandas (motoras, conceptuales, actitudinales, entre "
                "otras) planteadas por cada una de ellas, para mejorar el "
                "desempeño y alcanzar el objetivo de la misma."
            ),
            codigo="EF.3.4.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Participar en diferentes tipos de prácticas deportivas "
                "(juegos modificados y atléticos), reconociendo sus lógicas "
                "particulares y resolviendo las situaciones problemáticas de "
                "los mismos, mediante la construcción de respuestas técnicas "
                "y tácticas que le permitan ajustar sus acciones y "
                "decisiones al logro de los objetivos del juego."
            ),
            codigo="EF.3.4.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Construir estrategias individuales y colectivas para "
                "abordar los desafíos que presenta cada práctica deportiva, "
                "reconociendo y asumiendo diferentes roles(atacante o "
                "defensor), según las situaciones del juego y las "
                "posibilidades de acción de los participantes."
            ),
            codigo="EF.3.4.5.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Identificar semejanzas y diferencias entre los juegos "
                "modificados/atléticos y los deportes, en sus "
                "características, objetivos, reglas, la presencia de los "
                "mismos en sus contextos y sobre las posibilidades de "
                "participación y elección para practicarlos."
            ),
            codigo="EF.3.4.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Reconocer las intenciones tácticas ofensivas (ejemplo: "
                "desmarque, búsqueda de espacios libres, retrasar el retorno "
                "del móvil) y defensivas (ejemplo: marcar, cubrir los "
                "espacios libres, devolver el móvil) como recursos para "
                "resolver favorablemente la participación en los juegos "
                "modificados."
            ),
            codigo="EF.3.4.7.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque4,
        ),
        # Bloque 5
        Destreza(
            description=(
                "Identificar y analizar la influencia de mis experiencias "
                "corporales y lo que me generan emocionalmente (deseo, "
                "miedo, entusiasmo, frustración, disposición, interés, entre "
                "otros) en la construcción de mis posibilidades de "
                "participación y elección de diferentes prácticas "
                "corporales."
            ),
            codigo="EF.3.5.1.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer y analizar las representaciones propias y del "
                "entorno social acerca del propio desempeño y de las "
                "diferentes prácticas corporales, identificando los efectos "
                "que producen las etiquetas sociales (hábil-inhábil, "
                "bueno-malo, femenino-masculino, entre otras) en mi "
                "identidad corporal y en la de las demás personas."
            ),
            codigo="EF.3.5.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Identificar y valorar la necesidad de generar espacios de "
                "confianza que habiliten la construcción de identidades "
                "colectivas, para facilitar el aprendizaje de diferentes "
                "prácticas corporales."
            ),
            codigo="EF.3.5.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer las facilidades y dificultades (motoras, "
                "cognitivas, sociales, entre otras) propias, para construir "
                "individual o colectivamente mis maneras de resolver las "
                "prácticas corporales."
            ),
            codigo="EF.3.5.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Percibir y registrar cuáles son los grupos musculares que "
                "necesitan ser activados(contraídos), relajados y "
                "flexibilizados y vivenciar las posibilidades de movimiento "
                "que poseen las articulaciones, para mejorar el conocimiento "
                "del propio cuerpo y optimizar la ejecución en las prácticas "
                "corporales."
            ),
            codigo="EF.3.5.5.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque5,
        ),
        # Bloque 6
        Destreza(
            description=(
                "Reconocer los diferentes objetivos posibles (recreativo, "
                "mejora del desempeño propio o colectivo, de alto "
                "rendimiento, entre otros) cuando se realizan prácticas "
                "corporales para poder decidir en cuáles elige participar."
            ),
            codigo="EF.3.6.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Realizar acondicionamiento corporal, antes y después de la "
                "participación, en prácticas corporales, identificando su "
                "importancia para mejorar el desempeño y evitar lesiones."
            ),
            codigo="EF.3.6.2.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la condición física de partida (capacidades "
                "coordinativas y condicionales: flexibilidad, velocidad, "
                "resistencia y fuerza) y mejorarla de manera segura y "
                "saludable, en relación a las demandas y objetivos que "
                "presentan las diferentes prácticas corporales."
            ),
            codigo="EF.3.6.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del cuidado de sí y de las demás "
                "personas durante la participación en diferentes prácticas "
                "corporales, identificando los posibles riesgos."
            ),
            codigo="EF.3.6.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la presencia de placer y displacer en la "
                "participación en prácticas corporales, para elegir aquellas "
                "que lo identifican, y practicarla de modo placentero dentro "
                "y fuera del contexto escolar."
            ),
            codigo="EF.3.6.5.",
            asignatura=educacion_fisica,
            subnivel=media,
            bloque=bloque6,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0037_auto_20180809_1800'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
