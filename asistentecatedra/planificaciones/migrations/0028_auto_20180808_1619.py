from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignatura
    lengua_literatura = Asignatura.objects.get(name='Lengua y Literatura')

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
                "Infiere el contenido y el uso de diversos textos escritos "
                "que se utilizan en actividades cotidianas, mediante el "
                "análisis de su silueta y paratextos(soporte, formato, "
                "tipografía, imagen, color, estructura externa) y reflexiona "
                "sobre su intención comunicativa."
            ),
            codigo="CE.LL.1.1.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Distingue palabras y expresiones coloquiales de su "
                "localidad(términos, dichos populares, etc.) e indaga sobre "
                "sus significados, reconoce la entonación y pronunciación de "
                "los diferentes dialectos del habla castellana del país e "
                "interactúa respetuosamente con sus hablantes."
            ),
            codigo="CE.LL.1.2.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Desarrolla la expresión oral en contextos cotidianos usando "
                "la conciencia lingüística la acompaña de "
                "recursosaudiovisuales en situaciones de expresión creativa "
                "y adapta el tono de voz, los gestos, la entonación y el "
                "vocabulario, según el contexto y la intención de la "
                "situación comunicativa que enfrente."
            ),
            codigo="CE.LL.1.3.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Elabora significados de diversos materiales impresos del "
                "entorno, a partir de la diferenciación entre imageny texto "
                "escrito, la relación entre el contenido del texto con sus "
                "conocimientos y experiencias previas, y los elementos del "
                "texto entre sí(personajes, escenarios, eventos, etc.) de "
                "predecir a partir del contenido y los paratextos y de la "
                "posterior comprobación o descarte de sus hipótesis "
                "autorregula su comprensión mediante el parafraseo y "
                "formulación de preguntas sobre el contenido del texto."
            ),
            codigo="CE.LL.1.4.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Accede a la lectura por placer y como medio para aprender, "
                "utilizando los recursos de la biblioteca de aula yde la web "
                "registra la información consultada mediante dibujos y otros "
                "gráficos."
            ),
            codigo="CE.LL.1.5.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Registra, expresa y comunica ideas mediante sus propios "
                "códigos explora la formación de palabras y oraciones, "
                "utilizando la conciencia lingüística(fonológica, léxica, "
                "sintáctica y semántica) selecciona y utiliza diferentes "
                "recursos y materiales para sus producciones escritas y "
                "muestra interés por escribir, al reconocer que puede "
                "expresar por escrito, los sentimientos y las opiniones que "
                "le generan las diferentes situaciones cotidianas."
            ),
            codigo="CE.LL.1.6.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Desarrolla su gusto por la escucha de textos literarios con "
                "disfrute de las palabras y las ideas; representa pasajes de "
                "los textos literarios escuchados, utilizando sus propios "
                "códigos, dibujos y/o escenificaciones corporales, y "
                "establece relaciones entre textos leídos o escuchados y el "
                "entorno personal."
            ),
            codigo="CE.LL.1.7.",
            asignatura=lengua_literatura,
            subnivel=preparatoria
        ),
        # Elemental
        CriterioEvaluacion(
            description=(
                "Diferencia la intención comunicativa de diversos textos de "
                "uso cotidiano (periódicos, revistas, correspondencia, "
                "publicidad, campañas sociales, etc.) y expresa con "
                "honestidad, opiniones valorativas sobre la utilidad de su "
                "información."
            ),
            codigo="CE.LL.2.1.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Distingue y busca conocer el significado de palabras y "
                "expresiones de las lenguas originarias y/o variedades "
                "lingüísticas del Ecuador, e indaga sobre los dialectos del "
                "castellano en el país."
            ),
            codigo="CE.LL.2.2.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Dialoga, demostrando capacidad de escucha, manteniendo el "
                "tema de conversación, expresando ideas, experiencias y "
                "necesidades con un vocabulario pertinente y siguiendo las "
                "pautas básicas de la comunicación oral, a partir de una "
                "reflexión sobre la expresión oral con uso de la conciencia "
                "lingüística."
            ),
            codigo="CE.LL.2.3.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Expone oralmente sobre temas de interés personal y grupal "
                "en el contexto escolar, y los enriquece con recursos "
                "audiovisuales y otros."
            ),
            codigo="CE.LL.2.4.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Comprende contenidos implícitos y explícitos, emite "
                "criterios, opiniones y juicios de valor sobre textos "
                "literarios y no literarios, mediante el uso de diferentes "
                "estrategias para construir significados."
            ),
            codigo="CE.LL.2.5.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Aplica conocimientos lingüísticos en la decodificación y "
                "comprensión de textos, leyendo oralmente con fluidez y "
                "entonación en contextos significativos de aprendizaje y de "
                "manera silenciosa y personal en situaciones de recreación, "
                "información y estudio."
            ),
            codigo="CE.LL.2.6.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Escoge, de una selección previa realizada por el docente, "
                "textos de la biblioteca de aula, de la escuela y de la web "
                "y los consulta para satisfacer sus necesidades personales, "
                "de recreación, información y aprendizaje, enriqueciendo sus "
                "ideas e indagando sobre temas de interés."
            ),
            codigo="CE.LL.2.7.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Aplica el proceso de escritura en la producción de textos "
                "narrativos y descriptivos, usando estrategias y procesos de "
                "pensamiento los apoya y enriquece con paratextos y recursos "
                "de las TIC, y cita fuentes cuando sea el caso."
            ),
            codigo="CE.LL.2.8.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Utiliza elementos de la lengua apropiados para diferentes "
                "tipos de textos narrativos y descriptivos emplea una "
                "diversidad de formatos, recursos y materiales para "
                "comunicar ideas con eficiencia."
            ),
            codigo="CE.LL.2.9.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Escucha y lee diversos géneros literarios(textos populares "
                "y de autores ecuatorianos) como medio para potenciar la "
                "imaginación, la curiosidad, la memoria, de manera que "
                "desarrolla preferencias en el gusto literario y adquiere "
                "autonomía en la lectura."
            ),
            codigo="CE.LL.2.10.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Produce y recrea textos literarios, a partir de otros "
                "leídos y escuchados (textos populares y de autores "
                "ecuatorianos), valiéndose de diversos medios y recursos "
                "(incluidas las TIC)."
            ),
            codigo="CE.LL.2.11.",
            asignatura=lengua_literatura,
            subnivel=elemental
        ),
        # Media
        CriterioEvaluacion(
            description=(
                "Distingue la función de transmisión cultural de la lengua, "
                "reconoce las influencias lingüísticas y culturales que "
                "explican los dialectos del castellano en el Ecuador e "
                "indaga sobre las características de los pueblos y "
                "nacionalidades del país que tienen otras lenguas."
            ),
            codigo="CE.LL.3.1.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Participa en situaciones comunicativas orales, escuchando "
                "de manera activa y mostrando respeto frente a las "
                "intervenciones de los demás en la búsqueda de acuerdos, "
                "organiza su discurso de acuerdo con las estructuras básicas "
                "de la lengua oral, reflexiona sobre los efectos del uso de "
                "estereotipos y prejuicios, adapta el vocabulario y se apoya "
                "enrecursos y producciones audiovisuales, según las diversas "
                "situaciones comunicativas a las que se enfrente."
            ),
            codigo="CE.LL.3.2.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Establece relaciones explícitas entre los contenidos de dos "
                "o más textos, los compara, contrasta sus fuentes,realiza "
                "inferencias fundamentales y proyectivo-valorativas, valora "
                "sus contenidos y aspectos de forma a partir de criterios "
                "establecidos, reconoce el punto de vista, las motivaciones "
                "y los argumentos del autor al monitorear y autorregular su "
                "comprensión mediante el uso de estrategias cognitivas de "
                "comprensión."
            ),
            codigo="CE.LL.3.3.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Aplica sus conocimientos lingüísticos(léxicos, semánticos, "
                "sintácticos y fonológicos) en la decodificación y "
                "comprensión de textos, leyendo con fluidez y entonación en "
                "diversos contextos(familiares, escolares y sociales) y con "
                "diferentes propósitos(exponer, informar, narrar, compartir, "
                "etc.)."
            ),
            codigo="CE.LL.3.4.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Consulta bibliotecas y recursos digitales en la web, genera "
                "criterios para identificar, comparar y contrastar fuentes, "
                "y registra la información consultada en esquemas de diverso "
                "tipo."
            ),
            codigo="CE.LL.3.5.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Produce textos con tramas narrativas, descriptivas, "
                "expositivas e instructivas, y las integra cuando es "
                "pertinente utiliza los elementos de la lengua más "
                "apropiados para cada uno, logrando coherencia y cohesión "
                "autorregula la escritura mediante la aplicación del proceso "
                "de producción, estrategias de pensamiento, y se apoya en "
                "diferentes formatos, recursos y materiales, incluidas las "
                "TIC, en las situaciones comunicativas que lo requieran."
            ),
            codigo="CE.LL.3.6.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Elige lecturas basándose en preferencias personales, "
                "reconoce los elementos característicos que le dan sentido y "
                "participa en discusiones literarias, desarrollando la "
                "lectura crítica."
            ),
            codigo="CE.LL.3.7.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Reinventa textos literarios, reconociendo la fuente "
                "original, los relaciona con el contexto cultural propio y "
                "de otros entornos, incorpora los recursos del lenguaje "
                "figurado y diversos medios y recursos(incluidas las TIC)."
            ),
            codigo="CE.LL.3.8.",
            asignatura=lengua_literatura,
            subnivel=media
        ),
        # Superior
        CriterioEvaluacion(
            description=(
                "Explica los aportes de la cultura escrita al desarrollo "
                "histórico, social y cultural de la humanidad y valora la "
                "diversidad del mundo expresada en textos escritos "
                "representativos de las diferentes culturas, en diversas "
                "épocas históricas."
            ),
            codigo="CE.LL.4.1.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica la influencia de las variaciones lingüísticas "
                "socioculturales y situacionales del Ecuador en las "
                "relaciones sociales, así como la correspondencia entre la "
                "estructura de la lengua y las formas de pensar y actuar de "
                "las personas."
            ),
            codigo="CE.LL.4.2.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Valora el contenido explícito de dos o más textos orales, "
                "identificando contradicciones, ambigüedades, falacias, "
                "distorsiones, desviaciones en el discurso y reflexiona "
                "sobre los efectos del uso de estereotipos y prejuicios en "
                "la comunicación."
            ),
            codigo="CE.LL.4.3.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Organiza sus discursos según las estructuras básicas de la "
                "lengua oral, utiliza un vocabulario acorde a la "
                "intención(construir acuerdos, solucionar problemas, etc.) y "
                "al contexto e integra una variedad de recursos, formatos y "
                "soportes, evaluando su impacto en la audiencia."
            ),
            codigo="CE.LL.4.4.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Comprende en sus niveles literal, inferencial y "
                "crítico-valorativo diversos tipos de texto, al comparar "
                "bajo criterios preestablecidos las relaciones explícitas "
                "entre sus contenidos, inferir el tema, el punto de vista "
                "del autor, las motivaciones y argumentos de un texto, "
                "distinguir las diferentes perspectivas en conflicto sobre "
                "un mismo tema, autorregular la comprensión mediante la "
                "aplicación de estrategias cognitivas autoseleccionadas de "
                "acuerdo con el propósito de lectura y a dificultades "
                "identificadas y valora contenidos al contrastarlos con "
                "fuentes adicionales, identificando contradicciones y "
                "ambigüedades."
            ),
            codigo="CE.LL.4.5.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Consulta bibliotecas y recursos digitales en la web, "
                "comparándolos y valorándolos en función de la confiabilidad "
                "de la fuente, el propósito de la lectura y la calidad de la "
                "información, recogiéndola, contrastándola y organizándola "
                "en esquemas de diverso tipo."
            ),
            codigo="CE.LL.4.6.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Produce diferentes tipos de textos "
                "periodísticos(reportajes, crónicas, noticias, entrevistas, "
                "artículos de opinión, entre otros) y académicos(artículos y "
                "proyectos de investigación, informes, reseñas, resúmenes, "
                "ensayos) con coherencia y cohesión, autorregulando la "
                "escritura mediante la aplicación del proceso de producción, "
                "el uso de estrategias y procesos de pensamiento, matizando "
                "y precisando significados y apoyándose en diferentes "
                "formatos, recursos y materiales, incluidas las TIC, y cita "
                "e identifica fuentes con pertinencia."
            ),
            codigo="CE.LL.4.7.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Lee textos literarios en función de sus preferencias "
                "personales, los interpreta y sustenta su interpretación "
                "aldebatir críticamente sobre ella, basándose en "
                "indagaciones sobre el tema, género y contexto."
            ),
            codigo="CE.LL.4.8.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Compone y recrea textos literarios que adaptan o combinan "
                "diversas estructuras y recursos literarios, expresa "
                "intenciones determinadas(ironía, sarcasmo, humor, etc.) "
                "mediante el uso creativo del significado de las palabras, "
                "la utilización colaborativa de diversos medios y recursos "
                "de las TIC, a partir de su experiencia personal."
            ),
            codigo="CE.LL.4.9.",
            asignatura=lengua_literatura,
            subnivel=superior
        ),
        # Bachillerato
        CriterioEvaluacion(
            description=(
                "Indaga sobre la evolución de la cultura escrita en la era "
                "digital(transformaciones y tendencias actuales y futuras) e "
                "identifica las implicaciones socioculturales de su "
                "producción y consumo."
            ),
            codigo="CE.LL.5.1.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza las causas de la diglosia en relación con las "
                "lenguas originarias y sus consecuencias en diversos "
                "ámbitos, y las variaciones lingüísticas socioculturales del "
                "Ecuador desde diversas perspectivas."
            ),
            codigo="CE.LL.5.2.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Escucha y valora el contenido explícito e implícito del "
                "discurso y con sus respuestas persuade mediante la "
                "argumentación y la contraargumentación, utilizando "
                "diferentes formatos(debates, mesas redondas, etc.), "
                "registros y otros recursos del discurso oral con dominio de "
                "las estructuras lingüísticas, evaluando su impacto en la "
                "audiencia."
            ),
            codigo="CE.LL.5.3.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Valora los contenidos explícitos e implícitos y los "
                "aspectos formales de dos o más textos, en función del "
                "propósito comunicativo, el contexto sociocultural y el "
                "punto de vista del autor aplica estrategias cognitivas y "
                "metacognitivas para autorregular la comprensión, identifica "
                "contradicciones, ambigüedades y falacias, elabora "
                "argumentos propios y los contrasta con fuentes adicionales, "
                "mediante el uso de esquemas y estrategias personales para "
                "recoger, comparar y organizar la información."
            ),
            codigo="CE.LL.5.4.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Consulta bases de datos digitales y otros recursos de la "
                "web con capacidad para seleccionar fuentes de acuerdo al "
                "propósito de lectura valora su confiabilidad y punto de "
                "vista, y recoge, compara y organiza la información "
                "consultada, mediante el uso de esquemas y estrategias "
                "personales."
            ),
            codigo="CE.LL.5.5.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Aplica el proceso de escritura en la construcción de textos "
                "académicos argumentativos, selecciona el tema, formula la "
                "tesis y diferentes tipos de argumentos expresados en "
                "párrafos apropiados, selecciona con precisión las palabras "
                "por su significado para expresar matices y producir efectos "
                "en los lectores, aplica normas de citación e identificación "
                "de fuentes con rigor y honestidad académica, en diferentes "
                "soportes impresos y digitales."
            ),
            codigo="CE.LL.5.6.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Ubica cronológicamente los textos más representativos de la "
                "literatura de Grecia, Roma, América Latina y Ecuador, "
                "examina críticamente las bases de la cultura occidental y "
                "establece sus aportes en los procesos de visibilización de "
                "la heterogeneidad cultural."
            ),
            codigo="CE.LL.5.7.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Recrea los textos literarios leídos desde la experiencia "
                "personal, adaptando diversos recursos literarios, y "
                "experimenta la escritura creativa con diferentes "
                "estructuras literarias."
            ),
            codigo="CE.LL.5.8.",
            asignatura=lengua_literatura,
            subnivel=bachillerato
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0027_auto_20180808_1531'),
    ]

    operations = [
        migrations.RunPython(create_criterios)
    ]
