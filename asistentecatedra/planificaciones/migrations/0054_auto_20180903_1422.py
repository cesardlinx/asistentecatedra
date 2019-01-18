from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.1.4.")
    criterio1_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.1.5.")
    criterio1_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.1.6.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.5.")
    criterio2_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.2.6.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.8.")
    criterio3_9 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.9.")
    criterio3_10 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.10.")
    criterio3_11 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.11.")
    criterio3_12 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.12.")
    criterio3_13 = CriterioEvaluacion.objects.get(codigo="CE.CS.3.13.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.8.")
    criterio4_9 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.9.")
    criterio4_10 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.10.")
    criterio4_11 = CriterioEvaluacion.objects.get(codigo="CE.CS.4.11.")

    Indicador.objects.bulk_create([
        # Preparatoria
        Indicador(
            description=(
                "Expresa sus datos personales (nombre, apellidos, edad, "
                "teléfono, lugar donde vive y país en el que vive) y "
                "reconoce que es un ser que siente, piensa, opina y tiene "
                "necesidades. (J.4.)"
            ),
            codigo="I.CS.1.1.1.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Reconoce que tiene una historia personal, familiar y que "
                "forma parte de una comunidad y de un núcleo familiar con el "
                "que comparte actividades, de recreación y celebración, y "
                "que posee características estructurales que hay que "
                "respetar y valorar. (S1)"
            ),
            codigo="I.CS.1.1.2.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Practica con autonomía y responsabilidad actividades y "
                "tareas cotidianas, como hábitos de alimentación, higiene y "
                "cuidado personal. (J.3., I.4.)"
            ),
            codigo="I.CS.1.2.1.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Reconoce las situaciones de peligro de su entorno cercano, "
                "en función de evitar accidentes, mediante la aplicación de "
                "normas de seguridad, autorregulación y participación de las "
                "actividades propuestas por la comunidad escolar. (J.3.)"
            ),
            codigo="I.CS.1.2.2.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Practica normas de respeto consigo mismo y con los demás, "
                "respetando las diferencias individuales existentes, tanto "
                "en criterio como en opiniones, y practica los acuerdos "
                "establecidos con el grupo. (J.3., S.2., S.3., S.4.)"
            ),
            codigo="I.CS.1.3.1.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Reconoce sus derechos y responsabilidades y la importancia "
                "de asumir con responsabilidad sus compromisos, y discrimina "
                "los modelos positivos y negativos de comportamiento de su "
                "medio natural y social. (J.2., S.1.)"
            ),
            codigo="I.CS.1.3.2.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Reconoce la organización y dependencias de la vivienda y de "
                "la escuela, identificando la utilidad de la tecnología en "
                "esos espacios. (I.2.)"
            ),
            codigo="I.CS.1.4.1.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Reconoce la función que cumplen los medios de transporte, "
                "los medios de comunicación y las principales ocupaciones y "
                "profesiones que existen en la comunidad a la que pertenece. "
                "(J.1., I.2.)"
            ),
            codigo="I.CS.1.5.1.",
            criterio_evaluacion=criterio1_5
        ),
        Indicador(
            description=(
                "Identifica alguna de las manifestaciones culturales "
                "(música, comida, festividades, tradición oral) de la "
                "localidad y describe los lugares, tradiciones y costumbres "
                "importantes de la región y país al que pertenece. (J.1., "
                "I.2., S.2.)"
            ),
            codigo="I.CS.1.6.1.",
            criterio_evaluacion=criterio1_6
        ),
        # Elemental
        Indicador(
            description=(
                "Describe los diferentes tipos de familia y reflexiona sobre "
                "los derechos que ejercen y las responsabilidades que "
                "cumplen cada uno de sus miembros, reconociendo su historia "
                "familiar como parte importante en el fortalecimiento de su "
                "propia identidad. (J.1., J.3.)"
            ),
            codigo="I.CS.2.1.1.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Analiza los lazos y la historia familiar que unen a los "
                "miembros de su familia, identificando la importancia de "
                "contar con acuerdos, vínculos, valores, trabajo equitativo, "
                "derechos y responsabilidades que cumplir en función del "
                "bienestar común. (J.1., S.1.)"
            ),
            codigo="I.CS.2.1.2.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Infiere que la ubicación de su vivienda, escuela y "
                "localidad le otorga características diferenciales en cuanto "
                "a estructuras, accidentes geográficos y riesgos naturales, "
                "y analiza las posibles alternativas que puede aplicar en "
                "caso de un desastre natural. (J.4., I.2., S.1.)"
            ),
            codigo="I.CS.2.2.1.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Reconoce los datos importantes de su escuela (nombre, "
                "símbolos, historia) y la identifica como un espacio de "
                "socialización e intercambio de aprendizajes con compañeros "
                "y maestros, que influirán en la construcción de su "
                "identidad. (J.3., I.2.)"
            ),
            codigo="I.CS.2.3.1.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Reconoce que las acciones de cooperación, trabajo solidario "
                "y reciprocidad, el cumplimiento de sus derechos y "
                "obligaciones relacionadas con el tránsito y educación vial, "
                "contribuyen al desarrollo de la comunidad y elabora una "
                "declaración de derechos para los niños, en función del Buen "
                "Vivir. (J.2., J.3.)"
            ),
            codigo="I.CS.2.3.2.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Reconoce las características más relevantes (actividades "
                "culturales, patrimonios, acontecimientos, lugares, "
                "personajes y diversidad humana, natural, cultural y "
                "actividades económicas y atractivos turísticos) de su "
                "localidad, parroquia, cantón, provincia y país. (J.1., "
                "I.2.)"
            ),
            codigo="I.CS.2.4.1.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Analiza la división político-administrativa de su "
                "localidad, comunidad, parroquia, cantón y provincia, "
                "reconociendo las funciones y responsabilidades de las "
                "autoridades y ciudadanos en la conservación de medios de "
                "transporte, servicios públicos y vías de comunicación que "
                "brinden seguridad y calidad de vida a sus habitantes. "
                "(J.2., I.2.)"
            ),
            codigo="I.CS.2.4.2.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Reconoce la capital, las ciudades y el hecho histórico más "
                "relevante de su provincia, así como sus autoridades y las "
                "funciones y responsabilidades primoriales que estas tienen "
                "que cumplir en función de mejorar la calidad de vida de sus "
                "habitantes. (I.2.)"
            ),
            codigo="I.CS.2.5.1.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Analiza la geografía de su provincia y reconoce las "
                "acciones concretas que pueden realizar sus autoridades, a "
                "fin de prevenir los posibles desastres naturales, problemas "
                "económicos y demográficos. (I.1., I.2.)"
            ),
            codigo="I.CS.2.5.2.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Reconoce que todos los ecuatorianos tenemos derechos, "
                "deberes, cualidades y valores humanos que aportan en la "
                "construcción de nuestra identidad y cultura nacional. "
                "(J.1., S.2.)"
            ),
            codigo="I.CS.2.6.1.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Examina los límites, regiones naturales, diversidad de "
                "flora y fauna en relación con la división territorial del "
                "Ecuador, la provisión de servicios públicos, los "
                "patrimonios y la responsabilidad de los ecuatorianos, en "
                "función de su conservación y desarrollo sustentable. (J.1.)"
            ),
            codigo="I.CS.2.6.2.",
            criterio_evaluacion=criterio2_6
        ),
        Indicador(
            description=(
                "Reconoce la ubicación del país y sus semejanzas con los "
                "países del resto del continente, con énfasis en los países "
                "de América del Sur, reconociendo que todos estamos "
                "vinculados por el respeto y promoción de derechos humanos "
                "universales. (J.3., S.2.)"
            ),
            codigo="I.CS.2.6.3.",
            criterio_evaluacion=criterio2_6
        ),
        # Media
        Indicador(
            description=(
                "Explica la evolución de la organización económica y social "
                "de los primeros pobladores y sociedades agrícolas "
                "aborígenes mediante narraciones históricas con fundamento "
                "científico. (I.2.)"
            ),
            codigo="I.CS.3.1.1.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Analiza la relación entre organización social y política de "
                "los cacicazgos y la dominación incaica e invasión española, "
                "destacando sus enfrentamientos, alianzas y sitios "
                "arqueológicos, mediante narraciones históricas con "
                "fundamento científico. (I.2.)"
            ),
            codigo="I.CS.3.1.2.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Examina los cambios y las lecciones de la Conquista y "
                "Colonización (mestizaje, fundación de ciudades, producción "
                "textil, cambios en la vida cotidiana, diferencias sociales, "
                "discriminación, obras y trabajo artísticos de indígenas y "
                "mestizos). (I.2.)"
            ),
            codigo="I.CS.3.2.1.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Relaciona las causas de la crisis que sufrió la Audiencia "
                "de Quito con la consolidación del latifundio, la función de "
                "la cultura oficial, y el papel de la educación con los "
                "primeros esfuerzos por definir la identidad del “país”, "
                "destacando las lecciones que dejaron la Conquista y "
                "Colonización en este proceso. (I.2.)"
            ),
            codigo="I.CS.3.2.2.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Analiza la relación entre el proceso de la Revolución de "
                "Quito de 1809, el vacío revolucionario de 1812 a 1820 y el "
                "proyecto bolivariano. (I.2.)"
            ),
            codigo="I.CS.3.3.1.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Analiza las condiciones económicas, políticas y sociales de "
                "la incorporación del Distrito del Sur a Colombia en "
                "relación con el alcance del proyecto bolivariano y su "
                "influencia en la integración andina y latinoamericana. "
                "(I.2.)"
            ),
            codigo="I.CS.3.3.2.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Analiza las condiciones del Ecuador de 1830 (población, "
                "territorio, diversidad étnica, grupos sociales, vida en las "
                "ciudades), el papel de la regionalización y sus oligarquías "
                "en la reproducción de la pobreza y desunión. (I.2.)"
            ),
            codigo="I.CS.3.4.1.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Explica los alcances de la educación, la cultura popular, "
                "la iglesia y el dominio de las oligarquías regionales en la "
                "organización del Estado ecuatoriano. (I.2.)"
            ),
            codigo="I.CS.3.4.2.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Explica la vinculación del país al sistema mundial de "
                "producción, destacando el papel del floreanismo, el "
                "esfuerzo organizador de Rocafuerte, la Revolución marcista, "
                "el régimen de García Moreno y el auge cacaotero. (I.2.)"
            ),
            codigo="I.CS.3.5.1.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Explica los principales esfuerzos intelectuales que se "
                "dieron a fines del siglo XIX por entender el país, su "
                "identidad y la consolidación de unidad nacional, "
                "reconociendo el papel que tuvo la Revolución liberal, el "
                "Estado laico y la modernización.(I.2.)"
            ),
            codigo="I.CS.3.5.2.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Reconoce las condiciones de vida de los sectores populares "
                "durante el predominio plutocrático, la crisis política, los "
                "cambios en la vida cotidiana en la primera mitad del siglo "
                "XX y los procesos históricos entre 1925 a 1938. (J.1., "
                "J.3., I.2.)"
            ),
            codigo="I.CS.3.6.1.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Relaciona la guerra con el Perú, el “auge bananero” y las "
                "condiciones de vida de los sectores populares con el "
                "predominio de la oligarquía. (I.2.)"
            ),
            codigo="I.CS.3.6.2.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Reconoce el papel de la educación y de los derechos "
                "sociales y políticos en la prevalencia de transformaciones "
                "agrarias, procesos de industrialización, modernización, "
                "reformas religiosas y cambios tecnológicos. (J.1., I.2.)"
            ),
            codigo="I.CS.3.7.1.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Explica el surgimiento del “boom” petrolero ecuatoriano y "
                "su relación con el avance de la educación, el crecimiento "
                "poblacional, la migración interna, cambios sociales y "
                "políticos en la transición al régimen constitucional de "
                "fines de los años setenta e inicios de los años ochenta. "
                "(I.2.)"
            ),
            codigo="I.CS.3.7.2.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Discute los cambios surgidos a fines del siglo XX y "
                "comienzos del XXI con el predominio del neoliberalismo, los "
                "conflictos y transformaciones políticas y económicas, el "
                "papel de los movimientos sociales (indígenas, trabajadores, "
                "empresarios, mujeres, ecologistas), el papel del Ecuador en "
                "el panorama internacional, la promoción social, sus "
                "desafíos frente a la globalización, el Buen Vivir y la "
                "vigencia de la democracia y sus consecuencias en la "
                "sociedad actual. (J.1., I.2.)"
            ),
            codigo="I.CS.3.7.3.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Compara las décadas de 1960-1970 y 1970-1979, enfatizando "
                "el papel de las fuerzas armadas, los movimientos sociales y "
                "el papel del Estado en la vigencia de la democracia, la "
                "calidad de vida de los ecuatorianos y el Buen Vivir. (J.1., "
                "I.2.)"
            ),
            codigo="I.CS.3.7.4.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Describe el territorio del Ecuador, sus características "
                "geográficas (relieves, suelos y regiones naturales) que lo "
                "identifican como parte del espacio andino. (J.1., I.2.)"
            ),
            codigo="I.CS.3.8.1.",
            criterio_evaluacion=criterio3_8
        ),
        Indicador(
            description=(
                "Analiza la estructura geológica del Ecuador, su volcanismo "
                "activo y sus riesgos sísmicos, empleando mapas e imágenes "
                "satelitales. (J.1., J.3., I.1., I.2.)"
            ),
            codigo="I.CS.3.9.1.",
            criterio_evaluacion=criterio3_9
        ),
        Indicador(
            description=(
                "Describe la influencia de los recursos hídricos del Ecuador "
                "y del clima en la vida vegetal, animal y humana, mediante "
                "la interpretación de mapas e imágenes satelitales en "
                "función de reconocer posibles desastres. (J.1., J.3.,I.1., "
                "I.2.)"
            ),
            codigo="I.CS.3.9.2.",
            criterio_evaluacion=criterio3_9
        ),
        Indicador(
            description=(
                "Explica los orígenes de la diversidad poblacional del país, "
                "a partir del análisis de su evolución histórica, luchas por "
                "la liberación, ubicación geográfica, características "
                "culturales (vestimenta, costumbres, alimentación, "
                "festividades, actividades laborales) y la reconoce como "
                "riqueza y oportunidad para el desarrollo y crecimiento del "
                "país. (J.1., I.2.)"
            ),
            codigo="I.CS.3.10.1.",
            criterio_evaluacion=criterio3_10
        ),
        Indicador(
            description=(
                "Compara el crecimiento de la población del Ecuador con la "
                "de otros países, con criterios etarios, grupos vulnerables, "
                "étnicos, culturales y de localización en el territorio, y "
                "procesos de inmigración, acceso a educación, salud, empleo "
                "y servicios básicos, valorando la unidad nacional en la "
                "diversidad. (J.1., J.4., S.2.)"
            ),
            codigo="I.CS.3.10.2.",
            criterio_evaluacion=criterio3_10
        ),
        Indicador(
            description=(
                "Analiza las ventajas y desventajas de la organización "
                "territorial del país, las características de sus gobiernos "
                "(provinciales, municipales y parroquiales) y sus formas de "
                "participación popular, reconociendo las concordancias o "
                "inconsistencias entre la división natural y territorial "
                "existente en el país. (J.1., I.2.)"
            ),
            codigo="I.CS.3.11.1.",
            criterio_evaluacion=criterio3_11
        ),
        Indicador(
            description=(
                "Analiza los principales rasgos físicos de las provincias "
                "(relieves, hidrografía, climas, áreas cultivables, pisos "
                "ecológicos, etc.), mediante ejercicios gráficos, el uso de "
                "Internet y las redes sociales, destacando sus semejanzas y "
                "diferencias. (J.1., I.2.)"
            ),
            codigo="I.CS.3.11.2.",
            criterio_evaluacion=criterio3_11
        ),
        Indicador(
            description=(
                "Examina las áreas protegidas del país y lo relaciona con "
                "los efectos del calentamiento global y cambio climático, "
                "planteando actividades concretas para su protección y "
                "conservación. (J.3., S.1.)"
            ),
            codigo="I.CS.3.12.1.",
            criterio_evaluacion=criterio3_12
        ),
        Indicador(
            description=(
                "Reconoce al Ecuador como un país diverso, destacando el "
                "valor de sus bosques y desarrollando una cultura de respeto "
                "al ambiente. (J.3., S.1.)"
            ),
            codigo="I.CS.3.12.2.",
            criterio_evaluacion=criterio3_12
        ),
        Indicador(
            description=(
                "Examina la importancia de las organizaciones sociales, a "
                "partir del análisis de sus características, función social "
                "y transformaciones históricas, reconociendo el laicismo y "
                "el derecho a la libertad de cultos como un avance "
                "significativo para lograr una sociedad más justa y "
                "equitativa. (J.1.,J.3., S.1.)"
            ),
            codigo="I.CS.3.13.1.",
            criterio_evaluacion=criterio3_13
        ),
        Indicador(
            description=(
                "Analiza la participación de los miembros de la sociedad "
                "(mujeres, hombres, personas con discapacidad) en el marco "
                "de la diversidad e identifica las medidas y acciones "
                "concretas que posibilitan un trato más justo a las personas "
                "con discapacidad. (J.1., I.1.)"
            ),
            codigo="I.CS.3.13.2.",
            criterio_evaluacion=criterio3_13
        ),
        # Superior
        Indicador(
            description=(
                "Explica la importancia de la historia para la comprensión "
                "del origen de la humanidad, del trabajo como factor "
                "fundamental de la evolución y desarrollo de una sociedad, "
                "el papel de la mujer en la invención de la agricultura y la "
                "influencia de la agricultura y de la escritura en las "
                "formas de vida y organización social de los pueblos. (I.2.)"
            ),
            codigo="I.CS.4.1.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Analiza la evolución y relación entre el origen de los "
                "primeros pobladores de América, la formación de grandes "
                "civilizaciones, el desarrollo de las culturas andinas, el "
                "origen y desarrollo del Imperio inca y la estructura "
                "organizativa del Tahuantinsuyo, destacando el legado "
                "material y cultural indígena y los rasgos más "
                "significativos que diferencian las culturas americanas. "
                "(I.2.)"
            ),
            codigo="I.CS.4.1.2.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Compara los Imperios esclavistas de la Antigüedad en el "
                "Oriente Medio con el Imperio romano, los Imperios asiáticos "
                "(China e India), reconociendo que las estructuras de "
                "desigualdad son semejantes en diversos momentos históricos "
                "y el impacto del surgimiento del Islam en Arabia y su "
                "difusión al norte de África. (I.2.)"
            ),
            codigo="I.CS.4.2.1.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Examina las motivaciones de los europeos para buscar nuevas "
                "rutas marítimas, su llegada a la India y el "
                "“descubrimiento” de América, los mecanismos de gobierno y "
                "extracción de riquezas del Imperio colonial español en "
                "América, y su relación con las transformaciones en los "
                "siglos XVI y XVII de la América española, las innovaciones "
                "y progresos científicos y tecnológicos de los siglos "
                "posteriores, estableciendo semejanzas y diferencias de esta "
                "colonización con el portugués y anglosajón. (I.2.)"
            ),
            codigo="I.CS.4.2.2.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Examina los orígenes de la conciencia humanista y el "
                "cristianismo, y la influencia de las culturas mediterráneas "
                "en el pensamiento filosófico y democrático, como "
                "antecedente para la tolerancia y la diversidad religiosa. "
                "(I.2.)"
            ),
            codigo="I.CS.4.3.1.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Relaciona los cambios producidos en las cruzadas y el fin "
                "del medioevo con la transición a una sociedad feudal "
                "europea en función de potenciar el entendimiento de la "
                "diversidad religiosa. (J.3., I.2.)"
            ),
            codigo="I.CS.4.3.2.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Explica el avance del capitalismo, el crecimiento de la "
                "producción manufacturera, la independencia de los Estados "
                "Unidos y el sentido de las revoluciones europeas de fines "
                "del siglo XVIII y XIX, destacando la herencia de las "
                "sociedades coloniales en la América del presente. (I.2.)"
            ),
            codigo="I.CS.4.3.3.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Examina el impacto de la Revolución bolchevique, la Primera "
                "y Segunda Guerra Mundial, la Gran Depresión, la fundación "
                "de la República Popular China en la sociedad "
                "latinoamericana, destacando el papel de América Latina en "
                "la fundación de la Organización de las Naciones Unidas y la "
                "lucha por el respeto a los derechos humanos. (J.3., I.2.)"
            ),
            codigo="I.CS.4.4.1.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Compara el contenido de las luchas anticoloniales con la "
                "lucha por los derechos civiles, destacando la importancia "
                "de una cultura de paz y respeto a los derechos humanos. "
                "(J.3., I.2.)"
            ),
            codigo="I.CS.4.4.2.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Examina las causas y consecuencias de la movilización "
                "social e insurgencia en la América Latina de los años "
                "setenta, la Revolución cubana y las características de las "
                "dictaduras latinoamericanas, evaluando la importancia de "
                "una cultura de paz y respeto a los derechos humanos.(J.3.)"
            ),
            codigo="I.CS.4.4.3.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Analiza la Ilustración europea y latinoamericana como "
                "antecedente de los procesos de independencia, destacando "
                "sus causas, limitaciones, el papel de los "
                "afrodescendientes, y las características y limitaciones de "
                "los Estados nacionales latinoamericanos.(J.1., J.2., J.3.)"
            ),
            codigo="I.CS.4.5.1.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Examina el proyecto integracionista bolivariano, en el "
                "contexto del desarrollo del capitalismo, destacando el "
                "valor de la independencia y la libertad para las naciones "
                "en el presente, los avances científicos y técnicos que "
                "posibilitaron el gran auge de la industria y los cambios "
                "socioeconómicos a inicios del desarrollismo. (J.1., I.1.)"
            ),
            codigo="I.CS.4.5.2.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Compara la trayectoria de América Latina en los siglos XIX "
                "y XX, considerando su incorporación en el mercado mundial, "
                "expansión de la industria, sistemas constitucionales, "
                "conflictos por la definición de fronteras, cambios "
                "socioeconómicos e inicios del desarrollismo, implantación e "
                "influencia en la situación económica y social bajo el "
                "neoliberalismo y desafíos en cuanto al manejo de "
                "información y medios de comunicación. (I.2.)"
            ),
            codigo="I.CS.4.5.3.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Explica el proceso formativo de la Tierra, la gestación de "
                "los continentes y sus características generales, las eras "
                "geológicas, océanos, mares, movimientos y climas, y su "
                "impacto en posibles desastres naturales y planes de "
                "contingencia en los ámbitos geográfico, demográfico y "
                "económico. (I.1., I.2.)"
            ),
            codigo="I.CS.4.6.1.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Aplica diversos instrumentos y recursos cartográficos para "
                "describir las características fundamentales de África, "
                "Europa, Asia y Oceanía (relieves, hidrografía, climas, "
                "demografía y principales indicadores de vida). (I.1., I.2.)"
            ),
            codigo="I.CS.4.6.2.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Explica las características fundamentales de América del "
                "Norte, Central, del Caribe y del Sur, destacando algunos "
                "rasgos geográficos más relevantes relacionados con la "
                "economía, la demografía y calidad de vida. (I.1.,I.2.)"
            ),
            codigo="I.CS.4.6.3.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Examina la interrelación entre lugares, personas y "
                "productos involucrados en el sector primario, secundario y "
                "de servicios destacando sus fortalezas, oportunidades, "
                "debilidades y amenazas y el impacto económico y social en "
                "los recursos naturales. (J.4., I.1.)"
            ),
            codigo="I.CS.4.7.1.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Explica el papel que tiene el sector financiero, el sector "
                "servicios y el Estado en la economía del país, "
                "identificando sus efectos en la vida de las personas y "
                "principales problemas económicos. (J.1., S.1.)"
            ),
            codigo="I.CS.4.7.2.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Discute el concepto de “desarrollo” en contraste con el de "
                "Buen Vivir, destacando sus implicaciones sobre el respeto a "
                "los derechos fundamentales (educación y salud) y demandas "
                "sociales (vivienda, transporte, empleo y seguridad social) "
                "que existen en el país. (J.1., J.4., I.2.)"
            ),
            codigo="I.CS.4.8.1.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Relaciona los objetivos del Buen Vivir con las actividades "
                "recreativas, opciones de ocio y el deporte. (J.1., S.1., "
                "S.3.)"
            ),
            codigo="I.CS.4.8.2.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Analiza las causas, consecuencias y el papel que ha tenido "
                "la migración en América Latina, reconociendo la diversidad "
                "cultural y humana como resultado de este proceso, "
                "destacando el rol de los jóvenes en la integración Andina y "
                "sudamericana, y el impacto que esta y la globalización "
                "tienen en la sociedad ecuatoriana. (I.2., S.1.)"
            ),
            codigo="I.CS.4.9.1.",
            criterio_evaluacion=criterio4_9
        ),
        Indicador(
            description=(
                "Diferencia la población mundial en función de su sexo, edad "
                "y distribución en los continentes, reconociendo los "
                "procesos de integración internacional que se dan en el "
                "mundo. (I.1., I.2.)"
            ),
            codigo="I.CS.4.9.2.",
            criterio_evaluacion=criterio4_9
        ),
        Indicador(
            description=(
                "Discute las causas y consecuencias de la pobreza en el país "
                "y América Latina, destacando la concentración de la "
                "riqueza, las guerras, los conflictos mundiales, la doble "
                "ciudadanía y el tráfico de personas y de drogas como "
                "problemas que afectan a la población mundial. (J.1., I.2.)"
            ),
            codigo="I.CS.4.9.3.",
            criterio_evaluacion=criterio4_9
        ),
        Indicador(
            description=(
                "Explica la interculturalidad desde el análisis de las "
                "diferentes manifestaciones culturales del Ecuador (nacional "
                "y popular), sus raíces históricas u origen, localización, "
                "rasgos más destacados, y las acciones concretas para "
                "practicarla en espacios cercanos, y reconoce sus "
                "diferencias con la “cultura de masas”. (J.1., S.2.)"
            ),
            codigo="I.CS.4.10.1.",
            criterio_evaluacion=criterio4_10
        ),
        Indicador(
            description=(
                "Discute la relación entre democracia y libertad de "
                "expresión, medios de comunicación, valores democráticos "
                "(libertad, equidad y solidaridad) y gobierno del pueblo, "
                "reconociendo el papel de la Constitución como garante de "
                "los derechos ciudadanos y la lucha por los derechos "
                "humanos. (J.1., J.2., J.3.)"
            ),
            codigo="I.CS.4.10.2.",
            criterio_evaluacion=criterio4_10
        ),
        Indicador(
            description=(
                "Relaciona el ejercicio de la ciudadanía ecuatoriana con el "
                "Estado, la Constitución, la participación ciudadana "
                "(canales y formas) y los procesos de integración (regional "
                "e internacional), en un contexto de interculturalidad, "
                "unidad nacional y globalización. (J.1., J.3., I.1.)"
            ),
            codigo="I.CS.4.11.1.",
            criterio_evaluacion=criterio4_11
        ),
        Indicador(
            description=(
                "Analiza los mecanismos que tiene el Estado, la fuerza "
                "pública y los ciudadanos para el cumplimiento de su papel "
                "como garantes y veedores de los derechos humanos, en un "
                "contexto de interculturalidad, unidad nacional y "
                "globalización. (J.1., S.1.)"
            ),
            codigo="I.CS.4.11.2.",
            criterio_evaluacion=criterio4_11
        ),
        Indicador(
            description=(
                "Distingue las semejanzas y diferencias entre los derechos "
                "fundamentales estipulados en el Código de la Niñez y "
                "Adolescencia y los derechos humanos, reconociendo que los "
                "derechos implican deberes y responsabilidades. (J.1., J.3.)"
            ),
            codigo="I.CS.4.11.3.",
            criterio_evaluacion=criterio4_11
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0053_auto_20180903_1342'),
    ]

    operations = [
        migrations.RunPython(create_indicadores)
    ]
