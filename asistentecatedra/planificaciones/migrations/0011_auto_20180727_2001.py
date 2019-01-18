from django.db import migrations


def create_objetivos_naturales(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    ciencias_naturales = Area.objects.get(name='Ciencias Naturales')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Desarrollar habilidades de pensamiento científico con el "
                "fin de lograr flexibilidad intelectual, espíritu indagador "
                "y pensamiento crítico; demostrar curiosidad por explorar el "
                "medio que les rodea y valorar la naturaleza como resultado "
                "de la comprensión de las interacciones entre los seres "
                "vivos y el ambiente físico."
            ),
            codigo="OG.CN.1.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Comprender el punto de vista de la ciencia sobre la "
                "naturaleza de los seres vivos, su diversidad, "
                "interrelaciones y evolución; sobre la Tierra, sus cambios y "
                "su lugar en el Universo, y sobre los procesos, físicos y "
                "químicos, que se producen en la materia."
            ),
            codigo="OG.CN.2.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Integrar los conceptos de las ciencias biológicas, "
                "químicas, físicas, geológicas y astronómicas, para "
                "comprender la ciencia, la tecnología y la sociedad, ligadas "
                "a la capacidad de inventar, innovar y dar soluciones a la "
                "crisis socioambiental."
            ),
            codigo="OG.CN.3.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Reconocer y valorar los aportes de la ciencia para "
                "comprender los aspectos básicos de la estructura y el "
                "funcionamiento de su cuerpo, con el fin de aplicar medidas "
                "de promoción, protección y prevención de la salud integral."
            ),
            codigo="OG.CN.4.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Resolver problemas de la ciencia mediante el método "
                "científico, a partir de la identificación de problemas, la "
                "búsqueda crítica de información, la elaboración de "
                "conjeturas, el diseño de actividades experimentales, el "
                "análisis y la comunicación de resultados confiables y "
                "éticos."
            ),
            codigo="OG.CN.5.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Usar las tecnologías de la información y la comunicación "
                "(TIC) como herramientas para la búsqueda crítica de "
                "información, el análisis y la comunicación de sus "
                "experiencias y conclusiones sobre los fenómenos y hechos "
                "naturales y sociales."
            ),
            codigo="OG.CN.6.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Utilizar el lenguaje oral y el escrito con propiedad, así "
                "como otros sistemas de notación y representación, cuando se "
                "requiera."
            ),
            codigo="OG.CN.7.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Comunicar información científica, resultados y conclusiones "
                "de sus indagaciones a diferentes interlocutores, mediante "
                "diversas técnicas y recursos, la argumentación críticas y "
                "reflexiva y la justificación con pruebas y evidencias."
            ),
            codigo="OG.CN.8.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Comprender y valorar los saberes ancestrales y la historia "
                "del desarrollo científico, tecnológico y cultural, "
                "considerando la acción que estos ejercen en la vida "
                "personal y social."
            ),
            codigo="OG.CN.9.",
            area=ciencias_naturales
        ),
        ObjetivoGeneral(
            description=(
                "Apreciar la importancia de la formación científica, los "
                "valores y actitudes propios del pensamiento científico, y "
                "adoptar una actitud crítica y fundamentada ante los grandes "
                "problemas que hoy plantean las relaciones entre ciencia y "
                "sociedad."
            ),
            codigo="OG.CN.10.",
            area=ciencias_naturales
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0010_auto_20180727_1945'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_naturales)
    ]
