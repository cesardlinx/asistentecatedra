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
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Superior
        # Bloque 1
        Destreza(
            description=(
                "Participar en diferentes categorías de juegos "
                "(tradicionales, populares, modificados, masivos, "
                "expresivos, con elementos, en el medio natural, entre "
                "otros), reconociendo el aporte cultural proveniente de sus "
                "orígenes, objetivos y lógicas a la identidad nacional."
            ),
            codigo="EF.4.1.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Crear y recrear individualmente y con pares nuevos juegos, "
                "acordando objetivos y reglas, respetando los acuerdos y "
                "modificando las reglas para continuar participando y/o "
                "jugando, según sus intereses y necesidades."
            ),
            codigo="EF.4.1.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar en juegos de diferentes lógicas, identificando "
                "las demandas (motoras, intelectuales, emocionales, "
                "sociales, entre otras) que cada uno le presenta, para "
                "ajustar las decisiones y acciones (técnicas de movimiento) "
                "que le permitan conseguir el objetivo de manera segura, "
                "teniendo en cuenta el entorno."
            ),
            codigo="EF.4.1.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer y mejorar las propias posibilidades de "
                "participación (motora, intelectual, emocional, social, "
                "entre otras) en los juegos, y hacerlas conscientes para "
                "optimizar el disfrute y elegir jugarlos fuera de las "
                "instituciones educativas."
            ),
            codigo="EF.4.1.4.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer las diferencias entre pares como requisito "
                "necesario para cooperar, trabajar en equipo y construir "
                "estrategias colectivas que le permitan alcanzar los "
                "objetivos de los juegos."
            ),
            codigo="EF.4.1.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar el rol que ocupa en los juegos colectivos para "
                "construir y poner en práctica respuestas tácticas "
                "individuales y colectivas que le permitan resolver "
                "situaciones del juego."
            ),
            codigo="EF.4.1.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer y analizar las estrategias que utiliza el "
                "adversario para contrarrestarlas con estrategias "
                "individuales y colectivas y alcanzar los objetivos del "
                "juego."
            ),
            codigo="EF.4.1.7.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Acondicionar los espacios y construir materiales para poder "
                "realizar los juegos de manera segura, priorizando el uso de "
                "materiales reciclables."
            ),
            codigo="EF.4.1.8.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar situaciones riesgosas antes y durante la "
                "participación en los juegos y acordar pautas de trabajo "
                "seguras y respetarlas para el cuidado de sí y de las demás "
                "personas."
            ),
            codigo="EF.4.1.9.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Diferenciar habilidades motrices básicas (caminar, correr, "
                "lanzar y saltar) de ejercicios construidos (acrobacias, "
                "posiciones invertidas, destrezas, entre otros) y practicar "
                "con diferentes grados de dificultad, realizando los ajustes "
                "corporales necesarios para poder ejecutarlos de manera "
                "segura y placentera."
            ),
            codigo="EF.4.2.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer la condición física (capacidad que tiene los "
                "sujetos para realizar actividad física) como un estado "
                "inherente a cada sujeto, que puede mejorarse o deteriorarse "
                "en función de las propias acciones, para tomar decisiones "
                "tendientes a optimizarla."
            ),
            codigo="EF.4.2.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Construir grupalmente (con y sin elementos: pañuelos, "
                "cuerdas, ulas, cintas, pelotas, bastones y clavas) "
                "composiciones gimnásticas y coreografías, identificando las "
                "características, utilizando los desplazamientos gimnásticos "
                "como enlaces y acordando pautas de trabajo colectivo para "
                "encontrar maneras seguras, eficaces y placenteras de "
                "realizarlas."
            ),
            codigo="EF.4.2.3.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer la implicancia de las capacidades coordinativas "
                "en la manipulación de elementos para mejorar su dominio, "
                "durante la participación en prácticas gimnasticas."
            ),
            codigo="EF.4.2.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Asociar y transferir los ejercicios, destrezas y acrobacias "
                "aprendidas a otras prácticas corporales colectivas, "
                "considerando las condiciones espaciales, temporales, "
                "recursos requeridos, y la necesidad de acuerdos grupales "
                "para su realización de modo saludable, seguro y placentero."
            ),
            codigo="EF.4.2.5.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Expresar y comunicar percepciones, sensaciones y estados de "
                "ánimos en composiciones expresivas (individuales y "
                "colectivas), incorporando recursos (música, escenografía, "
                "luces, combinación de prácticas, tipos de lenguajes, etc.) "
                "que permitan una construcción escénica para ser presentada "
                "ante un público (de pares, institucional o comunitario)."
            ),
            codigo="EF.4.3.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer diferentes prácticas corporales expresivo "
                "comunicativas (danzas, teatralizaciones o circo), como "
                "rasgos representativos de la identidad cultural de un grupo "
                "o región."
            ),
            codigo="EF.4.3.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Identificar y diferenciar los recursos expresivos "
                "(intencionalidad de movimiento, sensaciones, estados de "
                "ánimo, gestos, uso del tiempo y espacio, entre otros) de "
                "aquellos recursos que enriquecen los montajes escénicos "
                "(música, escenografía, luces, combinación de prácticas, "
                "tipos de lenguajes, etc.) para mejorar la participación en "
                "diferentes prácticas expresivo-comunicativas."
            ),
            codigo="EF.4.3.3.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Vincular las prácticas corporales expresivo-comunicativas "
                "populares (fiestas, rituales ancestrales, danzas "
                "callejeras, carnavales, entre otros) a los significados de "
                "origen para resignificarlas y recrearlas, reconociendo el "
                "aporte que realizan a la identidad cultural de una "
                "comunidad."
            ),
            codigo="EF.4.3.4.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer aquellos elementos que favorecen u obstaculizan "
                "su participación en las prácticas corporales "
                "expresivo-comunicativas (confianza, vergüenza, timidez, "
                "respeto, entre otras) y poner en práctica estrategias para "
                "mejorar sus intervenciones."
            ),
            codigo="EF.4.3.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer la importancia de construir espacios colectivos "
                "colaborativos de confianza y respeto entre pares, para "
                "construir producciones expresivo-comunicativas de manera "
                "placentera y segura, según los roles propios y de cada "
                "participante (protagonista, espectador)."
            ),
            codigo="EF.4.3.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Elaborar, comunicar, reproducir e interpretar mensajes en "
                "contextos escénicos, que vinculen la creación de prácticas "
                "corporales expresivo-comunicativas (danzas, "
                "teatralizaciones, circos, coreografías, kermes, "
                "celebración) con saberes de otras áreas, para ser "
                "presentados ante un público."
            ),
            codigo="EF.4.3.7.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer las diferencias y posibilidades que brindan la "
                "improvisación y el ensayo, en relación a los objetivos de "
                "las prácticas corporales expresivo-comunicativas e "
                "incorporar el ensayo como una práctica "
                "gimnástica(repetitiva/sistemática) que permite mejorar el "
                "desempeño en las presentaciones."
            ),
            codigo="EF.4.3.8.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque3,
        ),
        # Bloque 4
        Destreza(
            description=(
                "Practicar diferentes tipos de deportes (individuales y "
                "colectivos; cerrados y abiertos; al aire libre o en "
                "espacios cubiertos; de invasión, en la naturaleza, entre "
                "otras), identificando similitudes y diferencias entre "
                "ellos, y reconocer modos de participación según ámbito "
                "deportivo (recreativo, federativo, de alto rendimiento, "
                "entre otros), para considerar requisitos necesarios que le "
                "permitan continuar practicándolo."
            ),
            codigo="EF.4.4.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Reconocer las diferencias entre competencia y exitismo, "
                "para comprender la importancia de la participación en "
                "prácticas deportivas recreativas."
            ),
            codigo="EF.4.4.2.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Identificar las diferencias entre las reglas en los "
                "deportes (institucionalizada) y en los juegos (adaptables, "
                "modificables, flexibles), para reconocer las posibilidades "
                "de participación y posibles modos de intervención en los "
                "mismos."
            ),
            codigo="EF.4.4.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Participar en deportes, juegos deportivos y juegos "
                "modificados comprendiendo sus diferentes lógicas (bate y "
                "campo, invasión, cancha dividida, blanco y diana), "
                "objetivos y reglas utilizando diferentes tácticas y "
                "estrategias para resolver los problemas que se presentan, "
                "asumiendo un rol y valorando la importancia de la ayuda y "
                "el trabajo en equipo, como indispensable para lograr el "
                "objetivo de dichas prácticas."
            ),
            codigo="EF.4.4.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Explorar y practicar maneras efectivas de resolver técnica "
                "y tácticamente los objetivos de deportes y juegos "
                "deportivos, reconociendo la posibilidad de mejorarlas para "
                "optimizar la propia participación y la del equipo, durante "
                "la práctica de los mismos."
            ),
            codigo="EF.4.4.5.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del cuidado de sí y de las demás "
                "personas en la práctica de deportes y juegos deportivos, "
                "identificando al adversario como compañero necesario para "
                "poder participar en ellas."
            ),
            codigo="EF.4.4.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Comprender y poner en práctica el concepto de juego limpio "
                "(fairplay) traducido en acciones y decisiones, y su "
                "relación con el respeto de acuerdos (reglas o pautas), como "
                "requisito necesario para jugar con otras personas."
            ),
            codigo="EF.4.4.7.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque4,
        ),
        # Bloque 5
        Destreza(
            description=(
                "Tomar decisiones sobre su cuerpo a partir del "
                "reconocimiento de su competencia motriz (sus capacidades "
                "motoras y habilidades motrices), la construcción de su "
                "imagen y esquema corporal y de los vínculos emocionales con "
                "las prácticas corporales, en interacción con sus pares "
                "durante su participación en prácticas corporales."
            ),
            codigo="EF.4.5.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer y analizar la influencia que generan las "
                "etiquetas sociales(bueno-malo, niño-niña, hábil-inhábil, "
                "lindo-feo, entre otras) en las posibilidades de "
                "construcción de la identidad corporal, para respetar y "
                "valorar las diferencias personales y sociales."
            ),
            codigo="EF.4.5.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Diferenciar los conceptos de cuerpo como organismo "
                "biológico y cuerpo como construcción social, para reconocer "
                "sentidos, percepciones, emociones y formas de actuar, entre "
                "otras, que inciden en la construcción de la identidad "
                "corporal."
            ),
            codigo="EF.4.5.3.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer los aspectos que promueve la selección de "
                "prácticas corporales, para practicarlas de manera "
                "sistemática, segura y placentera."
            ),
            codigo="EF.4.5.4.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque5,
        ),
        # Bloque 6
        Destreza(
            description=(
                "Reconocer los conocimientos corporales y ejercitaciones "
                "necesarios para lograr el objetivo personal propuesto en la "
                "participación de la práctica corporal."
            ),
            codigo="EF.4.6.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Construir maneras de estar y permanecer saludables "
                "(equilibrio emocional, corporal, ambiental, entre otros), a "
                "partir del reconocimiento de los posibles beneficios a "
                "corto y largo plazo que aporta la participación en "
                "diferentes prácticas corporales, dentro y fuera de la "
                "institución educativa."
            ),
            codigo="EF.4.6.2.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la relación entre la actividad corporal "
                "confortable y placentera, con el bienestar/salud personal y "
                "ambiental, para evitar malestares producidos por el "
                "sedentarismo o la inadecuada realización de actividades "
                "físicas."
            ),
            codigo="EF.4.6.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Explorar e identificar los posibles cambios corporales que "
                "se producen durante y después de la realización de la "
                "práctica corporal, para ser cuidadosos y disfrutar de los "
                "beneficios que la misma produce."
            ),
            codigo="EF.4.6.4.",
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Identificar la importancia del acondicionamiento corporal "
                "previo a la realización de prácticas corporales y "
                "realizarlo para disminuir los riesgos de lesiones y "
                "promover el cuidado de si, de sus pares."
            ),
            codigo="EF.4.6.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Identificar las habilidades motrices que se deben mejorar y "
                "ejercitarlas de forma segura y saludable, para lograr el "
                "objetivo de las prácticas corporales que realiza."
            ),
            codigo="EF.4.6.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=superior,
            bloque=bloque6,
        ),
        # Bachillerato
        # Bloque 1
        Destreza(
            description=(
                "Reconocer a los juegos como manifestaciones constantes en "
                "la historia del hombre y relacionarlas con sus contextos de "
                "origen, su cultura específica y los sentidos y significados "
                "que le permiten a sus participantes convertirlos en una "
                "posible práctica recreativa."
            ),
            codigo="EF.5.1.1.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reconocer cómo impactan los juegos en las diferentes "
                "dimensiones del sujeto, en la social (como facilitador de "
                "relaciones interpersonales), en la motriz (su influencia "
                "como motivador en el desarrollo de las capacidades "
                "coordinativas y condicionales), en la afectiva (la "
                "presencia de las emociones al jugar), en la cognitiva (en "
                "la toma de decisiones a la hora de resolver los problemas "
                "que le presenta el juego), etc."
            ),
            codigo="EF.5.1.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar y participar de juegos modificados (de bate y "
                "campo, de cancha dividida, de blanco y diana y de "
                "invasión), cooperativos (como categoría que involucra otros "
                "juegos), reconociendo diferencias y similitudes con "
                "prácticas deportivas y maneras en que participa/juega para "
                "alcanzar sus objetivos, utilizando tácticas y estrategias "
                "posibles y realizando adecuaciones que considere "
                "necesarias."
            ),
            codigo="EF.5.1.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar los requerimientos motores necesarios para "
                "trabajar en su mejora y poder participar/jugar de distintos "
                "juegos de manera confortable, segura y placentera."
            ),
            codigo="EF.5.1.4.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar de juegos colectivos reconociendo la importancia "
                "del trabajo en equipo (posibilidades y dificultades), de "
                "cooperar y oponerse y el papel de la comunicación motriz "
                "entre los jugadores, para resolver diferentes situaciones "
                "de juego y alcanzar sus objetivos."
            ),
            codigo="EF.5.1.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Reconocer la diferencia entre las prácticas gimnásticas "
                "como prácticas sistemáticas (para mejorar la condición "
                "física: capacidades coordinativas y condicionales, "
                "flexibilidad, velocidad, resistencia y fuerza) y la "
                "práctica gimnástica como práctica deportiva (aeróbica, "
                "artística, rítmica, acro-sport, entre otras) para poder "
                "elegir cómo realizarlas de manera consciente, segura y "
                "saludable."
            ),
            codigo="EF.5.2.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer la necesidad de mejorar de modo saludable la "
                "condición física (capacidad que tienen los sujetos para "
                "realizar actividad física) para favorecer la participación "
                "en diferentes prácticas corporales, así como en acciones "
                "cotidianas."
            ),
            codigo="EF.5.2.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Construir ejercicios que mejoren la condición física y "
                "elaborar entrenamientos básicos para ponerlos en práctica, "
                "tomando como punto de partida su estado de inicio y las "
                "prácticas corporales hacia las cuales están orientados."
            ),
            codigo="EF.5.2.3.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Explorar y reconocer las adaptaciones necesarias de la "
                "respiración y la postura (posiciones favorables en función "
                "de las características corporales de cada sujeto), en "
                "relación a las demandas de la práctica gimnástica y "
                "realizarlas de manera segura, placentera y saludable."
            ),
            codigo="EF.5.2.4.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reconocer posibilidades de dominio corporal en la ejecución "
                "de movimientos y manejo de objetos durante las prácticas "
                "gimnásticas, para mejorarlos de manera consciente, segura y "
                "saludable."
            ),
            codigo="EF.5.2.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Reconocer las prácticas corporales expresivo-comunicativas "
                "como producciones valiosas e identitarias para sus "
                "protagonistas (con orígenes, contextos de producción y "
                "sentidos/significados), y a la vez como posibles "
                "favorecedoras de la socialización y vinculación entre pares "
                "y con la cultura."
            ),
            codigo="EF.5.3.1.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Explorar e identificar diferentes tipos de danzas "
                "(tradicionales, populares, contemporáneas, entre otras), "
                "sus pasos básicos y sus coreografías y las posibilidades de "
                "crear nuevas y propias formas de danzar y expresarse "
                "corporalmente."
            ),
            codigo="EF.5.3.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Identificar los requerimientos (motores, emocionales, "
                "cognitivos, entre otros) que presentan diferentes prácticas "
                "expresivo-comunicativas y vincularlos con sus "
                "características (pasos básicos, música, duración, "
                "coreografía), para tomar decisiones sobre los modos de "
                "participación en ellas según los objetivos individuales y "
                "colectivos."
            ),
            codigo="EF.5.3.3.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Identificar y producir creaciones escénicas colectivas, "
                "vinculando más de una práctica corporal (como lo hacen el "
                "circo, la murga, los carnavales, entre otras), para crear y "
                "comunicar mensajes."
            ),
            codigo="EF.5.3.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear acciones y secuencias motrices, utilizando diferentes "
                "recursos expresivos (intencionalidad expresiva de "
                "diferentes movimientos, según tiempo y espacio: "
                "lento-rápido, simultaneo-alternado, continuo-discontinuo, "
                "atrás-adelante, otros), desde la necesidad propia de "
                "manifestarse mediante el lenguaje corporal para enriquecer "
                "las posibilidades de comunicación individual y colectiva."
            ),
            codigo="EF.5.3.5.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Diferenciar los roles de espectadores y protagonistas, "
                "construyendo maneras de participación respetuosa en ambos, "
                "para transferirlas a situaciones en la vida cotidiana."
            ),
            codigo="EF.5.3.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        # Bloque 4
        Destreza(
            description=(
                "Participar en diversas prácticas deportivas (individuales, "
                "colectivas, abiertas, cerradas, de contacto, entre otras) "
                "reconociendo sus diferencias según los ámbitos en que se "
                "practican (recreativo, amateur, federativo, alto "
                "rendimiento, entre otros), sus objetivos y los modos de "
                "alcanzarlos, para poder elegirlas, apropiarlas y continuar "
                "practicándolas a lo largo de sus vidas."
            ),
            codigo="EF.5.4.1.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Participar en prácticas deportivas comprendiendo la lógica "
                "interna (principios y acciones tácticas) de cada una y "
                "realizando ajustes técnicos, tácticos y estratégicos, en "
                "función de las reglas y requerimientos (motores, "
                "emocionales, cognitivos, sociales) para su resolución "
                "eficaz y confortable."
            ),
            codigo="EF.5.4.2.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Analizar el reglamento de los deportes y reconocerlo como "
                "conjunto de normas producidas por las federaciones, que "
                "marcan los límites y oportunidades de actuación, para tomar "
                "decisiones sobre los modos de participación que le permitan "
                "alcanzar los objetivos de dicha práctica."
            ),
            codigo="EF.5.4.3.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Realizar prácticas deportivas de manera participativa, "
                "inclusiva y reflexiva, democratizando los roles, funciones "
                "y respetando la diversidad cultural y motriz de los "
                "participantes y promoviendo los ajustes por parte de todos, "
                "para garantizar el acceso a la equidad."
            ),
            codigo="EF.5.4.4.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del trabajo en equipo, la ayuda y "
                "la cooperación (como requisito para la oposición), para "
                "lograr el objetivo de las prácticas deportivas y poder "
                "participar en ellas de manera segura y saludable dentro y "
                "fuera del colegio."
            ),
            codigo="EF.5.4.5.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Participar en diferentes prácticas deportivas utilizando "
                "diferentes acciones técnicas y tácticas que favorezcan la "
                "continuidad del juego, reconociendo que las ejecuciones "
                "técnicas y respuestas tácticas cobran sentido en los "
                "contextos de juego (y en función del reglamento)."
            ),
            codigo="EF.5.4.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Percibir y registrar sensaciones asociadas a la práctica "
                "del deporte (comodidad, incomodidad, cansancio, plenitud, "
                "bienestar, frustración, alegría, etc.), como "
                "obstaculizadoras o favorecedoras de su desempeño en el "
                "mismo."
            ),
            codigo="EF.5.4.7.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Reconocer los valores del juego limpio (en función del "
                "respeto a los acuerdos y reglas) y participar en prácticas "
                "deportivas en coherencia con ellos, para transferir esos "
                "valores a situaciones cotidianas."
            ),
            codigo="EF.5.4.8.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        Destreza(
            description=(
                "Comprender la necesidad de una preparación física adecuada "
                "y coherente con las prácticas deportivas, en función de sus "
                "objetivos (recreativo, federativo, de alto rendimiento) y "
                "requerimientos motrices, para minimizar los riesgos de "
                "lesiones y optimizar el desempeño seguro en el deporte de "
                "que se trate."
            ),
            codigo="EF.5.4.9.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque4,
        ),
        # Bloque 5
        Destreza(
            description=(
                "Percibir y tomar conciencia de su estado corporal "
                "(respiración, postura temperatura, acciones musculares, "
                "posiciones, otros) en movimiento y en reposo, durante la "
                "realización de prácticas corporales para mejorar la "
                "participación consciente."
            ),
            codigo="EF.5.5.1.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer a la competencia motriz propia como un estado de "
                "construcción constante que se aprende en relación con la "
                "conciencia corporal, el deseo y las experiencias con "
                "prácticas corporales individuales y con otros."
            ),
            codigo="EF.5.5.2.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer percepciones y sensaciones favorecedoras y "
                "obstaculizadoras del deseo de moverse (dolor, fatiga, "
                "entusiasmo, placer, entre otras), para tomar decisiones "
                "personales que colaboren con la participación sistemática "
                "en prácticas corporales."
            ),
            codigo="EF.5.5.3.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer el impacto de las representaciones sociales sobre "
                "el “lo femenino” y “lo masculino” en la constitución de la "
                "identidad corporal, para analizar críticamente sus sentidos "
                "y significados como facilitadores u obstaculizadores de la "
                "construcción de la competencia motriz."
            ),
            codigo="EF.5.5.4.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Reconocer la influencia de las percepciones de sí y de las "
                "demás personas sobre el propio desempeño, para analizarlas "
                "críticamente y construir posibilidades de participación."
            ),
            codigo="EF.5.5.5.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque5,
        ),
        Destreza(
            description=(
                "Analizar críticamente los vínculos entre los intereses y "
                "valores que portan los modelos estéticos hegemónicos y "
                "estereotipos de movimientos en relación a la singularidad "
                "de los sujetos y sus contextos."
            ),
            codigo="EF.5.5.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque5,
        ),
        # Bloque 6
        Destreza(
            description=(
                "Identificar las demandas de las prácticas corporales para "
                "mejorar la condición física de base y el logro de los "
                "objetivos personales."
            ),
            codigo="EF.5.6.1.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Comprender que las relaciones entre actividades físicas y "
                "salud no son directas, sino complejas, para asumir una "
                "actitud crítica y reflexiva sobre las maneras en que "
                "deberían realizarse para que las mismas sean saludables."
            ),
            codigo="EF.5.6.2.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer los beneficios que la actividad física puede "
                "aportar a su salud y su condición física, como un estado "
                "que puede mejorarse o deteriorarse en función del tipo y "
                "pertinencia de las actividades físicas y prácticas "
                "corporales que realiza."
            ),
            codigo="EF.5.6.3.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la importancia de las diferencias individuales "
                "durante la participación en diferentes prácticas "
                "corporales, para identificar las maneras más saludables de "
                "alcanzar objetivos personales."
            ),
            codigo="EF.5.6.4.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la importancia de los controles médicos previos y "
                "posteriores a la realización de prácticas corporales "
                "sistemáticas, como promotores de condiciones de "
                "participación responsable y saludable."
            ),
            codigo="EF.5.6.5.",
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Elaborar y poner en práctica planes básicos de trabajo "
                "propios, para mejorar la condición física de partida en "
                "función de los objetivos a alcanzar, los conocimientos "
                "sobre las actividades pertinentes para hacerlo y los "
                "cuidados a tener en cuenta para minimizar riesgos y "
                "optimizar resultados positivos."
            ),
            codigo="EF.5.6.6.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
        Destreza(
            description=(
                "Reconocer la importancia del cuidado personal, comunitario "
                "y ambiental (seguridad e higiene) antes, durante y luego de "
                "la realización de diferentes prácticas corporales, para "
                "favorecer que la participación sea segura, saludable y "
                "placentera."
            ),
            codigo="EF.5.6.7.",
            imprescindible=True,
            asignatura=educacion_fisica,
            subnivel=bachillerato,
            bloque=bloque6,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0038_auto_20180810_1553'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
