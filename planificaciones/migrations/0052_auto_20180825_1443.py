from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

    # Criterios de evaluación
    criterio1_1 = CriterioEvaluacion.objects.get(codigo="CE.M.1.1.")
    criterio1_2 = CriterioEvaluacion.objects.get(codigo="CE.M.1.2.")
    criterio1_3 = CriterioEvaluacion.objects.get(codigo="CE.M.1.3.")
    criterio1_4 = CriterioEvaluacion.objects.get(codigo="CE.M.1.4.")
    criterio1_5 = CriterioEvaluacion.objects.get(codigo="CE.M.1.5.")
    criterio2_1 = CriterioEvaluacion.objects.get(codigo="CE.M.2.1.")
    criterio2_2 = CriterioEvaluacion.objects.get(codigo="CE.M.2.2.")
    criterio2_3 = CriterioEvaluacion.objects.get(codigo="CE.M.2.3.")
    criterio2_4 = CriterioEvaluacion.objects.get(codigo="CE.M.2.4.")
    criterio2_5 = CriterioEvaluacion.objects.get(codigo="CE.M.2.5.")
    criterio3_1 = CriterioEvaluacion.objects.get(codigo="CE.M.3.1.")
    criterio3_2 = CriterioEvaluacion.objects.get(codigo="CE.M.3.2.")
    criterio3_3 = CriterioEvaluacion.objects.get(codigo="CE.M.3.3.")
    criterio3_4 = CriterioEvaluacion.objects.get(codigo="CE.M.3.4.")
    criterio3_5 = CriterioEvaluacion.objects.get(codigo="CE.M.3.5.")
    criterio3_6 = CriterioEvaluacion.objects.get(codigo="CE.M.3.6.")
    criterio3_7 = CriterioEvaluacion.objects.get(codigo="CE.M.3.7.")
    criterio3_8 = CriterioEvaluacion.objects.get(codigo="CE.M.3.8.")
    criterio3_9 = CriterioEvaluacion.objects.get(codigo="CE.M.3.9.")
    criterio3_10 = CriterioEvaluacion.objects.get(codigo="CE.M.3.10.")
    criterio3_11 = CriterioEvaluacion.objects.get(codigo="CE.M.3.11.")
    criterio4_1 = CriterioEvaluacion.objects.get(codigo="CE.M.4.1.")
    criterio4_2 = CriterioEvaluacion.objects.get(codigo="CE.M.4.2.")
    criterio4_3 = CriterioEvaluacion.objects.get(codigo="CE.M.4.3.")
    criterio4_4 = CriterioEvaluacion.objects.get(codigo="CE.M.4.4.")
    criterio4_5 = CriterioEvaluacion.objects.get(codigo="CE.M.4.5.")
    criterio4_6 = CriterioEvaluacion.objects.get(codigo="CE.M.4.6.")
    criterio4_7 = CriterioEvaluacion.objects.get(codigo="CE.M.4.7.")
    criterio4_8 = CriterioEvaluacion.objects.get(codigo="CE.M.4.8.")
    criterio5_1 = CriterioEvaluacion.objects.get(codigo="CE.M.5.1.")
    criterio5_2 = CriterioEvaluacion.objects.get(codigo="CE.M.5.2.")
    criterio5_3 = CriterioEvaluacion.objects.get(codigo="CE.M.5.3.")
    criterio5_4 = CriterioEvaluacion.objects.get(codigo="CE.M.5.4.")
    criterio5_5 = CriterioEvaluacion.objects.get(codigo="CE.M.5.5.")
    criterio5_6 = CriterioEvaluacion.objects.get(codigo="CE.M.5.6.")
    criterio5_7 = CriterioEvaluacion.objects.get(codigo="CE.M.5.7.")
    criterio5_8 = CriterioEvaluacion.objects.get(codigo="CE.M.5.8.")
    criterio5_9 = CriterioEvaluacion.objects.get(codigo="CE.M.5.9.")
    criterio5_10 = CriterioEvaluacion.objects.get(codigo="CE.M.5.10.")
    criterio5_11 = CriterioEvaluacion.objects.get(codigo="CE.M.5.11.")

    Indicador.objects.bulk_create([
        # Preparatoria
        Indicador(
            description=(
                "Compara y distingue objetos según su color, tamaño, "
                "longitud, textura y forma en situaciones cotidianas (I.2.)"
            ),
            codigo="I.M.1.1.1.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Describe la ubicación de los objetos del entorno (I.3.)"
            ),
            codigo="I.M.1.1.2.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Construye series utilizando objetos del entorno, sonidos, "
                "movimientos, figuras y cuerpos geométricos y agrupaciones "
                "de elementos (I.1., I.4.)"
            ),
            codigo="I.M.1.1.3.",
            criterio_evaluacion=criterio1_1
        ),
        Indicador(
            description=(
                "Establece relaciones de orden y escribe secuencias "
                "numéricas ascendentes y descendentes, con números naturales "
                "del 1 al 10 y con números ordinales, hasta el quinto, para "
                "explicar situaciones cotidianas. (I.3., I.4.)"
            ),
            codigo="I.M.1.2.1.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Resuelve situaciones cotidianas que requieren de la "
                "comparación de colecciones de objetos mediante el uso de "
                "cuantificadores, la adición y sustracción, con números "
                "naturales hasta el 10, y el conteo de colecciones de "
                "objetos hasta el 20. (I.1., I.2.)"
            ),
            codigo="I.M.1.2.2.",
            criterio_evaluacion=criterio1_2
        ),
        Indicador(
            description=(
                "Encuentra, en el entorno y en elementos de su uso personal, "
                "objetos que contienen o son semejantes a los cuerpos y "
                "figuras geométricas, los selecciona de acuerdo a su interés "
                "y comparte con sus compañeros las razones de la selección. "
                "(J.1., S.1., I.4.)"
            ),
            codigo="I.M.1.3.1.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Clasifica objetos del entorno y los agrupa considerando su "
                "tamaño, longitud, capacidad, peso o temperatura y expresa "
                "verbalmente los criterios de la agrupación. (I.2.)"
            ),
            codigo="I.M.1.3.2.",
            criterio_evaluacion=criterio1_3
        ),
        Indicador(
            description=(
                "Utiliza unidades de medida no convencionales y el conteo de "
                "cantidades hasta el 20 para indicar la longitud, peso o el "
                "costo de objetos del entorno y dar solución a situaciones "
                "cotidianas sencillas. (I.2.)"
            ),
            codigo="I.M.1.4.1.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Emplea unidades de tiempo para ordenar secuencias "
                "temporales que describan actividades significativas y sus "
                "actividades cotidianas. (J.3., I.2.)"
            ),
            codigo="I.M.1.4.2.",
            criterio_evaluacion=criterio1_4
        ),
        Indicador(
            description=(
                "Soluciona problemas mediante la organización y "
                "representación de datos estadísticos provenientes de "
                "situaciones cotidianas y de la identificación en eventos "
                "probables y no probables del entorno. (I.2.)"
            ),
            codigo="I.M.1.5.1.",
            criterio_evaluacion=criterio1_5
        ),
        # Elemental
        Indicador(
            description=(
                "Discrimina propiedades de los objetos y obtiene "
                "subconjuntos de un conjunto universo. (S.2.)"
            ),
            codigo="I.M.2.1.1.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Propone patrones y construye series de objetos, figuras y "
                "secuencias numéricas. (I.1.)"
            ),
            codigo="I.M.2.1.2.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Discrimina en diagramas, tablas y una cuadrícula los pares "
                "ordenados del producto cartesiano AxB que cumplen una "
                "relación uno a uno. (I.3., I.4.)"
            ),
            codigo="I.M.2.1.3.",
            criterio_evaluacion=criterio2_1
        ),
        Indicador(
            description=(
                "Completa secuencias numéricas ascendentes o descendentes "
                "con números naturales de hasta cuatro cifras, utilizando "
                "material concreto, simbologías, estrategias de conteo y la "
                "representación en la semirrecta numérica; separa números "
                "pares e impares. (I.3.)"
            ),
            codigo="I.M.2.2.1.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Aplica de manera razonada la composición y descomposición "
                "de unidades, decenas, centenas y unidades de mil, para "
                "establecer relaciones de orden (=, <, >), calcula adiciones "
                "y sustracciones, y da solución a problemas matemáticos "
                "sencillos del entorno. (I.2., S.4.)"
            ),
            codigo="I.M.2.2.2.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Opera utilizando la adición y sustracción con números "
                "naturales de hasta cuatro cifras en el contexto de un "
                "problema matemático del entorno, y emplea las propiedades "
                "conmutativa y asociativa de la adición para mostrar "
                "procesos y verificar resultados. (I.2., I.4.)"
            ),
            codigo="I.M.2.2.3.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Opera utilizando la multiplicación sin reagrupación y la "
                "división exacta (divisor de una cifra) con números "
                "naturales en el contexto de un problema del entorno; usa "
                "reglas y las propiedades conmutativa y asociativa de la "
                "multiplicación para mostrar procesos y verificar "
                "resultados; reconoce mitades y dobles en objetos. (I.2., "
                "I.4.)"
            ),
            codigo="I.M.2.2.4.",
            criterio_evaluacion=criterio2_2
        ),
        Indicador(
            description=(
                "Clasifica, según sus elementos y propiedades, cuerpos y "
                "figuras geométricas. (I.4.)"
            ),
            codigo="I.M.2.3.1.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Identifica elementos básicos de la Geometría en cuerpos y "
                "figuras geométricas. (I.2., S.2.)"
            ),
            codigo="I.M.2.3.2.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Utiliza elementos básicos de la Geometría para dibujar y "
                "describir figuras planas en objetos del entorno. (I.2., "
                "S.2.)"
            ),
            codigo="I.M.2.3.3.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Resuelve situaciones cotidianas que requieran de la "
                "medición y/o estimación del perímetro de figuras "
                "planas.(I.2., I.4.)"
            ),
            codigo="I.M.2.3.4.",
            criterio_evaluacion=criterio2_3
        ),
        Indicador(
            description=(
                "Resuelve situaciones problémicas sencillas que requieran de "
                "la comparación de longitudes y la conversión de unidades. "
                "(I.2.)"
            ),
            codigo="I.M.2.4.1.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Destaca situaciones cotidianas que requieran de la "
                "conversión de unidades monetarias. (J.2., J.3.)"
            ),
            codigo="I.M.2.4.2.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Utiliza las unidades de tiempo y la lectura del reloj "
                "analógico para describir sus actividades cotidianas. (J.2., "
                "I.3.)"
            ),
            codigo="I.M.2.4.3.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Resuelve situaciones problémicas sencillas que requieran de "
                "la comparación de la masa de objetos del entorno, de la "
                "conversión entre kilogramo y gramo, y la identificación de "
                "la libra como unidad de medida de masa. (I.2., I.4.)"
            ),
            codigo="I.M.2.4.4.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Resuelve situaciones problémicas sencillas que requieran de "
                "la estimación y comparación de capacidades y la conversión "
                "entre la unidad de medida de capacidad y sus submúltiplos. "
                "(I.2., I.4.)"
            ),
            codigo="I.M.2.4.5.",
            criterio_evaluacion=criterio2_4
        ),
        Indicador(
            description=(
                "Comunica, representa e interpreta información del entorno "
                "inmediato en tablas de frecuencias y diagramas de barras; "
                "explica conclusiones y asume compromisos. (I.3.,J.4.)"
            ),
            codigo="I.M.2.5.1.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Resuelve situaciones cotidianas que requieran de la "
                "realización de combinaciones simples de hasta tres por tres "
                "elementos. (I.2., I.4.)"
            ),
            codigo="I.M.2.5.2.",
            criterio_evaluacion=criterio2_5
        ),
        Indicador(
            description=(
                "Analiza una experiencia aleatoria en actividades "
                "lúdicas.(I.1.)"
            ),
            codigo="I.M.2.5.3.",
            criterio_evaluacion=criterio2_5
        ),
        # Media
        Indicador(
            description=(
                "Aplica estrategias de cálculo, los algoritmos de adiciones, "
                "sustracciones, multiplicaciones y divisiones con números "
                "naturales, y la tecnología en la construcción de sucesiones "
                "numéricas crecientes y decrecientes, y en la solución de "
                "situaciones cotidianas sencillas. (I.3., I.4.)"
            ),
            codigo="I.M.3.1.1.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Formula y resuelve problemas que impliquen operaciones "
                "combinadas; utiliza el cálculo mental, escrito o la "
                "tecnología en la explicación de procesos de planteamiento, "
                "solución y comprobación. (I.2., I.3.)"
            ),
            codigo="I.M.3.1.2.",
            criterio_evaluacion=criterio3_1
        ),
        Indicador(
            description=(
                "Expresa números naturales de hasta nueve dígitos y números "
                "decimales como una suma de los valores posicionales de sus "
                "cifras, y realiza cálculo mental y estimaciones. (I.3., "
                "I.4.)"
            ),
            codigo="I.M.3.2.1.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Selecciona la expresión numérica y estrategia adecuadas "
                "(material concreto o la semirrecta numérica), para "
                "secuenciar y ordenar un conjunto de números naturales, "
                "fraccionarios y decimales, e interpreta información del "
                "entorno. (I.2., I.4.)"
            ),
            codigo="I.M.3.2.2.",
            criterio_evaluacion=criterio3_2
        ),
        Indicador(
            description=(
                "Aplica la descomposición de factores primos y el cálculo "
                "del MCD y el MCM de números naturales en la resolución de "
                "problemas; expresa con claridad y precisión los resultados "
                "obtenidos. (I.3., I.4.)"
            ),
            codigo="I.M.3.3.1.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Emplea el cálculo y la estimación de raíces cuadradas y "
                "cúbicas, potencias de números naturales, y medidas de "
                "superficie y volumen en el planteamiento y solución de "
                "problemas; discute en equipo y verifica resultados con el "
                "uso responsable de la tecnología. (I.2., S.4.)"
            ),
            codigo="I.M.3.3.2.",
            criterio_evaluacion=criterio3_3
        ),
        Indicador(
            description=(
                "Utiliza números romanos, decimales y fraccionarios para "
                "expresar y comunicar situaciones cotidianas, leer "
                "información de distintos medios y resolver problemas. "
                "(I.3.)"
            ),
            codigo="I.M.3.4.1.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Aplica las equivalencias entre números fraccionarios y "
                "decimales en la resolución de ejercicios y situaciones "
                "reales; decide según la naturaleza del cálculo y el "
                "procedimiento a utilizar. (I.1., I.3.)"
            ),
            codigo="I.M.3.4.2.",
            criterio_evaluacion=criterio3_4
        ),
        Indicador(
            description=(
                "Aplica las propiedades de las operaciones (adición y "
                "multiplicación), estrategias de cálculo mental, algoritmos "
                "de la adición, sustracción, multiplicación y división de "
                "números naturales, decimales y fraccionarios, y la "
                "tecnología, para resolver ejercicios y problemas con "
                "operaciones combinadas. (I.1.)"
            ),
            codigo="I.M.3.5.1.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Formula y resuelve problemas contextualizados; decide los "
                "procedimientos y las operaciones con números naturales, "
                "decimales y fraccionarios a utilizar; y emplea propiedades "
                "de las operaciones (adición y multiplicación), las reglas "
                "de redondeo y la tecnología en la interpretación y "
                "verificación de los resultados obtenidos. (I.2., I.3.)"
            ),
            codigo="I.M.3.5.2.",
            criterio_evaluacion=criterio3_5
        ),
        Indicador(
            description=(
                "Explica situaciones cotidianas significativas relacionadas "
                "con la localización de lugares y magnitudes directa o "
                "inversamente proporcionales, empleando como estrategia la "
                "representación en gráficas cartesianas con números "
                "naturales, decimales o fraccionarios. (I.1., I.2.)"
            ),
            codigo="I.M.3.6.1.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Representa porcentajes como un decimal o una fracción y en "
                "diagramas circulares; y explica, comunica e interpreta "
                "información porcentual del entorno. (I.2.)"
            ),
            codigo="I.M.3.6.2.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Plantea y resuelve problemas de proporcionalidad, y "
                "justifica procesos empleando representaciones gráficas; "
                "verifica resultados y argumenta con criterios razonados la "
                "utilidad de documentos comerciales. (J.4., I.2.)"
            ),
            codigo="I.M.3.6.3.",
            criterio_evaluacion=criterio3_6
        ),
        Indicador(
            description=(
                "Construye, con el uso de material geométrico, triángulos, "
                "paralelogramos y trapecios, a partir del análisis de sus "
                "características y la aplicación de los conocimientos sobre "
                "la posición relativa de dos rectas y las clases de ángulos; "
                "soluciona situaciones cotidianas. (J.1., I.2.)"
            ),
            codigo="I.M.3.7.1.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Reconoce características y elementos de polígonos regulares "
                "e irregulares, poliedros y cuerpos de revolución; los "
                "relaciona con objetos del entorno circundante; y aplica "
                "estos conocimientos en la resolución de situaciones "
                "problema. (J.1., I.2.)"

            ),
            codigo="I.M.3.7.2.",
            criterio_evaluacion=criterio3_7
        ),
        Indicador(
            description=(
                "Deduce, a partir del análisis de los elementos de polígonos "
                "regulares e irregulares y el círculo, fórmulas de perímetro "
                "y área; y las aplica en la solución de problemas "
                "geométricos y la descripción de objetos culturales o "
                "naturales del entorno. (I.2., I.3.)"
            ),
            codigo="I.M.3.8.1.",
            criterio_evaluacion=criterio3_8
        ),
        Indicador(
            description=(
                "Utiliza unidades de longitud, superficie, volumen, masa, "
                "angulares y de tiempo, y los instrumentos adecuados para "
                "realizar mediciones y estimaciones, y resolver situaciones "
                "de la vida real. (J.2., I.2.)"
            ),
            codigo="I.M.3.9.1.",
            criterio_evaluacion=criterio3_9
        ),
        Indicador(
            description=(
                "Resuelve situaciones problemáticas variadas empleando "
                "relaciones y conversiones entre unidades, múltiplos y "
                "submúltiplos, en medidas de tiempo, angulares, de longitud, "
                "superficie, volumen y masa; justifica los procesos "
                "utilizados y comunica información. (I.1., I.2.)"
            ),
            codigo="I.M.3.9.2.",
            criterio_evaluacion=criterio3_9
        ),
        Indicador(
            description=(
                "Construye, con o sin el uso de programas informáticos, "
                "tablas de frecuencias y diagramas estadísticos, para "
                "representar y analizar datos discretos del entorno. (I.3.)"
            ),
            codigo="I.M.3.10.1.",
            criterio_evaluacion=criterio3_10
        ),
        Indicador(
            description=(
                "Analiza, interpreta información y emite conclusiones a "
                "partir del análisis de parámetros estadísticos (media, "
                "mediana, moda, rango) y de datos discretos provenientes del "
                "entorno, con el uso de medios tecnológicos.(I.2., I.3.)"
            ),
            codigo="I.M.3.10.2.",
            criterio_evaluacion=criterio3_10
        ),
        Indicador(
            description=(
                "Resuelve situaciones cotidianas empleando como estrategia "
                "las combinaciones simples. (I.1., I.3.)"
            ),
            codigo="I.M.3.11.1.",
            criterio_evaluacion=criterio3_11
        ),
        Indicador(
            description=(
                "Asigna probabilidades (gráficamente o con fracciones) a "
                "diferentes sucesos, en experiencias aleatorias, y resuelve "
                "situaciones cotidianas. (J.2., I.2.)"
            ),
            codigo="I.M.3.11.2.",
            criterio_evaluacion=criterio3_11
        ),
        # Superior
        Indicador(
            description=(
                "Ejemplifica situaciones reales en las que se utilizan los "
                "números enteros; establece relaciones de orden empleando la "
                "recta numérica; aplica las propiedades algebraicas de los "
                "números enteros en la solución de expresiones con "
                "operaciones combinadas, empleando correctamente la "
                "prioridad de las operaciones; juzga la necesidad del uso de "
                "la tecnología. (I.4.)"
            ),
            codigo="I.M.4.1.1.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Formula y resuelve problemas aplicando las propiedades "
                "algebraicas de los números enteros y el planteamiento y "
                "resolución de ecuaciones e inecuaciones de primer grado con "
                "una incógnita; juzga e interpreta las soluciones obtenidas "
                "dentro del contexto del problema. (I.2.)"
            ),
            codigo="I.M.4.1.2.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Establece relaciones de orden en un conjunto de números "
                "racionales e irracionales, con el empleo de la recta "
                "numérica (representación geométrica); aplica las "
                "propiedades algebraicas de las operaciones (adición y "
                "multiplicación) y las reglas de los radicales en el cálculo "
                "de ejercicios numéricos y algebraicos con operaciones "
                "combinadas; atiende correctamente la jerarquía de las "
                "operaciones. (I.4.)"
            ),
            codigo="I.M.4.1.3.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Formula y resuelve problemas aplicando las propiedades "
                "algebraicas de los números racionales y el planteamiento y "
                "resolución de ecuaciones e inecuaciones de primer grado con "
                "una incógnita. (I.2.)"
            ),
            codigo="I.M.4.1.4.",
            criterio_evaluacion=criterio4_1
        ),
        Indicador(
            description=(
                "Emplea las operaciones con polinomios de grado ≤2 en la "
                "solución de ejercicios numéricos y algebraicos; expresa "
                "polinomios de grado 2 como la multiplicación de polinomios "
                "de grado 1. (I.4.)"
            ),
            codigo="I.M.4.2.1.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Establece relaciones de orden en el conjunto de los números "
                "reales; aproxima a decimales; y aplica las propiedades "
                "algebraicas de los números reales en el cálculo de "
                "operaciones (adición, producto, potencias, raíces) y la "
                "solución de expresiones numéricas (con radicales en el "
                "denominador) y algebraicas (productos notables). (I.4.)"
            ),
            codigo="I.M.4.2.2.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Expresa raíces como potencias con exponentes racionales, y "
                "emplea las potencias de números reales con exponentes "
                "enteros para leer y escribir en notación científica "
                "información que contenga números muy grandes o muy "
                "pequeños. (I.3., I.4.)"
            ),
            codigo="I.M.4.2.3.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Resuelve problemas que requieran de ecuaciones de primer "
                "grado con una incógnita en R; utiliza las distintas "
                "notaciones para los intervalos y su representación gráfica "
                "en la solución de inecuaciones de primer grado y sistemas "
                "de inecuaciones lineales con dos incógnitas de manera "
                "gráfica, en R. (I.1., I.4.)"
            ),
            codigo="I.M.4.2.4.",
            criterio_evaluacion=criterio4_2
        ),
        Indicador(
            description=(
                "Representa como pares ordenados el producto cartesiano de "
                "dos conjuntos, e identifica las relaciones reflexivas, "
                "simétricas, transitivas y de equivalencia de un subconjunto "
                "de dicho producto. (I.4.)"
            ),
            codigo="I.M.4.3.1.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Resuelve problemas mediante la elaboración de modelos "
                "matemáticos sencillos, como funciones; emplea gráficas de "
                "barras, bastones y diagramas circulares para representar "
                "funciones y analizar e interpretar la solución en el "
                "contexto del problema. (I.2.)"
            ),
            codigo="I.M.4.3.2.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Determina el comportamiento (función creciente o "
                "decreciente) de las funciones lineales en Z, basándose en "
                "su formulación algebraica, tabla de valores o en gráficas; "
                "valora el empleo de la tecnología. (I.4.)"
            ),
            codigo="I.M.4.3.3.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Utiliza las TIC para graficar funciones lineales, "
                "cuadráticas y potencia (n=1, 2, 3), y para analizar las "
                "características geométricas de la función lineal (pendiente "
                "e intersecciones), la función potencia (monotonía) y la "
                "función cuadrática (dominio, recorrido, monotonía, máximos, "
                "mínimo, paridad); reconoce cuándo un problema puede ser "
                "modelado utilizando una función lineal o cuadrática, lo "
                "resuelve y plantea otros similares. (J.1., I.4.)"
            ),
            codigo="I.M.4.3.4.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Plantea y resuelve problemas que involucren sistemas de dos "
                "ecuaciones lineales con dos incógnitas, ecuaciones de "
                "segundo grado y la aplicación de las propiedades de las "
                "raíces de la ecuación de segundo grado; juzga la validez de "
                "las soluciones obtenidas en el contexto del problema. "
                "(I.4., J.2.)"
            ),
            codigo="I.M.4.3.5.",
            criterio_evaluacion=criterio4_3
        ),
        Indicador(
            description=(
                "Representa, de forma gráfica y algebraica, las operaciones "
                "de unión, intersección, diferencia y complemento entre "
                "conjuntos; utiliza conectivos lógicos, tautologías y la "
                "lógica proposicional en la solución de problemas, "
                "comunicando resultados y estrategias mediante el "
                "razonamiento lógico. (I.3., I.4.)"
            ),
            codigo="I.M.4.4.1.",
            criterio_evaluacion=criterio4_4
        ),
        Indicador(
            description=(
                "Construye figuras simétricas; resuelve problemas "
                "geométricos que impliquen el cálculo de longitudes con la "
                "aplicación de conceptos de semejanza y la aplicación del "
                "teorema de Tales; justifica procesos aplicando los "
                "conceptos de congruencia y semejanza. (I.1., I.4.)"
            ),
            codigo="I.M.4.5.1.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Construye triángulos dadas algunas medidas de ángulos o "
                "lados; dibuja sus rectas y puntos notables como estrategia "
                "para plantear y resolver problemas de perímetro y área de "
                "triángulos; comunica los procesos y estrategias utilizados. "
                "(I.3.)"
            ),
            codigo="I.M.4.5.2.",
            criterio_evaluacion=criterio4_5
        ),
        Indicador(
            description=(
                "Demuestra el teorema de Pitágoras valiéndose de diferentes "
                "estrategias, y lo aplica en la resolución de ejercicios o "
                "situaciones reales relacionadas a triángulos rectángulos; "
                "demuestra creatividad en los procesos empleados y valora el "
                "trabajo individual o grupal. (I.1., S.4.)"
            ),
            codigo="I.M.4.6.1.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Reconoce y aplica las razones trigonométricas y sus "
                "relaciones en la resolución de triángulos rectángulos y en "
                "situaciones problema de la vida real. (I.3.)"
            ),
            codigo="I.M.4.6.2.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Resuelve problemas geométricos que requieran del cálculo de "
                "áreas de polígonos regulares, áreas y volúmenes de "
                "pirámides, prismas, conos y cilindros; aplica, como "
                "estrategia de solución, la descomposición en triángulos y/o "
                "la de cuerpos geométricos; explica los procesos de solución "
                "empleando la construcción de polígonos regulares y cuerpos "
                "geométricos; juzga la validez de resultados.(I.3., I.4.)"
            ),
            codigo="I.M.4.6.3.",
            criterio_evaluacion=criterio4_6
        ),
        Indicador(
            description=(
                "Interpreta datos agrupados y no agrupados en tablas de "
                "distribución de frecuencias y gráficas estadísticas "
                "(histogramas, polígono de frecuencias, ojiva y/o diagramas "
                "circulares), con el uso de la tecnología; interpreta "
                "funciones y juzga la validez de procedimientos, la "
                "coherencia y la honestidad de los resultados obtenidos. "
                "(J.2., I.3.)"
            ),
            codigo="I.M.4.7.1.",
            criterio_evaluacion=criterio4_7
        ),
        Indicador(
            description=(
                "Utiliza información cuantificable del contexto social; "
                "utiliza variables; aplica niveles de medición; calcula e "
                "interpreta medidas de tendencia central (media, mediana y "
                "moda), de dispersión (rango, varianza y desviación "
                "estándar) y de posición (cuartiles, deciles, percentiles); "
                "analiza críticamente información a través de tablas o "
                "gráficos; resuelve problemas en forma grupal e individual; "
                "y comunica estrategias, opiniones y resultados. (I.4., "
                "S.4.)"
            ),
            codigo="I.M.4.8.1.",
            criterio_evaluacion=criterio4_8
        ),
        Indicador(
            description=(
                "Calcula probabilidades de eventos aleatorios empleando "
                "combinaciones y permutaciones, el cálculo del factorial de "
                "un número y el coeficiente binomial; operaciones con "
                "eventos (unión, intersección, diferencia y complemento) y "
                "las leyes de De Morgan. Valora las diferentes estrategias y "
                "explica con claridad el proceso lógico seguido para la "
                "resolución de problemas. (I.2., I.4.)"
            ),
            codigo="I.M.4.8.2.",
            criterio_evaluacion=criterio4_8
        ),
        # Bachillerato
        Indicador(
            description=(
                "Aplica las propiedades algebraicas de los números reales en "
                "productos notables, factorización, potenciación y "
                "radicación. (I.3.)"
            ),
            codigo="I.M.5.1.1.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Halla la solución de una ecuación de primer grado, con "
                "valor absoluto, con una o dos variables; resuelve "
                "analíticamente una inecuación; expresa su respuesta en "
                "intervalos y la gráfica en la recta numérica; despeja una "
                "variable de una fórmula para aplicarla en diferentes "
                "contextos. (I.2.)"
            ),
            codigo="I.M.5.1.2.",
            criterio_evaluacion=criterio5_1
        ),
        Indicador(
            description=(
                "Resuelve sistemas de ecuaciones mxn con diferentes tipos de "
                "soluciones y empleando varios métodos, y los aplica en "
                "funciones racionales y en problemas de aplicación; juzga la "
                "validez de sus hallazgos. (I.2.)"
            ),
            codigo="I.M.5.2.1.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Opera con matrices de hasta tercer orden, calcula el "
                "determinante, la matriz inversa y las aplica en sistemas de "
                "ecuaciones. (I.3.)"
            ),
            codigo="I.M.5.2.2.",
            criterio_evaluacion=criterio5_2
        ),
        Indicador(
            description=(
                "Grafica funciones reales y analiza su dominio, recorrido, "
                "monotonía, ceros, extremos, paridad; identifica las "
                "funciones afines, potencia, raíz cuadrada, valor absoluto; "
                "reconoce si una función es inyectiva, sobreyectiva o "
                "biyectiva; realiza operaciones con funciones aplicando las "
                "propiedades de los números reales en problemas reales e "
                "hipotéticos. (I.4.)"
            ),
            codigo="I.M.5.3.1.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Representa gráficamente funciones cuadráticas; halla las "
                "intersecciones con los ejes, el dominio, rango, vértice y "
                "monotonía; emplea sistemas de ecuaciones para calcular la "
                "intersección entre una recta y una parábola o dos "
                "parábolas; emplea modelos cuadráticos para resolver "
                "problemas, de manera intuitiva halla un límite y la "
                "derivada; optimiza procesos empleando las TIC. (13, 14)"
            ),
            codigo="I.M.5.3.2.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Reconoce funciones polinomiales de grado n, opera con "
                "funciones polinomiales de grado ≤4 y racionales de grado "
                "≤3; plantea modelos matemáticos para resolver problemas "
                "aplicados a la informática; emplea el teorema de Horner y "
                "el teorema del residuo para factorizar polinomios; con la "
                "ayuda de las TIC, escribe las ecuaciones de las asíntotas, "
                "y discute la validez de sus resultados.(I.3., I.4.)"
            ),
            codigo="I.M.5.3.3.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Halla gráfica y analíticamente el dominio, recorrido, "
                "monotonía, periodicidad, desplazamientos, máximos y mínimos "
                "de funciones trigonométricas para modelar movimientos "
                "circulares y comportamientos de fenómenos naturales, y "
                "discute su pertinencia; emplea la tecnología para "
                "corroborar sus resultados. (J.3., I.2.)"
            ),
            codigo="I.M.5.3.4.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Obtiene la gráfica de una función exponencial a partir de "
                "a^x, mediante traslaciones, homotecias y reflexiones; "
                "concibe la función logarítmica como inversa de la función "
                "exponencial; aplica propiedades de los logaritmos y halla "
                "su dominio, recorrido, asíntotas, intersecciones con los "
                "ejes; las aplica en situaciones reales e hipotéticas, con y "
                "sin apoyo de la tecnología. (I.3.)"
            ),
            codigo="I.M.5.3.5.",
            criterio_evaluacion=criterio5_3
        ),
        Indicador(
            description=(
                "Identifica las sucesiones según sus características y halla "
                "los parámetros desconocidos; aplica progresiones en "
                "aplicaciones cotidianas y analiza el sistema financiero "
                "local, apreciando la importancia de estos conocimientos "
                "para la toma de decisiones asertivas. (J.2.)"
            ),
            codigo="I.M.5.4.1.",
            criterio_evaluacion=criterio5_4
        ),
        Indicador(
            description=(
                "Emplea el concepto de límites en sucesiones convergentes y "
                "sucesiones reales; opera con funciones escalonadas; halla "
                "de manera intuitiva derivadas de funciones polinomiales; "
                "diferencia funciones mediante las respectivas reglas para "
                "resolver problemas de optimización; concibe la integración "
                "como proceso inverso, y realiza conexiones geométricas y "
                "físicas. (I.2.)"
            ),
            codigo="I.M.5.5.1.",
            criterio_evaluacion=criterio5_5
        ),
        Indicador(
            description=(
                "Grafica vectores en el plano; halla su módulo y realiza "
                "operaciones de suma, resta y producto por un escalar; "
                "resuelve problemas aplicados a la Geometría y a la Física. "
                "(I.2.)"
            ),
            codigo="I.M.5.6.1.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Realiza operaciones en el espacio vectorial R2; calcula la "
                "distancia entre dos puntos, el módulo y la dirección de un "
                "vector; reconoce cuando dos vectores son ortogonales; y "
                "aplica este conocimiento en problemas físicos, apoyado en "
                "las TIC. (I.3.)"
            ),
            codigo="I.M.5.6.2.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Determina la ecuación de la recta de forma vectorial y "
                "paramétrica; identifica su pendiente, la distancia a un "
                "punto y la posición relativa entre dos rectas, la ecuación "
                "de una recta bisectriz, sus aplicaciones reales, la validez "
                "de sus resultados y el aporte de las TIC. (I.3.)"
            ),
            codigo="I.M.5.6.3.",
            criterio_evaluacion=criterio5_6
        ),
        Indicador(
            description=(
                "Opera analítica, geométrica y gráficamente, con vectores, "
                "rectas y planos en el espacio; expresa la ecuación de la "
                "recta de forma paramétrica y vectorial; halla mediante tres "
                "puntos dicha ecuación o a partir de la intersección de dos "
                "planos, y determina la ortogonalidad de los mismos, para "
                "efectuar aplicaciones geométricas. (I.2.)"
            ),
            codigo="I.M.5.7.1.",
            criterio_evaluacion=criterio5_7
        ),
        Indicador(
            description=(
                "Utiliza métodos gráficos y analíticos para la resolución de "
                "sistemas de ecuaciones lineales y de inecuaciones, para "
                "determinar el conjunto de soluciones factibles y la "
                "solución óptima de un problema de programación lineal. "
                "(I.3.)"
            ),
            codigo="I.M.5.8.1.",
            criterio_evaluacion=criterio5_8
        ),
        Indicador(
            description=(
                "Calcula, con y sin apoyo de las TIC, las medidas de "
                "centralización y dispersión para datos agrupados y no "
                "agrupados; representa la información en gráficos "
                "estadísticos apropiados y los interpreta, juzgando su "
                "validez. (J.2.,I.3.)"
            ),
            codigo="I.M.5.9.1.",
            criterio_evaluacion=criterio5_9
        ),
        Indicador(
            description=(
                "Identifica los experimentos y eventos de un problema y "
                "aplica las reglas de adición, complemento y producto de "
                "manera pertinente; se apoya en las técnicas de conteo y en "
                "la tecnología para el cálculo de probabilidades, y juzga la "
                "validez de sus hallazgos de acuerdo a un determinado "
                "contexto. (I.4.)"
            ),
            codigo="I.M.5.10.1.",
            criterio_evaluacion=criterio5_10
        ),
        Indicador(
            description=(
                "Identifica variables aleatorias discretas y halla la media, "
                "varianza y desviación típica; reconoce un experimento de "
                "Bernoulli y la distribución binomial para emplearlos en la "
                "resolución de problemas cotidianos y el cálculo de "
                "probabilidades; realiza gráficos con el apoyo de las TIC. "
                "(I.3.)"
            ),
            codigo="I.M.5.10.2.",
            criterio_evaluacion=criterio5_10
        ),
        Indicador(
            description=(
                "Grafica un diagrama de dispersión y la recta de dispersión "
                "para analizar la relación entre dos variables; calcula el "
                "coeficiente de correlación para interpretar si dicha "
                "relación es nula, débil, moderada, fuerte o perfecta; "
                "realiza un análisis bidimensional y, mediante la recta de "
                "regresión, efectúa predicciones, justificando la validez de "
                "sus hallazgos y su importancia para la toma de decisiones "
                "asertivas. (J.2., I.3.)"
            ),
            codigo="I.M.5.11.1.",
            criterio_evaluacion=criterio5_11
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0051_auto_20180825_1409'),
    ]

    operations = [
        migrations.RunPython(create_indicadores,
                             reverse_code=migrations.RunPython.noop)
    ]
