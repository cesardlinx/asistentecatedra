from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    historia = Asignatura.objects.get(name='Historia')
    educacion_ciudadania = Asignatura.objects.get(
        name='Educación para la Ciudadanía')
    filosofia = Asignatura.objects.get(name='Filosofía')

    # Bloques Historia
    bloque1_historia = BloqueCurricular.objects.get(
        name="Los orígenes y las primeras culturas de la humanidad"
    )
    bloque2_historia = BloqueCurricular.objects.get(
        name="De la Edad Media a la Modernidad"
    )
    bloque3_historia = BloqueCurricular.objects.get(
        name="América latina: mestizaje y liberación"
    )
    bloque4_historia = BloqueCurricular.objects.get(
        name="Economía: trabajo y sociedad"
    )

    # Bloques Educación para la ciudadanía
    bloque1_ciudadania = BloqueCurricular.objects.get(
        name="Ciudadanía y derechos")
    bloque2_ciudadania = BloqueCurricular.objects.get(
        name="La democracia moderna"
    )
    bloque3_ciudadania = BloqueCurricular.objects.get(
        name="La democracia y la construcción de un Estado plurinacional"
    )
    bloque4_ciudadania = BloqueCurricular.objects.get(
        name="El Estado y su organización"
    )

    # Bloques Filosofía
    bloque1_filosofia = BloqueCurricular.objects.get(
        name=("El orígen del pensamiento filosófico y su relación con la "
              "ciudadanía")
    )
    bloque2_filosofia = BloqueCurricular.objects.get(
        name=("La argumentación y la construcción del discurso lógico, oral "
              "y escrito")
    )
    bloque3_filosofia = BloqueCurricular.objects.get(
        name="Filosofía occidental y filosofía latinoamericana"
    )
    bloque4_filosofia = BloqueCurricular.objects.get(
        name="El individuo y la comunidad: lo ético, lo estético, lo hedónico"
    )

    # Subnivel
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Historia
        # Bloque 1
        Destreza(
            description=(
                "Contrastar los conceptos de historia e historiografía con "
                "el fin de diferenciar la realidad de la construcción "
                "intelectual."
            ),
            codigo="CS.H.5.1.1.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Examinar el término “cultura” como producción material y "
                "simbólica y ejemplificar con aspectos de la vida cotidiana."
            ),
            codigo="CS.H.5.1.2.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Explicar y valorar la importancia del trabajo colectivo y "
                "solidario como condición de la existencia y supervivencia "
                "humana."
            ),
            codigo="CS.H.5.1.3.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar y comprender los contenidos y las formas de la "
                "educación en la comunidad primitiva (qué se enseñaba y cómo "
                "se enseñaba)."
            ),
            codigo="CS.H.5.1.4.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Utilizar diversas fuentes y relativizar los diversos "
                "enfoques en relación con problemas determinados."
            ),
            codigo="CS.H.5.1.5.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Aplicar técnica y éticamente las diversas fuentes en una "
                "investigación."
            ),
            codigo="CS.H.5.1.6.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Explicar y valorar la función del trabajo humano en la "
                "construcción de la historia y la cultura."
            ),
            codigo="CS.H.5.1.7.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Describir y evaluar la influencia de la elaboración de "
                "herramientas en la transformación biológica y social del "
                "ser humano."
            ),
            codigo="CS.H.5.1.8.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Relacionar e interpretar las características esenciales del "
                "Paleolítico y la producción del arte rupestre."
            ),
            codigo="CS.H.5.1.9.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Identificar las materias primas y explicar su relación con "
                "el tipo de utensilios y herramientas que se confeccionaban."
            ),
            codigo="CS.H.5.1.10.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Determinar el impacto de la revolución neolítica "
                "(domesticación de plantas y animales y sedentarismo) en la "
                "transformación de la sociedad humana."
            ),
            codigo="CS.H.5.1.11.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar el proceso de división del trabajo y la producción "
                "y apropiación de excedentes."
            ),
            codigo="CS.H.5.1.12.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Investigar los posibles orígenes de la propiedad privada "
                "sobre los medios de producción y su justificación "
                "ideológica."
            ),
            codigo="CS.H.5.1.13.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar y evaluar el rol y prestigio de la mujer en la "
                "comunidad primitiva a partir de su función productiva, "
                "social y cultural."
            ),
            codigo="CS.H.5.1.14.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Determinar las causas de la crisis de la comunidad "
                "matriarcal y la irrupción del dominio patriarcal en el "
                "desarrollo de la humanidad (machismo)."
            ),
            codigo="CS.H.5.1.15.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Describir y valorar los grandes aportes de las culturas de "
                "Mesopotamia al desarrollo tecnológico, económico y "
                "científico desde la perspectiva de su condición de “cuna de "
                "la humanidad”."
            ),
            codigo="CS.H.5.1.16.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Describir y valorar los grandes aportes de la cultura china "
                "al desarrollo tecnológico, económico y científico de la "
                "humanidad."
            ),
            codigo="CS.H.5.1.17.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Describir y valorar los grandes aportes de la cultura de la "
                "India al desarrollo tecnológico, económico y científico."
            ),
            codigo="CS.H.5.1.18.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar y evaluar la existencia y la división de castas en "
                "la sociedad hindú."
            ),
            codigo="CS.H.5.1.19.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Describir y valorar los grandes aportes de la cultura "
                "egipcia al desarrollo tecnológico, económico y científico."
            ),
            codigo="CS.H.5.1.20.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Identificar y evaluar los aportes de las grandes culturas "
                "de la Antigüedad que han marcado significativamente la "
                "fisonomía del mundo contemporáneo."
            ),
            codigo="CS.H.5.1.21.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Investigar y valorar el rol de la mujer en la sociedad del "
                "Medio Oriente en comparación con la situación "
                "contemporánea."
            ),
            codigo="CS.H.5.1.22.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar y discutir el concepto de “yihad” en la cultura "
                "islámica a la luz del análisis de diversas fuentes."
            ),
            codigo="CS.H.5.1.23.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Reconocer la influencia de los griegos, sobre todo en el "
                "Imperio romano, en el Imperio bizantino y, casi dos mil "
                "años después, en la Europa del Renacimiento."
            ),
            codigo="CS.H.5.1.24.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Valorar la influencia del pensamiento griego en la cultura "
                "occidental, mediante el reconocimiento del carácter "
                "racional que lo distinguió."
            ),
            codigo="CS.H.5.1.25.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Distinguir y explicar las limitaciones de la democracia y "
                "de la ciudadanía en la civilización griega."
            ),
            codigo="CS.H.5.1.26.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Investigar y valorar los aportes de la mujer griega desde "
                "diversos ámbitos de participación: Safo de Lesbos, Aspasia "
                "de Mileto e Hipatia."
            ),
            codigo="CS.H.5.1.27.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Diferenciar e interpretar el rol distinto de la mujer en "
                "Atenas y en Esparta, en la perspectiva de relativizar su "
                "protagonismo social."
            ),
            codigo="CS.H.5.1.28.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Comprender las causas y los principales problemas de la "
                "expansión imperial romana."
            ),
            codigo="CS.H.5.1.29.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar las contribuciones del derecho romano al sistema "
                "jurídico ecuatoriano diferenciándolo del Common Law o "
                "derecho anglosajón."
            ),
            codigo="CS.H.5.1.30.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Analizar y comparar los roles de la mujer de los diferentes "
                "estratos sociales en la Roma antigua."
            ),
            codigo="CS.H.5.1.31.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Determinar los elementos del judaísmo que influyeron en la "
                "conformación de la cultura occidental mediante un análisis "
                "del monoteísmo y la concepción lineal del tiempo."
            ),
            codigo="CS.H.5.1.32.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        Destreza(
            description=(
                "Investigar los posibles antecedentes históricos del "
                "conflicto entre judíos y palestinos."
            ),
            codigo="CS.H.5.1.33.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque1_historia
        ),
        # Bloque 2
        Destreza(
            description=(
                "Determinar las causas y consecuencias de la decadencia y "
                "caída del Imperio romano."
            ),
            codigo="CS.H.5.2.1.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Caracterizar y diferenciar el Imperio romano de Occidente "
                "del Imperio romano de Oriente en el arte y la cultura."
            ),
            codigo="CS.H.5.2.2.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Analizar y valorar la importancia y trascendencia del "
                "Imperio bizantino en la cultura, la religión y la "
                "legislación a lo largo de la Edad Media."
            ),
            codigo="CS.H.5.2.3.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Examinar y relacionar los procesos de expansión del "
                "cristianismo y del islamismo y los conflictos motivados por "
                "ellos."
            ),
            codigo="CS.H.5.2.4.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Analizar la influencia y los cambios que introdujo el "
                "cristianismo y el islamismo en la vida cotidiana."
            ),
            codigo="CS.H.5.2.5.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Analizar y valorar el rol de la mujer desde la perspectiva "
                "del pensamiento judeocristiano."
            ),
            codigo="CS.H.5.2.6.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Reconocer las motivaciones económicas de las cruzadas en la "
                "Edad Media en el contexto de las luchas religiosas."
            ),
            codigo="CS.H.5.2.7.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Analizar el papel e influencia del Tribunal de la "
                "Inquisición en la persecución de la ciencia y la caza de "
                "“brujas”."
            ),
            codigo="CS.H.5.2.8.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Comprender el intento del Imperio carolingio de recuperar "
                "los ámbitos político, religioso y cultural de la época "
                "medieval considerando su legado a la conformación del Sacro "
                "Imperio Romano Germánico."
            ),
            codigo="CS.H.5.2.9.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Explicar el contexto en el que surgieron las primeras "
                "universidades europeas, y el papel que desempeñó la Iglesia "
                "en la trasmisión de la cultura."
            ),
            codigo="CS.H.5.2.10.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Identificar los principales aportes culturales del "
                "medioevo, destacando las contribuciones de la arquitectura, "
                "pintura y escultura."
            ),
            codigo="CS.H.5.2.11.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Distinguir e interpretar las principales características "
                "del arte arquitectónico románico y gótico en función de su "
                "simbología social."
            ),
            codigo="CS.H.5.2.12.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Determinar y comprender el origen y los principios "
                "fundamentales del Islam."
            ),
            codigo="CS.H.5.2.13.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Describir y evaluar la influencia cultural del Islam en la "
                "península Ibérica durante la Edad Media y su traslado a "
                "América con la conquista española."
            ),
            codigo="CS.H.5.2.14.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Sintetizar la expansión del Islam entre los siglos VII y "
                "VIII desde la península Ibérica en occidente hasta la India "
                "en oriente."
            ),
            codigo="CS.H.5.2.15.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Describir y analizar las principales contribuciones de la "
                "civilización árabe al arte y la cultura."
            ),
            codigo="CS.H.5.2.16.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Investigar y contrastar en fuentes diversas la situación y "
                "el rol de la mujer dentro de las sociedades islámicas."
            ),
            codigo="CS.H.5.2.17.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Argumentar los esenciales principios comunes del judaísmo, "
                "el cristianismo y el islamismo y sus diferencias "
                "fundamentales."
            ),
            codigo="CS.H.5.2.18.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Identificar las condiciones de surgimiento del Renacimiento "
                "y de la nueva visión del ser humano, el Humanismo."
            ),
            codigo="CS.H.5.2.19.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Describir y explicar los principales aportes del "
                "Renacimiento a las humanidades y las ciencias."
            ),
            codigo="CS.H.5.2.20.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Distinguir las causas y consecuencias de la Reforma y sus "
                "principales respuestas al cisma religioso de Occidente."
            ),
            codigo="CS.H.5.2.21.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Analizar la Contrarreforma y las diferentes estrategias que "
                "utilizó la Iglesia católica para combatir la Reforma "
                "Protestante."
            ),
            codigo="CS.H.5.2.22.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Reconocer la Ilustración como base intelectual de la "
                "modernidad, sus principales representantes y postulados."
            ),
            codigo="CS.H.5.2.23.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Establecer relaciones entre el humanismo renacentista y el "
                "pensamiento ilustrado a partir de su visión racional y "
                "antropocéntrica."
            ),
            codigo="CS.H.5.2.24.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Argumentar sobre las principales causas y consecuencias de "
                "la Revolución francesa y la vigencia de sus postulados "
                "principales hasta el presente."
            ),
            codigo="CS.H.5.2.25.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Determinar los alcances y las limitaciones del proyecto "
                "napoleónico en función de la expansión de los principios de "
                "la Revolución francesa."
            ),
            codigo="CS.H.5.2.26.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Identificar y comprender el origen del movimiento obrero a "
                "partir de las revoluciones industriales y el surgimiento "
                "del pensamiento socialista."
            ),
            codigo="CS.H.5.2.27.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Identificar y contextualizar las reivindicaciones de los "
                "movimientos de mujeres e indígenas para comprender las "
                "razones de su invisibilización y exclusión milenaria."
            ),
            codigo="CS.H.5.2.28.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Indagar la biografía y el protagonismo sociopolítico de "
                "Dolores Cacuango, Tránsito Amaguaña y Rigoberta Menchú en "
                "los procesos de liberación de Ecuador y América Latina."
            ),
            codigo="CS.H.5.2.29.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Identificar y contextualizar las reivindicaciones de los "
                "movimientos ecologista y ecofeminista a partir de la "
                "crítica a la visión mercantilista de la Madre Tierra "
                "(Pachamama)."
            ),
            codigo="CS.H.5.2.30.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Examinar y valorar las propuestas de los movimientos "
                "ecologistas frente al modelo capitalista de producción."
            ),
            codigo="CS.H.5.2.31.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Distinguir e interpretar los principales movimientos "
                "artísticos contemporáneos como expresiones subjetivas de "
                "respuesta frente al poder y los conflictos sociales."
            ),
            codigo="CS.H.5.2.32.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Analizar y comprender el papel y la importancia de los "
                "medios de comunicación impresos y audiovisuales en la "
                "producción y la reproducción de las relaciones de poder."
            ),
            codigo="CS.H.5.2.33.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        Destreza(
            description=(
                "Identificar y valorar las diversas expresiones del arte "
                "popular en sus múltiples manifestaciones: regionales, "
                "provinciales, urbanas, rurales, etc."
            ),
            codigo="CS.H.5.2.34.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque2_historia
        ),
        # Bloque 3
        Destreza(
            description=(
                "Identificar y valorar las producciones intelectuales más "
                "significativas de las culturas aborígenes de América Latina "
                "precolombina (mayas, aztecas e incas)."
            ),
            codigo="CS.H.5.3.1.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Explicar las diversas formas de vida y de organización "
                "social de las grandes culturas nativas de América aborigen "
                "en función de valorar su capacidad de innovación y "
                "creatividad."
            ),
            codigo="CS.H.5.3.2.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Valorar la experticia en el diseño, organización y "
                "funciones de las edificaciones precolombinas en relación "
                "con su entorno geográfico y cultural."
            ),
            codigo="CS.H.5.3.3.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Establecer la vinculación entre la arquitectura y la "
                "astronomía a partir del análisis de las edificaciones "
                "arquitectónicas."
            ),
            codigo="CS.H.5.3.4.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Comparar los diseños y funciones arquitectónicas de mayas, "
                "aztecas e incas para valorar su creatividad y destrezas "
                "tecnológicas."
            ),
            codigo="CS.H.5.3.5.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Sintetizar los principios de organización e intercambio "
                "social (reciprocidad y redistribución) de los pobladores "
                "nativos de los Andes, en función de la equidad y la "
                "justicia social."
            ),
            codigo="CS.H.5.3.6.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Comprender la diversidad productiva en el “archipiélago de "
                "pisos ecológicos” en relación con el respeto a los ciclos "
                "vitales de la naturaleza."
            ),
            codigo="CS.H.5.3.7.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Explicar las razones de la distribución poblacional "
                "dispersa en la geografía andina a partir de la relación con "
                "el modelo productivo."
            ),
            codigo="CS.H.5.3.8.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Describir y valorar las destrezas arquitectónicas incaicas "
                "en la construcción de edificaciones, caminos y canales de "
                "riego, muchos de los cuales permanecen hasta el presente."
            ),
            codigo="CS.H.5.3.9.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Examinar el impacto de la Conquista a través del estudio de "
                "la implementación de relaciones de explotación y "
                "sometimiento de la población aborigen."
            ),
            codigo="CS.H.5.3.10.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar el impacto ecológico y el cambio en los hábitos "
                "culturales y sociales de la población indígena a partir de "
                "la introducción de especies animales y vegetales foráneas."
            ),
            codigo="CS.H.5.3.11.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar y comprender las causas y consecuencias del "
                "proceso de evangelización y “extirpación de idolatrías” en "
                "el mundo indígena."
            ),
            codigo="CS.H.5.3.12.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Establecer las razones de las diferentes formas de "
                "extracción de riqueza por parte de los conquistadores "
                "españoles."
            ),
            codigo="CS.H.5.3.13.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Explicar el nuevo papel que se le asignó a la mita andina "
                "como forma de distribución de la fuerza de trabajo en la "
                "economía colonial."
            ),
            codigo="CS.H.5.3.14.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar y evaluar las razones por las cuales se decide "
                "traer personas esclavizadas a América Latina."
            ),
            codigo="CS.H.5.3.15.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Examinar y valorar los elementos culturales africanos que "
                "se integraron al mundo latinoamericano (música, danza, "
                "religión) sobre todo en República Dominicana, Brasil, "
                "Panamá, Perú, Venezuela, Ecuador, Colombia y Cuba."
            ),
            codigo="CS.H.5.3.16.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Explicar los antecedentes históricos de la comunidad "
                "afrodescendiente de Esmeraldas y de El Chota y sus formas "
                "de expresión cultural."
            ),
            codigo="CS.H.5.3.17.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Identificar y evaluar el protagonismo de las potencias "
                "involucradas en el tráfico de personas esclavizadas a "
                "América Latina."
            ),
            codigo="CS.H.5.3.18.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Sintetizar el proceso de colonización portugués en Brasil "
                "desde el “descubrimiento” hasta 1530."
            ),
            codigo="CS.H.5.3.19.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar y diferenciar cada uno de los ciclos económicos: "
                "de “descubrimiento”, de la caña de azúcar y del oro."
            ),
            codigo="CS.H.5.3.20.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Examinar la economía latifundista y su relación con la mano "
                "de obra esclava."
            ),
            codigo="CS.H.5.3.21.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar quiénes eran los “bandeirantes” y el rol que "
                "jugaron en el tráfico de personas esclavizadas."
            ),
            codigo="CS.H.5.3.22.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Contrastar los procesos de colonización hispánico, "
                "portugués y anglosajón, y establecer sus semejanzas y "
                "diferencias."
            ),
            codigo="CS.H.5.3.23.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar y valorar las características del mestizaje y el "
                "sincretismo en el arte colonial hispanoamericano."
            ),
            codigo="CS.H.5.3.24.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Comprender la función evangelizadora que cumplía el arte "
                "colonial por medio de la pintura, la escultura y la "
                "arquitectura."
            ),
            codigo="CS.H.5.3.25.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Establecer las características y la función social del arte "
                "barroco y el arte mudéjar y sus diferencias."
            ),
            codigo="CS.H.5.3.26.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar y explicar la función de los conventos y las "
                "misiones dentro del proceso de consolidación y expansión "
                "religiosa de la Colonia."
            ),
            codigo="CS.H.5.3.27.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar y comparar la situación y los roles de la mujer de "
                "los diversos estratos sociales en la Colonia."
            ),
            codigo="CS.H.5.3.28.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar la vinculación de las instituciones educativas a "
                "las órdenes religiosas y los niveles de acceso de los "
                "distintos estamentos sociales."
            ),
            codigo="CS.H.5.3.29.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar y contextualizar el origen y función de la "
                "hacienda y la plantación en la economía colonial en "
                "relación con el mercado interno y externo."
            ),
            codigo="CS.H.5.3.30.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Establecer las semejanzas y diferencias entre la hacienda y "
                "la plantación, considerando los factores fundamentales de "
                "producción."
            ),
            codigo="CS.H.5.3.31.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Conceptualizar los términos casta, clase y estamento con el "
                "fin de comprender los procesos de lucha y movilidad social."
            ),
            codigo="CS.H.5.3.32.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Identificar y diferenciar los distintos estamentos, castas "
                "y clases existentes en la Colonia."
            ),
            codigo="CS.H.5.3.33.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar y valorar las motivaciones y repercusiones de las "
                "principales sublevaciones indígenas en el siglo XVIII."
            ),
            codigo="CS.H.5.3.34.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Investigar la biografía y protagonismo de Julián Apaza Nina "
                "(Túpac Katari), José Gabriel Condorcanqui Noguera (Túpac "
                "Amaru II) y Fernando Daquilema en las respectivas "
                "sublevaciones que lideraron."
            ),
            codigo="CS.H.5.3.35.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar la contradicción entre los procesos de "
                "independencia política y la dependencia económica de "
                "Latinoamérica como proveedor de materias primas al mercado "
                "internacional."
            ),
            codigo="CS.H.5.3.36.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Comprender y evaluar el proyecto político republicano "
                "criollo sobre una base social excluyente de indígenas y "
                "afrodescendientes."
            ),
            codigo="CS.H.5.3.37.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Identificar y comprender las diversas oleadas migratorias a "
                "América Latina, su procedencia y sus aportes al desarrollo "
                "económico y cultural de la región."
            ),
            codigo="CS.H.5.3.38.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Comprender y evaluar las revoluciones liberales y los "
                "alcances y limitaciones de sus proyectos nacionales."
            ),
            codigo="CS.H.5.3.39.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar la Revolución mexicana desde sus protagonistas "
                "individuales y colectivos, sus motivaciones y principales "
                "propuestas de cambio."
            ),
            codigo="CS.H.5.3.40.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar las posibles razones por las cuales Francisco "
                "Villa y Emiliano Zapata carecieron de un sólido proyecto "
                "político."
            ),
            codigo="CS.H.5.3.41.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar la influencia de la Revolución mexicana en "
                "posteriores movimientos de liberación en América Latina "
                "(Tupamaros, EZLN, FARC, ELN, Sendero Luminoso)."
            ),
            codigo="CS.H.5.3.42.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar las causas y repercusiones de la Gran Depresión en "
                "la economía latinoamericana y ecuatoriana."
            ),
            codigo="CS.H.5.3.43.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Identificar el contexto en el que surge la Comisión "
                "Económica para América Latina (CEPAL) y evaluar sus "
                "propuestas para la región."
            ),
            codigo="CS.H.5.3.44.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Identificar y evaluar las motivaciones del proceso "
                "revolucionario cubano y sus repercusiones en América "
                "Latina."
            ),
            codigo="CS.H.5.3.45.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Examinar los principales logros y limitaciones de la "
                "Revolución cubana dentro del contexto del embargo económico "
                "norteamericano."
            ),
            codigo="CS.H.5.3.46.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Resumir las biografías de Ernesto Guevara de la Serna y "
                "Fidel Castro Ruz y analizar su controvertido liderazgo "
                "revolucionario."
            ),
            codigo="CS.H.5.3.47.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Determinar la relación entre el auge petrolero, el "
                "endeudamiento externo ecuatoriano y su posterior crisis."
            ),
            codigo="CS.H.5.3.48.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Explicar las consecuencias del feriado bancario y la "
                "dolarización en la economía del país, empleando diferentes "
                "fuentes."
            ),
            codigo="CS.H.5.3.49.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Describir y explicar el proceso de migración de los años "
                "noventa a partir de una experiencia personal cercana y su "
                "relación con la crisis económica del país."
            ),
            codigo="CS.H.5.3.50.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Analizar el proyecto de la “Revolución Ciudadana” (R.C.) en "
                "el contexto de la crisis de los partidos políticos "
                "tradicionales y de la caída de los gobiernos de Abdalá "
                "Bucaram Ortiz, Jamil Mahuad Witt y Lucio Gutiérrez Borbúa."
            ),
            codigo="CS.H.5.3.51.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Discutir el impacto del proyecto político actual en el área "
                "social y económica de los ciudadanos."
            ),
            codigo="CS.H.5.3.52.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        Destreza(
            description=(
                "Contrastar la situación política actual del país con la de "
                "gobiernos anteriores, analizando las propuestas de "
                "educación, salud y vivienda de distintos regímenes."
            ),
            codigo="CS.H.5.3.53.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque3_historia
        ),
        # Bloque 4
        Destreza(
            description=(
                "Examinar el modo de producción que primó en el Paleolítico, "
                "destacando las relaciones sociales y las herramientas que "
                "utilizaban para la recolección, la caza y la pesca."
            ),
            codigo="CS.H.5.4.1.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar los cambios que generó la revolución neolítica, "
                "con la domesticación de plantas y animales en la producción "
                "de excedentes y la división y especialización del trabajo."
            ),
            codigo="CS.H.5.4.2.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Determinar las circunstancias que marcaron la transición de "
                "la comunidad primitiva a la sociedad dividida en clases "
                "(esclavismo)."
            ),
            codigo="CS.H.5.4.3.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar las circunstancias económicas por las que el ser "
                "humano es convertido en cosa o mercancía, en propiedad de "
                "otra persona."
            ),
            codigo="CS.H.5.4.4.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Comparar sociedades esclavistas del Viejo Mundo con formas "
                "modernas de esclavitud, en función de determinar la "
                "existencia de condiciones que permiten todavía esta forma "
                "de explotación humana."
            ),
            codigo="CS.H.5.4.5.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Distinguir las razones que determinaron la transición del "
                "esclavismo al feudalismo después de la caída del Imperio "
                "romano."
            ),
            codigo="CS.H.5.4.6.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Sintetizar las características del feudalismo, el sistema "
                "económico, social y político de Europa de la Edad Media, "
                "enfocándose en la estructura de la sociedad."
            ),
            codigo="CS.H.5.4.7.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Discutir las características de producción agrícola, minera "
                "y manufacturera en la América precolombina, desde el "
                "análisis de sus condiciones propias de evolución histórica."
            ),
            codigo="CS.H.5.4.8.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Interpretar el proceso de configuración del mercantilismo "
                "en Europa, destacando las consecuencias que tuvo en la "
                "conquista y colonización de América y su relación con el "
                "origen del capitalismo."
            ),
            codigo="CS.H.5.4.9.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Examinar el proceso de acumulación originaria de capital en "
                "el contexto de la “economía triangular” (manufacturas, "
                "personas esclavizadas y materias primas / Europa – África y "
                "América)."
            ),
            codigo="CS.H.5.4.10.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Describir elementos de diversas teorías y sistemas "
                "económicos adoptados en la América colonial, considerando "
                "sus similitudes y diferencias con las características del "
                "esclavismo, el feudalismo y el mercantilismo."
            ),
            codigo="CS.H.5.4.11.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Construir interpretaciones sobre el sistema económico que "
                "introdujo España en la América colonial."
            ),
            codigo="CS.H.5.4.12.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Sintetizar el origen, desarrollo y características de las "
                "primeras etapas del sistema capitalista."
            ),
            codigo="CS.H.5.4.13.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Caracterizar la fase imperialista del capitalismo a través "
                "del análisis del predominio supraestatal de las empresas "
                "transnacionales a nivel planetario."
            ),
            codigo="CS.H.5.4.14.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar las características principales que definen al "
                "liberalismo, desde el punto de vista de la Economía y la "
                "Política."
            ),
            codigo="CS.H.5.4.15.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Identificar y diferenciar la Primera y Segunda Revolución "
                "Industrial tomando en cuenta las fuentes de energía, la "
                "tecnificación, la mecanización de la fuerza de trabajo y el "
                "impacto en el medio ambiente."
            ),
            codigo="CS.H.5.4.16.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Examinar la “Tercera Revolución Industrial” fundamentada en "
                "las TIC, la cibernética y la robótica y su impacto en la "
                "sociedad y la naturaleza."
            ),
            codigo="CS.H.5.4.17.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar los procesos revolucionarios liberales más "
                "importantes (Independencia de los EE.UU., Revolución "
                "francesa e independencias hispanoamericanas) tomando en "
                "cuenta sus proyectos económicos."
            ),
            codigo="CS.H.5.4.18.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Conceptualizar los términos proteccionismo y librecambismo "
                "desde la Economía Política y sus principales "
                "representantes."
            ),
            codigo="CS.H.5.4.19.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Contextualizar el momento histórico en que se posiciona el "
                "debate entre proteccionismo y librecambismo."
            ),
            codigo="CS.H.5.4.20.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Distinguir las principales características del socialismo "
                "como sistema económico, tomando en cuenta los elementos que "
                "lo definen y diferentes enfoques para abordarlo: socialismo "
                "utópico y marxismo."
            ),
            codigo="CS.H.5.4.21.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Determinar el contexto histórico de aparecimiento de las "
                "ideas socialistas y su influencia en los procesos sociales "
                "de los siglos XIX y XX."
            ),
            codigo="CS.H.5.4.22.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Identificar las tres grandes revoluciones socialistas del "
                "siglo XX (Rusia, China y Cuba) y establecer sus "
                "características específicas."
            ),
            codigo="CS.H.5.4.23.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Argumentar el protagonismo de América Latina en el contexto "
                "de la Guerra Fría y su actitud frente a los EE.UU. y la "
                "URSS."
            ),
            codigo="CS.H.5.4.24.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Identificar las causas y consecuencias económicas y "
                "políticas de la caída del socialismo soviético, destacando "
                "el papel que cumplió la Perestroika en la Unión Soviética."
            ),
            codigo="CS.H.5.4.25.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Discutir las reformas políticas y económicas en la "
                "República Popular China con base en los modelos y teorías "
                "estudiados."
            ),
            codigo="CS.H.5.4.26.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Contextualizar el origen del neoliberalismo y su "
                "implementación en América Latina y el Ecuador."
            ),
            codigo="CS.H.5.4.27.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Determinar las principales políticas o medidas económicas "
                "implementadas en América Latina desde la perspectiva del "
                "neoliberalismo."
            ),
            codigo="CS.H.5.4.28.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar las causas de la crisis de los años ochenta y las "
                "medidas económicas aplicadas para resolverlas en América "
                "Latina y el Ecuador."
            ),
            codigo="CS.H.5.4.29.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Explicar el significado de la globalización en el contexto "
                "del conflicto entre la homogenización y la defensa de la "
                "diversidad y los valores identitarios locales."
            ),
            codigo="CS.H.5.4.30.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Determinar los principales retos que enfrenta la "
                "integración latinoamericana, con base en el análisis de los "
                "logros y limitaciones de los proyectos regionales "
                "implementados."
            ),
            codigo="CS.H.5.4.31.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Contrastar los principales postulados del socialismo del "
                "siglo XXI con los del socialismo clásico en función de "
                "comprender los proyectos progresistas de América Latina."
            ),
            codigo="CS.H.5.4.32.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela "
                "fisiocrática como reacción al mercantilismo."
            ),
            codigo="CS.H.5.4.33.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela clásica "
                "como la primera escuela económica moderna."
            ),
            codigo="CS.H.5.4.34.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela marxista "
                "como crítica a la escuela clásica."
            ),
            codigo="CS.H.5.4.35.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela "
                "neoclásica como tentativa de integrar el análisis "
                "marginalista y algunas ideas de la escuela clásica."
            ),
            codigo="CS.H.5.4.36.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela de "
                "Chicago como contradicción de las teorías de la síntesis "
                "clásico-keynesiana."
            ),
            codigo="CS.H.5.4.37.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela "
                "keynesiana como respuesta a la Gran Depresión."
            ),
            codigo="CS.H.5.4.38.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela "
                "estructuralista como respuesta a la dependencia económica "
                "de América Latina."
            ),
            codigo="CS.H.5.4.39.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Analizar el origen y los principios de la escuela "
                "neoliberal como crítica al Estado de Bienestar."
            ),
            codigo="CS.H.5.4.40.",
            imprescindible=True,
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        Destreza(
            description=(
                "Construir un modelo económico a partir de todas las teorías "
                "estudiadas, en función de la satisfacción de las "
                "necesidades de la mayoría de la población de América Latina "
                "y el Ecuador."
            ),
            codigo="CS.H.5.4.41.",
            asignatura=historia,
            subnivel=bachillerato,
            bloque=bloque4_historia
        ),
        # Educación para la ciudadanía
        # Bloque 1
        Destreza(
            description=(
                "Determinar el origen y evolución histórica del concepto "
                "“ciudadanía” en la Grecia y la Roma antigua."
            ),
            codigo="CS.EC.5.1.1.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Determinar el origen y evolución histórica del concepto "
                "“derechos” a partir de la organización política de la "
                "sociedad (polis)."
            ),
            codigo="CS.EC.5.1.2.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Analizar los procesos históricos que propiciaron la "
                "Declaración de los Derechos del Hombre y del Ciudadano, "
                "mediante el análisis multicausal de los mismos."
            ),
            codigo="CS.EC.5.1.3.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Discutir los procesos históricos que propiciaron la "
                "Declaración de los Derechos de la Mujer y la Ciudadana, "
                "mediante el análisis multicausal de los mismos."
            ),
            codigo="CS.EC.5.1.4.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Determinar la trascendencia de la Declaración Universal de "
                "los Derechos Humanos, desde la comprensión de su "
                "significado político."
            ),
            codigo="CS.EC.5.1.5.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Reconocer la igualdad natural de los seres humanos y la "
                "protección de la vida frente a la arbitrariedad del poder "
                "desde el análisis político."
            ),
            codigo="CS.EC.5.1.6.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Identificar y analizar cada una de las diferentes "
                "generaciones de derechos y el contexto histórico de su "
                "surgimiento."
            ),
            codigo="CS.EC.5.1.7.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Analizar el significado jurídico posterior de los "
                "principios declaratorios de igualdad natural y protección a "
                "la vida, considerando la relación derechos - obligaciones y "
                "derechos - responsabilidades."
            ),
            codigo="CS.EC.5.1.8.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Explicar el principio de igualdad, a través del ejercicio "
                "del sufragio universal como condición de participación "
                "igualitaria."
            ),
            codigo="CS.EC.5.1.9.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Discernir la igualdad como principio generador de opciones "
                "y oportunidades para todos."
            ),
            codigo="CS.EC.5.1.10.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Establecer la relación entre individuo, sociedad y poder "
                "político, a partir de los derechos universales y desde el "
                "estudio de casos (la disidencia política, los desplazados, "
                "los refugiados)."
            ),
            codigo="CS.EC.5.1.11.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Analizar la evolución del concepto “igualdad natural”, a "
                "partir del acceso al sufragio universal por los diferentes "
                "grupos sociales (personas esclavizadas, mujeres, "
                "analfabetos, personas privadas de libertad, migrantes, "
                "personas con discapacidad, grupos minoritarios y/o "
                "vulnerables, etc.)."
            ),
            codigo="CS.EC.5.1.12.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        Destreza(
            description=(
                "Analizar el principio de igualdad natural expresado en "
                "otros ámbitos (educativo, político, económico, social, "
                "religioso, etc.), a partir del estudio de casos y de la "
                "ejemplificación de la realidad ecuatoriana."
            ),
            codigo="CS.EC.5.1.13.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque1_ciudadania
        ),
        # Bloque 2
        Destreza(
            description=(
                "Contextualizar el nacimiento de la democracia moderna, "
                "considerando los procesos históricos que la alumbraron."
            ),
            codigo="CS.EC.5.2.1.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Explicar la democracia moderna mediante el análisis de su "
                "significado radical: inexistencia de títulos naturales para "
                "gobernar, como el principio de filiación, el buen "
                "nacimiento, el linaje, la riqueza, la edad o la "
                "meritocracia."
            ),
            codigo="CS.EC.5.2.2.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Determinar los parámetros sobre los que se construye el "
                "concepto de ciudadanía en la democracia moderna, su "
                "concepción y roles, a partir del análisis de las "
                "características de esta última."
            ),
            codigo="CS.EC.5.2.3.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Discutir de manera informada la implicación de los "
                "principios de alternabilidad y de la despersonalización del "
                "poder como fundamentos de un sistema democrático "
                "pluralista."
            ),
            codigo="CS.EC.5.2.4.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Determinar las contradicciones del significado de soberanía "
                "del pueblo, considerando la evolución del concepto y sus "
                "cambios sustanciales."
            ),
            codigo="CS.EC.5.2.5.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Contrastar los derechos civiles y los derechos políticos, a "
                "partir del análisis de las características particulares de "
                "cada uno."
            ),
            codigo="CS.EC.5.2.6.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Describir los procesos de búsqueda de la legitimidad del "
                "poder político, por medio del análisis de los mecanismos de "
                "legitimación social."
            ),
            codigo="CS.EC.5.2.7.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Diferenciar varias formas de comprender la democracia, a "
                "partir del estudio comparativo de casos y de la "
                "ejemplificación."
            ),
            codigo="CS.EC.5.2.8.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Examinar el significado de la representación política, "
                "considerando las contribuciones de la democracia "
                "representativa."
            ),
            codigo="CS.EC.5.2.9.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Analizar la definición de democracia representativa, "
                "identificando sus límites y dificultades, considerando la "
                "distancia entre gobernantes y gobernados, electores y "
                "elegidos, los riesgos de tomar decisiones en nombre del "
                "electorado y la ausencia de rendición de cuentas."
            ),
            codigo="CS.EC.5.2.10.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Establecer la importancia de la rendición de cuentas y la "
                "aplicación de sistemas de control como mecanismos para "
                "reforzar y afianzar los sistemas democráticos "
                "representativos."
            ),
            codigo="CS.EC.5.2.11.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Definir el principio de deliberación a partir de sus "
                "implicaciones como procedimiento colectivo de toma de "
                "decisiones."
            ),
            codigo="CS.EC.5.2.12.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Examinar la posible complementariedad de la democracia "
                "representativa y la democracia deliberativa."
            ),
            codigo="CS.EC.5.2.13.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Evaluar la necesidad de la deliberación como esfera "
                "política, considerando su aplicabilidad y las dificultades "
                "que conlleva la realización del ideal deliberativo."
            ),
            codigo="CS.EC.5.2.14.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Establecer las ventajas y las limitaciones de la democracia "
                "deliberativa, considerando aspectos como la posibilidad de "
                "expresión social, la falta de información del público, "
                "entre otros."
            ),
            codigo="CS.EC.5.2.15.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Identificar los mecanismos de deliberación pública, "
                "considerando su complejidad y su aplicabilidad."
            ),
            codigo="CS.EC.5.2.16.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Distinguir la democracia social de la democracia política "
                "desde el estudio de experiencias en la sociedad civil y en "
                "la sociedad política, por medio de la ejemplificación."

            ),
            codigo="CS.EC.5.2.17.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Reconocer la democracia como una experiencia social "
                "enfocándose en el análisis de sus manifestaciones y "
                "expresiones en la vida cotidiana y en las prácticas "
                "ciudadanas comunes."
            ),
            codigo="CS.EC.5.2.18.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Analizar ejemplos de procesos deliberativos en el hogar, la "
                "escuela y la comunidad, poniendo énfasis en los mecanismos "
                "que los propician, facilitan y/o dificultan."
            ),
            codigo="CS.EC.5.2.19.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Discutir nuevos mecanismos de expresión y prácticas "
                "deliberativas, considerando las diversas formas de relación "
                "entre los ciudadanos en los nuevos espacios (redes "
                "sociales, Internet, etc.)."
            ),
            codigo="CS.EC.5.2.20.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        Destreza(
            description=(
                "Aplicar el diálogo y la deliberación como forma de consenso "
                "y disenso."
            ),
            codigo="CS.EC.5.2.21.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque2_ciudadania
        ),
        # Bloque 3
        Destreza(
            description=(
                "Explicar el desarrollo de la democracia en Ecuador desde un "
                "Estado excluyente en 1830, hasta llegar a la declaración de "
                "Estado plurinacional establecida en la Constitución del "
                "2008."
            ),
            codigo="CS.EC.5.3.1.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Discutir la cultura nacional fundamentada en la "
                "plurinacionalidad, tomando en cuenta los aportes que cada "
                "componente brinda desde su especificidad."
            ),
            codigo="CS.EC.5.3.2.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Analizar y valorar cada uno de los fundamentos sociales del "
                "Ecuador (indígena, afro ecuatoriano, mestizo y montubio) "
                "como un camino en la comprensión de la otredad y de la "
                "armonía social."
            ),
            codigo="CS.EC.5.3.3.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Comprender y valorar los aportes particulares de cada "
                "cultura en la construcción de una sociedad intercultural."
            ),
            codigo="CS.EC.5.3.4.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Determinar la evolución histórica de las demandas sociales "
                "de los pueblos y nacionalidades, en función de la "
                "construcción de un Estado incluyente y sostenible."
            ),
            codigo="CS.EC.5.3.5.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Reconocer la democracia como forma paradójica, a partir de "
                "su dificultad para concretar las expectativas sociales "
                "(igualdad social, movilidad social, autonomía del "
                "individuo)."
            ),
            codigo="CS.EC.5.3.6.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Identificar las limitaciones de la democracia, considerando "
                "la persistencia de exclusiones sociales, la tendencia a la "
                "corrupción y el surgumiento de nuevas élites."
            ),
            codigo="CS.EC.5.3.7.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Explicar el carácter ambiguo y complejo de la política, a "
                "partir del análisis de las luchas sociales y las luchas "
                "políticas por el cumplimiento de los derechos sociales."
            ),
            codigo="CS.EC.5.3.8.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        Destreza(
            description=(
                "Describir los alcances y limitaciones de la representación "
                "política otorgada a los representantes de la ciudadanía, "
                "reconociendo el derecho ciudadano de exigir la rendición de "
                "cuentas y/o la revocatoria del mandato."
            ),
            codigo="CS.EC.5.3.9.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque3_ciudadania
        ),
        # Bloque 4
        Destreza(
            description=(
                "Reconocer el surgimiento y evolución del Estado como forma "
                "de control social."
            ),
            codigo="CS.EC.5.4.1.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Identificar y analizar el rol de cada uno de los "
                "componentes del Estado: fuerzas armadas, derecho (leyes), "
                "tribunales de justicia, burocracia, cárceles, aparatos "
                "ideológicos (medios de comunicación), etc., y su impacto en "
                "las distintas clases sociales."
            ),
            codigo="CS.EC.5.4.2.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Diferenciar Estado, nación y gobierno a través de la "
                "identificación de sus funciones específicas y su rol "
                "histórico."
            ),
            codigo="CS.EC.5.4.3.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Determinar el significado de las Asambleas Nacionales "
                "Constituyentes desde las revoluciones del siglo XVIII."
            ),
            codigo="CS.EC.5.4.4.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Establecer la necesidad de las Asambleas Constituyentes "
                "como generadoras de otras instituciones políticas, a partir "
                "de la ejemplificación."
            ),
            codigo="CS.EC.5.4.5.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Identificar al pueblo como sujeto de las Asambleas "
                "Constituyentes, a partir del análisis del principio de "
                "soberanía."
            ),
            codigo="CS.EC.5.4.6.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Comparar las cartas constitucionales del Ecuador atendiendo "
                "a la progresión de los derechos de ciudadanía."
            ),
            codigo="CS.EC.5.4.7.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Caracterizar las Constituciones como expresión política de "
                "la sociedad y no solo como instrumentos jurídicos, mediante "
                "el análisis de las demandas sociales que estas recogen."
            ),
            codigo="CS.EC.5.4.8.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Señalar los postulados del republicanismo, tomando en "
                "cuenta las diferencias con otros modelos de organización "
                "política."
            ),
            codigo="CS.EC.5.4.9.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Identificar formas de republicanismo (federalismo, "
                "centralismo y confederalismo), a partir del análisis de "
                "determinados estados latinoamericanos (México, Venezuela, "
                "Argentina y Brasil)."
            ),
            codigo="CS.EC.5.4.10.",
            imprescindible=True,
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Estudiar la base filosófico-política de la Constitución del "
                "Estado ecuatoriano a partir de la Asamblea Constituyente de "
                "2008."
            ),
            codigo="CS.EC.5.4.11.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        Destreza(
            description=(
                "Explicar los roles que cumplen las funciones del Estado "
                "ecuatoriano a partir del análisis de los mecanismos de "
                "ordenamiento social, estructura y esquema de "
                "funcionamiento."
            ),
            codigo="CS.EC.5.4.12.",
            asignatura=educacion_ciudadania,
            subnivel=bachillerato,
            bloque=bloque4_ciudadania
        ),
        # Filosofía
        # Bloque 1
        Destreza(
            description=(
                "Comprender el origen del pensamiento filosófico a partir de "
                "la crítica al pensamiento mítico mediante la reflexión en "
                "torno a problemas concretos."
            ),
            codigo="CS.F.5.1.1.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Comprender el surgimiento del pensamiento filosófico como "
                "un esfuerzo para explicar los fenómenos de la naturaleza y "
                "la sociedad a partir de ellas mismas."
            ),
            codigo="CS.F.5.1.2.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Analizar y comprender las diversas producciones del "
                "pensamiento humano (matemática, geometría, música, arte, "
                "etc.) en el contexto del origen de la filosofía y su aporte "
                "a la misma."
            ),
            codigo="CS.F.5.1.3.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Discutir la relación entre armonía musical y armonía "
                "cósmica, considerando que “cosmos” significa “orden” y "
                "“armonía”."
            ),
            codigo="CS.F.5.1.4.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Analizar y valorar el pensamiento de Hipatia dentro de la "
                "escuela neoplatónica en la Grecia del siglo V."
            ),
            codigo="CS.F.5.1.5.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Discutir los desafíos planteados por Hipatia como pensadora "
                "y como mujer en la perspectiva de comprender actuales "
                "formas de intolerancia e irracionalidad."
            ),
            codigo="CS.F.5.1.6.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Analizar los conceptos fundamentales sobre la comunidad, el "
                "quehacer y las formas políticas, desde el enfoque de "
                "igualdad."
            ),
            codigo="CS.F.5.1.7.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Describir y categorizar el alcance de la idea del ser "
                "humano como “animal político” en función de su necesidad de "
                "vivir en sociedad."
            ),
            codigo="CS.F.5.1.8.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Discutir las desigualdades de la democracia originaria "
                "griega y su relación con la actualidad."
            ),
            codigo="CS.F.5.1.9.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Establecer la importancia de la persuasión como base de la "
                "deliberación en el ejercicio de la ciudadanía."
            ),
            codigo="CS.F.5.1.10.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Aplicar el método socrático y el diálogo estructurado en "
                "función de la construcción de un pensamiento creativo."
            ),
            codigo="CS.F.5.1.11.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        Destreza(
            description=(
                "Establecer las bases fundamentales del diálogo racional "
                "como experiencia comunicativa fecunda."
            ),
            codigo="CS.F.5.1.12.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque1_filosofia
        ),
        # Bloque 2
        Destreza(
            description=(
                "Diferenciar la verdad de la validez, mediante el uso de "
                "ejemplos en la discusión de un tema generador y la "
                "aplicación de los conocimientos adquiridos."
            ),
            codigo="CS.F.5.2.1.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Diferenciar el concepto de verdad en las ciencias formales "
                "y en las ciencias fácticas, como antecedente para abordar "
                "el estudio de las ciencias."
            ),
            codigo="CS.F.5.2.2.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Analizar las estructuras y los principios generales de la "
                "argumentación lógica (lógica aristotélica, silogismos) para "
                "cultivar un pensamiento coherente y riguroso."
            ),
            codigo="CS.F.5.2.3.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Diferenciar las falacias de las paradojas, en función de un "
                "ejercicio válido de razonamiento."
            ),
            codigo="CS.F.5.2.4.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Analizar la presencia de las principales falacias en textos "
                "académicos y de la prensa nacional e internacional."
            ),
            codigo="CS.F.5.2.5.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Comprender y aplicar los principios de la argumentación "
                "lógica, en función del desarrollo de la capacidad de "
                "argumentación y deliberación."
            ),
            codigo="CS.F.5.2.6.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Identificar y decodificar contradicciones, paradojas y "
                "falacias en discursos orales y escritos tomando en cuenta "
                "estos conceptos y sus significados."
            ),
            codigo="CS.F.5.2.7.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Identificar falacias lógicas o del pensamiento (de "
                "autoridad, ad hominem, etc.), mediante su reconocimiento en "
                "discursos de los medios de comunicación de masas."
            ),
            codigo="CS.F.5.2.8.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Comprender y aplicar los procedimientos de la lógica "
                "simbólica y sus conectores para construir cadenas "
                "argumentativas."
            ),
            codigo="CS.F.5.2.9.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Explicar el proceso de formación del pensamiento y la "
                "construcción de conceptos y teorías, diferenciándolo de la "
                "realidad a que hacen referencia, mediante ejercicios de "
                "conceptualización."
            ),
            codigo="CS.F.5.2.10.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Aplicar los conceptos de validez y de verdad en discursos "
                "de líderes políticos y editoriales de prensa."
            ),
            codigo="CS.F.5.2.11.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Establecer semejanzas y diferencias entre las formas de "
                "pensamiento cotidiano y el ejercicio del pensamiento "
                "filosófico y científico, en función de su valoración "
                "diferenciada."
            ),
            codigo="CS.F.5.2.12.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Distinguir las características del ensayo latinoamericano y "
                "del tratado europeo en textos representativos."
            ),
            codigo="CS.F.5.2.13.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Contrastar las perspectivas de objetividad y subjetividad "
                "presentes en el tratado europeo y en el ensayo "
                "latinoamericano, mediante el análisis del discurso, su "
                "descomposición en elementos y su posterior síntesis."
            ),
            codigo="CS.F.5.2.14.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Desarrollar alguna reflexión filosófica que evidencie los "
                "rasgos distintivos entre ensayo y tratado."
            ),
            codigo="CS.F.5.2.15.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Identificar tesis centrales y secundarias en un discurso "
                "filosófico corto."
            ),
            codigo="CS.F.5.2.16.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Identificar características de la identidad del “ser” "
                "latinoamericano en diversas expresiones artísticas "
                "(pintura, escultura, poesía, arquitectura, novela, ensayo "
                "literario) para elaborar un discurso y repensar su “ethos” "
                "a inicios del siglo XXI."
            ),
            codigo="CS.F.5.2.17.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        Destreza(
            description=(
                "Analizar las nuevas concepciones de la filosofía "
                "latinoamericana por medio de ejercicios orales y escritos."
            ),
            codigo="CS.F.5.2.18.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque2_filosofia
        ),
        # Bloque 3
        Destreza(
            description=(
                "Analizar las diferencias entre el pensamiento filosófico "
                "occidental y el pensamiento social latinoamericano, "
                "mediante la lectura comparada y crítica de textos "
                "fundamentales."
            ),
            codigo="CS.F.5.3.1.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Contrastar la reflexión de lo absoluto y la reflexión de "
                "los hechos factuales, en función de identificar la "
                "tendencia filosófica y su autor."
            ),
            codigo="CS.F.5.3.2.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Analizar las características del pensamiento filosófico "
                "latinoamericano, sus temas centrales y dudas sustanciales."
            ),
            codigo="CS.F.5.3.3.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Diferenciar el referente esencial de la reflexión "
                "filosófica europea (yo) y latinoamericana (nosotros) dentro "
                "de sus propias coordenadas históricas."
            ),
            codigo="CS.F.5.3.4.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Identificar los métodos de comprensión de la realidad en la "
                "filosofía latinoamericana a partir sus temas y sus formas "
                "de tratamiento de conceptos como libertad y liberación."
            ),
            codigo="CS.F.5.3.5.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Discutir los grandes temas críticos vinculados a la "
                "identidad y la cultura, a partir del descubrimiento de "
                "elementos de análisis propios en autores latinoamericanos."
            ),
            codigo="CS.F.5.3.6.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Cuestionar ideas previas de otras disciplinas "
                "contrastándolas con la filosofía, usando el vocabulario "
                "filosófico pertinente."
            ),
            codigo="CS.F.5.3.7.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Identificar las relaciones de poder que legitima o "
                "cuestiona la filosofía clásica y latinoamericana, en "
                "función de sus motivaciones y resultados políticos."
            ),
            codigo="CS.F.5.3.8.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Aplicar el método socrático en la reflexión del problema de "
                "la “liberación” frente al tópico de la “libertad”, desde "
                "diversas perspectivas (historia social y política, ensayos "
                "filosóficos)."
            ),
            codigo="CS.F.5.3.9.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        Destreza(
            description=(
                "Discutir las propuestas del Sumak Kawsay como proyecto "
                "utópico de otro mundo posible en función de la construcción "
                "de una nueva sociedad."
            ),
            codigo="CS.F.5.3.10.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque3_filosofia
        ),
        # Bloque 4
        Destreza(
            description=(
                "Discutir las virtudes platónicas y aristotélicas presentes "
                "en las acciones humanas y aplicarlas a la sociedad actual."
            ),
            codigo="CS.F.5.4.1.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Diferenciar comportamientos éticos y antiéticos desde el "
                "análisis de dilemas y estudios de caso."
            ),
            codigo="CS.F.5.4.2.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Explicar la dicotomía entre el bien y el mal en el análisis "
                "de casos de la vida cotidiana."
            ),
            codigo="CS.F.5.4.3.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Comprender la visión occidental y cristiana sobre la virtud "
                "y el pecado, mediante el estudio de creencias manifiestas "
                "en el medio ecuatoriano."
            ),
            codigo="CS.F.5.4.4.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Ejercer el pensamiento filosófico en la elaboración de "
                "preguntas complejas en función de ensayar respuestas "
                "significativas."
            ),
            codigo="CS.F.5.4.5.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Reflexionar en torno a las corrientes estudiadas sobre el "
                "bien y el mal y formar una opinión argumentada sobre su "
                "utilidad en la vida cotidiana."
            ),
            codigo="CS.F.5.4.6.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Contrastar las posiciones ético-filosóficas del kantismo y "
                "el utilitarismo, en función de comprender la construcción "
                "social y simbólica de la acción humana."
            ),
            codigo="CS.F.5.4.7.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Discutir la relación y pertinencia de la ética en la "
                "política y la política en la ética, en función de un "
                "ejercicio ciudadano responsable."
            ),
            codigo="CS.F.5.4.8.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Valorar el sistema político democrático desde una ética "
                "socio-histórica que lo hace posible, mediante el desarrollo "
                "de un discurso y alternativas de participación en este "
                "sistema."
            ),
            codigo="CS.F.5.4.9.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Evaluar los significados de estética y belleza en "
                "diferentes expresiones, épocas y culturas (arte, artesanía, "
                "música, estética personal) por medio de la experiencia "
                "personal y la indagación grupal."
            ),
            codigo="CS.F.5.4.10.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Comprender la felicidad a partir de la acción y la "
                "reflexión humana, tomando en cuenta el análisis de lo "
                "público y lo privado."
            ),
            codigo="CS.F.5.4.11.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Discutir el tratamiento del placer en Epicuro y Onfray como "
                "representantes de distintas épocas históricas, mediante la "
                "elaboración de argumentos basados en lecturas "
                "seleccionadas."
            ),
            codigo="CS.F.5.4.12.",
            imprescindible=True,
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
        Destreza(
            description=(
                "Discutir el tema del placer en la sociedad consumista "
                "moderna (lo utilitarista, lo individualista, lo descartable "
                "y lo desechable) desde la perspectiva de la ética, la "
                "solidaridad y el bienestar colectivo."
            ),
            codigo="CS.F.5.4.13.",
            asignatura=filosofia,
            subnivel=bachillerato,
            bloque=bloque4_filosofia
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0046_auto_20180814_1612'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
