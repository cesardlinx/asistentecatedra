from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )

    # Asignaturas
    historia = Asignatura.objects.get(name='Historia')
    filosofia = Asignatura.objects.get(name='Filosofía')
    educacion_ciudadania = Asignatura.objects.get(
        name='Educación para la Ciudadanía'
    )

    # bachillerato
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    CriterioEvaluacion.objects.bulk_create([
        # Historia
        CriterioEvaluacion(
            description=(
                "Analiza y diferencia la historia real de la construcción "
                "cultural historiográfica producto de la investigación "
                "basada en fuentes, enfoques y condicionantes materiales y "
                "simbólicos."
            ),
            codigo="CE.CS.H.5.1.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica y valora la importancia del trabajo como eje de la "
                "supervivencia humana y de las revoluciones culturales "
                "paleolítica y neolítica."
            ),
            codigo="CE.CS.H.5.2.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y evalúa la organización social y educativa de la "
                "comunidad primitiva matriarcal y su crisis a partir de la "
                "división del trabajo, la aparición de la propiedad privada, "
                "las clases sociales y el predomino patriarcal sustentado "
                "enla apropiación privada de la riqueza social y el "
                "machismo."
            ),
            codigo="CE.CS.H.5.3.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica y valora el papel protagónico de la mujer a lo "
                "largo de toda la historia, desde la comunidad primitiva "
                "hasta el presente, destacando sus liderazgos intelectuales "
                "y políticos, sus luchas contra la dominación y sus "
                "distintos roles sociales."
            ),
            codigo="CE.CS.H.5.4.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Describe y valora los grandes aportes tecnológicos, "
                "económicos y científicos de las culturas de Mesopotamia, "
                "China, India y Egipto a la humanidad, y su impacto en la "
                "contemporaneidad."
            ),
            codigo="CE.CS.H.5.5.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y comprende la influencia de griegos, romanos y "
                "judíos en la conformación de la modernidad occidental "
                "capitalista, el Renacimiento, el Humanismo y la Reforma, "
                "por medio de la razón, el derecho, el monoteísmo y la "
                "visión lineal del tiempo."
            ),
            codigo="CE.CS.H.5.6.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina la trascendencia del Imperio bizantino, como "
                "heredero y custodio de la herencia grecorromana, en "
                "relación con el Renacimiento, la difusión del cristianismo "
                "y el islamismo, la conservación del arte y la cultura "
                "grecolatina y el desarrollo educativo universitario, en un "
                "contexto de guerras religiosas y luchas feudales."
            ),
            codigo="CE.CS.H.5.7.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina y evalúa el legado artístico y cultural del Islam, "
                "su origen, expansión, su conflicto histórico con el Estado "
                "judío y sus contrastes con el judaísmo y el cristianismo."
            ),
            codigo="CE.CS.H.5.8.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y comprende el origen y desarrollo de la "
                "Modernidad, a partir del análisis del Renacimiento, la "
                "Reforma, la Ilustración, la Revolución francesa y el "
                "proyecto napoleónico como puntos de culminación y crisis de "
                "la modernidad."
            ),
            codigo="CE.CS.H.5.9.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica y valora el origen, desarrollo, propuestas y "
                "desafíos de los movimientos sociales, sus formas de lucha y "
                "respuesta a las relaciones de poder y los medios de "
                "comunicación."
            ),
            codigo="CE.CS.H.5.10.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica y valora las contribuciones éticas, intelectuales, "
                "económicas y ecológicas de las grandes culturas "
                "precolombinas, destacando su relación armónica con la "
                "naturaleza, sus formas equitativas de organización y "
                "justicia social y su legado arquitectónico."
            ),
            codigo="CE.CS.H.5.11.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina el impacto de la Conquista y Colonización europea "
                "en América en los hábitos y relaciones sociales, en la "
                "alienación aborigen y la formación del mestizaje y su "
                "legado cultural, considerando los procesos de explotación "
                "en haciendas y plantaciones, la introducción de especies "
                "animales y vegetales foráneas y el tráfico de perosnas "
                "esclavizadas liderado por las grandes potencias."
            ),
            codigo="CE.CS.H.5.12.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y contrasta el proceso de conquista y colonización "
                "portuguesa en Brasil, y sus especificidades económicas en "
                "relación con la Conquista y Colonización española."
            ),
            codigo="CE.CS.H.5.13.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina y comprende los procesos de mestizaje y sincretismo "
                "artístico y cultural hispanoamericano, considerando la "
                "función social e ideológica del arte, la educación y la "
                "evangelización en las relaciones de poder colonial."
            ),
            codigo="CE.CS.H.5.14.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y discute el origen, desarrollo y propuestas de los "
                "grandes movimientos de liberación de los siglos XVIII, XIX "
                "y XX en América Latina, destacando el papel de sus líderes "
                "y protagonistas colectivos y la vigencia o caducidad de sus "
                "ideales originarios."
            ),
            codigo="CE.CS.H.5.15.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica y comprende las contradicciones de los procesos de "
                "independencia latinoamericana y la formación de sus "
                "repúblicas liberales excluyentes y racistas, las "
                "limitaciones de las democracias burguesas expresadas en la "
                "crisis económica de los treinta, y la respuesta de la CEPAL "
                "como opción aún vigente en un escenario histórico "
                "cambiante."
            ),
            codigo="CE.CS.H.5.16.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina y evalúa el proceso económico, político y social "
                "del Ecuador a partir del “boom” petrolero, su relación con "
                "la crisis de la deuda, la crisis de los 80 y el proyecto de "
                "“Revolución Ciudadana”."
            ),
            codigo="CE.CS.H.5.17.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y compara los sistemas socioeconómicos esclavista y "
                "feudal, sus características y transición, con las formas "
                "económicas precolombinas y el “modelo colonial” "
                "mercantilista, en relación con el proceso de acumulación "
                "originaria de capital."
            ),
            codigo="CE.CS.H.5.18.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina y determina el origen, desarrollo y etapas del "
                "capitalismo, su ideología liberal, sus revoluciones "
                "económicas y políticas fundamentales y el debate "
                "librecambismo – proteccionismo aún vigente."
            ),
            codigo="CE.CS.H.5.19.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina y determina el origen histórico del socialismo, sus "
                "características y revoluciones más significativas, su lucha "
                "y crisis en el contexto de la “Guerra Fría” y el dominio "
                "neoliberal y su relación con el socialismo del siglo XXI y "
                "las nuevas propuestas en América Latina."
            ),
            codigo="CE.CS.H.5.20.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Identifica y explica el origen histórico y los principios "
                "fundamentales de las principales corrientes del pensamiento "
                "económico, consideradas como respuestas concretas a "
                "procesos sociales reales, y su relación con nuestra "
                "realidad nacional y latinoamericana."
            ),
            codigo="CE.CS.H.5.21.",
            asignatura=historia,
            subnivel=bachillerato
        ),
        # #Educación para la ciudadanía
        CriterioEvaluacion(
            description=(
                "Explica la evolución histórica de la ciudadanía, los "
                "derechos y las declaraciones de derechos reconociendo su "
                "relación con el individuo, la sociedad y poder político."
            ),
            codigo="CE.CS.EC.5.1.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina la igualdad natural y su traducción jurídica como "
                "base fundamental del reconocimiento de oportunidades, "
                "derechos y obligaciones en diferentes espacios políticos, "
                "sociales o comunitarios, sin distinción a ningún grupo "
                "social."
            ),
            codigo="CE.CS.EC.5.2.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina el origen y características de la democracia "
                "moderna(representativa y deliberativa), reconociendo la "
                "complementariedad y ventajas o desventajas que hay entre "
                "ellas, así como el papel del ciudadano, partiendo del "
                "estudio de diversas fuentes y casos."
            ),
            codigo="CE.CS.EC.5.3.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza la importancia de la deliberación ciudadana en los "
                "procesos democráticos y los mecanismos de legitimación "
                "social del poder político, para el sostenimiento de la "
                "democracia representativa o social basada en el "
                "cumplimiento de los derechos civiles y políticos."
            ),
            codigo="CE.CS.EC.5.4.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Practica y valora el ejercicio de la deliberación "
                "democrática en los diferentes espacios cotidianos, "
                "reconociéndolo como mecanismo de expresión para el "
                "ejercicio de la ciudadanía y cumplimiento de derechos y "
                "obligaciones que permiten el consenso y disenso en un grupo "
                "social."
            ),
            codigo="CE.CS.EC.5.5.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica el desarrollo de la democracia en el país, "
                "identificando los procesos inclusivos, las limitaciones en "
                "la concreción de demandas sociales, los alcances y "
                "mecanismos de acción ciudadana para la eficacia de la "
                "representación política."
            ),
            codigo="CE.CS.EC.5.6.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina los beneficios de la cultura nacional fundamentada "
                "en la plurinacionalidad, valorando los aportes de cada "
                "cultura y sus luchas sociales y políticas por alcanzar la "
                "plenitud en la construcción y cumplimiento de sus derechos, "
                "en pos de una sociedad intercultural."
            ),
            codigo="CE.CS.EC.5.7.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica la evolución histórica del Estado como forma de "
                "control social, identificando los mecanismos e "
                "instituciones que emplea para ejercer dicho control, y las "
                "funciones que lo diferencian de nación y gobierno."
            ),
            codigo="CE.CS.EC.5.8.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina el significado político y social de las Asambleas "
                "Constituyentes, considerando su necesidad, el protagonismo "
                "del pueblo como legitimador de su poder y las "
                "Constituciones como producto político y jurídico de sus "
                "acciones."
            ),
            codigo="CE.CS.EC.5.9.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Examina las formas y postulados del republicanismo en "
                "contraste con otras formas de comprender la democracia, "
                "partiendo del análisis de casos."
            ),
            codigo="CE.CS.EC.5.10.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato
        ),
        # Filosofía
        CriterioEvaluacion(
            description=(
                "Contrasta el pensamiento mítico y cotidiano del pensamiento "
                "científico y filosófico, estableciendo semejanzas y "
                "diferencias, considerando su relación con varias "
                "disciplinas y su esfuerzo por plantear preguntas complejas "
                "y explicar la sociedad y la naturaleza por ellas mismas."
            ),
            codigo="CE.CS.F.5.1.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Relaciona la reflexión filosófica con los conflictos de "
                "poder, el ejercicio político y ciudadano por medio del "
                "análisis de sus conceptos fundamentales, la práctica del "
                "método socrático, la deliberación, la persuasión racional y "
                "creativa, en función de la igualdad social y la crítica a "
                "toda forma de intolerancia al pensamiento diferente, como "
                "en el caso de Hipatia."
            ),
            codigo="CE.CS.F.5.2.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Diferencia la verdad de la validez aplicándolas a la "
                "formación de conceptos y teorías y diferenciándolas en las "
                "ciencias formales y fácticas, mediante el uso de ejemplos."
            ),
            codigo="CE.CS.F.5.3.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Comprende y aplica los instrumentos intelectuales de la "
                "argumentación lógica, evitando falacias, paradojas y "
                "contradicciones, estableciendo las ideas centrales y "
                "secundarias en la construcción de un discurso coherente y "
                "riguroso."
            ),
            codigo="CE.CS.F.5.4.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Compara las características del pensamiento filosófico "
                "occidental y latinoamericano, con sus nuevas concepciones, "
                "identificando sus preocupaciones esenciales (“yo” – "
                "“nosotros”; “objetividad” – “subjetividad”; “libertad” – "
                "“liberación”), su contexto histórico, su identidad, cultura "
                "y las características de sus productos intelectuales "
                "específicos (el ensayo y el tratado), discutiendo desde el "
                "método socrático el Sumak Kawsay como proyecto utópico "
                "posible en la construcción del “ser” latinoamericano."
            ),
            codigo="CE.CS.F.5.5.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Discute los fundamentos de la ética, las nociones de bien y "
                "mal, a partir del análisis de las virtudes platónicas y "
                "aristotélicas, la concepción cristiana de la virtud y el "
                "pecado y las reflexiones de Kant y Bentham, aplicándolas a "
                "la sociedad y la política."
            ),
            codigo="CE.CS.F.5.6.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y diferencia los significados de estética y placer "
                "en diferentes contextos históricos, considerando su "
                "relación con el espacio público y el privado y las "
                "reflexiones de Epicuro y Onfray."
            ),
            codigo="CE.CS.F.5.7.",
            asignatura=filosofia,
            subnivel=bachillerato
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0032_auto_20180809_1258'),
    ]

    operations = [
        migrations.RunPython(create_criterios)
    ]
