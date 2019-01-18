from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.4.")
    criterio1_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.5.")
    criterio1_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.6.")
    criterio1_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.1.7.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.6.")
    criterio2_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.7.")
    criterio2_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.8.")
    criterio2_9 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.9.")
    criterio2_10 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.10.")
    criterio2_11 = CriterioEvaluacion.objects.get(codigo="CE.LL.2.11.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.3.8.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.8.")
    criterio4_9 = CriterioEvaluacion.objects.get(codigo="CE.LL.4.9.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.4.")
    criterio5_5 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.5.")
    criterio5_6 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.6.")
    criterio5_7 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.7.")
    criterio5_8 = CriterioEvaluacion.objects.get(codigo="CE.LL.5.8.")

    Indicador.objects.bulk_create([
        # Preparatoria
        Indicador(
            description=(
                "Interpreta la silueta y los paratextos (soporte, formato, "
                "tipografía, imagen, color, estructura externa) de diversos "
                "textos escritos cotidianos, deduciendo su contenido y uso; "
                "reflexiona sobre su intención comunicativa. (I.3., I.4.)"
            ),
            codigo="I.LL.1.1.1.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Distingue palabras y expresiones coloquiales de su "
                "localidad (términos, dichos populares, etc.) e indaga sobre "
                "sus significados, reconoce la entonación y pronunciación de "
                "los diferentes dialectos del habla castellana del país e "
                "interactúa respetuosamente con sus hablantes. (J.2.,S.3.)"
            ),
            codigo="I.LL.1.2.1.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Desarrolla la expresión oral en contextos cotidianos usando "
                "la conciencia lingüística; la acompaña de recursos "
                "audiovisuales en situaciones de expresión creativa; y "
                "adapta el tono de voz, los gestos, la entonación y el "
                "vocabulario, según el contexto y la intención de la "
                "situación comunicativa que enfrente. (J.3., I.3.)"
            ),
            codigo="I.LL.1.3.1.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Elabora significados de diversos materiales impresos del "
                "entorno, a partir de diferenciar entre imagen y texto "
                "escrito; de relacionar el contenido del texto con sus "
                "conocimientos y experiencias previas, y los elementos del "
                "texto entre sí (personajes, escenarios, eventos, etc.); de "
                "predecir a partir del contenido y los paratextos; y de la "
                "posterior comprobación o descarte de sus hipótesis; "
                "autorregulando su comprensión mediante el parafraseo y "
                "formulación de preguntas sobre el contenido del texto. "
                "(I.3.)"
            ),
            codigo="I.LL.1.4.1.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Accede a la lectura por placer y como medio para aprender, "
                "utilizando los recursos de la biblioteca de aula y de la "
                "web; registra la información consultada mediante dibujos y "
                "otros gráficos. (J.2., I.3.)"
            ),
            codigo="I.LL.1.5.1.",
            criterio_evaluacion=criterio1_5
        ),
        Indicador(
            description=(
                "Registra, expresa y comunica ideas mediante sus propios "
                "códigos; explora la formación de palabras y oraciones, "
                "utilizando la conciencia lingüística (fonológica, léxica, "
                "sintáctica y semántica); selecciona y utiliza diferentes "
                "recursos y materiales para sus producciones escritas; y "
                "muestra interés por escribir al reconocer que puede "
                "expresar por escrito sentimientos y opiniones que le "
                "generan las diferentes situaciones cotidianas. (I.1., I.2., "
                "I.3.)"
            ),
            codigo="I.LL.1.6.1.",
            criterio_evaluacion=criterio1_6
        ),
        Indicador(
            description=(
                "Desarrolla su gusto por la escucha de textos literarios con "
                "disfrute de las palabras y las ideas; representa pasajes de "
                "los textos literarios escuchados, utilizando sus propios "
                "códigos, dibujos y/o escenificaciones corporales, y "
                "establece relaciones entre textos leídos o escuchados y el "
                "entorno personal. (I.1., I.2., S.3.)"
            ),
            codigo="I.LL.1.7.1.",
            criterio_evaluacion=criterio1_7
        ),
        # Elemental
        Indicador(
            description=(
                "Reconoce el uso de textos escritos (periódicos, revistas, "
                "correspondencia, publicidad, campañas sociales, etc.) en la "
                "vida cotidiana, identifica su intención comunicativa y "
                "emite opiniones valorativas sobre la utilidad de su "
                "información. (J.2., I.3.)"
            ),
            codigo="I.LL.2.1.1.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Identifica el significado de palabras y expresiones de las "
                "lenguas originarias y/o variedades lingüísticas del "
                "Ecuador, e indaga sobre los dialectos del castellano en el "
                "país. (I.2., I.3.)"
            ),
            codigo="I.LL.2.2.1.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Muestra capacidad de escucha al mantener el tema de "
                "conversación e intercambiar ideas, y sigue las pautas "
                "básicas de la comunicación oral. (I.3., I.4.)"
            ),
            codigo="I.LL.2.3.1.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Interviene espontáneamente en situaciones informales de "
                "comunicación oral, expresa ideas, experiencias y "
                "necesidades con un vocabulario pertinente a la situación "
                "comunicativa, y sigue las pautas básicas de la comunicación "
                "oral. (I.3.)"
            ),
            codigo="I.LL.2.3.2.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Realiza exposiciones orales, adecuadas al contexto escolar, "
                "sobre temas de interés personal y grupal, y las enriquece "
                "con recursos audiovisuales y otros. (I.3., S.4.)"
            ),
            codigo="I.LL.2.4.1.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Construye los significados de un texto a partir del "
                "establecimiento de relaciones de semejanza-diferencia, "
                "objeto-atributo, antecedente-consecuente, secuencia "
                "temporal, problema-solución, concepto-ejemplo, al "
                "comprender los contenidos explícitos e implícitos de un "
                "texto y registrar la información en tablas, gráficos, "
                "cuadros y otros organizadores gráficos sencillos. (I.3., "
                "I.4.)"
            ),
            codigo="I.LL.2.5.1.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Comprende los contenidos implícitos de un texto basándose "
                "en inferencias espacio-temporales, referenciales y de "
                "causa-efecto, y amplía la comprensión de un texto mediante "
                "la identificación de los significados de las palabras, "
                "utilizando estrategias de derivación (familia de palabras), "
                "sinonimia-antonimia, contextualización, prefijos y sufijos "
                "y etimología. (I.2., I.4.)"
            ),
            codigo="I.LL.2.5.2.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Construye criterios, opiniones y emite juicios acerca del "
                "contenido de un texto, al distinguir realidad y ficción, "
                "hechos, datos y opiniones, y desarrolla estrategias "
                "cognitivas como lectura de paratextos, establecimiento del "
                "propósito de lectura, relectura, relectura selectiva y "
                "parafraseo, para autorregular la comprensión. (J.4., I.3.)"
            ),
            codigo="I.LL.2.5.3.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Aplica los conocimientos lingüísticos (léxicos, semánticos, "
                "sintácticos y fonológicos) en la decodificación y "
                "comprensión de textos, leyendo oralmente con fluidez y "
                "entonación en contextos significativos de aprendizaje y de "
                "manera silenciosa y personal en situaciones de recreación, "
                "información y estudio. (J.3., I.3.)"
            ),
            codigo="I.LL.2.6.1.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Escoge, de una selección previa realizada por el docente, "
                "textos de la biblioteca del aula, de la escuela y de la web "
                "y los consulta para satisfacer sus necesidades personales, "
                "de recreación, información y aprendizaje, enriqueciendo sus "
                "ideas e indagando temas de interés. (J.4., I.2.)"
            ),
            codigo="I.LL.2.7.1.",
            criterio_evaluacion=criterio2_7
        ),
        Indicador(
            description=(
                "Aplica el proceso de escritura en la producción de textos "
                "narrativos (relatos escritos de experiencias personales, "
                "hechos cotidianos u otros sucesos y acontecimientos de "
                "interés), usando estrategias y procesos de pensamiento "
                "(ampliación de ideas, secuencia lógica, selección "
                "ordenación y jerarquización de ideas; y uso de "
                "organizadores gráficos, entre otros), apoyándolo y "
                "enriqueciéndolo con paratextos y recursos de las TIC, en "
                "las situaciones comunicativas que lo requieran. (J.2., "
                "I.3.)"
            ),
            codigo="I.LL.2.8.1.",
            criterio_evaluacion=criterio2_8
        ),
        Indicador(
            description=(
                "Aplica el proceso de escritura en la producción de textos "
                "descriptivos (de objetos, animales, lugares y personas), "
                "usando estrategias y procesos de pensamiento (ampliación de "
                "ideas, secuencia lógica, selección ordenación y "
                "jerarquización de ideas; organizadores gráficos, entre "
                "otros), y cita fuentes cuando sea el caso, en las "
                "situaciones comunicativas que lo requieran. (J.2., I.3.)"
            ),
            codigo="I.LL.2.8.2.",
            criterio_evaluacion=criterio2_8
        ),
        Indicador(
            description=(
                "Escribe diferentes tipos de textos narrativos (relatos "
                "escritos de experiencias personales, hechos cotidianos u "
                "otros sucesos y acontecimientos de interés), ordena las "
                "ideas cronológicamente mediante conectores temporales y "
                "aditivos, y utiliza una diversidad de formatos, recursos y "
                "materiales. (I.1., I.3.)"
            ),
            codigo="I.LL.2.9.1.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Aplica progresivamente las reglas de escritura mediante la "
                "reflexión fonológica en la escritura ortográfica de fonemas "
                "que tienen dos y tres representaciones gráficas; la letra "
                "formada por dos sonidos /ks/: “x”, la letra que no tiene "
                "sonido: “h” y la letra “w” que tiene escaso uso en "
                "castellano. (I.3.)"
            ),
            codigo="I.LL.2.9.2.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Escribe diferentes tipos de textos descriptivos (de "
                "objetos, animales, lugares y personas); ordena las ideas "
                "según una secuencia lógica, por temas y subtemas; utiliza "
                "conectores consecutivos, atributos, adjetivos calificativos "
                "y posesivos, y una diversidad de formatos, recursos y "
                "materiales, en las situaciones comunicativas que lo "
                "requieran. (I.1., I.3.)"
            ),
            codigo="I.LL.2.9.3.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Escucha y lee diversos géneros literarios (textos populares "
                "y de autores ecuatorianos) como medio para potenciar la "
                "imaginación, la curiosidad, la memoria, de manera que "
                "desarrolla preferencias en el gusto literario y adquiere "
                "autonomía en la lectura. (I.1., I.3.)"
            ),
            codigo="I.LL.2.10.1.",
            criterio_evaluacion=criterio2_10
        ),

        Indicador(
            description=(
                "Recrea textos literarios (adivinanzas, trabalenguas, "
                "retahílas, nanas, rondas, villancicos, chistes, refranes, "
                "coplas, loas) con diversos medios y recursos (incluidas las "
                "TIC). (I.3., I.4.)"
            ),
            codigo="I.LL.2.11.1.",
            criterio_evaluacion=criterio2_11
        ),
        Indicador(
            description=(
                "Escribe textos propios a partir de otros (cuentos, fábulas, "
                "poemas, leyendas, canciones) con nuevas versiones de "
                "escenas, personajes u otros elementos, con diversos medios "
                "y recursos (incluidas las TIC). (I.3., S.3.)"
            ),
            codigo="I.LL.2.11.2.",
            criterio_evaluacion=criterio2_11
        ),
        # Media
        Indicador(
            description=(
                "Reconoce la funcionalidad de la lengua escrita como "
                "manifestación cultural y de identidad en diferentes "
                "contextos y situaciones, atendiendo a la diversidad "
                "lingüística del Ecuador. (I.3., S.2.)"
            ),
            codigo="I.LL.3.1.1.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Indaga sobre las influencias lingüísticas y culturales que "
                "explican los diferentes dialectos del castellano, así como "
                "la presencia de varias nacionalidades y pueblos que hablan "
                "otras lenguas en el país. (I.3., S.2.)"
            ),
            codigo="I.LL.3.1.2.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Escucha discursos orales (conversaciones, diálogos, "
                "narraciones, discusiones, entrevistas, exposiciones, "
                "presentaciones), parafrasea su contenido y participa de "
                "manera respetuosa frente a las intervenciones de los demás, "
                "buscando acuerdos en el debate de temas conflictivos. "
                "(J.3., S.1.)"
            ),
            codigo="I.LL.3.2.1.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Propone intervenciones orales con una intención "
                "comunicativa, organiza el discurso de acuerdo con las "
                "estructuras básicas de la lengua oral, reflexiona sobre los "
                "efectos del uso de estereotipos y prejuicios, adapta el "
                "vocabulario, según las diversas situaciones comunicativas a "
                "las que se enfrente. (J.3., I.4.)"
            ),
            codigo="I.LL.3.2.2.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Establece relaciones explícitas entre los contenidos de dos "
                "o más textos, los compara, contrasta sus fuentes, reconoce "
                "el punto de vista, las motivaciones y los argumentos del "
                "autor al monitorear y autorregular su comprensión mediante "
                "el uso de estrategias cognitivas. (I.3.,I.4.)"
            ),
            codigo="I.LL.3.3.1.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Realiza inferencias fundamentales y proyectivovalorativas, "
                "valora los contenidos y aspectos de forma a partir de "
                "criterios preestablecidos, reconoce el punto de vista, las "
                "motivaciones y los argumentos del autor al monitorear y "
                "autorregular su comprensión mediante el uso de estrategias "
                "cognitivas. (J.2., J.4.)"
            ),
            codigo="I.LL.3.3.2.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Aplica sus conocimientos lingüísticos (léxicos, semánticos, "
                "sintácticos y fonológicos) en la decodificación y "
                "comprensión de textos, leyendo con fluidez y entonación en "
                "diversos contextos (familiares, escolares y sociales) y con "
                "diferentes propósitos (exponer, informar, narrar, "
                "compartir, etc.). (I.3., I.4.)"
            ),
            codigo="I.LL.3.4.1.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Identifica, compara y contrasta fuentes consultadas en "
                "bibliotecas y en la web, registra la información consultada "
                "en esquemas de diverso tipo y genera criterios para el "
                "análisis de su confiabilidad. (J.2., I.4.)"
            ),
            codigo="I.LL.3.5.1.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Produce textos narrativos, descriptivos, expositivos e "
                "instructivos; autorregula la escritura mediante la "
                "aplicación del proceso de escritura y el uso de estrategias "
                "y procesos de pensamiento; organiza ideas en párrafos con "
                "unidad de sentido, con precisión y claridad; utiliza un "
                "vocabulario, según un determinado campo semántico y "
                "elementos gramaticales apropiados, y se apoya en el empleo "
                "de diferentes formatos, recursos y materiales, incluidas "
                "las TIC, en las situaciones comunicativas que lo requieran. "
                "(I.2.,I.4.)"
            ),
            codigo="I.LL.3.6.1.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Escribe cartas, noticias, diario personal, entre otros "
                "textos narrativos, (organizando los hechos y acciones con "
                "criterios de secuencia lógica y temporal, manejo de persona "
                "y tiempo verbal, conectores temporales y aditivos, "
                "proposiciones y conjunciones) y los integra en diversos "
                "tipos de textos producidos con una intención comunicativa y "
                "en un contexto determinado. (I.3., I.4.)"
            ),
            codigo="I.LL.3.6.2.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Escribe textos descriptivos organizados, usando recursos "
                "estilísticos para la descripción de objetos, personajes y "
                "lugares (topografía, prosopografía, etopeya, descripción de "
                "objetos), estructuras descriptivas en diferentes tipos de "
                "texto (guía turística, biografía o autobiografía, reseña, "
                "entre otros), elementos gramaticales adecuados: atributos, "
                "adjetivos calificativos y posesivos; conectores de adición, "
                "de comparación, orden, y un vocabulario específico relativo "
                "al ser, objeto, lugar o hecho que se describe, y los "
                "integra en diversos tipos de textos producidos con una "
                "intención comunicativa y en un contexto determinado. (I.3., "
                "I.4.)"
            ),
            codigo="I.LL.3.6.3.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Escribe diferentes tipos de texto con estructuras "
                "expositivas (informe, noticia, entre otros), según su "
                "estructura, con secuencia lógica, manejo coherente de la "
                "persona y del tiempo verbal; organiza las ideas en párrafos "
                "según esquemas expositivos de comparación-contraste, "
                "problema-solución, antecedente-consecuente y causa-efecto, "
                "y utiliza conectores causales y consecutivos, proposiciones "
                "y conjunciones, y los integra en diversos tipos de textos "
                "producidos con una intención comunicativa y en un contexto "
                "determinado. (I.3., I.4.)"
            ),
            codigo="I.LL.3.6.4.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Escribe diferentes tipos de texto con estructuras "
                "instructivas(receta, manual, entre otros) según una "
                "secuencia lógica, con concordancia de género, número, "
                "persona y y tiempo verbal, uso de conectores temporales y "
                "de orden organiza las ideas en párrafos diferentes con el "
                "uso de conectores lógicos, proposiciones y conjunciones, "
                "integrándolos en diversos tipos de textos producidos con "
                "una intención comunicativa y en un contexto determinado. "
                "(I.3., I.4.)"
            ),
            codigo="I.LL.3.6.5.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Reconoce en textos de literatura oral (canciones, "
                "adivinanzas, trabalenguas, retahílas, nanas, rondas, "
                "arrullos, amorfinos, chigualos) o escrita (cuentos, poemas, "
                "mitos, leyendas), los elementos característicos que les dan "
                "sentido; y participa en discusiones sobre textos literarios "
                "en las que aporta información, experiencias y opiniones. "
                "(I.3., S.4.)"
            ),
            codigo="I.LL.3.7.1.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Elige lecturas basándose en preferencias personales de "
                "autores, géneros o temas, maneja diversos soportes para "
                "formarse como lector autónomo y participa en discusiones "
                "literarias, desarrollando progresivamente la lectura "
                "crítica. (J.4., S.4.)"
            ),
            codigo="I.LL.3.7.2.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Reinventa textos literarios, reconociendo la fuente "
                "original, los relaciona con el contexto cultural propio y "
                "de otros entornos, incorpora recursos del lenguaje figurado "
                "y usa diversos medios y recursos (incluidas las TIC) para "
                "recrearlos. (J.2., I.2.)"
            ),
            codigo="I.LL.3.8.1.",
            criterio_evaluacion=criterio3_8
        ),
        # Superior
        Indicador(
            description=(
                "Explica el origen, el desarrollo y la influencia de la "
                "escritura en distintos momentos históricos, regiones y "
                "culturas del mundo, y valora la diversidad expresada en sus "
                "textos representativos. (S.2., I.3.)"
            ),
            codigo="I.LL.4.1.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Explica la influencia de las variaciones lingüísticas "
                "sociales y situacionales del Ecuador en las relaciones "
                "sociales, y la correspondencia entre la estructura de la "
                "lengua y las formas de pensar y actuar de las personas. "
                "(I.3.,S.3.)"
            ),
            codigo="I.LL.4.2.1.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Valora el contenido explícito de dos o más textos orales, "
                "identificando contradicciones, ambigüedades, falacias, "
                "distorsiones, desviaciones en el discurso; y reflexiona "
                "sobre los efectos de los estereotipos y prejuicios en la "
                "comunicación. (J.3., I.4.)"
            ),
            codigo="I.LL.4.3.1.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Construye acuerdos y soluciona problemas, utilizando los "
                "recursos del discurso oral (entonación, volumen, gestos, "
                "movimientos corporales y postura), de manera selectiva y "
                "crítica, y evalúa su impacto en la audiencia. (J.3.,I.3.)"
            ),
            codigo="I.LL.4.4.1.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Produce discursos (conversación, diálogo, narración, "
                "debate, conversatorio, presentación, entrevista, encuesta, "
                "exposición) organizados a partir del uso de las estructuras "
                "básicas de la lengua oral, utiliza un vocabulario acorde a "
                "la intención y el contexto, los apoya con una variedad de "
                "formatos, soportes y recursos (incluyendo los "
                "audiovisuales). (I.3., I.4.)"
            ),
            codigo="I.LL.4.4.2.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Compara, bajo criterios preestablecidos, las relaciones "
                "explícitas entre los contenidos de dos o más textos y "
                "contrasta sus fuentes; autorregula la comprensión mediante "
                "el uso de estrategias cognitivas autoseleccionadas, de "
                "acuerdo con el propósito de lectura y las dificultades "
                "identificadas, y valora el contenido explícito al "
                "identificar contradicciones y ambigüedades. (J.4., I.4.)"
            ),
            codigo="I.LL.4.5.1.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Construye significados implícitos al inferir el tema, el "
                "punto de vista del autor, las motivaciones y argumentos de "
                "un texto; los valora a partir del contraste con fuentes "
                "adicionales, y elabora criterios crítico-valorativos acerca "
                "de las diferentes perspectivas sobre un mismo tema en dos o "
                "más textos. (J.2., I.3.)"
            ),
            codigo="I.LL.4.5.2.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Consulta bibliotecas y recursos digitales en la web, con "
                "capacidad para comparar y valorar textos en función del "
                "propósito de lectura, la calidad de la información "
                "(claridad, organización, actualización, amplitud, "
                "profundidad) y la confiabilidad de la fuente, recogiendo, "
                "comparando y organizando la información consultada en "
                "esquemas de diversos tipos. (J.2., I.4.)"
            ),
            codigo="I.LL.4.6.1.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Estructura diferentes tipos de textos periodísticos "
                "(noticia, crónica, reportaje, entrevista, artículo de "
                "opinión, entre otros), y académicos (informe, reseña, "
                "ensayo narrativo, expositivo, literario y argumentativo, "
                "entre otros), combinando diferentes tramas (narrativa, "
                "descriptiva, expositiva, conversacional y argumentativa), "
                "tipos de párrafo (de descripción, ampliación, "
                "ejemplificación, definición, conclusivo, deductivo, "
                "inductivo) y diálogos directos e indirectos, según sean "
                "pertinentes; elabora preguntas indagatorias; maneja las "
                "normas de citación e identificación de fuentes más comunes, "
                "y utiliza herramientas de edición de textos en distintos "
                "programas informáticos y de la web. (J.2., I.4.)"
            ),
            codigo="I.LL.4.7.1.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Usa el procedimiento de producción de textos en la "
                "escritura de textos periodísticos y académicos y aplica "
                "estrategias que apoyen cada uno de sus pasos "
                "(planificación: lectura previa, lluvia de ideas, "
                "organizadores gráficos, consultas, selección de la tesis, "
                "el título que denote el tema, lluvia de ideas con los "
                "subtemas, elaboración del plan; redacción: selección y "
                "jerarquización de los subtemas, selección, ampliación, "
                "jerarquización, secuenciación, relación causal, temporal, "
                "analógica, transitiva y recíproca entre ideas, análisis, "
                "representación de conceptos; revisión: uso de diccionarios, "
                "listas de cotejo, rúbricas, entre otras); maneja las normas "
                "de citación e identificación de fuentes más utilizadas "
                "(APA, Chicago y otras). (J.2., I.4.)"
            ),
            codigo="I.LL.4.7.2.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Utiliza elementos gramaticales en la producción de textos "
                "periodísticos y académicos (oraciones compuestas "
                "coordinadas, subordinadas, yuxtapuestas; conectores "
                "lógicos: de énfasis, ilustración, cambio de perspectiva, "
                "condición y conclusión; puntuación en oraciones compuestas "
                "–dos puntos, coma, punto y coma–; modos verbales, tiempos "
                "verbales complejos y verboides; voz activa y voz pasiva; "
                "conjunciones propias e impropias; frases nominales, "
                "adjetivas, adverbiales, preposicionales y verbales; guion, "
                "comillas, dos puntos e interjecciones en diálogos; tilde en "
                "pronombres interrogativos, mayúsculas, adverbios terminados "
                "en “-mente” y en palabras compuestas), en función de "
                "mejorar la claridad y precisión y matizar las ideas y los "
                "significados de oraciones y párrafos. (I.3., I.4.)"
            ),
            codigo="I.LL.4.7.3.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Interpreta textos literarios a partir de las "
                "características del género al que pertenecen, y debate "
                "críticamente su interpretación basándose en indagaciones "
                "sobre el tema, género y contexto. (J.4., S.4.)"
            ),
            codigo="I.LL.4.8.1.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Elige lecturas en función de sus preferencias personales de "
                "autor, género, estilo, temas y contextos socioculturales; "
                "maneja diversos soportes, y debate críticamente su "
                "interpretación basándose en indagaciones sobre el tema, "
                "género y contexto. (J.4., I.3.)"
            ),
            codigo="I.LL.4.8.2.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Compone y recrea textos literarios que adaptan o combinan "
                "diversas estructuras y recursos, expresando intenciones "
                "determinadas (ironía, sarcasmo, humor, etc.) mediante el "
                "uso creativo del significado de las palabras y el uso "
                "colaborativo de diversos medios y recursos de las TIC. "
                "(I.3., I.4.)"
            ),
            codigo="I.LL.4.9.1.",
            criterio_evaluacion=criterio4_9
        ),
        # Bachillerato
        Indicador(
            description=(
                "Reconoce las transformaciones de la cultura escrita en la "
                "era digital (usos del lenguaje escrito, formas de lectura y "
                "escritura) y sus implicaciones socioculturales.(J.3., "
                "I.2.)."
            ),
            codigo="I.LL.5.1.1.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Analiza críticamente desde diversas perspectivas (social, "
                "étnica, de género, cultural), los usos de la lengua y de "
                "las variedades lingüísticas que implican algún tipo de "
                "discriminación (diglosia) en la literatura, el humor y el "
                "periodismo. (I.3., S.1.)"
            ),
            codigo="I.LL.5.2.1.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Identifica contradicciones, ambigüedades, falacias, "
                "distorsiones y desviaciones en el discurso, seleccionando "
                "críticamente los recursos del discurso oral y evaluando su "
                "impacto en la audiencia para valorar el contenido explícito "
                "de un texto oral. (I.4., S.4.)"
            ),
            codigo="I.LL.5.3.1.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Analiza los significados connotativos del discurso, "
                "seleccionando críticamente los recursos del discurso oral y "
                "evaluando su impacto en la audiencia para valorar el "
                "contenido implícito de un texto oral. (I.4., S.4.)"
            ),
            codigo="I.LL.5.3.2.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Persuade mediante la argumentación y contraargumentación "
                "con dominio de las estructuras lingüísticas, seleccionando "
                "críticamente los recursos del discurso oral y evaluando su "
                "impacto en la audiencia, en diferentes formatos y "
                "registros. (I.3., S.4.)"
            ),
            codigo="I.LL.5.3.3.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Identifica contradicciones, ambigüedades y falacias, al "
                "valorar el contenido explícito de un texto; elabora "
                "argumentos propios, los contrasta con fuentes adicionales "
                "para valorar el contenido implícito y aplica estrategias "
                "cognitivas y metacognitivas de comprensión; recoge, compara "
                "y organiza la información, mediante el uso de esquemas y "
                "estrategias personales (J.2., I.4.)"
            ),
            codigo="I.LL.5.4.1.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Interpreta los aspectos formales y el contenido de un "
                "texto, en función del propósito comunicativo, el contexto "
                "sociocultural y el punto de vista del autor; recoge, "
                "compara y organiza la información consultada, mediante el "
                "uso de esquemas y estrategias personales. (J.4., I.3.)"
            ),
            codigo="I.LL.5.4.2.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Consulta bases de datos digitales y otros recursos de la "
                "web con capacidad para seleccionar y valorar fuentes según "
                "el propósito de lectura, su confiabilidad y punto de vista; "
                "recoge, compara y organiza la información consultada, "
                "esquemas y estrategias personales. (J.4., I.3.)"
            ),
            codigo="I.LL.5.5.1.",
            criterio_evaluacion=criterio5_5
        ),
        Indicador(
            description=(
                "Aplica el proceso de producción en la escritura de textos "
                "con estructura argumentativa, elabora argumentos (de hecho, "
                "definición, autoridad, analogía, ejemplificación, "
                "experiencia, explicación, deducción), aplica las normas de "
                "citación e identificación de fuentes con rigor y honestidad "
                "académica, en diferentes soportes impresos y digitales. "
                "(J.2., I.3.)"
            ),
            codigo="I.LL.5.6.1.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Expresa su postura u opinión sobre diferentes temas de la "
                "cotidianidad y académicos con coherencia y cohesión, "
                "mediante la selección de un vocabulario preciso y el uso de "
                "diferentes tipos de párrafos para expresar matices y "
                "producir determinados efectos en los lectores, en "
                "diferentes soportes impresos y digitales. (I.3., I.4.)"
            ),
            codigo="I.LL.5.6.2.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Ubica cronológicamente los textos más representativos de la "
                "literatura de Grecia y Roma, y examina críticamente las "
                "bases de la cultura occidental. (I.4.)"
            ),
            codigo="I.LL.5.7.1.",
            criterio_evaluacion=criterio5_7
        ),
        Indicador(
            description=(
                "Ubica cronológicamente los textos más representativos de la "
                "literatura latinoamericana: siglos XIX a XXI, y establece "
                "sus aportes en los procesos de reconocimiento y "
                "visibilización de la heterogeneidad cultural. (I.4., S.1.)"
            ),
            codigo="I.LL.5.7.2.",
            criterio_evaluacion=criterio5_7
        ),
        Indicador(
            description=(
                "Ubica cronológicamente los textos más representativos de la "
                "literatura ecuatoriana: siglos XIX a XXI, y establece sus "
                "aportes en la construcción de una cultura diversa y plural. "
                "(I.4., S.1.)"
            ),
            codigo="I.LL.5.7.3.",
            criterio_evaluacion=criterio5_7
        ),
        Indicador(
            description=(
                "Recrea textos literarios leídos desde la experiencia "
                "personal, adaptando diversos recursos literarios; "
                "experimenta con diversas estructuras literarias, "
                "lingüísticas, visuales y sonoras en la composición de "
                "textos. (I.1., I.3.)"
            ),
            codigo="I.LL.5.8.1.",
            criterio_evaluacion=criterio5_8
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0050_auto_20180825_1047'),
    ]

    operations = [
        migrations.RunPython(create_indicadores)
    ]
