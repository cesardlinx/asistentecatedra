from django.db import migrations


def create_objetivos_interdisciplinar(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    interdisciplinar = Area.objects.get(name='Interdisciplinar')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Incentivar el espíritu emprendedor del estudiante desde "
                "diferentes perspectivas y áreas del emprendimiento: "
                "comunitario, asociativo, empresarial, cultural, deportivo, "
                "artístico, social, etc."
            ),
            codigo="OG.EG.1.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Comprender los conceptos de “ingresos”, “gastos” e "
                "“inversiones” como elementos fundamentales para la toma de "
                "decisiones."
            ),
            codigo="OG.EG.2.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Resumir, organizar y registrar la contabilidad básica de un "
                "emprendimiento a partir de la comprensión de las cuentas, "
                "libros contables y estados financieros."
            ),
            codigo="OG.EG.3.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Conocer y explicar los requisitos y responsabilidades "
                "legales y sociales que debe cumplir un emprendedor en el "
                "momento de crear y mantener un emprendimiento, como forma "
                "de retribuir al Estado por los servicios recibidos."
            ),
            codigo="OG.EG.4.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Analizar las necesidades de la población, recolectar "
                "información basada en muestras e indagar sobre datos "
                "relacionados con el emprendimiento utilizando herramientas "
                "estadísticas."
            ),
            codigo="OG.EG.5.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Elaborar y analizar conceptos y principios básicos de "
                "administración de empresas y economía para la toma de "
                "decisiones y explicar su impacto en el desarrollo del "
                "emprendimiento."
            ),
            codigo="OG.EG.6.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Diseñar y formular un proyecto básico de emprendimiento con "
                "todos los elementos necesarios y componentes de innovación."
            ),
            codigo="OG.EG.7.",
            area=interdisciplinar
        ),
        ObjetivoGeneral(
            description=(
                "Conocer metodologías y técnicas para evaluar cuantitativa y "
                "cualitativamente la factibilidad de un proyecto de "
                "emprendimiento."
            ),
            codigo="OG.EG.8.",
            area=interdisciplinar
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0014_auto_20180727_2049'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_interdisciplinar)
    ]
