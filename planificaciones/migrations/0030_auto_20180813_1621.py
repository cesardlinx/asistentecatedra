from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    matematica = Asignatura.objects.get(name="Matemática")

    # Bloques
    bloque1 = BloqueCurricular.objects.get(name="Álgebra y funciones")
    bloque2 = BloqueCurricular.objects.get(name="Geometría y medida")
    bloque3 = BloqueCurricular.objects.get(name="Estadística y probabilidad")

    # Subniveles
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Superior
        # Bloque 1
        Destreza(
            description=(
                "Reconocer los elementos del conjunto de números enteros Z, "
                "ejemplificando situaciones reales en las que se utilizan "
                "los números enteros negativos."
            ),
            codigo="M.4.1.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Establecer relaciones de orden en un conjunto de números "
                "enteros, utilizando la recta numérica y la simbología"
                "matemática (=, <, ≤, >, ≥)."
            ),
            codigo="M.4.1.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Operar en Z (adición, sustracción, multiplicación) de forma "
                "numérica, aplicando el orden de operación."
            ),
            codigo="M.4.1.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Deducir y aplicar las propiedades algebraicas (adición y "
                "multiplicación) de los números enteros en operaciones "
                "numéricas."
            ),
            codigo="M.4.1.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular la potencia de números enteros con exponentes "
                "naturales."
            ),
            codigo="M.4.1.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular raíces de números enteros no negativos que "
                "intervienen en expresiones matemáticas."
            ),
            codigo="M.4.1.6.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar operaciones combinadas en Z aplicando el orden de "
                "operación, y verificar resultados utilizando la tecnología."
            ),
            codigo="M.4.1.7.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Expresar enunciados simples en lenguaje matemático "
                "(algebraico) para resolver problemas."
            ),
            codigo="M.4.1.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades algebraicas (adición y "
                "multiplicación) de los números enteros en la suma de "
                "monomios homogéneos y la multiplicación de términos "
                "algebraicos."
            ),
            codigo="M.4.1.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver ecuaciones de primer grado con una incógnita en Z "
                "en la solución de problemas."
            ),
            codigo="M.4.1.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver inecuaciones de primer grado con una incógnita en "
                "Z, de manera analítica, en la solución de ejercicios "
                "numéricos y problemas."
            ),
            codigo="M.4.1.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de aplicación con enunciados "
                "que involucren ecuaciones o inecuaciones de primer grado "
                "con una incógnita en Z, e interpretar y juzgar la validez "
                "de las soluciones obtenidas dentro del contexto del "
                "problema."
            ),
            codigo="M.4.1.12.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el conjunto de los números racionales Q e "
                "identificar sus elementos."
            ),
            codigo="M.4.1.13.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar y reconocer los números racionales como un "
                "número decimal y/o como una fracción."
            ),
            codigo="M.4.1.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de orden en un conjunto de números "
                "racionales utilizando la recta numérica y la simbología"
                "matemática (=, <, ≤, >, ≥)."
            ),
            codigo="M.4.1.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Operar en Q (adición y multiplicación) resolviendo "
                "ejercicios numéricos."
            ),
            codigo="M.4.1.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades algebraicas para la suma y la "
                "multiplicación de números racionales en la solución de "
                "ejercicios numéricos."
            ),
            codigo="M.4.1.17.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular potencias de números racionales con exponentes "
                "enteros."
            ),
            codigo="M.4.1.18.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular raíces de números racionales no negativos en la "
                "solución de ejercicios numéricos (con operaciones "
                "combinadas) y algebraicos, atendiendo la jerarquía de la "
                "operación."
            ),
            codigo="M.4.1.19.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver ecuaciones de primer grado con una incógnita en Q "
                "en la solución de problemas sencillos."
            ),
            codigo="M.4.1.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver inecuaciones de primer grado con una incógnita en "
                "Q de manera algebraica."
            ),
            codigo="M.4.1.21.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de aplicación con enunciados "
                "que involucren ecuaciones o inecuaciones de primer grado "
                "con una incógnita en Q, e interpretar y juzgar la validez "
                "de las soluciones obtenidas dentro del contexto del "
                "problema."
            ),
            codigo="M.4.1.22.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer polinomios de grados 1 y 2."
            ),
            codigo="M.4.1.23.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Operar con polinomios de grado ≤2 (adición y producto por "
                "escalar) en ejercicios numéricos y algebraicos."
            ),
            codigo="M.4.1.24.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reescribir polinomios de grado 2 con la multiplicación de "
                "polinomios de grado 1."
            ),
            codigo="M.4.1.25.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el conjunto de los números irracionales e "
                "identificar sus elementos."
            ),
            codigo="M.4.1.26.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Simplificar expresiones numéricas aplicando las reglas de "
                "los radicales."
            ),
            codigo="M.4.1.27.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el conjunto de los números reales R e identificar "
                "sus elementos."
            ),
            codigo="M.4.1.28.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aproximar números reales a números decimales para resolver "
                "problemas."
            ),
            codigo="M.4.1.29.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de orden en un conjunto de números "
                "reales utilizando la recta numérica y la simbología"
                "matemática (=, <, ≤, >, ≥)."
            ),
            codigo="M.4.1.30.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular adiciones y multiplicaciones con números reales y "
                "con términos algebraicos aplicando propiedades en R "
                "(propiedad distributiva de la suma con respecto al "
                "producto)."
            ),
            codigo="M.4.1.31.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular expresiones numéricas y algebraicas usando las "
                "operaciones básicas y las propiedades algebraicas en R."
            ),
            codigo="M.4.1.32.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y calcular productos notables e identificar "
                "factores de expresiones algebraicas."
            ),
            codigo="M.4.1.33.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las potencias de números reales con exponentes "
                "enteros para la notación científica."
            ),
            codigo="M.4.1.34.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular raíces cuadradas de números reales no negativos y "
                "raíces cúbicas de números reales, aplicando las propiedades "
                "en R."
            ),
            codigo="M.4.1.35.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reescribir expresiones numéricas o algebraicas con raíces "
                "en el denominador utilizando propiedades en R "
                "(racionalización)."
            ),
            codigo="M.4.1.36.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar las raíces como potencias con exponentes "
                "racionales para calcular potencias de números reales no "
                "negativos con exponentes racionales en R."
            ),
            codigo="M.4.1.37.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver ecuaciones de primer grado con una incógnita en R "
                "para resolver problemas sencillos."
            ),
            codigo="M.4.1.38.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar un intervalo en R de manera algebraica y "
                "gráfica, y reconocer el intervalo como la solución de una "
                "inecuación de primer grado con una incógnita en R."
            ),
            codigo="M.4.1.39.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver de manera geométrica una inecuación lineal con dos "
                "incógnitas en el plano cartesiano sombreando la solución."
            ),
            codigo="M.4.1.40.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver un sistema de inecuaciones lineales con dos "
                "incógnitas de manera gráfica (en el plano) y reconocer la "
                "zona común sombreada como solución del sistema."
            ),
            codigo="M.4.1.41.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular el producto cartesiano entre dos conjuntos para "
                "definir relaciones binarias (subconjuntos), "
                "representándolas con pares ordenados."
            ),
            codigo="M.4.1.42.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar relaciones reflexivas, simétricas, transitivas "
                "y de equivalencia sobre un subconjunto del producto "
                "cartesiano."
            ),
            codigo="M.4.1.43.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer funciones de manera algebraica y de "
                "manera gráfica, con diagramas de Venn, determinando su "
                "dominio y recorrido en Z."
            ),
            codigo="M.4.1.44.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar funciones de forma gráfica, con barras, "
                "bastones y diagramas circulares, y analizar sus "
                "características."
            ),
            codigo="M.4.1.45.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Elaborar modelos matemáticos sencillos como funciones en la "
                "solución de problemas."
            ),
            codigo="M.4.1.46.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer funciones lineales en Z, con base en "
                "tablas de valores, de formulación algebraica y/o "
                "representación gráfica, con o sin el uso de la tecnología."
            ),
            codigo="M.4.1.47.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer funciones crecientes y decrecientes a partir de "
                "su representación gráfica o tabla de valores."
            ),
            codigo="M.4.1.48.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer una función real identificando sus "
                "características: dominio, recorrido, monotonía, cortes con "
                "los ejes."
            ),
            codigo="M.4.1.49.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer una función lineal de manera algebraica "
                "y gráfica (con o sin el empleo de la tecnología), e "
                "identificar su monotonía a partir de la gráfica o su "
                "pendiente."
            ),
            codigo="M.4.1.50.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer funciones potencia con n=1, 2, 3, "
                "representarlas de manera gráfica e identificar su "
                "monotonía."
            ),
            codigo="M.4.1.51.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar e interpretar modelos matemáticos con funciones "
                "lineales, y resolver problemas."
            ),
            codigo="M.4.1.52.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la recta como la solución gráfica de una ecuación "
                "lineal con dos incógnitas en R."
            ),
            codigo="M.4.1.53.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la intersección de dos rectas como la solución "
                "gráfica de un sistema de dos ecuaciones lineales con dos "
                "incógnitas."
            ),
            codigo="M.4.1.54.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver un sistema de dos ecuaciones lineales con dos "
                "incógnitas de manera algebraica, utilizando los métodos de "
                "determinante (Cramer), de igualación, y de eliminación "
                "gaussiana."
            ),
            codigo="M.4.1.55.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de texto con enunciados que "
                "invo- lucren funciones lineales y sistemas de dos "
                "ecuaciones lineales con dos incógnitas; e interpretar y "
                "juzgar la validez de las soluciones obtenidas dentro del "
                "contexto del problema."
            ),
            codigo="M.4.1.56.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir y reconocer una función cuadrática de manera "
                "algebraica y gráfica, determinando sus características: "
                "dominio, recorrido, monotonía, máximos, mínimos y paridad."
            ),
            codigo="M.4.1.57.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer los ceros de la función cuadrática como la "
                "solución de la ecuación de segundo grado con una incógnita."
            ),
            codigo="M.4.1.58.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver la ecuación de segundo grado con una incógnita de "
                "manera analítica (por factoreo, completación de cuadrados, "
                "fórmula binomial) en la solución de problemas."
            ),
            codigo="M.4.1.59.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de las raíces de la ecuación de "
                "segundo grado con una incógnita para resolver problemas."
            ),
            codigo="M.4.1.60.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver (con apoyo de las TIC) y plantear problemas con "
                "enunciados que involucren modelos con funciones "
                "cuadráticas, e interpretar y juzgar la validez de las "
                "soluciones obtenidas dentro del contexto del problema."
            ),
            codigo="M.4.1.61.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Definir y reconocer proposiciones simples a las que se "
                "puede asignar un valor de verdad para relacionarlas entre "
                "sí con conectivos lógicos: negación, disyunción, "
                "conjunción, condicionante y bicondicionante; y formar "
                "proposiciones compuestas (que tienen un valor de verdad que "
                "puede ser determinado)."
            ),
            codigo="M.4.2.1.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir y reconocer una tautología para la construcción de "
                "tablas de verdad."
            ),
            codigo="M.4.2.2.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Conocer y aplicar las leyes de la lógica proposicional en "
                "la solución de problemas."
            ),
            codigo="M.4.2.3.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir y reconocer conjuntos y sus características para "
                "operar con ellos (unión, intersección, diferencia, "
                "complemento) de forma gráfica y algebraica."
            ),
            codigo="M.4.2.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir e identificar figuras geométricas semejantes, de "
                "acuerdo a las medidas de los ángulos y a la relación entre "
                "las medidas de los lados, determinando el factor de escala "
                "entre las figuras (teorema de Thales)."
            ),
            codigo="M.4.2.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar la semejanza en la construcción de figuras "
                "semejantes, el cálculo de longitudes y la solución de "
                "problemas geométricos."
            ),
            codigo="M.4.2.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer y trazar líneas de simetría en figuras "
                "geométricas para completarlas o resolverlas."
            ),
            codigo="M.4.2.7.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Clasificar y construir triángulos, utilizando regla y "
                "compás, bajo condiciones de ciertas medidas de lados y/o "
                "ángulos."
            ),
            codigo="M.4.2.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir e identificar la congruencia de dos triángulos de "
                "acuerdo a criterios que consideran las medidas de sus lados "
                "y/o sus ángulos."
            ),
            codigo="M.4.2.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar criterios de semejanza para reconocer triángulos "
                "rectángulos semejantes y resolver problemas."
            ),
            codigo="M.4.2.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el perímetro y el área de triángulos en la "
                "resolución de problemas."
            ),
            codigo="M.4.2.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir y dibujar medianas y baricentro, mediatrices y "
                "circuncentro, alturas y ortocentro, bisectrices e incentro "
                "en un triángulo."
            ),
            codigo="M.4.2.12.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Plantear y resolver problemas que impliquen la "
                "identificación de las características de las rectas y "
                "puntos notables de un triángulo."
            ),
            codigo="M.4.2.13.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Demostrar el teorema de Pitágoras utilizando áreas de "
                "regiones rectangulares."
            ),
            codigo="M.4.2.14.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar el teorema de Pitágoras en la resolución de "
                "triángulos rectángulos."
            ),
            codigo="M.4.2.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Definir e identificar las relaciones trigonométricas en el "
                "triángulo rectángulo (seno, coseno, tangente) para resolver "
                "numéricamente triángulos rectángulos."
            ),
            codigo="M.4.2.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas que involucren triángulos "
                "rectángulos en contextos reales, e interpretar y juzgar la "
                "validez de las soluciones obtenidas dentro del contexto del "
                "problema."
            ),
            codigo="M.4.2.17.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el área de polígonos regulares por descomposición "
                "en triángulos."
            ),
            codigo="M.4.2.18.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar la descomposición en triángulos en el cálculo de "
                "áreas de figuras geométricas compuestas."
            ),
            codigo="M.4.2.19.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Construir pirámides, prismas, conos y cilindros a partir de "
                "patrones en dos dimensiones (redes), para calcular el área "
                "lateral y total de estos cuerpos geométricos."
            ),
            codigo="M.4.2.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el volumen de pirámides, prismas, conos y "
                "cilindros aplicando las fórmulas respectivas."
            ),
            codigo="M.4.2.21.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Resolver problemas que impliquen el cálculo de volúmenes de "
                "cuerpos compuestos (usando la descomposición de cuerpos)."
            ),
            codigo="M.4.2.22.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Organizar datos procesados en tablas de frecuencias para "
                "definir la función asociada, y representarlos gráficamente "
                "con ayuda de las TIC."
            ),
            codigo="M.4.3.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Organizar datos no agrupados (máximo 20) y datos "
                "agrupados(máximo 50) en tablas de distribución de "
                "frecuencias: absoluta, relativa, relativa acumulada y "
                "acumulada, para analizar el significado de los datos."
            ),
            codigo="M.4.3.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Representar de manera gráfica, con el uso de la tecnología, "
                "las frecuencias: histograma o gráfico con barras (polígono "
                "de frecuencias), gráfico de frecuencias acumuladas (ojiva), "
                "diagrama circular, en función de analizar datos."
            ),
            codigo="M.4.3.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Definir y aplicar la metodología para realizar un estudio "
                "estadístico: estadística descriptiva."
            ),
            codigo="M.4.3.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Definir y utilizar variables cualitativas y cuantitativas."
            ),
            codigo="M.4.3.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Definir y aplicar niveles de medición: nominal, ordinal, "
                "intervalo y razón."
            ),
            codigo="M.4.3.6.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular e interpretar las medidas de tendencia central "
                "(media, mediana, moda) y medidas de dispersión (rango, "
                "varianza y desviación estándar) de un conjunto de datos en "
                "la solución de problemas."
            ),
            codigo="M.4.3.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Determinar las medidas de posición: cuartiles, deciles, "
                "percentiles, para resolver problemas."
            ),
            codigo="M.4.3.8.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Definir la probabilidad (empírica) y el azar de un evento o "
                "experimento estadístico para determinar eventos o "
                "experimentos independientes."
            ),
            codigo="M.4.3.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Aplicar métodos de conteo (combinaciones y permutaciones) "
                "en el cálculo de probabilidades."
            ),
            codigo="M.4.3.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular el factorial de un número natural y el coeficiente "
                "binomial en el cálculo de probabilidades."
            ),
            codigo="M.4.3.11.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Operar con eventos (unión, intersección, diferencia y "
                "complemento) y aplicar las leyes de De Morgan para calcular "
                "probabilidades en la resolución de problemas."
            ),
            codigo="M.4.3.12.",
            asignatura=matematica,
            subnivel=superior,
            bloque=bloque3
        ),
        # Bachillerato
        # Bloque 1
        Destreza(
            description=(
                "Aplicar las propiedades algebraicas de los números reales "
                "en la resolución de productos notables y en la "
                "factorización de expresiones algebraicas."
            ),
            codigo="M.5.1.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Deducir propiedades algebraicas de la potenciación de "
                "números reales con exponentes enteros en la simplificación "
                "de expresiones numéricas y algebraicas."
            ),
            codigo="M.5.1.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Transformar raíces n-ésimas de un número real en potencias "
                "con exponentes racionales para simplificar expresiones "
                "numéricas y algebraicas."
            ),
            codigo="M.5.1.3.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades algebraicas de los números reales "
                "para resolver fórmulas (Física, Química, Biología), y "
                "ecuaciones que se deriven de dichas fórmulas."
            ),
            codigo="M.5.1.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar la intersección gráfica de dos rectas como "
                "solución de un sistema de dos ecuaciones lineales con dos "
                "incógnitas."
            ),
            codigo="M.5.1.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver analíticamente sistemas de dos ecuaciones lineales "
                "con dos incógnitas utilizando diferentes métodos "
                "(igualación, sustitución, eliminación)."
            ),
            codigo="M.5.1.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de orden de los números reales para "
                "realizar operaciones con intervalos (unión, intersección, "
                "diferencia y complemento), de manera gráfica (en la recta "
                "numérica) y de manera analítica."
            ),
            codigo="M.5.1.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de orden de los números reales para "
                "resolver ecuaciones e inecuaciones de primer grado con una "
                "incógnita y con valor absoluto."
            ),
            codigo="M.5.1.8.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver sistemas de tres ecuaciones lineales con dos "
                "incógnitas (ninguna solución, solución única, infinitas "
                "soluciones) utilizando los métodos de sustitución o "
                "eliminación gaussiana."
            ),
            codigo="M.5.1.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver sistemas de ecuaciones lineales con tres "
                "incógnitas (infinitas soluciones) utilizando los métodos de "
                "sustitución o eliminación gaussiana."
            ),
            codigo="M.5.1.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver sistemas de dos ecuaciones lineales con tres "
                "incógnitas (ninguna solución, solución única, infinitas "
                "soluciones), de manera analítica, utilizando los métodos de "
                "sustitución o eliminación gaussiana."
            ),
            codigo="M.5.1.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Descomponer funciones racionales en fracciones parciales "
                "resolviendo los sistemas de ecuaciones correspondientes."
            ),
            codigo="M.5.1.12.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de aplicación de sistemas de "
                "ecuaciones lineales (hasta tres ecuaciones lineales con "
                "hasta tres incógnitas); interpretar y juzgar la validez de "
                "las soluciones obtenidas dentro del contexto del problema."
            ),
            codigo="M.5.1.13.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el conjunto de matrices M2×2 [R] y sus elementos, "
                "así como las matrices especiales: nula e identidad."
            ),
            codigo="M.5.1.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar las operaciones de adición y producto entre "
                "matrices"
                "M2×2 [R], producto de escalares por matrices M2×2 [R], "
                "potencias de matrices M2×2 [R], aplicando las propiedades de "
                "números reales."
            ),
            codigo="M.5.1.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular el producto de una matriz de M2×2 [R] por un vector "
                "en el plano y analizar su resultado (vector y no matriz)."
            ),
            codigo="M.5.1.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer matrices reales de mxn e identificar las "
                "operaciones que son posibles de realizar entre ellas según "
                "sus dimensiones."
            ),
            codigo="M.5.1.17.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular determinantes de matrices reales cuadradas de "
                "orden 2 y 3 para resolver sistemas de ecuaciones."
            ),
            codigo="M.5.1.18.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular la matriz inversa A-1de una matriz cuadrada A cuyo "
                "determinante sea diferente a 0 por el método de Gauss "
                "(matriz ampliada), para resolver sistemas de ecuaciones "
                "lineales."
            ),
            codigo="M.5.1.19.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Graficar y analizar el dominio, el recorrido, la monotonía, "
                "ceros, extremos y paridad de las diferentes funciones "
                "reales (función afín a trozos, función potencia entera "
                "negativa con n=-1, -2, función raíz cuadrada, función valor "
                "absoluto de la función afín) utilizando TIC."
            ),
            codigo="M.5.1.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar la composición de funciones reales analizando las "
                "características de la función resultante (dominio, "
                "recorrido, monotonía, máximos, mínimos, paridad)."
            ),
            codigo="M.5.1.21.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver (con o sin el uso de la tecnología) problemas o "
                "situaciones, reales o hipotéticas, con el empleo de la "
                "modelización con funciones reales (función afín a trozos, "
                "función potencia entera negativa con n=-1, -2, función raíz "
                "cuadrada, función valor absoluto de la función afín), "
                "identificando las variables significativas presentes y las "
                "relaciones entre ellas; juzgar la pertinencia y validez de "
                "los resultados obtenidos."
            ),
            codigo="M.5.1.22.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer funciones inyectivas, sobreyectivas y biyectivas "
                "para calcular la función inversa (de funciones biyectivas) "
                "comprobando con la composición de funciones."
            ),
            codigo="M.5.1.23.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear aplicaciones de la composición de "
                "funciones reales en problemas reales o hipotéticos."
            ),
            codigo="M.5.1.24.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar las operaciones de adición y producto entre "
                "funciones reales, y el producto de números reales por "
                "funciones reales, aplicando propiedades de los números "
                "reales."
            ),
            codigo="M.5.1.25.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de las raíces de la ecuación de "
                "segundo grado en la factorización de una función "
                "cuadrática."
            ),
            codigo="M.5.1.26.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver ecuaciones que se pueden reducir a ecuaciones de "
                "segundo grado con una incógnita."
            ),
            codigo="M.5.1.27.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar la intersección gráfica de una recta y una "
                "parábola como solución de un sistema de dos ecuaciones: una "
                "cuadrática y otra lineal."
            ),
            codigo="M.5.1.28.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar la intersección gráfica de dos parábolas como "
                "solución de un sistema de dos ecuaciones de segundo grado "
                "con dos incógnitas."
            ),
            codigo="M.5.1.29.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver sistemas de dos ecuaciones con dos incógnitas: una "
                "de primer grado y una de segundo grado; y sistemas de dos "
                "ecuaciones de segundo grado con dos incógnitas, de forma "
                "analítica."
            ),
            codigo="M.5.1.30.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver (con o sin el uso de la tecnología) problemas o "
                "situaciones, reales o hipotéticas, que pueden ser "
                "modelizados con funciones cuadráticas, identificando las "
                "variables significativas presentes y las relaciones entre "
                "ellas; juzgar la pertinencia y validez de los resultados "
                "obtenidos."
            ),
            codigo="M.5.1.31.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular, de manera intuitiva, el límite cuando de una "
                "función cuadrática con el uso de la calculadora como una "
                "distancia entre dos número reales."
            ),
            codigo="M.5.1.32.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular de manera intuitiva la derivada de funciones "
                "cuadráticas, a partir del cociente incremental."
            ),
            codigo="M.5.1.33.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar de manera geométrica (pendiente de la secante) "
                "y física el cociente incremental (velocidad media) de "
                "funciones cuadráticas, con apoyo de las TIC."
            ),
            codigo="M.5.1.34.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar de manera geométrica y física la primera "
                "derivada (pendiente de la tangente, velocidad instantánea) "
                "de funciones cuadráticas, con apoyo de las TIC."
            ),
            codigo="M.5.1.35.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar de manera física la segunda derivada "
                "(aceleración media, aceleración instantánea) de una función "
                "cuadrática, con apoyo de las TIC (calculadora gráfica, "
                "software, applets)."
            ),
            codigo="M.5.1.36.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas, reales o hipotéticos, que "
                "pueden ser modelizados con derivadas de funciones "
                "cuadráticas, identificando las variables significativas "
                "presentes y las relaciones entre ellas; juzgar la "
                "pertinencia y validez de los resultados obtenidos."
            ),
            codigo="M.5.1.37.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer funciones polinomiales de grado n (entero "
                "positivo) con coeficientes reales en diversos ejemplos."
            ),
            codigo="M.5.1.38.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar operaciones de suma, multiplicación y división "
                "entre funciones polinomiales, y multiplicación de números "
                "reales por polinomios, en ejercicios algebraicos de "
                "simplificación."
            ),
            codigo="M.5.1.39.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las operaciones entre polinomios de grados ≤4, "
                "esquema"
                "de Hörner, teorema del residuo y sus respectivas propiedades "
                "para factorizar polinomios de grados ≤4 y reescribir los "
                "polinomios."
            ),
            codigo="M.5.1.40.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver aplicaciones de los polinomios de grados ≤4 en la "
                "informática (sistemas de numeración, conversión de sistema "
                "de numeración binario a decimal y viceversa) en la solución "
                "de problemas."
            ),
            codigo="M.5.1.41.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver problemas o situaciones que pueden ser modelizados "
                "con funciones polinomiales, identificando las variables "
                "significativas presentes y las relaciones entre ellas, y "
                "juzgar la validez y pertinencia de los resultados "
                "obtenidos."
            ),
            codigo="M.5.1.42.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Graficar funciones racionales con cocientes de polinomios "
                "de grado ≤3 en diversos ejemplos, y determinar las "
                "ecuaciones de las asíntotas, si las tuvieran, con ayuda de "
                "la TIC."
            ),
            codigo="M.5.1.43.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Determinar el dominio, rango, ceros, paridad, monotonía, "
                "extremos y asíntotas de funciones racionales con cocientes "
                "de polinomios de grado ≤3 con apoyo de las TIC."
            ),
            codigo="M.5.1.44.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar operaciones de suma y multiplicación entre "
                "funciones racionales y de multiplicación de números reales "
                "por funciones racionales en ejercicios algebraicos, para "
                "simplificar las funciones."
            ),
            codigo="M.5.1.45.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver aplicaciones, problemas o situaciones que pueden "
                "ser modelizados con funciones racionales, identificando las "
                "variables significativas presentes y las relaciones entre "
                "ellas, y juzgar la validez y pertinencia de los resultados "
                "obtenidos con apoyo de las TIC."
            ),
            codigo="M.5.1.46.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular de manera intuitiva la derivada de funciones "
                "polinomiales de grado ≤4 a partir del cociente incremental."
            ),
            codigo="M.5.1.47.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar de manera geométrica (pendiente de la secante) "
                "y física el cociente incremental (velocidad media) de "
                "funciones polinomiales de grado ≤4, con apoyo de las TIC."
            ),
            codigo="M.5.1.48.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar de manera geométrica y física la primera "
                "derivada (pendiente de la tangente, velocidad instantánea) "
                "de funciones polinomiales de grado ≤4, con apoyo de las "
                "TIC."
            ),
            codigo="M.5.1.49.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Interpretar de manera física la segunda derivada "
                "(aceleración media, aceleración instantánea) de una función "
                "polinomial de grado ≤4, para analizar la monotonía, "
                "determinar los máximos y mínimos de estas funciones y "
                "graficarlas con apoyo de las TIC (calculadora gráfica, "
                "software, applets)."
            ),
            codigo="M.5.1.50.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular de manera intuitiva la derivada de funciones "
                "racionales cuyos numeradores y denominadores sean "
                "polinomios de grado ≤2, para analizar la monotonía, "
                "determinar los máximos y mínimos de estas funciones y "
                "graficarlas con apoyo de las TIC (calculadora gráfica, "
                "software, applets)."
            ),
            codigo="M.5.1.51.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver aplicaciones reales o hipotéticas con ayuda de las "
                "derivadas de funciones polinomiales de grado ≤4 y de "
                "funciones racionales cuyos numeradores y denominadores sean "
                "polinomios de grado ≤2, y juzgar la validez y pertinencia "
                "de los resultados obtenidos."
            ),
            codigo="M.5.1.52.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar sucesiones numéricas reales, sucesiones "
                "monótonas y sucesiones definidas por recurrencia a partir "
                "de las fórmulas que las definen."
            ),
            codigo="M.5.1.53.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y calcular uno o varios parámetros de una "
                "progresión (aritmética o geométrica) conocidos otros "
                "parámetros."
            ),
            codigo="M.5.1.54.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar los conocimientos sobre progresiones aritméticas, "
                "progresiones geométricas y sumas parciales finitas de "
                "sucesiones numéricas para resolver aplicaciones, en general "
                "y de manera especial en el ámbito financiero, de las "
                "sucesiones numéricas reales."
            ),
            codigo="M.5.1.55.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver ejercicios numéricos y problemas con la aplicación "
                "de las progresiones aritméticas, geométricas y sumas "
                "parciales finitas de sucesiones numéricas."
            ),
            codigo="M.5.1.56.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer las aplicaciones de las sucesiones numéricas "
                "reales en el ámbito financiero y resolver problemas, juzgar "
                "la validez de las soluciones obtenidas dentro del contexto "
                "del problema."
            ),
            codigo="M.5.1.57.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Emplear progresiones aritméticas, geométricas y sumas "
                "parciales finitas de sucesiones numéricas en el "
                "planteamiento y resolución de problemas de diferentes "
                "ámbitos."
            ),
            codigo="M.5.1.58.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar las operaciones de suma y multiplicación entre "
                "sucesiones numéricas reales y la multiplicación de "
                "escalares por sucesiones numéricas reales aplicando las "
                "propiedades de los números reales."
            ),
            codigo="M.5.1.59.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar sucesiones convergentes y calcular el límite de "
                "la sucesión."
            ),
            codigo="M.5.1.60.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Conocer y aplicar el álgebra de límites de sucesiones "
                "convergentes en la resolución de aplicaciones o problemas "
                "con sucesiones reales en matemática financiera (interés "
                "compuesto), e interpretar y juzgar la validez de las "
                "soluciones obtenidas."
            ),
            codigo="M.5.1.61.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y graficar las funciones escalonadas para "
                "calcular el área encerrada entre la curva y el eje X."
            ),
            codigo="M.5.1.62.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar las operaciones de suma y multiplicación de "
                "funciones escalonadas y de multiplicación de números reales "
                "por funciones escalonadas aplicando las propiedades de los "
                "números reales."
            ),
            codigo="M.5.1.63.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular la integral definida de una función escalonada, "
                "identificar sus propiedades cuando los límites de "
                "integración son iguales y cuando se intercambian los "
                "límites de integración."
            ),
            codigo="M.5.1.64.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar la interpretación geométrica de la integral de una "
                "función escalonada no negativa como la superficie limitada "
                "por la curva y el eje x."
            ),
            codigo="M.5.1.65.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular la integral definida de una función polinomial de "
                "grado ≤4 aproximando el cálculo como una sucesión de "
                "funciones escalonadas."
            ),
            codigo="M.5.1.66.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la derivación y la integración como procesos "
                "inversos."
            ),
            codigo="M.5.1.67.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar el segundo teorema del cálculo diferencial e "
                "integral para el cálculo de la integral definida de una "
                "función polinomial de grado ≤4 (primitiva)."
            ),
            codigo="M.5.1.68.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear aplicaciones geométricas (cálculo de "
                "áreas) y físicas (velocidad media, espacio recorrido) de la "
                "integral definida, e interpretar y juzgar la validez de las "
                "soluciones obtenidas."
            ),
            codigo="M.5.1.69.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Definir las funciones seno, coseno y tangente a partir de "
                "las relaciones trigonométricas en el círculo trigonométrico "
                "(unidad) e identificar sus respectivas gráficas a partir "
                "del análisis de sus características particulares."
            ),
            codigo="M.5.1.70.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y graficar funciones periódicas determinando el "
                "período y amplitud de las mismas, su dominio y recorrido, "
                "monotonía, paridad."
            ),
            codigo="M.5.1.71.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer las funciones trigonométricas (seno, coseno, "
                "tangente, secante, cosecante y cotangente), sus propiedades "
                "y las relaciones existentes entre estas funciones y "
                "representarlas de manera gráfica con apoyo de las TIC "
                "(calculadora gráfica, software, applets)."
            ),
            codigo="M.5.1.72.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y resolver (con apoyo de las TIC) aplicaciones, "
                "problemas o situaciones reales o hipotéticas que pueden ser "
                "modelizados con funciones trigonométricas, identificando "
                "las variables significativas presentes y las relaciones "
                "entre ellas, y juzgar la validez y pertinencia de los "
                "resultados obtenidos."
            ),
            codigo="M.5.1.73.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y graficar funciones exponenciales analizando sus "
                "características: monotonía, concavidad y comportamiento al "
                "infinito."
            ),
            codigo="M.5.1.74.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la función logarítmica como la función inversa de "
                "la función exponencial para calcular el logaritmo de un "
                "número y graficarla analizando esta relación para "
                "determinar sus características."
            ),
            codigo="M.5.1.75.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer sucesiones numéricas reales que convergen para "
                "determinar su límite."
            ),
            codigo="M.5.1.76.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de los exponentes y los logaritmos "
                "para resolver ecuaciones e inecuaciones con funciones "
                "exponenciales y logarítmicas, con ayuda de las TIC."
            ),
            codigo="M.5.1.77.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y resolver aplicaciones, problemas o situaciones "
                "reales o hipotéticas que pueden ser modelizados con "
                "funciones exponenciales o logarítmicas, identificando las "
                "variables significativas presentes y las relaciones entre "
                "ellas, y juzgar la validez y pertinencia de los resultados "
                "obtenidos."
            ),
            codigo="M.5.1.78.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Graficar vectores en el plano (coordenadas) identificando "
                "sus características: dirección, sentido y longitud o norma."
            ),
            codigo="M.5.2.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular la longitud o norma (aplicando el teorema de "
                "Pitágoras) para establecer la igualdad entre dos vectores."
            ),
            codigo="M.5.2.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Sumar, restar vectores y multiplicar un escalar por un "
                "vector de forma geométrica y de forma analítica, aplicando "
                "propiedades de los números reales y de los vectores en el "
                "plano."
            ),
            codigo="M.5.2.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de aplicaciones geométricas y "
                "físicas (posición, velocidad, aceleración, fuerza, entre "
                "otras) de los vectores en el plano, e interpretar y juzgar "
                "la validez de las soluciones obtenidas dentro del contexto "
                "del problema."
            ),
            codigo="M.5.2.4.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar las operaciones de adición entre elementos de R2 y "
                "de producto por un número escalar de manera geométrica y "
                "analítica aplicando propiedades de los números reales."
            ),
            codigo="M.5.2.5.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer los vectores como elementos geométricos de R2."
            ),
            codigo="M.5.2.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el producto escalar entre dos vectores y la norma "
                "de un vector para determinar la distancia entre dos puntos "
                "A y B en R2 como la norma del vector."
            ),
            codigo="M.5.2.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer que dos vectores son ortogonales cuando su "
                "producto escalar es cero, y aplicar el teorema de Pitágoras "
                "para resolver y plantear aplicaciones geométricas con "
                "operaciones y elementos de R2, apoyándose en el uso de las "
                "TIC (software como Geogebra, calculadora gráfica, applets "
                "en Internet)."
            ),
            codigo="M.5.2.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Escribir y reconocer la ecuación vectorial y paramétrica de "
                "una recta a partir de un punto de la recta y un vector "
                "dirección, o a partir de dos puntos de la recta."
            ),
            codigo="M.5.2.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar la pendiente de una recta a partir de la "
                "ecuación vectorial de la recta, para escribir la ecuación "
                "cartesiana de la recta y la ecuación general de la recta."
            ),
            codigo="M.5.2.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Determinar la posición relativa de dos rectas en R2 (rectas "
                "paralelas, que se cortan, perpendiculares) en la resolución "
                "de problemas (por ejemplo: trayectoria de aviones o de "
                "barcos para determinar si se interceptan)."
            ),
            codigo="M.5.2.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular la distancia de un punto P a una recta (como la "
                "longitud del vector formado por el punto P y la proyección "
                "perpendicular del punto en la recta P´, utilizando la "
                "condición de ortogonalidad del vector dirección de la recta "
                "y el vector ) en la resolución de problemas (distancia "
                "entre dos rectas paralelas)."
            ),
            codigo="M.5.2.12.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Determinar la ecuación de la recta bisectriz de un ángulo "
                "como aplicación de la distancia de un punto a una recta."
            ),
            codigo="M.5.2.13.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Resolver y plantear aplicaciones de la ecuación vectorial, "
                "paramétrica y cartesiana de la recta con apoyo de las TIC."
            ),
            codigo="M.5.2.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar el producto escalar entre dos vectores, la norma de "
                "un vector, la distancia entre dos puntos, el ángulo entre "
                "dos vectores y la proyección ortogonal de un vector sobre "
                "otro, para resolver problemas geométricos, reales o "
                "hipotéticos, en R2."
            ),
            codigo="M.5.2.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Describir la circunferencia, la parábola, la elipse y la "
                "hipérbola como lugares geométricos en el plano."
            ),
            codigo="M.5.2.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Escribir y reconocer las ecuaciones cartesianas de la "
                "circunferencia, la parábola, la elipse y la hipérbola con "
                "centro en el origen y con centro fuera del origen para "
                "resolver y plantear problemas (por ejemplo, en física: "
                "órbitas planetarias, tiro parabólico, etc.), identificando "
                "la validez y pertinencia de los resultados obtenidos."
            ),
            codigo="M.5.2.17.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar las operaciones de adición entre elementos de R3 y "
                "de producto por un número escalar de manera geométrica y "
                "analítica, aplicando propiedades de los números reales; y "
                "reconocer los vectores como elementos geométricos de R3."
            ),
            codigo="M.5.2.18.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el producto escalar entre dos vectores y la norma "
                "de un vector para determinar la distancia entre dos puntos "
                "A y B en R3 como la norma del vector."
            ),
            codigo="M.5.2.19.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Escribir y reconocer la ecuación vectorial y paramétrica de "
                "una recta a partir de un punto de la recta y un vector "
                "dirección, o a partir de dos puntos de la recta, y "
                "graficarlas en R3."
            ),
            codigo="M.5.2.20.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Determinar la ecuación vectorial de un plano a partir de un "
                "punto del plano y dos vectores dirección; a partir de tres "
                "puntos del plano; a partir de una recta contenida en el "
                "plano y un punto."
            ),
            codigo="M.5.2.21.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Determinar la ecuación de la recta formada como "
                "intersección de dos planos como solución del sistema de "
                "ecuaciones planteado por las ecuaciones de los planos."
            ),
            codigo="M.5.2.22.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Determinar si dos planos son paralelos (cuando no hay "
                "solución) o perpendiculares (si los vectores normales a los "
                "planos son perpendiculares) para resolver aplicaciones "
                "geométricas en R3."
            ),
            codigo="M.5.2.23.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar la divisibilidad de números enteros, el cálculo del "
                "máximo común divisor y del mínimo común múltiplo de un "
                "conjunto de números enteros, y la resolución de ecuaciones "
                "lineales con dos incógnitas (con soluciones enteras no "
                "negativas) en la solución de problemas."
            ),
            codigo="M.5.2.24.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer un subconjunto convexo en R2 y determinar el "
                "conjunto de soluciones factibles, de forma gráfica y "
                "analítica, para resolver problemas de programación lineal "
                "simple (minimización en un conjunto de soluciones factibles "
                "de un funcional lineal definido en R2)."
            ),
            codigo="M.5.2.25.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar un proceso de solución gráfica y analítica del "
                "problema de programación lineal graficando las inecuaciones "
                "lineales, determinando los puntos extremos del conjunto de "
                "soluciones factibles, y encontrar la solución óptima."
            ),
            codigo="M.5.2.26.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Resolver y plantear aplicaciones (un modelo simple de línea "
                "de producción, un modelo en la industria química, un "
                "problema de transporte simplificado), interpretando y "
                "juzgando la validez de las soluciones obtenidas dentro del "
                "contexto del problema."
            ),
            codigo="M.5.2.27.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Calcular e interpretar la media, mediana, moda, rango, "
                "varianza y desviación estándar para datos no agrupados y "
                "agrupados, con apoyo de las TIC."
            ),
            codigo="M.5.3.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de aplicación de las medidas "
                "de tendencia central y de dispersión para datos agrupados, "
                "con apoyo de las TIC."
            ),
            codigo="M.5.3.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Juzgar la validez de las soluciones obtenidas en los "
                "problemas de aplicación de las medidas de tendencia central "
                "y de dispersión para datos agrupados dentro del contexto "
                "del problema, con apoyo de las TIC."
            ),
            codigo="M.5.3.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular e interpretar el coeficiente de variación de un "
                "conjunto de datos (agrupados y no agrupados)."
            ),
            codigo="M.5.3.4.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Determinar los cuantiles (cuartiles, deciles y percentiles) "
                "para datos no agrupados y para datos agrupados."
            ),
            codigo="M.5.3.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Representar en diagramas de caja los cuartiles, mediana, "
                "valor máximo y valor mínimo de un conjunto de datos."
            ),
            codigo="M.5.3.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer los experimentos y eventos en un problema de "
                "texto, y aplicar el concepto de probabilidad y los axiomas "
                "de probabilidad en la resolución de problemas."
            ),
            codigo="M.5.3.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Determinar la probabilidad empírica de un evento repitiendo "
                "el experimento aleatorio tantas veces como sea posible (50, "
                "100… veces), con apoyo de las TIC."
            ),
            codigo="M.5.3.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Realizar operaciones con sucesos: unión, intersección, "
                "diferencia y complemento, leyes de De Morgan, en la "
                "resolución de problemas."
            ),
            codigo="M.5.3.9.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular el factorial de un número natural y el coeficiente "
                "binomial para determinar el binomio de Newton."
            ),
            codigo="M.5.3.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Aplicar los métodos de conteo: permutaciones, "
                "combinaciones, para determinar la probabilidad de eventos "
                "simples y, a partir de ellos, la probabilidad de eventos "
                "compuestos, en la resolución de problemas."
            ),
            codigo="M.5.3.11.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar variables aleatorias de manera intuitiva y de "
                "manera formal como una función real y aplicando la función "
                "aditiva de conjuntos, determinar la función de probabilidad "
                "en la resolución de problemas."
            ),
            codigo="M.5.3.12.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer experimentos en los que se requiere utilizar la "
                "probabilidad condicionada mediante el análisis de la "
                "dependencia de los eventos involucrados, y calcular la "
                "probabilidad de un evento sujeto a varias condiciones "
                "aplicando el teorema de Bayes en la resolución de "
                "problemas."
            ),
            codigo="M.5.3.13.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer variables aleatorias discretas cuyo recorrido es "
                "un conjunto discreto en ejemplos numéricos y experimentos y "
                "la distribución de probabilidad para una variable aleatoria "
                "discreta como una función real a partir del cálculo de "
                "probabilidades acumuladas definidas bajo ciertas "
                "condiciones dadas."
            ),
            codigo="M.5.3.14.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular e interpretar la media, la varianza y la "
                "desviación estándar de una variable aleatoria discreta."
            ),
            codigo="M.5.3.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas que involucren el trabajo con "
                "probabilidades y variables aleatorias discretas."
            ),
            codigo="M.5.3.16.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Juzgar la validez de las soluciones obtenidas en los "
                "problemas que involucren el trabajo con probabilidades y "
                "variables aleatorias discretas dentro del contexto del "
                "problema."
            ),
            codigo="M.5.3.17.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Identificar variables aleatorias discretas en problemas de "
                "texto y reconocer la distribución de Poisson, como ejemplo "
                "de variables aleatorias discretas y sus aplicaciones."
            ),
            codigo="M.5.3.18.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer un experimento de Bernoulli en diferentes "
                "contextos (control de calidad, análisis de datos, entre "
                "otros) y la distribución binomial en problemas de texto, "
                "identificando los valores de p y q."
            ),
            codigo="M.5.3.19.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular probabilidades binomiales con la fórmula (o con el "
                "apoyo de las TIC), la media, la varianza de distribuciones "
                "binomiales, y graficar."
            ),
            codigo="M.5.3.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar las formas de las gráficas de distribuciones "
                "binomiales en ejemplos de aplicación, con el apoyo de las "
                "TIC, y juzgar en contexto la validez y pertinencia de los "
                "resultados obtenidos."
            ),
            codigo="M.5.3.21.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular la covarianza de dos variables aleatorias para "
                "determinar la dependencia lineal (directa, indirecta o no "
                "existente) entre dichas variables aleatorias."
            ),
            codigo="M.5.3.22.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Determinar la recta de regresión lineal que pasa por el "
                "centro de gravedad de la distribución para predecir valores "
                "de la variable dependiente utilizando la recta de regresión "
                "lineal, o calcular otra recta de regresión intercambiando "
                "las variables para predecir la otra variable."
            ),
            codigo="M.5.3.23.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Utilizar el método de mínimos cuadrados para determinar la "
                "recta de regresión en la resolución de problemas "
                "hipotéticos o reales, con apoyo de las TIC."
            ),
            codigo="M.5.3.24.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Juzgar la validez de las soluciones obtenidas en el método "
                "de mínimos cuadrados al determinar la recta de regresión en "
                "la resolución de problemas hipotéticos o reales dentro del "
                "contexto del problema, con el apoyo de las TIC."
            ),
            codigo="M.5.3.25.",
            asignatura=matematica,
            subnivel=bachillerato,
            bloque=bloque3
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0029_auto_20180813_1543'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
