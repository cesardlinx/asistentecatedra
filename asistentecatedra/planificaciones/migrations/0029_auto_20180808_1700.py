from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignatura
    matematica = Asignatura.objects.get(name='Matemática')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    CriterioEvaluacion.objects.bulk_create([
        # Preparatoria
        CriterioEvaluacion(
            description=(
                "Clasifica objetos del entorno, establece sus semejanzas y "
                "diferencias, la ubicación en la que se encuentran en "
                "referencia a sí mismo y a otros objetos, selecciona los "
                "atributos que los caracterizan para construir patrones "
                "sencillos y expresar situaciones cotidianas."
            ),
            codigo="CE.M.1.1.",
            asignatura=matematica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Utiliza el conteo de colecciones de objetos de hasta 20 "
                "unidades el conocimiento de cantidad y los numerales del 0 "
                "al 10 para ordenar, sumar o restar y resolver problemas "
                "sencillos en situaciones significativas."
            ),
            codigo="CE.M.1.2.",
            asignatura=matematica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Utiliza las nociones de longitud, capacidad, volumen y "
                "superficie, peso o temperatura (corto/largo/alto/bajo; "
                "vacío/lleno; grande/pequeño; liviano/pesado; caliente/frío) "
                "para describir y comparar objetos o lugares, identificar "
                "cuerpos (prismas, cilindros y esferas) y figuras "
                "geométricas (triángulos, cuadrados y círculos) en su "
                "entorno; comprende y valora el espacio que lo rodea y "
                "soluciona de forma individual o grupal situaciones "
                "cotidianas."
            ),
            codigo="CE.M.1.3.",
            asignatura=matematica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Resuelve situaciones que requieran de la comparación y "
                "medición(con unidades no convencionales) de longitudes y "
                "pesos de elementos del entorno, la identificación de "
                "monedas, de hasta 10 centavos, y la descripción de sus "
                "actividades cotidianas de acuerdo a secuencias temporales."
            ),
            codigo="CE.M.1.4.",
            asignatura=matematica,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Resuelve problemas cotidianos a través de la aplicación de "
                "procesos de observación de eventos y la recolección, "
                "organización, representación y explicación de información "
                "proveniente de su entorno inmediato."
            ),
            codigo="CE.M.1.5.",
            asignatura=matematica,
            subnivel=preparatoria
        ),
        # Elemental
        CriterioEvaluacion(
            description=(
                "Descubre regularidades matemáticas del entorno inmediato "
                "utilizando los conocimientos de conjuntos y las operaciones "
                "básicas con números naturales, para explicar verbalmente, "
                "en forma ordenada, clara y razonada, situaciones cotidianas "
                "y procedimientos para construir otras regularidades."
            ),
            codigo="CE.M.2.1.",
            asignatura=matematica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Aplica estrategias de conteo, el concepto de número, "
                "expresiones matemáticas sencillas, propiedades de la suma y "
                "la multiplicación, procedimientos de cálculos de suma, "
                "resta, multiplicación sin reagrupación y división "
                "exacta(divisor de una cifra) con números naturales hasta 9 "
                "999, para formular y resolver problemas de la vida "
                "cotidiana del entorno y explicar de forma razonada los "
                "resultados obtenidos."
            ),
            codigo="CE.M.2.2.",
            asignatura=matematica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Emplea elementos básicos de geometría, las propiedades de "
                "cuerpos y figuras geométricas, la medición, estimación y "
                "cálculos de perímetros, para enfrentar situaciones "
                "cotidianas de carácter geométrico."
            ),
            codigo="CE.M.2.3.",
            asignatura=matematica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Resuelve problemas cotidianos sencillos que requieran el "
                "uso de instrumentos de medida y la conversión de unidades, "
                "para determinar la longitud, masa, capacidad y costo de "
                "objetos del entorno, y explicar actividades cotidianas en "
                "función del tiempo."
            ),
            codigo="CE.M.2.4.",
            asignatura=matematica,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Examina datos cuantificables del entorno cercano utilizando "
                "algunos recursos sencillos de recolección y representación "
                "gráfica(pictogramas y diagramas de barras), para "
                "interpretar y comunicar, oralmente y por escrito, "
                "información y conclusiones, asumiendo compromisos."
            ),
            codigo="CE.M.2.5.",
            asignatura=matematica,
            subnivel=elemental
        ),
        # Media
        CriterioEvaluacion(
            description=(
                "Emplea de forma razonada la tecnología, estrategias de "
                "cálculo y los algoritmos de la adición, sustracción, "
                "multiplicación y división de números naturales, en el "
                "planteamiento y solución de problemas, la generación de "
                "sucesiones numéricas, la revisión de procesos y la "
                "comprobación de resultados explica con claridad los "
                "procesos utilizados."
            ),
            codigo="CE.M.3.1.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Aprecia la utilidad de las relaciones de secuencia y orden "
                "entre diferentes conjuntos numéricos, así como el uso de la "
                "simbología matemática, cuando enfrenta, interpreta y "
                "analiza la veracidad de la información numérica que se "
                "presenta en el entorno."
            ),
            codigo="CE.M.3.2.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Aplica la descomposición en factores primos, el cálculo de "
                "MCM, MCD, potencias y raíces con números naturales, y el "
                "conocimiento de medidas de superficie y volumen, para "
                "resolver problemas numéricos, reconociendo críticamente el "
                "valor de la utilidad de la tecnología en los cálculos y la "
                "verificación de resultados valora los argumentos de otros "
                "al expresar la lógica de los procesos realizados."
            ),
            codigo="CE.M.3.3.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Utiliza un determinado conjunto de números para expresar "
                "situaciones reales, establecer equivalencias entre "
                "diferentes sistemas numéricos y juzgar la validez de la "
                "información presentada en diferentes medios."
            ),
            codigo="CE.M.3.4.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Plantea problemas numéricos en los que intervienen números "
                "naturales, decimales o fraccionarios, asociados a "
                "situaciones del entorno para el planteamiento emplea "
                "estrategias de cálculo mental, y para su solución, los "
                "algoritmos de las operaciones y propiedades. Justifica "
                "procesos y emplea de forma crítica la tecnología, como "
                "medio de verificación de resultados."
            ),
            codigo="CE.M.3.5.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Formula y resuelve problemas de proporcionalidad directa e "
                "inversa emplea, como estrategias de solución, el "
                "planteamiento de razones y proporciones provenientes de "
                "tablas, diagramas y gráficas cartesianas y explica de forma "
                "razonada los procesos empleados y la importancia del manejo "
                "honesto y responsable de documentos comerciales."
            ),
            codigo="CE.M.3.6.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Explica las características y propiedades de figuras planas "
                "y cuerpos geométricos, al construirlas en un plano utiliza "
                "como justificación de los procesos de construcción los "
                "conocimientos sobre posición relativa de dos rectas y la "
                "clasificación de ángulos resuelve problemas que implican el "
                "uso de elementos de figuras o cuerpos geométricos y el "
                "empleo de la fórmula de Euler."
            ),
            codigo="CE.M.3.7.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Resuelve problemas cotidianos que impliquen el cálculo del "
                "perímetro y el área de figuras planas; deduce estrategias "
                "de solución con el empleo de fórmulas; explica de manera "
                "razonada los procesos utilizados; verifica resultados y "
                "juzga su validez."
            ),
            codigo="CE.M.3.8.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Emplea, como estrategia para la solución de problemas "
                "geométricos, los procesos de conversión de unidades "
                "justifica la necesidad de expresar unidades en múltiplos o "
                "submúltiplos para optimizar procesos e interpretar datos y "
                "comunicar información."
            ),
            codigo="CE.M.3.9.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Emplea programas informáticos para realizar estudios "
                "estadísticos sencillos formular conclusiones de información "
                "estadística del entorno presentada en gráficos y tablas y "
                "utilizar parámetros estadísticos, como la media, mediana, "
                "moda y rango, en la explicación de conclusiones."
            ),
            codigo="CE.M.3.10.",
            asignatura=matematica,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Emplea combinaciones simples y el cálculo de probabilidades "
                "como estrategia para resolver situaciones cotidianas "
                "explica y justifica de forma crítica y razonada los "
                "procesos y resultados obtenidos en el contexto del "
                "problema."
            ),
            codigo="CE.M.3.11.",
            asignatura=matematica,
            subnivel=media
        ),
        # Superior
        CriterioEvaluacion(
            description=(
                "Emplea las relaciones de orden, las propiedades "
                "algebraicas(adición y multiplicación), las operaciones con "
                "distintos tipos de números(Z, Q, I) y expresiones "
                "algebraicas, para afrontar inecuaciones y ecuaciones con "
                "soluciones de diferentes campos numéricos, y resolver "
                "problemas de la vida real, seleccionando la forma de "
                "cálculo apropiada e interpretando y juzgando las soluciones "
                "obtenidas dentro del contexto del problema analiza la "
                "necesidad del uso de la tecnología."
            ),
            codigo="CE.M.4.1.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Emplea las relaciones de orden, las propiedades algebraicas "
                "de las operaciones en R y expresiones algebraicas, para "
                "afrontar inecuaciones, ecuaciones y sistemas de "
                "inecuaciones con soluciones de diferentes campos numéricos, "
                "y resolver problemas de la vida real, seleccionando la "
                "notación y la forma de cálculo apropiada e interpretando y "
                "juzgando las soluciones obtenidas dentro del contexto del "
                "problema analiza la necesidad del uso de la tecnología."
            ),
            codigo="CE.M.4.2.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Define funciones elementales(función real, función "
                "cuadrática), reconoce sus representaciones, propiedades y "
                "fórmulas algebraicas, analiza la importancia de ejes, "
                "unidades, dominio y escalas, y resuelve problemas que "
                "pueden ser modelados a través de funciones elementales "
                "propone y resuelve problemas que requieran el planteamiento "
                "de sistemas de ecuaciones lineales con dos incógnitas y "
                "ecuaciones de segundo grado juzga la necesidad del uso de "
                "la tecnología."

            ),
            codigo="CE.M.4.3.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Valora la importancia de la teoría de conjuntos para "
                "definir conceptos e interpretar propiedades aplica las "
                "leyes de la lógica proposicional en la solución de "
                "problemas y la elaboración de argumentos lógicos."
            ),
            codigo="CE.M.4.4.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Emplea la congruencia, semejanza, simetría y las "
                "características sobre las rectas y puntos notables, en la "
                "construcción de figuras aplica los conceptos de semejanza "
                "para solucionar problemas de perímetros y áreas de figuras, "
                "considerando como paso previo el cálculo de longitudes. "
                "Explica los procesos de solución de problemas utilizando "
                "como argumento criterios de semejanza, congruencia y las "
                "propiedades y elementos de triángulos. Expresa con claridad "
                "los procesos seguidos y los razonamientos empleados."
            ),
            codigo="CE.M.4.5.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Utiliza estrategias de descomposición en triángulos en el "
                "cálculo de áreas de figuras compuestas, y en el cálculo de "
                "cuerpos compuestos aplica el teorema de Pitágoras y las "
                "relaciones trigonométricas para el cálculo de longitudes "
                "desconocidas de elementos de polígonos o cuerpos "
                "geométricos, como requerimiento previo a calcular áreas de "
                "polígonos regulares, y áreas y volúmenes de cuerpos, en "
                "contextos geométricos o en situaciones reales. Valora el "
                "trabajo en equipo con una actitud flexible, abierta y "
                "crítica."
            ),
            codigo="CE.M.4.6.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Representa gráficamente información estadística, mediante "
                "tablas de distribución de frecuencias y con el uso de la "
                "tecnología. Interpreta y codifica información a través de "
                "gráficas. Valora la claridad, el orden y la honestidad en "
                "el tratamiento y presentación de datos. Promueve el trabajo "
                "colaborativo en el análisis crítico de la información "
                "recibida de los medios de comunicación."
            ),
            codigo="CE.M.4.7.",
            asignatura=matematica,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Analiza y representa un grupo de datos utilizando los "
                "elementos de la estadística descriptiva(variables, "
                "nivelesde medición, medidas de tendencia central, de "
                "dispersión y de posición). Razona sobre los posibles "
                "resultados de un experimento aleatorio sencillo. Calcula "
                "probabilidades aplicando como estrategia técnicas de "
                "conteo, el cálculo del factorial de un número y el "
                "coeficiente binomial, operaciones con conjuntos y las leyes "
                "de De Morgan. Valora la importancia de realizar estudios "
                "estadísticos para comprender el medio y plantear soluciones "
                "a problemas de la vida diaria. Emplea medios tecnológicos, "
                "con creatividad y autonomía, en el desarrollo de procesos "
                "estadísticos. Respeta las ideas ajenas y argumenta "
                "procesos."
            ),
            codigo="CE.M.4.8.",
            asignatura=matematica,
            subnivel=superior
        ),
        # Bachillerato
        CriterioEvaluacion(
            description=(
                "Emplea conceptos básicos de las propiedades algebraicas de "
                "los números reales para optimizar procesos, realizar "
                "simplificaciones y resolver ejercicios de ecuaciones e "
                "inecuaciones, aplicados en contextos reales e hipotéticos."
            ),
            codigo="CE.M.5.1.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Emplea sistemas de ecuaciones 3x3 aplicando diferentes "
                "métodos, incluida la eliminación gaussiana opera con "
                "matrices cuadradas y de orden mxn."
            ),
            codigo="CE.M.5.2.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Opera y emplea funciones reales, lineales, cuadráticas, "
                "polinomiales, exponenciales, logarítmicas y trigonométricas "
                "para plantear situaciones hipotéticas y cotidianas que "
                "puedan resolverse mediante modelos matemáticos comenta la "
                "validez y limitaciones de los procedimientos empleados y "
                "verifica sus resultados mediante el uso de las TIC."
            ),
            codigo="CE.M.5.3.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Reconoce patrones presentes en sucesiones numéricas reales, "
                "monótonas y definidas por recurrencia identifica las "
                "progresiones aritméticas y geométricas y, mediante sus "
                "propiedades y fórmulas, resuelve problemas reales de "
                "matemática financiera e hipotética."
            ),
            codigo="CE.M.5.4.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Aplica el álgebra de límites como base para el cálculo "
                "diferencial e integral, interpreta las derivadas de forma "
                "geométrica y física, y resuelve ejercicios de áreas y "
                "problemas de optimización."
            ),
            codigo="CE.M.5.5.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Emplea vectores geométricos en el plano y operaciones en "
                "R2, con aplicaciones en física y en la ecuación de la recta "
                "utiliza métodos gráficos, analíticos y tecnológicos."
            ),
            codigo="CE.M.5.6.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Efectúa operaciones en el espacio(tres dimensiones) con "
                "vectores, rectas y planos identifica si son paralelos o "
                "perpendiculares, y halla sus intersecciones."
            ),
            codigo="CE.M.5.7.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Aplica los sistemas de inecuaciones lineales y el conjunto "
                "de soluciones factibles para hallar los puntos extremos y "
                "la solución óptima en problemas de programación lineal."
            ),
            codigo="CE.M.5.8.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Emplea la estadística descriptiva para resumir, organizar, "
                "graficar e interpretar datos agrupados y no agrupados."
            ),
            codigo="CE.M.5.9.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Emplea técnicas de conteo y teoría de probabilidades para "
                "calcular la posibilidad de que un determinado evento ocurra "
                "identifica variables aleatorias resuelve problemas con o "
                "sin TIC contrasta los procesos, y discute sus resultados."
            ),
            codigo="CE.M.5.10.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Efectúa procedimientos estadísticos para realizar "
                "inferencias, analizar la distribución binomial y calcular "
                "probabilidades, en diferentes contextos y con ayuda de las "
                "TIC."
            ),
            codigo="CE.M.5.11.",
            asignatura=matematica,
            subnivel=bachillerato
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0028_auto_20180808_1619'),
    ]

    operations = [
        migrations.RunPython(create_criterios)
    ]
