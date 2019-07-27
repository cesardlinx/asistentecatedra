from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignatura
    estudios_sociales = Asignatura.objects.get(name='Estudios Sociales')

    # Subniveles
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    CriterioEvaluacion.objects.bulk_create([
        # Elemental
        CriterioEvaluacion(
            description=(
                "Identifica los diferentes tipos de familia basándose en el "
                "análisis de sus diferencias, reconociéndola como fuente de "
                "bienestar e indaga su historia familiar para fortalecer su "
                "propia identidad."
            ),
            codigo="CE.CS.2.1.",
            asignatura=estudios_sociales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Examina los posibles riesgos que existen en su vivienda, "
                "escuela y localidad, reconociendo los planes de "
                "contingencia que puede aplicar en caso de algún desastre "
                "natural."
            ),
            codigo="CE.CS.2.2.",
            asignatura=estudios_sociales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Explica la importancia que tienen la escuela y la comunidad "
                "como espacios en los que se fomentan las relaciones "
                "humanas, el aprendizaje y su desarrollo como ciudadano "
                "responsable."
            ),
            codigo="CE.CS.2.3.",
            asignatura=estudios_sociales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Analiza las características fundamentales del espacio del "
                "que forma parte, destacando la historia, la diversidad, la "
                "economía, la división político-administrativa, los riesgos "
                "naturales, los servicios públicos y las normas y derechos "
                "de los ciudadanos, en función de una convivencia humana "
                "solidaria y la construcción del Buen Vivir."
            ),
            codigo="CE.CS.2.4.",
            asignatura=estudios_sociales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Analiza las características principales de su provincia "
                "(hecho histórico, ciudades principales, geografía, "
                "problemas naturales, económicos y demográficos, funciones y "
                "responsabilidades de sus autoridades), desarrollando su "
                "sentido de identidad y pertenencia."
            ),
            codigo="CE.CS.2.5.",
            asignatura=estudios_sociales,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Explica las características diferenciales del Ecuador "
                "(cualidades, valores, grupos sociales y étnicos, regiones "
                "naturales, ubicación, derechos, responsabilidades) que "
                "aportan en la construcción de identidad y cultura nacional."
            ),
            codigo="CE.CS.2.6.",
            asignatura=estudios_sociales,
            subnivel=elemental
        ),
        # Media
        CriterioEvaluacion(
            description=(
                "Analiza la evolución de la organización económica, política "
                "y social que se dio en la época aborigen, destacando los "
                "enfrentamientos y alianzas de los incas ante la Conquista "
                "española."
            ),
            codigo="CE.CS.3.1.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Examina los cambios y lecciones que se dieron en la "
                "Conquista y Colonización de América (el origen de mestizos, "
                "afro-ecuatorianos, la dominación cultural, las "
                "sublevaciones indígenas y mestizas, su aporte al arte como "
                "expresión del dominio cultural), destacando la lucha de los "
                "indígenas por la identidad."
            ),
            codigo="CE.CS.3.2.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Examina la independencia ecuatoriana desde los procesos de "
                "Quito, Guayaquil y Pichincha hasta su incorporación al "
                "proyecto integracionista bolivariano de Colombia, "
                "destacando las condiciones económicas, políticas, sociales "
                "y las contradicciones prevalecientes en que se produjo."
            ),
            codigo="CE.CS.3.3.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y relaciona las nacientes condiciones de la "
                "República del Ecuador: su territorio, sociedad (urbana y "
                "rural), regionalización oligárquica, educación, cultura, "
                "pobreza y falta de unidad."
            ),
            codigo="CE.CS.3.4.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y explica la construcción histórica del Ecuador del "
                "siglo XIX, destacando el papel de Flores y Rocafuerte, la "
                "Revolución liberal, el proceso modernizador de García "
                "Moreno, la búsqueda de la identidad y unidad nacionales y "
                "el predominio de la burguesía comercial y bancaria."
            ),
            codigo="CE.CS.3.5.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Relaciona el papel de la oligarquía liberal y plutocrática "
                "con la crisis económica de los años veinte y territorial de "
                "los años cuarenta, las respuestas sociales y artísticas, la "
                "inestabilidad política de los años veinticinco al treinta y "
                "ocho, el origen del velasquismo, el conflicto bélico "
                "limítrofe con el Perú, el auge bananero y sus repercusiones "
                "en la vida social, económica y política."
            ),
            codigo="CE.CS.3.6.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Analiza la evolución histórica del Ecuador desde la segunda "
                "mitad del siglo XX hasta inicios del siglo XXI, subrayando "
                "los cambios a nivel agrario, energético, político, "
                "demográfico, migratorio, educativo, la modernización del "
                "Estado, “boom” petrolero, los proyectos desarrollistas, el "
                "retorno al régimen constitucional en 1979, el predominio "
                "neoliberal, la crisis de la deuda externa, la migración, "
                "los movimientos indígenas y sociales contemporáneos y los "
                "desafíos del Ecuador frente a la democracia, la unidad "
                "nacional y la globalización."
            ),
            codigo="CE.CS.3.7.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Distingue, con diversos recursos cartográficos, las "
                "regiones del Ecuador según sus características geográficas "
                "naturales."
            ),
            codigo="CE.CS.3.8.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Examina las características del país, recursos naturales y "
                "posibles riesgos y oportunidades de desarrollo y seguridad "
                "a nivel nacional y regional."
            ),
            codigo="CE.CS.3.9.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Examina la diversidad demografía de la población "
                "ecuatoriana en función de su origen y evolución histórica, "
                "grupos etarios y movimientos migratorios, valorando su "
                "aporte en el desarrollo integral del país."
            ),
            codigo="CE.CS.3.10.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica la división territorial y natural del "
                "Ecuador(provincias, cantones y parroquias), en función de "
                "sus características físicas, político-administrativas y sus "
                "formas de participación ciudadana."
            ),
            codigo="CE.CS.3.11.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Plantea estrategias de solución y reducción de los efectos "
                "del calentamiento global y cambio climático, a partir del "
                "análisis de su contexto próximo."
            ),
            codigo="CE.CS.3.12.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Examina la importancia de la organización social y de la "
                "participación de hombres, mujeres, personas con "
                "discapacidad para la defensa de derechos y objetivos "
                "comunes de una sociedad inclusiva, justa y equitativa."
            ),
            codigo="CE.CS.3.13.",
            asignatura=estudios_sociales,
            subnivel=media
        ),
        # Superior
        CriterioEvaluacion(
            description=(
                "Analiza y utiliza los conceptos de “historia y trabajo”, "
                "como herramientas teóricas en función de comprender el "
                "proceso de producción y reproducción de la cultura material "
                "y simbólica de los pueblos americanos y de la humanidad, "
                "destacando el protagonismo de la mujer en su evolución."
            ),
            codigo="CE.CS.4.1.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Analiza el origen de las sociedades divididas en clases en "
                "el mundo (esclavitud, pobreza), en función de los "
                "acontecimientos históricos de colonización y conquista "
                "(conquista del Imperio romano, conquista del Imperio inca, "
                "conquista europea en América) y la supervivencia de "
                "estructuras de desigualdad."
            ),
            codigo="CE.CS.4.2.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Examina las diferentes formas de conciencia e insurgencia "
                "social(cristianismo, humanismo, revoluciones, etc.) como "
                "expresiones y representaciones del poder en el contexto del "
                "paso de la antigüedad al feudalismo y al capitalismo, y el "
                "desarrollo de la modernidad, con sus transformaciones "
                "económicas, sociales, políticas e ideológicas en el mundo y "
                "América Latina."
            ),
            codigo="CE.CS.4.3.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica y aprecia los diversos procesos de conflictividad, "
                "insurgencia y lucha social por la independencia y la "
                "liberación de los pueblos, sus organizaciones y propuestas "
                "contra la guerra y en defensa de la paz y respeto de los "
                "derechos humanos en América Latina y el mundo."
            ),
            codigo="CE.CS.4.4.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y relaciona los procesos históricos "
                "latinoamericanos, su independencia, integración, tareas y "
                "desafíos contemporáneos por la equidad, la inclusión y la "
                "justicia social."
            ),
            codigo="CE.CS.4.5.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Examina conceptual y prácticamente la Cartografía, en "
                "función de comprender los procesos de formación de la "
                "Tierra, las características diferenciales de sus "
                "continentes, océanos, mares y climas, reconociendo sus "
                "posibles riesgos, los planes de contingencia "
                "correspondientes y características particulares(económicas, "
                "demográficas, calidad de vida)."
            ),
            codigo="CE.CS.4.6.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Explica el rol y funcionamiento de los sectores económicos "
                "del Ecuador y el papel que cumplen cada uno de ellos en la "
                "economía del país, reconociendo la intervención del Estado "
                "en la economía y sus efectos en la sociedad."
            ),
            codigo="CE.CS.4.7.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y discute el concepto de Buen Vivir como respuesta "
                "integral a los problemas de educación, salud, vivienda, "
                "transporte, empleo y recreación del ser humano."
            ),
            codigo="CE.CS.4.8.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Examina la diversidad cultural de la población mundial a "
                "partir del análisis de género, grupo etario, movilidad y "
                "número de habitantes, según su distribución espacial en los "
                "cinco continentes, destacando el papel de la migración, de "
                "los jóvenes y las características esenciales que nos "
                "hermanan como parte de la Comunidad Andina y Sudamérica."
            ),
            codigo="CE.CS.4.9.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Examina la relación entre la democracia y la "
                "interculturalidad, reconociendo la importancia de la lucha "
                "por los derechos humanos, la Constitución, las "
                "manifestaciones culturales(nacional y popular) en la "
                "implementación y valoración de la interculturalidad en "
                "todos los espacios."
            ),
            codigo="CE.CS.4.10.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Analiza los derechos y responsabilidades sociales y "
                "políticas que tienen el Estado, la fuerza pública y la "
                "ciudadanía como grupo social, destacando aquellos "
                "referentes a las niñas, niños y jóvenes señalados en el "
                "Código de la Niñez y Adolescencia."
            ),
            codigo="CE.CS.4.11.",
            asignatura=estudios_sociales,
            subnivel=superior
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0022_auto_20180808_1840'),
    ]

    operations = [
        migrations.RunPython(
            create_criterios, reverse_code=migrations.RunPython.noop)
    ]
