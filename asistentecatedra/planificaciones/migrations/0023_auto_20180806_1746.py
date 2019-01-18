from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignaturas
    historia = Asignatura.objects.get(name='Historia')
    filosofia = Asignatura.objects.get(name='Filosofía')
    educacion_ciudadania = Asignatura.objects.get(
        name='Educación para la Ciudadanía')

    # Subniveles
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Objetivo.objects.bulk_create([
        # Historia
        Objetivo(
            description=(
                "Valorar los aportes de los pueblos orientales y americanos "
                "al acervo cultural humano, por medio del conocimiento de "
                "sus más significativos logros intelectuales, científicos, "
                "etc., para desechar visiones etnocéntricas y "
                "discriminatorias basadas en prejuicios y estereotipos."
            ),
            codigo='O.CS.H.5.1.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                "Identificar las manifestaciones culturales, a partir de la "
                "descripción del contexto histórico en que se originaron, "
                "para distinguir cuáles de estos elementos son parte de "
                "nuestra identidad latinoamericana y ecuatoriana, en la "
                "actualidad."
            ),
            codigo='O.CS.H.5.2.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                'Analizar y comprender los conceptos de "tiempo, historia, '
                'cultura y trabajo", a través del examen de las diferentes '
                'producciones y manifestaciones humanas para establecer las '
                'razones profundas de sus afanes, proyectos y utopías.'
            ),
            codigo='O.CS.H.5.3.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                "Estimar los principales aportes culturales de las diversas "
                "civilizaciones del orbe en la construcción de la historia "
                "universal y latinoamericana, mediante la identificación de "
                "sus contribuciones más importantes, para valorar la "
                "diversidad pasada y presente."
            ),
            codigo='O.CS.H.5.4.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                "Distinguir los grandes procesos económicos, sociales, "
                "culturales, políticos e ideológicos en América Latina y el "
                "Ecuador durante los últimos siglos, a partir del análisis "
                "de sus procesos de mestizaje y liberación, para comprender "
                "las razones profundas de sus formas de ser, pensar y "
                "actuar."
            ),
            codigo='O.CS.H.5.5.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                "Examinar los sistemas, teorías y escuelas económicas, a "
                "través de su relación con el trabajo, la producción y sus "
                "efectos en la sociedad, para decodificar la información de "
                "los medios de comunicación con las herramientas "
                "conceptuales idóneas, y poder enfrentar los retos sociales "
                "como ciudadanos y como agentes de cambio, ya sea en el "
                "mundo laboral, personal o comunitario."
            ),
            codigo='O.CS.H.5.6.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                "Reivindicar el rol histórico de la mujer y otros grupos "
                "sociales invisibilizados, destacando su protagonismo en la "
                "producción material y espiritual de la sociedad, en la "
                "invención y reproducción de saberes, costumbres y valores, "
                "y sus luchas sociales, para analizar y cuestionar diversas "
                "formas de discriminación, estereotipos y prejuicios."
            ),
            codigo='O.CS.H.5.7.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        Objetivo(
            description=(
                "Identificar el valor y la pertinencia de las diversas "
                "fuentes de información, incluyendo recursos multimedia, "
                "empleadas en la construcción de las narraciones históricas, "
                "utilizando medios de comunicación y TIC, diferenciando la "
                "construcción intelectual, de la realidad."
            ),
            codigo='O.CS.H.5.8.',
            subnivel=bachillerato,
            asignatura=historia
        ),
        # Filosofía
        Objetivo(
            description=(
                "Desarrollar mecanismos intelectuales que otorgan las "
                "lógicas polivalentes simbólicas contemporáneas para el "
                "análisis argumentativo y para el conocimiento del lenguaje "
                "humano, a través del combate a las falacias, "
                "contradicciones, juicios a priori, etc., en función de "
                "desarrollar en el estudiante una ética del razonamiento "
                "fundamentado y argumentado racionalmente."
            ),
            codigo='O.CS.F.5.1.',
            subnivel=bachillerato,
            asignatura=filosofia
        ),
        Objetivo(
            description=(
                "Analizar, comprender y valorar la complejidad histórica del "
                "pensamiento latinoamericano en su relación con otras formas "
                "de filosofar y pensar la realidad, a través de su "
                "imbricación con las urgencias vitales de su historia, para "
                "comprender la razón de ser de su “nosotros” pensante, a "
                "diferencia del “yo” pensante occidental."
            ),
            codigo='O.CS.F.5.2.',
            subnivel=bachillerato,
            asignatura=filosofia
        ),
        Objetivo(
            description=(
                "Comprender la dimensión espacial desde los conceptos "
                "filosóficos de Cosmos y Armonía, vinculándolos con los de "
                "Sumak Kawsay y Pachamama, en el afán de reivindicar una "
                "comprensión integral y alternativa."
            ),
            codigo='O.CS.F.5.3.',
            subnivel=bachillerato,
            asignatura=filosofia
        ),
        Objetivo(
            description=(
                "Interpretar las experiencias humanas por medio del análisis "
                "de las dimensiones ética, estética y política, la felicidad "
                "y el placer, para examinar y distinguir los principios y "
                "las implicaciones que se anudan en ellas en la vida "
                "cotidiana y en los grandes proyectos históricos."
            ),
            codigo='O.CS.F.5.4.',
            subnivel=bachillerato,
            asignatura=filosofia
        ),
        Objetivo(
            description=(
                "Conocer y aplicar las reglas de la argumentación lógica "
                "para validar razonamientos que contribuyan al desarrollo de "
                "la argumentación, la deliberación y la persuación, en "
                "función de una forma democrática de comunicación."
            ),
            codigo='O.CS.F.5.5.',
            subnivel=bachillerato,
            asignatura=filosofia
        ),
        # Educación para la Ciudadanía
        Objetivo(
            description=(
                "Analizar, comprender y valorar la importancia y "
                "trascendencia histórica de la Declaración de los Derechos "
                "del Hombre y del Ciudadano, de la Declaración de los "
                "Derechos de la Mujer y la Ciudadana y de la Declaración "
                "Universal de los Derechos Humanos en la construcción de las "
                "democracias modernas, para comprender su fundamento y "
                "estructura."
            ),
            codigo='O.CS.EC.5.1.',
            subnivel=bachillerato,
            asignatura=educacion_ciudadania
        ),
        Objetivo(
            description=(
                "Determinar el origen y significación de los conceptos de "
                "Ciudadanía y Derechos, como sustratos esenciales sobre los "
                "que descansa la democracia y el modelo latinoamericano de "
                "República, en función de la construcción permanente de la "
                "igualdad y la dignidad humanas."
            ),
            codigo='O.CS.EC.5.2.',
            subnivel=bachillerato,
            asignatura=educacion_ciudadania
        ),
        Objetivo(
            description=(
                "Utilizar y valorar el diálogo como forma de aproximación "
                "colectiva, reconociendo y practicando sus valores "
                "intrínsecos como el respeto mutuo, la tolerancia, el "
                "sentido autocrítico y demás valores democráticos."
            ),
            codigo='O.CS.EC.5.3.',
            subnivel=bachillerato,
            asignatura=educacion_ciudadania
        ),
        Objetivo(
            description=(
                "Construir un significado históricamente fundamentado y "
                "socialmente comprometido de ciudadanía, para discernir los "
                "significados de la actividad socio-política de los "
                "individuos y saber demandar y ejercer los derechos así como "
                "cumplir los deberes que la sustentan."
            ),
            codigo='O.CS.EC.5.4.',
            subnivel=bachillerato,
            asignatura=educacion_ciudadania
        ),
        Objetivo(
            description=(
                "Caracterizar y analizar la democracia moderna como "
                "experiencia y práctica social, además de política, "
                "sustentada en sus distintas formas de manifestación y "
                "relación con la configuración de una cultura plurinacional."
            ),
            codigo='O.CS.EC.5.5.',
            subnivel=bachillerato,
            asignatura=educacion_ciudadania
        ),
        Objetivo(
            description=(
                "Utilizar los medios de comunicación y las TIC para obtener, "
                "analizar y contrastar información que recoja diferentes "
                "enfoques y puntos de vista, con el fin de construir un "
                "pensamiento crítico, fundamentado, estructurado, coherente "
                "y riguroso."
            ),
            codigo='O.CS.EC.5.6.',
            subnivel=bachillerato,
            asignatura=educacion_ciudadania
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0022_auto_20180806_1513'),
    ]

    operations = [
        migrations.RunPython(create_objetivos)
    ]
