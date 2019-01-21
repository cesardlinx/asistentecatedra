from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    literatura = Asignatura.objects.get(name="Lengua y Literatura")

    # Bloques
    bloque1 = BloqueCurricular.objects.get(name="Lengua y cultura")
    bloque2 = BloqueCurricular.objects.get(name="Comunicación oral")
    bloque3 = BloqueCurricular.objects.get(name="Lectura")
    bloque4 = BloqueCurricular.objects.get(name="Escritura")
    bloque5 = BloqueCurricular.objects.get(name="Literatura")

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')

    Destreza.objects.bulk_create([
        # Preparatoria
        Destreza(
            description=(
                "Predecir el contenido y el uso de diversos textos escritos "
                "que se utilizan en actividades cotidianas del entorno "
                "escolar y familiar."
            ),
            codigo="LL.1.5.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reflexionar sobre la intención comunicativa que tienen "
                "diversos textos de uso cotidiano."
            ),
            codigo="LL.1.5.2.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Distinguir expresiones y tonos dialectales del habla "
                "castellana para interactuar con respeto y valorar la "
                "diversidad cultural del país."
            ),
            codigo="LL.1.5.3.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer palabras y expresiones de las lenguas originarias "
                "del Ecuador e indagar sobre sus significados."
            ),
            codigo="LL.1.5.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Desarrollar la expresión oral en contextos cotidianos "
                "usando la conciencia lingüística (semántica, léxica y "
                "sintáctica)."
            ),
            codigo="LL.1.5.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Adaptar el tono de voz, los gestos, la entonación y el "
                "vocabulario a diversas situaciones comunicativas, según el "
                "contexto y la intención."
            ),
            codigo="LL.1.5.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Acompañar el lenguaje oral, en situaciones de expresión "
                "creativa, utilizando recursos audiovisuales."
            ),
            codigo="LL.1.5.7.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Diferenciar entre imagen y texto escrito en diversos "
                "materiales impresos del entorno."
            ),
            codigo="LL.1.5.8.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Extraer información explícita que permita identificar "
                "elementos del texto, relacionarlos y darles sentido "
                "(personajes, escenarios, eventos, etc.)."
            ),
            codigo="LL.1.5.9.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Construir significados mediante el establecimiento de "
                "conexiones entre el contenido del texto y la experiencia "
                "personal."
            ),
            codigo="LL.1.5.10.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Elaborar significados de un texto mediante la activación de "
                "los conocimientos previos, comprobación o descarte de "
                "hipótesis, y predicción a partir del contenido y "
                "paratextos."
            ),
            codigo="LL.1.5.11.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Parafrasear y formular preguntas sobre el contenido del "
                "texto como parte del proceso de autorregular su "
                "comprensión."
            ),
            codigo="LL.1.5.12.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Acceder a la lectura por placer y para aprender, utilizando "
                "la biblioteca de aula y otros recursos."
            ),
            codigo="LL.1.5.13.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Satisfacer la curiosidad sobre temas de interés, utilizando "
                "la lectura como recurso de aprendizaje y registrar "
                "información consultada mediante dibujos y otros gráficos."
            ),
            codigo="LL.1.5.14.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Utiliza recursos digitales para satisfacer sus necesdades "
                "de ocio y aprendizaje."
            ),
            codigo="LL.1.5.15.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Explorar la formación de palabras y oraciones, utilizando "
                "la conciencia lingüística (fonológica, léxica y semántica)."
            ),
            codigo="LL.1.5.16.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Registrar, expresar y comunicar ideas, mediante sus propios "
                "códigos."
            ),
            codigo="LL.1.5.17.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Realizar sus producciones escritas mediante la selección y "
                "utilización de diferentes recursos y materiales."
            ),
            codigo="LL.1.5.18.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Mostrar interés por escribir, al reconocer que puede "
                "expresar por escrito, los sentimientos y las opiniones que "
                "le generan las diferentes situaciones cotidianas."
            ),
            codigo="LL.1.5.19.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Escuchar textos literarios con disfrute de las palabras y "
                "las ideas."
            ),
            codigo="LL.1.5.20.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Escuchar textos literarios para establecer relaciones entre "
                "el texto y el entorno personal."
            ),
            codigo="LL.1.5.21.",
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Representar pasajes de los textos literarios escuchados, "
                "utilizando sus propios códigos, dibujos y /o "
                "escenificaciones corporales."
            ),
            codigo="LL.1.5.22.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=preparatoria,
        ),
        # Elemental
        # Bloque 1
        Destreza(
            description=(
                "Distinguir la intención comunicativa (persuadir, expresar "
                "emociones, informar, requerir, etc.) que tienen diversos "
                "textos de uso cotidiano desde el análisis del propósito de "
                "su contenido."
            ),
            codigo="LL.2.1.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Emitir, con honestidad, opiniones valorativas sobre la "
                "utilidad de la información contenida en textos de uso "
                "cotidiano en diferentes situaciones comunicativas."
            ),
            codigo="LL.2.1.2.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer palabras y expresiones propias de las lenguas "
                "originarias y/o variedades lingüísticas del Ecuador, en "
                "diferentes tipos de textos de uso cotidiano, e indagar "
                "sobre sus significados en el contexto de la "
                "interculturalidad y de la pluriculturalidad."
            ),
            codigo="LL.2.1.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar sobre los dialectos del castellano en el país."
            ),
            codigo="LL.2.1.4.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Compartir de manera espontánea sus ideas, experiencias y "
                "necesidades en situaciones informales de la vida cotidiana."
            ),
            codigo="LL.2.2.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Dialogar con capacidad para escuchar, mantener el tema e "
                "intercambiar ideas en situaciones informales de la vida "
                "cotidiana."
            ),
            codigo="LL.2.2.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Usar las pautas básicas de la comunicación oral (turnos en "
                "la conversación, ceder la palabra, contacto visual, escucha "
                "activa) y emplear el vocabulario acorde con la situación "
                "comunicativa."
            ),
            codigo="LL.2.2.3.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reflexionar sobre la expresión oral con uso de la "
                "conciencia lingüística (léxica, semántica, sintáctica y "
                "fonológica) en contextos cotidianos."
            ),
            codigo="LL.2.2.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar exposiciones orales sobre temas de interés "
                "personal y grupal en el contexto escolar."
            ),
            codigo="LL.2.2.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Enriquecer sus presentaciones orales con la selección y "
                "adaptación de recursos audiovisuales y otros."
            ),
            codigo="LL.2.2.6.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Construir los significados de un texto a partir del "
                "establecimiento de relaciones de semejanza, diferencia, "
                "objeto-atributo, antecedente–consecuente, secuencia "
                "temporal, problema-solución, concepto-ejemplo."
            ),
            codigo="LL.2.3.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Comprender los contenidos implícitos de un texto basándose "
                "en inferencias espacio-temporales, referenciales y de "
                "causa-efecto."
            ),
            codigo="LL.2.3.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Ampliar la comprensión de un texto mediante la "
                "identificación de los significados de las palabras, "
                "utilizando las estrategias de derivación (familia de "
                "palabras), sinonimia–antonimia, contextualización, prefijos "
                "y sufijos y etimología."
            ),
            codigo="LL.2.3.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Comprender los contenidos explícitos e implícitos de un "
                "texto al registrar la información en tablas, gráficos, "
                "cuadros y otros organizadores gráficos sencillos."
            ),
            codigo="LL.2.3.4.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Desarrollar estrategias cognitivas como lectura de "
                "paratextos, establecimiento del propósito de lectura, "
                "relectura, relectura selectiva y parafraseo para "
                "autorregular la comprensión de textos."
            ),
            codigo="LL.2.3.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Construir criterios, opiniones y emitir juicios sobre el "
                "contenido de un texto al distinguir realidad y ficción, "
                "hechos, datos y opiniones."
            ),
            codigo="LL.2.3.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Enriquecer las ideas e indagar sobre temas de interés "
                "mediante la consulta de diccionarios, textos escolares, "
                "enciclopBedias y otros recursos de la biblioteca y la web."
            ),
            codigo="LL.2.3.7.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Aplicar los conocimientos lingüísticos (léxicos, "
                "semánticos, sintácticos y fonológicos) en la decodificación "
                "y comprensión de textos."
            ),
            codigo="LL.2.3.8.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Leer oralmente con fluidez y entonación en contextos "
                "significativos de aprendizaje."
            ),
            codigo="LL.2.3.9.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Leer de manera silenciosa y personal en situaciones de "
                "recreación, información y estudio."
            ),
            codigo="LL.2.3.10.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Elegir, de una selección previa realizada por el docente, "
                "textos de la biblioteca de aula, de la escuela y de la web "
                "que satisfagan sus necesidades personales, de recreación, "
                "información y aprendizaje."
            ),
            codigo="LL.2.3.11.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Desarrollar progresivamente autonomía y calidad en el "
                "proceso de escritura de relatos de experiencias personales, "
                "hechos cotidianos u otros sucesos, acontecimientos de "
                "interés y descripciones de objetos, animales, lugares y "
                "personas; aplicando la planificación en el proceso de "
                "escritura (con organizadores gráficos de acuerdo a la "
                "estructura del texto), teniendo en cuenta la conciencia "
                "lingüística (léxica, semántica, sintáctica y fonológica) en "
                "cada uno de sus pasos."
            ),
            codigo="LL.2.4.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Aplicar estrategias de pensamiento (ampliación de ideas, "
                "secuencia lógica, selección, ordenación y jerarquización de "
                "ideas, uso de organizadores gráficos, entre otras) en la "
                "escritura de relatos de experiencias personales, hechos "
                "cotidianos u otros sucesos y acontecimientos de interés, y "
                "en las descripciones de objetos, animales, lugares y "
                "personas, durante la autoevaluación de sus escritos."
            ),
            codigo="LL.2.4.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Redactar, en situaciones comunicativas que lo requieran, "
                "narraciones de experiencias personales, hechos cotidianos u "
                "otros sucesos o acontecimientos de interés, ordenándolos "
                "cronológicamente y enlazándolos por medio de conectores "
                "temporales y aditivos."
            ),
            codigo="LL.2.4.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Escribir descripciones de objetos, animales, lugares y "
                "personas; ordenando las ideas según una secuencia lógica, "
                "por temas y subtemas, por medio de conectores consecutivos, "
                "atributos, adjetivos calificativos y posesivos, en "
                "situaciones comunicativas que lo requieran."
            ),
            codigo="LL.2.4.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Utilizar diversos formatos, recursos y materiales, entre "
                "otras estrategias que apoyen la escritura de relatos de "
                "experiencias personales, hechos cotidianos u otros sucesos "
                "o acontecimientos de interés, y de descripciones de "
                "objetos, animales y lugares."
            ),
            codigo="LL.2.4.5.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Apoyar y enriquecer el proceso de escritura de sus relatos "
                "de experiencias personales y hechos cotidianos y de "
                "descripciones de objetos, animales y lugares, mediante "
                "paratextos, recursos TIC y la citación de fuentes."
            ),
            codigo="LL.2.4.6.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Aplicar progresivamente las reglas de escritura mediante la "
                "reflexión fonológica en la escritura ortográfica de fonemas "
                "que tienen dos y tres representaciones gráficas, la letra "
                "que representa los sonidos /ks/: “x”, la letra que no tiene "
                "sonido: “h” y la letra “w” que tiene escaso uso en "
                "castellano."
            ),
            codigo="LL.2.4.7.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Escuchar y leer diversos géneros literarios (privilegiando "
                "textos ecuatorianos, populares y de autor), para potenciar "
                "la imaginación, la curiosidad y la memoria."
            ),
            codigo="LL.2.5.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Escuchar y leer diversos géneros literarios (privilegiando "
                "textos ecuatorianos, populares y de autor), para "
                "desarrollar preferencias en el gusto literario y generar "
                "autonomía en la lectura."
            ),
            codigo="LL.2.5.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Recrear textos literarios con nuevas versiones de escenas, "
                "personajes u otros elementos."
            ),
            codigo="LL.2.5.3.",
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Explorar y motivar la escritura creativa al interactuar de "
                "manera lúdica con textos literarios leídos o escuchados "
                "(privilegiando textos ecuatorianos, populares y de autor)."
            ),
            codigo="LL.2.5.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Recrear textos literarios leídos o escuchados "
                "(privilegiando textos ecuatorianos, populares y de autor), "
                "con diversos medios y recursos (incluidas las TIC)."
            ),
            codigo="LL.2.5.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=elemental,
            bloque=bloque5
        ),
        # Media
        # Bloque 1
        Destreza(
            description=(
                "Participar en contextos y situaciones que evidencien la "
                "funcionalidad de la lengua escrita como herramienta "
                "cultural."
            ),
            codigo="LL.3.1.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar sobre las influencias lingüísticas y culturales que "
                "explican los dialectos del castellano en el Ecuador."
            ),
            codigo="LL.3.1.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar sobre las características de los pueblos y "
                "nacionalidades del Ecuador que tienen otras lenguas."
            ),
            codigo="LL.3.1.3.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Escuchar discursos orales y formular juicios de valor con "
                "respecto a su contenido y forma, y participar de manera "
                "respetuosa frente a las intervenciones de los demás."
            ),
            codigo="LL.3.2.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Proponer intervenciones orales con una intención "
                "comunicativa, organizar el discurso según las estructuras "
                "básicas de la lengua oral y utilizar un vocabulario "
                "adecuado a diversas situaciones comunicativas."
            ),
            codigo="LL.3.2.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Apoyar el discurso con recursos y producciones "
                "audiovisuales."
            ),
            codigo="LL.3.2.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reflexionar sobre los efectos del uso de estereotipos y "
                "prejuicios en la comunicación."
            ),
            codigo="LL.3.2.4.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Construir acuerdos en los intercambios orales que se "
                "establecen en torno a temas conflictivos."
            ),
            codigo="LL.3.2.5.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Establecer las relaciones explícitas entre los contenidos "
                "de dos o más textos, comparar y contrastar fuentes."
            ),
            codigo="LL.3.3.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Comprender los contenidos implícitos de un texto mediante "
                "la realización de inferencias fundamentales y "
                "proyectivo-valorativas a partir del contenido de un texto."
            ),
            codigo="LL.3.3.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Inferir y sintetizar el contenido esencial de un texto al "
                "diferenciar el tema de las ideas principales."
            ),
            codigo="LL.3.3.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Autorregular la comprensión de textos mediante el uso de "
                "estrategias cognitivas de comprensión: parafrasear, releer, "
                "formular preguntas, leer selectivamente, consultar fuentes "
                "adicionales."
            ),
            codigo="LL.3.3.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Valorar los aspectos de forma y el contenido de un texto, a "
                "partir de criterios preestablecidos."
            ),
            codigo="LL.3.3.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Acceder a bibliotecas y recursos digitales en la web, "
                "identificando las fuentes consultadas."
            ),
            codigo="LL.3.3.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Registrar la información consultada con el uso de esquemas "
                "de diverso tipo."
            ),
            codigo="LL.3.3.7.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Leer con fluidez y entonación en diversos contextos "
                "(familiares, escolares y sociales) y con diferentes "
                "propósitos (exponer, informar, narrar, compartir, etc.)."
            ),
            codigo="LL.3.3.8.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Generar criterios para el análisis de la confiabilidad de "
                "las fuentes consultadas."
            ),
            codigo="LL.3.3.9.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer el punto de vista del autor y las motivaciones y "
                "argumentos de un texto."
            ),
            codigo="LL.3.3.10.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Aplicar los conocimientos lingüísticos (léxicos, "
                "semánticos, sintácticos y fonológicos) en la decodificación "
                "y comprensión de textos."
            ),
            codigo="LL.3.3.11.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Relatar textos con secuencia lógica, manejo de conectores y "
                "coherencia en el uso de la persona y tiempo verbal, e "
                "integrarlos en diversas situaciones comunicativas."
            ),
            codigo="LL.3.4.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Escribir descripciones organizadas y con vocabulario "
                "específico relativo al ser, objeto, lugar o hecho que se "
                "describe e integrarlas en producciones escritas."
            ),
            codigo="LL.3.4.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Escribir exposiciones organizadas en párrafos según "
                "esquemas de comparación, problema-solución y antecedente "
                "con secuente, en las situaciones comunicativas que lo "
                "requieran."
            ),
            codigo="LL.3.4.3.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Escribir instrucciones con secuencia lógica, uso de "
                "conectores temporales y de orden, y coherencia en el manejo "
                "del verbo y la persona, en situaciones comunicativas que lo "
                "requieran."
            ),
            codigo="LL.3.4.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Integrar relatos, descripciones, exposiciones e "
                "instrucciones en diferentes tipos de texto producidos con "
                "una intención comunicativa y en un contexto determinado."
            ),
            codigo="LL.3.4.5.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Autorregular la producción escrita mediante el uso habitual "
                "del procedimiento de planificación, redacción y revisión "
                "del texto."
            ),
            codigo="LL.3.4.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Usar estrategias y procesos de pensamiento que apoyen la "
                "escritura."
            ),
            codigo="LL.3.4.7.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Lograr precisión y claridad en sus producciones escritas, "
                "mediante el uso de vocabulario según un determinado campo "
                "semántico."
            ),
            codigo="LL.3.4.8.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Organizar las ideas con unidad de sentido a partir de la "
                "construcción de párrafos."
            ),
            codigo="LL.3.4.9.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Expresar sus ideas con precisión e integrar en las "
                "producciones escritas los diferentes tipos de sustantivo, "
                "pronombre, adjetivo, verbo, adverbio y sus modificadores."
            ),
            codigo="LL.3.4.10.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Mejorar la cohesión interna del párrafo y la organización "
                "del texto mediante el uso de conectores lógicos."
            ),
            codigo="LL.3.4.11.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Comunicar ideas con eficiencia a partir de la aplicación de "
                "las reglas de uso de las letras y de la tilde."
            ),
            codigo="LL.3.4.12.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Producir escritos de acuerdo con la situación comunicativa, "
                "mediante el empleo de diversos formatos, recursos y "
                "materiales."
            ),
            codigo="LL.3.4.13.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Apoyar el proceso de escritura colaborativa e individual "
                "mediante el uso de diversos recursos de las TIC."
            ),
            codigo="LL.3.4.14.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Reconocer en un texto literario los elementos "
                "característicos que le dan sentido."
            ),
            codigo="LL.3.5.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Participar en discusiones sobre textos literarios con el "
                "aporte de información, experiencias y opiniones para "
                "desarrollar progresivamente la lectura crítica."
            ),
            codigo="LL.3.5.2.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Elegir lecturas basándose en preferencias personales de "
                "autor, género o temas y el manejo de diversos soportes para "
                "formarse como lector autónomo."
            ),
            codigo="LL.3.5.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Incorporar los recursos del lenguaje figurado en sus "
                "ejercicios de creación literaria."
            ),
            codigo="LL.3.5.4.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Reinventar los textos literarios y relacionarlos con el "
                "contexto cultural propio y de otros entornos."
            ),
            codigo="LL.3.5.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Recrear textos literarios leídos o escuchados mediante el "
                "uso de diversos medios y recursos (incluidas las TIC)."
            ),
            codigo="LL.3.5.6.",
            asignatura=literatura,
            subnivel=media,
            bloque=bloque5
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0039_auto_20180812_1723'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
