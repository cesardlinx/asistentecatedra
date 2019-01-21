from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignaturas
    fisica = Asignatura.objects.get(name='Física')
    biologia = Asignatura.objects.get(name='Biología')
    quimica = Asignatura.objects.get(name='Química')

    # Subniveles
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Objetivo.objects.bulk_create([
        # Física
        Objetivo(
            description=(
                "Comprender que el desarrollo de la Física está ligado a la "
                "historia de la humanidad y al avance de la civilización y "
                "apreciar su contribución en el progreso socioeconómico, "
                "cultural y tecnológico de la sociedad."
            ),
            codigo='O.CN.F.5.1.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Comprender que la Física es un conjunto de teorías cuya "
                "validez ha tenido que comprobarse en cada caso, por medio "
                "de la experimentación."
            ),
            codigo='O.CN.F.5.2.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Comunicar resultados de experimentaciones realizadas, "
                "relacionados con fenómenos físicos, mediante informes "
                "estructurados, detallando la metodología utilizada, con la "
                "correcta expresión de las magnitudes medidas o calculadas."
            ),
            codigo='O.CN.F.5.3.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Comunicar información con contenido científico, utilizando "
                "el lenguaje oral y escrito con rigor conceptual, "
                "interpretar leyes, así como expresar argumentaciones y "
                "explicaciones en el ámbito de la Física."
            ),
            codigo='O.CN.F.5.4.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Describir los fenómenos que aparecen en la naturaleza, "
                "analizando las características más relevantes y las "
                "magnitudes que intervienen y progresar en el dominio de los "
                "conocimientos de Física, de menor a mayor profundidad, para "
                "aplicarlas a las necesidades y potencialidades de nuestro "
                "país."
            ),
            codigo='O.CN.F.5.5.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Reconocer el carácter experimental de la Física, así como "
                "sus aportaciones al desarrollo humano, por medio de la "
                "historia, comprendiendo las discrepancias que han superado "
                "los dogmas, y los avances científicos que han influido en "
                "la evolución cultural de la sociedad."
            ),
            codigo='O.CN.F.5.6.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Comprender la importancia de aplicar los conocimientos de "
                "las leyes físicas para satisfacer los requerimientos del "
                "ser humano a nivel local y mundial, y plantear soluciones a "
                "los problemas locales y generales a los que se enfrenta la "
                "sociedad."
            ),
            codigo='O.CN.F.5.7.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Desarrollar habilidades para la comprensión y difusión de "
                "los temas referentes a la cultura científica y de aspectos "
                "aplicados a la Física clásica y moderna, demostrando un "
                "espíritu científico, innovador y solidario, valorando las "
                "aportaciones de sus compañeros"
            ),
            codigo='O.CN.F.5.8.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        Objetivo(
            description=(
                "Diseñar y construir dispositivos y aparatos que permitan "
                "comprobar y demostrar leyes físicas, aplicando los "
                "conceptos adquiridos a través de las destrezas con "
                "criterios de desempeño."
            ),
            codigo='O.CN.F.5.9.',
            subnivel=bachillerato,
            asignatura=fisica
        ),
        # Biología
        Objetivo(
            description=(
                "Demostrar habilidades de pensamiento científico a fin de "
                "lograr flexibilidad intelectual; espíritu crítico; "
                "curiosidad acerca de la vida y con respecto a los seres "
                "vivos y el ambiente; trabajo autónomo y en equipo, "
                "colaborativo y participativo; creatividad para enfrentar "
                "desafíos e interés por profundizar los conocimientos "
                "adquiridos y continuar aprendiendo a lo largo de la vida, "
                "actuando con ética y honestidad."
            ),
            codigo='O.CN.B.5.1.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Desarrollar la curiosidad intelectual para comprender los "
                "principales conceptos, modelos, teorías y leyes "
                "relacionadas con los sistemas biologicos a diferentes "
                "escalas, desde los procesos subcelulares hasta la dinámica "
                "de los ecosistemas, y los procesos por los cuales los seres "
                "vivos persisten y cambian a lo largo del tiempo, para "
                "actuar con respeto hacia nosotros y la naturaleza."
            ),
            codigo='O.CN.B.5.2.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Integrar los conceptos de las ciencias biológicas para "
                "comprender la interdependencia de los seres humanos con la "
                "biodiversidad, y evaluar de forma crítica y responsable la "
                "aplicación de los avances científicos y tecnológicos en un "
                "contexto histórico-social, para encontrar soluciones "
                "innovadoras a problemas contemporáneos relacionados, "
                "respetando nuestras culturas, valores y tradiciones."
            ),
            codigo='O.CN.B.5.3.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Valorar los aportes de la ciencia en función del "
                "razonamiento lógico, crítico y complejo para comprender de "
                "manera integral la estructura y funcionamiento de su "
                "cuerpo, con el fin de aplicar medidas de promoción, "
                "protección y prevención que lleven al desarrollo de una "
                "salud integral, buscando el equilibrio físico, mental y "
                "emocional como parte esencial del plan de vida."
            ),
            codigo='O.CN.B.5.4.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Planificar y llevar a cabo investigaciones de campo, de "
                "laboratorio, de gestión o de otros tipos, que incluyan la "
                "exigencia de un trabajo en equipo, la recolección y "
                "análisis de datos cuantitativos y cualitativos; la "
                "interpretación de evidencias; la evaluación de los "
                "resultados de manera crítica, creativa y reflexiva, para la "
                "comunicación de los hallazgos, resultados, argumentos y "
                "conclusiones con honestidad."
            ),
            codigo='O.CN.B.5.5.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Manejar las tecnologías de la información y la comunicación "
                "(TIC) para apoyar sus procesos de aprendizaje, por medio de "
                "la indagación efectiva de información científica, la "
                "identificación y selección de fuentes confiables, y el uso "
                "de herramientas que permitan una adecuada divulgación de la "
                "información científica."
            ),
            codigo='O.CN.B.5.6.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Utilizar el lenguaje y la argumentación científica para "
                "debatir sobre los conceptos que manejan la tecnología y la "
                "sociedad acerca del cuidado del ambiente, la salud para "
                "armonizar lo físico y lo intelectual, las aplicaciones "
                "científicas y tecnológicas en diversas áreas del "
                "conocimento, encaminado a las necesidades y potencialidades "
                "de nuestro país."
            ),
            codigo='O.CN.B.5.7.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Comunicar, de manera segura y efectiva, el conocimiento "
                "científico y los resultados de sus indagaciones a "
                "diferentes interlocutores, mediante la argumentación "
                "analítica, crítica, reflexiva, y la justificación con "
                "pruebas y evidencias; y escuchar de manera respetuosa las "
                "perspectivas de otras personas."
            ),
            codigo='O.CN.B.5.8.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Apreciar el desarrollo del conocimiento científico a lo "
                "largo del tiempo, por medio de la indagación sobre la "
                "manera en que los científicos utilizan con ética la "
                "Biología en un amplio rango de aplicaciones, y la forma en "
                "que el conocimiento biológico influye en las sociedades a "
                "nivel local, regional y global, asumiendo responsabilidad "
                "social."
            ),
            codigo='O.CN.B.5.9.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Valorar la ciencia como el conjunto de procesos que "
                "permiten evaluar la realidad y las relaciones con otros "
                "seres vivos y con el ambiente, de manera objetiva y "
                "crítica."
            ),
            codigo='O.CN.B.5.10.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        Objetivo(
            description=(
                "Orientar el comportamiento hacia actitudes y prácticas "
                "responsables frente a los impactos socioambientales "
                "producidos por actividades antrópicas, que los preparen "
                "para la toma de decisiones fundamentadas en pro del "
                "desarrollo sostenible, para actuar con respeto y "
                "responsabilidad con los recursos de nuestro país."
            ),
            codigo='O.CN.B.5.11.',
            subnivel=bachillerato,
            asignatura=biologia
        ),
        # Química
        Objetivo(
            description=(
                "Reconocer la importancia de la Química dentro de la Ciencia "
                "y su impacto en la sociedad industrial y tecnológica para "
                "promover y fomentar el Buen Vivir asumiendo responsabilidad "
                "social."
            ),
            codigo='O.CN.Q.5.1.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Demostrar conocimiento y comprensión de los hechos "
                "esenciales, conceptos, principios, teorías y leyes "
                "relacionadas con la Química a partir de la curiosidad "
                "científica, generando un compromiso potencial con la "
                "sociedad."
            ),
            codigo='O.CN.Q.5.2.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Interpretar la estructura atómica y molecular, desarrollar "
                "configuraciones electrónicas y explicar su valor predictivo "
                "en el estudio de las propiedades químicas de los elementos "
                "y compuestos, impulsando un trabajo colaborativo, ético y "
                "honesto."
            ),
            codigo='O.CN.Q.5.3.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Reconocer, a partir de la curiosidad intelectual y la "
                "indagación, los factores que dan origen a las "
                "transformaciones de la materia, comprender que esta se "
                "conserva y proceder con respeto hacia la naturaleza para "
                "evidenciar los cambios de estado."
            ),
            codigo='O.CN.Q.5.4.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Identificar los elementos químicos y sus compuestos "
                "principales desde la perspectiva de su importancia "
                "económica, industrial, medioambiental y en la vida diaria."
            ),
            codigo='O.CN.Q.5.5.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Optimizar el uso de la información de la tabla periódica "
                "sobre las propiedades de los elementos químicos y utilizar "
                "la variación periódica como guía para cualquier trabajo de "
                "investigación científica sea individual o colectivo."
            ),
            codigo='O.CN.Q.5.6.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Relacionar las propiedades de los elementos y de sus "
                "compuestos con la naturaleza de su enlace y con su "
                "estructura generando así iniciativas propias en la "
                "formación de conocimientos con responsabilidad social."
            ),
            codigo='O.CN.Q.5.7.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Obtener por síntesis diferentes compuestos inorgánicos u "
                "orgánicos que requieren procedimientos experimentales "
                "básicos y específicos, actuando con ética y "
                "responsabilidad."
            ),
            codigo='O.CN.Q.5.8.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Reconocer diversos tipos de sistemas dispersos según el "
                "estado de agregación de sus componentes, y el tamaño de las "
                "partículas de su fase dispersa, sus propiedades y "
                "aplicaciones tecnológicas y preparar diversos tipos de "
                "disoluciones de concentraciones conocidas en un entorno de "
                "trabajo colaborativo utilizando todos los recursos físicos "
                "e intelectuales."
            ),
            codigo='O.CN.Q.5.9.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Manipular con seguridad materiales y reactivos químicos "
                "teniendo en cuenta sus propiedades físicas y químicas, "
                "considerando la leyenda de los pictogramas y cualquier "
                "peligro específico asociado con su uso, actuando de manera "
                "responsable con el ambiente."
            ),
            codigo='O.CN.Q.5.10.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
        Objetivo(
            description=(
                "Evaluar, interpretar y sintetizar datos e información sobre "
                "las propiedades físicas y las características estructurales "
                "de los compuestos químicos para constuir nuestra identidad "
                "y cultura de investigación científica."
            ),
            codigo='O.CN.Q.5.11.',
            subnivel=bachillerato,
            asignatura=quimica
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0020_auto_20180805_2039'),
    ]

    operations = [
        migrations.RunPython(
            create_objetivos, reverse_code=migrations.RunPython.noop)
    ]
