from django.db import migrations


def create_objetivos_literatura(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    lengua_literatura = Area.objects.get(name='Lengua y Literatura')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Desempeñarse como usuarios competentes de la cultura "
                "escrita en diversos contexto personales, sociales y "
                "culturales para actuar con autonomía y ejercer una "
                "ciudadanía plena."
            ),
            codigo="OG.LL.1.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Valorar la diversidad lingüística a partir del conocimiento "
                "de su aporte a la construcción de una sociedad "
                "intercultural y plurinacional, en un marco de interacción "
                "respetuosa y de fortalecimiento de la identidad."
            ),
            codigo="OG.LL.2.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Evaluar, con sentido crítico, discursos orales relacionados "
                "con la actualidad social y cultural para asumir y "
                "consolidar una perspectiva personal."
            ),
            codigo="OG.LL.3.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Participar de manera fluida y eficiente en diversas "
                "situaciones de comunicación oral, formales y no formales, "
                "integrando los conocimientos sobre la estructura de la "
                "lengua oral y utilizando vocabulario especializado, según "
                "la intencionalidad del discurso."
            ),
            codigo="OG.LL.4.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Leer de manera autónoma y aplicar estrategias cognitivas y "
                "metacognitivas de comprensión, según el protocolo de "
                "lectura."
            ),
            codigo="OG.LL.5.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Seleccionar textos, demostrando una actitud reflexiva y "
                "crítica con respecto a la calidad y veracidad de la "
                "información disponible en diversas fuentes para hacer uso "
                "selectivo y sistemático de la misma."
            ),
            codigo="OG.LL.6.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Producir diferentes tipos de texto, con distintos "
                "propósitos y en variadas situaciones comunicativas, en "
                "diversos soportes disponibles para comunicarse, aprender y "
                "construir conocimientos."
            ),
            codigo="OG.LL.7.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Aplicar los conocimientos sobre los elementos estructurales "
                "y funcionales de la lengua castellana en los procesos de "
                "composición y revisión de textos escritos para comunicarse "
                "de manera eficiente."
            ),
            codigo="OG.LL.8.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Seleccionar y examinar textos literarios, en el marco de la "
                "tradición nacional y mundial, para ponerlos en diálogo con "
                "la historia y la cultura."
            ),
            codigo="OG.LL.9.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Apropiarse del patrimonio literario ecuatoriano, a partir "
                "del conocimiento de sus principales exponentes, para "
                "construir un sentido de pertenencia."
            ),
            codigo="OG.LL.10.",
            area=lengua_literatura
        ),
        ObjetivoGeneral(
            description=(
                "Ampliar las posibilidades expresivas de la escritura al "
                "desarrollar una sensibilidad estética e imaginativa en el "
                "uso personal y creativo del lenguaje."
            ),
            codigo="OG.LL.11.",
            area=lengua_literatura
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0007_auto_20180727_1712'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_literatura)
    ]
