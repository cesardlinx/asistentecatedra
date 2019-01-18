from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    educacion_fisica = Asignatura.objects.get(name='Educación Física')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Objetivo.objects.bulk_create([
        # Preparatoria
        Objetivo(
            description=(
                "Participar en prácticas corporales (juegos, danzas, bailes, "
                "mímicas entre otras) de manera espontánea, segura y "
                "placentera, individualmente y con otras personas."
            ),
            codigo='O.EF.1.1.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer (en todas las dimensiones: motriz, emocional, "
                "conceptual, entre otras), sus posibilidades de "
                "participación en prácticas corporales, individuales y con "
                "otras personas."
            ),
            codigo='O.EF.1.2.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Desempeñar de modo seguro prácticas corporales (lúdicas y "
                "expresivo-comunicativas) que favorezcan el desarrollo de "
                "las habilidades motrices básicas y, de manera específica, "
                "la motricidad gruesa y fina, de acuerdo a sus necesidades y "
                "a las colectivas, en función de las prácticas corporales "
                "que elijan."

            ),
            codigo='O.EF.1.3.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Percibir su corporeidad y comenzar a construir conciencia "
                "de su propio cuerpo y la necesidad de cuidarlo."
            ),
            codigo='O.EF.1.4.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Explorar los beneficios que aportan los aprendizajes en "
                "Educación Física para el cuidado y mejora de la salud y "
                "bienestar personal acorde a sus intereses y necesidades."
            ),
            codigo='O.EF.1.5.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer sus posibilidades de acción durante su "
                "participación en diferentes prácticas corporales "
                "individuales."
            ),
            codigo='O.EF.1.6.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer las acciones individuales y colectivas realizadas "
                "en diversas prácticas corporales que colaboran con el "
                "cuidado de su entorno próximo."
            ),
            codigo='O.EF.1.7.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Identificar los sentidos y significados que tienen "
                "diferentes prácticas corporales en su entorno familiar y "
                "escolar."
            ),
            codigo='O.EF.1.8.',
            subnivel=preparatoria,
            asignatura=educacion_fisica
        ),
        # Elemental
        Objetivo(
            description=(
                "Participar democráticamente en prácticas corporales de "
                "diferentes regiones, de manera segura y placentera."
            ),
            codigo='O.EF.2.1.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Identificar requerimientos motores, conceptuales y "
                "actitudinales necesarios para participar de manera segura y "
                "placentera, acordando y respetando reglas y pautas de "
                "trabajo en diversas prácticas corporales."
            ),
            codigo='O.EF.2.2.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer diferentes posibilidades de participación "
                "individual y colectiva según las demandas de los pares, de "
                "cada práctica corporal y de las características del "
                "contexto en el que se realiza."
            ),
            codigo='O.EF.2.3.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Desempeñar de modo seguro prácticas corporales (lúdicas, "
                "expresivo-comunicativas y gimnásticas), que favorezcan la "
                "combinación de habilidades motrices básicas y capacidades "
                "motoras, de acuerdo a sus necesidades y a las colectivas, "
                "en función de las prácticas corporales que elijan."
            ),
            codigo='O.EF.2.4.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Mejorar sus posibilidades (corporales, "
                "expresivo-comunicativas, actitudinales, afectivas, entre "
                "otras) de participación en diferentes prácticas corporales "
                "dentro y fuera de la escuela a lo largo de su vida."
            ),
            codigo='O.EF.2.5.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer los beneficios que aportan los aprendizajes en "
                "Educación Física para el cuidado y mejora de la salud y "
                "bienestar personal, acorde a sus intereses y necesidades."
            ),
            codigo='O.EF.2.6.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer a sus pares como diferentes de sí y ncesarios "
                "para participar en prácticas corporales colectivas."
            ),
            codigo='O.EF.2.7.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer la importancia de llevar a cabo estrategias "
                "colectivas de cuidado de su entorno, a partir de las "
                "posibilidades que brindan las prácticas corporales."
            ),
            codigo='O.EF.2.8.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer los sentidos y significados que se construyen "
                "acerca de diferentes prácticas corporales en su barrio, "
                "parroquia y/o cantón."
            ),
            codigo='O.EF.2.9.',
            subnivel=elemental,
            asignatura=educacion_fisica
        ),
        # Media
        Objetivo(
            description=(
                "Participar en prácticas corporales de manera segura, "
                "atendiendo al cuidado de sí mismo, de sus pares y el medio "
                "ambiente."
            ),
            codigo='O.EF.3.1.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer sus intereses y necesidades para participar de "
                "manera democrática y placentera en prácticas corporales."
            ),
            codigo='O.EF.3.2.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer la influencia de sus experiencias previas en su "
                "dominio motor, y trabajar para alcanzar el mejor "
                "rendimiento posible en relación con la práctica corporal "
                "que elija."
            ),
            codigo='O.EF.3.3.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Participar de modo seguro y saludable en prácticas "
                "corporales (lúdicas, expresivo-comunicativas, gimnásticas y "
                "deportivas) que favorezcan el desarrollo integral de "
                "habilidades y destrezas motrices, capacidades motoras "
                "(coordinativas y condicionales), de acuerdo a sus "
                "necesidades y a las colectivas, en función de las"
                "pŕacticas corporales que elijan."
            ),
            codigo='O.EF.3.4.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocerse capaz de mejorar sus competencias y generar "
                "disposición para participar de prácticas corporales "
                "individuales y con otros."
            ),
            codigo='O.EF.3.5.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Valorar los beneficios que aportan los aprendizajes en "
                "Educación Física para el cuidado y mejora de la salud y "
                "bienestar personal, acorde a sus intereses y necesidades."
            ),
            codigo='O.EF.3.6.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer y valorar la necesidad de acordar con pares para "
                "participar en diferentes prácticas corporales."
            ),
            codigo='O.EF.3.7.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Construir acuerdos colectivos en diversas prácticas "
                "corporales, reconociendo y valorando la necesidad de cuidar "
                "y preservar las características del entorno que lo rodea."
            ),
            codigo='O.EF.3.8.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer la existencia de diversas prácticas corporales "
                "que adquieren sentido y significado en el contexto de cada "
                "cultura."
            ),
            codigo='O.EF.3.9.',
            subnivel=media,
            asignatura=educacion_fisica
        ),
        # Superior
        Objetivo(
            description=(
                "Participar en prácticas corporales de manera democrática, "
                "segura y placentera, con la posibilidad de crearlas y "
                "recrearlas no solo en el ámbito de las instituciones "
                "educativas."
            ),
            codigo='O.EF.4.1.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Avanzar en su comprensión crítica de la noción de sujeto "
                "saludable y actuar de manera coherente con ello."
            ),
            codigo='O.EF.4.2.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocerse capaz de participar de manera eficaz y "
                "confortable en prácticas corporales individualmente y con "
                "otras personas."
            ),
            codigo='O.EF.4.3.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Participar autónomamente en prácticas corporales (lúdicas, "
                "expresivo-comunicativas, gimnásticas y deportivas) que "
                "contribuyan a mejorar las habilidades y destrezas motrices, "
                "teniendo consciencia de sus capacidades motoras para una "
                "práctica segura y saludable de acuerdo a sus necesidades y "
                "a las colectivas, en función de las prácticas corporales "
                "que elijan."
            ),
            codigo='O.EF.4.4.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Profundizar en la comprensión de sí como sujeto corporal y "
                "contextuado, contribuyendo a la participación autónoma y "
                "crítica en prácticas corporales en el entorno escolar y en "
                "su vida fuera de las instituciones educativas."
            ),
            codigo='O.EF.4.5.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Experimentar los beneficios que aportan los aprendizajes en "
                "Educación Física para el cuidado y mejora de la salud y "
                "bienestar personal, acorde a sus intereses y necesidades."
            ),
            codigo='O.EF.4.6.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Distinguir las diferencias individuales y culturales "
                "presentes en el colectivo, para construir espacios de "
                "consenso que le permitan participar en diferentes prácticas "
                "corporales."
            ),
            codigo='O.EF.4.7.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Sensibilizarse frente al entorno que lo rodea, para "
                "reconocerlo como espacio propio y vital que necesita de "
                "cuidado durante su participación en diversas prácticas "
                "corporales."
            ),
            codigo='O.EF.4.8.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
        Objetivo(
            description=(
                "Reconocer y valorar los sentidos y significados que se "
                "construyen y se transmiten, mediante las prácticas "
                "corporales en diversas culturas."
            ),
            codigo='O.EF.4.9.',
            subnivel=superior,
            asignatura=educacion_fisica
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0018_auto_20180803_1400'),
    ]

    operations = [
        migrations.RunPython(create_objetivos)
    ]
