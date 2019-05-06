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
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Superior
        # Bloque 1
        Destreza(
            description=(
                "Indagar y explicar los aportes de la cultura escrita al "
                "desarrollo histórico, social y cultural de la humanidad."
            ),
            codigo="LL.4.1.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Valorar la diversidad cultural del mundo expresada en "
                "textos escritos representativos de las diferentes culturas, "
                "en diversas épocas históricas."
            ),
            codigo="LL.4.1.2.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar sobre las variaciones lingüísticas socioculturales "
                "del Ecuador y explicar su influencia en las relaciones "
                "sociales."
            ),
            codigo="LL.4.1.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar y explicar la influencia de la estructura de la "
                "lengua en las formas de pensar y actuar de las personas."
            ),
            codigo="LL.4.1.4.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Utilizar recursos de la comunicación oral en contextos de "
                "intercambio social, construcción de acuerdos y resolución "
                "de problemas."
            ),
            codigo="LL.4.2.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Organizar el discurso mediante el uso de las estructuras "
                "básicas de la lengua oral, la selección y empleo de "
                "vocabulario específico, acorde con la intencionalidad, en "
                "diversos contextos comunicativos formales e informales."
            ),
            codigo="LL.4.2.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Producir discursos que integren una variedad de recursos, "
                "formatos y soportes."
            ),
            codigo="LL.4.2.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reflexionar sobre los efectos del uso de estereotipos y "
                "prejuicios en la comunicación."
            ),
            codigo="LL.4.2.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar, de manera selectiva y crítica, los recursos del "
                "discurso oral y evaluar su impacto en la audiencia."
            ),
            codigo="LL.4.2.5.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Valorar el contenido explícito de dos o más textos orales e "
                "identificar contradicciones, ambigüedades, falacias, "
                "distorsiones y desviaciones en el discurso."
            ),
            codigo="LL.4.2.6.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Comparar, bajo criterios preestablecidos, las relaciones "
                "explícitas entre los contenidos de dos o más textos y "
                "contrastar sus fuentes."
            ),
            codigo="LL.4.3.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Construir significados implícitos al inferir el tema, el "
                "punto de vista del autor, las motivaciones y argumentos de "
                "un texto."
            ),
            codigo="LL.4.3.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Elaborar criterios crítico-valorativos al distinguir las "
                "diferentes perspectivas en conflicto sobre un mismo tema, "
                "en diferentes textos."
            ),
            codigo="LL.4.3.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Autorregular la comprensión de un texto mediante la "
                "aplicación de estrategias cognitivas de comprensión "
                "autoseleccionadas, de acuerdo con el propósito de lectura y "
                "las dificultades identificadas."
            ),
            codigo="LL.4.3.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Valorar y comparar textos de consulta en función del "
                "propósito de lectura y la calidad de la información "
                "(claridad, organización, actualización, amplitud, "
                "profundidad y otros)."
            ),
            codigo="LL.4.3.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Consultar bibliotecas y recursos digitales en la web, con "
                "capacidad para analizar la confiabilidad de la fuente."
            ),
            codigo="LL.4.3.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Recoger, comparar y organizar información consultada en "
                "esquemas de diverso tipo."
            ),
            codigo="LL.4.3.7.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Valorar el contenido implícito de un texto en contraste con "
                "fuentes adicionales."
            ),
            codigo="LL.4.3.8.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Valorar el contenido explícito de un texto al identificar "
                "contradicciones y ambigüedades."
            ),
            codigo="LL.4.3.9.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Consultar bases de datos digitales y otros recursos de la "
                "web, con capacidad para seleccionar fuentes según el "
                "propósito de lectura, y valorar la confiabilidad e interés "
                "o punto de vista de las fuentes escogidas."
            ),
            codigo="LL.4.3.10.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Escribir textos periodísticos y académicos con manejo de su "
                "estructura básica, y sustentar las ideas con razones y "
                "ejemplos organizados de manera jerárquica."
            ),
            codigo="LL.4.4.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Lograr cohesión y coherencia en la escritura de textos "
                "periodísticos y académicos mediante la construcción y "
                "organización de diferentes tipos de párrafo."
            ),
            codigo="LL.4.4.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Usar estrategias y procesos de pensamiento que apoyen la "
                "escritura de diferentes tipos de textos periodísticos y "
                "académicos."
            ),
            codigo="LL.4.4.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Autorregular la escritura de textos periodísticos y "
                "académicos con la selección y aplicación de variadas "
                "técnicas y recursos."
            ),
            codigo="LL.4.4.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Usar el procedimiento de planificación, redacción y "
                "revisión en la escritura de diferentes tipos de textos "
                "periodísticos y académicos."
            ),
            codigo="LL.4.4.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Mejorar la claridad y precisión de diferentes tipos de "
                "textos periodísticos y académicos mediante la escritura de "
                "oraciones compuestas y la utilización de nexos, "
                "modificadores, objetos, complementos y signos de "
                "puntuación."
            ),
            codigo="LL.4.4.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Matizar y precisar las ideas y los significados de "
                "oraciones y párrafos mediante el uso selectivo de modos "
                "verbales, tiempos verbales complejos, verboides, voz activa "
                "y pasiva, conjunciones y frases nominales, adjetivas, "
                "adverbiales, preposicionales y verbales."
            ),
            codigo="LL.4.4.7.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Comunicar ideas con eficiencia aplicando, de manera "
                "autónoma, las reglas de uso de las letras, de la puntuación "
                "y de la tilde."
            ),
            codigo="LL.4.4.8.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Escribir diálogos directos e indirectos e integrarlos en "
                "diferentes tipos de texto, según la intención comunicativa."
            ),
            codigo="LL.4.4.9.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Manejar las normas de citación e identificación de fuentes "
                "más utilizadas."
            ),
            codigo="LL.4.4.10.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Usar recursos de las TIC para apoyar el proceso de "
                "escritura colaborativa e individual."
            ),
            codigo="LL.4.4.11.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Interpretar un texto literario desde las características "
                "del género al que pertenece."
            ),
            codigo="LL.4.5.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Debatir críticamente la interpretación de un texto "
                "literario basándose en indagaciones sobre el tema, género y "
                "contexto."
            ),
            codigo="LL.4.5.2.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Elegir lecturas basándose en preferencias personales de "
                "autor, género, estilo, temas y contextos socioculturales, "
                "con el manejo de diversos soportes."
            ),
            codigo="LL.4.5.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Componer textos creativos que adapten o combinen diversas "
                "estructuras y recursos literarios."
            ),
            codigo="LL.4.5.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Expresar intenciones determinadas (ironía, sarcasmo, humor, "
                "etc.) con el uso creativo del significado de las palabras."
            ),
            codigo="LL.4.5.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Recrear textos literarios leídos o escuchados con el uso "
                "colaborativo de diversos medios y recursos de las TIC."
            ),
            codigo="LL.4.5.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Recrear textos literarios leídos o escuchados desde la "
                "experiencia personal, adaptando diversos recursos "
                "literarios."
            ),
            codigo="LL.4.5.7.",
            asignatura=literatura,
            subnivel=superior,
            bloque=bloque5
        ),
        # Bachillerato
        # Bloque 1
        Destreza(
            description=(
                "Indagar sobre las transformaciones y las tendencias "
                "actuales y futuras de la evolución de la cultura escrita en "
                "la era digital."
            ),
            codigo="LL.5.1.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar las implicaciones socioculturales de la "
                "producción y el consumo de cultura digital."
            ),
            codigo="LL.5.1.2.",
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar las causas de la diglosia en relación con las "
                "lenguas originarias y sus consecuencias en el ámbito "
                "educativo, la identidad, los derechos colectivos y la vida "
                "cotidiana."
            ),
            codigo="LL.5.1.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar críticamente las variaciones lingüísticas "
                "socioculturales del Ecuador desde diversas perspectivas."
            ),
            codigo="LL.5.1.4.",
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Valorar el contenido explícito de dos o más textos orales e "
                "identificar contradicciones, ambigüedades, falacias, "
                "distorsiones y desviaciones en el discurso."
            ),
            codigo="LL.5.2.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Valorar el contenido implícito de un texto oral a partir "
                "del análisis connotativo del discurso."
            ),
            codigo="LL.5.2.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar los diferentes formatos y registros de la "
                "comunicación oral para persuadir mediante la argumentación "
                "y contraargumentación, con dominio de las estructuras "
                "lingüísticas."
            ),
            codigo="LL.5.2.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar de manera selectiva y crítica los recursos del "
                "discurso oral y evaluar su impacto en la audiencia."
            ),
            codigo="LL.5.2.4.",
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Valorar el contenido explícito de dos o más textos al "
                "identificar contradicciones, ambigüedades y falacias."
            ),
            codigo="LL.5.3.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Valorar el contenido implícito de un texto con argumentos "
                "propios, al contrastarlo con fuentes adicionales."
            ),
            codigo="LL.5.3.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Autorregular la comprensión de un texto mediante la "
                "aplicación de estrategias cognitivas y metacognitivas de "
                "comprensión."
            ),
            codigo="LL.5.3.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Valorar los aspectos formales y el contenido del texto en "
                "función del propósito comunicativo, el contexto "
                "sociocultural y el punto de vista del autor."
            ),
            codigo="LL.5.3.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Consultar bases de datos digitales y otros recursos de la "
                "web con capacidad para seleccionar fuentes según el "
                "propósito de lectura y valorar la confiabilidad e interés o "
                "punto de vista de las fuentes escogidas."
            ),
            codigo="LL.5.3.5.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Recoger, comparar y organizar información consultada "
                "utilizando esquemas y estrategias personales."
            ),
            codigo="LL.5.3.6.",
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Construir un texto argumentativo, seleccionando el tema y "
                "formulando la tesis."
            ),
            codigo="LL.5.4.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Defender una tesis mediante la formulación de diferentes "
                "tipos de argumento."
            ),
            codigo="LL.5.4.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Aplicar las normas de citación e identificación de fuentes "
                "con rigor y honestidad académica."
            ),
            codigo="LL.5.4.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Usar de forma habitual el procedimiento de planificación, "
                "redacción y revisión para autorregular la producción "
                "escrita, y seleccionar y aplicar variadas técnicas y "
                "recursos."
            ),
            codigo="LL.5.4.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Producir textos mediante el uso de diferentes soportes "
                "impresos y digitales."
            ),
            codigo="LL.5.4.5.",
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Expresar su postura u opinión sobre diferentes temas de la "
                "cotidianidad y académicos, mediante el uso crítico del "
                "significado de las palabras."
            ),
            codigo="LL.5.4.6.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Desarrollar un tema con coherencia, cohesión y precisión, y "
                "en diferentes tipos de párrafos."
            ),
            codigo="LL.5.4.7.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Expresar matices y producir efectos determinados en los "
                "lectores, mediante la selección de un vocabulario preciso."
            ),
            codigo="LL.5.4.8.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Ubicar cronológicamente los textos más representativos de "
                "la literatura de Grecia y Roma, y examinar críticamente las "
                "bases de la cultura occidental."
            ),
            codigo="LL.5.5.1.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Ubicar cronológicamente los textos más representativos de "
                "la literatura latinoamericana: siglos XIX a XXI, y "
                "establecer sus aportes en los procesos de reconocimiento y "
                "visibilización de la heterogeneidad cultural."
            ),
            codigo="LL.5.5.2.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Ubicar cronológicamente los textos más representativos de "
                "la literatura ecuatoriana: siglos XIX a XXI, y establecer "
                "sus aportes en la construcción de una cultura diversa y "
                "plural."
            ),
            codigo="LL.5.5.3.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Recrear los textos literarios leídos desde la experiencia "
                "personal, mediante la adaptación de diversos recursos "
                "literarios."
            ),
            codigo="LL.5.5.4.",
            imprescindible=True,
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Experimentar la escritura creativa con diferentes "
                "estructuras literarias, lingüísticas, visuales y sonoras en "
                "la recreación de textos literarios."
            ),
            codigo="LL.5.5.5.",
            asignatura=literatura,
            subnivel=bachillerato,
            bloque=bloque5
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0040_auto_20180813_1041'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
