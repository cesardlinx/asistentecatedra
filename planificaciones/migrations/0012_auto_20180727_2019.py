from django.db import migrations


def create_objetivos_sociales(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    ciencias_sociales = Area.objects.get(name='Ciencias Sociales')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Potenciar la construcción de una identidad personal y "
                "social auténtica a través de la comprensión de los procesos "
                "históricos y los aportes culturales locales, regionales y "
                "globales, en función de ejercer una libertad y autonomía "
                "solidaria y comprometida con los otros."
            ),
            codigo="OG.CS.1.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Contextualizar la realidad ecuatoriana, a través de su "
                "ubicación y comprensión dentro del proceso histórico "
                "latinoamericano y mundial, para entender sus procesos de "
                "dependencia y liberación, históricos y contemporáneos."
            ),
            codigo="OG.CS.2.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Comprender la dinámica individuo-sociedad, por medio del "
                "análisis de las relaciones entre las personas, los "
                "acontecimientos, procesos históricos y geográficos en el "
                "espacio-tiempo, a fin de comprender los patrones de cambio, "
                "permanencia y continuidad de los diferentes fenómenos "
                "sociales y sus consecuencias."
            ),
            codigo="OG.CS.3.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Determinar los orígenes del universo, el sistema solar, la "
                "Tierra, la vida y el ser humano, sus características y "
                "relaciones históricas y geográficas, para comprender y "
                "valorar la vida en todas sus manifestaciones."
            ),
            codigo="OG.CS.4.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Identificar y relacionar la geografía local, regional y "
                "global, para comprender los procesos de globalización e "
                "interdependencia de las distintas realidades geopolíticas."
            ),
            codigo="OG.CS.5.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Construir una conciencia cívica, crítica y autónoma, a "
                "través dela interiorización y práctica de los derechos "
                "humanos universales y ciudadanos, para desarrollar "
                "actitudes de solidaridad y participación en la vida "
                "comunitaria."
            ),
            codigo="OG.CS.6.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Adoptar una actitud crítica frente a la desigualdad "
                "socioeconómica y toda forma de discriminación, y de respeto "
                "ante la diversidad, por medio de la contextualización "
                "histórica de los procesos sociales y su desnaturalización, "
                "para promover una sociedad plural, justa y solidaria."
            ),
            codigo="OG.CS.7.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Aplicar los conocimientos adquiridos, a través del "
                "ejercicio de una ética solidaria y ecológica que apunte a "
                "la construcción y consolidación de una sociedad nueva "
                "basada en el respeto a la dignidad humana y de todas las "
                "formas de vida."
            ),
            codigo="OG.CS.8.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Promover y estimular el cuidado del entorno natural y "
                "cultural, a través de su conocimeinto y valoración, para "
                "garantizar una convivencia armónica y responsable con todas "
                "las formas de vida del planeta."
            ),
            codigo="OG.CS.9.",
            area=ciencias_sociales
        ),
        ObjetivoGeneral(
            description=(
                "Usar y contrastar diversas fuentes, metodologías "
                "cualitativas y cuantitativas y herramientas cartográficas, "
                "utilizando medios de comunicación y TIC, en la codificación "
                "e interpretación crítica de discursos e imágenes, para "
                "desarrollar un cirterio propio acerca de la realidad local, "
                "regional y global, y reducir la brecha digital."
            ),
            codigo="OG.CS.10.",
            area=ciencias_sociales
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0011_auto_20180727_2001'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_sociales,
                             reverse_code=migrations.RunPython.noop)
    ]
