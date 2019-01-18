from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    ciencias_naturales = Asignatura.objects.get(name='Ciencias Naturales')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Objetivo.objects.bulk_create([
        # Preparatoria
        Objetivo(
            description=(
                "Observar y describir la materia inerte natural y creada y "
                "los seres vivos del entorno, para diferenciarlos según sus "
                "características."
            ),
            codigo='O.CN.1.1.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Explorar y describir las características y necesidades de "
                "los seres vivos, desde sus propias experiencias."
            ),
            codigo='O.CN.1.2.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Observar e identificar la utilidad de las plantas y los "
                "animales en las actividades cotidianas de los seres humanos "
                "y comunicar las diferentes maneras de cuidarlos."
            ),
            codigo='O.CN.1.3.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Explorar su cuerpo, ubicar los órganos de los sentidos y "
                "aplicar medidas de vida saludable."
            ),
            codigo='O.CN.1.4.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Experimentar y describir las propiedades y el movimiento de "
                "los objetos, según sus tipos y usos en la vida cotidiana, e "
                "identificar los materiales que los constituyen."
            ),
            codigo='O.CN.1.5.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Indagar y describir las fuentes de luz y sonido y "
                "clasificarlas según su origen, para establecer semejanzas y "
                "diferencias entre ellas."
            ),
            codigo='O.CN.1.6.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Observar y registrar los cambios atmosféricos cotidianos y "
                "el impacto que tienen en las plantas, en los animales e "
                "incluso en sí mismos."
            ),
            codigo='O.CN.1.7.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Comprender que las observaciones, mediante los sentidos "
                "permiten obtener información del medio."
            ),
            codigo='O.CN.1.8.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Hacer preguntas y dar respuestas de hechos cotidianos y "
                "fenómenos naturales y sociales relacionados con el "
                "desarrollo de la ciencia, la tecnología y la sociedad."
            ),
            codigo='O.CN.1.9.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Demostrar las habilidades de indagación científica en el "
                "estudio del entorno natural."
            ),
            codigo='O.CN.1.10.',
            subnivel=preparatoria,
            asignatura=ciencias_naturales
        ),
        # Elemental
        Objetivo(
            description=(
                "Explorar y comprender los ciclos de vida y las "
                "características esenciales de las plantas y los animales, "
                "para establecer semejanzas y diferencias; clasificarlos en "
                "angiospermas o gimnospermas, vertebrados o invertebrados, "
                "respectivamente, y relacionarlos con su hábitat."
            ),
            codigo='O.CN.2.1.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Explorar y discutir las clases de hábitats, las reacciones "
                "de los seres vivos cuando los hábitats naturales cambian, "
                "las amenazas que causan su degradación y establecer la toma "
                "de decisiones pertinentes."
            ),
            codigo='O.CN.2.2.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Ubicar en su cuerpo los órganos relacionados con las "
                "necesidades vitales y explicar sus características y "
                "funciones, especialmente de aquellos que forman el sistema "
                "osteomuscular."
            ),
            codigo='O.CN.2.3.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Describir, dar ejemplos y aplicar hábitos de vida "
                "saludables para mantener el cuerpo sano y prevenir "
                "enfermedades."
            ),
            codigo='O.CN.2.4.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Experimentar y describir los cambios y el movimiento de los "
                "objetos por acción de la fuerza, en máquinas simples de uso "
                "cotidiano."
            ),
            codigo='O.CN.2.5.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Indagar en forma experimental y describir los estados "
                "físicos de la materia y sus cambios y verificarlos en el "
                "entorno."
            ),
            codigo='O.CN.2.6.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Indagar y explicar las formas de la materia y las fuentes "
                "de energía, sus clases, transformaciones, formas de "
                "propagación y usos en la vida cotidiana."
            ),
            codigo='O.CN.2.7.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Inferir las relaciones simples de causa-efecto de los "
                "fenómenos que se producen en el Universo y la Tierra, como "
                "las fases de la Luna y los movimientos de la Tierra, y "
                "analizar la importancia de los recursos naturales para la "
                "vida de los seres vivos."
            ),
            codigo='O.CN.2.8.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Comprender que la observación, la exploración y la "
                "experimentación son habilidades del pensamiento científico "
                "que facilitan la comprensión del desarrollo histórico de la "
                "ciencia, la tecnología y la sociedad."
            ),
            codigo='O.CN.2.9.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Aplicar habilidades de indagación científica para "
                "relacionar el medio físico con los seres vivos y comunicar "
                "los resultados con honestidad."
            ),
            codigo='O.CN.2.10.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Indagar y comunicar los conocimientos aplicados a la "
                "agricultura tradicional por civilizaciones ancestrales y "
                "culturales indígenas del Ecuador."
            ),
            codigo='O.CN.2.11.',
            subnivel=elemental,
            asignatura=ciencias_naturales
        ),
        # Media
        Objetivo(
            description=(
                "Observar y describir animales invertebrados y plantas sin "
                "semillas; agruparlos de acuerdo a sus características y "
                "analizar los ciclos reproductivos."
            ),
            codigo='O.CN.3.1.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Experimentar, analizar y relacionar las funciones de "
                "nutrición, respiración y fotosíntesis de las plantas, para "
                "comprender el mantenimiento de la vida en el planeta."
            ),
            codigo='O.CN.3.2.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Indagar los ecosistemas, su biodiversidad con sus "
                "interrelaciones y adaptaciones con el fin de valorar la "
                "diversidad de los ecosistemas y las especies y comprender "
                "que Ecuador es un país megadiverso."
            ),
            codigo='O.CN.3.3.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Analizar la estructura y función de los aparatos digestivo, "
                "respiratorio, circulatorio y excretor, establecer su "
                "relación funcional e indagar la estructura y función del "
                "sistema reproductor humano femenino y masculino, "
                "relacionándolo con los cambios en el comportamiento de los "
                "púberes."
            ),
            codigo='O.CN.3.4.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Valorar las acciones que conservan una salud integral, "
                "entendida como un estado de bienestar físico, mental y "
                "social en los púberes."
            ),
            codigo='O.CN.3.5.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Experimentar y diferenciar los tipos de fuerzas y los "
                "efectos de su aplicación sobre las variables físicas de "
                "objetos de uso cotidiano y explicar sus conclusiones."
            ),
            codigo='O.CN.3.6.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Formular preguntas y dar respuestas sobre las propiedades "
                "de la materia, la energía y sus manifestaciones, por medio "
                "de la indagación experimental y valorar su aplicación en la "
                "vida cotidiana."
            ),
            codigo='O.CN.3.7.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Inferir algunas de las relaciones de causa-efecto que se "
                "producen en la atmósfera y en la Tierra, como la radiación "
                "solar, los patrones de calentamiento de la superficie "
                "terrestre y el clima."
            ),
            codigo='O.CN.3.8.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Comprender la evolución histórica del conocimiento, con el "
                "propósito de valorar las investigaciones que han "
                "contribuido significativamente al avance de la ciencia y la "
                "tecnología."
            ),
            codigo='O.CN.3.9.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Usar habilidades de indagación científica y valorar la "
                "importancia del proceso investigativo en los fenómenos "
                "naturales cotidianos, desde las experiencias hasta el "
                "conocimiento científico."
            ),
            codigo='O.CN.3.10.',
            subnivel=media,
            asignatura=ciencias_naturales
        ),
        # Superior
        Objetivo(
            description=(
                "Describir los tipos y características de las células, el "
                "ciclo celular, los mecanísmos de reproducción celular y la "
                "constitución de los tejidos, que permiten comprender la "
                "compleja estructura y los niveles de organización de la "
                "materia viva."
            ),
            codigo='O.CN.4.1.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Describir la reproducción asexual y sexual en los seres "
                "vivos y deducir su importancia para la supervivencia y "
                "diversidad de las especies."
            ),
            codigo='O.CN.4.2.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Diseñar modelos representativos de los flujos de energía en "
                "cadenas y redes alimenticias, identificar los impactos de "
                "la actividad humana en los ecosistemas e interpretar las "
                "principales amenazas."
            ),
            codigo='O.CN.4.3.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Describir las etapas de la reproducción humana como "
                "aspectos fundamentales para comprender la fecundación, la "
                "implantación, el desarrollo del embrión y el nacimiento, y "
                "analizar la importancia de la nutrición prenatal y de la "
                "lactancia."
            ),
            codigo='O.CN.4.4.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Identificar las principales relaciones entre el ser humano "
                "y otros seres vivos que afectan su salud, la forma de "
                "controlar las infecciones a través de barreras "
                "inmunológicas naturales y artificiales."
            ),
            codigo='O.CN.4.5.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Investigar en forma experimental el cambio de posición y "
                "velocidad de los objetos por acción de una fuerza, su "
                "estabilidad o inestabilidad y los efectos de la fuerza "
                "gravitacional."
            ),
            codigo='O.CN.4.6.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Analizar la materia orgánica e inorgánica, establecer sus "
                "semejanzas y diferencias según sus propiedades, e "
                "identificar al carbono como elemento constitutivo de las "
                "biomoléculas (carbohidratos, proteínas, lípidos y ácidos "
                "nucléicos)."
            ),
            codigo='O.CN.4.7.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Investigar en forma documental la estructura y composición "
                "del Universo; las evidencias geológicas y paleontológicas "
                "en los cambios de la Tierra y el efecto de los ciclos "
                "biogeoquímicos en el medio natural. Todo, con el fin de "
                "predecir el impacto de las actividades humanas e "
                "interpretar las consecuencias del cambio climático y el "
                "calentamiento global."
            ),
            codigo='O.CN.4.8.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Comprender la conexión entre la ciencia y los problemas "
                "reales del mundo, como un proceso de alfabetización "
                "científica, para lograr, en los estudiantes, el interés "
                "hacia la ciencia, la tecnología y la sociedad."
            ),
            codigo='O.CN.4.9.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
        Objetivo(
            description=(
                "Utilizar el método científico para el desarrollo de "
                "habilidades de investigación científica, que promuevan "
                "pensamiento crítico, reflexivo y creativo enfocado a la "
                "resolución de problemas."
            ),
            codigo='O.CN.4.10.',
            subnivel=superior,
            asignatura=ciencias_naturales
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0019_auto_20180803_1740'),
    ]

    operations = [
        migrations.RunPython(create_objetivos)
    ]
