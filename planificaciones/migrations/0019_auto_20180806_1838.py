from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    matematica = Asignatura.objects.get(name='Matemática')

    # Subniveles
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Objetivo.objects.bulk_create([
        # Elemental
        Objetivo(
            description=(
                "Explicar y construir patrones de figuras y numéricos "
                "relacionándolos con la suma, la resta y la multiplicación, "
                "para desarrollar el pensamiento lógico-matemático."
            ),
            codigo='O.M.2.1.',
            subnivel=elemental,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Utilizar objetos del entorno para formar conjuntos, "
                "establecer gráficamente la correspondencia entre sus "
                "elementos y desarrollar la comprensión de modelos "
                "matemáticos."
            ),
            codigo='O.M.2.2.',
            subnivel=elemental,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Integrar concretamente el concepto de número, y reconocer "
                "situaciones del entorno en las que se presenten problemas "
                "que requieran la formulación de expresiones matemáticas "
                "sencillas, para resolverlas, de forma individual o grupal, "
                "utilizando los algoritmos de adivinación, sustracción, "
                "multiplicación y división exacta."
            ),
            codigo='O.M.2.3.',
            subnivel=elemental,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Aplicar estrategias de conteo, procedimientos de cálculos "
                "de suma, resta, multiplicación y divisiones del 0 al 9999, "
                "para resolver de forma colaborativa problemas cotidianos de "
                "su entorno."
            ),
            codigo='O.M.2.4.',
            subnivel=elemental,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Comprender el espacio que lo rodea, valorar lugares "
                "históricos, turísticos y bienes naturales, identificando "
                "como conceptos matemáticos los elementos y propiedades de "
                "cuerpos y figuras geométricas en objetos del entorno."
            ),
            codigo='O.M.2.5.',
            subnivel=elemental,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Resolver situaciones cotidianas que impliquen la medición, "
                "estimación y el cálculo de longitudes, capacidades y masas, "
                "con unidades convencionales y no convencionales de objetos "
                "de su entorno, para una mejor comprensión del espacio que "
                "le rodea, la valoración de su tiempo y el de los otros, y "
                "el fomento de la honestidad e integridad en sus actos."
            ),
            codigo='O.M.2.6.',
            subnivel=elemental,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Participar en proyectos de análisis de información del "
                "entorno inmediato, mediante la recolección y representación "
                "de datos estadísticos en pictogramas y diagramas de barras; "
                "potenciando, así, el pensamiento lógico-matemático y "
                "creativo, al interpretar la información y expresar "
                "conclusiones asumiendo compromisos."
            ),
            codigo='O.M.2.7.',
            subnivel=elemental,
            asignatura=matematica
        ),
        # Media
        Objetivo(
            description=(
                "Utilizar el sistema de coordenadas cartesianas y la "
                "generación de sucesiones con sumas, restas, "
                "multiplicaciones y divisiones, como estrategias para "
                "solucionar problemas del entorno, justificar resultados, "
                "comprender modelos matemáticos y desarrollar el pensamiento "
                "lógico-matemático."
            ),
            codigo='O.M.3.1.',
            subnivel=media,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Participar en equipos de trabajo, en la solución de "
                "problemas de la vida cotidiana, empleando como estrategias "
                "los algoritmos de las operaciones con números naturales, "
                "decimales y fracciones, la tecnología y los conceptos de "
                "proporcionalidad."
            ),
            codigo='O.M.3.2.',
            subnivel=media,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Resolver problemas cotidianos que requieran del cálculo de "
                "perímetros y áreas de polígonos regulares; la estimación y "
                "medición de longitudes, áreas, volúmenes y masas de "
                "objetos; la conversión de unidades; y el uso de la "
                "tecnología, para comprender el espacio donde se "
                "desenvuelve."
            ),
            codigo='O.M.3.3.',
            subnivel=media,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Descubrir patrones geométricos en diversos juegos "
                "infantiles, en edificaciones, en objetos culturales, entre "
                "otros, para apreciar la Matemática y fomentar la "
                "perseverancia en la búsqueda de soluciones ante situaciones "
                "cotidianas."
            ),
            codigo='O.M.3.4.',
            subnivel=media,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Analizar, interpretar y representar información estadística "
                "mediante el empleo de TIC, y calcular medidas de tendencia "
                "central con el uso de información de datos publicados en "
                "medios de comunicación, para así fomentar y fortalecer la "
                "vinculación con la realidad ecuatoriana."
            ),
            codigo='O.M.3.5.',
            subnivel=media,
            asignatura=matematica
        ),
        # Superior
        Objetivo(
            description=(
                "Reconocer las relaciones existentes entre los conjuntos de "
                "números enteros, racionales, irracionales y reales; ordenar "
                "estos números y operar con ellos para lograr una mejor "
                "comprensión de procesos algebraicos y de las funciones "
                "(discretas y continuas); y fomentar el pensamiento lógico y "
                "creativo."
            ),
            codigo='O.M.4.1.',
            subnivel=superior,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Reconocer y aplicar las propiedades conmutativa, "
                "asociativa; las cuatro operaciones básicas; y la "
                "potenciación y radicación para la simplificación de "
                "polinomios, a través de la resolución de problemas."
            ),
            codigo='O.M.4.2.',
            subnivel=superior,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Representar y resolver de manera gráfica (utilizando las "
                "TIC) y analítica ecuaciones e inecuaciones con una "
                "variable; ecuaciones de segundo grado con una variable; y "
                "sistemas de dos ecuaciones lineales con dos incógnitas, "
                "para aplicarlos en la solución de situaciones concretas."
            ),
            codigo='O.M.4.3.',
            subnivel=superior,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Aplicar las operaciones básicas, la radicación y la "
                "potenciación en la resolución de problemas con números "
                "enteros, racionales, irracionales y reales, para "
                "desarrollar el pensamiento lógico y crítico."
            ),
            codigo='O.M.4.4.',
            subnivel=superior,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Aplicar el teorema de Pitágoras para deducir y entender las "
                "relaciones trigonométricas (utilizando las TIC) y las "
                "fórmulas usadas en el cálculo de perímetros, áreas, "
                "volúmenes, ángulos de cuerpos y figuras geométricas, con el "
                "propósito de resolver problemas. Argumentar con lógica los "
                "procesos empleados para alcanzar un mejor entendimiento del "
                "entorno cultural, social y natural; y fomentar y fortalecer "
                "la apropiación y cuidado de los bienes patrimoniales del "
                "país."

            ),
            codigo='O.M.4.5.',
            subnivel=superior,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Aplicar las conversiones de unidades de medida del SI y de "
                "otros sistemas en la resolución de problemas que involucren "
                "perímetro y área de figuras planas, áreas y volúmenes de "
                "cuerpos geométricos, así como diferentes situaciones "
                "cotidianas que impliquen medición, comparación, cálculo y "
                "equivalencia entre unidades."
            ),
            codigo='O.M.4.6.',
            subnivel=superior,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Representar, analizar e interpretar datos estadísticos y "
                "situaciones probabilísticas con el uso de las TIC, para "
                "conocer y comprender mejor el entorno social y económico, "
                "con pensamiento crítico y reflexivo."
            ),
            codigo='O.M.4.7.',
            subnivel=superior,
            asignatura=matematica
        ),
        # Bachillerato
        Objetivo(
            description=(
                "Proponer soluciones creativas a situaciones concretas de la "
                "realidad nacional y mundial mediante la aplicación de las "
                "operaciones básicas de los diferentes conjuntos numéricos, "
                "y el uso de modelos funcionales, algorítmos apropiados, "
                "estratgias y métodos formales y no formales de razonamiento "
                "matemático, que lleven a juzgar con responsabilidad la "
                "validez de procedimientos y los resultados en un contexto."
            ),
            codigo='O.M.5.1.',
            subnivel=bachillerato,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Producir, comunicar y generalizar información, de manera "
                "escrita, verbal, simbólica, gráfica y/o tecnológica, "
                "mediante la aplicación de conocimientos matemáticos y el "
                "manejo organizado, responsable y honesto de las fuentes de "
                "datos, para así comprender otras disciplinas, entender las "
                "necesidades y potencialidades de nuestro país, y tomar "
                "decisiones con responsabilidad social."
            ),
            codigo='O.M.5.2.',
            subnivel=bachillerato,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Desarrollar estrategias individuales y grupales que "
                "permitan un cálculo mental y escrito, exácto o estimado; y "
                "la capacidad de interpretación y solución de situaciones "
                "problemáticas del medio."
            ),
            codigo='O.M.5.3.',
            subnivel=bachillerato,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Valorar el empleo de las TIC para realizar cálculos y "
                "resolver, de manera razonaada y crítica, problemas de la "
                "realidad nacional, argumentando la pertienencia de los "
                "métodos utilizados y juzgando la validez de los resultados."
            ),
            codigo='O.M.5.4.',
            subnivel=bachillerato,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Valorar, sobre la base de un pensamiento crítico, creativo, "
                "reflexivo y lógico, la vinculación de los conocimientos "
                "matemáticos con los de las otras disciplinas científicas y "
                "los saberes acestrales, para así plantear soluciones a "
                "problemas de la realidad y contribuir al desarrollo del "
                "entorno social, natural y cultural."
            ),
            codigo='O.M.5.5.',
            subnivel=bachillerato,
            asignatura=matematica
        ),
        Objetivo(
            description=(
                "Desarrollar la curiosidad y la creatividad a través del uso "
                "de herramientas matemáticas al momento de enfrentar y "
                "solucionar problemas de la realidad nacional, demostrando "
                "actitudes de orden, perseverancia y capacidades de "
                "investigación."
            ),
            codigo='O.M.5.6.',
            subnivel=bachillerato,
            asignatura=matematica
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0018_auto_20180806_1746'),
    ]

    operations = [
        migrations.RunPython(
            create_objetivos, reverse_code=migrations.RunPython.noop)
    ]
