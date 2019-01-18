from django.db import migrations


def create_objetivos_cultural(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    educacion_cultural = Area.objects.get(
        name='Educación Cultural y Artística')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Valorar las posibilidades y limitaciones de materiales, "
                "herramientas y técnicas de diferentes lenguajes artísticos "
                "en procesos de interpretación y/o creación de producciones "
                "propias."
            ),
            codigo="OG.ECA.1.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Respetar y valorar el patrimonio cultural tangible e "
                "intangible, propio y de otros pueblos, como resultado de la "
                "participación en procesos de investigación, observación y "
                "análisis de sus características, y así contribuir a su "
                "conservación y renovación."
            ),
            codigo="OG.ECA.2.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Considerar el papel que desempeñan los conocimientos y "
                "habilidades artísticos en la vida personal y laboral, y "
                "explicar sus funciones en el desempeño de distintas "
                "profesiones."
            ),
            codigo="OG.ECA.3.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Asumir distintos roles y responsabilidades en proyectos de "
                "interpretación y/o creación colectiva, y usar argumentos "
                "fundamentados en la toma de decisiones, para llegar a "
                "acuerdos que posibiliten su consecución."
            ),
            codigo="OG.ECA.4.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Apreciar de manera sensible y crítica los productos del "
                "arte y la cultura, para valorarlos y actuar, como público, "
                "de manera personal, informada y comprometida."
            ),
            codigo="OG.ECA.5.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Utilizar medios audiovisuales y tecnologías digitales para "
                "el conocimiento, el disfrute y la producción de arte y "
                "cultura."
            ),
            codigo="OG.ECA.6.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Crear productos artísticos que expresen visiones propias, "
                "sensibles e innovadoras, mediante el empleo consciente de "
                "elementos y principios del arte."
            ),
            codigo="OG.ECA.7.",
            area=educacion_cultural
        ),
        ObjetivoGeneral(
            description=(
                "Explorar su mundo interior para ser más consciente de las "
                "ideas y emociones que suscitan en las distintas "
                "producciones culturales y artísticas, y las que pueden "
                "expresar en sus propias creaciones, manifestándolas con "
                "convicción y conciencia."
            ),
            codigo="OG.ECA.8.",
            area=educacion_cultural
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0009_auto_20180727_1915'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_cultural)
    ]
