from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')
    Indicador = apps.get_model('planificaciones', 'Indicador')

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.1.4.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.ECA.2.6.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.ECA.3.6.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.ECA.4.6.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.ECA.5.4.")

    Indicador.objects.bulk_create([
        # Preparatoria
        Indicador(
            description=(
                "Manifiesta curiosidad e interés por explorar de manera "
                "espontánea las cualidades de la voz, el cuerpo y de "
                "elementos del entorno, natural y artificial, y describe sus "
                "características. (J.4., I.2.)"
            ),
            codigo="I.ECA.1.1.1.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Se interesa y participa activamente en la realización de "
                "juegos sensoriomotores y en procesos de improvisación y "
                "creación musical. (I.3., S.1.)"
            ),
            codigo="I.ECA.1.1.2.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Hace una diferenciación básica de las manifestaciones "
                "culturales y artísticas de su entorno próximo, "
                "identificando a sus actores y/o creadores, y expresa las "
                "ideas y emociones que suscita la observación de las mismas. "
                "(J.1., I.2., S.2.)"
            ),
            codigo="I.ECA.1.2.1.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Reconoce y describe corporal, gráfica o verbalmente ideas, "
                "sentimientos o emociones (alegría, tristeza, paso del "
                "tiempo, presencia de la naturaleza, etc.) en la observación "
                "de imágenes y la escucha de piezas musicales. (I.2., J.3.)"
            ),
            codigo="I.ECA.1.2.2.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Participa en juegos simbólicos y realiza producciones "
                "artísticas sencillas con una intención expresiva y/o "
                "comunicativa. (I.3., S.1.)"
            ),
            codigo="I.ECA.1.3.1.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Intuye las posibilidades del propio cuerpo en actividades "
                "de movimiento y de juego dramático. (J.1., S.1.)"
            ),
            codigo="I.ECA.1.3.2.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Establece relaciones empáticas con sus compañeros y los "
                "adultos que eventualmente participan en la realización de "
                "actividades artísticas colectivas. (S.1., I.3.)"
            ),
            codigo="I.ECA.1.4.1.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Comprende la planificación del proceso de trabajo que se le "
                "propone o que surge del grupo en la realización de "
                "producciones artísticas colectivas. (S.4., J.2., I.2., "
                "I.4.)"
            ),
            codigo="I.ECA.1.4.2.",
            criterio_evaluacion=criterio1_4
        ),
        # Elemental
        Indicador(
            description=(
                "Observa y explora las características y posibilidades de su "
                "propio cuerpo, en reposo y en movimiento, usa el "
                "conocimiento de sí mismo para expresarse y representarse "
                "empleando distintos materiales, y reflexiona sobre los "
                "resultados obtenidos. (I.2., S.3.)"
            ),
            codigo="I.ECA.2.1.1.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Describe los rasgos característicos de personas de su "
                "entorno y de personas representadas en objetos artesanales, "
                "esculturas o imágenes de su contexto próximo. (S.2., I.2.)"
            ),
            codigo="I.ECA.2.1.2.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Identifica las cualidades de elementos del entorno natural "
                "y artificial, como resultado de un proceso de exploración "
                "sensorial, y recrea sus posibilidades a través del "
                "movimiento y la representación visual y sonora. (I.2.,S.3.)"
            ),
            codigo="I.ECA.2.2.1.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Usa la información obtenida de un proceso de exploración "
                "sensorial para seleccionar los materiales adecuados para la "
                "elaboración de productos sonoros, plásticos, gastronómicos, "
                "etc. (S.3., I.3.)"
            ),
            codigo="I.ECA.2.2.2.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Observa y comenta las características de representaciones "
                "del entorno natural y artificial, y de objetos y obras "
                "artísticas construidos con los elementos de dichos "
                "entornos. (S.3., I.2.)"
            ),
            codigo="I.ECA.2.3.1.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Utiliza diversas técnicas para la representación del "
                "entorno natural y artificial. (J.2., S.3.)"
            ),
            codigo="I.ECA.2.3.2.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Toma como modelo objetos y creaciones artísticas para la "
                "elaboración de producciones propias. (J.2.,S.3.)"
            ),
            codigo="I.ECA.2.3.3.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Elabora producciones artísticas basándose en la observación "
                "de otras creaciones, tomadas como referente. (S.3., J.2.)"
            ),
            codigo="I.ECA.2.4.1.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Participa en representaciones escénicas, de movimiento y "
                "musicales, demostrando un dominio elemental de las técnicas "
                "artísticas propias de cada forma de expresión. (S.3., I.2.)"
            ),
            codigo="I.ECA.2.4.2.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Siente curiosidad ante expresiones culturales y artísticas "
                "del entorno próximo y expresa sus puntos de vista a través "
                "de descripciones verbales o comentarios escritos. "
                "(I.2.,I.4.)."
            ),
            codigo="I.ECA.2.5.1.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Realiza registros gráficos, sonoros o audiovisuales de "
                "manifestaciones culturales y artísticas del entorno "
                "próximo, y utiliza dichos registros para la creación de "
                "álbumes, carteles, murales, archivos sonoros, etc. (I.1., "
                "S.3.)"
            ),
            codigo="I.ECA.2.5.2.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Identifica platos típicos de la zona y participa en "
                "procesos de documentación gráfica o escrita. (I.3., S.2.)"
            ),
            codigo="I.ECA.2.6.1.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Busca información sobre la gastronomía local y organiza los "
                "datos obtenidos mediante la creación de planos, "
                "calendarios, cartas, etc. (I.2., I.4.)"
            ),
            codigo="I.ECA.2.6.2.",
            criterio_evaluacion=criterio2_6
        ),
        # Medio
        Indicador(
            description=(
                "Explora, describe y representa la propia imagen y algunos "
                "momentos relevantes de la historia personal a través de "
                "distintos medios de expresión (gestual, gráfico, verbal, "
                "fotográfico, sonoro, etc.). (J.4., S.2., S.3.)"
            ),
            codigo="I.ECA.3.1.1.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Utiliza medios audiovisuales y tecnologías de la "
                "información y la comunicación para realizar y difundir "
                "creaciones artísticas propias. (I.2., S.3.)"
            ),
            codigo="I.ECA.3.1.2.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Utiliza un lenguaje sencillo pero preciso al describir las "
                "características de producciones artísticas realizadas con "
                "objetos artificiales y naturales. (J.3., I.3.)"
            ),
            codigo="I.ECA.3.2.1.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Diseña y planifica los pasos a seguir en la construcción de "
                "títeres e instrumentos musicales tomando en consideración "
                "lo observado en procesos de experimentación con materiales "
                "naturales y artificiales, y seleccionando los más "
                "adecuados. (J.3., S.3.)"
            ),
            codigo="I.ECA.3.2.2.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Participa activamente y aporta ideas en procesos de "
                "interpretación teatral y creación musical, utilizando "
                "títeres e instrumentos musicales construidos con materiales "
                "naturales y de desecho. (J.2., S.3.)"
            ),
            codigo="I.ECA.3.2.3.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Emplea, de forma básica, algunos recursos audiovisuales y "
                "tecnológicos para la creación de animaciones sencillas. "
                "(I.2., I.4.)"
            ),
            codigo="I.ECA.3.2.4.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Identifica y describe diferentes tipos de manifestaciones y "
                "productos en el contexto de la cultura popular, así como su "
                "presencia en los ámbitos cotidianos. (J.1., S.2.)"
            ),
            codigo="I.ECA.3.3.1.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Muestra una actitud de escucha, interés y receptividad "
                "hacia los recuerdos, los conocimientos técnicos y las "
                "opiniones de distintos agentes del arte y la cultura. "
                "(S.2., I.4.)"
            ),
            codigo="I.ECA.3.3.2.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Utiliza los conocimientos adquiridos en procesos de "
                "búsqueda de información, observación y diálogo, para "
                "documentar y dar opiniones informadas sobre manifestaciones "
                "artísticas y culturales. (I.1., I.3.)"
            ),
            codigo="I.ECA.3.3.3.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Describe y comenta la proyección de la propia sombra "
                "corporal y las características del teatro de sombras, como "
                "resultado de un proceso de observación y búsqueda de "
                "información. (S.3., I.4.)"
            ),
            codigo="I.ECA.3.4.1.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Emplea algunos recursos básicos del teatro de sombras en "
                "procesos de creación colectiva e interpretación. (S.1., "
                "S.3.)"
            ),
            codigo="I.ECA.3.4.2.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Relata la historia o la situación sobre la que se "
                "construyen algunas piezas de música descriptiva o "
                "programática escuchadas en el aula con la ayuda de soportes "
                "visuales o audiovisuales. (I.2., I.3.)"
            ),
            codigo="I.ECA.3.5.1.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Contar historias reales o inventadas a través de sonidos, "
                "gestos o movimientos como resultado de un proceso de "
                "creación o improvisación individual o colectiva. (S.3., "
                "I.1.)"
            ),
            codigo="I.ECA.3.5.2.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Reconoce y valora las características fundamentales de las "
                "fiestas de especial relevancia en su comunidad, participa "
                "en su organización y las documenta a través de la captura "
                "de imágenes y videos, o de la selección de recursos "
                "encontrados en Internet. (I.2.,S.1.)"
            ),
            codigo="I.ECA.3.6.1.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Participa activamente en la elaboración de objetos "
                "artesanales, máscaras o vestimentas, y en la interpretación "
                "de bailes y canciones propios de algunas fiestas de "
                "especial relevancia para la comunidad. (J.1., S.1., S.3.)"
            ),
            codigo="I.ECA.3.6.2.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Sitúa en el espacio y el tiempo imágenes y piezas musicales "
                "que evoquen acontecimientos significativos, rituales, "
                "personajes o hechos relevantes. (I.4., S.3.)"
            ),
            codigo="I.ECA.3.6.3.",
            criterio_evaluacion=criterio3_6
        ),
        # Superior
        Indicador(
            description=(
                "Observa con cierta autonomía manifestaciones culturales y "
                "artísticas, y expresa las características de lo observado y "
                "sus puntos de vista en situaciones de diálogo. (I.3., S.1., "
                "S.3.)"
            ),
            codigo="I.ECA.4.1.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Selecciona las fuentes de información más adecuadas para "
                "obtener datos previos y posteriores a una visita cultural. "
                "(I.2., S.3.)"
            ),
            codigo="I.ECA.4.1.2.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Organiza cronológicamente piezas musicales y obras "
                "artísticas de distintas características, elaborando líneas "
                "del tiempo u otros recursos gráficos. (I.3., S.3.)"
            ),
            codigo="I.ECA.4.1.3.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "tiliza técnicas de búsqueda y organización de la "
                "información, métodos sencillos de investigación, técnicas "
                "de entrevista y otros procedimientos adecuados para "
                "adquirir datos relevantes relacionados con distintas formas "
                "de expresión artística y cultural. (I.1., I.4.)"
            ),
            codigo="I.ECA.4.2.1.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Demuestra la comprensión de datos sobre manifestaciones "
                "artísticas y culturales obtenidos en procesos de "
                "observación y búsqueda de información organizándolos y "
                "empleándolos en la elaboración de presentaciones, guías "
                "culturales, dosieres y otros documentos impresos o "
                "digitales. (I.2., S.3.)"
            ),
            codigo="I.ECA.4.2.2.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Analiza y compara datos referidos a la consideración social "
                "e histórica de elementos, formas de expresión o agentes "
                "relacionados con el arte: la figura humana, las mujeres, el "
                "trabajo de artesanas y artesanos, el cine, etc. (I.4., "
                "S.1.)"
            ),
            codigo="I.ECA.4.2.3.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Reconoce y describe algunas características diferenciadoras "
                "en manifestaciones artísticas y culturales. (I.1., S.2.)"
            ),
            codigo="I.ECA.4.2.4.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Aprecia la diversidad de las expresiones culturales y "
                "artísticas del Ecuador y de otras culturas, y aplica con "
                "autonomía criterios de selección y consumo de contenidos. "
                "(I.4., S.2.)"
            ),
            codigo="I.ECA.4.2.5.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Observa y explica las principales características de formas "
                "de expresión artística contemporánea, en las que "
                "intervienen distintos lenguajes (performances, "
                "instalaciones, representaciones teatrales, etc.). (S.3., "
                "I.3.)"
            ),
            codigo="I.ECA.4.3.1.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Aplica los conocimientos sobre instalaciones y performance "
                "en procesos de creación colectiva. (J.2., S.2., S.3.)"
            ),
            codigo="I.ECA.4.3.2.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Documenta o describe las principales características de una "
                "instalación artística mediante el registro fotográfico o la "
                "escritura, aportando argumentos y puntos de vista "
                "personales. (I.3., I.4.)"
            ),
            codigo="I.ECA.4.3.3.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Aplica técnicas, recursos y convenciones básicos de los "
                "distintos lenguajes artísticos en la representación de la "
                "figura humana, en representaciones teatrales inspiradas en "
                "poemas o cuentos, en monólogos o en la creación de planos y "
                "maquetas. (J.4., I.4.)."
            ),
            codigo="I.ECA.4.4.1.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Recopila y organiza documentos gráficos, visuales o "
                "audiovisuales que reflejen los gustos y preferencias "
                "personales, y muestras de las propias creaciones para "
                "elaborar diarios y portafolios personales. (J.4., I.4.)"
            ),
            codigo="I.ECA.4.4.2.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Transforma o recrea creaciones artísticas preexistentes "
                "(construcciones, danzas, canciones, etc.) utilizando "
                "técnicas de remezcla, añadiendo elementos del arte "
                "contemporáneo o combinando distintas formas de expresión "
                "(por ejemplo, danza y video; imágenes y expresión corporal, "
                "etc.). (S.3., I.4., J.2.)."
            ),
            codigo="I.ECA.4.4.3.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Organiza de manera coherente un proceso de trabajo de "
                "interpretación o creación artística, asumiendo distintos "
                "roles y esforzándose por respetar sus fases. (S.3.,I.4.)"
            ),
            codigo="I.ECA.4.5.1.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Demuestra la capacidad de aplicar conocimientos y técnicas "
                "en procesos de autoaprendizaje, diseño y desarrollo de "
                "proyectos artísticos. (S.3., I.4.)."
            ),
            codigo="I.ECA.4.5.2.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Busca, analiza y selecciona información relacionada con el "
                "arte y la cultura para construir conocimiento y utilizarla "
                "en investigaciones y en la elaboración de diaporamas, "
                "pequeñas producciones audiovisuales, presentaciones "
                "multimedia, etc. (I.2., S.1.)"
            ),
            codigo="I.ECA.4.6.1.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Utiliza las posibilidades que ofrecen los medios "
                "audiovisuales y recursos tecnológicos a su alcance para la "
                "creación individual o colectiva, y para la difusión de "
                "contenidos artísticos, exponiéndolos ante un público "
                "global. (I.3., S.3.)"
            ),
            codigo="I.ECA.4.6.2.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Elabora producciones audiovisuales y/o multimedia, "
                "originales o derivadas de la remezcla o reelaboración de "
                "contenidos existentes, reconociendo la aportación de los "
                "creadores originales y la riqueza de las nuevas versiones. "
                "(S.3., I.4., J.3.)"
            ),
            codigo="I.ECA.4.6.3.",
            criterio_evaluacion=criterio4_6
        ),
        # Bachillerato
        Indicador(
            description=(
                "Reconoce y describe los elementos, personajes, símbolos, "
                "técnicas e ideas principales de producciones artísticas de "
                "distintas épocas y culturas, y las asocia con formas de "
                "pensar, movimientos estéticos y modas. (I.2., S.3.)"
            ),
            codigo="I.ECA.5.1.1.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Identifica la presencia de las mujeres en algunas "
                "manifestaciones culturales y artísticas, e infiere y "
                "describe sus funciones (autoras, intérpretes, directoras, "
                "artesanas, presentes como motivo de representación, etc.). "
                "(I.4., S.2.)"
            ),
            codigo="I.ECA.5.1.2.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Investiga con autonomía manifestaciones culturales y "
                "artísticas de distintas épocas y contextos, y utiliza "
                "adecuadamente la información recogida de diferentes fuentes "
                "en debates, en la elaboración de críticas escritas, usando "
                "un lenguaje apropiado, y en la elaboración de producciones "
                "artísticas, audiovisuales y multimedia. (I.2., J.3.)"
            ),
            codigo="I.ECA.5.1.3.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Observa producciones artísticas (artes visuales, cine, "
                "publicidad, fotografía, música, teatro, etc.) de distintas "
                "características, reflexiona sobre los recursos utilizados "
                "para expresar ideas y para generar emociones en el "
                "espectador, y crea presentaciones, sonorizaciones y otras "
                "producciones para explicar o aplicar lo aprendido durante "
                "los procesos de observación. (S.3., I.1.)"
            ),
            codigo="I.ECA.5.2.1.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Reelabora ideas, transforma producciones de otras personas "
                "y plantea múltiples soluciones para la renovación o "
                "remezcla de producciones artísticas preexistentes. (I.3., "
                "S.3.)"
            ),
            codigo="I.ECA.5.2.2.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Explica algunas diferencias que se perciben en la manera de "
                "representar ideas, gestos, expresiones, emociones o "
                "sentimientos en obras artísticas de distintas épocas y "
                "culturas, y expresa situaciones, ideas y emociones propias "
                "en la elaboración de producciones artísticas y multimedia. "
                "(I.3., I.4.)"
            ),
            codigo="I.ECA.5.2.3.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Organiza de manera coherente un proceso de creación "
                "artística o un evento cultural, y hace un esfuerzo por "
                "mantener sus fases, realizando los ajustes necesarios "
                "cuando se presentan problemas. (J.4., S.4.)"
            ),
            codigo="I.ECA.5.3.1.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Argumenta razonadamente el proceso seguido en la "
                "elaboración de una producción artística o en la "
                "organización de un evento cultural, valora y autoevalúa su "
                "propio trabajo, y propone modificaciones y mejoras como "
                "resultado del proceso de autoreflexión y del intercambio de "
                "ideas con el público u otros especialistas.(I.1.,J.3.)"
            ),
            codigo="I.ECA.5.3.2.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Desarrolla una nueva destreza o elabora una producción "
                "artística como resultado de un proceso de autoaprendizaje, "
                "utilizando fuentes seleccionadas por el estudiante. (I.4., "
                "S.3.)"
            ),
            codigo="I.ECA.5.3.3.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Conoce las técnicas, recursos y convenciones de los "
                "distintos lenguajes artísticos y los utiliza de forma "
                "adecuada en sus producciones, buscando soluciones y "
                "aplicando estrategias para expresar ideas, sentimientos y "
                "emociones. (I.2., S.3.)"
            ),
            codigo="I.ECA.5.3.4.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Asume el trabajo compartido con responsabilidad, respetando "
                "las intervenciones y aportaciones de los demás, y "
                "colaborando en la elaboración de un proyecto artístico "
                "colectivo, desde la idea inicial hasta su conclusión. "
                "(S.1., S.4.)"
            ),
            codigo="I.ECA.5.3.5.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Selecciona los recursos más adecuados (fotografía, "
                "presentaciones multimedia, documentos escritos, videos, "
                "etc.) para documentar los procesos de creación artística o "
                "los eventos culturales, y los publica y difunde utilizando "
                "los medios adecuados. (I.3., S.3.)"
            ),
            codigo="I.ECA.5.3.6.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Selecciona, ordena y reúne muestras significativas de las "
                "producciones realizadas en un portafolio, blog, catálogo u "
                "otro recurso digital adecuado para presentar y reflexionar "
                "sobre las creaciones artísticas propias. (I.4., S.3.)"
            ),
            codigo="I.ECA.5.4.1.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Utiliza diferentes recursos audiovisuales y tecnológicos en "
                "la elaboración de catálogos de profesiones relacionadas con "
                "el arte y la cultura, la producción de audiovisuales en las "
                "que algunos profesionales ofrezcan testimonios sobre su "
                "trabajo, y la difusión de jornadas y otros eventos que "
                "ayuden a conocer el trabajo de artistas y agentes de la "
                "cultura. (I.3., S.3.)"
            ),
            codigo="I.ECA.5.4.2.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Reconoce el papel que desempeñan las tecnologías de la "
                "información y la comunicación a la hora de crear, "
                "almacenar, distribuir y acceder a manifestaciones "
                "culturales y artísticas, y utilizarlas para las creaciones "
                "y la difusión del propio trabajo. (I.1., I.3., S.3.)"
            ),
            codigo="I.ECA.5.4.3.",
            criterio_evaluacion=criterio5_4
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0048_auto_20180815_1730'),
    ]

    operations = [
        migrations.RunPython(create_indicadores)
    ]
