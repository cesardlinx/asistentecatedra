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
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')

    Destreza.objects.bulk_create([
        # Preparatoria
        Destreza(
            description=(
                "Reconocer los colores primarios: rojo, amarillo y azul; los "
                "colores blanco y negro y los colores secundarios, en "
                "objetos del entorno."
            ),
            codigo="M.1.4.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer la posición de objetos del entorno: derecha, "
                "izquierda."
            ),
            codigo="M.1.4.2.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer la derecha e izquierda en los demás."
            ),
            codigo="M.1.4.3.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Distinguir la ubicación de objetos del entorno según las "
                "nociones arriba/abajo, delante/atrás y encima/debajo."
            ),
            codigo="M.1.4.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer las semejanzas y diferencias entre los objetos "
                "del entorno de acuerdo a su forma y sus características "
                "físicas (color, tamaño y longitud)."
            ),
            codigo="M.1.4.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Agrupar colecciones de objetos del entorno según sus "
                "características físicas: color, tamaño (grande/pequeño), "
                "longitud (alto/bajo y largo/corto)."
            ),
            codigo="M.1.4.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Discriminar texturas entre objetos del entorno: liso, "
                "áspero, suave, duro, rugoso, delicado."
            ),
            codigo="M.1.4.7.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Describir y reproducir patrones con objetos del entorno por "
                "color, forma, tamaño, longitud o con siluetas de figuras "
                "geométricas, sonidos y movimientos."
            ),
            codigo="M.1.4.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Describir y reproducir patrones con cuerpos geométricos."
            ),
            codigo="M.1.4.9.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Describir y construir patrones sencillos agrupando "
                "cantidades de hasta diez elementos."
            ),
            codigo="M.1.4.10.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Establecer relaciones de orden: ‘más que’ y ‘menos que’, "
                "entre objetos del entorno."
            ),
            codigo="M.1.4.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Utilizar la noción de cantidad en estimaciones y "
                "comparaciones de colecciones de objetos mediante el uso de "
                "cuantificadores como: muchos, pocos, uno, ninguno, todos."
            ),
            codigo="M.1.4.12.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Contar colecciones de objetos en el círculo del 1 al 20 en "
                "circunstancias de la cotidianidad."
            ),
            codigo="M.1.4.13.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Identificar cantidades y asociarlas con los numerales 1 al "
                "10 y el 0."
            ),
            codigo="M.1.4.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Escribir los números naturales, de 0 a 10, en contextos "
                "significativos."
            ),
            codigo="M.1.4.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Utilizar los números ordinales, del primero al quinto, en "
                "la ubicación de elementos del entorno."
            ),
            codigo="M.1.4.16.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Realizar adiciones y sustracciones con números naturales "
                "del 0 al 10, con el uso de material concreto."
            ),
            codigo="M.1.4.17.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Leer y escribir, en forma ascendente y descendente, los "
                "números naturales del 1 al 10."
            ),
            codigo="M.1.4.18.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer cuerpos geométricos en objetos del entorno."
            ),
            codigo="M.1.4.19.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Establecer semejanzas y diferencias entre objetos del "
                "entorno y cuerpos geométricos."
            ),
            codigo="M.1.4.20.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer figuras geométricas (triángulo, cuadrado, "
                "rectángulo y círculo) en objetos del entorno."
            ),
            codigo="M.1.4.21.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Describir objetos del entorno utilizando nociones de "
                "longitud: alto/bajo, largo/corto, cerca/lejos."
            ),
            codigo="M.1.4.22.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Medir, estimar y comparar objetos del entorno utilizando "
                "unidades no convencionales de longitud (palmos, cuartas, "
                "cintas, lápices, pies, entre otras)."
            ),
            codigo="M.1.4.23.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Describir y comparar objetos del entorno, según nociones de "
                "volumen y superficie: tamaño grande, pequeño."
            ),
            codigo="M.1.4.24.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Comparar objetos según la noción de capacidad "
                "(lleno/vacío)."
            ),
            codigo="M.1.4.25.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Comparar objetos según la noción de peso (pesado/liviano)."
            ),
            codigo="M.1.4.26.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Medir, estimar y comparar objetos según la noción de peso "
                "con unidades de medida no convencionales."
            ),
            codigo="M.1.4.27.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Reconocer las monedas de 1, 5 y 10 centavos en situaciones "
                "lúdicas."
            ),
            codigo="M.1.4.28.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Comparar y relacionar actividades con las nociones de "
                "tiempo: ayer, hoy, mañana, tarde, noche, antes, ahora, "
                "después y días de la semana en situaciones cotidianas."
            ),
            codigo="M.1.4.29.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Contar y nombrar los días de la semana y los meses del año "
                "utilizando el calendario."
            ),
            codigo="M.1.4.30.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Comparar y relacionar las nociones de joven/viejo, en los "
                "miembros de la familia."
            ),
            codigo="M.1.4.31.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Discriminar temperaturas entre objetos del entorno "
                "(frío/caliente)."
            ),
            codigo="M.1.4.32.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Identificar eventos probables y no probables en situaciones "
                "cotidianas."
            ),
            codigo="M.1.4.33.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recolectar y representar información del entorno en "
                "pictogramas, solucionando problemas sencillos."
            ),
            codigo="M.1.4.34.",
            asignatura=matematica,
            subnivel=preparatoria,
        ),
        # Elemental
        # Bloque 1
        Destreza(
            description=(
                "Representar gráficamente conjuntos y subconjuntos, "
                "discriminando las propiedades o atributos de los objetos."
            ),
            codigo="M.2.1.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir y reproducir patrones de objetos y figuras "
                "basándose en sus atributos."
            ),
            codigo="M.2.1.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir y reproducir patrones numéricos basados en sumas "
                "y restas, contando hacia adelante y hacia atrás."
            ),
            codigo="M.2.1.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Describir y reproducir patrones numéricos crecientes con la "
                "suma y la multiplicación."
            ),
            codigo="M.2.1.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Construir patrones de figuras basándose en sus atributos y "
                "patrones numéricos a partir de la suma, resta y "
                "multiplicación."
            ),
            codigo="M.2.1.5.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar los elementos del conjunto de salida con los "
                "elementos del conjunto de llegada, a partir de la "
                "correspondencia entre elementos."
            ),
            codigo="M.2.1.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar, en diagramas, tablas y una cuadrícula, las "
                "parejas ordenadas de una relación específica entre los "
                "elementos del conjunto de salida y los elementos del "
                "conjunto de llegada."
            ),
            codigo="M.2.1.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los elementos relacionados de un conjunto de "
                "salida y un conjunto de llegada como pares ordenados del "
                "producto cartesiano AxB."
            ),
            codigo="M.2.1.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar por extensión y gráficamente los pares "
                "ordenados del producto cartesiano AxB."
            ),
            codigo="M.2.1.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar los elementos de los conjuntos de salida y de "
                "llegada, a partir de los pares ordenados representados en "
                "una cuadrícula."
            ),
            codigo="M.2.1.10.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar el subconjunto de pares ordenados del producto "
                "cartesiano AxB que cumplen con una relación de "
                "correspondencia uno a uno."
            ),
            codigo="M.2.1.11.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar, escribir y leer los números naturales del 0 al "
                "9 999 en forma concreta, gráfica (en la semirrecta "
                "numérica) y simbólica."
            ),
            codigo="M.2.1.12.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Contar cantidades del 0 al 9 999 para verificar "
                "estimaciones (en grupos de dos, tres, cinco y diez)."
            ),
            codigo="M.2.1.13.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el valor posicional de números naturales de hasta "
                "cuatro cifras, basándose en la composición y descomposición "
                "de unidades, decenas, centenas y unidades de mil, mediante "
                "el uso de material concreto y con representación simbólica."
            ),
            codigo="M.2.1.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de secuencia y de orden en un "
                "conjunto de números naturales de hasta cuatro cifras, "
                "utilizando material concreto y simbología matemática (=, <, "
                ">,)."
            ),
            codigo="M.2.1.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer números ordinales del primero al vigésimo para "
                "organizar objetos o elementos."
            ),
            codigo="M.2.1.16.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer y diferenciar los números pares e impares por "
                "agrupación y de manera numérica."
            ),
            codigo="M.2.1.17.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer mitades y dobles en unidades de objetos."
            ),
            codigo="M.2.1.18.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar la noción de adición con la de agregar objetos a "
                "un conjunto."
            ),
            codigo="M.2.1.19.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Vincular la noción de sustracción con la noción de quitar "
                "objetos de un conjunto y la de establecer la diferencia "
                "entre dos cantidades."
            ),
            codigo="M.2.1.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar adiciones y sustracciones con los números hasta 9 "
                "999, con material concreto, mentalmente, gráficamente y de "
                "manera numérica."
            ),
            codigo="M.2.1.21.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar estrategias de descomposición en decenas, centenas "
                "y miles en cálculos de suma y resta."
            ),
            codigo="M.2.1.22.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades conmutativa y asociativa de la "
                "adición en estrategias de cálculo mental."
            ),
            codigo="M.2.1.23.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear, de forma individual o grupal, "
                "problemas que requieran el uso de sumas y restas con "
                "números hasta de cuatro cifras, e interpretar la solución "
                "dentro del contexto del problema."
            ),
            codigo="M.2.1.24.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar la noción de multiplicación con patrones de "
                "sumandos iguales o con situaciones de “tantas veces tanto”."
            ),
            codigo="M.2.1.25.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar multiplicaciones en función del modelo grupal, "
                "geométrico y lineal."
            ),
            codigo="M.2.1.26.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Memorizar paulatinamente las combinaciones multiplicativas "
                "(tablas de multiplicar) con la manipulación y visualización "
                "de material concreto."
            ),
            codigo="M.2.1.27.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las reglas de multiplicación por 10, 100 y 1 000 en "
                "números de hasta dos cifras."
            ),
            codigo="M.2.1.28.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades conmutativa y asociativa de la "
                "multiplicación en el cálculo escrito y mental, y en la "
                "resolución de problemas."
            ),
            codigo="M.2.1.29.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Relacionar la noción de división con patrones de resta "
                "iguales o reparto de cantidades en tantos iguales."
            ),
            codigo="M.2.1.30.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la relación entre división y multiplicación como "
                "operaciones inversas."
            ),
            codigo="M.2.1.31.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular mentalmente productos y cocientes exactos "
                "utilizando varias estrategias."
            ),
            codigo="M.2.1.32.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver problemas relacionados con la multiplicación y la "
                "división utilizando varias estrategias, e interpretar la "
                "solución dentro del contexto del problema."
            ),
            codigo="M.2.1.33.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Reconocer y diferenciar los elementos y propiedades de "
                "cilindros, esferas, conos, cubos, pirámides de base "
                "cuadrada y prismas rectangulares en objetos del entorno y/o "
                "modelos geométricos."
            ),
            codigo="M.2.2.1.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Clasificar objetos, cuerpos geométricos y figuras "
                "geométricas según sus propiedades."
            ),
            codigo="M.2.2.2.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar formas cuadradas, triangulares, rectangulares y "
                "circulares en cuerpos geométricos del entorno y/o modelos "
                "geométricos."
            ),
            codigo="M.2.2.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Construir figuras geométricas como cuadrados, triángulos, "
                "rectángulos y círculos."
            ),
            codigo="M.2.2.4.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Distinguir lados, frontera interior y exterior, vértices y "
                "ángulos en figuras geométricas: cuadrados, triángulos, "
                "rectángulos y círculos."
            ),
            codigo="M.2.2.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer y diferenciar cuadrados y rectángulos a partir "
                "del análisis de sus características, y determinar el "
                "perímetro de cuadrados y rectángulos por estimación y/o "
                "medición."
            ),
            codigo="M.2.2.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer líneas, rectas y curvas en figuras planas y "
                "cuerpos."
            ),
            codigo="M.2.2.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Representar de forma gráfica la semirrecta, el segmento y "
                "el ángulo."
            ),
            codigo="M.2.2.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer y clasificar ángulos según su amplitud (rectos, "
                "agudos y obtusos) en objetos, cuerpos y figuras "
                "geométricas."
            ),
            codigo="M.2.2.9.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Medir, estimar y comparar longitudes de objetos del "
                "entorno, contrastándolas con patrones de medidas no "
                "convencionales."
            ),
            codigo="M.2.2.10.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar las unidades de medida de longitud: el metro y sus "
                "submúltiplos (dm, cm, mm) en la estimación y medición de "
                "longitudes de objetos del entorno."
            ),
            codigo="M.2.2.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones simples de medidas de longitud del "
                "metro a sus submúltiplos."
            ),
            codigo="M.2.2.12.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Representar cantidades monetarias con el uso de monedas y "
                "billetes de 1, 5, 10, 20, 50 y 100 (didácticos)."
            ),
            codigo="M.2.2.13.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones monetarias simples en situaciones "
                "significativas."
            ),
            codigo="M.2.2.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar la unidad monetaria en actividades lúdicas y en "
                "transacciones cotidianas simples, destacando la importancia "
                "de la integridad y la honestidad."
            ),
            codigo="M.2.2.15.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer día, noche, mañana, tarde, hoy, ayer, días de la "
                "semana y los meses del año para valorar el tiempo propio y "
                "el de los demás, y ordenar situaciones temporales "
                "secuenciales asociándolas con eventos significativos."
            ),
            codigo="M.2.2.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones usuales entre años, meses, semanas, "
                "días, horas, minutos y segundos en situaciones "
                "significativas."
            ),
            codigo="M.2.2.17.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Leer horas y minutos en un reloj analógico."
            ),
            codigo="M.2.2.18.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Medir, estimar y comparar masas contrastándolas con "
                "patrones de medidas no convencionales."
            ),
            codigo="M.2.2.19.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar las unidades de medida de masa: el gramo y el "
                "kilogramo, en la estimación y medición de objetos del "
                "entorno."
            ),
            codigo="M.2.2.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones simples de medidas de masa."
            ),
            codigo="M.2.2.21.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar la libra como unidad de medida de masa."
            ),
            codigo="M.2.2.22.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Medir, estimar y comparar capacidades contrastándolas con "
                "patrones de medidas no convencionales."
            ),
            codigo="M.2.2.23.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar las unidades de medida de capacidad: el litro y "
                "sus submúltiplos (dl, cl, ml) en la estimación y medición "
                "de objetos del entorno."
            ),
            codigo="M.2.2.24.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones simples de medidas de capacidad del "
                "litro a sus submúltiplos."
            ),
            codigo="M.2.2.25.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Organizar y representar datos estadísticos relativos a su "
                "entorno en tablas de frecuencias, pictogramas y diagramas "
                "de barras, en función de explicar e interpretar "
                "conclusiones y asumir compromisos."
            ),
            codigo="M.2.3.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Realizar combinaciones simples y solucionar situaciones "
                "cotidianas."
            ),
            codigo="M.2.3.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Reconocer experiencias aleatorias en situaciones "
                "cotidianas."
            ),
            codigo="M.2.3.3.",
            asignatura=matematica,
            subnivel=elemental,
            bloque=bloque3
        ),
        # Media
        # Bloque 1
        Destreza(
            description=(
                "Generar sucesiones con sumas, restas, multiplicaciones y "
                "divisiones, con números naturales, a partir de ejercicios "
                "numéricos o problemas sencillos."
            ),
            codigo="M.3.1.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Leer y ubicar pares ordenados en el sistema de coordenadas "
                "rectangulares, con números naturales, decimales y "
                "fracciones."
            ),
            codigo="M.3.1.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Utilizar el sistema de coordenadas para representar "
                "situaciones significativas."
            ),
            codigo="M.3.1.3.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Leer y escribir números naturales en cualquier contexto."
            ),
            codigo="M.3.1.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer el valor posicional de números naturales de hasta "
                "nueve cifras, basándose en su composición y descomposición, "
                "con el uso de material concreto y con representación "
                "simbólica."
            ),
            codigo="M.3.1.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de secuencia y orden en un conjunto "
                "de números naturales de hasta nueve cifras, utilizando "
                "material concreto, la semirrecta numérica y simbología "
                "matemática (=, <, >)."
            ),
            codigo="M.3.1.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer términos de la adición y sustracción, y calcular "
                "la suma o la diferencia de números naturales."
            ),
            codigo="M.3.1.7.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de la adición como estrategia de "
                "cálculo mental y la solución de problemas."
            ),
            codigo="M.3.1.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer términos y realizar multiplicaciones entre "
                "números naturales, aplicando el algoritmo de la "
                "multiplicación y con el uso de la tecnología."
            ),
            codigo="M.3.1.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las propiedades de la multiplicación en el cálculo "
                "escrito y mental, y la resolución de ejercicios y "
                "problemas."
            ),
            codigo="M.3.1.10.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer términos y realizar divisiones entre números "
                "naturales con residuo, con el dividendo mayor que el "
                "divisor, aplicando el algoritmo correspondiente y con el "
                "uso de la tecnología."
            ),
            codigo="M.3.1.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular productos y cocientes de números naturales por 10, "
                "100 y 1 000."
            ),
            codigo="M.3.1.12.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver problemas que requieran el uso de operaciones "
                "combinadas con números naturales e interpretar la solución "
                "dentro del contexto del problema."
            ),
            codigo="M.3.1.13.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar múltiplos y divisores de un conjunto de números "
                "naturales."
            ),
            codigo="M.3.1.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Utilizar criterios de divisibilidad por 2, 3, 4, 5, 6, 9 y "
                "10 en la descomposición de números naturales en factores "
                "primos y en la resolución de problemas."
            ),
            codigo="M.3.1.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar números primos y números compuestos por su "
                "definición, aplicando criterios de divisibilidad."
            ),
            codigo="M.3.1.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Encontrar el máximo común divisor y el mínimo común "
                "múltiplo de un conjunto de números naturales."
            ),
            codigo="M.3.1.17.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver problemas que impliquen el cálculo del MCM y el "
                "MCD."
            ),
            codigo="M.3.1.18.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Identificar la potenciación como una operación "
                "multiplicativa en los números naturales."
            ),
            codigo="M.3.1.19.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Asociar las potencias con exponentes 2 (cuadrados) y 3 "
                "(cubos) con representaciones en dos y tres dimensiones o "
                "con áreas y volúmenes."
            ),
            codigo="M.3.1.20.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer la radicación como la operación inversa a la "
                "potenciación."
            ),
            codigo="M.3.1.21.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de potenciación y radicación, "
                "utilizando varias estrategias, e interpretar la solución "
                "dentro del contexto del problema."
            ),
            codigo="M.3.1.22.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular y reconocer cuadrados y cubos de números "
                "inferiores a 20."
            ),
            codigo="M.3.1.23.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular raíces cuadradas y cúbicas utilizando la "
                "estimación, la descomposición en factores primos y la "
                "tecnología."
            ),
            codigo="M.3.1.24.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Leer y escribir cantidades expresadas en números romanos "
                "hasta 1 000."
            ),
            codigo="M.3.1.25.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer, leer y escribir los números decimales utilizados "
                "en la vida cotidiana."
            ),
            codigo="M.3.1.26.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de secuencia y orden en un conjunto "
                "de números decimales, utilizando material concreto, la "
                "semirrecta numérica graduada y simbología matemática (=, <, "
                ">)."
            ),
            codigo="M.3.1.27.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular, aplicando algoritmos y la tecnología, sumas, "
                "restas, multiplicaciones y divisiones con números "
                "decimales."
            ),
            codigo="M.3.1.28.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Aplicar las reglas del redondeo en la resolución de "
                "problemas."
            ),
            codigo="M.3.1.29.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Utilizar el cálculo de productos o cocientes por 10, 100 o "
                "1 000 con números decimales, como estrategia de cálculo "
                "mental y solución de problemas."
            ),
            codigo="M.3.1.30.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas con sumas, restas, "
                "multiplicaciones y divisiones con números decimales, "
                "utilizando varias estrategias, e interpretar la solución "
                "dentro del contexto del problema."
            ),
            codigo="M.3.1.31.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas con operaciones combinadas "
                "con números decimales, utilizando varias estrategias, e "
                "interpretar la solución dentro del contexto del problema."
            ),
            codigo="M.3.1.32.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Leer y escribir fracciones a partir de un objeto, un "
                "conjunto de objetos fraccionables o una unidad de medida."
            ),
            codigo="M.3.1.33.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar fracciones en la semirrecta numérica y "
                "gráficamente, para expresar y resolver situaciones "
                "cotidianas."
            ),
            codigo="M.3.1.34.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer los números decimales: décimos, centésimos y "
                "milésimos, como la expresión decimal de fracciones por "
                "medio de la división."
            ),
            codigo="M.3.1.35.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Transformar números decimales a fracciones con denominador "
                "10, 100 y 1 000."
            ),
            codigo="M.3.1.36.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de orden entre fracciones, utilizando "
                "material concreto, la semirrecta numérica y simbología "
                "matemática (=, <, >)."
            ),
            codigo="M.3.1.37.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Establecer relaciones de secuencia y orden entre números "
                "naturales, fracciones y decimales, utilizando material "
                "concreto, la semirrecta numérica y simbología matemática "
                "(=, <, >)."
            ),
            codigo="M.3.1.38.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular sumas y restas con fracciones obteniendo el "
                "denominador común."
            ),
            codigo="M.3.1.39.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar multiplicaciones y divisiones entre fracciones, "
                "empleando como estrategia la simplificación."
            ),
            codigo="M.3.1.40.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Realizar cálculos combinados de sumas, restas, "
                "multiplicaciones y divisiones con fracciones."
            ),
            codigo="M.3.1.41.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas de sumas, restas, "
                "multiplicaciones y divisiones con fracciones, e interpretar "
                "la solución dentro del contexto del problema."
            ),
            codigo="M.3.1.42.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas que contienen combinaciones "
                "de sumas, restas, multiplicaciones y divisiones con números "
                "naturales, fracciones y decimales, e interpretar la "
                "solución dentro del contexto del problema."
            ),
            codigo="M.3.1.43.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Reconocer las magnitudes directa o inversamente "
                "proporcionales en situaciones cotidianas; elaborar tablas y "
                "plantear proporciones."
            ),
            codigo="M.3.1.44.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Expresar porcentajes como fracciones y decimales, o "
                "fracciones y decimales como porcentajes, en función de "
                "explicar situaciones cotidianas."
            ),
            codigo="M.3.1.45.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Representar porcentajes en diagramas circulares como una "
                "estrategia para comunicar información de distinta índole."
            ),
            codigo="M.3.1.46.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Calcular porcentajes en aplicaciones cotidianas: facturas, "
                "notas de venta, rebajas, cuentas de ahorro, interés simple "
                "y otros."
            ),
            codigo="M.3.1.47.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        Destreza(
            description=(
                "Resolver y plantear problemas con la aplicación de la "
                "proporcionalidad directa o inversa, e interpretar la "
                "solución dentro del contexto del problema."
            ),
            codigo="M.3.1.48.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque1
        ),
        # Bloque 2
        Destreza(
            description=(
                "Reconocer rectas paralelas, secantes y secantes "
                "perpendiculares en figuras geométricas planas."
            ),
            codigo="M.3.2.1.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Determinar la posición relativa de dos rectas en gráficos "
                "(paralelas, secantes y secantes perpendiculares)."
            ),
            codigo="M.3.2.2.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Identificar paralelogramos y trapecios a partir del "
                "análisis de sus características y propiedades."
            ),
            codigo="M.3.2.3.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el perímetro; deducir y calcular el área de "
                "paralelogramos y trapecios en la resolución de problemas."
            ),
            codigo="M.3.2.4.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Clasificar triángulos, por sus lados (en equiláteros, "
                "isósceles y escalenos) y por sus ángulos (en rectángulos, "
                "acutángulos y obtusángulos)."
            ),
            codigo="M.3.2.5.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular el perímetro de triángulos; deducir y calcular el "
                "área de triángulos en la resolución de problemas."
            ),
            codigo="M.3.2.6.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Construir, con el uso de una regla y un compás, triángulos, "
                "paralelogramos y trapecios, fijando medidas de lados y/o "
                "ángulos."
            ),
            codigo="M.3.2.7.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Clasificar polígonos regulares e irregulares según sus "
                "lados y ángulos."
            ),
            codigo="M.3.2.8.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Calcular, en la resolución de problemas, el perímetro y "
                "área de polígonos regulares, aplicando la fórmula "
                "correspondiente."
            ),
            codigo="M.3.2.9.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Resolver problemas que impliquen el cálculo del perímetro "
                "de polígonos irregulares."
            ),
            codigo="M.3.2.10.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer los elementos de un círculo en representaciones "
                "gráficas, y calcular la longitud (perímetro) de la "
                "circunferencia y el área de un círculo en la resolución de "
                "problemas."
            ),
            codigo="M.3.2.11.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Clasificar poliedros y cuerpos de revolución de acuerdo a "
                "sus características y elementos."
            ),
            codigo="M.3.2.12.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Aplicar la fórmula de Euler en la resolución de problemas."
            ),
            codigo="M.3.2.13.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones simples de medidas de longitud del "
                "metro, múltiplos y submúltiplos en la resolución de "
                "problemas."
            ),
            codigo="M.3.2.14.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer el metro cuadrado como unidad de medida de "
                "superficie, los submúltiplos y múltiplos, y realizar "
                "conversiones en la resolución de problemas."
            ),
            codigo="M.3.2.15.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Relacionar las medidas de superficie con las medidas "
                "agrarias más usuales (hectárea, área, centiárea) en la "
                "resolución de problemas."
            ),
            codigo="M.3.2.16.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer el metro cúbico como unidad de medida de volumen, "
                "los submúltiplos y múltiplos; relacionar medidas de volumen "
                "y capacidad; y realizar conversiones en la resolución de "
                "problemas."
            ),
            codigo="M.3.2.17.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Comparar el kilogramo, el gramo y la libra con las medidas "
                "de masa de la localidad, a partir de experiencias concretas "
                "y del uso de instrumentos de medida."
            ),
            codigo="M.3.2.18.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Realizar conversiones simples entre el kilogramo, el gramo "
                "y la libra en la solución de problemas cotidianos."
            ),
            codigo="M.3.2.19.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Medir ángulos rectos, agudos y obtusos, con el graduador u "
                "otras estrategias, para dar solución a situaciones "
                "cotidianas."
            ),
            codigo="M.3.2.20.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Reconocer los ángulos como parte del sistema sexagesimal en "
                "la conversión de grados a minutos."
            ),
            codigo="M.3.2.21.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Convertir medidas decimales de ángulos a grados y minutos, "
                "en función de explicar situaciones cotidianas."
            ),
            codigo="M.3.2.22.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        Destreza(
            description=(
                "Utilizar siglo, década y lustro para interpretar "
                "información del entorno."
            ),
            codigo="M.3.2.23.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque2
        ),
        # Bloque 3
        Destreza(
            description=(
                "Analizar y representar, en tablas de frecuencias, diagramas "
                "de barra, circulares y poligonales, datos discretos "
                "recolectados en el entorno e información publicada en "
                "medios de comunicación."
            ),
            codigo="M.3.3.1.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Analizar e interpretar el significado de calcular medidas "
                "de tendencia central (media, mediana y moda) y medidas de "
                "dispersión (el rango), de un conjunto de datos estadísticos "
                "discretos tomados del entorno y de medios de comunicación."
            ),
            codigo="M.3.3.2.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Emplear programas informáticos para tabular y representar "
                "datos discretos estadísticos obtenidos del entorno."
            ),
            codigo="M.3.3.3.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Realizar combinaciones simples de hasta tres por cuatro "
                "elementos para explicar situaciones cotidianas."
            ),
            codigo="M.3.3.4.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Describir las experiencias y sucesos aleatorios a través "
                "del análisis de sus representaciones gráficas y el uso de "
                "la terminología adecuada."
            ),
            codigo="M.3.3.5.",
            imprescindible=True,
            asignatura=matematica,
            subnivel=media,
            bloque=bloque3
        ),
        Destreza(
            description=(
                "Calcular la probabilidad de que un evento ocurra, "
                "gráficamente y con el uso de fracciones, en función de "
                "resolver problemas asociados a probabilidades de "
                "situaciones significativas."
            ),
            codigo="M.3.3.6.",
            asignatura=matematica,
            subnivel=media,
            bloque=bloque3
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0041_auto_20180813_1430'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
