from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    gestion = Asignatura.objects.get(name='Emprendimiento y Gestión')

    # Bloques Emprendimiento y Gestión
    bloque1_emprendimiento = BloqueCurricular.objects.get(
        name="Planificación y control financiero del emprendimiento")
    bloque2_emprendimiento = BloqueCurricular.objects.get(
        name="Responsabilidad legal y social del emprendedor"
    )
    bloque3_emprendimiento = BloqueCurricular.objects.get(
        name="Investigación de mercado y estadística aplicada")
    bloque4_emprendimiento = BloqueCurricular.objects.get(
        name="Economía para la toma de decisiones")
    bloque5_emprendimiento = BloqueCurricular.objects.get(
        name="Formulación del proyecto de emprendimiento")
    bloque6_emprendimiento = BloqueCurricular.objects.get(
        name="Evaluación del proyecto de emprendimiento")

    # Subnivel
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Emprendimiento y Gestión
        # Bloque 1
        Destreza(
            description=(
                "Describir y explicar los conceptos financieros básicos de "
                "un emprendimiento, como “ingresos”, “costos”, “gastos” e "
                "“inversión”, “punto de equilibrio” y sus proyecciones "
                "futuras como elemento fundamental para las proyecciones."
            ),
            codigo="EG.5.1.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Distinguir los diferentes tipos de costos y gastos de un "
                "emprendimiento para determinar detenidamente el capital de "
                "trabajo necesario para un emprendimiento."
            ),
            codigo="EG.5.1.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar la obligatoriedad jurídica de llevar "
                "contabilidad, de acuerdo a lo establecido por las normas "
                "tributarias, como elemento fundamental para determinar la "
                "forma de llevar la contabilidad."
            ),
            codigo="EG.5.1.3.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Deducir la importancia de la contabilidad como elemento de "
                "control financiero del emprendimiento."
            ),
            codigo="EG.5.1.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Explicar las principales normas contables, relacionadas con "
                "la partida doble, para establecer los impactos en las "
                "cuentas."
            ),
            codigo="EG.5.1.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Clasificar las principales cuentas contables con su "
                "respectivo nombre para personificarlas, mediante la "
                "determinación de la naturaleza de su función en los "
                "asientos contables, tales como caja, bancos, cuentas por "
                "cobrar, inventarios, activos fijos, depreciación, capital, "
                "cuentas por pagar, préstamos bancarios, capital."
            ),
            codigo="EG.5.1.6.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar los componentes básicos del activo, pasivo, "
                "patrimonio, ingresos, costos y gastos, de acuerdo con la "
                "normativa contable, para clasificar adecuadamente las "
                "cuentas contables."
            ),
            codigo="EG.5.1.7.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Interpretar las cuentas contables mediante la "
                "identificación de los cambios que causan las transacciones "
                "en los activos, pasivos y patrimonios, reflejados en la "
                "cuenta por partida doble."
            ),
            codigo="EG.5.1.8.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Elaborar un balance general básico mediante la aplicación "
                "de los principios, conceptos y técnicas contables y la "
                "normatividad vigente."
            ),
            codigo="EG.5.1.9.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Elaborar un estado de pérdidas y ganancias básico mediante "
                "la aplicación de las cuentas contables y la ecuación "
                "contable en un caso de estudio."
            ),
            codigo="EG.5.1.10.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        # Bloque 2
        Destreza(
            description=(
                "Elaborar un mapeo de los requisitos legales básicos para "
                "iniciar actividades de emprendimiento que permitan "
                "formalizarlo."
            ),
            codigo="EG.5.2.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar las obligaciones legales que debe cumplir un "
                "emprendedor como elemento fundamental para la operación del "
                "emprendimiento."
            ),
            codigo="EG.5.2.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y argumentar la importancia del pago de las "
                "obligaciones sociales y tributarias a la autoridad "
                "respectiva, como retribución de los servicios públicos "
                "utilizados e incentivos fiscales recibidos, para fomentar "
                "una cultura tributaria."
            ),
            codigo="EG.5.2.3.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar los conocimientos tributarios en el llenado de los "
                "formularios básicos del SRI (RISE, IVA e Impuesto a la "
                "Renta)."
            ),
            codigo="EG.5.2.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        # Bloque 3
        Destreza(
            description=(
                "Proponer y definir productos o servicios determinados por "
                "las necesidades de su entorno."
            ),
            codigo="EG.5.3.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y explicar los componentes del diseño de la "
                "investigación de campo para obtener información certera "
                "sobre el tema que se desee investigar o profundizar."
            ),
            codigo="EG.5.3.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Diseñar los instrumentos de investigación que se aplicarán "
                "para obtener información de campo que permita direccionar "
                "las ideas del emprendimiento."
            ),
            codigo="EG.5.3.3.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Ejecutar una investigación de campo entre los clientes "
                "potenciales/usuarios determinados, para establecer las "
                "necesidades de la zona geográfica, de tal manera que se "
                "determinen las ideas potenciales de emprendimiento."
            ),
            codigo="EG.5.3.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Describir los conocimientos estadísticos básicos para "
                "tabular los datos recabados en una investigación de campo."
            ),
            codigo="EG.5.3.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Presentar la información obtenida en una investigación de "
                "campo de forma resumida y concisa, en función de su "
                "utilidad para la toma de decisiones."
            ),
            codigo="EG.5.3.6.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Analizar estadísticamente la información de mercado (oferta "
                "y demanda) a partir de la representación gráfica de los "
                "datos procesados en tablas, gráficas, histogramas, cálculo "
                "de frecuencias, diagramas, estudios de medidas de tendencia "
                "central (media, mediana, moda)."
            ),
            codigo="EG.5.3.7.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Utilizar metodologías para interpretar datos estadísticos "
                "como fundamento para la toma de decisiones y la selección "
                "de las ideas de emprendimiento con mayor probabilidad de "
                "éxito."
            ),
            codigo="EG.5.3.8.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        # Bloque 4
        Destreza(
            description=(
                "Aplicar en un emprendimiento los elementos básicos de los "
                "principios de administración (planeación, organización, "
                "integración, dirección y control), para generar las "
                "habilidades directivas que el emprendedor requiere."
            ),
            codigo="EG.5.4.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Desarrollar criterios sobre administración para generar "
                "eficacia en los emprendimientos."
            ),
            codigo="EG.5.4.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar, valorar e implementar el concepto de "
                "“responsabilidad social” en el desarrollo de "
                "emprendimientos, como elemento fundamental para la "
                "generación de emprendimientos de carácter social."
            ),
            codigo="EG.5.4.3.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Analizar conceptos básicos de economía (“inflación”, "
                "“oferta”, “demanda”, “mercado”, “empleo”, etc.) con el fin "
                "de establecer su impacto en las decisiones relativas al "
                "emprendimiento."
            ),
            codigo="EG.5.4.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar principios básicos de microeconomía en el "
                "desarrollo de emprendimientos, como elemento para la toma "
                "de decisiones."
            ),
            codigo="EG.5.4.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Analizar y aplicar los conceptos de “ingresos y costos "
                "marginales” en un proyecto de emprendimiento (costos "
                "hundidos) y su impacto en la rentabilidad del mismo."
            ),
            codigo="EG.5.4.6.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        # Bloque 5
        Destreza(
            description=(
                "Determinar las necesidades de la zona geográfica y la forma "
                "en que el emprendimiento las satisfaría, como elemento "
                "fundamental para seleccionar una idea de negocio."
            ),
            codigo="EG.5.5.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Exponer, de forma sintética y sencilla, el bien o servicio "
                "seleccionado (idea de emprendimiento) y sus características "
                "principales, de tal manera que, en un lapso muy corto, se "
                "genere impacto entre quienes escuchan."
            ),
            codigo="EG.5.5.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Representar gráficamente la estructura organizacional y las "
                "principales funciones de las diferentes áreas del nuevo "
                "emprendimiento, para identificar los recursos humanos "
                "requeridos."
            ),
            codigo="EG.5.5.3.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Describir detalladamente el proceso operacional o "
                "productivo del nuevo emprendimiento con todos los "
                "componentes y recursos requeridos (humanos y materiales), "
                "para asegurar la fabricación de un producto o la generación "
                "de un servicio de alta calidad."
            ),
            codigo="EG.5.5.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Explicar detalladamente el proceso operacional o productivo "
                "del nuevo emprendimiento con todos los componentes y "
                "recursos requeridos (humanos y materiales), para asegurar "
                "la fabricación de un producto o la generación de un "
                "servicio de alta calidad."
            ),
            codigo="EG.5.5.4.1.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Determinar el monto de los bienes que el nuevo "
                "emprendimiento requiere, para establecer el valor de la "
                "inversión necesaria."
            ),
            codigo="EG.5.5.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Determinar el costo de producción de los bienes o el costo "
                "de los servicios como elemento fundamental para conocer los "
                "gastos que la operación requiere."
            ),
            codigo="EG.5.5.6.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar los costos fijos y variables (directos e "
                "indirectos) en un ejercicio de bienes o servicios."
            ),
            codigo="EG.5.5.7.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y explicar de forma sencilla el segmento de "
                "mercado que se desea alcanzar y sus características, para "
                "establecer estrategias adecuadas para convertirlo en "
                "cliente/usuario."
            ),
            codigo="EG.5.5.8.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Establecer las variables de mercado (producto, precio, "
                "plaza, promoción y personalización) del nuevo "
                "emprendimiento, para satisfacer las necesidades del "
                "segmento de mercado seleccionado."
            ),
            codigo="EG.5.5.9.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y explicar los mecanismos de comunicación "
                "(publicidad y promoción) que se implementará en el futuro "
                "emprendimiento, en función de la caracterización del "
                "segmento de mercado que se aspira alcanzar."
            ),
            codigo="EG.5.5.10.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar metodologías para elaborar una proyección de "
                "ingresos (incluyendo incrementos paulatinos y ciclicidad), "
                "considerando las unidades vendidas y los precios de venta, "
                "para establecer el monto de ingresos del nuevo "
                "emprendimiento."
            ),
            codigo="EG.5.5.11.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Utilizar metodologías para elaborar proyecciones de costos "
                "y gastos, que permitan establecer el monto necesario para "
                "cumplir con estas obligaciones de fondos futuros."
            ),
            codigo="EG.5.5.12.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Utilizar hojas electrónicas para realizar proyecciones "
                "utilizando las TIC de manera que se facilite su "
                "elaboración."
            ),
            codigo="EG.5.5.13.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Elaborar el plan de ingresos y egresos del futuro "
                "emprendimiento, que permita la evaluación cuantitativa del "
                "mismo."
            ),
            codigo="EG.5.5.14.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Calcular el margen de contribución del producto o servicio "
                "del emprendimiento."
            ),
            codigo="EG.5.5.15.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Calcular el punto de equilibrio de una empresa a partir de "
                "la identificación de costos unitarios."
            ),
            codigo="EG.5.5.16.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        # Bloque 6
        Destreza(
            description=(
                "Aplicar técnicas básicas para la evaluación financiera de "
                "un proyecto de emprendimiento (como análisis de "
                "rentabilidad, periodo de recuperación, tasa interna de "
                "retorno y valor actual neto) que permitan tomar decisiones "
                "sobre su implementación, tales como Análisis de "
                "Rentabilidad, Período de Recuperación, Tasa Interna de "
                "Retorno y Valor Actual Neto."
            ),
            codigo="EG.5.6.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque6_emprendimiento
        ),
        Destreza(
            description=(
                "Tomar decisiones sobre la implementación de un proyecto de "
                "emprendimiento basadas en las herramientas de análisis de "
                "rentabilidad, periodo de recuperación, tasa interna de "
                "retorno y valor actual neto."
            ),
            codigo="EG.5.6.1.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque6_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar metodologías para la evaluación cualitativa de un "
                "proyecto de emprendimiento (cobertura de necesidades y "
                "empleo generado) que permitan establecer su factibilidad, "
                "los riesgos existentes y medidas mitigantes propicias."
            ),
            codigo="EG.5.6.2.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque6_emprendimiento
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0034_auto_20180815_0902'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
