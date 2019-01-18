from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignatura
    educacion_fisica = Asignatura.objects.get(name='Educación Física')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    CriterioEvaluacion.objects.bulk_create([
        # Preparatoria
        CriterioEvaluacion(
            description=(
                "Construye y comunica mensajes expresivos(convencionales y/o "
                "espontáneos) utilizando gestos, ritmos, posturas, tipos de "
                "movimiento reconociendo sus estados de ánimo y sus "
                "posibilidades de creación, expresión, interpretación y "
                "traducción de mensajes corporales propios y de pares, a "
                "otros lenguajes establece acuerdos colectivos(de seguridad "
                "de respeto a diferentes formas de expresión, entre otros) "
                "que favorezcan la participación en prácticas corporales "
                "expresivo-comunicativas."
            ),
            codigo="CE.EF.1.1.",
            asignatura=educacion_fisica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Experimenta las mejores maneras de practicar habilidades "
                "motrices básicas, destrezas y acrobacias, a partir de "
                "identificar cómo las realiza, las diferencias entre las "
                "mismas, la implicancia de las partes, posiciones, "
                "posibilidades de movimiento del cuerpo, sus estados "
                "corporales, sus ritmos internos, sus capacidades motoras y "
                "su disposición para autosuperarse, realizando los acuerdos "
                "necesarios para el cuidado de sí mismo y de sus pares "
                "(seguridad e higiene)."
            ),
            codigo="CE.EF.1.2.",
            asignatura=educacion_fisica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Construye y comunica mensajes expresivos(convencionales y/o "
                "espontáneos), utilizando gestos, ritmos, posturas, tipos de "
                "movimiento en el tiempo y el espacio, reconociendo sus "
                "ritmos internos, sus estados corporales y de ánimo y sus "
                "posibilidades de creación, expresión, interpretación y "
                "traducción de mensajes corporales propios y de pares a "
                "otros lenguajes, estableciendo acuerdos colectivos(de "
                "seguridad e higiene individual, colectiva y del ambiente de "
                "aprendizaje, de respeto a diferentes formas de expresión, "
                "entre otros) que favorezcan la participación en prácticas "
                "corporales expresivo-comunicativas."
            ),
            codigo="CE.EF.1.3.",
            asignatura=educacion_fisica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Participa en diferentes prácticas corporales tomando "
                "decisiones sobre sus modos de intervención, a partir del "
                "reconocimiento de sus estados corporales y ritmos internos "
                "en reposo y durante la acción, su ubicación en el tiempo y "
                "el espacio de manera estática y dinámica, las "
                "características y posibilidades de movimiento de sus partes "
                "y segmentos corporales."
            ),
            codigo="CE.EF.1.4.",
            asignatura=educacion_fisica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Comprende la necesidad de cuidar de sí mismo y del ambiente "
                "de aprendizaje antes, durante y después de su participación "
                "en diferentes prácticas corporales."
            ),
            codigo="CE.EF.1.5.",
            asignatura=educacion_fisica,
            subnivel=preparatoria
        ),
        # Elemental
        CriterioEvaluacion(
            description=(
                "Participa colectivamente y de modo seguro en juegos propios "
                "de la región, identificando características, objetivos, "
                "roles de los participantes y demandas(motoras, "
                "conceptuales, actitudinales, implementos, entre otras) que "
                "le permitan agruparlos en categorías y mejorar su "
                "desempeño, construyendo cooperativa y colaborativamente "
                "posibilidades de participación."
            ),
            codigo="CE.EF.2.1.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Participa con pares en diferentes juegos identificando "
                "características, objetivos, reglas, demandas de los juegos, "
                "posibles situaciones de riesgo, la condición y disposición "
                "personal, la necesidad de construir y acordar pautas de "
                "seguridad, juego y cooperación necesarios, según el "
                "ambiente/contexto en que los practica y la necesidad de "
                "respetarlos para cuidar de sí, de sus pares y de su "
                "entorno, y así poder disfrutarlos."
            ),
            codigo="CE.EF.2.2.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Reconoce diferentes tipos de acrobacias, destrezas y "
                "habilidades motrices básicas individuales y grupales, y las "
                "realiza percibiendo las acciones motrices que necesita "
                "mejorar y las diversas posiciones que adopta su cuerpo en "
                "el tiempo y el espacio, reconociendo sus condiciones y "
                "disposiciones en vínculo con la práctica e identificando "
                "los posibles riesgos durante la realización de las mismas, "
                "y construyendo con pares la confianza necesaria para "
                "participar de manera segura en la construcción de "
                "combinaciones gimnásticas."
            ),
            codigo="CE.EF.2.3.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Realiza de manera segura y saludable posiciones invertidas, "
                "destrezas y acrobacias individuales y grupales, "
                "identificando las posiciones, apoyos, contracciones, "
                "relajaciones, contactos del cuerpo, las articulaciones y el "
                "predominio de diferentes capacidades motoras(coordinativas "
                "y condicionales) que participan cuando se trabajan en "
                "diferentes situaciones."
            ),
            codigo="CE.EF.2.4.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Construye colectivamente composiciones "
                "expresivo-comunicativas en un ambiente seguro y de "
                "confianza, ajustando rítmicamente las posibilidades "
                "expresivas de sus movimientos, reconociendo estados "
                "corporales y ritmos internos, y empleando los recursos "
                "expresivos(estados de ánimo, emociones, sensaciones, "
                "posibilidades expresivas de los movimientos, otros) "
                "adecuados al mensaje que se desea comunicar."
            ),
            codigo="CE.EF.2.5.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Participa individual y colectivamente en diversas prácticas "
                "corporales expresivo-comunicativas(danzas, circos, "
                "teatralizaciones, carnavales, otras) propias de la región, "
                "reconociendo y valorando los sentidos identitarios y de "
                "pertencia cultural que los contextos le otorgan a las "
                "mismas, construyendo con pares diferentes posibilidades de "
                "participación."
            ),
            codigo="CE.EF.2.6.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Participa en diferentes prácticas corporales regulando sus "
                "acciones motrices, a partir de la percepción de sus "
                "músculos y articulaciones(formas y posibilidades de "
                "movimiento), las diferentes posiciones que su cuerpo adopta "
                "en el tiempo y el espacio, sus ritmos internos y estados "
                "corporales, en función de las demandas y objetivos de las "
                "prácticas corporales."
            ),
            codigo="CE.EF.2.7.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Construye diversas posibilidades de participación colectiva "
                "en las prácticas corporales, reconociendo sus condiciones y "
                "disposiciones y colaborando con sus pares."
            ),
            codigo="CE.EF.2.8.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Participa en prácticas corporales de forma segura, "
                "reconociendo posturas favorables, adecuadas y menos lesivas "
                "en función de las características del propio cuerpo, "
                "maneras saludables y beneficiosas de realizarlas, e "
                "identificando riesgos y acordando los cuidados necesarios "
                "para consigo, las demás personas y el entorno."
            ),
            codigo="CE.EF.2.9.",
            asignatura=educacion_fisica,
            subnivel=elemental
        ),
        # Media
        CriterioEvaluacion(
            description=(
                "Participa y/o juega de manera segura y democrática con sus "
                "pares en diferentes juegos(creados, de diferentes regiones, "
                "entre otros), reconociéndolos como producciones de la "
                "cultura(propia y de otras), identificando sus "
                "características, objetivos y proveniencias y acordando, "
                "respetando y modificando las reglas según sus intereses y "
                "necesidades."
            ),
            codigo="CE.EF.3.1.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Construye con pares y trabajando en equipo diferentes "
                "posibilidades de participación que mejoren de manera segura "
                "su desempeño y posibiliten el logro del objetivo en "
                "diversos juegos, a partir del reconocimiento de sus "
                "experiencias corporales, su propio desempeño(posibilidades "
                "y dificultades), la importancia del cuidado de sí y de las "
                "demás personas, y la diferencia entre juegos y deportes, "
                "teniendo en cuenta objetivos, características, reglas, "
                "demandas, roles de los participantes y situaciones de "
                "juego."
            ),
            codigo="CE.EF.3.2.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Construye individual y colectivamente secuencias "
                "gimnásticas, identificando sus experiencias previas, "
                "realizando el acondicionamiento corporal necesario, "
                "ejecutando diferentes variantes de destrezas y acrobacias, "
                "percibiendo el uso del tiempo y el espacio, las capacidades "
                "motoras a mejorar y realizando los acuerdos de seguridad, "
                "confianza y trabajo en equipo necesarios."
            ),
            codigo="CE.EF.3.3.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Construye individual y colectivamente composiciones "
                "expresivo-comunicativas de manera segura y colaborativa, "
                "reconociendo y valorando el aporte cultural de diversas "
                "manifestaciones expresivas de la propia región y de otras "
                "regiones a la riqueza nacional, utilizando y compartiendo "
                "con pares diferentes recursos(emociones, sensaciones, "
                "estados de ánimo, movimientos, experiencias previas, otros) "
                "y ajustando rítmicamente(al ritmo musical y de pares) la "
                "intencionalidad expresiva de sus movimientos, durante la "
                "interpretación de mensajes escénicos y/o historias reales o "
                "ficticias ante diferentes públicos."
            ),
            codigo="CE.EF.3.4.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Participa y/o juega de manera segura con sus pares en "
                "diferentes juegos de iniciación deportiva(modificados, "
                "atléticos, entre otros), realizando el acondicionamiento "
                "corporal necesario y construyendo espacios de confianza "
                "colectivos que permitan la creación de diferentes "
                "respuestas técnicas(facilidades y dificultades propias), "
                "tácticas(intenciones en ataque y defensa) y estratégicas a "
                "partir de la identificación de sus lógicas, "
                "características, objetivos, demandas y condición física de "
                "partida acordando, respetando y modificando las reglas "
                "según sus intereses y necesidades y estableciendo "
                "diferencias y similitudes con los deportes y sus "
                "características."

            ),
            codigo="CE.EF.3.5.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Construye conocimiento/s sobre su cuerpo, sus posibilidades "
                "de acción(contracción, relajación muscular y posibilidades "
                "de movimientos articulares) y cómo mejorarlas, analizando "
                "la influencia de sus experiencias corporales, los efectos "
                "de las representaciones sociales(propias y del entorno) "
                "sobre las prácticas corporales, reconociendo las "
                "facilidades y dificultades propias y la importancia de "
                "construir espacios de confianza colectivos durante su "
                "proceso de aprendizaje."
            ),
            codigo="CE.EF.3.6.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Mejora su desempeño en diferentes prácticas corporales de "
                "manera segura, saludable y placentera, identificando "
                "dificultades propias y de sus pares, reconociendo su "
                "condición física de partida y realizando acondicionamiento "
                "corporal necesario, en relación a los objetivos y demandas "
                "de la práctica."
            ),
            codigo="CE.EF.3.7.",
            asignatura=educacion_fisica,
            subnivel=media
        ),
        # Superior
        CriterioEvaluacion(
            description=(
                "Participa en diferentes categorías de juegos "
                "(tradicionales, populares, modificados, masivos, "
                "expresivos, con elementos, en el medio natural, entre "
                "otros), mejorando sus posibilidades y las de sus pares de "
                "alcanzar los objetivos, a partir del reconocimiento de "
                "lógicas, características básicas, orígenes, demandas "
                "(motoras, intelectuales, emocionales, sociales), influencia "
                "de etiquetas sociales, conocimientos corporales necesarios "
                "y posibles riesgos, construyendo individual y "
                "colectivamente estrategias, materiales y espacios seguros "
                "de juego."
            ),
            codigo="CE.EF.4.1.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Crea y recrea diferentes juegos (individuales, colectivos, "
                "con elementos, sin elementos, de persecución, cooperativos, "
                "entre otros) individual y colectivamente de manera segura, "
                "estableciendo objetivos, construyendo tácticas y "
                "estrategias en función de las demandas (motoras, "
                "intelectuales, emocionales, sociales) que cada juego le "
                "presenta, y de las diferentes posibilidades de acción de "
                "los participantes, asumiendo diferentes roles de juego "
                "antes y durante su participación en los mismos."
            ),
            codigo="CE.EF.4.2.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Construye grupalmente de manera segura, eficaz y placentera "
                "composiciones y coreografías gimnásticas (con y sin "
                "elementos), identificando su competencia motríz y su "
                "condición física de partida, practicando con diferentes "
                "niveles de dificultad la utilización de elementos y "
                "desplazamientos gimnásticos diferenciando ejercicios "
                "construidos de habilidades motrices básicas y transfiriendo "
                "ejercicios, destrezas y acrobacias gimnásticas a otras "
                "prácticas corporales."
            ),
            codigo="CE.EF.4.3.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Crea y recrea diferentes prácticas corporales "
                "expresivo-comunicativas en escenarios individuales y "
                "grupales, expresando y comunicando percepciones, "
                "sensaciones y estados de ánimo, utilizando diversos "
                "recursos en la construcción escénica, reconociendo los "
                "sentidos y contextos de origen de diversas prácticas "
                "expresivo-comunicativas e identificando los elementos "
                "favorecedores y obstaculizadores de su participación en las "
                "mismas."
            ),
            codigo="CE.EF.4.4.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Construye espacios escénicos individuales y grupales, "
                "empleando diferentes recursos expresivos (percepciones, "
                "sensaciones, estados de ánimo, música, vestuarios, entre "
                "otras), identificando las posibilidades que ofrecen la "
                "improvisación, el ensayo, las coreografías y composiciones, "
                "y valorando la importancia de confiar, respetar y cuidar de "
                "sí mismo y de sus pares antes, durante y después de "
                "expresar y comunicar mensajes ante diversos públicos."
            ),
            codigo="CE.EF.4.5.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Participa de manera colaborativa y segura en diversas "
                "prácticas deportivas, identificando las características que "
                "las diferencian de los juegos(reglas, lógicas, objetivos, "
                "entre otros), reconociendo la necesidad del trabajo en "
                "equipo y el juego limpio, y construyendo las mejores formas "
                "individuales y colectivas de resolver las situaciones "
                "problemas que se presentan, mediante el uso de diferentes "
                "técnicas, tácticas y estrategias individuales y colectivas."
            ),
            codigo="CE.EF.4.6.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Participa en diferentes prácticas corporales de manera "
                "segura, identificando las razones que le permiten "
                "elegirlas(sentidos, facilidades, obstáculos y concepciones "
                "culturales en la construcción de su identidad corporal, el "
                "cuerpo como organismo biológico y/o construcción social, "
                "etiquetas sociales, entre otras), reconociendo su "
                "competencia motriz en interacción con otras personas y la "
                "necesidad de valorar y respetar las diferencias sociales y "
                "personales."
            ),
            codigo="CE.EF.4.7.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Participa en diferentes prácticas corporales, comprendiendo "
                "la relación entre la actividad corporal confortable y "
                "placentera con la vida activa y el bienestar/salud "
                "personal/ambiental, reconociendo las ejercitaciones y "
                "conocimientos (corporales y de la práctica) necesarios en "
                "el logro de los objetivos personales, examinando los "
                "cambios y malestares corporales, identificando posibles "
                "beneficios y riesgos producidos durante y después de la "
                "realización de diferentes prácticas corporales."
            ),
            codigo="CE.EF.4.8.",
            asignatura=educacion_fisica,
            subnivel=superior
        ),
        # Bachillerato
        CriterioEvaluacion(
            description=(
                "Participa en diferentes juegos reconociéndolos como "
                "manifestaciones sociales, históricas y culturales con "
                "impacto en las dimensiones social, motriz, afectiva y "
                "cognitiva del sujeto, según el contexto de origen de la "
                "práctica, construyendo diversas estrategias y tácticas "
                "colectivas, a partir de la identificación de los "
                "requerimientos, su competencia motriz, las diferencias "
                "entre los participantes, la importancia de la comunicación, "
                "la cooperación, las potencialidades, dificultades y valores "
                "del trabajo en equipo, transfiriendo estos conocimientos a "
                "acciones cotidianas."
            ),
            codigo="CE.EF.5.1.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Participa en prácticas gimnásticas sistemáticas, "
                "diferenciándolas de las deportivas, partiendo de la "
                "identificación de las demandas de la práctica y la "
                "construcción de ejercicios básicos, que mejoren de manera "
                "saludable su condición física, su dominio corporal, el "
                "manejo de objetos, su respiración y postura y le permitan "
                "alcanzar sus objetivos."
            ),
            codigo="CE.EF.5.2.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Produce creaciones escénicas combinando diferentes "
                "prácticas corporales expresivo-comunicativas (acrobacias, "
                "danzas, teatro, gimnasia, entre otras), a partir de la "
                "identificación de sus requerimientos (motores, emocionales, "
                "cognitivos, entre otros), reconociéndolas como producciones "
                "socioculturales valiosas para diversos contextos, con "
                "sentido para las personas que las practican."
            ),
            codigo="CE.EF.5.3.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Construye como protagonista y/o espectador espacios de "
                "trabajo colectivo respetuosos, que favorezcan la creación "
                "de nuevas formas de danzar a partir del reconocimiento de "
                "las características de diferentes danzas "
                "convencionales(pasos básicos, coreografías, etc.) y la "
                "utilización de acciones y secuencias con intencionalidad "
                "expresiva."
            ),
            codigo="CE.EF.5.4.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Participa en diferentes prácticas deportivas, de manera "
                "segura, eficaz y colaborativa, comprendiendo las "
                "posibilidades de acción que permiten los reglamentos, "
                "realizando los ajustes individuales, colectivos y "
                "contextuales (técnicos, tácticos, estratégicos y "
                "corporales) necesarios en el trabajo de equipo para lograr "
                "los objetivos, identificando la lógica interna, valorando "
                "el juego limpio y percibiendo las sensaciones que favorecen "
                "u obstaculizan su desempeño y participación dentro y fuera "
                "de la institución educativa."
            ),
            codigo="CE.EF.5.5.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Percibe y toma conciencia sobre su competencia motriz, su "
                "estado corporal en movimiento y/o en reposo, las "
                "sensaciones y percepciones ligadas al deseo de moverse y a "
                "la decisión de mejorar su participación consciente en "
                "prácticas corporales individuales y con otras personas."
            ),
            codigo="CE.EF.5.6.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza el impacto que producen las etiquetas sociales, los "
                "modelos estéticos, los movimientos estereotipados y los "
                "sentidos sociales de lo “femenino” y “masculino” en la "
                "construcción de la identidad corporal, la competencia "
                "motriz, la singularidad de los sujetos, su deseo y su "
                "potencial de moverse."
            ),
            codigo="CE.EF.5.7.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Realiza diferentes prácticas corporales, comprendiendo las "
                "relaciones complejas entre ellas y la salud, reconociendo "
                "las demandas, los objetivos a alcanzar, la importancia del "
                "cuidado personal, comunitario y ambiental y los beneficios "
                "de realizarlas de manera pertinente."
            ),
            codigo="CE.EF.5.8.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Participa en diferentes prácticas corporales de manera "
                "sistemática, saludable y reflexiva, construyendo planes de "
                "trabajo pertinentes y reconociendo la importancia de las "
                "diferencias individuales y de los controles médicos (dentro "
                "y fuera del colegio)."
            ),
            codigo="CE.EF.5.9.",
            asignatura=educacion_fisica,
            subnivel=bachillerato
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0026_auto_20180808_1049'),
    ]

    operations = [
        migrations.RunPython(create_criterios)
    ]
