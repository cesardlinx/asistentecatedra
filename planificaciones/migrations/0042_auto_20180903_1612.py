from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

    criterio_gestion_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.1.")
    criterio_gestion_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.2.")
    criterio_gestion_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.3.")
    criterio_gestion_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.4.")
    criterio_gestion_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.5.")
    criterio_gestion_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.6.")
    criterio_gestion_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.7.")
    criterio_gestion_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.8.")
    criterio_gestion_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.9.")
    criterio_gestion_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.10.")
    criterio_gestion_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.EG.5.11.")

    Indicador.objects.bulk_create([
        # Emprendimiento y gestión
        Indicador(
            description=(
                "Determina proyecciones financieras y el capital de trabajo "
                "de un emprendimiento basándose en conceptos financieros "
                "básicos. (I.1., I.4.)"
            ),
            codigo="I.EG.5.1.1.",
            criterio_evaluacion=criterio_gestion_5_1
        ),
        Indicador(
            description=(
                "Ordena las cuentas contables de acuerdo con la naturaleza "
                "de la función de los asientos contables en aquellos "
                "emprendimientos obligados a llevar contabilidad, tomando en "
                "cuenta las normas tributarias establecidas por la autoridad "
                "competente. (I.4., J.2.)"
            ),
            codigo="I.EG.5.2.1.",
            criterio_evaluacion=criterio_gestion_5_2
        ),
        Indicador(
            description=(
                "Registra transacciones en las cuentas contables bajo el "
                "principio de partida doble, según la normativa contable "
                "vigente. (J.2., I.4.)"
            ),
            codigo="I.EG.5.2.2.",
            criterio_evaluacion=criterio_gestion_5_2
        ),
        Indicador(
            description=(
                "Construye estados financieros (balance general y estado de "
                "pérdidas y ganancias) aplicando técnicas contables y la "
                "normativa vigente. (I.4., J.3.)"
            ),
            codigo="I.EG.5.2.3.",
            criterio_evaluacion=criterio_gestion_5_2
        ),
        Indicador(
            description=(
                "Comprende la importancia de generar una cultura tanto "
                "tributaria como de responsabilidad legal en cualquier "
                "emprendimiento, para validar sus operaciones en el mercado. "
                "(S.1., I.1.)"
            ),
            codigo="I.EG.5.3.1.",
            criterio_evaluacion=criterio_gestion_5_3
        ),
        Indicador(
            description=(
                "Determina, en una zona geográfica, la necesidad de un "
                "determinado bien o servicio para convertirla en su cliente "
                "frecuente. (S.4., S.1.)"
            ),
            codigo="I.EG.5.4.1.",
            criterio_evaluacion=criterio_gestion_5_4
        ),
        Indicador(
            description=(
                "Ejecuta investigaciones de campo y diseña instrumentos de "
                "investigación para seleccionar las ideas de emprendimiento "
                "que presenten mayor factibilidad en el mercado. (I.1., "
                "S.2.)"
            ),
            codigo="I.EG.5.4.2.",
            criterio_evaluacion=criterio_gestion_5_4
        ),
        Indicador(
            description=(
                "Presenta la información de mercado (oferta y demanda) a "
                "través de la representación gráfica de los datos "
                "procesados, en tablas, gráficas, histogramas, cálculo de "
                "frecuencias, diagramas, y estudios de medidas de tendencia "
                "central (media, mediana, moda), así como la información "
                "obtenida en la investigación de campo de forma resumida y "
                "concisa, de tal manera que se facilite la toma de "
                "decisiones. (I.2., I.4.)"
            ),
            codigo="I.EG.5.5.1.",
            criterio_evaluacion=criterio_gestion_5_5
        ),
        Indicador(
            description=(
                "Valora, de acuerdo con un criterio administrativo, la "
                "responsabilidad social en la planificación de los recursos "
                "humanos (estructura organizacional, proceso de "
                "contratación, capacitación, deberes y derechos laborales, "
                "despido) y diagrama una estructura organizacional óptima "
                "para un emprendimiento. (I.4, S.3.)"
            ),
            codigo="I.EG.5.6.1.",
            criterio_evaluacion=criterio_gestion_5_6
        ),
        Indicador(
            description=(
                "Comprueba la rentabilidad de un emprendimiento a partir del "
                "análisis de indicadores económicos (inflación, oferta, "
                "demanda, mercado, empleo, etc.), para favorecer la toma de "
                "decisiones. (I.2., I.1.)"
            ),
            codigo="I.EG.5.7.1.",
            criterio_evaluacion=criterio_gestion_5_7
        ),
        Indicador(
            description=(
                "Analiza la rentabilidad de un emprendimiento a partir de "
                "sus costos marginales (costos hundidos). (I.2., S.3.)"
            ),
            codigo="I.EG.5.7.2.",
            criterio_evaluacion=criterio_gestion_5_7
        ),
        Indicador(
            description=(
                "Realiza una mezcla adecuada de las variables de mercado "
                "(producto, precio, plaza, promoción y personalización) para "
                "un bien o servicio nuevo que presenta a un segmento de "
                "mercado específico mediante mecanismos de comunicación "
                "eficaces. (I.3., S.1.)"
            ),
            codigo="I.EG.5.8.1.",
            criterio_evaluacion=criterio_gestion_5_8
        ),
        Indicador(
            description=(
                "Especifica detalladamente las actividades de la "
                "planificación de producción (recursos humanos y materiales) "
                "para que un emprendimiento sea de calidad y productivo. "
                "(I.1., S.1.)"
            ),
            codigo="I.EG.5.9.1.",
            criterio_evaluacion=criterio_gestion_5_9
        ),
        Indicador(
            description=(
                "Determina la cantidad de bienes o servicios que se debe "
                "producir debido a la proporción de los costos de producción "
                "(c ostos fijos, variables, directos e indirectos) y los "
                "gastos incurridos, para que el emprendimiento sea "
                "productivo. (I.1., S.1.)"
            ),
            codigo="I.EG.5.9.2.",
            criterio_evaluacion=criterio_gestion_5_9
        ),
        Indicador(
            description=(
                "Aplica las TIC para proyectar costos y gastos, calcular el "
                "punto de equilibrio del emprendimiento y el margen de "
                "contribución del producto o servicio ofertado. (I.3.,I.1.)"
            ),
            codigo="I.EG.5.10.1.",
            criterio_evaluacion=criterio_gestion_5_10
        ),
        Indicador(
            description=(
                "Aplica las TIC en proyecciones de efectivo con experiencia "
                "en incrementos paulatinos y ciclicidad del mercado "
                "(considerando las unidades vendidas y los precios de "
                "venta), para establecer el monto de ingresos futuros del "
                "emprendimiento. (I.3., I.2.)"
            ),
            codigo="I.EG.5.10.2.",
            criterio_evaluacion=criterio_gestion_5_10
        ),
        Indicador(
            description=(
                "Elige el proyecto de emprendimiento con menor riesgo "
                "financiero después de analizar la rentabilidad, periodo de "
                "recuperación, tasa interna de retorno y valor actual neto. "
                "(I.1., I.2.)"
            ),
            codigo="I.EG.5.11.1.",
            criterio_evaluacion=criterio_gestion_5_11
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0041_auto_20180903_1534'),
    ]

    operations = [
        migrations.RunPython(create_indicadores,
                             reverse_code=migrations.RunPython.noop)
    ]
