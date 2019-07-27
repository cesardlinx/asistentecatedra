from django.db import migrations


def create_objetivos_matematica(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    matematica = Area.objects.get(name='Matemática')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Proponer soluciones creativas a situaciones concretas de la "
                "realidad nacional y mundial mediante la aplicación de las "
                "operaciones básicas de los diferentes conjuntos numéricos, "
                "y el uso de modelos funcionales, algoritmos apropiados, "
                "estrategias y métodos formales y no formales de "
                "razonamiento matemático, que lleven a juzgar con "
                "responsabilidad la validez de procedimientos y los "
                "resultados en un contexto."
            ),
            codigo="OG.M.1.",
            area=matematica
        ),
        ObjetivoGeneral(
            description=(
                "Producir, comunicar y generalizar información, de manera "
                "escrita, verbal, simbólica, gráfica y/o tecnológica, "
                "mediante la aplicación de conocimientos matemáticos y el "
                "manejo organizado, responsable y honesto de las fuentes de "
                "datos, para así comprender otras disciplinas, entender las "
                "necesidades y potencialidades de nuestro país, y tomar "
                "decisiones con responsabilidad social."
            ),
            codigo="OG.M.2.",
            area=matematica
        ),
        ObjetivoGeneral(
            description=(
                "Desarrollar estrategias individuales y grupales que "
                "permitan un cálculo mental y escrito, exacto o estimado; y "
                "la capacidad de interpretación y solución de situaciones "
                "problémicas del medio."
            ),
            codigo="OG.M.3.",
            area=matematica
        ),
        ObjetivoGeneral(
            description=(
                "Valorar el empleo de las TIC para realizar cálculos y "
                "resolver, de manera razonada y crítica, problemas de la "
                "realidad nacional, argumentando la pertinencia de los "
                "métodos utilizados y juzgando la validez de los resultados."
            ),
            codigo="OG.M.4.",
            area=matematica
        ),
        ObjetivoGeneral(
            description=(
                "Valorar, sobre la base de un pensamiento crítico, creativo, "
                "reflexivo y lógico, la vinculación de los conocimientos "
                "matemáticos con los de otras disciplinas científicas y los "
                "saberes ancestrales, para así plantear soluciones a "
                "problemas de la realidad y contribuir al desarrollo del "
                "entorno social, natural y cultural."
            ),
            codigo="OG.M.5.",
            area=matematica
        ),
        ObjetivoGeneral(
            description=(
                "Desarrollar la curiosidad y la creatividad a través del uso "
                "de herramientas matemáticas al momento de enfrentar y "
                "solucionar problemas de la realidad nacional, demostrando "
                "actitudes de orden, perseverancia y capacidades de "
                "investigación."
            ),
            codigo="OG.M.6.",
            area=matematica
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0010_auto_20180727_2019'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_matematica,
                             reverse_code=migrations.RunPython.noop)
    ]
