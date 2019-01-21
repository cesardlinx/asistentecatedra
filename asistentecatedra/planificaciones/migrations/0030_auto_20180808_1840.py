from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignatura
    ciencias_naturales = Asignatura.objects.get(name='Ciencias Naturales')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    CriterioEvaluacion.objects.bulk_create([
        # Preparatoria
        CriterioEvaluacion(
            description=(
                "Explica desde su propia experiencia las características "
                "(crecer, reproducirse, responder a estímulos), necesidades "
                "(alimento, aire, agua), hábitat e importancia de los seres "
                "vivos (ser humano, animales domésticos y silvestres, "
                "plantas cultivadas y silvestres), los diferencia de la "
                "materia inerte (natural y creada) y comunica formas de "
                "cuidado y respeto."
            ),
            codigo="CE.CN.1.1.",
            asignatura=ciencias_naturales,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Relaciona los órganos de los sentidos con las funciones, "
                "percepciones de su entorno y sensaciones de las partes "
                "principales de su cuerpo, para establecer hábitos de vida "
                "saludable (higiene corporal, alimentación sana, juego y "
                "descanso) que incluyan medidas de prevención para una buena "
                "salud de las personas."
            ),
            codigo="CE.CN.1.2.",
            asignatura=ciencias_naturales,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Explica las propiedades físicas, tipo de materiales, "
                "movimiento ante una fuerza ejercida y los cambios que se "
                "producen ante agentes naturales(calor, luz, agua y fuerza), "
                "en objetos de uso cotidiano."
            ),
            codigo="CE.CN.1.3.",
            asignatura=ciencias_naturales,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Explica, desde la observación y percepción, las principales "
                "fuentes de luz y sonido en función del origen (natural y "
                "artificial, débil y fuerte) y emite la diferencia entre "
                "sonido y ruido."
            ),
            codigo="CE.CN.1.4.",
            asignatura=ciencias_naturales,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Aprecia el paisaje local desde la identificación de las "
                "características de los elementos naturales y construidos, "
                "el tiempo atmosférico y sus cambios y efectos en los seres "
                "vivos."
            ),
            codigo="CE.CN.1.5.",
            asignatura=ciencias_naturales,
            subnivel=preparatoria
        ),
        # Elemental
        CriterioEvaluacion(
            description=(
                "Analiza la importancia del ciclo vital de los seres "
                "vivos(humanos, animales y plantas) a partir de la "
                "observación y/o experimentación de sus cambios y etapas, "
                "destacando la importancia de la polinización y dispersión "
                "de las semillas."
            ),
            codigo="CE.CN.2.1.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Aprecia la diversidad de plantas y animales, en función de "
                "la comprensión de sus características, funciones, "
                "importancia, relación con el hábitat en donde se "
                "desarrollan, identificación de las contribuciones de la "
                "flora ecuatoriana al avance científico y utilidad para el "
                "ser humano."
            ),
            codigo="CE.CN.2.2.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Propone medidas de protección y cuidado hacia los hábitat "
                "locales y de las regiones naturales del Ecuador, desde la "
                "comprensión de las características, la diversidad de "
                "vertebrados y plantas con semilla, las reacciones de los "
                "seres vivos a los cambios y amenazas a las que están "
                "expuestos."
            ),
            codigo="CE.CN.2.3.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Promueve estrategias para mantener una vida saludable, a "
                "partir de la comprensión del funcionamiento y estructura "
                "del cerebro, el corazón, los pulmones, el estómago, el "
                "esqueleto, los músculos y las articulaciones, la necesidad "
                "de mantener una dieta equilibrada, una correcta actividad "
                "física, manejar normas de higiene corporal, y un adecuado "
                "manejo de alimentos en sus actividades cotidianas en su "
                "hogar y fuera de él."
            ),
            codigo="CE.CN.2.4.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta a partir de la observación y experimentación con "
                "los objetos (por ejemplo, los usados en la preparación de "
                "alimentos cotidianos); descubren sus propiedades (masa, "
                "volumen, peso), estados físicos cambiantes (sólido, líquido "
                "y gaseoso), y que se clasifican en sustancias puras o "
                "mezclas (naturales y artificiales), que se pueden separar."
            ),
            codigo="CE.CN.2.5.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta desde la observación y experimentación, la "
                "importancia del movimiento y rapidez de los objetos a "
                "partir de la acción de una fuerza en máquinas simples por "
                "acción de la fuerza de la gravedad."
            ),
            codigo="CE.CN.2.6.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Explica desde la observación y exploración las fuentes, "
                "formas y transformación de la energía, reconociendo su "
                "importancia para el movimiento de los cuerpos y la "
                "realización de todo tipo de trabajo en la vida cotidiana."
            ),
            codigo="CE.CN.2.7.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta, a partir de la observación e indagación en "
                "diversas fuentes, las características de la luz, su bloqueo "
                "y propagación en objetos de su entorno inmediato."
            ),
            codigo="CE.CN.2.8.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Propone actividades que los seres vivos podrían hacer "
                "durante el día y la noche, a partir de la comprensión de la "
                "influencia del Sol y la Luna sobre la Tierra, el clima y "
                "los conocimientos ancestrales, y sus conocimientos sobre "
                "herramientas, tecnologías tradicionales usadas para la "
                "agricultura, la observación de los astros, la predicción "
                "del tiempo y los fenómenos atmosféricos."
            ),
            codigo="CE.CN.2.9.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Establece las características, importancia y localización "
                "de los recursos naturales (renovables y no renovables) de "
                "las regiones del Ecuador y emite razones para realizar una "
                "explotación controlada."
            ),
            codigo="CE.CN.2.10.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Propone medidas de prevención y conservación de los "
                "recursos naturales(suelo y agua), a partir del conocimiento "
                "de las características, formación, clasificación y causas "
                "del deterioro del suelo identificar la importancia, el "
                "ciclo, los usos, el proceso de potabilización del agua y la "
                "utilización de tecnologías limpias para su manejo."
            ),
            codigo="CE.CN.2.11.",
            asignatura=ciencias_naturales,
            subnivel=elemental
        ),
        # Media
        CriterioEvaluacion(
            description=(
                "Explica la importancia de los invertebrados, reconociendo "
                "las amenazas a las que están sujetos y proponiendo medidas "
                "para su protección en las regiones naturales del Ecuador, a "
                "partir de la observación e indagación guiada y en función "
                "de la comprensión de sus características, clasificación, "
                "diversidad y la diferenciación entre los ciclos "
                "reproductivos de vertebrados e invertebrados."
            ),
            codigo="CE.CN.3.1.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta desde la indagación y ejecución de sencillos "
                "experimentos, la importancia de los procesos de "
                "fotosíntesis, nutrición, respiración, reproducción, y la "
                "relación con la humedad del suelo, diversidad y "
                "clasificación de las plantas sin semilla de las regionales "
                "naturales del Ecuador reconoce las posibles amenazas y "
                "propone, mediante trabajo colaborativo, medidas de "
                "protección."
            ),
            codigo="CE.CN.3.2.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Analiza, desde la indagación y observación, la dinámica de "
                "los ecosistemas en función de sus características y clases, "
                "los mecanismos de interrelación con los seres vivos, los "
                "procesos de adaptación de la diversidad biológica que "
                "presentan, las causas y consecuencias de la extinción de "
                "las especies, las técnicas y prácticas para el manejo de "
                "desechos, potenciando el trabajo colaborativo y promoviendo "
                "medidas de preservación y cuidado de la diversidad nativa, "
                "en las Áreas Naturales Protegidas del Ecuador."
            ),
            codigo="CE.CN.3.3.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica, desde la observación e indagación, la estructura, "
                "función e influencia del sistema reproductor(masculino y "
                "femenino), endócrino y nervioso los relaciona con los "
                "procesos fisiológicos, anatómicos y conductuales que se "
                "presentan en la pubertad y con los aspectos biológicos, "
                "psicológicos y sociales que determinan la sexualidad como "
                "condición humana."
            ),
            codigo="CE.CN.3.4.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Propone acciones para la salud integral (una dieta "
                "equilibrada, actividad física, normas de higiene y el uso "
                "de medicinas ancestrales) a partir de la comprensión e "
                "indagación de la estructura y función de los aparatos "
                "digestivo, respiratorio, circulatorio, excretor y de los "
                "órganos de los sentidos, relacionándolos con las "
                "enfermedades, los desórdenes alimenticios (bulimia, "
                "anorexia) y los efectos nocivos por consumo de drogas "
                "estimulantes, depresoras y alucinógenas en su cuerpo."
            ),
            codigo="CE.CN.3.5.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica, desde la experimentación y la revisión de diversas "
                "fuentes, la evolución de las teorías sobre la composición "
                "de la materia (átomos, elementos y moléculas), su "
                "clasificación (sustancias puras y mezclas homogéneas y "
                "heterogéneas), sus propiedades (elasticidad, dureza y "
                "brillo) y la clasificación de los compuestos químicos "
                "(orgánicos e inorgánicos), destancando las sustancias, las "
                "mezclas y los compuestos de uso cotidiano y/o tradicionales "
                "del país."
            ),
            codigo="CE.CN.3.6.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica, desde la exploración y experimentación en objetos "
                "de uso cotidiano, los tipos de fuerza (contacto, campo) y "
                "sus efectos en el cambio de la forma, la rapidez y la "
                "dirección del movimiento de los objetos."
            ),
            codigo="CE.CN.3.7.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica, desde la ejecución de experimentos sencillos, en "
                "varias sustancias y cuerpos del entorno, las diferencias "
                "entre calor y temperatura; y, comunica, de forma gráfica, "
                "las formas de transmisión del calor (conducción, convección "
                "y radiación)."
            ),
            codigo="CE.CN.3.8.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Analiza las características, importancia, aplicaciones, "
                "fundamentos y transformación de las energías térmica, "
                "eléctrica y magnética, a partir de la indagación, "
                "observación de representaciones analógicas, digitales y la "
                "exploración en objetos de su entorno(brújulas, motores "
                "eléctricos). Explica la importancia de realizar estudios "
                "ambientales y sociales para mitigar los impactos de las "
                "centrales hidroeléctricas en el ambiente."
            ),
            codigo="CE.CN.3.9.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Analiza, desde la indagación de diversas fuentes, los "
                "efectos de los fenómenos geológicos sobre el planeta "
                "Tierra, tomando en cuenta la composición del Sistema Solar, "
                "la estructura de la Tierra, la influencia de las placas "
                "tectónicas en la formación de la cordillera de los Andes y "
                "la distribución de la biodiversidad en las regiones "
                "naturales del Ecuador, reforzando su análisis con las "
                "contribuciones científicas al campo de la vulcanología del "
                "país."
            ),
            codigo="CE.CN.3.10.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica la formación del viento, nubes y lluvia, en función "
                "de la incidencia del patrón de radiación solar, patrón de "
                "calentamiento de la superficie terrestre y comprensión del "
                "Sol como fuente de energía de la Tierra."
            ),
            codigo="CE.CN.3.11.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica, desde la observación e indagación en diversas "
                "fuentes, las causas y consecuencias de las catástrofes "
                "climáticas en los seres vivos y sus hábitat, en función del "
                "conocimiento previo de las características, elementos y "
                "factores del clima, la función y propiedades del aire y la "
                "capa de ozono en la atmósfera, valorando la importancia de "
                "las estaciones y datos meteorológicos y proponiendo medidas "
                "de protección ante los rayos UV."
            ),
            codigo="CE.CN.3.12.",
            asignatura=ciencias_naturales,
            subnivel=media
        ),
        # Superior
        CriterioEvaluacion(
            description=(
                "Explica a partir de la indagación y exploración el nivel de "
                "complejidad de los seres vivos, a partir del análisis de "
                "sus propiedades, niveles de organización, diversidad y la "
                "clasificación de grupos taxonómicos dados."
            ),
            codigo="CE.CN.4.1.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Ejemplifica la complejidad de los seres vivos(animales y "
                "vegetales) a partir de la diferenciación de células y "
                "tejidos que los conforman, la importancia del ciclo celular "
                "que desarrollan, los tipos de reproducción que ejecutan e "
                "identifica el aporte de la tecnología para el desarrollo de "
                "la ciencia."
            ),
            codigo="CE.CN.4.2.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Diseña modelos representativos sobre la relación que "
                "encuentra entre la conformación y funcionamiento de "
                "cadenas, redes y pirámides alimenticias, el desarrollo de "
                "ciclos de los bioelementos(carbono, oxígeno, nitrógeno), "
                "con el flujo de energía al interior de un "
                "ecosistema(acuático o terrestre) así como determina los "
                "efectos de la actividad humana en el funcionamiento de los "
                "ecosistemas y en la relación clima-vegetación, a partir de "
                "la investigación y la formulación de hipótesis pertinentes."
            ),
            codigo="CE.CN.4.3.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Analiza la importancia que tiene la creación de Áreas "
                "Protegidas en el país para la conservación de la vida "
                "silvestre, la investigación y la educación, tomando en "
                "cuenta información sobre los biomas del mundo, "
                "comprendiendo los impactos de las actividades humanas en "
                "estos ecosistemas y promoviendo estrategias de "
                "conservación."
            ),
            codigo="CE.CN.4.4.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica la evolución biológica a través de investigaciones "
                "guiadas sobre evidencias evolutivas (registro fósil, deriva "
                "continental, extinción masiva de las especies), los "
                "principios de selección natural y procesos que generan la "
                "diversidad biológica. Infiere la importancia de la "
                "determinación de las eras y épocas geológicas de la Tierra, "
                "a través del fechado radiactivo y sus aplicaciones."
            ),
            codigo="CE.CN.4.5.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Formula su proyecto de toma de decisiones pertinentes, a "
                "partir del análisis de medidas de prevención, comprensión "
                "de las etapas de reproducción humana, importancia de la "
                "perpetuación de la especie, el cuidado prenatal y la "
                "lactancia durante el desarrollo del ser humano, causas y "
                "consecuencias de infecciones de transmisión sexual y los "
                "tipos de infecciones(virales, bacterianas y micóticas) a "
                "los que se expone el ser humano."
            ),
            codigo="CE.CN.4.6.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Propone medidas de prevención(uso de antibióticos y "
                "vacunas), contagio y propagación de bacterias y virus en "
                "función de sus características, evolución, estructura, "
                "función del sistema inmunitario y barreras inmunológicas, "
                "tipos de inmunidad, formas de transmisión, identificando "
                "además otros organismos patógenos para el ser humano."
            ),
            codigo="CE.CN.4.7.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica, a partir de la experimentación, el cambio de "
                "posición de los objetos en función de las fuerzas (fuerzas "
                "equilibradas y fuerzas no equilibradas), que actúan sobre "
                "ellos y establece la velocidad de un objeto como la "
                "relación entre el espacio recorrido y el tiempo "
                "transcurrido."
            ),
            codigo="CE.CN.4.8.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica, a partir de la experimentación, la relación entre "
                "densidad de objetos(sólidos, líquidos y gaseosos), la "
                "flotación o hundimiento de objetos, el efecto de la presión "
                "sobre los fluidos(líquidos y gases). Expone el efecto de "
                "lapresión atmosférica sobre diferentes objetos, su "
                "aplicación y relación con la presión absoluta y la presión "
                "manométrica."
            ),
            codigo="CE.CN.4.9.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Establece las diferencias entre el efecto de la fuerza "
                "gravitacional de la Tierra, con la fuerza gravitacional del "
                "Sol en relación a los objetos que los rodean, fortaleciendo "
                "su estudio con los aportes de verificación experimental a "
                "la ley de la gravitación universal."
            ),
            codigo="CE.CN.4.10.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Determina las características y propiedades de la materia "
                "orgánica e inorgánica en diferentes tipos de compuestos y "
                "reconoce al carbono como elemento fundamental de las "
                "biomoléculas y su importancia para los seres vivos."
            ),
            codigo="CE.CN.4.11.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Infiere la importancia del desarrollo de la astronomía a "
                "partir de la explicación de la configuración del "
                "Universo(galaxias, planetas, satélites, cometas, "
                "asteroides, tipos de estrellas y sus constelaciones), su "
                "origen y fenómenos astronómicos, apoyándose en la "
                "investigación y uso de medios tecnológicos."
            ),
            codigo="CE.CN.4.12.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Infiere la importancia de las interacciones de los ciclos "
                "biogeoquímicos en la biósfera (litósfera, hidrósfera y "
                "atmósfera), y los efectos del cambio climático producto de "
                "la alteración de las corrientes marinas y el impacto de las "
                "actividades humanas en los ecosistemas y la sociedad."
            ),
            codigo="CE.CN.4.13.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica el fenómeno de movimiento de las placas tectónicas, "
                "partiendo de la relación con las erupciones volcánicas, la "
                "formación y ciclo de las rocas, infiriendo los efectos de "
                "estos procesos en los cambios climáticos y distribución de "
                "organismos en los ecosistemas."
            ),
            codigo="CE.CN.4.14.",
            asignatura=ciencias_naturales,
            subnivel=superior
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0029_auto_20180808_1700'),
    ]

    operations = [
        migrations.RunPython(
            create_criterios, reverse_code=migrations.RunPython.noop)
    ]
