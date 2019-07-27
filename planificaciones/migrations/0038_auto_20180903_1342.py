from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

    # Criterios de evaluación
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.6.")
    criterio2_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.7.")
    criterio2_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.8.")
    criterio2_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.9.")
    criterio2_10 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.10.")
    criterio2_11 = CriterioEvaluacion.objects.get(codigo="CE.CN.2.11.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.8.")
    criterio3_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.9.")
    criterio3_10 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.10.")
    criterio3_11 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.11.")
    criterio3_12 = CriterioEvaluacion.objects.get(codigo="CE.CN.3.12.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.8.")
    criterio4_9 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.9.")
    criterio4_10 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.10.")
    criterio4_11 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.11.")
    criterio4_12 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.12.")
    criterio4_13 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.13.")
    criterio4_14 = CriterioEvaluacion.objects.get(codigo="CE.CN.4.14.")

    Indicador.objects.bulk_create([
        # Elemental
        Indicador(
            description=(
                "Explica el ciclo vital del ser humano, plantas y animales "
                "(insectos, peces, anfibios, reptiles, aves y mamíferos), "
                "desde la identificación de los cambios que se producen en "
                "sus etapas e importancia. (J.2., J.3.)"
            ),
            codigo="I.CN.2.1.1.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Explica la importancia de la polinización y dispersión de "
                "las semillas en el ciclo vital de las plantas, a partir de "
                "experiencias sencillas de germinación. (J.3., I.2.)"
            ),
            codigo="I.CN.2.1.2.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Clasifica a los animales en vertebrados e invertebrados, en "
                "función de la presencia o ausencia de columna vertebral y "
                "sus características externas (partes del cuerpo, cubierta "
                "corporal, tamaño, forma de desplazarse, alimentación). A su "
                "vez, agrupa a los vertebrados según sus características, "
                "examina su utilidad para el ser humano y su relación con el "
                "hábitat en donde se desarrollan. (J.3., I.2.)"
            ),
            codigo="I.CN.2.2.1.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Clasifica a las plantas en angiospermas y gimnospermas en "
                "función de sus semejanzas y diferencias. Describe sus "
                "partes, las clasifica según su estrato (árbol, arbusto y "
                "hierba), y usos (industriales, medicinales y ornamentales). "
                "Expone el aporte al conocimiento científico que realizó el "
                "ecuatoriano Misael Acosta Solís, a partir del estudio de la "
                "flora ecuatoriana. (J.3., S.4.)"
            ),
            codigo="I.CN.2.2.2.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Clasifica los hábitats locales según sus características y "
                "diversidad de vertebrados y plantas con semilla que "
                "presenten. (J.1., J.3.)"
            ),
            codigo="I.CN.2.3.1.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Propone medidas de protección para la conservación de los "
                "hábitats locales, en función de identificar las amenazas y "
                "cambios a los que está expuesta la diversidad de plantas y "
                "animales de las regiones naturales del Ecuador. (.J3., "
                "I.1.)"
            ),
            codigo="I.CN.2.3.2.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Explica con lenguaje claro y pertinente, la ubicación del "
                "cerebro, pulmones, corazón, esqueleto, músculos y "
                "articulaciones en su cuerpo; y sus respectivas funciones "
                "(soporte, movimiento y protección), estructura y relación "
                "con el mantenimiento de la vida. (J3, I3)"
            ),
            codigo="I.CN.2.4.1.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Explica la importancia de mantener una vida saludable en "
                "función de la comprensión de habituarse a una dieta "
                "alimenticia equilibrada, realizar actividad física según la "
                "edad, cumplir con normas de higiene corporal y el adecuado "
                "manejo de alimentos en sus actividades cotidianas, dentro "
                "del hogar como fuera de él. (J3, S1)"
            ),
            codigo="I.CN.2.4.2.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Demuestra a partir de la experimentación con diferentes "
                "objetos del entorno los estados de la materia (sólido, "
                "líquido y gaseoso) y sus cambios frente a la variación de "
                "la temperatura. (J.3., I.2.)"
            ),
            codigo="I.CN.2.5.1.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Demuestra a partir de la ejecución de experimentos "
                "sencillos y uso de instrumentos y unidades de medida, las "
                "propiedades de la materia (masa, peso, volumen) los tipos "
                "(sustancias puras y mezclas naturales y artificiales) y "
                "empleando técnicas sencillas separa mezclas que se usan en "
                "su vida cotidiana. (J.3., I.2.)"
            ),
            codigo="I.CN.2.5.2.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Demuestra a partir del uso de máquinas simples, el "
                "movimiento (rapidez y dirección) de los objetos en función "
                "de la acción de una fuerza. (J.3., I.2.)"
            ),
            codigo="I.CN.2.6.1.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Explica a partir de la experimentación el movimiento de los "
                "objetos en función de la acción de la fuerza de la "
                "gravedad. (J.3., I.2.)"
            ),
            codigo="I.CN.2.6.2.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Explica desde su propia experiencia las fuentes (sol, agua, "
                "viento, olas, volcanes, biomasa, gas natural), formas "
                "(cinética, potencial, térmica, lumínica, química, sonora, "
                "eléctrica) y transformación (calor, luz, sonido, y "
                "movimiento) de la energía y su importancia para el "
                "movimiento de los cuerpos y la realización de todo tipo de "
                "trabajo. (J.3.,S.3.)"
            ),
            codigo="I.CN.2.7.1.",
            criterio_evaluacion=criterio2_7
        ),
        Indicador(
            description=(
                "Diferencia objetos luminosos y no luminosos, transparentes "
                "y opacos, según las características de la luz; la sombra y "
                "penumbra, según el bloqueo de luz; y su propagación en "
                "diferentes medios. (J.3., I.3.)"
            ),
            codigo="I.CN.2.8.1.",
            criterio_evaluacion=criterio2_8
        ),
        Indicador(
            description=(
                "Propone actividades que los seres vivos pueden cumplir "
                "durante el día y la noche (ciclo diario), en función de la "
                "comprensión de la influencia del Sol (forma, tamaño. "
                "posición), la Luna (forma, tamaño, movimiento, fases) y las "
                "estrellas sobre la Tierra (forma, tamaño, movimiento) y el "
                "clima. (J.3., I.2.)"
            ),
            codigo="I.CN.2.9.1.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Aprecia los conocimientos ancestrales sobre la influencia "
                "del Sol, la Luna y la tecnología agrícola, aplicada por las "
                "culturas indígenas, pueblo afroecuatoriano y montubio en la "
                "agricultura tradicional. (J.3., S.2.)"
            ),
            codigo="I.CN.2.9.2.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Describir y representar los instrumentos tecnológicos y "
                "ancestrales usados para la observación astronómica, la "
                "predicción del tiempo y los fenómenos atmosféricos. (J.3., "
                "S.2.)"
            ),
            codigo="I.CN.2.9.3.",
            criterio_evaluacion=criterio2_9
        ),
        Indicador(
            description=(
                "Clasifica a los recursos naturales en renovables y no "
                "renovables en función de sus características, importancia, "
                "usos y propone razones para realizar la explotación "
                "controlada en las regiones naturales del país. (J.3., I.4.)"
            ),
            codigo="I.CN.2.10.1.",
            criterio_evaluacion=criterio2_10
        ),
        Indicador(
            description=(
                "Analiza las características, formación, clasificación y "
                "causas del deterioro del suelo y propone estrategias de "
                "conservación para este recurso natural. (J.3., I.2.)"
            ),
            codigo="I.CN.2.11.1.",
            criterio_evaluacion=criterio2_11
        ),
        Indicador(
            description=(
                "Analiza, a partir de la indagación en diversas fuentes, la "
                "importancia del agua, el ciclo, usos, proceso de "
                "potabilización y la utilización de tecnologías limpias para "
                "su manejo y conservación. (J.3., I.2.)"
            ),
            codigo="I.CN.2.11.2.",
            criterio_evaluacion=criterio2_11
        ),
        # Media
        Indicador(
            description=(
                "Identifica a los invertebrados representativos de las "
                "regiones naturales del Ecuador, en función de sus "
                "semejanzas y diferencias, su diversidad, las amenazas a las "
                "que están expuestos y propone medidas para su protección. "
                "(J.3., I.1.)"
            ),
            codigo="I.CN.3.1.1.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Identifica las diferencias e importancia del ciclo "
                "reproductivo (sexual y asexual) de los vertebrados e "
                "invertebrados de las regiones naturales del Ecuador, para "
                "el mantenimiento de la vida. (J.3.)"
            ),
            codigo="I.CN.3.1.2.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Explica con lenguaje claro y apropiado la importancia de "
                "los procesos de fotosíntesis, nutrición, respiración, "
                "relación con la humedad del suelo e importancia para el "
                "ambiente. (J.3., I.3.)"
            ),
            codigo="I.CN.3.2.1.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Explica el proceso de reproducción de las plantas a partir "
                "de reconocer sus estructuras, las fases, los factores y/o "
                "los agentes que intervienen en la fecundación, reconoce su "
                "importancia para el mantenimiento de la vida, y mediante "
                "trabajo colaborativo propone medidas de protección y "
                "cuidado. (J.3., I.1., S.4.)"
            ),
            codigo="I.CN.3.2.2.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Examina la dinámica de los ecosistemas en función de sus "
                "características, clases, diversidad biológica, adaptación "
                "de especies y las interacciones (interespecíficas e "
                "intraespecíficas), que en ellos se producen. (J.3.)"
            ),
            codigo="I.CN.3.3.1.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Determina desde la observación e investigación guiada, las "
                "causas y consecuencias de la alteración de los ecosistemas "
                "locales e infiere el impacto en la calidad del ambiente. "
                "(J.3., I.2.)"
            ),
            codigo="I.CN.3.3.2.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Plantea y comunica medidas de protección (manejo de "
                "desechos sólidos), hacia los ecosistemas y las especies "
                "nativas amenazadas en las Áreas Naturales Protegidas del "
                "Ecuador, afianzando su propuesta en los aportes científicos "
                "de investigadores locales. (J.3., I.1., I.3.)"
            ),
            codigo="I.CN.3.3.3.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Establece relaciones entre el sistema reproductivo, "
                "endócrino y nervioso, a partir de su estructura, funciones "
                "e influencia en los cambios que se presentan en la "
                "pubertad. (J.3., J.4.)"
            ),
            codigo="I.CN.3.4.1.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Argumenta los cambios (fisiológicos, anatómicos y "
                "conductuales) que se producen durante la pubertad y los "
                "aspectos (biológicos, psicológicos y sociales) que "
                "determinan la sexualidad como manifestación humana. "
                "(J.3.,J.4.)"
            ),
            codigo="I.CN.3.4.2.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Explica la estructura, función y relación que existe entre "
                "el aparato digestivo, respiratorio, excretor, reproductor y "
                "los órganos de los sentidos, desde la observación de "
                "representaciones analógicas o digitales y modelado de "
                "estructuras.(J.3., I.2.)"
            ),
            codigo="I.CN.3.5.1.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Promueve medidas de prevención y cuidado (actividad física, "
                "higiene corporal, dieta equilibrada) hacia su cuerpo, "
                "conociendo el daño que puede provocar el consumo de "
                "sustancias nocivas y los desórdenes alimenticios (bulimia, "
                "anorexia) en los sistemas digestivo, respiratorio, "
                "circulatorio, excretor y reproductor. Reconoce la "
                "contribución de la medicina ancestral y la medicina moderna "
                "para el tratamiento de enfermedades y mantenimiento de la "
                "salud integral. (J.3., S.2.)"
            ),
            codigo="I.CN.3.5.2.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Explica desde la observación de diferentes representaciones "
                "cómo las teorías sobre la composición de la materia han "
                "evolucionado, hasta comprender que está constituida por "
                "átomos, elementos y moléculas. (J.3.)"
            ),
            codigo="I.CN.3.6.1.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Clasifica la materia en sustancias puras y mezclas. Además, "
                "reconoce las mezclas homogéneas y heterogéneas desde la "
                "manipulación de bebidas tradicionales del país. (J.3., "
                "S.2.)"
            ),
            codigo="I.CN.3.6.2.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Demuestra, a partir de la exploración de sustancias de uso "
                "cotidiano (bebidas tradicionales), las propiedades de la "
                "materia y de los compuestos químicos orgánicos e "
                "inorgánicos. (J.3., S.2.)"
            ),
            codigo="I.CN.3.6.3.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Describe los tipos de fuerza y el cambio de forma, rapidez "
                "y dirección del movimiento de los objetos, desde la "
                "exploración y experimentación en objetos de uso cotidiano. "
                "(J.3.)"
            ),
            codigo="I.CN.3.7.1.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Establece diferencias entre calor y temperatura y comunica, "
                "de forma gráfica, las formas de transmisión del calor "
                "(conducción, convección y radiación), apoyándose en la "
                "ejecución de experimentos sencillos de varias sustancias y "
                "cuerpos de su entorno. (J.3., I.2., I.3.)"
            ),
            codigo="I.CN.3.8.1.",
            criterio_evaluacion=criterio3_8
        ),
        Indicador(
            description=(
                "Analiza las características, importancia, aplicaciones y "
                "fundamentos del magnetismo, de la energía térmica y de la "
                "energía eléctrica. (J.3., I.2.)"
            ),
            codigo="I.CN.3.9.1.",
            criterio_evaluacion=criterio3_9
        ),
        Indicador(
            description=(
                "Explica la importancia de la transformación de la energía "
                "eléctrica, así como la necesidad de realizar estudios "
                "ambientales y sociales para mitigar los impactos de las "
                "centrales hidroeléctricas en el ambiente. (J.3., I.2.)"
            ),
            codigo="I.CN.3.9.2.",
            criterio_evaluacion=criterio3_9
        ),
        Indicador(
            description=(
                "Analiza la estructura de la Tierra (capas, componentes) "
                "como parte del sistema solar y su órbita, con respecto al "
                "Sol y el resto de planetas. (J.3.)"
            ),
            codigo="I.CN.3.10.1.",
            criterio_evaluacion=criterio3_10
        ),
        Indicador(
            description=(
                "Explica el proceso de formación de la Cordillera de los "
                "Andes y la biodiversidad de especies en las regiones "
                "naturales del Ecuador, en función de la comprensión del "
                "movimiento de las placas tectónicas como fenómeno "
                "geológico, y de las contribuciones científicas y "
                "tecnológicas en el campo de la vulcanología nacional. "
                "(J.1., J.3.)"
            ),
            codigo="I.CN.3.10.2.",
            criterio_evaluacion=criterio3_10
        ),
        Indicador(
            description=(
                "Interpreta los patrones de calentamiento de la superficie "
                "terrestre a causa de la energía del Sol y su relación con "
                "la formación de los vientos, nubes y lluvia, según su "
                "ubicación geográfica. (J.3., I.2.)."
            ),
            codigo="I.CN.3.11.1.",
            criterio_evaluacion=criterio3_11
        ),
        Indicador(
            description=(
                "Analiza la incidencia de la radiación solar sobre la "
                "superficie terrestre y determina la importancia del Sol "
                "como fuente de energía renovable. (J.3., S.3.)"
            ),
            codigo="I.CN.3.11.2.",
            criterio_evaluacion=criterio3_11
        ),
        Indicador(
            description=(
                "Propone medidas de protección ante los rayos UV, de acuerdo "
                "con la comprensión de las funciones de las capas "
                "atmosféricas y la importancia de la capa de ozono. (J.2., "
                "J.3., S.1.)"
            ),
            codigo="I.CN.3.12.1.",
            criterio_evaluacion=criterio3_12
        ),
        Indicador(
            description=(
                "Explica las causas y consecuencias de las catástrofes "
                "climáticas a partir del conocimiento de las "
                "características, elementos y factores del clima, "
                "considerando datos meteorológicos locales y características "
                "del clima en las diferentes regiones naturales del Ecuador. "
                "(J.3.)"
            ),
            codigo="I.CN.3.12.2.",
            criterio_evaluacion=criterio3_12
        ),
        Indicador(
            description=(
                "Formula una investigación sencilla del estado de la calidad "
                "del aire, en función de la comprensión de su importancia "
                "para la vida, sus propiedades, las funciones y efectos de "
                "la contaminación en el ambiente. (J.3., S.3.)"
            ),
            codigo="I.CN.3.12.3.",
            criterio_evaluacion=criterio3_12
        ),
        # Superior
        Indicador(
            description=(
                "Analiza el nivel de complejidad de la materia viva y los "
                "organismos, en función de sus propiedades y niveles de "
                "organización. (J.3.)"
            ),
            codigo="I.CN.4.1.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Clasifica seres vivos según criterios taxonómicos dados "
                "(dominio y reino) y establece relación entre el grupo "
                "taxonómico y los niveles de organización que presenta y su "
                "diversidad. (J.3., I.2.)"
            ),
            codigo="I.CN.4.1.2.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Determina la complejidad de las células en función de sus "
                "características estructurales, funcionales y tipos e "
                "identifica las herramientas tecnológicas que contribuyen al "
                "conocimiento de la citología. (J.3., I.2.)"
            ),
            codigo="I.CN.4.2.1.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Diferencia las clases de tejidos, animales y vegetales, de "
                "acuerdo a características, funciones y ubicación e "
                "identifica la contribución del microscopio para el "
                "desarrollo de la histología. (J.3., I.2.)"
            ),
            codigo="I.CN.4.2.2.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Explica el ciclo celular de diferentes tipos de células, su "
                "importancia para la formación de tejidos animales, tejidos "
                "vegetales y gametos e identifica la contribución "
                "tecnológica al conocimiento de la estructura y procesos que "
                "cumplen los seres vivos. (J3, I2)"
            ),
            codigo="I.CN.4.2.3.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Diferencia la reproducción sexual de la asexual y determina "
                "la importancia para la supervivencia de diferentes "
                "especies. (J.3., S.1.)"
            ),
            codigo="I.CN.4.2.4.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Elabora la representación de una red alimenticia (por "
                "ejemplo, el manglar) en la que se identifican cadenas "
                "alimenticias conformadas por organismos productores, "
                "consumidores y descomponedores. (J.3., J.4.)"
            ),
            codigo="I.CN.4.3.1.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Relaciona el desarrollo de los ciclos de carbono, oxígeno y "
                "nitrógeno con el flujo de energía como mecanismo de "
                "reciclaje de estos elementos, y el funcionamiento de las "
                "cadenas tróficas en los ecosistemas. (J.3., J.1.)"
            ),
            codigo="I.CN.4.3.2.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Formula hipótesis pertinentes sobre el impacto de la "
                "actividad humana en la dinámica de los ecosistemas y en la "
                "relación clima-vegetación. (J.3., J.2.)"
            ),
            codigo="I.CN.4.3.3.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Identifica, desde la observación de diversas fuentes, los "
                "ecosistemas de Ecuador y biomas del mundo, en función de la "
                "importancia, ubicación geográfica, clima y biodiversidad "
                "que presentan. (J.3., J.1.)"
            ),
            codigo="I.CN.4.4.1.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Argumenta, desde la investigación de diferentes fuentes, la "
                "importancia de las áreas protegidas como mecanismo de "
                "conservación de la vida silvestre, de investigación y "
                "educación, deduciendo el impacto de la actividad humana en "
                "los hábitats y ecosistemas. Propone medidas para su "
                "protección y conservación. (J.1., J.3., I.1.)"
            ),
            codigo="I.CN.4.4.2.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Analiza los procesos y cambios evolutivos en los seres "
                "vivos, como efecto de la selección natural y de eventos "
                "geológicos, a través de la descripción de evidencias: "
                "registros fósiles, deriva continental y la extinción masiva "
                "de la especies. (J.3.)"
            ),
            codigo="I.CN.4.5.1.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Infiere la importancia del estudio de los procesos "
                "geológicos y sus efectos en la Tierra, en función del "
                "análisis de las eras y épocas geológicas de la Tierra, "
                "determinadas a través del fechado radiactivo y sus "
                "aplicaciones. (J.3.)"
            ),
            codigo="I.CN.4.5.2.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Entiende los riesgos de una maternidad/paternidad prematura "
                "según su proyecto de vida, partiendo del análisis de las "
                "etapas de la reproducción humana, la importancia del "
                "cuidado prenatal y la lactancia. (J.3., J.4., S.1.)"
            ),
            codigo="I.CN.4.6.1.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Analiza desde diferentes fuentes (estadísticas actuales del "
                "país) las causas y consecuencia de infecciones de "
                "transmisión sexual, los tipos de infecciones (virales, "
                "bacterianas y micóticas), las medidas de prevención, su "
                "influencia en la salud reproductiva y valora los programas "
                "y campañas de salud sexual del entorno. (J.3., J.4., S.1.)"
            ),
            codigo="I.CN.4.6.2.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Propone medidas de prevención, a partir de la comprensión "
                "de las formas de contagio, propagación de las bacterias y "
                "su resistencia a los antibióticos; de su estructura, "
                "evolución, función del sistema inmunitario, barreras "
                "inmunológicas (primarias, secundarias y terciarias) y los "
                "tipos de inmunidad (natural, artificial, activa y "
                "pasiva).(J.3., I.1.)"
            ),
            codigo="I.CN.4.7.1.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Propone medidas de prevención (uso de vacunas), a partir de "
                "la comprensión de las formas de contagio y propagación de "
                "los virus, sus características, estructura, formas de "
                "transmisión y reconoce otros organismos patógenos que "
                "afectan al ser humano de forma transitoria y permanente "
                "(hongos ectoparásitos y endoparásitos). (J.3.,I.1.)"
            ),
            codigo="I.CN.4.7.2.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Relaciona el cambio de posición de los objetos en función "
                "de las fuerzas equilibradas y fuerzas no equilibradas "
                "(posición, rapidez, velocidad, magnitud, dirección y "
                "aceleración) que actúan sobre ellos. (J.3.)"
            ),
            codigo="I.CN.4.8.1.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Determina la velocidad que alcanza un objeto a partir de la "
                "relación entre el espacio recorrido y el tiempo "
                "transcurrido. (J.3.)"
            ),
            codigo="I.CN.4.8.2.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Determina la relación entre densidad de objetos (sólidos, "
                "líquidos y gaseosos), la flotación o hundimiento de "
                "objetos, y el efecto de la presión sobre los fluidos "
                "(líquidos y gases). (J.3.)"
            ),
            codigo="I.CN.4.9.1.",
            criterio_evaluacion=criterio4_9
        ),
        Indicador(
            description=(
                "Explica con lenguaje claro y pertinente el efecto de la "
                "presión atmosférica sobre varios objetos (sólidos, líquidos "
                "y gases), sus aplicaciones y la relación con la presión "
                "absoluta y la presión manométrica. (J.3., I.3.)"
            ),
            codigo="I.CN.4.9.2.",
            criterio_evaluacion=criterio4_9
        ),
        Indicador(
            description=(
                "Establece diferencias entre el efecto de la fuerza "
                "gravitacional de la Tierra (interpreta la ley de Newton) "
                "con la fuerza gravitacional del Sol en relación a los "
                "objetos que los rodean, fortaleciendo su estudio con los "
                "aportes a la ley de la gravitación universal de Pedro "
                "Vicente Maldonado. (J.3.)"
            ),
            codigo="I.CN.4.10.1.",
            criterio_evaluacion=criterio4_10
        ),
        Indicador(
            description=(
                "Establece diferencia entre materia orgánica e inorgánica en "
                "función de las características y propiedades que presentan "
                "y relaciona la materia orgánica con las biomoléculas. "
                "(J.3.)"
            ),
            codigo="I.CN.4.11.1.",
            criterio_evaluacion=criterio4_11
        ),
        Indicador(
            description=(
                "Establece la importancia del carbono (propiedades físicas y "
                "químicas) como elemento constitutivo de las biomoléculas y "
                "su importancia para los seres vivos, desde la comprensión "
                "de sus características y propiedades físicas y químicas. "
                "(J.3.)"
            ),
            codigo="I.CN.4.11.2.",
            criterio_evaluacion=criterio4_11
        ),
        Indicador(
            description=(
                "Diferencia entre los componentes del Universo (galaxias, "
                "planetas, satélites, cometas, asteroides, tipos de "
                "estrellas y sus constelaciones), de acuerdo a la estructura "
                "y origen que presentan, a partir del uso de diversos "
                "recursos de información. (J.3.)"
            ),
            codigo="I.CN.4.12.1.",
            criterio_evaluacion=criterio4_12
        ),
        Indicador(
            description=(
                "Explica la relación entre la posición relativa del Sol, la "
                "Tierra y la Luna, con el desarrollo de algunos fenómenos "
                "astronómicos, apoyando su estudio en la revisión de la "
                "historia de la astronomía en diversa fuentes analógicos y/o "
                "digitales. (J.3.)"
            ),
            codigo="I.CN.4.12.2.",
            criterio_evaluacion=criterio4_12
        ),
        Indicador(
            description=(
                "Determina, desde la observación de modelos e información de "
                "diversas fuentes, la interacción de los ciclos "
                "biogeoquímicos en un ecosistema y deduce los impactos que "
                "producirían las actividades humanas en estos "
                "espacios.(J.3., I.4.)"
            ),
            codigo="I.CN.4.13.1.",
            criterio_evaluacion=criterio4_13
        ),
        Indicador(
            description=(
                "Analiza los efectos de la alteración de las corrientes "
                "marinas en el cambio climático, y a su vez, el impacto de "
                "las actividades humanas en los ecosistemas y la sociedad, "
                "apoyando su estudio en la revisión de diversas fuentes. "
                "(J.3., I.4.)"
            ),
            codigo="I.CN.4.13.2.",
            criterio_evaluacion=criterio4_13
        ),
        Indicador(
            description=(
                "Explica, desde el estudio de teorías y análisis de "
                "evidencias, el movimiento de placas tectónicas, su relación "
                "con los procesos de erupciones volcánicas e infiere los "
                "efectos en el clima y la distribución de organismos en los "
                "ecosistemas. (J.3., J.1.)"
            ),
            codigo="I.CN.4.14.1.",
            criterio_evaluacion=criterio4_14
        ),
        Indicador(
            description=(
                "Explica el proceso de formación de las rocas y su relación "
                "con los procesos eruptivos en la corteza terrestre. (J.3.)"
            ),
            codigo="I.CN.4.14.2.",
            criterio_evaluacion=criterio4_14
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0037_auto_20180825_1443'),
    ]

    operations = [
        migrations.RunPython(create_indicadores,
                             reverse_code=migrations.RunPython.noop)
    ]
