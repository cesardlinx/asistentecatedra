from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    ciencias_naturales = Asignatura.objects.get(name='Ciencias Naturales')

    # Bloques
    bloque1 = BloqueCurricular.objects.get(
        numero_bloque=1, asignatura=ciencias_naturales
    )
    bloque2 = BloqueCurricular.objects.get(
        numero_bloque=2, asignatura=ciencias_naturales
    )
    bloque3 = BloqueCurricular.objects.get(
        numero_bloque=3, asignatura=ciencias_naturales
    )
    bloque4 = BloqueCurricular.objects.get(
        numero_bloque=4, asignatura=ciencias_naturales
    )
    bloque5 = BloqueCurricular.objects.get(
        numero_bloque=5, asignatura=ciencias_naturales
    )

    # Subniveles
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Destreza.objects.bulk_create([
        # Elemental
        # Bloque 1
        Destreza(
            description=(
                "Observar las etapas del ciclo vital del ser humano y "
                "registrar gráficamente los cambios de acuerdo a la edad."
            ),
            codigo="CN.2.1.1.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Observar e identificar los cambios en el ciclo vital de "
                "diferentes animales (insectos, peces, anfibios, reptiles, "
                "aves y mamíferos) y compararlos con los cambios en el ciclo "
                "vital del ser humano."
            ),
            codigo="CN.2.1.2.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Experimentar y predecir las etapas del ciclo vital de las "
                "plantas, sus cambios y respuestas a los estímulos, al "
                "observar la germinación de la semilla, y reconocer la "
                "importancia de la polinización y la dispersión de la "
                "semilla."
            ),
            codigo="CN.2.1.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Observar y describir las características de los animales y "
                "clasificarlos en vertebrados e invertebrados, por la "
                "presencia o ausencia de columna vertebral."
            ),
            codigo="CN.2.1.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar sobre los animales útiles para el ser humano e "
                "identificar lo que proveen como alimento, vestido, compañía "
                "y protección."
            ),
            codigo="CN.2.1.5.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Observar en forma guiada y describir las características de "
                "los animales vertebrados, agruparlos de acuerdo a sus "
                "características y relacionarlos con su hábitat."
            ),
            codigo="CN.2.1.6.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Observar y describir las partes de la planta, explicar sus "
                "funciones y clasificarlas por su estrato y uso."
            ),
            codigo="CN.2.1.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Observar y describir las plantas con semillas y "
                "clasificarlas en angiospermas y gimnospermas, según sus "
                "semejanzas y diferencias."
            ),
            codigo="CN.2.1.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar, mediante el uso de las TIC y otros recursos, la "
                "diversidad e importancia de los vertebrados y las plantas "
                "con semillas de las regiones naturales del Ecuador; "
                "identificar acciones de protección y cuidado."
            ),
            codigo="CN.2.1.9.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar y describir las características de los hábitats "
                "locales, clasificarlos según sus características e "
                "identificar sus plantas y animales."
            ),
            codigo="CN.2.1.10.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar en forma guiada sobre las reacciones de los seres "
                "vivos a los cambios de los hábitats naturales y "
                "ejemplificar medidas enfocadas en su cuidado."
            ),
            codigo="CN.2.1.11.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar e identificar las diferentes clases de amenazas que "
                "se manifiestan en los hábitats locales, distinguir las "
                "medidas de control que se aplican en la localidad y "
                "proponer medidas para detener su degradación."
            ),
            codigo="CN.2.1.12.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Ubicar el cerebro, el corazón, los pulmones y el estómago "
                "en su cuerpo, explicar sus funciones y relacionarlas con el "
                "mantenimiento de la vida."
            ),
            codigo="CN.2.2.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explorar y describir los órganos que permiten el movimiento "
                "del cuerpo y ejemplificar la función coordinada del "
                "esqueleto y de los músculos en su cuerpo."
            ),
            codigo="CN.2.2.2.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Observar y analizar la estructura y función del sistema "
                "osteomuscular y describirlo desde sus funciones de soporte, "
                "movimiento y protección del cuerpo."
            ),
            codigo="CN.2.2.3.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar la importancia de la alimentación saludable y la "
                "actividad física, de acuerdo a su edad y a las actividades "
                "diarias que realiza."
            ),
            codigo="CN.2.2.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar y aplicar normas de higiene corporal y de "
                "manejo de alimentos; predecir las consecuencias si no se "
                "las cumple."
            ),
            codigo="CN.2.2.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Observar y analizar la pirámide alimenticia, seleccionar "
                "los alimentos de una dieta diaria equilibrada y "
                "clasificarlos en energéticos, constructores y reguladores."
            ),
            codigo="CN.2.2.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Observar y describir los estados físicos de los objetos del "
                "entorno y diferenciarlos, por sus características físicas, "
                "en sólidos, líquidos y gaseosos."
            ),
            codigo="CN.2.3.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Describir los cambios del estado físico de la materia en la "
                "naturaleza; experimentar con el agua e identificar sus "
                "cambios ante la variación de temperatura."
            ),
            codigo="CN.2.3.2.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar y describir las propiedades generales de la "
                "materia en los objetos del entorno; medir masa, volumen y "
                "peso con instrumentos y unidades de medida."
            ),
            codigo="CN.2.3.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar e identificar las clases de la materia y "
                "diferenciarlas, por sus características, en sustancias "
                "puras y mezclas naturales y artificiales."
            ),
            codigo="CN.2.3.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar la separación de las mezclas mediante la "
                "aplicación de métodos y técnicas sencillas, y comunicar los "
                "resultados."
            ),
            codigo="CN.2.3.5.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar y experimentar el movimiento de los objetos del "
                "entorno y explicar la dirección y la rapidez de movimiento."
            ),
            codigo="CN.2.3.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar, experimentar y describir la acción de la fuerza "
                "de las máquinas simples que se utilizan en trabajos "
                "cotidianos."
            ),
            codigo="CN.2.3.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar y explicar la fuerza de gravedad y experimentarla "
                "mediante la caída de los cuerpos."
            ),
            codigo="CN.2.3.8.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explorar e identificar la energía, sus formas y fuentes en "
                "la naturaleza; compararlas y explicar su importancia para "
                "la vida, para el movimiento de los cuerpos y para la "
                "realización de todo tipo de trabajos."
            ),
            codigo="CN.2.3.9.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar y describir las trasformaciones de la energía y "
                "explorar, en la localidad, sus usos en la vida cotidiana."
            ),
            codigo="CN.2.3.10.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar y explicar las características de la luz y "
                "diferenciar los objetos luminosos y no luminosos, "
                "transparentes y opacos."
            ),
            codigo="CN.2.3.11.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar y describir el bloqueo de la luz y las "
                "características de la sombra y la penumbra; experimentar y "
                "explicar sus diferencias, y relacionar con los eclipses."
            ),
            codigo="CN.2.3.12.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar, mediante el uso de las TIC y otros recursos, la "
                "propagación de la luz y experimentarla en diferentes "
                "medios."
            ),
            codigo="CN.2.3.13.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Observar y reconocer el ciclo diario en los seres vivos y "
                "el ambiente y formular preguntas sobre los animales que "
                "realizan sus actividades durante la noche y durante el día."
            ),
            codigo="CN.2.4.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Diferenciar las características del día y de la noche a "
                "partir de la observación de la presencia del Sol, la Luna y "
                "las estrellas, la luminosidad del cielo y la sensación de "
                "frío y calor, y describir las respuestas de los seres "
                "vivos."
            ),
            codigo="CN.2.4.2.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Describir las características de la Tierra y sus "
                "movimientos de traslación y rotación y relacionarlos con "
                "las estaciones, el día, la noche y su influencia en el "
                "clima, tanto local como global."
            ),
            codigo="CN.2.4.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar y describir, mediante el uso de las TIC y otros "
                "recursos, las características del Sol, la Tierra y la Luna "
                "y distinguir sus semejanzas y diferencias de acuerdo a su "
                "forma, tamaño y movimiento."
            ),
            codigo="CN.2.4.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar en forma directa las fases de la Luna e "
                "identificar su influencia en algunos fenómenos "
                "superficiales de la Tierra."
            ),
            codigo="CN.2.4.5.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar, mediante el uso de las TIC y otros recursos, sobre "
                "la influencia del Sol en el suelo, el agua, el aire y los "
                "seres vivos; explicarla e interpretar sus efectos."
            ),
            codigo="CN.2.4.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Definir los recursos naturales, clasificarlos en renovables "
                "y no renovables y destacar su importancia como fuente de "
                "alimentos, energía y materias primas."
            ),
            codigo="CN.2.4.7.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Explorar y discutir cuáles son los principales recursos "
                "naturales renovables de la localidad e identificar sus "
                "características y usos."
            ),
            codigo="CN.2.4.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Explorar y discutir los principales recursos naturales no "
                "renovables de las regiones naturales del país y dar razones "
                "para realizar la explotación controlada."
            ),
            codigo="CN.2.4.9.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar, por medio de la experimentación, y describir las "
                "características y la formación del suelo; reconocerlo como "
                "un recurso natural."
            ),
            codigo="CN.2.4.10.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar y clasificar los tipos de suelo por sus componentes "
                "e identificar las causas de su deterioro y las formas de "
                "conservarlo en la localidad."
            ),
            codigo="CN.2.4.11.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar y describir el ciclo del agua en la naturaleza y "
                "reconocer que el agua es un recurso imprescindible para la "
                "vida."
            ),
            codigo="CN.2.4.12.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar y describir las características del agua, sus usos "
                "y conservación y destacar la importancia de conservar las "
                "fuentes de agua dulce."
            ),
            codigo="CN.2.4.13.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Analizar y elaborar modelos del proceso de potabilización "
                "del agua y explicar la razón de tratar el agua destinada al "
                "consumo humano."
            ),
            codigo="CN.2.4.14.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Indagar, en forma guiada, sobre los conocimientos de "
                "civilizaciones ancestrales sobre el Sol y la Luna y su "
                "aplicación en la agricultura tradicional; seleccionar "
                "información y comunicar los resultados con recursos "
                "pertinentes."
            ),
            codigo="CN.2.5.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Observar las características del cielo, medir algunos "
                "fenómenos atmosféricos, mediante la creación y/o uso de "
                "instrumentos tecnológicos, registrarlos gráficamente y "
                "predecir el tiempo atmosférico."
            ),
            codigo="CN.2.5.2.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Explorar, en forma guiada, el manejo de los alimentos y las "
                "normas de higiene en mercados locales; predecir las "
                "consecuencias de un manejo inadecuado para la salud de las "
                "personas de la localidad."
            ),
            codigo="CN.2.5.3.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Observar, con instrumentos tecnológicos adecuados, la "
                "posición del Sol durante el día, registrarla mediante "
                "fotografías o gráficos, hacer preguntas y dar respuestas "
                "sobre su posición en la mañana, el mediodía y la tarde."
            ),
            codigo="CN.2.5.4.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar, en forma guiada mediante el uso de las TIC y otros "
                "recursos, sobre el desarrollo tecnológico de instrumentos "
                "para la observación astronómica; comunicar y reconocer los "
                "aportes de la ciencia y la tecnología para el conocimiento "
                "del Universo."
            ),
            codigo="CN.2.5.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Experimentar, en forma guiada, los tipos de mezclas que se "
                "usan en la preparación de diferentes alimentos; identificar "
                "el estado físico de los componentes y comunicar sus "
                "conclusiones."
            ),
            codigo="CN.2.5.6.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar, mediante el uso de las TIC y otros recursos, sobre "
                "las tecnologías agrícolas tradicionales de las culturas "
                "indígenas, y pueblos afroecuatoriano y montubio del "
                "Ecuador; comunicar las conclusiones y reconocer los aportes "
                "de los saberes tradicionales en el manejo del suelo."
            ),
            codigo="CN.2.5.7.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar y explicar, por medio de modelos, la aplicación de "
                "tecnologías limpias en el manejo del agua para consumo "
                "humano; comunicar las medidas de prevención para evitar su "
                "contaminación."
            ),
            codigo="CN.2.5.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar, mediante el uso de las TIC y otros recursos, la "
                "contribución del científico ecuatoriano Misael Acosta Solís "
                "al conocimiento de la flora ecuatoriana; reconocer su "
                "aporte en los herbarios nacionales como fuente de "
                "información."
            ),
            codigo="CN.2.5.9.",
            asignatura=ciencias_naturales,
            subnivel=elemental,
            bloque=bloque5
        ),
        # Media
        # Bloque 1
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, las "
                "características de los animales invertebrados, describirlas "
                "y clasificarlos de acuerdo a sus semejanzas y diferencias."
            ),
            codigo="CN.3.1.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explorar y clasificar las plantas sin semillas y explicar "
                "su relación con la humedad del suelo y su importancia para "
                "el ambiente."
            ),
            codigo="CN.3.1.2.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Experimentar sobre la fotosíntesis, la nutrición y la "
                "respiración en las plantas, explicarlas y deducir su "
                "importancia para el mantenimiento de la vida."
            ),
            codigo="CN.3.1.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, la diversidad "
                "de invertebrados de las regiones naturales de Ecuador y "
                "proponer medidas de protección frente a sus amenazas."
            ),
            codigo="CN.3.1.4.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, la diversidad "
                "de plantas sin semillas de las regiones naturales de "
                "Ecuador y proponer medidas de protección frente a las "
                "amenazas."
            ),
            codigo="CN.3.1.5.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar y describir el ciclo reproductivo de los "
                "vertebrados y diferenciarlos según su tipo de reproducción."
            ),
            codigo="CN.3.1.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar y describir el ciclo reproductivo de los "
                "invertebrados y diferenciarlos según su tipo de "
                "reproducción."
            ),
            codigo="CN.3.1.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar y describir el ciclo reproductivo de las plantas e "
                "identificar los agentes polinizadores que intervienen en su "
                "fecundación."
            ),
            codigo="CN.3.1.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, las "
                "características de los ecosistemas y sus clases, "
                "interpretar las interrelaciones de los seres vivos en los "
                "ecosistemas y clasificarlos en productores, consumidores y "
                "descomponedores."
            ),
            codigo="CN.3.1.9.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, la diversidad "
                "biológica de los ecosistemas de Ecuador e identificar la "
                "flora y fauna representativas de los ecosistemas naturales "
                "de la localidad."
            ),
            codigo="CN.3.1.10.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar y explicar las adaptaciones de plantas y animales a "
                "las condiciones ambientales de diferentes ecosistemas y "
                "relacionarlas con su supervivencia."
            ),
            codigo="CN.3.1.11.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explorar y describir las interacciones, intraespecíficas e "
                "interespecíficas, en diversos ecosistemas, diferenciarlas y "
                "explicar la importancia de las relaciones."
            ),
            codigo="CN.3.1.12.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar en diversas fuentes y describir las causas y "
                "consecuencias potenciales de la extinción de las especies "
                "en un determinado ecosistema, y proponer medidas de "
                "protección de la biodiversidad amenazada."
            ),
            codigo="CN.3.1.13.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Indagar y describir la estructura y función del sistema "
                "reproductor humano, femenino y masculino, y explicar su "
                "importancia en la transmisión de las características "
                "hereditarias."
            ),
            codigo="CN.3.2.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Examinar los cambios fisiológicos, anatómicos y "
                "conductuales durante la pubertad, formular preguntas y "
                "encontrar respuestas sobre el inicio de la madurez sexual "
                "en mujeres y hombres, basándose en sus propias "
                "experiencias."
            ),
            codigo="CN.3.2.2.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir, con apoyo de modelos, la estructura y función de "
                "los sistemas digestivo, respiratorio, circulatorio y "
                "excretor y promover su cuidado."
            ),
            codigo="CN.3.2.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar, con apoyo de modelos, la estructura y función del "
                "sistema endocrino e interpretar su importancia para el "
                "mantenimiento del equilibrio del medio interno "
                "(homeostasis) y en cambios que se dan en la pubertad."
            ),
            codigo="CN.3.2.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, la estructura "
                "y función del sistema nervioso, relacionarlo con el sistema "
                "endocrino, y explicar su importancia para la recepción de "
                "los estímulos del ambiente y la producción de respuestas."
            ),
            codigo="CN.3.2.5.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explorar y describir la estructura y función de los órganos "
                "de los sentidos, y explicar su importancia para la relación "
                "con el ambiente social y natural."
            ),
            codigo="CN.3.2.6.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer la importancia de la actividad física, la higiene "
                "corporal y la dieta equilibrada en la pubertad para "
                "mantener la salud integral y comunicar los beneficios por "
                "diferentes medios."
            ),
            codigo="CN.3.2.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Diseñar y ejecutar una indagación documental sobre las "
                "causas de las enfermedades de los sistemas digestivo, "
                "respiratorio, circulatorio, excretor y reproductor y "
                "comunicar las medidas de prevención."
            ),
            codigo="CN.3.2.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Planificar y ejecutar una indagación documental sobre los "
                "efectos nocivos de las drogas - estimulantes, depresoras, "
                "alucinógenas-, y analizar las prácticas que se aplican para "
                "la erradicación del consumo."
            ),
            codigo="CN.3.2.9.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Observar los aspectos biológicos, psicológicos y sociales "
                "que determinan la sexualidad, y analizarla como una "
                "manifestación humana."
            ),
            codigo="CN.3.2.10.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Explorar y demostrar las propiedades específicas de la "
                "materia, experimentar, probar las predicciones y comunicar "
                "los resultados."
            ),
            codigo="CN.3.3.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, la "
                "constitución de la materia, analizar el modelo didáctico "
                "del átomo y describir los elementos químicos y las "
                "moléculas."
            ),
            codigo="CN.3.3.2.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar y clasificar la materia en sustancias puras y "
                "mezclas, y relacionarlas con los estados físicos de la "
                "materia."
            ),
            codigo="CN.3.3.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar y establecer preguntas sobre las propiedades de los "
                "compuestos químicos, clasificarlos en orgánicos e "
                "inorgánicos, y reconocerlos en sustancias de uso cotidiano."
            ),
            codigo="CN.3.3.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar y diferenciar los tipos de fuerzas y explicar "
                "sus efectos en objetos de uso cotidiano."
            ),
            codigo="CN.3.3.5.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explorar e interpretar los efectos de la aplicación de las "
                "fuerzas en los cambios de la forma, la rapidez y la "
                "dirección de movimiento de los objetos y comunicar sus "
                "conclusiones."
            ),
            codigo="CN.3.3.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Demostrar experimentalmente y diferenciar entre temperatura "
                "y calor, verificarlas por medición en varias sustancias y "
                "mediante el equilibrio térmico de los cuerpos."
            ),
            codigo="CN.3.3.7.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar la transmisión de calor y deducir la forma en "
                "que se producen la conducción, la convección y la "
                "radiación."
            ),
            codigo="CN.3.3.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, las "
                "aplicaciones de la energía térmica en la máquina de vapor e "
                "interpretar su importancia en el desarrollo industrial."
            ),
            codigo="CN.3.3.9.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar y explicar los fundamentos y aplicaciones de la "
                "electricidad, examinarlos en diseños experimentales y "
                "elaborar circuitos eléctricos con materiales de fácil "
                "manejo."
            ),
            codigo="CN.3.3.10.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar las transformaciones de la energía eléctrica, "
                "desde su generación en las centrales hidroeléctricas hasta "
                "su conversión en luz, sonido, movimiento y calor."
            ),
            codigo="CN.3.3.11.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar, identificar y describir las características y "
                "aplicaciones prácticas del magnetismo en objetos como la "
                "brújula sencilla y los motores eléctricos."
            ),
            codigo="CN.3.3.12.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Indagar e identificar al Sol como fuente de energía de la "
                "Tierra e inferir su importancia como recurso renovable."
            ),
            codigo="CN.3.4.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, las orbitas "
                "planetarias y el movimiento de los planetas alrededor del "
                "Sol."
            ),
            codigo="CN.3.4.2.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, sobre el "
                "sistema solar, describir algunos de sus componentes, usar "
                "modelos de simulación y explicar los eclipses de la Luna y "
                "el Sol."
            ),
            codigo="CN.3.4.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Analizar modelos de la estructura de la Tierra y "
                "diferenciar sus capas de acuerdo a sus componentes."
            ),
            codigo="CN.3.4.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar, con uso de las TIC y otros recursos, los efectos "
                "de los fenómenos geológicos, relacionarlos con la formación "
                "de nuevos relieves, organizar campañas de prevención ante "
                "las amenazas de origen natural."
            ),
            codigo="CN.3.4.5.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Analizar la influencia de las placas tectónicas en los "
                "movimientos orogénicos y epirogénicos que formaron la "
                "cordillera de Los Andes y explicar su influencia en la "
                "distribución de la biodiversidad en las regiones naturales "
                "de Ecuador."
            ),
            codigo="CN.3.4.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Explicar, con apoyo de modelos, los patrones de incidencia "
                "de la radiación solar sobre la superficie terrestre y "
                "relacionar las variaciones de intensidad de la radiación "
                "solar con la ubicación geográfica."
            ),
            codigo="CN.3.4.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Analizar e interpretar los patrones de calentamiento de la "
                "superficie terrestre y explicar su relación con la "
                "formación de vientos, nubes y lluvias."
            ),
            codigo="CN.3.4.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar, con uso de las TIC y otros recursos, la "
                "atmósfera, describir sus capas según su distancia desde la "
                "litósfera e identificar su importancia para el "
                "mantenimiento de la vida."
            ),
            codigo="CN.3.4.9.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Reconocer la función de la capa de ozono y ejemplificar "
                "medidas de protección ante los rayos UV."
            ),
            codigo="CN.3.4.10.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Experimentar y describir las propiedades y funciones del "
                "aire, deducir la importancia de este en la vida de los "
                "seres e identificarlo como un recurso natural renovable."
            ),
            codigo="CN.3.4.11.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar y explicar las características, elementos y "
                "factores del clima, diferenciarlo del tiempo atmosférico, "
                "registrar y analizar datos meteorológicos de la localidad "
                "con apoyo de instrumentos de medición."
            ),
            codigo="CN.3.4.12.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar en diferentes medios las características del clima "
                "en las regiones naturales de Ecuador, explicarlas y "
                "establecer la importancia de las estaciones meteorológicas."
            ),
            codigo="CN.3.4.13.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar e inferir las características y efectos de las "
                "catástrofes climáticas y establecer las consecuencias en "
                "los seres vivos y sus hábitats."
            ),
            codigo="CN.3.4.14.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Recoger información acerca de los conocimientos ancestrales "
                "de la medicina indígena, pueblos afroecuatoriano y montubio "
                "de Ecuador y argumentar sobre la importancia que tienen en "
                "el descubrimiento de nuevos medicamentos."
            ),
            codigo="CN.3.5.1.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Diseñar una investigación de campo sobre las creencias "
                "relacionadas con la bulimia y la anorexia, y comparar sus "
                "resultados con las investigaciones científicas actuales."
            ),
            codigo="CN.3.5.2.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Planificar una indagación sobre el estado de la calidad del "
                "aire de la localidad, diseñar una experimentación sencilla "
                "que compruebe el nivel de contaminación local y explicar "
                "sus conclusiones acerca de los efectos de la contaminación "
                "en el ambiente."
            ),
            codigo="CN.3.5.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar el aporte de la ciencia y la tecnología para el "
                "manejo de desechos, aplicar técnicas de manejo de desechos "
                "sólidos en los ecosistemas del entorno e inferir el impacto "
                "en la calidad del ambiente."
            ),
            codigo="CN.3.5.4.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Planificar y realizar una indagación bibliográfica sobre el "
                "trabajo de los científicos en las Áreas Naturales "
                "Protegidas de Ecuador, y utilizar esa información para "
                "establecer la importancia de la preservación y el cuidado "
                "de la biodiversidad nativa."
            ),
            codigo="CN.3.5.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Analizar los impactos de las centrales hidroeléctricas en "
                "el ambiente y explicar sobre la importancia de los estudios "
                "ambientales y sociales para mitigar sus impactos."
            ),
            codigo="CN.3.5.6.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar sobre los científicos que han contribuido "
                "significativamente al avance de la ciencia y la tecnología "
                "en el campo de la vulcanología en el país, e interpretar la "
                "importancia que tienen sus investigaciones para la "
                "prevención y el control de riesgos."
            ),
            codigo="CN.3.5.7.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar sobre las bebidas tradicionales del país, formular "
                "hipótesis sobre el tipo de mezclas a las que corresponden, "
                "usar técnicas e instrumentos para probar estas hipótesis, "
                "interpretar los resultados y comunicar sus conclusiones."
            ),
            codigo="CN.3.5.8.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Planificar y ejecutar una indagación sobre la evolución del "
                "conocimiento acerca de la composición de la materia, desde "
                "las ideas de los griegos hasta las teorías modernas; "
                "representarla en una línea de tiempo y deducir los cambios "
                "de la ciencia en el tiempo."
            ),
            codigo="CN.3.5.9.",
            asignatura=ciencias_naturales,
            subnivel=media,
            bloque=bloque5
        ),
        # Superior
        # Bloque 1
        Destreza(
            description=(
                "Indagar y explicar las propiedades de los seres vivos e "
                "inferir su importancia para el mantenimiento de la vida en "
                "la Tierra."
            ),
            codigo="CN.4.1.1.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explorar e identificar los niveles de organización de la "
                "materia viva, de acuerdo al nivel de complejidad."
            ),
            codigo="CN.4.1.2.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar, con uso del microscopio, de las TIC u otros "
                "recursos, y describir las características estructurales y "
                "funcionales de las células, y clasificarlas por su grado de "
                "complejidad, nutrición, tamaño y forma."
            ),
            codigo="CN.4.1.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir, con apoyo de modelos, la estructura de las "
                "células animales y vegetales, reconocer sus diferencias y "
                "explicar las características, funciones e importancia de "
                "los organelos."
            ),
            codigo="CN.4.1.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Diseñar y ejecutar una indagación experimental y explicar "
                "las clases de tejidos animales y vegetales, "
                "diferenciándolos por sus características, funciones y "
                "ubicación."
            ),
            codigo="CN.4.1.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el proceso del ciclo celular e investigar "
                "experimentalmente los ciclos celulares mitótico y meiótico, "
                "describirlos y establecer su importancia en la "
                "proliferación celular y en la formación de gametos."
            ),
            codigo="CN.4.1.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar los niveles de organización y diversidad de los "
                "seres vivos y clasificarlos en grupos taxonómicos, de "
                "acuerdo con las características observadas a simple vista y "
                "las invisibles para el ojo humano."
            ),
            codigo="CN.4.1.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Usar modelos y describir la reproducción sexual en los "
                "seres vivos y deducir su importancia para la supervivencia "
                "de la especie."
            ),
            codigo="CN.4.1.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Usar modelos y describir la reproducción asexual en los "
                "seres vivos, identificar sus tipos y deducir su importancia "
                "para la supervivencia de la especie."
            ),
            codigo="CN.4.1.9.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Observar y explicar en diferentes ecosistemas las cadenas, "
                "redes y pirámides alimenticias, identificar los organismos "
                "productores, consumidores y descomponedores y analizar los "
                "efectos de la actividad humana sobre las redes "
                "alimenticias."
            ),
            codigo="CN.4.1.10.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Diseñar modelos representativos del flujo de energía en "
                "cadenas y redes alimenticias, explicar y demostrar el rol "
                "de los seres vivos en la trasmisión de energía en los "
                "diferentes niveles tróficos."
            ),
            codigo="CN.4.1.11.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar los elementos carbono, oxígeno y nitrógeno con "
                "el flujo de energía en las cadenas tróficas de los "
                "diferentes ecosistemas."
            ),
            codigo="CN.4.1.12.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar e inferir los impactos de las actividades humanas "
                "en los ecosistemas, establecer sus consecuencias y proponer "
                "medidas de cuidado del ambiente."
            ),
            codigo="CN.4.1.13.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar y formular hipótesis sobre los procesos y cambios "
                "evolutivos en los seres vivos, y deducir las modificaciones "
                "que se presentan en la descendencia como un proceso "
                "generador de la diversidad biológica."
            ),
            codigo="CN.4.1.14.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar e interpretar los principios de la selección "
                "natural como un aspecto fundamental de la teoría de la "
                "evolución biológica."
            ),
            codigo="CN.4.1.15.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar e identificar situaciones problémicas sobre el "
                "proceso evolutivo de la vida con relación a los eventos "
                "geológicos e interpretar los modelos teóricos del registro "
                "fósil, la deriva continental y la extinción masiva de "
                "especies."
            ),
            codigo="CN.4.1.16.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar sobre las áreas protegidas del país, ubicarlas e "
                "interpretarlas como espacios de conservación de la vida "
                "silvestre, de investigación y educación."
            ),
            codigo="CN.4.1.17.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Analizar y explicar las etapas de la reproducción humana, "
                "deducir su importancia como un mecanismo de perpetuación de "
                "la especie y argumentar sobre la importancia de la "
                "nutrición prenatal y la lactancia como forma de enriquecer "
                "la afectividad."
            ),
            codigo="CN.4.2.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Investigar en forma documental y explicar la evolución de "
                "las bacterias y la resistencia a los antibióticos, deducir "
                "sus causas y las consecuencias de estas para el ser humano."
            ),
            codigo="CN.4.2.2.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar, con apoyo de modelos, el sistema inmunitario, "
                "identificar las clases de barreras inmunológicas, "
                "interpretar los tipos de inmunidad que presenta el ser "
                "humano e infiere sobre la importancia de la vacunación."
            ),
            codigo="CN.4.2.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Indagar sobre la salud sexual en los adolescentes y "
                "proponer un proyecto de vida satisfactorio en el que se "
                "concientice sobre los riesgos."
            ),
            codigo="CN.4.2.4.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Investigar en forma documental y registrar evidencias sobre "
                "las infecciones de transmisión sexual, agruparlas en "
                "virales, bacterianas y micóticas, inferir sus causas y "
                "consecuencias y reconocer medidas de prevención."
            ),
            codigo="CN.4.2.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explorar y describir la relación del ser humano con "
                "organismos patógenos que afectan la salud de manera "
                "transitoria y permanente y ejemplificar las medidas "
                "preventivas que eviten el contagio y su propagación."
            ),
            codigo="CN.4.2.6.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir las características de los virus, indagar las "
                "formas de transmisión y comunicar las medidas preventivas, "
                "por diferentes medios."
            ),
            codigo="CN.4.2.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Investigar en forma experimental y explicar la posición de "
                "un objeto respecto a una referencia, ejemplificar y medir "
                "el cambio de posición durante un tiempo determinado."
            ),
            codigo="CN.4.3.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar y analizar la rapidez promedio de un objeto en "
                "situaciones cotidianas que relacionan distancia y tiempo "
                "transcurrido."
            ),
            codigo="CN.4.3.2.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar y describir la velocidad de un objeto con "
                "referencia a su dirección y rapidez, e inferir las "
                "características de la velocidad."
            ),
            codigo="CN.4.3.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explicar, a partir de modelos, la magnitud y dirección de "
                "la fuerza y demostrar el resultado acumulativo de dos o más "
                "fuerzas que actúan sobre un objeto al mismo tiempo."
            ),
            codigo="CN.4.3.4.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar la aplicación de fuerzas equilibradas sobre un "
                "objeto en una superficie horizontal con mínima fricción y "
                "concluir que la velocidad de movimiento del objeto no "
                "cambia."
            ),
            codigo="CN.4.3.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar y analizar una fuerza no equilibrada y demostrar "
                "su efecto en el cambio de velocidad en un objeto."
            ),
            codigo="CN.4.3.6.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explorar, identificar y diferenciar las fuerzas que actúan "
                "sobre un objeto estático."
            ),
            codigo="CN.4.3.7.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar y explicar la relación entre masa y fuerza y "
                "la respuesta de un objeto en forma de aceleración."
            ),
            codigo="CN.4.3.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Experimentar con la densidad de objetos sólidos, líquidos y "
                "gaseosos, al pesar, medir y registrar los datos de masa y "
                "volumen, y comunicar los resultados."
            ),
            codigo="CN.4.3.9.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explicar la presión sobre los fluidos y verificar "
                "experimentalmente el principio de Pascal en el "
                "funcionamiento de la prensa hidráulica."
            ),
            codigo="CN.4.3.10.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Observar a partir de una experiencia y explicar la presión "
                "atmosférica, e interpretar su variación respecto a la "
                "altitud."
            ),
            codigo="CN.4.3.11.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explicar, con apoyo de modelos, la presión absoluta con "
                "relación a la presión atmosférica e identificar la presión "
                "manométrica."
            ),
            codigo="CN.4.3.12.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Diseñar un modelo que demuestre el principio de Arquímedes, "
                "inferir el peso aparente de un objeto y explicar la "
                "flotación o hundimiento de un objeto en relación con la "
                "densidad del agua."
            ),
            codigo="CN.4.3.13.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar y explicar el origen de la fuerza gravitacional de "
                "la Tierra y su efecto en los objetos sobre la superficie, e "
                "interpretar la relación masa-distancia según la ley de "
                "Newton."
            ),
            codigo="CN.4.3.14.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, la gravedad "
                "solar y las orbitas planetarias y explicar sobre el "
                "movimiento de los planetas alrededor del Sol."
            ),
            codigo="CN.4.3.15.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Diseñar una investigación experimental para analizar las "
                "características de la materia orgánica e inorgánica en "
                "diferentes compuestos, diferenciar los dos tipos de materia "
                "según sus propiedades e inferir la importancia de la "
                "química."
            ),
            codigo="CN.4.3.16.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar sobre el elemento carbono, caracterizarlo según sus "
                "propiedades físicas y químicas, y relacionarlo con la "
                "constitución de objetos y seres vivos."
            ),
            codigo="CN.4.3.17.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Explicar el papel del carbono como elemento base de la "
                "química de la vida e identificarlo en las biomoléculas."
            ),
            codigo="CN.4.3.18.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Indagar experimentalmente, analizar y describir las "
                "características de las biomoléculas y relacionarlas con las "
                "funciones en los seres vivos."
            ),
            codigo="CN.4.3.19.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque3
        ),
        # Bloque 4
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, sobre el "
                "origen del Universo, analizar la teoría del Big Bang y "
                "demostrarla en modelos actuales de la cosmología teórica."
            ),
            codigo="CN.4.4.1.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC, modelos y otros recursos, la "
                "configuración y forma de las galaxias y los tipos de "
                "estrellas, describir y explicar el uso de las tecnologías "
                "digitales y los aportes de astrónomos y físicos para el "
                "conocimiento del Universo."
            ),
            codigo="CN.4.4.2.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar, con uso de las TIC y otros recursos, y explicar "
                "la apariencia general de los planetas, satélites, cometas y "
                "asteroides, y elaborar modelos representativos del sistema "
                "solar."
            ),
            codigo="CN.4.4.3.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar en el mapa del cielo, la forma y ubicación de las "
                "constelaciones y explicar sus evidencias sustentadas en "
                "teorías y creencias, con un lenguaje pertinente y modelos "
                "representativos."
            ),
            codigo="CN.4.4.4.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Describir la posición relativa del Sol, la Tierra y la Luna "
                "y distinguir los fenómenos astronómicos que se producen en "
                "el espacio."
            ),
            codigo="CN.4.4.5.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Reconocer, con uso de las TIC y otros recursos, los "
                "diferentes tipos de radiaciones del espectro "
                "electromagnético y comprobar experimentalmente, a partir de "
                "la luz blanca, la mecánica de formación del arcoíris."
            ),
            codigo="CN.4.4.6.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Describir, con apoyo de modelos, los ciclos del oxígeno, el "
                "carbono, el nitrógeno y el fósforo, y explicar la "
                "importancia de estos para el reciclaje de los compuestos "
                "que mantienen la vida en el planeta."
            ),
            codigo="CN.4.4.7.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Explicar, con apoyo de modelos, la interacción de los "
                "ciclos biogeoquímicos en la biosfera (litósfera, la "
                "hidrósfera y la atmósfera), e inferir su importancia para "
                "el mantenimiento del equilibrio ecológico y los procesos "
                "vitales que tienen lugar en los seres vivos."
            ),
            codigo="CN.4.4.8.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar y destacar los impactos de las actividades humanas "
                "sobre los ciclos biogeoquímicos, y comunicar las "
                "alteraciones en el ciclo del agua debido al cambio "
                "climático."
            ),
            codigo="CN.4.4.9.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Investigar en forma documental sobre el cambio climático y "
                "sus efectos en los casquetes polares, nevados y capas de "
                "hielo, formular hipótesis sobre sus causas y registrar "
                "evidencias sobre la actividad humana y el impacto de esta "
                "en el clima."
            ),
            codigo="CN.4.4.10.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, y explicar "
                "los factores que afectan a las corrientes marinas, como la "
                "de Humboldt y El Niño, y evaluar los impactos en el clima, "
                "la vida marina y la industria pesquera."
            ),
            codigo="CN.4.4.11.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Observar, con uso de las TIC y otros recursos, los biomas "
                "del mundo, y describirlos tomando en cuenta su ubicación, "
                "clima y biodiversidad."
            ),
            codigo="CN.4.4.12.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Elaborar y ejecutar un plan de investigación documental "
                "sobre los ecosistemas de Ecuador, diferenciarlos por su "
                "ubicación geográfica, clima y biodiversidad, destacar su "
                "importancia y comunicar sus hallazgos por diferentes "
                "medios."
            ),
            codigo="CN.4.4.13.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar en forma documental sobre la historia de la vida en "
                "la Tierra, explicar los procesos por los cuales los "
                "organismos han ido evolucionando e interpretar la "
                "complejidad biológica actual."
            ),
            codigo="CN.4.4.14.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Formular hipótesis e investigar en forma documental los "
                "procesos geológicos y los efectos de las cinco extinciones "
                "masivas ocurridas en la Tierra, relacionarlas con el "
                "registro de los restos fósiles y diseñar una escala de "
                "tiempo sobre el registro paleontológico de la Tierra."
            ),
            codigo="CN.4.4.15.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Investigar en forma documental y procesar evidencias sobre "
                "los movimientos de las placas tectónicas, e inferir sus "
                "efectos en los cambios en el clima y en la distribución de "
                "los organismos."
            ),
            codigo="CN.4.4.16.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        Destreza(
            description=(
                "Indagar sobre la formación y el ciclo de las rocas, "
                "clasificarlas y describirlas de acuerdo a los procesos de "
                "formación y su composición."
            ),
            codigo="CN.4.4.17.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque4
        ),
        # Bloque 5
        Destreza(
            description=(
                "Indagar el proceso de desarrollo tecnológico del "
                "microscopio y del telescopio y analizar el aporte al "
                "desarrollo de la ciencia y la tecnología."
            ),
            codigo="CN.4.5.1.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Planificar y ejecutar una investigación documental sobre la "
                "historia de la astronomía y los hitos más importantes de la "
                "exploración espacial y comunicar sobre su impacto "
                "tecnológico."
            ),
            codigo="CN.4.5.2.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Planificar y ejecutar un proyecto de investigación "
                "documental sobre el fechado radioactivo de los cambios de "
                "la Tierra a lo largo del tiempo, inferir sobre su "
                "importancia para la determinación de las eras o épocas "
                "geológicas de la Tierra y comunicar de manera gráfica sus "
                "resultados."
            ),
            codigo="CN.4.5.3.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Investigar en forma documental sobre el aporte del "
                "científico ecuatoriano Pedro Vicente Maldonado en la "
                "verificación experimental de la ley de la gravitación "
                "universal, comunicar sus conclusiones y valorar su "
                "contribución."
            ),
            codigo="CN.4.5.4.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar, con uso de las TIC y otros recursos, y analizar "
                "las causas de los impactos de las actividades humanas en "
                "los hábitats, inferir sus consecuencias y discutir los "
                "resultados."
            ),
            codigo="CN.4.5.5.",
            imprescindible=True,
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Plantear problemas de salud sexual y reproductiva, "
                "relacionarlos con las infecciones de transmisión sexual, "
                "investigar las estadísticas actuales del país, identificar "
                "variables, comunicar los resultados y analizar los "
                "programas de salud sexual y reproductiva."
            ),
            codigo="CN.4.5.6.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Diseñar y ejecutar un plan de investigación documental, "
                "formular hipótesis sobre los efectos de las erupciones "
                "volcánicas en la corteza terrestre, contrastarla con los "
                "resultados y comunicar sus conclusiones."
            ),
            codigo="CN.4.5.7.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Formular hipótesis e investigar en forma documental sobre "
                "el funcionamiento de la cadena trófica en el manglar, "
                "identificar explicaciones consistentes, y aceptar o refutar "
                "la hipótesis planteada."
            ),
            codigo="CN.4.5.8.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
        Destreza(
            description=(
                "Indagar sobre el viaje de Alexander Von Humboldt a América "
                "y los aportes de sus descubrimientos e interpretar sus "
                "resultados acerca de las relaciones clima-vegetación."
            ),
            codigo="CN.4.5.9.",
            asignatura=ciencias_naturales,
            subnivel=superior,
            bloque=bloque5
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0030_auto_20180813_1621'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
