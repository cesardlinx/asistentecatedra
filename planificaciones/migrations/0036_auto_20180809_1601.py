from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    educacion_cultural = Asignatura.objects.get(
        name="Educación Cultural y Artística")

    # Bloques
    bloque1 = BloqueCurricular.objects.get(name="El yo: la identidad")
    bloque2 = BloqueCurricular.objects.get(
        name="El encuentro con otros: la alteridad"
    )
    bloque3 = BloqueCurricular.objects.get(
        name="El entorno: espacio, tiempo y objetos"
    )

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')

    Destreza.objects.bulk_create([
        # Preparatoria
        # Bloque 1
        Destreza(
            description=(
                "Practicar juegos sensoriomotores y expresar las emociones "
                "que estos suscitan a través de las acciones y los "
                "movimientos corporales."
            ),
            codigo="ECA.1.1.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Expresar la propia identidad, emociones y sentimientos a "
                "través del juego simbólico en su dimensión personal y "
                "libre, identificándose con personajes fantásticos o "
                "cotidianos."
            ),
            codigo="ECA.1.1.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Explorar las posibilidades sonoras de la voz, del propio "
                "cuerpo, de elementos de la naturaleza y de los objetos, y "
                "utilizar los sonidos encontrados en procesos de "
                "improvisación y creación musical libre y dirigida."
            ),
            codigo="ECA.1.1.3.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Utilizar la expresión gráfica o plástica como recurso para "
                "la expresión libre del yo, de la historia personal de cada "
                "uno."
            ),
            codigo="ECA.1.1.4.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Participar activamente en situaciones que posibiliten el "
                "desarrollo de la sensorialidad, experimentando con "
                "distintos olores, sabores, imágenes, texturas, sonidos, "
                "etc. del entorno próximo, natural y/o artificial."
            ),
            codigo="ECA.1.1.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Ejecutar movimientos locomotores (andar, correr, saltar, "
                "reptar, rodar, etc.) y funcionales en actividades de "
                "expresión corporal y juego libre y dirigido, para expresar "
                "sentimientos e ideas y descubrir las posibilidades del "
                "propio cuerpo."
            ),
            codigo="ECA.1.1.6.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Describir el propio cuerpo y explicar sensaciones y "
                "emociones a través de representaciones gráficas y de la "
                "palabra hablada."
            ),
            codigo="ECA.1.1.7.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Practicar juegos de luces y sombras, juegos en el espejo y "
                "otras actividades lúdicas que den lugar al encuentro con la "
                "imagen propia."
            ),
            codigo="ECA.1.1.8.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Registrar la imagen propia a través de autorretratos "
                "dibujados o fotografías."
            ),
            codigo="ECA.1.1.9.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Participar en situaciones de juego dramático para situarse, "
                "narrarse y ponerse en el lugar del otro contar historias "
                "con el otro y jugar a ser otras personas."
            ),
            codigo="ECA.1.2.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Danzar y participar en actividades de expresión corporal y "
                "movimiento que posibiliten el encuentro con el otro para "
                "compartir, llegar a acuerdos, tomar contacto y "
                "relacionarse."
            ),
            codigo="ECA.1.2.2.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Cantar y hacer música en grupo con sonidos corporales y/o "
                "producidos con objetos naturales (hojas o tallos de cebada, "
                "piedras, agua, etc.) o artificiales, disfrutando del "
                "encuentro con los otros y el sentimiento de pertenencia a "
                "un colectivo."
            ),
            codigo="ECA.1.2.3.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Producir obras plásticas o gráficas en grupo, llegando a "
                "acuerdos, respetando las opiniones de los otros y "
                "contribuyendo a la consecución de resultados."
            ),
            codigo="ECA.1.2.4.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar construcciones colectivas, como proyectos de "
                "ocupación del espacio compartido."
            ),
            codigo="ECA.1.2.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Relatar la historia colectiva o del nosotros a través de la "
                "palabra hablada, describiendo sensaciones, experiencias, "
                "emociones o proyectos colectivos."
            ),
            codigo="ECA.1.2.6.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Practicar juegos y actividades que posibiliten la "
                "observación del otro y del grupo, generando la noción de "
                "imagen compartida."
            ),
            codigo="ECA.1.2.7.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Dramatizar narraciones con un principio y un final "
                "reconocibles, con o sin diálogos, con personajes reales o "
                "simbólicos, consensuados y elegidos."
            ),
            codigo="ECA.1.3.1.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Expresar las ideas y emociones que suscita la observación "
                "de algunas manifestaciones culturales y artísticas "
                "(rituales, actos festivos, danzas, conocimientos y "
                "prácticas relativos a la naturaleza, artesanías, etc.), "
                "presentes en el entorno próximo."
            ),
            codigo="ECA.1.3.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Expresar corporal o gráficamente lo que sugieren piezas "
                "musicales de distintas épocas y culturas, incluyendo la "
                "propia."
            ),
            codigo="ECA.1.3.3.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Describir de manera sencilla los significados de imágenes "
                "delcontexto próximo que forman parte de la cultura visual."
            ),
            codigo="ECA.1.3.4.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Observar, en vivo, en grabaciones y en otros documentos "
                "gráficos y audiovisuales, las tareas que realizan algunos "
                "profesionales del arte y la cultura local(artesanos, "
                "músicos, actores, etc.), y nombrar algunas de ellas."
            ),
            codigo="ECA.1.3.5.",
            asignatura=educacion_cultural,
            subnivel=preparatoria,
            bloque=bloque3,
        ),
        # Elemental
        # Bloque 1
        Destreza(
            description=(
                "Experimentar con las posibilidades del color y del gesto "
                "espontáneo al plasmar la silueta del cuerpo, y las huellas "
                "de las manos y los pies sobre soportes diversos(papel, "
                "cartón, cartulina), de diferentes medidas, y sirviéndose de "
                "distintos materiales(pintura, arcilla, plantas, etc.)."
            ),
            codigo="ECA.2.1.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Definir la individualidad incorporando todos los elementos "
                "que se crean necesarios (un anillo en las manos, una flor "
                "en el pecho, una cara sin rostro, un pie verde y otro azul, "
                "etc.) a las representaciones gráficas del cuerpo."
            ),
            codigo="ECA.2.1.2.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reflexionar sobre los resultados obtenidos al representar "
                "el propio cuerpo y exponerlos de forma oral."
            ),
            codigo="ECA.2.1.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Experimentar la percepción de olores, sonidos, sabores y "
                "texturas por medio de juegos sensoriales, en los que se "
                "adivine qué es lo que se saborea, se huele, se oye o se "
                "toca."
            ),
            codigo="ECA.2.1.4.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Recrear percepciones sensoriales por medio del movimiento y "
                "la representación visual y sonora, sirviéndose de "
                "sinestesias como: pintar lo amargo, tocar lo dulce, poner "
                "sonido a lo rugoso, darle movimiento al color rojo, bailar "
                "una pintura, etc."
            ),
            codigo="ECA.2.1.5.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Explorar las posibilidades del cuerpo en movimiento en "
                "respuesta a estímulos diversos (recorridos, relatos, "
                "imágenes, piezas musicales, sonidos, etc.)."
            ),
            codigo="ECA.2.1.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Nombrar las características de texturas naturales y "
                "artificiales, como resultado de un proceso de exploración "
                "visual y táctil, y recrear sus posibilidades en la "
                "invención de texturas nuevas."
            ),
            codigo="ECA.2.1.7.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Describir las características y las sensaciones que "
                "producen algunos elementos presentes en el entorno natural "
                "(plantas, árboles, minerales, animales, agua, sonidos), "
                "como resultado de un proceso de exploración sensorial."
            ),
            codigo="ECA.2.1.8.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Explorar, a través de los sentidos, las cualidades y "
                "posibilidades de los materiales orgánicos e inorgánicos, y "
                "utilizarlos para la creación de producciones plásticas, "
                "títeres, objetos sonoros, etc."
            ),
            codigo="ECA.2.1.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Representar la propia vivienda mediante dibujos, maquetas, "
                "construcciones con materiales, etc. y describir verbalmente "
                "sus principales características."
            ),
            codigo="ECA.2.1.10.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Interpretar en pequeños grupos historias breves, inspiradas "
                "en situaciones próximas, relatos oídos, anécdotas vividas o "
                "cuentos leídos, llegando a acuerdos sobre el desarrollo de "
                "la acción y sobre algunos elementos visuales y sonoros para "
                "caracterizar espacios y personajes."
            ),
            codigo="ECA.2.2.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Practicar juegos rítmicos (rondas infantiles, juegos "
                "tradicionales de las distintas nacionalidades del Ecuador, "
                "juegos de manos, etc.) que posibiliten el desarrollo de "
                "diferentes habilidades motrices."
            ),
            codigo="ECA.2.2.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Crear coreografías a partir de la improvisación de los "
                "movimientos sugeridos por distintas piezas musicales, "
                "explorando diferentes posibilidades de interacción "
                "(dirigir, seguir, acercarse, alejarse, etc.) con los "
                "miembros del grupo."
            ),
            codigo="ECA.2.2.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Observar y comparar distintas representaciones del entorno "
                "natural y artificial (fotografía aérea, pintura de "
                "paisajes, dibujos, planos de viviendas, maquetas de "
                "edificios, mapas, grabaciones y mapas sonoros, videos, "
                "etc.)."
            ),
            codigo="ECA.2.2.4.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar representaciones propias, individuales o en grupo "
                "del entorno natural y artificial, utilizando distintas "
                "técnicas."
            ),
            codigo="ECA.2.2.5.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Observar creaciones en las que se usen elementos del "
                "entorno natural y artificial (producciones de land art, "
                "construcción de instrumentos musicales con vegetales, etc.) "
                "y comentar sus características."
            ),
            codigo="ECA.2.2.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Utilizar elementos del entorno natural y artificial "
                "(madera, hojas, piedras, etc.) en la creación colectiva de "
                "producciones artísticas sencillas."
            ),
            codigo="ECA.2.2.7.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Observar esculturas sonoras y, en pequeños grupos, "
                "construir algunas pensadas para distintos espacios (el "
                "hogar, el colegio, parques u otros espacios comunitarios); "
                "instalarlas y observar el uso que hacen de ellas los "
                "habitantes o transeúntes."
            ),
            codigo="ECA.2.2.8.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Representar cuentos, mitos, leyendas, historias y relatos "
                "con títeres o marionetas construidos en el aula, "
                "coordinando la propia acción con la de los otros y llegando "
                "a acuerdos tanto en el proceso de construcción como en los "
                "ensayos y la representación."
            ),
            codigo="ECA.2.2.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Representar, por medio de dramatizaciones, ilustraciones o "
                "secuencias sonoras, el resultado de incluir, en cuentos o "
                "historias tradicionales de las distintas nacionalidades del "
                "Ecuador, personajes de otros cuentos o historias, como "
                "elemento sorpresa o distorsionador."
            ),
            codigo="ECA.2.2.10.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Documentar con imágenes, dibujos, fotografías y/o videos el "
                "proceso de elaboración de comidas típicas de la zona, y "
                "crear recetarios ilustrados."
            ),
            codigo="ECA.2.2.11.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Explicar, tras la observación de videos breves, cómo "
                "algunos grupos musicales(como Seis On, Stomp, etc.) "
                "utilizan utensilios de cocina como instrumentos."
            ),
            codigo="ECA.2.2.12.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Crear e interpretar, en pequeños grupos, piezas rítmicas, "
                "usando utensilios de cocina como instrumentos musicales."
            ),
            codigo="ECA.2.2.13.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Explicar las similitudes y diferencias en los rasgos (el "
                "color de piel, el pelo, la fisonomía, el tono de voz, etc.) "
                "de los compañeros, la familia, los miembros de la comunidad "
                "y de otras culturas, a partir de la observación directa o a "
                "través de fotografías."
            ),
            codigo="ECA.2.3.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar en el entorno próximo para descubrir "
                "representaciones de personas en la artesanía, las "
                "esculturas y las imágenes que conforman la cultura visual y "
                "observar, describir y comparar los hallazgos."
            ),
            codigo="ECA.2.3.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Describir los elementos plásticos presentes en el entorno "
                "artificial (edificios, mobiliario urbano, obras expuestas "
                "en las calles o los museos, etc.) utilizando un vocabulario "
                "adecuado."
            ),
            codigo="ECA.2.3.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Comentar las impresiones que suscita la observación de "
                "producciones escénicas(música, danza, teatro, etc.) del "
                "entorno próximo, representadas en las calles, en la "
                "comunidad, en auditorios o en otros escenarios."
            ),
            codigo="ECA.2.3.4.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Seleccionar imágenes de algunos de los lugares más "
                "representativos del patrimonio cultural y natural del "
                "entorno próximo paracrear álbumes, carteles o murales."
            ),
            codigo="ECA.2.3.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Realizar grabaciones sonoras o audiovisuales de algunos de "
                "los lugares más representativos del patrimonio cultural y "
                "natural del entorno próximo."
            ),
            codigo="ECA.2.3.6.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Redactar textos breves que describan las características de "
                "algunos de los lugares más representativos del patrimonio "
                "cultural y natural del entorno próximo."
            ),
            codigo="ECA.2.3.7.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Diseñar y construir juguetes tradicionales o populares "
                "(pitos, casitas con sus muebles y vajilla, muñecos, carros, "
                "caleidoscopios, zancos, trompos, catapultas, perinolas, "
                "yoyos, etc.) utilizando materiales de desecho o de bajo "
                "costo (barro, arcilla, madera, hojalata, totora, lana, "
                "paja, tagua, telas, etc.)."
            ),
            codigo="ECA.2.3.8.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Observar, fotografiar y comparar construcciones y lugares "
                "representativos del patrimonio cultural y natural del "
                "entorno próximo (viviendas, monumentos y sitios "
                "arqueológicos, edificios históricos y modernos, bosques, "
                "etc.) durante la realización de paseos."
            ),
            codigo="ECA.2.3.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear carteles o catálogos sencillos, con fotografías de "
                "construcciones del entorno próximo, en los que se describan "
                "las principales características de cada una de ellas."
            ),
            codigo="ECA.2.3.10.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Recopilar información sobre algunas características "
                "relevantes de personajes de cuentos tradicionales, mitos y "
                "leyendas de las distintas nacionalidades del Ecuador."
            ),
            codigo="ECA.2.3.11.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Idear modificaciones posibles de personajes de cuentos "
                "tradicionales, mitos y leyendas de las distintas "
                "nacionalidades del Ecuador plasmarlas en dibujos o figuras "
                "y elaborar historias nuevas."
            ),
            codigo="ECA.2.3.12.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Realizar transformaciones sobre materiales de uso cotidiano "
                "o desechado (lápices, telas, botellas de plástico, latas, "
                "cartones, etc.), variando su utilidad para convertirlos en "
                "animales o muñecos; añadirles adornos, modificar su color y "
                "construir estructuras."
            ),
            codigo="ECA.2.3.13.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Responsabilizarse de la transformación progresiva de "
                "algunos espacios del centro educativo, incorporando las "
                "producciones que elaboren a lo largo del curso."
            ),
            codigo="ECA.2.3.14.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Registrar los procesos de transformación de algunos "
                "espacios del centro educativo con fotografías periódicas "
                "que muestren los cambios o modificaciones."
            ),
            codigo="ECA.2.3.15.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar sobre los alimentos que forman una dieta "
                "tradicional, su forma de elaboración en épocas pasadas y su "
                "permanencia en el presente."
            ),
            codigo="ECA.2.3.16.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear planos sencillos que incluyan los nombres, la "
                "ubicación y las especialidades de los establecimientos de "
                "comida de la zona (puestos en la calle, bares, cafeterías, "
                "restaurantes)."
            ),
            codigo="ECA.2.3.17.",
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Identificar los platos típicos del país y elaborar un "
                "calendario para preparar algunas recetas en las fechas de "
                "celebración."
            ),
            codigo="ECA.2.3.18.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Producir imágenes, dibujos o collages para crear cartas de "
                "restaurantes hipotéticos con menús en los que predomine un "
                "color."
            ),
            codigo="ECA.2.3.19.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=elemental,
            bloque=bloque3,
        ),

    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0035_auto_20180809_1536'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
