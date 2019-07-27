from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    estudios_sociales = Asignatura.objects.get(name='Estudios Sociales')

    # Bloques
    bloque1 = BloqueCurricular.objects.get(name="Historia e identidad")
    bloque2 = BloqueCurricular.objects.get(
        name="Los seres humanos en el espacio")
    bloque3 = BloqueCurricular.objects.get(name="La convivencia")

    # Subniveles
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Destreza.objects.bulk_create([
        # Elemental
        # Bloque 1
        Destreza(
            description=(
                "Reconocer a la familia como espacio primigenio de comunidad "
                "y núcleo de la sociedad, constituída como un sistema "
                "abierto, donde sus miembros se interrelacionan y están "
                "unidos por lazos de parentesco, solidaridad, afinidad, "
                "necesidad y amor; apoyándose mutuamente para subsistir, "
                "concibiendose como seres únicos e irrepetibles."
            ),
            codigo="CS.2.1.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los tipos de familia basándose en el "
                "reconocimiento de sus diferencias, tanto en estructuras "
                "como en diversas realidades sociales (migración, divorcio, "
                "etc.)."
            ),
            codigo="CS.2.1.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar la historia de la familia considerando la "
                "procedencia de sus antepasados, su cultura y roles, en "
                "función de fortalecer la identidad como miembro de ella."
            ),
            codigo="CS.2.1.3.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la importancia de la escuela a partir de la "
                "investigación de sus orígenes fundacionales, la función "
                "social que cumple, sus características más sobresalientes "
                "(nombre, símbolos, entre otros) y su aporte a la comunidad."
            ),
            codigo="CS.2.1.4.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar la escuela como un espacio de socialización e "
                "intercambio de costumbres, tradiciones y conocimientos, que "
                "influyen en la construcción de la identidad."
            ),
            codigo="CS.2.1.5.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Indagar los orígenes fundacionales y las características "
                "más significativas de la localidad, parroquia, cantón y "
                "provincia, mediante el uso de diversas fuentes."
            ),
            codigo="CS.2.1.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el hecho histórico más relevante de la provincia, "
                "considerando fuentes y evidencias materiales (documentos, "
                "monumentos, museos, restos arqueológicos, etc.) y "
                "describirlo de forma oral, escrita o gráfica."
            ),
            codigo="CS.2.1.7.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer acontecimientos, lugares y personajes de la "
                "localidad, parroquia, cantón, provincia y país, destacando "
                "su relevancia en la cohesión social e identidad local o "
                "nacional."
            ),
            codigo="CS.2.1.8.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Distinguir y apreciar las actividades culturales "
                "(costumbres, alimentación, tradiciones, festividades, "
                "actividades recreativas, lenguas, religiones, expresiones "
                "artísticas) de la localidad, parroquia, cantón, provincia y "
                "país."
            ),
            codigo="CS.2.1.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Localizar y apreciar el patrimonio natural y cultural de la "
                "localidad, parroquia, cantón, provincia y país, mediante la "
                "identificación de sus características y el reconocimiento "
                "de la necesidad social de su cuidado y conservación."
            ),
            codigo="CS.2.1.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir la diversidad humana, cultural y natural a través "
                "del análisis de los grupos sociales y étnicos que forman "
                "parte del barrio, comunidad, parroquia, cantón, provincia y "
                "país, con el fin de reconocerlas como componentes de un "
                "país diverso."
            ),
            codigo="CS.2.1.11.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir y apreciar las cualidades y valores de los "
                "diversos grupos sociales y étnicos del Ecuador como aportes "
                "a la construcción de nuestra identidad y cultura nacional."
            ),
            codigo="CS.2.1.12.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Reconocer y ubicar la vivienda, la escuela y la localidad a "
                "partir de puntos de referencia y representaciones gráficas "
                "(croquis, planos, etc.), considerando accidentes "
                "geográficos y posibles riesgos naturales."
            ),
            codigo="CS.2.2.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir los diferentes tipos de vivienda y sus "
                "estructuras en las diversas localidades, regiones y climas, "
                "a través de la observación directa, el uso de las TIC y/u "
                "otros recursos."
            ),
            codigo="CS.2.2.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar los posibles riesgos que pueden presentarse en "
                "la vivienda para prevenirlos y salvaguardar la seguridad en "
                "el hogar."
            ),
            codigo="CS.2.2.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Proponer planes de contingencia que se pueden aplicar en "
                "caso de un desastre natural, en la vivienda o escuela."
            ),
            codigo="CS.2.2.4.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Opinar acerca de las oportunidades y amenazas de la "
                "ubicación geográfica de la localidad, comunidad, parroquia, "
                "cantón y provincia, por medio del uso de TIC y/o de "
                "material cartográfico."
            ),
            codigo="CS.2.2.5.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar las funciones y responsabilidades de las "
                "autoridades y ciudadanos, relacionadas con los fenómenos "
                "naturales y sus posibles amenazas, promoviendo medidas de "
                "prevención."
            ),
            codigo="CS.2.2.6.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir la división político-administrativa de la "
                "localidad, comunidad, parroquia, cantón y provincia, "
                "relacionándola con la construcción de la identidad local y "
                "sus valores específicos."
            ),
            codigo="CS.2.2.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar la capital, las ciudades y las autoridades de "
                "la provincia, considerando su nivel demográfico, la "
                "provisión de servicios básicos y la acción responsable en "
                "la solución de las necesidades sociales."
            ),
            codigo="CS.2.2.8.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar las parroquias urbanas y rurales a partir de su "
                "ubicación, organización administrativa y división "
                "territorial y reconocer la importancia de su creación para "
                "la atención de los problemas y necesidades de sus "
                "habitantes y del entorno."
            ),
            codigo="CS.2.2.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar la importancia de las actividades económicas "
                "(ocupaciones, turismo, medios de subsistencia, provisión de "
                "bienes y servicios) que caracterizan a la localidad, la "
                "comunidad, la parroquia, el cantón y la provincia, para "
                "identificar su influencia en la calidad de vida de sus "
                "habitantes."
            ),
            codigo="CS.2.2.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar los atractivos turísticos más importantes de la "
                "localidad, comunidad, parroquia, cantón, provincia y país, "
                "y su influencia en el desarrollo local y nacional."
            ),
            codigo="CS.2.2.11.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar los problemas económicos y demográficos que "
                "enfrenta la provincia: despoblación del campo, migración, "
                "concentración urbana, mortalidad, etc., a partir de la "
                "observación y análisis de datos estadísticos presentados en "
                "pictogramas, tablas y barras."
            ),
            codigo="CS.2.2.12.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Examinar y describir acciones para prevenir desastres "
                "tomando en cuenta los accidentes geográficos, las "
                "condiciones y ubicación de la vivienda y sus instalaciones."
            ),
            codigo="CS.2.2.13.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir la geografía de la provincia (relieve, "
                "hidrografía y diversidad natural) considerando su "
                "incidencia en la vida de sus habitantes y asociándola con "
                "los problemas ambientales y el uso, explotación y "
                "conservación de sus recursos naturales."
            ),
            codigo="CS.2.2.14.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir los medios de transporte, los servicios públicos "
                "y las vías de comunicación de la localidad, comunidad, "
                "parroquia, cantón y provincia, a partir del análisis de su "
                "impacto en la seguridad y calidad de vida de sus "
                "habitantes."
            ),
            codigo="CS.2.2.15.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar y apreciar la megadiversidad del Ecuador, a través "
                "de la identificación de sus límites, regiones naturales, "
                "provincias, su flora y fauna más representativa."
            ),
            codigo="CS.2.2.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer al Ecuador como parte del continente americano y "
                "el mundo, identificando las semejanzas de sus "
                "características (regiones naturales, clima, paisajes, flora "
                "y fauna) con las del resto del continente."
            ),
            codigo="CS.2.2.17.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Localizar los distintos territorios en los que se subdivide "
                "el continente americano: América del Norte, Centroamérica y "
                "América del Sur, a partir de la observación e "
                "interpretación de material cartográfico."
            ),
            codigo="CS.2.2.18.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar las relaciones del Ecuador con los países de "
                "América del Sur y sus puntos en común en función del "
                "desarrollo regional."
            ),
            codigo="CS.2.2.19.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Expresar opiniones acerca de las diversas formas de "
                "protección, seguridad, solidaridad y respeto en la familia, "
                "reconociendo la importancia de los acuerdos, vínculos "
                "afectivos, valores, derechos, responsabilidades y el "
                "trabajo equitativo de todos sus miembros en función del "
                "bienestar común."
            ),
            codigo="CS.2.3.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer la escuela como un espacio de interacción "
                "compartida, lúdico y de aprendizaje con compañeros y "
                "maestros, basado en acuerdos, normas, derechos y deberes."
            ),
            codigo="CS.2.3.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar los derechos de los ciudadanos ecuatorianos, en "
                "relación con el reconocimiento de sus deberes con el Estado "
                "y consigo mismos."
            ),
            codigo="CS.2.3.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar los derechos y responsabilidades de los niños y "
                "niñas mediante la participación en espacios familiares, "
                "escolares y en su ejercicio ciudadano."
            ),
            codigo="CS.2.3.4.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Describir los derechos y obligaciones más relevantes "
                "relacionados con el tránsito y la educación vial."
            ),
            codigo="CS.2.3.5.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Participar en acciones de cooperación, trabajo solidario y "
                "reciprocidad (minga, randi-randi) y apreciar su "
                "contribución al desarrollo de la comunidad, "
                "ejemplificándolas con temas de seguridad vial y desastres "
                "naturales."
            ),
            codigo="CS.2.3.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir la importancia de las normas, los derechos y las "
                "obligaciones en la construcción de relaciones personales y "
                "sociales equitativas y armónicas."
            ),
            codigo="CS.2.3.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Apreciar y practicar el cuidado de los servicios públicos y "
                "el patrimonio, en función del bienestar colectivo y el "
                "desarrollo sustentable."
            ),
            codigo="CS.2.3.8.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir el concepto de sustentabilidad como expresión de "
                "un compromiso ético, en función de legar un mundo mejor a "
                "las futuras generaciones."
            ),
            codigo="CS.2.3.9.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Examinar las cualidades y los valores humanos que nos hacen "
                "valiosos como ecuatorianos."
            ),
            codigo="CS.2.3.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Describir las funciones y responsabilidades primordiales "
                "que tienen las autoridades en función del servicio a la "
                "comunidad y la calidad de vida."
            ),
            codigo="CS.2.3.11.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer que todos los habitantes del mundo estamos "
                "vinculados por medio del respeto y la promoción de los "
                "derechos humanos universales, declarados por la "
                "Organización de las Naciones Unidas (ONU)."
            ),
            codigo="CS.2.3.12.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Elaborar una declaración de derechos para los niños que "
                "incluyan aspectos no tomados en cuenta hasta ahora por las "
                "declaraciones de los adultos, en función del Buen Vivir."
            ),
            codigo="CS.2.3.13.",
            asignatura=estudios_sociales,
            subnivel=elemental,
            bloque=bloque3
        ),
        # Media
        # Bloque 1
        Destreza(
            description=(
                "Analizar el origen de los primeros pobladores del Ecuador, "
                "sus rutas de llegada, sus herramientas y formas de trabajo "
                "colectivo."
            ),
            codigo="CS.3.1.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar la organización económica y social de las "
                "sociedades agrícolas con su alfarería y el surgimiento de "
                "sus primeros poblados."
            ),
            codigo="CS.3.1.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar la ubicación, la organización social y política "
                "de los cacicazgos mayores o señoríos étnicos, con sus "
                "relaciones de comercio, alianzas y enfrentamientos."
            ),
            codigo="CS.3.1.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar las características de la dominación incaica en el "
                "Ecuador, la organización de su imperio y sociedad."
            ),
            codigo="CS.3.1.4.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el ascenso de Atahualpa y la guerra civil como "
                "efectos de una crisis del incario y como antecedentes de la "
                "derrota ante la invasión española."
            ),
            codigo="CS.3.1.5.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar varios sitios arqueológicos y las piezas que se "
                "han conservado, reconociéndolas como patrimonio nacional."
            ),
            codigo="CS.3.1.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Documentar la Conquista española del Tahuantinsuyo, "
                "especialmente del norte, con sus enfrentamientos y "
                "alianzas."
            ),
            codigo="CS.3.1.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar y discutir el fundamento científico de ciertas "
                "narraciones históricas tradicionales como el Reino de "
                "Quito, la dinastía de los Shyris, etc."
            ),
            codigo="CS.3.1.8.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar a los conquistadores españoles, su relación con "
                "los indígenas y sus conflictos con la Corona, el "
                "surgimiento de los mestizos y la llegada de los negros "
                "esclavizados."
            ),
            codigo="CS.3.1.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar los hechos iniciales de la colonización, en "
                "especial la fundación de ciudades y su papel en la "
                "dominación."
            ),
            codigo="CS.3.1.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar la organización del trabajo en la Audiencia de "
                "Quito y el papel de la producción textil."
            ),
            codigo="CS.3.1.11.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar la estructura de la sociedad colonial y la vida "
                "cotidiana con sus diferencias sociales y prácticas "
                "discriminatorias."
            ),
            codigo="CS.3.1.12.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir el significado del concepto “colonia” y las "
                "lecciones que dejó la Conquista y Colonización hispánica en "
                "la vida de la sociedad nacional."
            ),
            codigo="CS.3.1.13.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar las causas de la crisis que sufrió la Audiencia "
                "de Quito en el marco de los grandes cambios de la monarquía "
                "española y el mundo."
            ),
            codigo="CS.3.1.14.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Destacar la consolidación del latifundio, el inicio de la "
                "expansión de la Costa y las grandes sublevaciones indígenas "
                "y de las ciudades."
            ),
            codigo="CS.3.1.15.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar la función de dominación de la cultura oficial y "
                "la educación colonial y el valor de las culturas populares "
                "como respuesta frente al poder."
            ),
            codigo="CS.3.1.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar las obras artísticas de la Colonia como productos "
                "de una sociedad de desigualdades, y su función cultural, "
                "estética e ideológica."
            ),
            codigo="CS.3.1.17.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el trabajo artístico indígena y mestizo y el "
                "compromiso de proteger el patrimonio nacional."
            ),
            codigo="CS.3.1.18.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar, al fin de la Colonia, los primeros esfuerzos "
                "por definir la identidad del “país” en el marco de las "
                "contradicciones prevalecientes."
            ),
            codigo="CS.3.1.19.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el proceso de la Revolución de Quito de 1809 y su "
                "impacto, sus principales actores colectivos y "
                "consecuencias."
            ),
            codigo="CS.3.1.20.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Determinar las causas del vacío revolucionario entre 1812 y "
                "1820 y la reactivación de la independencia en Guayaquil."
            ),
            codigo="CS.3.1.21.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir las condiciones en las que el actual territorio "
                "del Ecuador se incorporó a Colombia, en el marco de la "
                "continuidad de la lucha por la independencia."
            ),
            codigo="CS.3.1.22.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar las condiciones económicas, políticas y sociales "
                "en que el “Distrito del Sur” de Colombia participó en la "
                "vida de ese país."
            ),
            codigo="CS.3.1.23.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar el alcance del proyecto bolivariano y su "
                "influencia en la integración de los países andinos y "
                "latinoamericanos."
            ),
            codigo="CS.3.1.24.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los territorios que formaban parte del Ecuador "
                "en 1830, su población y diversidad étnica."
            ),
            codigo="CS.3.1.25.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir los grupos sociales del naciente Ecuador, en "
                "especial los vinculados al espacio rural."
            ),
            codigo="CS.3.1.26.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar la vida de las ciudades y los actores urbanos "
                "fundamentales con el comercio del país."
            ),
            codigo="CS.3.1.27.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar la influencia de la regionalización y del "
                "enfrentamiento de las élites del Ecuador, ejemplificado en "
                "el nombre de la nueva república."
            ),
            codigo="CS.3.1.28.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar los alcances de la educación y la cultura, así "
                "como la influencia de la Iglesia católica al inicio de la "
                "época republicana."
            ),
            codigo="CS.3.1.29.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los actores sociales fundamentales en la vida "
                "cotidiana y la cultura popular en el nuevo Estado."
            ),
            codigo="CS.3.1.30.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el dominio de las oligarquías regionales en la "
                "reproducción de la pobreza y la desunión del Ecuador "
                "naciente."
            ),
            codigo="CS.3.1.31.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar la organización del Estado ecuatoriano en sus "
                "primeros años de vida republicana."
            ),
            codigo="CS.3.1.32.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar los inicios históricos de la República, subrayando "
                "el predominio del floreanismo y el esfuerzo organizador de "
                "Rocafuerte."
            ),
            codigo="CS.3.1.33.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el impacto de la “Revolución marcista” y la "
                "situación de inestabilidad y conflicto que desembocó en la "
                "crisis nacional de 1859."
            ),
            codigo="CS.3.1.34.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el proceso de consolidación del Estado bajo el "
                "régimen de García Moreno y su proyecto."
            ),
            codigo="CS.3.1.35.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar la etapa 1875-1895 con el inicio del auge "
                "cacaotero y sus conflictos sociales y políticos."
            ),
            codigo="CS.3.1.36.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar los principales esfuerzos intelectuales que se "
                "dieron a fines del siglo XIX por entender el país y su "
                "identidad, precisando sus principales representantes."
            ),
            codigo="CS.3.1.37.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Señalar acciones para consolidar la unidad nacional y la "
                "soberanía del país, a partir del análisis del proceso "
                "ocurrido a fines del siglo XIX sobre la identidad del "
                "Ecuador."
            ),
            codigo="CS.3.1.38.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar la vinculación del país al sistema mundial con la "
                "producción y exportación de cacao y el predominio de la "
                "burguesía comercial y bancaria."
            ),
            codigo="CS.3.1.39.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir el proceso de la Revolución liberal liderada por "
                "Eloy Alfaro con sus principales hechos y conflictos."
            ),
            codigo="CS.3.1.40.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar los rasgos esenciales del Estado laico: separación "
                "Estado-Iglesia, la modernización estatal, la educación "
                "laica e incorporación de la mujer a la vida pública."
            ),
            codigo="CS.3.1.41.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar los cambios que se dieron en la sociedad con el "
                "laicismo y la modernización, y su impacto en la vida "
                "cotidiana y la cultura."
            ),
            codigo="CS.3.1.42.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir las principales incidencias del llamado "
                "“predominio plutocrático”, con énfasis en la crisis "
                "cacaotera y la reacción social."
            ),
            codigo="CS.3.1.43.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Distinguir las condiciones de vida de los sectores "
                "populares durante el predominio oligárquico y sus "
                "respuestas frente a él."
            ),
            codigo="CS.3.1.44.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar las causas y consecuencias de la crisis económica "
                "y política que se dio entre los años veinte y cuarenta, y "
                "las respuestas de la insurgencia social."
            ),
            codigo="CS.3.1.45.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar los impactos de la crisis en la vida política y el "
                "desarrollo de manifestaciones artísticas comprometidas con "
                "el cambio social."
            ),
            codigo="CS.3.1.46.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los principales rasgos de la vida cotidiana, "
                "vestidos, costumbres y diversiones en la primera mitad del "
                "siglo XX."
            ),
            codigo="CS.3.1.47.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el proceso histórico entre 1925 a 1938, sus "
                "reformas estatales, la inestabilidad política y el "
                "surgimiento del velasquismo."
            ),
            codigo="CS.3.1.48.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir las causas y consecuencias de la guerra con el "
                "Perú y la desmembración territorial, subrayando el papel de "
                "la oligarquía liberal en este proceso."
            ),
            codigo="CS.3.1.49.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar la etapa del “auge bananero”, marcado por el "
                "ascenso de los sectores medios y la organización estatal."
            ),
            codigo="CS.3.1.50.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar el avance de la educación y de los derechos "
                "políticos y sociales como producto histórico de la lucha "
                "por la democracia."
            ),
            codigo="CS.3.1.51.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Exponer el alcance de la transformación agraria y los "
                "procesos de industrialización con sus consecuencias en la "
                "economía y la política."
            ),
            codigo="CS.3.1.52.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el surgimiento del “boom” petrolero ecuatoriano en "
                "los años setenta y su impacto en la sociedad, el "
                "robustecimiento del Estado y el inicio del endeudamiento "
                "externo."
            ),
            codigo="CS.3.1.53.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir las condiciones del gran crecimiento poblacional "
                "del país, la expansión de las ciudades, la migración "
                "interna y el crecimiento de los servicios."
            ),
            codigo="CS.3.1.54.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la presencia de nuevos actores sociales, como "
                "trabajadores y empresarios, y el ascenso del movimiento "
                "indígena, las organizaciones de mujeres y ecologistas, en "
                "la construcción de la conciencia de la diversidad."
            ),
            codigo="CS.3.1.55.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar los cambios en la vida de la gente y la cultura a "
                "causa de la modernización, las reformas religiosas y los "
                "cambios tecnológicos."
            ),
            codigo="CS.3.1.56.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el papel que el Estado ha cumplido en la economía "
                "y la promoción social a fines del siglo XX."
            ),
            codigo="CS.3.1.57.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Comparar la década 1960-1970 con la subsiguiente 1970-1979, "
                "destacando el papel de las fuerzas armadas y los "
                "movimientos sociales."
            ),
            codigo="CS.3.1.58.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el proceso de transición al régimen constitucional "
                "de fines de los setenta e inicios de los ochenta, con los "
                "cambios sociales y políticos que se produjeron."
            ),
            codigo="CS.3.1.59.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar el papel que cumplió nuestro país al final del "
                "siglo XX en el panorama internacional."
            ),
            codigo="CS.3.1.60.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el predominio del neoliberalismo a fines del "
                "siglo XX e inicios del XXI, con el incremento de la deuda "
                "externa, la emigración, la concentración de la riqueza, el "
                "aumento de la pobreza, la respuesta de los movimientos "
                "sociales y la inestabilidad política."
            ),
            codigo="CS.3.1.61.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer la secuencia de los regímenes de las dos décadas "
                "finales del siglo XX, sus políticas económicas y la "
                "respuesta de la movilización social."
            ),
            codigo="CS.3.1.62.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar la vigencia de la democracia y sus consecuencias "
                "en la sociedad actual, en la calidad de vida y el Buen "
                "Vivir."
            ),
            codigo="CS.3.1.63.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir los hechos recientes del país a inicios del siglo "
                "XXI, con sus conflictos y transformaciones políticas y "
                "sociales."
            ),
            codigo="CS.3.1.64.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Revisar los desafíos más urgentes que tiene el Ecuador "
                "frente a la globalización, la democracia y la unidad "
                "nacional."
            ),
            codigo="CS.3.1.65.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el compromiso que tiene la juventud en la "
                "construcción del Ecuador del Buen Vivir y la integración "
                "regional."
            ),
            codigo="CS.3.1.66.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Describir el territorio del Ecuador, destacando sus "
                "características principales como parte integrante del "
                "espacio andino."
            ),
            codigo="CS.3.2.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar y describir las principales características y "
                "rasgos geográficos del Ecuador que lo hacen singular, a "
                "través de diversas herramientas gráficas y multimedia."
            ),
            codigo="CS.3.2.2.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Localizar los relieves, suelos y regiones naturales del "
                "Ecuador con el apoyo de diversos recursos cartográficos."
            ),
            codigo="CS.3.2.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir relieves, cordilleras y hoyas, sistemas "
                "fluviales, espacios agrícolas, pecuarios, selváticos, de "
                "páramo y las características peculiares de Costa, Sierra, "
                "Amazonía y región Insular de Galápagos."
            ),
            codigo="CS.3.2.4.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Interpretar mapas e imágenes satelitales en función de "
                "reconocer y ubicar las características del territorio y sus "
                "accidentes geográficos, relacionándolos con posibles "
                "desastres naturales."
            ),
            codigo="CS.3.2.5.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar la estructura geológica del territorio del "
                "Ecuador con su volcanismo activo, en relación con los "
                "riesgos para la población y los planes de contingencia para "
                "afrontarlos."
            ),
            codigo="CS.3.2.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Localizar los recursos hídricos del Ecuador con sus "
                "principales ríos y cuencas de agua considerando su "
                "aprovechamiento para el desarrollo nacional."
            ),
            codigo="CS.3.2.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Exponer la influencia de los climas y su impacto en la vida "
                "vegetal, animal y humana, considerando posibles riesgos "
                "(Fenómeno del Niño) y sus respectivos planes de "
                "contingencia."
            ),
            codigo="CS.3.2.8.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Discutir los riesgos sísmicos que existen en el Ecuador y "
                "las medidas que deben tomarse en caso de desastres, sobre "
                "todo de modo preventivo."
            ),
            codigo="CS.3.2.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar la gran diversidad de la población del Ecuador "
                "como riqueza y oportunidad para el desarrollo y crecimiento "
                "del país."
            ),
            codigo="CS.3.2.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Apreciar el origen diverso de la población ecuatoriana, su "
                "vocación y trabajo para construir un país unitario y "
                "equitativo."
            ),
            codigo="CS.3.2.11.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer y apreciar la diversidad de la población "
                "ecuatoriana a partir de la observación y el análisis de su "
                "ubicación geográfica, alimentación, forma de vestir, "
                "costumbres, fiestas, etc."
            ),
            codigo="CS.3.2.12.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Establecer el origen histórico de los indígenas, mestizos y "
                "afrodescendientes y montubios del Ecuador, su evolución "
                "histórica, en la Colonia y la República, su diversidad, "
                "identidad, organización y luchas por su liberación."
            ),
            codigo="CS.3.2.13.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar los diversos procesos de inmigración al "
                "Ecuador, el origen de los inmigrantes y su participación en "
                "la sociedad nacional, así como el impacto de la reciente "
                "migración al extranjero."

            ),
            codigo="CS.3.2.14.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Discutir las características comunes de la población "
                "ecuatoriana en relación con la construcción de la unidad "
                "nacional y el rechazo a toda forma de discriminación."
            ),
            codigo="CS.3.2.15.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Apreciar el crecimiento de la población del Ecuador, con "
                "énfasis en sus principales causas y consecuencias."
            ),
            codigo="CS.3.2.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar el acceso a educación y salud de los niños, niñas, "
                "adultos, mayores, y personas con discapacidad, considerando "
                "variables demográficas y geográficas."
            ),
            codigo="CS.3.2.17.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar indicadores de la población del Ecuador con los de "
                "otros países, destacando diferencias étnicas y culturales, "
                "niveles de acceso a empleo y servicios básicos."
            ),
            codigo="CS.3.2.18.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Establecer las ventajas y desventajas de la organización "
                "territorial del Ecuador en provincias, cantones, parroquias "
                "y regiones transversales, considerando su utilidad para el "
                "desarrollo nacional."
            ),
            codigo="CS.3.2.19.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Distinguir las características de los gobiernos "
                "provinciales del Ecuador, destacando su incidencia en la "
                "satisfacción de las necesidades de sus habitantes y la "
                "construcción de su identidad."
            ),
            codigo="CS.3.2.20.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar las características político-administrativas de "
                "los gobiernos provinciales, municipales y parroquiales del "
                "país, destacando su cercanía con el pueblo y su capacidad "
                "para enfrentar cuestiones locales."
            ),
            codigo="CS.3.2.21.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer las formas de participación popular de las "
                "provincias, cantones y parroquias en la vida pública, "
                "destacando el trabajo y la acción colectivos en pro del "
                "bien común."
            ),
            codigo="CS.3.2.22.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Exponer la realidad de la población del Ecuador, "
                "considerando su localización en el territorio a partir de "
                "los últimos censos realizados en el país."
            ),
            codigo="CS.3.2.23.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer los principales rasgos físicos (relieves, "
                "hidrografía, climas, áreas cultivables, pisos ecológicos, "
                "etc.), de las provincias de la Costa norte, de la Costa "
                "sur, de la Sierra norte, de la Sierra centro, de la Sierra "
                "sur, de la Amazonía y de la región Insular de Galápagos."
            ),
            codigo="CS.3.2.24.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer los rasgos más sobresalientes de las provincias "
                "del país basándonos en ejercicios gráficos, el uso de "
                "Internet, las redes sociales y destacar sus semejanzas y "
                "diferencias."
            ),
            codigo="CS.3.2.25.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar la división natural del Ecuador con su división "
                "territorial en función de establecer concordancias o "
                "inconsistencias para el desarrollo del país."
            ),
            codigo="CS.3.2.26.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Analizar las acciones y omisiones que provocan daños al "
                "ambiente y desarrollar una cultura de respeto con "
                "propuestas creativas y eficaces."
            ),
            codigo="CS.3.3.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Distinguir al Ecuador como uno de los países con mayor "
                "diversidad (cultural, étnica, geográfica, florística y "
                "faunística)."
            ),
            codigo="CS.3.3.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer las áreas protegidas del Ecuador, proponiendo "
                "actividades y estrategias para preservarlos."
            ),
            codigo="CS.3.3.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar las condiciones de los bosques ecuatorianos y las "
                "acciones que se pueden realizar para protegerlos y prevenir "
                "incendios."
            ),
            codigo="CS.3.3.4.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Comparar los efectos concretos que el cambio climático ha "
                "provocado en el país en los últimos tiempos y plantear "
                "acciones viables para revertir dicho proceso."
            ),
            codigo="CS.3.3.5.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir las causas y los efectos del calentamiento global "
                "en el planeta y las acciones colectivas que se deben tomar "
                "para enfrentarlo."
            ),
            codigo="CS.3.3.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Plantear actividades concretas para la protección y "
                "conservación del ambiente (siembra de árboles, reciclaje, "
                "ahorro de agua y combustibles, etc.)."
            ),
            codigo="CS.3.3.7.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer la importancia de la organización y la "
                "participación social como condición indispensable para "
                "construir una sociedad justa y solidaria."
            ),
            codigo="CS.3.3.8.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Destacar y analizar la existencia y el funcionamiento de "
                "las organizaciones sociales más representativas de la "
                "sociedad ecuatoriana."
            ),
            codigo="CS.3.3.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar los antiguos y nuevos movimientos sociales que "
                "han influido en las transformaciones de los últimos "
                "tiempos."
            ),
            codigo="CS.3.3.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir sobre las acciones que se pueden implementar "
                "dentro de la escuela para lograr una sociedad más justa y "
                "equitativa."
            ),
            codigo="CS.3.3.11.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar la participación de mujeres y hombres en el marco "
                "de la diversidad, la equidad de género y el rechazo a toda "
                "forma de discriminación."
            ),
            codigo="CS.3.3.12.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir la situación de las personas con discapacidad en "
                "el Ecuador y sus posibilidades de inclusión y participación "
                "productiva en la sociedad."
            ),
            codigo="CS.3.3.13.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Construir una propuesta colectiva con medidas y acciones "
                "concretas y viables tendientes a brindar un trato más justo "
                "a las personas con discapacidad."
            ),
            codigo="CS.3.3.14.",
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Examinar las principales denominaciones religiosas que "
                "existen en el Ecuador, destacando su función social y sus "
                "características más importantes."
            ),
            codigo="CS.3.3.15.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Destacar el avance que significó el establecimiento del "
                "laicismo y el derecho a la libertad de cultos en el país."
            ),
            codigo="CS.3.3.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=media,
            bloque=bloque3
        ),
        # Superior
        # Bloque 1
        Destreza(
            description=(
                "Reconocer el estudio de la Historia como conocimiento "
                "esencial para entender nuestro pasado y nuestra identidad y "
                "para comprender cómo influyen en el mundo en que vivimos."
            ),
            codigo="CS.4.1.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir el origen de la humanidad en África y su difusión "
                "a los cinco continentes, con base en el trabajo y su "
                "capacidad de adaptación a diversos ambientes y situaciones "
                "climáticas."
            ),
            codigo="CS.4.1.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir la influencia de la agricultura y la escritura en "
                "las formas de vida y de organización social de la "
                "humanidad."
            ),
            codigo="CS.4.1.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el trabajo como factor fundamental de la "
                "evolución y desarrollo de una sociedad, y su influencia en "
                "la construcción de la cultura material y simbólica de la "
                "humanidad."
            ),
            codigo="CS.4.1.4.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los grandes Imperios esclavistas de la "
                "Antigüedad en el Oriente Medio, destacando el rol de la "
                "agricultura, la escritura y los ejércitos."
            ),
            codigo="CS.4.1.5.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar y apreciar el surgimiento y desarrollo de los "
                "grandes Imperios asiáticos, especialmente de China e India."
            ),
            codigo="CS.4.1.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar la naturaleza de las culturas mediterráneas, "
                "especialmente la griega, con énfasis en su influencia en el "
                "pensamiento filosófico y democrático."
            ),
            codigo="CS.4.1.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Caracterizar el Imperio romano, su expansión en el "
                "Mediterráneo, sus rasgos esclavistas e institucionales e "
                "influencia ulterior."
            ),
            codigo="CS.4.1.8.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el surgimiento y difusión conflictiva del "
                "cristianismo en el espacio mediterráneo romano y luego en "
                "Europa."
            ),
            codigo="CS.4.1.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar en la historia las estructuras sociales de "
                "desigualdad, y comparar situaciones semejantes en diversos "
                "momentos históricos y lugares geográficos."
            ),
            codigo="CS.4.1.10.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Caracterizar el surgimiento del Islam en Arabia y su "
                "difusión al norte de África y otros lugares del viejo "
                "continente."
            ),
            codigo="CS.4.1.11.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar la estructura de la sociedad feudal europea, "
                "sus condiciones de explotación interna y los grupos "
                "sociales enfrentados."
            ),
            codigo="CS.4.1.12.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Destacar los cambios producidos con las cruzadas y el fin "
                "del medioevo y sus consecuencias."
            ),
            codigo="CS.4.1.13.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resumir el origen y desarrollo de la conciencia humanista "
                "que influyó en una nueva visión de las personas y el mundo."
            ),
            codigo="CS.4.1.14.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Practicar el entendimiento de la diversidad religiosa y la "
                "tolerancia en la vida social."
            ),
            codigo="CS.4.1.15.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el origen de los primeros pobladores de América y "
                "sus formas de supervivencia, con base en las evidencias "
                "materiales que se han descubierto."
            ),
            codigo="CS.4.1.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar el papel de la mujer en la invención de la "
                "agricultura como un esfuerzo de conocimiento y trabajo "
                "acumulado."
            ),
            codigo="CS.4.1.17.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Destacar el desarrollo de los pueblos aborígenes de América "
                "y la formación de grandes civilizaciones como la maya y la "
                "azteca."
            ),
            codigo="CS.4.1.18.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el desarrollo de las culturas andinas anteriores "
                "al incario con sus principales avances civilizatorios."
            ),
            codigo="CS.4.1.19.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el origen y desarrollo del Imperio inca como "
                "civilización y la influencia de su aparato político y "
                "militar."
            ),
            codigo="CS.4.1.20.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir la estructura organizativa del Tahuantinsuyo y la "
                "organización social para reproducirla y participar en ella."
            ),
            codigo="CS.4.1.21.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar y apreciar el legado material y cultural indígena "
                "en la configuración de los países latinoamericanos."
            ),
            codigo="CS.4.1.22.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Contrastar los rasgos más significativos que diferencien "
                "las culturas americanas de aquellas que llegaron con la "
                "conquista y la colonización europea."
            ),
            codigo="CS.4.1.23.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar las motivaciones de los europeos para buscar "
                "nuevas rutas marítimas al Lejano Oriente y analizar cómo "
                "llegaron a la India y “descubrieron” América."
            ),
            codigo="CS.4.1.24.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el proceso de conquista española del Imperio inca "
                "en crisis y la resistencia de los pueblos indígenas."
            ),
            codigo="CS.4.1.25.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Exponer la organización y los mecanismos de gobierno y de "
                "extracción de riquezas que empleaba el Imperio colonial "
                "español en América."
            ),
            codigo="CS.4.1.26.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Comparar el proceso de colonización española de América con "
                "el portugués y anglosajón, subrayando sus semejanzas y "
                "diferencias."
            ),
            codigo="CS.4.1.27.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el papel que cumplió la América española en un "
                "mundo en transformación durante los siglos XVI y XVII."
            ),
            codigo="CS.4.1.28.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Destacar la contribución de los progresos científicos de "
                "los siglos XVII y XVIII a los cambios sociales y "
                "económicos."
            ),
            codigo="CS.4.1.29.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el avance del capitalismo, el crecimiento de la "
                "producción manufacturera, la expansión de las ciudades y "
                "del intercambio internacional."
            ),
            codigo="CS.4.1.30.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el proceso de independencia de Estados Unidos, su "
                "establecimiento como la primera república democrática, y "
                "sus consecuencias."
            ),
            codigo="CS.4.1.31.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir el sentido de las revoluciones europeas de fines "
                "del siglo XVIII y XIX."
            ),
            codigo="CS.4.1.32.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Exponer la naturaleza de la Ilustración en Europa y América "
                "y las condiciones para la caída del Antiguo Régimen en "
                "ambos continentes."
            ),
            codigo="CS.4.1.33.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Evaluar la herencia de las sociedades coloniales en la "
                "América Latina del presente."
            ),
            codigo="CS.4.1.34.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar críticamente la naturaleza de las revoluciones "
                "independentistas de América Latina, sus causas y "
                "limitaciones."
            ),
            codigo="CS.4.1.35.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el proceso de independencia en Sudamérica desde el "
                "norte hasta el sur, reconociendo los actores sociales que "
                "participaron en él."
            ),
            codigo="CS.4.1.36.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Destacar la participación y el aporte de los "
                "afrodescendientes en los procesos de independencia de "
                "Latinoamérica."
            ),
            codigo="CS.4.1.37.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el contenido del proyecto de Simón Bolívar y la "
                "disolución de Colombia, con su proyección en los procesos "
                "de integración actuales."
            ),
            codigo="CS.4.1.38.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Contrastar los valores de la independencia y la libertad en "
                "el contexto de las naciones latinoamericanas en el siglo "
                "XIX y XX."
            ),
            codigo="CS.4.1.39.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar los avances científicos y técnicos que "
                "posibilitaron el gran auge de la industria y el cambio en "
                "las condiciones de vida que se dieron entre los siglos "
                "XVIII y XIX."
            ),
            codigo="CS.4.1.40.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Revisar el desarrollo del capitalismo en el mundo del siglo "
                "XIX, bajo condiciones de avance del imperialismo."
            ),
            codigo="CS.4.1.41.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Exponer las características de los Estados nacionales "
                "latinoamericanos luego de la Independencia y su influencia "
                "en la construcción de la identidad de los países en el "
                "presente."
            ),
            codigo="CS.4.1.42.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar las condiciones en las que las economías "
                "latinoamericanas se incorporaron al mercado mundial en el "
                "siglo XIX."
            ),
            codigo="CS.4.1.43.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir los procesos y conflictos que se dieron por la "
                "definición de las fronteras en América Latina."
            ),
            codigo="CS.4.1.44.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar las características de la expansión de la "
                "industria, el comercio internacional y el colonialismo a "
                "inicios del siglo XX."
            ),
            codigo="CS.4.1.45.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resumir la influencia y el impacto de la Revolución "
                "bolchevique y de la Primera Guerra Mundial en la economía y "
                "la sociedad latinoamericana."
            ),
            codigo="CS.4.1.46.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Examinar el impacto de la Gran Depresión y de los regímenes "
                "fascistas en la política y la sociedad latinoamericana."
            ),
            codigo="CS.4.1.47.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar el nivel de involucramiento de América Latina en "
                "la Segunda Guerra Mundial y su participación en la "
                "fundación y acciones de la Organización de las Naciones "
                "Unidas."
            ),
            codigo="CS.4.1.48.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar la trayectoria de Latinoamérica en la primera "
                "mitad del siglo XX, con sus cambios socioeconómicos e "
                "inicios del desarrollismo."
            ),
            codigo="CS.4.1.49.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar cambios en la realidad latinoamericana a partir "
                "de la fundación de la República Popular China, el ascenso "
                "de los países árabes y el predominio de la “Guerra Fría”."
            ),
            codigo="CS.4.1.50.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Comparar el contenido de las luchas anticoloniales de los "
                "países en vías de desarrollo y la fundación de nuevos "
                "países."
            ),
            codigo="CS.4.1.51.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir el alcance de las innovaciones científicas y "
                "tecnológicas, especialmente en la comunicación, en el "
                "contexto latinoamericano del siglo XX."
            ),
            codigo="CS.4.1.52.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer los movimientos de lucha por los derechos civiles "
                "en el marco de los procesos de integración y cooperación "
                "internacional."
            ),
            codigo="CS.4.1.53.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Discutir la pertinencia y validez de los postulados de "
                "Mahatma Gandhi en relación con la construcción de una "
                "cultura de paz y el respeto a los derechos humanos en la "
                "contemporaneidad."
            ),
            codigo="CS.4.1.54.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Evaluar la movilización social e insurgencia en la América "
                "Latina de los sesenta, la Revolución cubana y los inicios "
                "de la integración."
            ),
            codigo="CS.4.1.55.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Analizar las características de las dictaduras "
                "latinoamericanas y sus gobiernos, con énfasis en el "
                "desarrollismo y la represión."
            ),
            codigo="CS.4.1.56.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Apreciar el tránsito a los sistemas constitucionales "
                "latinoamericanos, destacando el valor de vivir en "
                "democracia."
            ),
            codigo="CS.4.1.57.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Explicar el proceso de implantación del neoliberalismo en "
                "América Latina."
            ),
            codigo="CS.4.1.58.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Comparar la situación económica y social de los países "
                "desarrollados y en vías de desarrollo."
            ),
            codigo="CS.4.1.59.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resumir los desafíos de América Latina frente al manejo de "
                "la información y los medios de comunicación en el marco de "
                "la situación económica, política y social actual."
            ),
            codigo="CS.4.1.60.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Examinar el proceso de formación de la Tierra, la gestación "
                "de los continentes y las sucesivas eras geológicas."
            ),
            codigo="CS.4.2.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Localizar y describir los océanos y mares del mundo, sus "
                "movimientos y efectos en la vida del planeta."
            ),
            codigo="CS.4.2.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir los diversos climas del planeta con sus "
                "características, variaciones e influencia en la población "
                "mundial, destacando posibles desastres naturales y sus "
                "correspondientes planes de contingencia."
            ),
            codigo="CS.4.2.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer el significado conceptual de Cartografía y "
                "examinar los diversos instrumentos y recursos "
                "cartográficos, sus características específicas y su "
                "utilidad para los estudios de Geografía y otras ciencias."
            ),
            codigo="CS.4.2.4.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir las características fundamentales de África, "
                "Europa, Asia y Oceanía: relieves, hidrografía, climas, "
                "demografía y principales indicadores de calidad de vida."
            ),
            codigo="CS.4.2.5.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar la extensión y características generales de los "
                "continentes desde perspectivas geográficas, demográficas, "
                "económicas, etc."
            ),
            codigo="CS.4.2.6.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir las características fundamentales de América del "
                "Norte, América Central y América del Sur: relieves, "
                "hidrografía, climas, demografía y principales indicadores "
                "de calidad de vida."
            ),
            codigo="CS.4.2.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar algunos rasgos geográficos relevantes entre las "
                "Américas, especialmente relacionados con la economía, la "
                "demografía y la calidad de vida."
            ),
            codigo="CS.4.2.8.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Localizar y apreciar los recursos naturales del Ecuador y "
                "establecer su importancia económica y social."
            ),
            codigo="CS.4.2.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Relacionar y discutir las actividades productivas del "
                "sector primario (agricultura, ganadería, pesca, minería) "
                "con los ingresos y calidad de vida de las personas que se "
                "dedican a ellas."
            ),
            codigo="CS.4.2.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar las actividades productivas del sector secundario "
                "nacional (industrias y artesanías) y las personas que se "
                "ocupan en ellas."
            ),
            codigo="CS.4.2.11.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Examinar la interrelación entre los lugares, las personas y "
                "los productos que están involucrados en el comercio y sus "
                "mutuas incidencias."
            ),
            codigo="CS.4.2.12.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Destacar la importancia del sector servicios en la economía "
                "nacional, destacando el turismo con sus fortalezas, "
                "oportunidades, debilidades y amenazas."
            ),
            codigo="CS.4.2.13.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar el papel del sector financiero en el país y la "
                "necesidad de su control por parte de la sociedad y el "
                "Estado."
            ),
            codigo="CS.4.2.14.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Establecer las diversas formas en que el Estado participa "
                "en la economía y los efectos de esa participación en la "
                "vida de la sociedad."
            ),
            codigo="CS.4.2.15.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar los principales problemas económicos del país, "
                "ejemplificando posibles alternativas de superación."
            ),
            codigo="CS.4.2.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Discutir el concepto de “desarrollo” en contraste con el "
                "Buen Vivir, desde una perspectiva integral, que incluya "
                "naturaleza, humanidad y sustentabilidad."
            ),
            codigo="CS.4.2.17.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Examinar la situación en que se encuentra el sistema "
                "educativo, sus niveles, crecimiento y calidad, frente a las "
                "necesidades nacionales."
            ),
            codigo="CS.4.2.18.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar el estado en que se encuentran los sistemas de "
                "salud en el país frente a las necesidades de la sociedad "
                "ecuatoriana."
            ),
            codigo="CS.4.2.19.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar las demandas existentes sobre vivienda "
                "comparándola con la forma en que se está enfrentando esta "
                "realidad en el país."
            ),
            codigo="CS.4.2.20.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Ubicar en el territorio las necesidades de transporte de la "
                "ciudadanía y los medios que se han establecido para "
                "satisfacerlas."
            ),
            codigo="CS.4.2.21.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Discutir la importancia del empleo y los problemas del "
                "subempleo y el desempleo, destacando la realidad de la "
                "Seguridad Social."
            ),
            codigo="CS.4.2.22.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer la importancia del deporte en la vida nacional, "
                "las principales disciplinas deportivas que se practican y "
                "los avances en su infraestructura."
            ),
            codigo="CS.4.2.23.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Relacionar las opciones de ocio y recreación de los "
                "ecuatorianos como ocasiones para estimular vínculos que "
                "posibiliten la construcción de la identidad nacional."
            ),
            codigo="CS.4.2.24.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer el Buen Vivir o Sumak Kawsay como una forma "
                "alternativa de enfrentar la vida, desechando las presiones "
                "del capitalismo y buscando el equilibrio del ser humano con "
                "la naturaleza."
            ),
            codigo="CS.4.2.25.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir y apreciar la diversidad cultural de la población "
                "mundial y el respeto que se merece frente a cualquier forma "
                "de discriminación."
            ),
            codigo="CS.4.2.26.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir los rasgos, antecedentes y valores esenciales de la "
                "diversidad humana que posibilitan la convivencia armónica y "
                "solidaria."
            ),
            codigo="CS.4.2.27.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Establecer el número de habitantes y su distribución en los "
                "continentes, con el detalle de sus características "
                "económicas, sociales y laborales esenciales."
            ),
            codigo="CS.4.2.28.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar los componentes etarios de la población "
                "mundial: niños, niñas, jóvenes y adultos, cotejándolos con "
                "datos sobre salud y educación."
            ),
            codigo="CS.4.2.29.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Discutir el papel que cumplen los jóvenes en la vida "
                "nacional e internacional a través de ejemplos de diversos "
                "países."
            ),
            codigo="CS.4.2.30.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Relacionar la población de hombres y mujeres en el mundo, "
                "considerando su distribución en los continentes y su "
                "promedio y niveles de calidad de vida."
            ),
            codigo="CS.4.2.31.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir el papel que han cumplido las migraciones en el "
                "pasado y presente de la humanidad."
            ),
            codigo="CS.4.2.32.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Explicar los principales flujos migratorios en América "
                "Latina, sus causas y consecuencias y sus dificultades y "
                "conflictos."
            ),
            codigo="CS.4.2.33.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar las incidencias más significativas de la "
                "globalización en la sociedad ecuatoriana y las posibles "
                "respuestas frente a ellas."
            ),
            codigo="CS.4.2.34.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Discutir las consecuencias que genera la concentración de "
                "la riqueza, proponiendo posibles opciones de solución."
            ),
            codigo="CS.4.2.35.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar los rasgos más importantes de la pobreza en "
                "América Latina, con énfasis en aspectos comparativos entre "
                "países."
            ),
            codigo="CS.4.2.36.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar las guerras como una de las principales causas "
                "de la pobreza en el mundo."
            ),
            codigo="CS.4.2.37.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer la influencia que han tenido en el Ecuador los "
                "conflictos mundiales recientes y el papel que ha tenido en "
                "ellos nuestro país."
            ),
            codigo="CS.4.2.38.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar los diversos procesos de integración internacional "
                "que se dan en el mundo, con énfasis particular en la Unión "
                "Europea, sus avances y problemas."
            ),
            codigo="CS.4.2.39.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar el origen y principales avances de la "
                "integración en la Comunidad Andina y Sudamérica, con sus "
                "problemas y perspectivas."
            ),
            codigo="CS.4.2.40.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Analizar la dimensión y gravedad del tráfico de personas y "
                "de drogas en relación con las propuestas de integración "
                "regional."
            ),
            codigo="CS.4.2.41.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Apreciar las culturas del Ecuador a partir del estudio de "
                "su origen, localización y rasgos más destacados."
            ),
            codigo="CS.4.3.1.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir las características, complejidades y posibilidades "
                "de la “cultura nacional” ecuatoriana."
            ),
            codigo="CS.4.3.2.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar el origen, las expresiones y manifestaciones de "
                "la cultura popular ecuatoriana como componente esencial de "
                "la cultura nacional."
            ),
            codigo="CS.4.3.3.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer la interculturalidad desde el análisis de las "
                "diferentes manifestaciones culturales y la construcción del "
                "Ecuador como unidad en la diversidad."
            ),
            codigo="CS.4.3.4.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Examinar el concepto “interculturalidad” y posibles "
                "acciones concretas de practicarlo en la escuela y otros "
                "espacios locales más cercanos."
            ),
            codigo="CS.4.3.5.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Determinar el papel político y social de los medios de "
                "comunicación en el Ecuador, y la forma en que cumplen su "
                "misión."
            ),
            codigo="CS.4.3.6.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Promover el respeto a la libre expresión mediante prácticas "
                "cotidianas, en la perspectiva de construir consensos y "
                "acuerdos colectivos."
            ),
            codigo="CS.4.3.7.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer la importancia de lo que se llama la “cultura de "
                "masas” en la sociedad actual."
            ),
            codigo="CS.4.3.8.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir la democracia como gobierno del pueblo, cuya "
                "vigencia se fundamenta en la libertad y la justicia social."
            ),
            codigo="CS.4.3.9.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer la vinculación de los ciudadanos con el país a "
                "través del Estado y el ejercicio de la ciudadanía."
            ),
            codigo="CS.4.3.10.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir los alcances y las dificultades de la doble "
                "ciudadanía en el Ecuador y el mundo."
            ),
            codigo="CS.4.3.11.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar los derechos fundamentales estipulados en el "
                "Código de la Niñez y la Adolescencia y reflexionar sobre "
                "ellos en función del Buen Vivir."
            ),
            codigo="CS.4.3.12.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer que la existencia de derechos implica deberes y "
                "responsabilidades que tenemos todos como parte de la "
                "sociedad."
            ),
            codigo="CS.4.3.13.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer la importancia de la lucha por los derechos "
                "humanos y su protección y cumplimiento como una "
                "responsabilidad de todos los ciudadanos y ciudadanas."
            ),
            codigo="CS.4.3.14.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar la tensión en relación con la vigencia de los "
                "derechos humanos, interculturalidad, unidad nacional y "
                "globalización."
            ),
            codigo="CS.4.3.15.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Destacar los valores de la libertad, la equidad y la "
                "solidaridad como fundamentos sociales esenciales de una "
                "democracia real."
            ),
            codigo="CS.4.3.16.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Discutir el significado de participación ciudadana y los "
                "canales y formas en que se la ejerce en una sociedad "
                "democrática."
            ),
            codigo="CS.4.3.17.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer el papel de la Constitución de la República como "
                "norma fundamental del Estado y base legal de la democracia."
            ),
            codigo="CS.4.3.18.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar la eficacia real de la Constitución como garante "
                "de los derechos ciudadanos, a partir del análisis de las "
                "garantías constitucionales."
            ),
            codigo="CS.4.3.19.",
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Relacionar el ejercicio de la ciudadanía ecuatoriana con la "
                "participación en los procesos de integración regional e "
                "internacional."
            ),
            codigo="CS.4.3.20.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar y diferenciar los órganos del gobierno y los "
                "del Estado ecuatoriano, sus principales atribuciones y sus "
                "mecanismos de vinculación con la sociedad civil."
            ),
            codigo="CS.4.3.21.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer y discutir la razón de ser, las funciones, los "
                "límites y las características de la fuerza pública."
            ),
            codigo="CS.4.3.22.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar el papel del Estado como garante de los derechos "
                "de las personas."
            ),
            codigo="CS.4.3.23.",
            imprescindible=True,
            asignatura=estudios_sociales,
            subnivel=superior,
            bloque=bloque3
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0031_auto_20180814_0700'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
