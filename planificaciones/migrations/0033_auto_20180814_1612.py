from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    fisica = Asignatura.objects.get(name='Física')
    biologia = Asignatura.objects.get(name='Biología')
    quimica = Asignatura.objects.get(name='Química')

    # Bloques Física
    bloque1_fisica = BloqueCurricular.objects.get(
        numero_bloque=1, asignatura=fisica
    )
    bloque2_fisica = BloqueCurricular.objects.get(
        numero_bloque=2, asignatura=fisica
    )
    bloque3_fisica = BloqueCurricular.objects.get(
        numero_bloque=3, asignatura=fisica
    )
    bloque4_fisica = BloqueCurricular.objects.get(
        numero_bloque=4, asignatura=fisica
    )
    bloque5_fisica = BloqueCurricular.objects.get(
        numero_bloque=5, asignatura=fisica
    )
    bloque6_fisica = BloqueCurricular.objects.get(
        numero_bloque=6, asignatura=fisica
    )

    # Bloques Biología
    bloque1_biologia = BloqueCurricular.objects.get(
        numero_bloque=1, asignatura=biologia
    )
    bloque2_biologia = BloqueCurricular.objects.get(
        numero_bloque=2, asignatura=biologia
    )
    bloque3_biologia = BloqueCurricular.objects.get(
        numero_bloque=3, asignatura=biologia
    )
    bloque4_biologia = BloqueCurricular.objects.get(
        numero_bloque=4, asignatura=biologia
    )
    bloque5_biologia = BloqueCurricular.objects.get(
        numero_bloque=5, asignatura=biologia
    )

    # Bloques Química
    bloque1_quimica = BloqueCurricular.objects.get(
        numero_bloque=1, asignatura=quimica
    )
    bloque2_quimica = BloqueCurricular.objects.get(
        numero_bloque=2, asignatura=quimica
    )
    bloque3_quimica = BloqueCurricular.objects.get(
        numero_bloque=3, asignatura=quimica
    )

    # Subnivel
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Física
        # Bloque 1
        Destreza(
            description=(
                "Determinar la posición y el desplazamiento de un objeto "
                "(considerado puntual) que se mueve, a lo largo de una "
                "trayectoria rectilínea, en un sistema de referencia "
                "establecida y sistematizar información relacionada al "
                "cambio de posición en función del tiempo, como resultado de "
                "la observación de movimiento de un objeto y el empleo de "
                "tablas y gráficas."
            ),
            codigo="CN.F.5.1.1.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar, por medio de la experimentación de un objeto y el "
                "análisis de tablas y gráficas, que el movimiento rectilíneo "
                "uniforme implica una velocidad constante."
            ),
            codigo="CN.F.5.1.2.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Obtener la velocidad instantánea empleando el gráfico "
                "posición en función del tiempo, y conceptualizar la "
                "aceleración media e instantánea, mediante el análisis de "
                "las gráficas velocidad en función del tiempo."
            ),
            codigo="CN.F.5.1.3.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Elaborar gráficos de velocidad versus tiempo, a partir de "
                "los gráficos posición versus tiempo; y determinar el "
                "desplazamiento a partir del gráfico velocidad versus "
                "tiempo."
            ),
            codigo="CN.F.5.1.4.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Reconocer que la posición, la trayectoria y el "
                "desplazamiento en dos dimensiones requieren un sistema de "
                "referencia y determinar gráfica y/o analíticamente los "
                "vectores posición y desplazamiento, así como la trayectoria "
                "de un objeto, entendiendo que en el movimiento en dos "
                "dimensiones, las direcciones perpendiculares del sistema de "
                "referencia son independientes."
            ),
            codigo="CN.F.5.1.5.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Establecer la relación entre las magnitudes escalares y "
                "vectoriales del movimiento en dos dimensiones, mediante el "
                "reconocimiento de que los vectores guardan tres "
                "informaciones independientes: magnitud, dirección y unidad "
                "respectiva, y que cualquier vector se puede proyectar en "
                "las direcciones de los ejes independientes del sistema de "
                "referencia, las llamadas componentes perpendiculares u "
                "ortogonales del vector."
            ),
            codigo="CN.F.5.1.6.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Establecer las diferencias entre vector posición y vector "
                "desplazamiento, y analizar gráficas que representen la "
                "trayectoria en dos dimensiones de un objeto, observando la "
                "ubicación del vector posición y vector desplazamiento para "
                "diferentes instantes."
            ),
            codigo="CN.F.5.1.7.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Analizar el movimiento en dos dimensiones de un objeto, "
                "mediante la obtención del vector velocidad promedio "
                "(multiplicando el vector desplazamiento por el recíproco "
                "del intervalo de tiempo implicado) y calcular la rapidez "
                "promedio, a partir de la distancia recorrida por un objeto "
                "que se mueve en dos dimensiones y el tiempo empleado en "
                "hacerlo."
            ),
            codigo="CN.F.5.1.8.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Construir, a partir del gráfico posición versus tiempo, el "
                "vector velocidad instantánea evaluado en el instante "
                "inicial, considerando los vectores, posiciones y "
                "desplazamiento para dos instantes diferentes, inicial y "
                "final, haciendo que el instante final se aproxime al "
                "inicial tanto como se desee (pero que nunca son iguales), y "
                "reconocer que la dirección del vector velocidad instantánea "
                "se encuentra en la dirección de la línea tangente a la "
                "trayectoria en el instante inicial."
            ),
            codigo="CN.F.5.1.9.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar la aceleración promedio de un objeto entre dos "
                "instantes diferentes, uno inicial y otro final, "
                "considerando el vector desplazamiento y el intervalo de "
                "tiempo implicado, reconocer e inferir que este vector tiene "
                "la dirección de la línea secante a la trayectoria; deducir "
                "gráficamente que para la trayectoria en dos dimensiones de "
                "un objeto en cada instante se pueden ubicar sus vectores: "
                "posición, velocidad y aceleración."
            ),
            codigo="CN.F.5.1.10.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Identificar que la disposición en el plano de los vectores "
                "velocidad (tangente a la trayectoria) y aceleración (hacia "
                "el interior de la trayectoria) se puede proyectar el vector "
                "aceleración en dos direcciones, una en la dirección de la "
                "velocidad y, la otra, perpendicular a ella."
            ),
            codigo="CN.F.5.1.11.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Analizar gráficamente que, en el caso particular de que la "
                "trayectoria sea un círculo, la aceleración normal se llama "
                "aceleración central (centrípeta) y determinar que en el "
                "movimiento circular solo se necesita el ángulo (medido en "
                "radianes) entre la posición del objeto y una dirección de "
                "referencia, mediante el análisis gráfico de un punto "
                "situado en un objeto que gira alrededor de un eje."
            ),
            codigo="CN.F.5.1.12.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Diferenciar, mediante el análisis de gráficos el movimiento "
                "circular uniforme (MCU) del movimiento circular "
                "uniformemente variado (MCUV), en función de la comprensión "
                "de las características y relaciones de las cuatro "
                "magnitudes de la cinemática del movimiento circular "
                "(posición angular, velocidad angular, aceleración angular y "
                "el tiempo)."
            ),
            codigo="CN.F.5.1.13.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Establecer las analogías entre el movimiento rectilíneo y "
                "el movimiento circular, mediante el análisis de sus "
                "ecuaciones."
            ),
            codigo="CN.F.5.1.14.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Resolver problemas de aplicación donde se relacionen las "
                "magnitudes angulares y las lineales."
            ),
            codigo="CN.F.5.1.15.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Indagar los estudios de Aristóteles, Galileo y Newton, para "
                "comparar sus experiencias frente a las razones por las que "
                "se mueven los objetos y despejar ideas preconcebidas sobre "
                "este fenómeno, con la finalidad de conceptualizar la "
                "primera ley de Newton (ley de la inercia) y determinar por "
                "medio de la experimentación que no se produce aceleración "
                "cuando las fuerzas están en equilibrio, por lo que un "
                "objeto continúa moviéndose con rapidez constante o "
                "permanece en reposo (primera ley de Newton o principio de "
                "inercia de Galileo)."
            ),
            codigo="CN.F.5.1.16.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar la segunda ley de Newton mediante la relación "
                "entre las magnitudes: aceleración y fuerza que actúan sobre "
                "un objeto y su masa, mediante experimentaciones formales o "
                "no formales."
            ),
            codigo="CN.F.5.1.17.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar la tercera ley de Newton en aplicaciones reales."
            ),
            codigo="CN.F.5.1.18.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Reconocer sistemas inerciales y no inerciales a través de "
                "la observación de videos y análisis de situaciones "
                "cotidianas y elaborar diagramas de cuerpo libre para "
                "conceptualizar las leyes de Newton, resolver problemas de "
                "aplicación."
            ),
            codigo="CN.F.5.1.19.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Reconocer que la fuerza es una magnitud de naturaleza "
                "vectorial, mediante la explicación gráfica de situaciones "
                "reales para resolver problemas donde se observen objetos en "
                "equilibrio u objetos acelerados."
            ),
            codigo="CN.F.5.1.20.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Analizar que las leyes de Newton no son exactas pero dan "
                "muy buenas aproximaciones cuando el objeto se mueve con muy "
                "pequeña rapidez, comparada con la rapidez de la luz o "
                "cuando el objeto es suficientemente grande para ignorar los "
                "efectos cuánticos, mediante la observación de videos "
                "relacionados."
            ),
            codigo="CN.F.5.1.21.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Reconocer que la velocidad es una información insuficiente "
                "y que lo fundamental es la vinculación de la masa del "
                "objeto con su velocidad a través de la cantidad de "
                "movimiento lineal, para comprender la ley de conservación "
                "de la cantidad de movimiento y demostrar analíticamente que "
                "el impulso de la fuerza que actúa sobre un objeto es igual "
                "a la variación de la cantidad de movimiento de ese objeto."
            ),
            codigo="CN.F.5.1.22.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar que la fuerza es la variación de momento lineal en "
                "el transcurso del tiempo, mediante ejemplos reales, y "
                "determinar mediante la aplicación del teorema del impulso, "
                "la cantidad de movimiento y de la tercera ley de Newton que "
                "para un sistema aislado de dos cuerpos, no existe cambio en "
                "el tiempo de la cantidad de movimiento total del sistema."
            ),
            codigo="CN.F.5.1.23.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar experimentalmente el centro de masa para un "
                "sistema simple de dos cuerpos y reconocer que el centro de "
                "masa de un sistema aislado puede permanecer en reposo o "
                "moverse en línea recta y velocidad constante."
            ),
            codigo="CN.F.5.1.24.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar que la intensidad del campo gravitatorio de un "
                "planeta determina la fuerza del peso de un objeto de masa "
                "(m), para establecer que el peso puede variar pero la masa "
                "es la misma."
            ),
            codigo="CN.F.5.1.25.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar que el lanzamiento vertical y la caída libre son "
                "casos concretos del movimiento unidimensional con "
                "aceleración constante (g), mediante ejemplificaciones y "
                "utilizar las ecuaciones del movimiento vertical en la "
                "solución de problemas."
            ),
            codigo="CN.F.5.1.26.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar el fenómeno de la aceleración cuando un cuerpo que "
                "cae libremente alcanza su rapidez terminal, mediante el "
                "análisis del rozamiento con el aire."
            ),
            codigo="CN.F.5.1.27.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Analizar que en el movimiento de proyectiles se observa la "
                "naturaleza vectorial de la segunda ley de Newton, mediante "
                "la aplicación de los movimientos rectilíneos antes "
                "estudiados."
            ),
            codigo="CN.F.5.1.28.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Describir el movimiento de proyectiles en la superficie de "
                "la Tierra, mediante la determinación de las coordenadas "
                "horizontal y vertical del objeto para cada instante del "
                "vuelo y de las relaciones entre sus magnitudes (velocidad, "
                "aceleración, tiempo); determinar el alcance horizontal y la "
                "altura máxima alcanzada por un proyectil y su relación con "
                "el ángulo de lanzamiento, a través del análisis del tiempo "
                "que se demora un objeto en seguir la trayectoria, que es el "
                "mismo que emplean sus proyecciones en los ejes."
            ),
            codigo="CN.F.5.1.29.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Observar en objetos y fenómenos las fuerzas de compresión o "
                "de tracción que causan la deformación de los objetos e "
                "inferir su importancia en su vida cotidiana."
            ),
            codigo="CN.F.5.1.30.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar que la fuerza que ejerce un resorte es "
                "proporcional a la deformación que experimenta y está "
                "dirigida hacia la posición de equilibrio (ley de Hooke), "
                "mediante prácticas experimentales y el análisis de su "
                "modelo matemático y de la característica de cada resorte."
            ),
            codigo="CN.F.5.1.31.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar que el movimiento circular uniforme requiere la "
                "aplicación de una fuerza constante dirigida hacia el centro "
                "del círculo, mediante la demostración analítica y/o "
                "experimental."
            ),
            codigo="CN.F.5.1.32.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Reconocer que la fuerza centrífuga es una fuerza ficticia "
                "que aparece en un sistema no inercial (inercia de "
                "movimiento), en función de explicar la acción de las "
                "fuerzas en el movimiento curvilíneo."
            ),
            codigo="CN.F.5.1.33.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Deducir las expresiones cinemáticas a través del análisis "
                "geométrico del movimiento armónico simple (MAS) y del uso "
                "de las funciones seno o coseno (en dependencia del eje "
                "escogido), y que se puede equiparar la amplitud A y la "
                "frecuencia angular w del MAS con el radio y la velocidad "
                "angular del MCU."
            ),
            codigo="CN.F.5.1.34.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar experimentalmente que un objeto sujeto a un "
                "resorte realiza un movimiento periódico (llamado movimiento "
                "armónico simple) cuando se estira o se comprime, generando "
                "una fuerza elástica dirigida hacia la posición de "
                "equilibrio y proporcional a la deformación."
            ),
            codigo="CN.F.5.1.35.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Identificar las magnitudes que intervienen en el movimiento "
                "armónico simple, por medio de la observación de mecanismos "
                "que tienen este tipo de movimiento y analizar "
                "geométricamente el movimiento armónico simple como un "
                "componente del movimiento circular uniforme, mediante la "
                "proyección del movimiento de un objeto en MAS sobre el "
                "diámetro horizontal de la circunferencia."
            ),
            codigo="CN.F.5.1.36.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Describir que si una masa se sujeta a un resorte, sin "
                "considerar fuerzas de fricción, se observa la conservación "
                "de la energía mecánica, considerando si el resorte está en "
                "posición horizontal o suspendido verticalmente, mediante la "
                "identificación de las energías que intervienen en cada "
                "caso."
            ),
            codigo="CN.F.5.1.37.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar que se detecta el origen de la carga eléctrica, "
                "partiendo de la comprensión de que esta reside en los "
                "constituyentes del átomo (electrones o protones) y que solo "
                "se detecta su presencia por los efectos entre ellas, "
                "comprobar la existencia de solo dos tipos de carga "
                "eléctrica a partir de mecanismos que permiten la "
                "identificación de fuerzas de atracción y repulsión entre "
                "objetos electrificados, en situaciones cotidianas y "
                "experimentar el proceso de carga por polarización "
                "electrostática, con materiales de uso cotidiano."
            ),
            codigo="CN.F.5.1.38.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Clasificar los diferentes materiales en conductores, "
                "semiconductores y aislantes, mediante el análisis de su "
                "capacidad, para conducir carga eléctrica."
            ),
            codigo="CN.F.5.1.39.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar que la masa del protón es mayor que la del "
                "electrón, mediante el análisis del experimento del físico "
                "alemán Eugen Goldstein e indagar sobre los experimentos que "
                "permitieron establecer la cuantización y la conservación de "
                "la carga eléctrica."
            ),
            codigo="CN.F.5.1.40.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Analizar y explicar los aparatos o dispositivos que tienen "
                "la característica de separar cargas eléctricas, mediante la "
                "descripción de objetos de uso cotidiano."
            ),
            codigo="CN.F.5.1.41.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar las propiedades de conductividad eléctrica de un "
                "metal en función del modelo del gas de electrones."
            ),
            codigo="CN.F.5.1.42.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Conceptualizar la ley de Coulomb en función de cuantificar "
                "con qué fuerza se atraen o se repelen las cargas eléctricas "
                "y determinar que esta fuerza electrostática también es de "
                "naturaleza vectorial."
            ),
            codigo="CN.F.5.1.43.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar el principio de superposición mediante el análisis "
                "de la fuerza resultante sobre cualquier carga, que resulta "
                "de la suma vectorial de las fuerzas ejercidas por las otras "
                "cargas que están presentes en una configuración estable."
            ),
            codigo="CN.F.5.1.44.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar que la presencia de un campo eléctrico alrededor "
                "de una carga puntual permite comprender la acción de la "
                "fuerza a distancia, la acción a distancia entre cargas a "
                "través de la conceptualización de campo eléctrico y la "
                "visualización de los efectos de las líneas de campo en "
                "demostraciones con material concreto, y determinar la "
                "fuerza que experimenta una carga dentro de un campo "
                "eléctrico, mediante la resolución de ejercicios y problemas "
                "de aplicación."
            ),
            codigo="CN.F.5.1.45.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Establecer que el trabajo efectuado por un agente externo "
                "al mover una carga de un punto a otro dentro del campo "
                "eléctrico se almacena como energía potencial eléctrica e "
                "identificar el agente externo que genera diferencia de "
                "potencial eléctrico, el mismo que es capaz de generar "
                "trabajo al mover una carga positiva unitaria de un punto a "
                "otro dentro de un campo eléctrico."
            ),
            codigo="CN.F.5.1.46.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Conceptualizar la corriente eléctrica como la tasa a la "
                "cual fluyen las cargas a través de una superficie A de un "
                "conductor, mediante su expresión matemática y establecer "
                "que cuando se presenta un movimiento ordenado de cargas "
                "–corriente eléctrica- se transfiere energía desde la "
                "batería, la cual se puede transformar en calor, luz o en "
                "otra forma de energía."
            ),
            codigo="CN.F.5.1.47.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Analizar el origen atómico-molecular de la resistencia "
                "eléctrica en función de comprender que se origina por "
                "colisión de los electrones libres contra la red cristalina "
                "del material y definir resistencia eléctrica con la "
                "finalidad de explicar el significado de resistor óhmico."
            ),
            codigo="CN.F.5.1.48.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Describir la relación entre diferencia de potencial "
                "(voltaje), corriente y resistencia eléctrica, la ley de "
                "Ohm, mediante la comprobación de que la corriente en un "
                "conductor es proporcional al voltaje aplicado (donde R es "
                "la constante de proporcionalidad)."
            ),
            codigo="CN.F.5.1.49.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar que la batería produce una corriente directa en un "
                "circuito, a través de la determinación de su resistencia "
                "eléctrica e inferir que la diferencia de potencial entre "
                "sus bornes en circuito cerrado se llama FEM."
            ),
            codigo="CN.F.5.1.50.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Comprobar la ley de Ohm en circuitos sencillos a partir de "
                "la experimentación, analizar el funcionamiento de un "
                "circuito eléctrico sencillo y su simbología mediante la "
                "identificación de sus elementos constitutivos y la "
                "aplicación de dos de las grandes leyes de conservación (de "
                "la carga y de la energía) y explicar el calentamiento de "
                "Joule y su significado mediante la determinación de la "
                "potencia disipada en un circuito básico."
            ),
            codigo="CN.F.5.1.51.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Comprobar que los imanes solo se atraen o repelen en "
                "función de concluir que existen dos polos magnéticos, "
                "explicar la acción a distancia de los polos magnéticos en "
                "los imanes, así como también los polos magnéticos del "
                "planeta y experimentar con las líneas de campo cerradas."
            ),
            codigo="CN.F.5.1.52.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Determinar experimentalmente que cuando un imán en barra se "
                "divide en dos trozos se obtienen dos imanes, cada uno con "
                "sus dos polos (norte y sur) y que aún no se ha observado "
                "monopolos magnéticos libres (solo un polo norte o uno sur), "
                "reconoce que las únicas fuentes de campos magnéticos son "
                "los materiales magnéticos y las corrientes eléctricas, "
                "explica su presencia en dispositivos de uso cotidiano."
            ),
            codigo="CN.F.5.1.53.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Reconocer la naturaleza vectorial de un campo magnético, a "
                "través del análisis de sus características, determinar la "
                "intensidad del campo magnético en la solución de problemas "
                "de aplicación práctica, establecer la fuerza que ejerce el "
                "campo magnético uniforme sobre una partícula cargada que se "
                "mueve en su interior a partir de su expresión matemática."
            ),
            codigo="CN.F.5.1.54.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Explicar el funcionamiento del motor eléctrico por medio de "
                "la acción de fuerzas magnéticas sobre un objeto que lleva "
                "corriente ubicada en el interior de un campo magnético "
                "uniforme."
            ),
            codigo="CN.F.5.1.55.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Obtener la magnitud y dirección del campo magnético próximo "
                "a un conductor rectilíneo largo, en la resolución de "
                "ejercicios y problemas de aplicación."
            ),
            codigo="CN.F.5.1.56.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        Destreza(
            description=(
                "Conceptualizar la ley de Ampère, mediante la identificación "
                "de que la circulación de un campo magnético en un camino "
                "cerrado es directamente proporcional a la corriente "
                "eléctrica encerrada por el camino."
            ),
            codigo="CN.F.5.1.57.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque1_fisica
        ),
        # Bloque 2
        Destreza(
            description=(
                "Definir el trabajo mecánico a partir del análisis de la "
                "acción de una fuerza constante aplicada a un objeto que se "
                "desplaza en forma rectilínea, considerando solo el "
                "componente de la fuerza en la dirección del desplazamiento."
            ),
            codigo="CN.F.5.2.1.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Demostrar analíticamente que la variación de la energía "
                "mecánica representa el trabajo realizado por un objeto, "
                "utilizando la segunda ley de Newton y las leyes de la "
                "cinemática y la conservación de la energía, a través de la "
                "resolución de problemas que involucren el análisis de "
                "sistemas conservativos donde solo fuerzas conservativas "
                "efectúan trabajo."
            ),
            codigo="CN.F.5.2.2.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Explicar que las fuerzas disipativas o de fricción se "
                "definen como las que realizan un trabajo negativo al mover "
                "un objeto a lo largo de cualquier trayectoria cerrada."
            ),
            codigo="CN.F.5.2.3.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Determinar el concepto de potencia mediante la comprensión "
                "del ritmo temporal con que ingresa o se retira energía de "
                "un sistema."
            ),
            codigo="CN.F.5.2.4.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Determinar que la temperatura de un sistema es la medida de "
                "la energía cinética promedio de sus partículas, haciendo "
                "una relación con el conocimiento de que la energía térmica "
                "de un sistema se debe al movimiento caótico de sus "
                "partículas y por tanto a su energía cinética."
            ),
            codigo="CN.F.5.2.5.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Describir el proceso de transferencia de calor entre y "
                "dentro de sistemas por conducción, convección y/o "
                "radiación, mediante prácticas de laboratorio."
            ),
            codigo="CN.F.5.2.6.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Analizar que la variación de la temperatura de una "
                "sustancia que no cambia de estado es proporcional a la "
                "cantidad de energía añadida o retirada de la sustancia y "
                "que la constante de proporcionalidad representa el "
                "recíproco de la capacidad calorífica de la sustancia."
            ),
            codigo="CN.F.5.2.7.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Explicar mediante la experimentación el equilibrio térmico "
                "usando los conceptos de calor específico, cambio de estado, "
                "calor latente, temperatura de equilibrio, en situaciones "
                "cotidianas."
            ),
            codigo="CN.F.5.2.8.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Reconocer que un sistema con energía térmica tiene la "
                "capacidad de realizar trabajo mecánico deduciendo que, "
                "cuando el trabajo termina, cambia la energía interna del "
                "sistema, a partir de la experimentación (máquinas "
                "térmicas)."
            ),
            codigo="CN.F.5.2.9.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Reconocer mediante la experimentación de motores de "
                "combustión interna y eléctricos, que en sistemas mecánicos, "
                "las transferencias y transformaciones de la energía siempre "
                "causan pérdida de calor hacia el ambiente, reduciendo la "
                "energía utilizable, considerando que un sistema mecánico no "
                "puede ser ciento por ciento eficiente."
            ),
            codigo="CN.F.5.2.10.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        Destreza(
            description=(
                "Experimentar y determinar que la mayoría de los procesos "
                "tienden a disminuir el orden de un sistema conforme "
                "transcurre el tiempo."
            ),
            codigo="CN.F.5.2.11.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque2_fisica
        ),
        # Bloque 3
        Destreza(
            description=(
                "Describir las relaciones de los elementos de la onda: "
                "amplitud, periodo y frecuencia, mediante su representación "
                "en diagramas que muestren el estado de las perturbaciones "
                "para diferentes instantes."
            ),
            codigo="CN.F.5.3.1.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Reconocer que las ondas se propagan con una velocidad que "
                "depende de las propiedades físicas del medio de "
                "propagación, en función de determinar que esta velocidad, "
                "en forma cinemática, se expresa como el producto de "
                "frecuencia por longitud de onda."
            ),
            codigo="CN.F.5.3.2.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Clasificar los tipos de onda (mecánica o no mecánica) que "
                "requieren o no de un medio elástico para su propagación, "
                "mediante el análisis de las características y el "
                "reconocimiento de que la única onda no mecánica conocida es "
                "la onda electromagnética, diferenciando entre ondas "
                "longitudinales y transversales con relación a la dirección "
                "de oscilación y la dirección de propagación."
            ),
            codigo="CN.F.5.3.3.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Explicar fenómenos relacionados con la reflexión y "
                "refracción, utilizando el modelo de onda mecánica (en "
                "resortes o cuerdas) y formación de imágenes en lentes y "
                "espejos, utilizando el modelo de rayos."
            ),
            codigo="CN.F.5.3.4.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Explicar el efecto Doppler por medio del análisis de la "
                "variación en la frecuencia o en la longitud de una onda, "
                "cuando la fuente y el observador se encuentran en "
                "movimiento relativo."
            ),
            codigo="CN.F.5.3.5.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Explicar que la luz exhibe propiedades de onda pero también "
                "de partícula, en función de determinar que no se puede "
                "modelar como una onda mecánica porque puede viajar a través "
                "del espacio vacío, a una velocidad de aproximadamente "
                "3x108m/s y explicar las diferentes bandas de longitud de "
                "onda en el espectro de onda electromagnético, estableciendo "
                "relaciones con las aplicaciones en dispositivos de uso "
                "cotidiano."
            ),
            codigo="CN.F.5.3.6.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Identificar que se generan campos magnéticos en las "
                "proximidades de un flujo eléctrico variable y campos "
                "eléctricos en las proximidades de flujos magnéticos "
                "variables, mediante la descripción de la inducción de "
                "Faraday según corresponda."
            ),
            codigo="CN.F.5.3.7.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        Destreza(
            description=(
                "Analizar el mecanismo de radiación electromagnética, "
                "mediante la observación de videos relacionados y la "
                "ejemplificación con aparatos de uso cotidiano."
            ),
            codigo="CN.F.5.3.8.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque3_fisica
        ),
        # Bloque 4
        Destreza(
            description=(
                "Explicar las tres leyes de Kepler sobre el movimiento "
                "planetario, mediante la indagación del trabajo "
                "investigativo de Tycho Brahe y el análisis de sus datos "
                "referentes al planeta Marte."
            ),
            codigo="CN.F.5.4.1.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque4_fisica
        ),
        Destreza(
            description=(
                "Establecer la ley de gravitación universal de Newton y su "
                "explicación del sistema Copernicano y de las leyes de "
                "Kepler, para comprender el aporte de la misión geodésica "
                "francesa en el Ecuador, con el apoyo profesional de Don "
                "Pedro Vicente Maldonado en la confirmación de la ley de "
                "gravitación, identificando el problema de acción a "
                "distancia que plantea la ley de gravitación newtoniana y su "
                "explicación a través del concepto de campo gravitacional."
            ),
            codigo="CN.F.5.4.2.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque4_fisica
        ),
        Destreza(
            description=(
                "Indagar sobre el cinturón de Kuiper y la nube de Oort, en "
                "función de reconocer que en el Sistema Solar y en sus "
                "límites existen otros elementos como asteroides, cometas y "
                "meteoritos."
            ),
            codigo="CN.F.5.4.3.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque4_fisica
        ),
        Destreza(
            description=(
                "Indagar sobre la ubicación del Sistema Solar en la galaxia "
                "para reconocer que está localizado a tres cuartos del "
                "centro de la Vía Láctea, que tiene forma de disco (espiral "
                "barrada) con un diámetro aproximado de cien mil (100 000) "
                "años luz."
            ),
            codigo="CN.F.5.4.4.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque4_fisica
        ),
        # Bloque 5
        Destreza(
            description=(
                "Explicar los fenómenos: radiación de cuerpo negro y efecto "
                "fotoeléctrico mediante el modelo de la luz como partícula "
                "(el fotón) y que a escala atómica la radiación "
                "electromagnética se emite o absorbe en unidades discretas e "
                "indivisibles llamadas fotones, cuya energía es proporcional "
                "a su frecuencia (constante de Planck)."
            ),
            codigo="CN.F.5.5.1.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Explicar que las partículas a escala atómica o menores "
                "presentan un comportamiento ondulatorio, a partir de la "
                "investigación del experimento de difracción de electrones "
                "en un cristal."
            ),
            codigo="CN.F.5.5.2.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Discutir que, a escala atómica, se produce una dualidad "
                "onda-partícula y establecer que por tradición las "
                "ondas-partículas se llaman partículas cuánticas."
            ),
            codigo="CN.F.5.5.3.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Indagar sobre el principio de incertidumbre de Heisenberg, "
                "en función de reconocer que para las llamadas partículas "
                "cuánticas existe una incertidumbre al tratar de determinar "
                "su posición y velocidad (momento lineal) simultáneamente."
            ),
            codigo="CN.F.5.5.4.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Analizar el experimento de la doble rendija en tres casos: "
                "empleando balas, empleando ondas y con electrones para "
                "reconocer que con los conceptos clásicos de partícula y "
                "onda, no existe manera de explicar el comportamiento de los "
                "electrones."
            ),
            codigo="CN.F.5.5.5.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Identificar que los electrones y el núcleo atómico se "
                "encuentran unidos por fuerzas eléctricas en función de "
                "determinar su importancia en el desarrollo de la física "
                "nuclear."
            ),
            codigo="CN.F.5.5.6.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Distinguir que la radiactividad es el fenómeno por el cual "
                "el átomo radiactivo emite ciertas —radiaciones— y este se "
                "transforma en otro elemento químico (el objetivo de los "
                "alquimistas), y establecer que hay tres formas comunes de "
                "desintegración radiactiva (alfa, beta y gamma) debido a la "
                "acción de la fuerza nuclear débil, para analizar los "
                "efectos de la emisión de cada una."
            ),
            codigo="CN.F.5.5.7.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Explicar mediante la indagación científica la importancia "
                "de las fuerzas fundamentales de la naturaleza (nuclear "
                "fuerte, nuclear débil, electromagnética y gravitacional), "
                "en los fenómenos naturales y la vida cotidiana."
            ),
            codigo="CN.F.5.5.8.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Determinar que los quarks son partículas elementales del "
                "átomo que constituyen a los protones, neutrones y cientos "
                "de otras partículas subnucleares (llamadas colectivamente "
                "hadrones), en función de sus características."
            ),
            codigo="CN.F.5.5.9.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Explicar desde la indagación que el modelo estándar solo "
                "permite la unión entre dos (mesones), o tres (bariones) "
                "quarks, los avances en las investigaciones sobre la "
                "estructura pentaquark y sus implicaciones en la ciencia y "
                "la tecnología."
            ),
            codigo="CN.F.5.5.10.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Indagar los hallazgos experimentales de partículas "
                "semejantes al electrón y la necesidad de plantear la "
                "existencia de tres variedades de neutrinos (tipo electrón, "
                "tipo muon y tipo tauón), y explicar sus características "
                "reconociendo que aún no se conoce exactamente el verdadero "
                "valor de la masa."
            ),
            codigo="CN.F.5.5.11.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Explicar el efecto de las fuerzas electromagnética, nuclear "
                "fuerte y la débil a partir de las partículas llamadas "
                "—cuantos del campo de fuerza”, y que todas estas partículas "
                "poseen espín entero y por ello son bosones."
            ),
            codigo="CN.F.5.5.12.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Explicar que en el modelo estándar todas las partículas y "
                "fuerzas se describen por medio de campos (de la partícula o "
                "fuerza) cuantizados y que sus “cuantos” no tienen masa, y "
                "relacionar la obtención de la masa con el campo de Higgs."
            ),
            codigo="CN.F.5.5.13.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Discutir sobre el modelo estándar y reconocer que explica "
                "todo lo que se observa hasta ahora en el Universo, "
                "excluyendo a la gravedad, la materia oscura y la energía "
                "oscura."
            ),
            codigo="CN.F.5.5.14.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        Destreza(
            description=(
                "Discutir sobre las características de la materia oscura y "
                "la energía oscura que constituyen el mayor porcentaje de la "
                "materia y energía presentes en el Universo, en función de "
                "determinar que todavía no se conoce su naturaleza pero sí "
                "sus efectos."
            ),
            codigo="CN.F.5.5.15.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque5_fisica
        ),
        # Bloque 6
        Destreza(
            description=(
                "Explicar las aplicaciones de la trasmisión de energía e "
                "información en ondas en los equipos de uso diario, "
                "comunicación, información, entretenimiento, aplicaciones "
                "médicas y de seguridad."
            ),
            codigo="CN.F.5.6.1.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque6_fisica
        ),
        Destreza(
            description=(
                "Ejemplificar, dentro de las actividades humanas, los "
                "avances de la mecatrónica al servicio de la sociedad, que "
                "han facilitado las labores humanas con la finalidad de "
                "proponer alguna creación propia."
            ),
            codigo="CN.F.5.6.2.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque6_fisica
        ),
        Destreza(
            description=(
                "Establecer semejanzas y diferencias entre el movimiento de "
                "la Luna y de los satélites artificiales alrededor de la "
                "Tierra, mediante el uso de simuladores."
            ),
            codigo="CN.F.5.6.3.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque6_fisica
        ),
        Destreza(
            description=(
                "Analizar la incidencia del electromagnetismo, la mecánica "
                "cuántica y la nanotecnología en las necesidades de la "
                "sociedad contemporánea."
            ),
            codigo="CN.F.5.6.4.",
            imprescindible=True,
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque6_fisica
        ),
        Destreza(
            description=(
                "Analizar los efectos que tiene la tecnología en la "
                "revolución de las industrias, con el fin de concienciar que "
                "el uso indebido del conocimiento y en especial que la "
                "aplicación de leyes físicas generan perjuicios a la "
                "sociedad."
            ),
            codigo="CN.F.5.6.5.",
            asignatura=fisica,
            subnivel=bachillerato,
            bloque=bloque6_fisica
        ),
        # Biología
        # Bloque 1
        Destreza(
            description=(
                "Indagar y analizar la teoría de la abiogénesis que explica "
                "el origen de la vida, e interpretar las distintas "
                "evidencias científicas."
            ),
            codigo="CN.B.5.1.1.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Identificar los elementos y compuestos químicos de la "
                "atmósfera de la Tierra primitiva, y relacionarlos con la "
                "formación abiogénica de las moléculas orgánicas que forman "
                "parte de la materia viva."
            ),
            codigo="CN.B.5.1.2.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Indagar los procesos de abiogénesis de las moléculas y "
                "macromoléculas orgánicas en otros lugares del universo, "
                "formular hipótesis sobre las teorías de diversos "
                "científicos, y comunicar los resultados."
            ),
            codigo="CN.B.5.1.3.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Describir y comparar las características básicas de las "
                "biomoléculas a partir de sus procesos de síntesis y "
                "diversidad de polímeros."
            ),
            codigo="CN.B.5.1.4.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Usar modelos y describir la estructura, diversidad y "
                "función de las biomoléculas que constituyen la materia "
                "viva, y experimentar con procedimientos sencillos."
            ),
            codigo="CN.B.5.1.5.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Establecer las principales evidencias de las teorías "
                "científicas sobre la evolución biológica y analizar el rol "
                "de la evolución con el proceso responsable del cambio y "
                "diversificación de la vida en la Tierra."
            ),
            codigo="CN.B.5.1.6.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Analizar los procesos de variación, aislamiento y "
                "migración, relacionados con la selección natural, y "
                "explicar el proceso evolutivo."
            ),
            codigo="CN.B.5.1.7.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Indagar los criterios de clasificación taxonómica actuales "
                "y demostrar, por medio de la exploración, que los sistemas "
                "de clasificación biológica reflejan un ancestro común y "
                "relaciones evolutivas entre grupos de organismos, y "
                "comunicar los resultados."
            ),
            codigo="CN.B.5.1.8.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Analizar los tipos de diversidad biológica a nivel de "
                "genes, especies y ecosistemas, y plantear su importancia "
                "para el mantenimiento de la vida en el planeta."
            ),
            codigo="CN.B.5.1.9.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Analizar la relación de las diversas formas de vida con el "
                "proceso evolutivo, y deducir esta relación con la "
                "recopilación de datos comparativos y los resultados de "
                "investigaciones de campo realizadas por diversos "
                "científicos."
            ),
            codigo="CN.B.5.1.10.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Usar modelos y describir la función del ADN como portador "
                "de la información genética que controla las características "
                "de los organismos y la transmisión de la herencia, y "
                "relacionar el ADN con los cromosomas y los genes."
            ),
            codigo="CN.B.5.1.11.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Analizar la transcripción y traducción del ARN, e "
                "interpretar estos procesos como un flujo de información "
                "hereditaria desde el ADN."
            ),
            codigo="CN.B.5.1.12.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Experimentar con los procesos de mitosis, meiosis, y "
                "demostrar la trasmisión de la información genética a la "
                "descendencia por medio de la fertilización."
            ),
            codigo="CN.B.5.1.13.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Describir las leyes de Mendel, diseñar patrones de "
                "cruzamiento y deducir porcentajes genotípicos y fenotípicos "
                "en diferentes generaciones."
            ),
            codigo="CN.B.5.1.14.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Experimentar e interpretar las leyes y principios no "
                "mendelianos de cruzamientos en insectos y vegetales."
            ),
            codigo="CN.B.5.1.15.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Indagar la teoría cromosómica de la herencia, y "
                "relacionarla con las leyes de Mendel."
            ),
            codigo="CN.B.5.1.16.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Investigar las causas de los cambios del ADN que producen "
                "alteraciones génicas, cromosómicas y genómicas, e "
                "identificar semejanzas y diferencias entre estas."
            ),
            codigo="CN.B.5.1.17.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Indagar y describir los biomas del mundo e interpretarlos "
                "como sitios donde se evidencia la evolución de la "
                "biodiversidad en respuesta a los factores geográficos y "
                "climáticos."
            ),
            codigo="CN.B.5.1.18.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Indagar en estudios científicos la biodiversidad del "
                "Ecuador, analizar los patrones de evolución de las especies "
                "nativas y endémicas representativas de los diferentes "
                "ecosistemas, y explicar su megadiversidad."
            ),
            codigo="CN.B.5.1.19.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Reflexionar acerca de la importancia social, económica y "
                "ambiental de la biodiversidad, e identificar la "
                "problemática y los retos del Ecuador frente al manejo "
                "sostenible de su patrimonio natural."
            ),
            codigo="CN.B.5.1.20.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Indagar y examinar las diferentes actividades humanas que "
                "afectan a los sistemas globales, e inferir la pérdida de "
                "biodiversidad a escala nacional, regional y global."
            ),
            codigo="CN.B.5.1.21.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        Destreza(
            description=(
                "Interpretar las estrategias y políticas nacionales e "
                "internacionales para la conservación de la biodiversidad in "
                "situ y ex situ, y la mitigación de problemas ambientales "
                "globales, y generar una actitud crítica, reflexiva y "
                "responsable en favor del ambiente."
            ),
            codigo="CN.B.5.1.22.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque1_biologia
        ),
        # Bloque 2
        Destreza(
            description=(
                "Analizar las hipótesis sobre la evolución de las células "
                "procariotas y eucariotas basadas en la teoría de la "
                "endosimbiosis, y establecer semejanzas y diferencias entre "
                "ambos tipos de células."
            ),
            codigo="CN.B.5.2.1.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque2_biologia
        ),
        Destreza(
            description=(
                "Describir los tipos de organización en las células animales "
                "y vegetales, comparar experimentalmente sus diferencias, y "
                "establecer semejanzas y diferencias entre organelos."
            ),
            codigo="CN.B.5.2.2.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque2_biologia
        ),
        Destreza(
            description=(
                "Usar modelos y describir la estructura y función de los "
                "organelos de las células eucariotas y diferenciar sus "
                "funciones en procesos anabólicos y catabólicos."
            ),
            codigo="CN.B.5.2.3.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque2_biologia
        ),
        Destreza(
            description=(
                "Explicar la estructura, composición y función de la "
                "membrana celular para relacionarlas con los tipos de "
                "transporte celular por medio de la experimentación, y "
                "observar el intercambio de sustancias entre la célula y el "
                "medio que la rodea."
            ),
            codigo="CN.B.5.2.4.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque2_biologia
        ),
        Destreza(
            description=(
                "Analizar la acción enzimática en los procesos metabólicos a "
                "nivel celular y evidenciar experimentalmente la influencia "
                "de diversos factores en la velocidad de las reacciones."
            ),
            codigo="CN.B.5.2.5.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque2_biologia
        ),
        Destreza(
            description=(
                "Explorar y comparar la fotosíntesis y la respiración "
                "celular como procesos complementarios en función de "
                "reactivos, productos y flujos de energía a nivel celular."
            ),
            codigo="CN.B.5.2.6.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque2_biologia
        ),
        # Bloque 3
        Destreza(
            description=(
                "Observar la forma y función de células y tejidos en "
                "organismos multicelulares animales y vegetales, e "
                "identificar su organización en órganos, aparatos y "
                "sistemas."
            ),
            codigo="CN.B.5.3.1.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Relacionar los procesos respiratorio, circulatorio, "
                "digestivo, excretor, de osmorregulación y termorregulación "
                "en animales con diferente grado de complejidad, y comparar "
                "la evolución de sus estructuras en relación con sus "
                "funciones."
            ),
            codigo="CN.B.5.3.2.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Describir el sistema osteoartromuscular mediante la "
                "identificación de células, tejidos y componentes, y "
                "comparar sus características en diferentes animales."
            ),
            codigo="CN.B.5.3.3.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Describir los sistemas nervioso y endocrino en animales con "
                "diferente grado de complejidad, explicar su coordinación "
                "funcional para adaptarse y responder a estímulos del "
                "ambiente, y utilizar modelos científicos que demuestren la "
                "evolución de estos sistemas."
            ),
            codigo="CN.B.5.3.4.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Usar modelos y explicar la evolución del sistema "
                "inmunológico en los animales invertebrados y vertebrados, y "
                "comparar los componentes y distintas respuestas "
                "inmunológicas."
            ),
            codigo="CN.B.5.3.5.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Observar y analizar los procesos de reproducción de "
                "animales, elaborar modelos del desarrollo embrionario, e "
                "identificar el origen de las células y la diferenciación de "
                "las estructuras."
            ),
            codigo="CN.B.5.3.6.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Examinar la estructura y función de los sistemas de "
                "transporte en las plantas, y describir la provisión de "
                "nutrientes y la excreción de desechos."
            ),
            codigo="CN.B.5.3.7.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Describir los mecanismos de regulación del crecimiento y "
                "desarrollo vegetal, experimentar e interpretar las "
                "variaciones del crecimiento y del desarrollo por la acción "
                "de las hormonas vegetales y la influencia de factores "
                "externos."
            ),
            codigo="CN.B.5.3.8.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        Destreza(
            description=(
                "Observar y analizar los procesos de reproducción de las "
                "plantas, elaborar modelos del desarrollo embrionario, e "
                "identificar el origen de las células y la diferenciación de "
                "las estructuras."
            ),
            codigo="CN.B.5.3.9.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque3_biologia
        ),
        # Bloque 4
        Destreza(
            description=(
                "Analizar el funcionamiento de los sistemas digestivo y "
                "excretor en el ser humano y explicar la relación funcional "
                "entre estos sistemas con flujogramas."
            ),
            codigo="CN.B.5.4.1.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Diseñar investigaciones experimentales y reconocer el valor "
                "nutricional de diferentes alimentos de uso cotidiano según "
                "la composición de sus biomoléculas, y establecer sus "
                "efectos en el metabolismo y la salud humana."
            ),
            codigo="CN.B.5.4.2.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Analizar y aplicar buenas prácticas que contribuyen a "
                "mantener un cuerpo saludable, y elaborar un plan de salud "
                "que considere una alimentación balanceada de acuerdo a su "
                "edad y actividad para asegurar su salud integral."
            ),
            codigo="CN.B.5.4.3.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Indagar acerca de las enfermedades nutricionales y "
                "desórdenes alimenticios más comunes que afectan a la "
                "población ecuatoriana, diseñar y ejecutar una investigación "
                "en relación a estas, su vínculo con la dimensión "
                "psicológica y comunicar por diferentes medios las medidas "
                "preventivas en cuanto a salud y nutrición."
            ),
            codigo="CN.B.5.4.4.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Usar modelos y describir los sistemas circulatorio y "
                "respiratorio en el ser humano, y establecer la relación "
                "funcional entre ellos, la cual mantiene el equilibrio "
                "homeostático."
            ),
            codigo="CN.B.5.4.5.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Indagar en diversas fuentes y sintetizar información sobre "
                "las enfermedades causadas por el consumo de tabaco, la "
                "falta de ejercicio, la exposición a contaminantes "
                "ambientales y a alimentos contaminados, y proponer medidas "
                "preventivas y la práctica de buenos hábitos."
            ),
            codigo="CN.B.5.4.6.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Usar modelos y describir el sistema osteoartromuscular del "
                "ser humano, en cuanto a su estructura y función, y proponer "
                "medidas para su cuidado."
            ),
            codigo="CN.B.5.4.7.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Establecer la relación entre la estructura y función del "
                "sistema nervioso y del sistema endocrino, en cuanto a su "
                "fisiología y la respuesta a la acción hormonal."
            ),
            codigo="CN.B.5.4.8.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Indagar en diversas fuentes sobre los efectos nocivos en el "
                "sistema nervioso ocasionados por el consumo de alcohol y "
                "otras drogas, y proponer medidas preventivas."
            ),
            codigo="CN.B.5.4.9.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Analizar las causas y consecuencias de las enfermedades que "
                "afectan al sistema neuroendocrino, y proponer medidas "
                "preventivas."
            ),
            codigo="CN.B.5.4.10.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Interpretar la respuesta del cuerpo humano frente a "
                "microorganismos patógenos, describir el proceso de "
                "respuesta inmunitaria e identificar las anomalías de este "
                "sistema."
            ),
            codigo="CN.B.5.4.11.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Analizar la fecundación humana, concepción, el desarrollo "
                "embrionario y fetal, parto y aborto, y explicar de forma "
                "integral la función de la reproducción humana."
            ),
            codigo="CN.B.5.4.12.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Indagar acerca del crecimiento y desarrollo del ser humano, "
                "reflexionar sobre la sexualidad, la promoción, prevención y "
                "protección de la salud sexual, reproductiva y afectiva."
            ),
            codigo="CN.B.5.4.13.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        Destreza(
            description=(
                "Relacionar la salud sexual y reproductiva con las "
                "implicaciones en el proyecto de vida."
            ),
            codigo="CN.B.5.4.14.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque4_biologia
        ),
        # Bloque 5
        Destreza(
            description=(
                "Explicar los sustentos teóricos de científicos sobre el "
                "origen de la vida y refutar la teoría de la generación "
                "espontánea sobre la base de experimentos sencillos."
            ),
            codigo="CN.B.5.5.1.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Indagar sobre la evolución de los pinzones de Galápagos que "
                "sustentó la teoría de la selección natural de Darwin, y "
                "analizar que se complementa con la teoría sintética de la "
                "evolución, propuesta por científicos contemporáneos."
            ),
            codigo="CN.B.5.5.2.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Analizar la selección artificial en el proceso de "
                "domesticación del maíz y del perro, y explicar los impactos "
                "de este tipo de selección en la actualidad."
            ),
            codigo="CN.B.5.5.3.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Indagar sobre el desarrollo de la Biotecnología en el campo "
                "de la Medicina y la Agricultura, e interpretar su "
                "aplicación en el mejoramiento de la alimentación y la "
                "nutrición de las personas."
            ),
            codigo="CN.B.5.5.4.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Indagar y elaborar una línea de tiempo del desarrollo "
                "histórico de la genética, desde las leyes de Mendel hasta "
                "el Proyecto Genoma Humano, y explicar su aporte para la "
                "salud humana."
            ),
            codigo="CN.B.5.5.5.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Indagar sobre la genética de poblaciones, analizar e "
                "inferir los resultados de binomios genéticos."
            ),
            codigo="CN.B.5.5.6.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Buscar, registrar y sistematizar información de diversas "
                "fuentes sobre el cáncer, y relacionarlo con el proceso de "
                "proliferación celular alterada."
            ),
            codigo="CN.B.5.5.7.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Indagar las aplicaciones de la ingeniería genética en la "
                "producción de alimentos y fármacos, sus implicaciones en la "
                "vida actual, y explicar el efecto de la terapia génica en "
                "el tratamiento de enfermedades humanas, considerando los "
                "cuestionamientos éticos y sociales."
            ),
            codigo="CN.B.5.5.8.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Indagar sobre los programas de salud pública sustentados en "
                "políticas estatales y en investigaciones socioeconómicas, y "
                "analizar sobre la importancia de la accesibilidad a la "
                "salud individual y colectiva, especialmente para "
                "poblaciones marginales, aisladas o de escasos recursos."
            ),
            codigo="CN.B.5.5.9.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Interpretar modelos poblacionales que relacionan el "
                "crecimiento poblacional con diferentes modelos de "
                "desarrollo económico, y tomar una postura frente al enfoque "
                "del uso sostenible de los recursos naturales."
            ),
            codigo="CN.B.5.5.10.",
            imprescindible=True,
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        Destreza(
            description=(
                "Planificar y ejecutar una investigación sobre los "
                "diferentes avances tecnológicos que cubren las necesidades "
                "de la creciente población humana, con un enfoque de "
                "desarrollo sostenible."
            ),
            codigo="CN.B.5.5.11.",
            asignatura=biologia,
            subnivel=bachillerato,
            bloque=bloque5_biologia
        ),
        # Química
        # Bloque 1
        Destreza(
            description=(
                "Analizar y clasificar las propiedades de los gases que se "
                "generan en la industria y aquellos que son más comunes en "
                "la vida y que inciden en la salud y el ambiente."
            ),
            codigo="CN.Q.5.1.1.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Examinar las leyes que rigen el comportamiento de los gases "
                "desde el análisis experimental y la interpretación de "
                "resultados, para reconocer los procesos físicos que ocurren "
                "en la cotidianidad."
            ),
            codigo="CN.Q.5.1.2.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Observar y comparar la teoría de Bohr con las teorías "
                "atómicas de Demócrito, Dalton, Thompson y Rutherford."
            ),
            codigo="CN.Q.5.1.3.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Deducir y comunicar que la teoría de Bohr del átomo de "
                "hidrógeno explica la estructura lineal de los espectros de "
                "los elementos químicos, partiendo de la observación, "
                "comparación y aplicación de los espectros de absorción y "
                "emisión con información obtenida a partir de las TIC."
            ),
            codigo="CN.Q.5.1.4.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Observar y aplicar el modelo mecánico-cuántico de la "
                "materia en la estructuración de la configuración "
                "electrónica de los átomos considerando la dualidad del "
                "electrón, los números cuánticos, los tipos de orbitales y "
                "la regla de Hund."
            ),
            codigo="CN.Q.5.1.5.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Relacionar la estructura electrónica de los átomos con la "
                "posición en la tabla periódica, para deducir las "
                "propiedades químicas de los elementos."
            ),
            codigo="CN.Q.5.1.6.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Comprobar y experimentar con base en prácticas de "
                "laboratorio y revisiones bibliográficas la variación "
                "periódica de las propiedades físicas y químicas de los "
                "elementos químicos en dependencia de la estructura "
                "electrónica de sus átomos."
            ),
            codigo="CN.Q.5.1.7.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Deducir y explicar la unión de átomos por su tendencia a "
                "donar, recibir o compartir electrones para alcanzar la "
                "estabilidad del gas noble más cercano, según la teoría de"
                "Kössel y Lewis."
            ),
            codigo="CN.Q.5.1.8.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Observar y clasificar el tipo de enlaces químicos y su "
                "fuerza partiendo del análisis de la relación existente "
                "entre la capacidad de transferir y compartir electrones y "
                "la configuración electrónica, con base en los valores de la "
                "electronegatividad."
            ),
            codigo="CN.Q.5.1.9.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Deducir y explicar las propiedades físicas de compuestos "
                "iónicos y covalentes desde el análisis de su estructura y "
                "el tipo de enlace que une a los átomos, así como de la "
                "comparación de las propiedades de sustancias comúnmente "
                "conocidas."
            ),
            codigo="CN.Q.5.1.10.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Establecer y diferenciar las fuerzas intermoleculares "
                "partiendo de la descripción del puente de hidrógeno, "
                "fuerzas de London y de Van der Walls, y dipolo-dipolo."
            ),
            codigo="CN.Q.5.1.11.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Deducir y predecir la posibilidad de formación de "
                "compuestos químicos, con base en el estado natural de los "
                "elementos, su estructura electrónica y su ubicación en la "
                "tabla periódica."
            ),
            codigo="CN.Q.5.1.12.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Interpretar las reacciones químicas como la reorganización "
                "y recombinación de los átomos con transferencia de energía, "
                "mediante la observación y cuantificación de átomos que "
                "participan en los reactivos y en los productos."
            ),
            codigo="CN.Q.5.1.13.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Comparar los tipos de reacciones químicas: combinación, "
                "descomposición, desplazamiento, exotérmicas y endotérmicas, "
                "partiendo de la experimentación, análisis e interpretación "
                "de los datos registrados y la complementación de "
                "información bibliográfica y procedente de las TIC."
            ),
            codigo="CN.Q.5.1.14.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Explicar que el carbono es un átomo excepcional, desde la "
                "observación y comparación de las propiedades de algunas de "
                "sus variedades alotrópicas y el análisis de las fórmulas de "
                "algunos compuestos."
            ),
            codigo="CN.Q.5.1.15.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Relacionar la estructura del átomo de carbono con su "
                "capacidad de formar enlaces de carbono-carbono, con la "
                "observación y descripción de modelos moleculares."
            ),
            codigo="CN.Q.5.1.16.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición de las moléculas "
                "orgánicas, las propiedades generales de los compuestos "
                "orgánicos y su diversidad, expresadas en fórmulas que "
                "indican la clase de átomos que las conforman, la cantidad "
                "de cada uno de ellos, los tipos de enlaces que los unen e "
                "incluso la estructura de las moléculas."
            ),
            codigo="CN.Q.5.1.17.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Categorizar y clasificar a los hidrocarburos por su "
                "composición, su estructura, el tipo de enlace que une a los "
                "átomos de carbono y el análisis de sus propiedades físicas "
                "y su comportamiento químico."
            ),
            codigo="CN.Q.5.1.18.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Clasificar, formular y nominar a los hidrocarburos "
                "alifáticos partiendo del análisis del número de carbonos, "
                "tipo y número de enlaces que están presentes en la cadena "
                "carbonada."
            ),
            codigo="CN.Q.5.1.19.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar a los alcanos, alquenos y alquinos "
                "por su estructura molecular, sus propiedades físicas y "
                "químicas en algunos productos de uso cotidiano (gas "
                "doméstico, kerosene, espelmas, eteno, acetileno)."
            ),
            codigo="CN.Q.5.1.20.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Explicar e interpretar la estructura de los compuestos "
                "aromáticos, particularmente del benceno, desde el análisis "
                "de su estructura molecular, propiedades físicas y "
                "comportamiento químico."
            ),
            codigo="CN.Q.5.1.21.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Clasificar y analizar las series homólogas, desde la "
                "estructura de los compuestos orgánicos, por el tipo de "
                "grupo funcional que posee y sus propiedades particulares."
            ),
            codigo="CN.Q.5.1.22.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Comparar las propiedades físicas y químicas de los "
                "compuestos oxigenados: alcoholes, aldehídos, ácidos, "
                "cetonas y éteres, mediante el análisis de sus grupos "
                "funcionales, usando las TIC."
            ),
            codigo="CN.Q.5.1.23.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Interpretar y analizar las reacciones de oxidación y "
                "reducción como la transferencia de electrones que "
                "experimentan los elementos."
            ),
            codigo="CN.Q.5.1.24.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Deducir el número o índice de oxidación de cada elemento "
                "que forma parte del compuesto químico e interpretar las "
                "reglas establecidas para determinar el número de oxidación."
            ),
            codigo="CN.Q.5.1.25.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Aplicar y experimentar diferentes métodos de igualación de "
                "ecuaciones tomando en cuenta el cumplimiento de la ley de "
                "la conservación de la masa y la energía, así como las "
                "reglas de número de oxidación en la igualación de las "
                "ecuaciones de óxido-reducción."
            ),
            codigo="CN.Q.5.1.26.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Examinar la diferente actividad de los metales, mediante la "
                "observación e interpretación de los fenómenos que se "
                "producen en la experimentación con agua y ácidos diluidos."
            ),
            codigo="CN.Q.5.1.27.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Determinar y comparar la velocidad de las reacciones "
                "químicas mediante la variación de factores como la "
                "concentración de uno de los reactivos, el incremento de "
                "temperatura y el uso de algún catalizador, para deducir su "
                "importancia."
            ),
            codigo="CN.Q.5.1.28.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        Destreza(
            description=(
                "Comparar y examinar las reacciones reversibles e "
                "irreversibles en función del equilibrio químico y la "
                "diferenciación del tipo de electrolitos que constituyen los "
                "compuestos químicos reaccionantes y los productos."
            ),
            codigo="CN.Q.5.1.29.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque1_quimica
        ),
        # Bloque 2
        Destreza(
            description=(
                "Analizar y clasificar los compuestos químicos binarios que "
                "tienen posibilidad de formarse entre dos elementos de "
                "acuerdo a su ubicación en la tabla periódica, su estructura "
                "electrónica y sus posibles grados de oxidación para deducir "
                "las fórmulas que los representan."
            ),
            codigo="CN.Q.5.2.1.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Comparar y examinar los valores de valencia y número de "
                "oxidación, partiendo del análisis de la electronegatividad, "
                "del tipo de enlace intramolecular y de las representaciones "
                "de Lewis de los compuestos químicos."
            ),
            codigo="CN.Q.5.2.2.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición, formulación y "
                "nomenclatura de los óxidos, así como el método a seguir "
                "para su obtención (vía directa o indirecta) mediante la "
                "identificación del estado natural de los elementos a "
                "combinar y la estructura electrónica de los mismos."
            ),
            codigo="CN.Q.5.2.3.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición, formulación y "
                "nomenclatura de los hidróxidos, diferenciar los métodos de "
                "obtención de los hidróxidos de los metales alcalinos del "
                "resto de metales e identificar la función de estos "
                "compuestos según"
                "la teoría de Brönsted-Lowry."
            ),
            codigo="CN.Q.5.2.4.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición, formulación y "
                "nomenclatura de los ácidos: hidrácidos y oxácidos, e "
                "identificar la función de estos compuestos según la teoría "
                "de"
                "Brönsted-Lowry."
            ),
            codigo="CN.Q.5.2.5.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición, formulación y "
                "nomenclatura de las sales, identificar claramente si "
                "provienen de un ácido oxácido o un hidrácido y utilizar "
                "correctamente los aniones simples o complejos, reconociendo "
                "la estabilidad de estos en la formación de distintas sales."
            ),
            codigo="CN.Q.5.2.6.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición, formulación y "
                "nomenclatura de los hidruros, diferenciar los metálicos de "
                "los no metálicos y estos últimos de los ácidos hidrácidos, "
                "resaltando las diferentes propiedades."
            ),
            codigo="CN.Q.5.2.7.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Deducir y comunicar que las ecuaciones químicas son las "
                "representaciones escritas de las reacciones que expresan "
                "todos los fenómenos y transformaciones que se producen."
            ),
            codigo="CN.Q.5.2.8.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Experimentar y deducir el cumplimiento de las leyes de "
                "transformación de la materia: leyes ponderales y de la "
                "conservación de la materia que rigen la formación de "
                "compuestos químicos."
            ),
            codigo="CN.Q.5.2.9.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Calcular y establecer la masa molecular de compuestos "
                "simples a partir de la masa atómica de sus componentes, "
                "para evidenciar que estas medidas son inmanejables en la "
                "práctica y que por tanto es necesario usar unidades de "
                "medida mayores, como el mol."
            ),
            codigo="CN.Q.5.2.10.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Utilizar el número de Avogadro en la determinación de la "
                "masa molar de varios elementos y compuestos químicos y "
                "establecer la diferencia con la masa de un átomo y una "
                "molécula."
            ),
            codigo="CN.Q.5.2.11.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y clasificar la composición porcentual de los "
                "compuestos químicos basándose en sus relaciones "
                "moleculares."
            ),
            codigo="CN.Q.5.2.12.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Examinar y aplicar el método más apropiado para balancear "
                "las ecuaciones químicas basándose en la escritura correcta "
                "de las fórmulas químicas y el conocimiento del rol que "
                "desempeñan los coeficientes y subíndices, para utilizarlos "
                "o modificarlos correctamente."
            ),
            codigo="CN.Q.5.2.13.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Establecer y examinar el comportamiento de los grupos "
                "funcionales en los compuestos orgánicos como parte de la "
                "molécula, que determina la reactividad y las propiedades "
                "químicas de los compuestos."
            ),
            codigo="CN.Q.5.2.14.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Diferenciar las fórmulas empíricas, moleculares, "
                "semidesarrolladas y desarrolladas y explicar la importancia "
                "de su uso en cada caso."
            ),
            codigo="CN.Q.5.2.15.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Analizar y aplicar los principios en los que se basa la "
                "nomenclatura de los compuestos orgánicos en algunas "
                "sustancias de uso cotidiano con sus nombres comerciales."
            ),
            codigo="CN.Q.5.2.16.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        Destreza(
            description=(
                "Establecer y analizar las diferentes clases de isomería "
                "resaltando sus principales características y explicando la "
                "actividad de los isómeros, mediante la interpretación de "
                "imágenes, ejemplos típicos y lecturas científicas."
            ),
            codigo="CN.Q.5.2.17.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque2_quimica
        ),
        # Bloque 3
        Destreza(
            description=(
                "Examinar y clasificar las características de los distintos "
                "tipos de sistemas dispersos según el estado de agregación "
                "de sus componentes y el tamaño de las partículas de la fase "
                "dispersa."
            ),
            codigo="CN.Q.5.3.1.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Comparar y analizar disoluciones de diferente concentración "
                "mediante la elaboración de soluciones de uso común."
            ),
            codigo="CN.Q.5.3.2.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Determinar y examinar la importancia de las reacciones "
                "ácido-base en la vida cotidiana."
            ),
            codigo="CN.Q.5.3.3.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Analizar y deducir a partir de la comprensión del "
                "significado de la acidez, la forma de su determinación y su "
                "importancia en diferentes ámbitos de la vida, como la "
                "aplicación de los antiácidos y el balance del pH estomacal, "
                "en la industria y en la agricultura, con ayuda de las TIC."
            ),
            codigo="CN.Q.5.3.4.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Deducir y comunicar la importancia del pH a través de la "
                "medición de este parámetro en varias soluciones de uso "
                "diario."
            ),
            codigo="CN.Q.5.3.5.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Diseñar y experimentar el proceso de desalinización en el "
                "hogar o en la comunidad como estrategia para la obtención "
                "de agua dulce."
            ),
            codigo="CN.Q.5.3.6.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Explicar y examinar el origen, la composición e importancia "
                "del petróleo, no solo como fuente de energía, sino como "
                "materia prima para la elaboración de una gran cantidad de "
                "productos, a partir del uso de las TIC."
            ),
            codigo="CN.Q.5.3.7.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Investigar y comunicar la importancia de los polímeros "
                "artificiales en sustitución de productos naturales en la "
                "industria y su aplicabilidad en la vida cotidiana, así como "
                "sus efectos negativos partiendo de la investigación en "
                "diferentes fuentes."
            ),
            codigo="CN.Q.5.3.8.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Examinar y explicar los símbolos que indican la presencia "
                "de los compuestos aromáticos y aplicar las medidas de "
                "seguridad recomendadas para su manejo."
            ),
            codigo="CN.Q.5.3.9.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Examinar y explicar la importancia de los alcoholes, "
                "aldehídos, cetonas y éteres en la industria, en la medicina "
                "y la vida diaria (solventes como la acetona, el alcohol, "
                "algunos éteres como antiséptico en quirófanos), así como el "
                "peligro de su empleo no apropiado (incidencia del alcohol "
                "en la química cerebral, muerte por ingestión del alcohol "
                "metílico)."
            ),
            codigo="CN.Q.5.3.10.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Examinar y comunicar la importancia de los ácidos "
                "carboxílicos grasos y ésteres, de las amidas y aminas, de "
                "los glúcidos, lípidos, proteínas y aminoácidos para el ser "
                "humano en la vida diaria, en la industria y en la medicina, "
                "así como las alteraciones que puede causar la deficiencia o "
                "exceso de su consumo, por ejemplo de las anfetaminas, para "
                "valorar la trascendencia de una dieta diaria balanceada, "
                "mediante el uso de las TIC."
            ),
            codigo="CN.Q.5.3.11.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Establecer y comunicar los factores que inciden en la "
                "velocidad de la corrosión y sus efectos, para adoptar "
                "métodos de prevención."
            ),
            codigo="CN.Q.5.3.12.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Examinar y comunicar los contaminantes y los efectos que "
                "producen en el entorno natural y la salud humana basándose "
                "en su toxicidad y su permanencia en el ambiente; y difundir "
                "el uso de prácticas ambientalmente amigables que se pueden "
                "utilizar en la vida diaria."
            ),
            codigo="CN.Q.5.3.13.",
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
        Destreza(
            description=(
                "Examinar y explicar la utilidad de algunos biomateriales "
                "para mejorar la calidad de vida de los seres humanos."
            ),
            codigo="CN.Q.5.3.14.",
            imprescindible=True,
            asignatura=quimica,
            subnivel=bachillerato,
            bloque=bloque3_quimica
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0032_auto_20180814_0732'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
