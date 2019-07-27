from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    lengua_literatura = Asignatura.objects.get(name='Lengua y Literatura')

    # Subniveles
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Objetivo.objects.bulk_create([
        # Elemental
        Objetivo(
            description=(
                "Comprender que la lengua escrita se usa con diversas "
                "intenciones según los contextos y las situaciones "
                "comunicativas, para desarrollar una actitud de indagación "
                "crítica frente a los textos escritos."
            ),
            codigo='O.LL.2.1.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Valorar la diversidad lingüística y cultural del país "
                "mediante el conocimiento y uso de algunas palabras y frases "
                "de las lenguas originarias, para fortalecer el sentido de "
                "identidad y pertenencia."
            ),
            codigo='O.LL.2.2.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Participar en situaciones de comunicación oral propias de "
                "los ámbitos familiar y escolar, con capacidad para "
                "escuchar, mantener el tema del diálogo y desarrollar ideas "
                "a partir del intercambio."
            ),
            codigo='O.LL.2.3.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Comunicar oralmente sus ideas de forma efectiva mediante el "
                "uso de las estructuras básicas de la lengua oral y "
                "vocabulario pertinente a la situación comunicativa."
            ),
            codigo='O.LL.2.4.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Leer de manera autónoma textos literarios y no literarios, "
                "para recrearse y satisfacer necesidades de información y "
                "aprendizaje."
            ),
            codigo='O.LL.2.5.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Desarrollar las habilidades de pensamiento para fortalecer "
                "las capacidades de resolución de problemas y aprendizaje "
                "autónomo mediante el uso de la lengua oral y escrita."
            ),
            codigo='O.LL.2.6.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Usar los recursos de la biblioteca de aula y explorar las "
                "TIC para enriquecer las actividades de lectura y escritura "
                "literaria y no literaria."
            ),
            codigo='O.LL.2.7.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Escribir relatos y textos expositivos y descriptivos, en "
                "diversos soportes disponibles, y emplearlos como medios de "
                "comunicación y expresión del pensamiento."
            ),
            codigo='O.LL.2.8.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Reflexionar sobre los patrones semánticos, léxicos, "
                "sintácticos, ortográficos y las propiedades textuales para "
                "aplicarlos en sus producciones escritas."
            ),
            codigo='O.LL.2.9.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Apropiarse del código alfabético del castellano y emplearlo "
                "de manera autónoma en la escritura."
            ),
            codigo='O.LL.2.10.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Apreciar el uso estético de la palabra, a partir de la "
                "escucha y la lectura de textos literarios, para potenciar "
                "la imaginación, la curiosidad, la memoria y desarrollar "
                "preferencias en el gusto literario."
            ),
            codigo='O.LL.2.11.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Demostrar una relación vivida con el lenguaje en la "
                "interacción con los textos literarios leídos o escuchados "
                "para explorar la escritura creativa."
            ),
            codigo='O.LL.2.12.',
            subnivel=elemental,
            asignatura=lengua_literatura
        ),
        # Media
        Objetivo(
            description=(
                "Interactuar con diversas expresiones culturales para "
                "acceder, participar y apropiarse de la cultura escrita."
            ),
            codigo='O.LL.3.1.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Valorar la diversidad cultural mediante el conocimiento de "
                "las lenguas originarias, para fomentar la interculturalidad "
                "en el país."
            ),
            codigo='O.LL.3.2.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Comprender discursos orales en diversos contexto de la "
                "actividad social y cultural y analizarlos con sentido "
                "crítico."
            ),
            codigo='O.LL.3.3.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Expresarse mediante el uso de estructuras básicas de la "
                "lengua oral en los diversos contextos de la actividad "
                "social y cultural, para exponer sus puntos de vista y "
                "respetar los ajenos."
            ),
            codigo='O.LL.3.4.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Participar en diversos contextos sociales y culturales y "
                "utilizar de manera adecuada las convenciones de la lengua "
                "oral para satisfacer necesidades de comunicación."
            ),
            codigo='O.LL.3.5.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Leer de manera autónoma textos no literarios, con fines de "
                "recreación, información y aprendizaje, y utilizar "
                "estrategias cognitivas de comprensión de acuerdo al tipo de "
                "texto."
            ),
            codigo='O.LL.3.6.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Usar los recursos que ofrecen las bibliotecas y las TIC "
                "para enriquecer las actividades de lectura y escritura "
                "literaria y no literaria, en interacción y colaboración con "
                "los demás."
            ),
            codigo='O.LL.3.7.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Escribir relatos y textos expositivos. descriptivos e "
                "instructivos, adecuados a una situación comunicativa y "
                "determinada para aprender, comunicarse y desarrollar el "
                "pensamiento."
            ),
            codigo='O.LL.3.8.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Utilizar los recursos de las TIC como medios de "
                "comunicación, aprendizaje y desarrollo del pensamiento."
            ),
            codigo='O.LL.3.9.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Aplicar los conocimientos semánticos, léxicos, sintácticos, "
                "ortográficos y las propiedades textuales en los procesos de "
                "composición y revisión de textos escritos."
            ),
            codigo='O.LL.3.10.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Seleccionar y disfrutar textos literarios para realizar "
                "interpretaciones personales y construir significados "
                "compartidos con otros lectores."
            ),
            codigo='O.LL.3.11.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Aplicar los recursos del lenguaje, a partir de los textos "
                "literarios, para fortalecer y profundizar la escritura "
                "creativa."
            ),
            codigo='O.LL.3.12.',
            subnivel=media,
            asignatura=lengua_literatura
        ),
        # Superior
        Objetivo(
            description=(
                "Reconocer las ventajas y beneficios que la cultura escrita "
                "ha aportado en diferentes momentos históricos y en diversos "
                "contextos de la vida social, cultural y académica, para "
                "enriquecer la concepción personal sobre el mundo."
            ),
            codigo='O.LL.4.1.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Valorar la diversidad lingüística del Ecuador en sus "
                "diferentes formas de expresión para fomentar la "
                "interculturalidad en el país."
            ),
            codigo='O.LL.4.2.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Analizar, con sentido crítico, discursos orales "
                "relacionados con la actualidad social y cultural para "
                "evitar estereotipos y prejuicios."
            ),
            codigo='O.LL.4.3.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Comunicarse oralmente con eficiencia en el uso de "
                "estructuras de la lengua oral en diversos contextos de la "
                "actividad social y cultural para exponer sus puntos de "
                "vista, construir acuerdos y resolver problemas."
            ),
            codigo='O.LL.4.4.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Participar de manera oral en diversos contextos sociales y "
                "culturales, a partir de un esquema previo; utilizar "
                "recursos audiovisuales y de las TIC para expresar sus "
                "opiniones y evaluar la pertinencia de los argumentos."
            ),
            codigo='O.LL.4.5.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Leer de manera autónoma textos no literarios, con fines de "
                "recreación, información y aprendizaje, y utilizar "
                "estrategias cognitivas de comprensión de acuerdo al tipo de "
                "texto."
            ),
            codigo='O.LL.4.6.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Utilizar las bibliotecas y las TIC de forma autónoma para "
                "localizar, seleccionar y organizar información como recurso "
                "de estudio e indagación."
            ),
            codigo='O.LL.4.7.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Escribir relatos y textos narrativos, expositivos, "
                "instructivos, descriptivos, explicativos y "
                "conversacionales, adecuados a una situación comunicativa "
                "determinada; emplear los recursos de las TIC como medios de "
                "comunicación, aprendizaje y expresión del pensamiento."
            ),
            codigo='O.LL.4.8.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Utilizar los recursos que ofrecen las TIC para desarrollar "
                "actividades de escritura literaria y no literaria en "
                "colaboración con los demás, en una variedad de entornos y "
                "medios digitales."
            ),
            codigo='O.LL.4.9.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Aplicar los conocimientos lingüísticos y explorar algunos "
                "recursos estilísticos en los procesos de composición y "
                "revisión de textos escritos para lograr claridad, precisión "
                "y cohesión."
            ),
            codigo='O.LL.4.10.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Realizar interpretaciones personales, en función de los "
                "elementos que ofrecen los textos literarios, y destacar las "
                "características del género al que pertenecen para iniciar "
                "la comprensión crítico-valorativa de la Literatura."
            ),
            codigo='O.LL.4.11.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),
        Objetivo(
            description=(
                "Utilizar de manera lúdica y personal los recursos propios "
                "del discurso literario en la escritura creativa para "
                "explorar la función estética del lenguaje."
            ),
            codigo='O.LL.4.12.',
            subnivel=superior,
            asignatura=lengua_literatura
        ),

    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0013_auto_20180731_0902'),
    ]

    operations = [
        migrations.RunPython(
            create_objetivos, reverse_code=migrations.RunPython.noop)
    ]
