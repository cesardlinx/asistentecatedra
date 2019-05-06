from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )

    # Asignaturas
    emprendimiento_gestion = Asignatura.objects.get(
        name='Emprendimiento y Gestión')

    # Subniveles
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    CriterioEvaluacion.objects.bulk_create([
        # Emprendimiento y Gestión
        CriterioEvaluacion(
            description=(
                "Utiliza los conceptos básicos contables para conocer el "
                "futuro financiero de un emprendimiento y determinar "
                "el capital de trabajo necesario."
            ),
            codigo="CE.EG.5.1.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Construye estados financieros(balance general y estado "
                "de pérdidas y ganancias) por medio de los cambios en "
                "las transacciones contables, basándose en la "
                "normativa contable y tributaria vigente."
            ),
            codigo="CE.EG.5.2.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Justifica la importancia del pago de las obligaciones "
                "legales y tributarias de un emprendimiento al llenar los "
                "formularios básicos del SRI(RISE, IVA e Impuesto a la "
                "Renta) con el objetivo de crear una cultura tributaria."
            ),
            codigo="CE.EG.5.3.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Detecta, por medio de la investigación de campo, la "
                "necesidad de productos o servicios en un mercado, para "
                "asegurar un ciclo de vida duradero."
            ),
            codigo="CE.EG.5.4.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Aplica procesos estadísticos que permiten una buena "
                "interpretación de la información de mercado, para "
                "asegurar más probabilidad de éxito en un emprendimiento."
            ),
            codigo="CE.EG.5.5.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Precisa una planificación de personal adecuada para "
                "elevar el rendimiento del emprendimiento."
            ),
            codigo="CE.EG.5.6.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Juzga la eficiencia de un emprendimiento a partir de "
                "las variables económicas (“inflación”, “oferta”, "
                "“demanda”, “mercado”, “empleo”, etc.) del entorno."

            ),
            codigo="CE.EG.5.7.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Ofrece un nuevo producto o servicio que impacte un "
                "segmento de mercado definido."
            ),
            codigo="CE.EG.5.8.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Demuestra de qué manera una planificación de "
                "producción(recursos humanos y materiales) "
                "apropiada permite conocer con exactitud los "
                "desembolsos de dinero que genera un emprendimiento, "
                "para mejorar su proceso productivo."
            ),
            codigo="CE.EG.5.9.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Determina la capacidad de comercialización del "
                "emprendimiento a partir de una planificación financiera."
            ),
            codigo="CE.EG.5.10.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Elige emprendimientos de menor riesgo basándose en el "
                "análisis de la rentabilidad, periodo de recuperación, "
                "tasa interna de retorno y valor actual neto."
            ),
            codigo="CE.EG.5.11.",
            asignatura=emprendimiento_gestion,
            subnivel=bachillerato
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0034_auto_20180809_1446'),
    ]

    operations = [
        migrations.RunPython(
            create_criterios, reverse_code=migrations.RunPython.noop)
    ]
