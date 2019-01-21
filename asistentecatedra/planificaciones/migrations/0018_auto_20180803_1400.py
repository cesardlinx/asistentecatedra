from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    educacion_cultural = Asignatura.objects.get(
        name='Educación Cultural y Artística'
    )

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Objetivo.objects.bulk_create([
        # Preparatoria
        Objetivo(
            description=(
                "Explorar las posibilidades de los sonidos, el movimiento "
                "y/o las imágenes a través de la participación en juegos que "
                "integren diversas opciones."
            ),
            codigo='O.ECA.1.1.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Observar e identificar prácticas y productos patrimoniales "
                "y producciones artísticas del entorno próximo."
            ),
            codigo='O.ECA.1.2.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Identificar y nombrar algunas profesiones del mundo del "
                "arte y la cultura."
            ),
            codigo='O.ECA.1.3.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Aportar ideas y llegar a acuerdos con los otros miembros "
                "del grupo en procesos de interpretación y creación "
                "artística."
            ),
            codigo='O.ECA.1.4.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Disfrutar como espectador de manifestaciones artísticas y "
                "culturales de su entorno inmediato."
            ),
            codigo='O.ECA.1.5.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Registrar imágenes y sonidos mediante el uso de medios "
                "audiovisuales y tecnologías digitales."
            ),
            codigo='O.ECA.1.6.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Practicar un amplio repertorio de juegos tradicionales y "
                "contemporáneos que involucren el uso del cuerpo, la voz y/o "
                "imágenes."
            ),
            codigo='O.ECA.1.7.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Expresar las ideas y sentimientos que suscitan las "
                "observaciones de distintas manifestaciones culturales y "
                "artísticas."
            ),
            codigo='O.ECA.1.8.',
            subnivel=preparatoria,
            asignatura=educacion_cultural
        ),
        # Elemental
        Objetivo(
            description=(
                "Realizar producciones artísticas individuales y colectivas "
                "a partir de la combinación de las técnicas y materiales "
                "dados."
            ),
            codigo='O.ECA.2.1.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Identificar y describir los elementos característicos de "
                "productos patrimoniales y producciones artísticas "
                "contemporáneas locales y universales."
            ),
            codigo='O.ECA.2.2.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Describir las principales características de algunas "
                "profesiones del mundo del arte y la cultura."
            ),
            codigo='O.ECA.2.3.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Asumir distintos roles en el desarrollo de proyectos "
                "culturales y artísticos."
            ),
            codigo='O.ECA.2.4.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Expresar las ideas y sentimientos que suscita la "
                "observación de producciones culturales y artísticas "
                "tradicionales y contemporáneas."
            ),
            codigo='O.ECA.2.5.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Utilizar medios audiovisuales y tecnologías digitales para "
                "buscar información sobre obras, autores o técnicas y crear "
                "producciones sonoras, visuales o audiovisuales sencillas."
            ),
            codigo='O.ECA.2.6.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Expresar y comunicar emociones o ideas a través del "
                "lenguaje sonoro, visual y corporal."
            ),
            codigo='O.ECA.2.7.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Buscar, seleccionar y organizar información sobre distintas "
                "manifestaciones culturales y artísticas, y exponer los "
                "conocimientos adquiridos."
            ),
            codigo='O.ECA.2.8.',
            subnivel=elemental,
            asignatura=educacion_cultural
        ),
        # Media
        Objetivo(
            description=(
                "Observar el uso de algunos materiales y técnicas en obras "
                "artísticas de distintas características, y aplicarlos en "
                "creaciones propias."
            ),
            codigo='O.ECA.3.1.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Explicar algunas características del patrimonio cultural, "
                "tangible e intangible, propio y de otros pueblos, a partir "
                "de la observación y el análisis de sus características; y "
                "colaborar en su conservación y renovación."
            ),
            codigo='O.ECA.3.2.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Realizar tasignaturas propias de algunas profesiones del "
                "mundo del arte y la cultura, a través de la participación "
                "en pequeños proyectos colaborativos realizados en la "
                "escuela o la comunidad."
            ),
            codigo='O.ECA.3.3.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Programar y realizar pequeños proyectos culturales o "
                "artísticos asumiendo distintos roles en su diseño y "
                "desarrollo."
            ),
            codigo='O.ECA.3.4.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Describir las principales características de un amplio "
                "repertorio de manifestaciones artísticas y culturales."
            ),
            codigo='O.ECA.3.5.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Usar recursos tecnológicos para la búsqueda de información "
                "sobre eventos y producciones culturales y artísticas, y "
                "para la creación y difusión de productos sonoros, visuales "
                "o audiovisuales."
            ),
            codigo='O.ECA.3.6.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Participar en procesos de interpretación y creación visual, "
                "corporal y/o sonora, individuales y colectivos, y valorar "
                "las aportaciones propias y ajenas."
            ),
            codigo='O.ECA.3.7.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Formular opiniones acerca de las manifestaciones culturales "
                "y artísticas, demostrando el conocmiento que se tiene de "
                "las mismas y el grado de disfrute o rechazo que cada una "
                "suscita."
            ),
            codigo='O.ECA.3.8.',
            subnivel=media,
            asignatura=educacion_cultural
        ),
        # Superior
        Objetivo(
            description=(
                "Comparar las posibilidades que ofrecen diversos materiales "
                "y técnicas de los diferentes lenguajes artísticos en "
                "procesos de interpretación y/o creación individual y "
                "colectiva."
            ),
            codigo='O.ECA.4.1.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Participar en la renovación del patrimonio cultural, "
                "tangible e e intangible, mediante la creación de productos "
                "culturales y artísticos en los que se mezclan elementos de "
                "lo ancestral y lo contemporáneo."
            ),
            codigo='O.ECA.4.2.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Explicar el papel que desempeñan los conocimientos y las "
                "habilidades artísticas en la vida de las personas, como "
                "recursos para el ocio y para el ejercicio de distintas "
                "profesiones."
            ),
            codigo='O.ECA.4.3.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Participar en proyectos de creación colectiva demostrando "
                "respeto por las ideas y formas de expresión propias y "
                "ajenas, y tomar conciencia, como miembro del gurpo, del "
                "enriquecimiento que se produce con las aportaciones de los "
                "demás."
            ),
            codigo='O.ECA.4.4.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Reconocer algunas características significativas de eventos "
                "culturales y obras artísticas de distintos estilos, y "
                "utilizar la terminología apropiada para describirlos y "
                "comentarlos."
            ),
            codigo='O.ECA.4.5.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Utilizar algunos medios audiovisuales y tecnologías "
                "digitales para el conocimiento, producción y disfrute del "
                "arte y la cultura."
            ),
            codigo='O.ECA.4.6.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Utilizar las posibilidades del cuerpo, la imagen y el "
                "sonido como recursos para expresar ideas y sentimientos, "
                "enriqueciendo sus posibilidades de comunicación, con "
                "respeto por las distintas formas de expresión y "
                "autoconfianza en las producciones propias."
            ),
            codigo='O.ECA.4.7.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
        Objetivo(
            description=(
                "Exponer ideas, sentimientos y puntos de vista personales "
                "sobre distintas manifestaciones culturales y artísticas, "
                "propias y ajenas."
            ),
            codigo='O.ECA.4.8.',
            subnivel=superior,
            asignatura=educacion_cultural
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0017_auto_20180731_1350'),
    ]

    operations = [
        migrations.RunPython(
            create_objetivos, reverse_code=migrations.RunPython.noop)
    ]
