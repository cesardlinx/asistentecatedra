from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    educacion_cultural = Asignatura.objects.get(
        name="Educación Cultural y Artística")

    # Subniveles
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    # Bloques
    bloque1 = BloqueCurricular.objects.get(name="El yo: la identidad")
    bloque2 = BloqueCurricular.objects.get(
        name="El encuentro con otros: la alteridad"
    )
    bloque3 = BloqueCurricular.objects.get(
        name="El entorno: espacio, tiempo y objetos"
    )

    Destreza.objects.bulk_create([
        # Media
        # Bloque 1
        Destreza(
            description=(
                "Representar momentos o situaciones que hayan sido "
                "relevantes en la historia personal de cada estudiante, a "
                "través de una palabra tratada de forma expresiva (escrita "
                "sobre papel, sobre arcilla a gran tamaño, en miniatura o en "
                "color, etc.), un dibujo o una fotografía."
            ),
            codigo="ECA.3.1.1.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar carteles o murales colectivos combinando palabras, "
                "fotografías o dibujos que representen momentos relevantes "
                "de la historia personal de cada estudiante."
            ),
            codigo="ECA.3.1.2.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Describir algunas características del propio rostro, como "
                "paso previo a la elaboración de un autorretrato, durante la "
                "observación del mismo frente a un espejo."
            ),
            codigo="ECA.3.1.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar autorretratos utilizando un espejo o una imagen "
                "fotográfica, y verbalizar las dificultades encontradas y la "
                "satisfacción con el resultado obtenido."
            ),
            codigo="ECA.3.1.4.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Crear galerías virtuales de autorretratos en los que se "
                "oculte una parte o la totalidad del rostro, y publicar las "
                "obras realizadas en tableros de Internet o una web o blog "
                "de aula."
            ),
            codigo="ECA.3.1.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Componer retratos sonoros combinando sonidos grabados y "
                "fragmentos de piezas musicales que cada estudiante escucha "
                "en su vida diaria."
            ),
            codigo="ECA.3.1.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Difundir los retratos sonoros grabados incorporándolos en "
                "sitios web que permitan la publicación de música, podcasts "
                "y fragmentos sonoros."
            ),
            codigo="ECA.3.1.7.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Describir la producción de artistas que transforman objetos "
                "artificiales o naturales en obras de arte (como Gilbert "
                "Legrand, Domenic Bahmann, Dan Cretu, Vanessa Zúñiga, etc.)."
            ),
            codigo="ECA.3.1.8.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Crear esculturas u obras plásticas transformando objetos "
                "naturales o artificiales en personajes u otros objetos."
            ),
            codigo="ECA.3.1.9.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Describir las creaciones de grupos musicales que utilizan "
                "instrumentos creados con materiales naturales y objetos de "
                "uso cotidiano o de desecho (por ejemplo, The Vegetable "
                "Orchestra; Les Luthiers; la Orquesta de Instrumentos "
                "Reciclados de Cateura, en Paraguay; Xavi Lozano; Junk Music "
                "Band; Percusionando, en Ecuador; Taller La Bola)."
            ),
            codigo="ECA.3.1.10.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Transformar materiales naturales y objetos de desecho en "
                "instrumentos musicales, a partir de un proceso de "
                "experimentación, diseño y planificación."
            ),
            codigo="ECA.3.1.11.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Crear documentos sencillos(informes, catálogos, etc.) con "
                "información sobre los textiles del país, como resultado de "
                "un proceso de búsqueda de información en libros e Internet."
            ),
            codigo="ECA.3.1.12.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Entrevistar a artesanos y artesanas, o familiares, que "
                "puedan aportar información sobre los textiles del país: "
                "fibras empleadas, tintes, dibujos, significación de los "
                "mismos, telares, utensilios, etc."
            ),
            codigo="ECA.3.1.13.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar un catálogo de figurines con vestimentas típicas y "
                "muestras aproximadas de tejidos, que podrán confeccionarse "
                "con telares sencillos."
            ),
            codigo="ECA.3.1.14.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Entrevistar a personas mayores(o a expertos) que puedan "
                "informar sobre juegos, hábitos y costumbres que hayan "
                "desaparecido o que apenas se practiquen en la actualidad."
            ),
            codigo="ECA.3.1.15.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar un glosario de términos relacionados con juegos, "
                "hábitos y costumbres que hayan desaparecido."
            ),
            codigo="ECA.3.1.16.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Dialogar sobre las emociones que pueden transmitirse por "
                "medio del gesto facial y corporal."
            ),
            codigo="ECA.3.2.1.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Explorar las posibilidades de expresión del gesto facial y "
                "corporal mediante juegos por parejas, en los que un "
                "compañero le pida a otro que exprese alegría, tristeza, "
                "soledad, miedo, sorpresa, etc."
            ),
            codigo="ECA.3.2.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar fotos de los rostros, entre compañeros, mostrando "
                "diversos gestos y rasgos."
            ),
            codigo="ECA.3.2.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Componer secuencias fotográficas combinando fotografías "
                "personales, de compañeros o recortadas de revistas y otros "
                "soportes gráficos."
            ),
            codigo="ECA.3.2.4.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Observar cómo se proyecta la sombra corporal a la luz del "
                "día y explorar sus posibilidades y los efectos que pueden "
                "lograrse utilizando un foco de luz."
            ),
            codigo="ECA.3.2.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Comentar las principales características del teatro de "
                "sombras a partir de la observación de representaciones "
                "grabadas en videos o la asistencia a espectáculos."
            ),
            codigo="ECA.3.2.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Buscar información sobre las técnicas y materiales "
                "necesarios para crear un teatro de sombras."
            ),
            codigo="ECA.3.2.7.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar creaciones colectivas (narraciones breves, danzas, "
                "etc.) usando las técnicas propias del teatro de sombras."
            ),
            codigo="ECA.3.2.8.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Musicalizar creaciones colectivas realizadas con las "
                "técnicas del teatro de sombras."
            ),
            codigo="ECA.3.2.9.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar representaciones teatrales con títeres elaborados "
                "a partir de siluetas o material de reciclaje, en las que "
                "haya un argumento, música y efectos sonoros y donde los "
                "estados de ánimo de los personajes se caractericen con la "
                "voz."
            ),
            codigo="ECA.3.2.10.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Inventar piezas musicales para instrumentos construidos con "
                "materiales naturales y objetos en procesos de creación e "
                "interpretación colectiva."
            ),
            codigo="ECA.3.2.11.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Improvisar escenas individuales o colectivas a partir de lo "
                "que sugiere un objeto real (por ejemplo, a partir de una "
                "escoba: el personaje se transforma en un barrendero, una "
                "bruja, etc.)."
            ),
            codigo="ECA.3.2.12.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Crear secuencias sonoras que describan relatos o historias "
                "breves cuyo contenido pueda advertirse en la audición."
            ),
            codigo="ECA.3.2.13.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Escuchar piezas de música descriptiva o programática "
                "valiéndose de imágenes o videos que ayuden a seguir el "
                "transcurso del relato."
            ),
            codigo="ECA.3.2.14.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Contar historias a través de gestos o movimientos "
                "inspirados en distintas formas de expresión: mimo, danza o "
                "dramatización."
            ),
            codigo="ECA.3.2.15.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Participar activamente en el montaje de alguna fiesta de "
                "especial relevancia para la comunidad, como el carnaval o "
                "las fiestas del Sol y la Luna."
            ),
            codigo="ECA.3.2.16.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Elaborar artesanías, máscaras, disfraces y vestimentas "
                "rituales relacionados con alguna fiesta de especial "
                "relevancia para la comunidad."
            ),
            codigo="ECA.3.2.17.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Interpretar bailes y canciones relacionados con alguna "
                "fiesta de especial relevancia para la comunidad."
            ),
            codigo="ECA.3.2.18.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Crear un álbum de clase con fotografías, dibujos, "
                "invitaciones, papel de regalo, cintas, así como textos "
                "breves, que muestren acontecimientos significativos de los "
                "estudiantes (cumpleaños, inicio y final de curso, "
                "conmemoraciones de la comunidad, celebraciones nacionales, "
                "etc.)."
            ),
            codigo="ECA.3.2.19.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Situar en un lugar y una época determinados a los "
                "personajes que aparecen en retratos de grupo, tanto en "
                "obras pictóricas como en esculturas, a partir de la "
                "observación de su vestimenta, los rasgos que definen su "
                "posición social o los objetos que les acompañan."
            ),
            codigo="ECA.3.3.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Componer murales fotográficos a partir de la recopilación, "
                "selección y clasificación de imágenes de grupos familiares "
                "reunidos en alguna ocasión especial (cumpleaños, bodas, "
                "primeras comuniones, bautizos, comidas de Navidad, "
                "vacaciones, etc.)."
            ),
            codigo="ECA.3.3.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Seleccionar fragmentos de música popular o académica que "
                "evoquen acontecimientos u ocasiones especiales cumpleaños, "
                "bodas, primeras comuniones, bautizos, comidas de Navidad, "
                "vacaciones, etc.), y usarlos como ambientación sonora para "
                "acompañar lo mostrado en un mural fotográfico."
            ),
            codigo="ECA.3.3.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Describir obras de artistas que utilizan objetos como "
                "elemento base de sus creaciones (por ejemplo, Chema Madoz, "
                "Chiharu Shiota, Martin Creed, Christo Vladimirov Javacheff, "
                "Hanoch Piven, Victor Nunes, Javier Pérez Estrella, Lygia "
                "Clark, Michelle Stitzlein)."
            ),
            codigo="ECA.3.3.4.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear obras (esculturas, fotografías, instalaciones, etc.) "
                "utilizando objetos iguales (como Angélica Dass o Christo "
                "Vladimirov Javacheff), diversos, o combinando objetos y "
                "dibujos."
            ),
            codigo="ECA.3.3.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear animaciones con técnicas sencillas, como stop motion, "
                "utilizando objetos que en la narrativa transforman sus "
                "funciones (por ejemplo, un tenedor que se convierte en "
                "escoba, una campana que se convierte en taza, una serpiente "
                "que se convierte en una cuerda, etc.)."
            ),
            codigo="ECA.3.3.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Recopilar imágenes de acontecimientos relevantes para la "
                "comunidad obtenidas personalmente por los estudiantes, "
                "proporcionadas por otros asistentes, o descargadas de "
                "Internet."
            ),
            codigo="ECA.3.3.7.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Crear colectivamente secuencias temporales (una línea de "
                "tiempo, libros con pie de foto, una aplicación con "
                "diapositivas, etc.) para mostrar imágenes de "
                "acontecimientos relevantes para la comunidad."
            ),
            codigo="ECA.3.3.8.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Geolocalizar en mapas virtuales datos e imágenes sobre "
                "celebraciones, fiestas y rituales específicos que se "
                "celebren en el país,recogidos en procesos de búsqueda de "
                "información para los que se utilicen distintas "
                "fuentes(libros, folletos, Internet, etc.)."
            ),
            codigo="ECA.3.3.9.",
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar sobre los rituales, celebraciones y fiestas más "
                "significativos que se dan a lo largo del año en Ecuador, y "
                "elaborar documentos en los que se deje constancia de su "
                "origen, de los ritos que se siguen, las vestimentas que se "
                "utilizan, las danzas que se bailan, los instrumentos que se "
                "tocan o los alimentos que se ingieren."
            ),
            codigo="ECA.3.3.10.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=media,
            bloque=bloque3,
        ),
        # Superior
        # Bloque 1
        Destreza(
            description=(
                "Analizar pinturas o esculturas en las que se represente a "
                "una o más personas, y definir la técnica utilizada, las "
                "características y el carácter del personaje, la función de "
                "la obra, etc."
            ),
            codigo="ECA.4.1.1.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Representarse a través de un dibujo, una pintura o una "
                "escultura, inspirándose en los modelos ofrecidos en obras "
                "de artistas locales e internacionales, del presente y del "
                "pasado."
            ),
            codigo="ECA.4.1.2.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Construir un diario personal con imágenes, objetos, "
                "recortes de prensa, fotografías, grabaciones sonoras, "
                "videos o textos significativos, en el que se deje "
                "constancia de los gustos e inquietudes y se refleje la "
                "individualidad."
            ),
            codigo="ECA.4.1.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Componer monólogos, con la intención de representarlos ante "
                "los demás, en los que los estudiantes relaten hechos, "
                "anécdotas o experiencias, y en los que haya la "
                "intencionalidad de expresar sentimientos y emociones."
            ),
            codigo="ECA.4.1.4.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar una línea de tiempo con las piezas musicales más "
                "significativas en cada una de las etapas vitales del "
                "individuo, y compararla con la de otros compañeros y "
                "compañeras, para encontrar similitudes y diferencias."
            ),
            codigo="ECA.4.1.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Seleccionar una actividad artesanal (tejido, cerámica, "
                "joyería, restauración de muebles, etc.) e informarse acerca "
                "de las técnicas, procesos y características del trabajo de "
                "los artesanos que la realizan."
            ),
            codigo="ECA.4.1.6.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Diseñar y desarrollar un proyecto artesanal (tejido, "
                "cerámica, joyería, etc.), demostrando el dominio de las "
                "técnicas necesarias para la elaboración de un producto."
            ),
            codigo="ECA.4.1.7.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Desarrollar un portafolio digital que contenga muestras de "
                "la producción artística propia y comentarios críticos sobre "
                "los productos incluidos."
            ),
            codigo="ECA.4.1.8.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Registrar fotográficamente el proceso de intervención de un "
                "espacio, propio o privado, en el que se realice una "
                "instalación personal visual y/o sonora."
            ),
            codigo="ECA.4.1.9.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Aportar argumentos personales al escribir la crítica de una "
                "instalación artística observada en vivo o a través de su "
                "registro en Internet u otras fuentes documentales."
            ),
            codigo="ECA.4.1.10.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Utilizar aplicaciones informáticas sencillas para la "
                "creación de diaporamas con secuencias de imágenes de la "
                "propia historia o relacionadas con un tema específico."
            ),
            codigo="ECA.4.1.11.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Seleccionar las piezas musicales más adecuadas para "
                "sonorizar un diaporama atendiendo al carácter y emociones "
                "que se quieran transmitir(diapora: varias diapositivas a la "
                "vez)."
            ),
            codigo="ECA.4.1.12.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Seleccionar materiales musicales, visuales o audiovisuales "
                "preexistentes y combinarlos con otros para crear un remix "
                "digital original."
            ),
            codigo="ECA.4.1.13.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Crear nuevas versiones de canciones o danzas tradicionales "
                "añadiendo elementos de los estilos contemporáneos (ritmos, "
                "instrumentos, cambios en las coreografías, etc.)."
            ),
            codigo="ECA.4.1.14.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar y exponer presentaciones relacionadas con obras, "
                "creadores y manifestaciones artísticas contemporáneas "
                "(pintura, música, arquitectura, escultura, ilustración, "
                "novela gráfica, fotografía, instalaciones, artesanías, "
                "tecnología), en las que se atienda a la coherencia y a la "
                "adecuada organización de la información."
            ),
            codigo="ECA.4.1.15.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Realizar, en plano y en volumen, representaciones de "
                "acciones y gestos, tanto del cuerpo como del rostro: "
                "figuras que caminan, personas que esperan, rostros que "
                "lloran, caras que ríen, etc."
            ),
            codigo="ECA.4.2.1.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Realizar representaciones teatrales inspiradas en poemas o "
                "cuentos previamente seleccionados por sus posibilidades "
                "dramáticas y por la intervención de varios personajes."
            ),
            codigo="ECA.4.2.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Participar en intercambios de opiniones e impresiones "
                "suscitadas por la observación de personajes que intervienen "
                "o están representados en obras artísticas."
            ),
            codigo="ECA.4.2.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Usar estrategias de autoaprendizaje para interpretar, "
                "individualmente o en grupo, algunas canciones y danzas "
                "representativas de la propia comunidad."
            ),
            codigo="ECA.4.2.4.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Participar activamente en la preparación y puesta en escena "
                "de una representación de danza, expresión corporal, teatro, "
                "música, títeres, etc. o en el rodaje de una pequeña "
                "producción audiovisual, responsabilizándose del rol elegido "
                "o asignado."
            ),
            codigo="ECA.4.2.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Compartir conocimientos, ideas y creaciones artísticas con "
                "estudiantes de otras culturas o países, a través de "
                "conexiones virtuales que favorezcan el entendimiento "
                "intercultural."
            ),
            codigo="ECA.4.2.6.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Diseñar y realizar una instalación colectiva partiendo de "
                "la reflexión crítica y creativa sobre el significado, usos, "
                "recuerdos o experiencias de un espacio de la escuela."
            ),
            codigo="ECA.4.2.7.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Intervenir algún espacio de la escuela o de la comunidad "
                "mediante la realización de una performance colectiva."
            ),
            codigo="ECA.4.2.8.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Asumir distintos roles en la realización de pequeñas "
                "producciones audiovisuales(documentales o de ficción): "
                "guionista, camarógrafo, director, actor, etc."
            ),
            codigo="ECA.4.2.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Conocer las fuentes que informan sobre el patrimonio "
                "histórico y la producción artística actual, y recopilar "
                "información previa a una visita cultural en grupo: normas "
                "que rigen en los espacios culturales, contenidos de los "
                "mismos, programaciones, itinerarios posibles, etc."
            ),
            codigo="ECA.4.2.10.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Reelaborar los datos e impresiones obtenidos en visitas "
                "culturales y dejar constancia en guías que servirán para "
                "animar a familias y compañeros a realizar dichas visitas, "
                "de forma autónoma o guiados por los propios estudiantes."
            ),
            codigo="ECA.4.2.11.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Indagar sobre lo que las diversas culturas y sociedades han "
                "considerado, a lo largo del tiempo, como ideal de la figura "
                "humana, y documentar los hallazgos en un texto escrito, con "
                "soporte de imágenes, o en un documento audiovisual."
            ),
            codigo="ECA.4.3.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Utilizar fuentes impresas y digitales para la búsqueda de "
                "información sobre mujeres artistas cuyas obras no han "
                "recibido la consideración que merecen (Artemisa "
                "Gentileschi, Camile Claudel, Luisa Roldán, Clara Schumann, "
                "Lili Boulanger, etc. y mujeres artistas contemporáneas)."
            ),
            codigo="ECA.4.3.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Analizar los condicionantes sociales e históricos que "
                "marcaron el trabajo de las mujeres artistas y exponer la "
                "información obtenida en distintos soportes(presentaciones, "
                "carteles, documentos escritos, blogs, etc.)."
            ),
            codigo="ECA.4.3.3.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Investigar, diseñar y crear una presentación multimedia o "
                "un producto audiovisual que muestre los itinerarios de "
                "estudio y las salidas profesionales de las distintas "
                "especialidades artísticas."
            ),
            codigo="ECA.4.3.4.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Entrevistar a artesanos y artistas locales, interesándose "
                "por su historia profesional y el trabajo que desarrollan, y "
                "eligiendo previamente el formato en el que se realizará y "
                "presentará la entrevista: audio, video, prensa escrita, "
                "etc."
            ),
            codigo="ECA.4.3.5.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Diseñar y elaborar una guía turística que incluya "
                "diferentes espacios dedicados al arte(museos, auditorios, "
                "teatros, salas de cine, etc.) del Ecuador."
            ),
            codigo="ECA.4.3.6.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Observar y analizar las obras de artistas contemporáneos "
                "que realizan instalaciones(como Martin Creed, Andy "
                "Goldsworthy, Micaela de Vivero, Pablo Gamboa, Juan "
                "Montelpare) explicando la idea que subyace en cada una de "
                "sus obras."
            ),
            codigo="ECA.4.3.7.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Explicar cómo se produce el movimiento en esculturas "
                "móviles y otros ejemplos de arte cinético, como resultado "
                "de un proceso de observación y reflexión."
            ),
            codigo="ECA.4.3.8.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar sobre la obra de creadores que realizan "
                "instalaciones artísticas valiéndose de recursos "
                "tecnológicos(por ejemplo, Paloma Muñoz, Zimoun, Berndnaut "
                "Smilde, Yannick Jacquet, Fred Penelle o Pamela Pazmiño)."
            ),
            codigo="ECA.4.3.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Fotografiar espacios, objetos y elementos naturales(hojas "
                "que se marchitan, frutas que se pudren, la sombra que "
                "proyecta un árbol, el movimiento de una nube) en diferentes "
                "momentos del día y crear presentaciones audiovisuales que "
                "muestren el transcurso del tiempo."
            ),
            codigo="ECA.4.3.10.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Mirar las primeras películas de la historia del cine e "
                "investigar en qué circunstancias técnicas y sociales se "
                "produjeron y qué impresión causaron en los espectadores, "
                "estableciendo comparaciones con el cine actual."
            ),
            codigo="ECA.4.3.11.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar sobre construcciones que pertenecen al patrimonio "
                "artístico y recrear dichos monumentos mediante "
                "representaciones en plano(croquis, planos, proyecciones) o "
                "en volumen(maquetas), imaginando cómo serían en su origen: "
                "completar partes que se han destruido, terminar lo que no "
                "se llegó a hacer, recuperar el color que se ha perdido, "
                "etc."
            ),
            codigo="ECA.4.3.12.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar sobre obras de la cultura ecuatoriana que "
                "representan señas de identidad(las cerámicas "
                "antropomórficas de la cultura Chorrera, Guangala, Tolita la "
                "metalurgia del oro, plata y cobre la escultura quiteña de "
                "la época colonial la tradición de los textiles los retratos "
                "de personalidades relevantes, etc) para elaborar pequeños "
                "dosieres con la información obtenida e ilustrarlos con "
                "imágenes."
            ),
            codigo="ECA.4.3.13.",
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Investigar sobre las manifestaciones musicales "
                "tradicionales del país(el pasillo, el sanjuanito, el "
                "albazo, el pasacalle), los instrumentos musicales que se "
                "emplean y los bailes que se ejecutan, con el objeto de "
                "recopilar la información obtenida en archivos sonoros y "
                "documentos gráficos."
            ),
            codigo="ECA.4.3.14.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Indagar sobre la visión del mundo en las culturas "
                "ancestrales, su incidencia en la vida cotidiana y su "
                "supervivencia en la actualidad, en ritos, celebraciones y "
                "ceremonias."
            ),
            codigo="ECA.4.3.15.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=superior,
            bloque=bloque3,
        ),
        # Bachillerato
        # Bloque 1
        Destreza(
            description=(
                "Realizar producciones artísticas (una canción, un dibujo, "
                "una escultura, un monólogo, una instalación, etc.) a partir "
                "de temas de interés personal o social, cuestionamientos, "
                "preocupaciones o ideas relevantes para la juventud."
            ),
            codigo="ECA.5.1.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Autoevaluarse durante los procesos de creación artística "
                "usando criterios técnicos, reconociendo las propias "
                "emociones y realizando los ajustes necesarios para lograr "
                "el producto deseado."
            ),
            codigo="ECA.5.1.2.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Expresar las opiniones y sentimientos que suscita la "
                "observación de obras artísticas de diferentes "
                "características, a través de la participación en diálogos o "
                "la elaboración de breves críticas escritas."
            ),
            codigo="ECA.5.1.3.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Investigar cómo diferentes artistas han representado o "
                "documentado, a través del dibujo o la fotografía, gestos y "
                "expresiones que nacen de las emociones personales en "
                "momentos específicos(maternidad, guerras, celebraciones, "
                "etc.) y elaborar una serie de dibujos o fotografías "
                "relacionados con un momento o tema concreto."
            ),
            codigo="ECA.5.1.4.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Reelaborar ideas y transformar producciones de otros "
                "creadores a través de procesos de renovación o remezcla, "
                "superando estereotipos y convencionalismos en las propias "
                "creaciones y mostrando actitudes de flexibilidad e interés "
                "por la experimentación."
            ),
            codigo="ECA.5.1.5.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Planificar de forma razonada los procesos propios de "
                "creación o interpretación artística, considerando las "
                "necesidades de expresión y comunicación, y elaborar un "
                "guion con los pasos a seguir y los recursos necesarios."
            ),
            codigo="ECA.5.1.6.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Identificar un ámbito o forma de expresión artística de "
                "interés (cerámica, joyería, mimo, percusión corporal, video "
                "arte, etc.), utilizar recursos para el "
                "autoaprendizaje(libros, videos, aprendizaje entre pares, "
                "consulta a especialistas) y aplicar los conocimientos y "
                "habilidades adquiridos en la creación de un pequeño "
                "proyecto o producto artístico."
            ),
            codigo="ECA.5.1.7.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Seleccionar un cómic o una novela gráfica, crear finales "
                "alternativos para la historia y elaborar una nueva versión "
                "con un programa informático de creación de cómics o de "
                "animación."
            ),
            codigo="ECA.5.1.8.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        Destreza(
            description=(
                "Elaborar un portafolio digital que reúna una muestra de las "
                "creaciones artísticas propias o en las que ha participado "
                "el estudiante, y añadir una breve explicación, valoración o "
                "comentario sobre cada una de las obras."
            ),
            codigo="ECA.5.1.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque1,
        ),
        # Bloque 2
        Destreza(
            description=(
                "Seleccionar, ensayar e interpretar obras musicales y "
                "escénicas (teatro, musicales, títeres, danza, ópera, etc.) "
                "asumiendo distintos roles(actor, director, escenógrafo, "
                "etc.) y contribuyendo a la consecución del resultado "
                "esperado."
            ),
            codigo="ECA.5.2.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Representar historias reales o inventadas a través de un "
                "guion gráfico, una secuencia sonora, una representación "
                "teatral, una creación corporal o un video."
            ),
            codigo="ECA.5.2.2.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Diseñar y desarrollar pequeños proyectos artísticos "
                "colectivos centrados en un tema de interés individual o "
                "social(discriminación, contaminación sonora, género, etc.) "
                "previendo todas las fases del proceso, desde su creación "
                "hasta su difusión y presentación."
            ),
            codigo="ECA.5.2.3.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Ensayar y grabar en video o audio distintas versiones de "
                "una improvisación o interpretación/representación "
                "artística(musical, dramática, corporal, etc.), revisar las "
                "diferentes versiones y reflexionar en grupo sobre los "
                "aspectos positivos y mejorables de cada una de ellas."
            ),
            codigo="ECA.5.2.4.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Documentar, con fotografías, dibujos, registros sonoros o "
                "audiovisuales, los procesos creativos y las exposiciones o "
                "representaciones colectivas realizadas, y crear catálogos, "
                "programas radiofónicos, cortos u otros productos que den "
                "cuenta de los mismos."
            ),
            codigo="ECA.5.2.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Participar en las distintas fases del proceso creativo "
                "(identificar un tema, investigar, explorar opciones, "
                "seleccionar y desarrollar ideas, recibir críticas, revisar "
                "y perfeccionar, interpretar o exponer), crear una obra "
                "original (de danza, música, escultura, pintura, cine, "
                "etc.), presentarla y debatir los resultados con la "
                "audiencia, con un artista invitado, un crítico u otro "
                "especialista."
            ),
            codigo="ECA.5.2.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Leer u observar distintas versiones de la representación de "
                "un mito, historias o leyendas populares, y crear, "
                "interpretar y grabar en video una versión propia, "
                "contextualizándola en un momento cultural e histórico "
                "contemporáneo revisar la adaptación, debatir acerca de las "
                "opciones creativas y comentar qué elementos de la historia "
                "permanecieron iguales y cuáles cambiaron."
            ),
            codigo="ECA.5.2.7.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Indagar sobre la música de compositores y compositoras del "
                "repertorio clásico o popular, y componer una pieza o "
                "canción con un estilo similar al de los compositores "
                "elegidos ensayarla, grabarla y publicarla en una web o un "
                "blog para que los oyentes puedan escucharla y comentarla."
            ),
            codigo="ECA.5.2.8.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Observar una selección de spots o clips de video "
                "(comerciales, políticos, etc.), considerar qué tipos de "
                "música se utilizan para despertar o manipular una respuesta "
                "emocional, y usar la información obtenida para seleccionar "
                "y reemplazar la banda sonora por otras que creen estados "
                "emocionales distintos."
            ),
            codigo="ECA.5.2.9.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        Destreza(
            description=(
                "Producir grafitis y otras obras de arte urbano utilizando "
                "las técnicas apropiadas y respetando las normativas para "
                "utilizar lugares públicos."
            ),
            codigo="ECA.5.2.10.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque2,
        ),
        # Bloque 3
        Destreza(
            description=(
                "Investigar, analizar y comparar los recursos usados por "
                "artistas compositores, coreógrafos, dramaturgos, etc. para "
                "comunicar determinadas ideas, temas o conceptos (la "
                "naturaleza, eventos históricos, problemáticas sociales, "
                "optimismo, pesimismo, etc.) y para despertar emociones o "
                "sentimientos (alegría, tristeza, tensión, ira, etc.) en los "
                "oyentes o espectadores, y crear presentaciones multimedia "
                "que ilustren cómo se consigue el efecto deseado en cada "
                "forma de expresión artística."
            ),
            codigo="ECA.5.3.1.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Utilizar fuentes escritas, conversaciones informales o "
                "entrevistas formales para investigar sobre mitos, historias "
                "y leyendas de la memoria cultural del entorno, y elaborar "
                "un documento textual, visual o audiovisual que recoja los "
                "hallazgos."
            ),
            codigo="ECA.5.3.2.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Identificar y describir los elementos fundamentales "
                "(imagen, tiempo, movimiento, sonido e iluminación) y las "
                "ideas principales, símbolos, personajes y mensajes de obras "
                "teatrales y producciones cinematográficas."
            ),
            codigo="ECA.5.3.3.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer a artistas y agentes culturales (individuales; "
                "femeninos y masculinos; colectivos; institucionales; etc.), "
                "obras y manifestaciones culturales del Ecuador, y "
                "relacionarlos con sus contextos históricos y sociales."
            ),
            codigo="ECA.5.3.4.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Identificar y describir distintos tipos de manifestaciones "
                "y productos culturales y artísticos utilizando un lenguaje "
                "técnico, expresando puntos de vista personales, y mostrando "
                "una actitud de escucha y receptividad hacia las opiniones "
                "de otras personas."
            ),
            codigo="ECA.5.3.5.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer y explicar diferentes maneras de entender y "
                "representar una idea, un sentimiento o una emoción en obras "
                "y manifestaciones artísticas y culturales de distintos "
                "momentos históricosy de diversas culturas."
            ),
            codigo="ECA.5.3.6.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Analizar y valorar producciones artísticas y eventos "
                "culturales usando criterios técnicos y reconociendo las "
                "emociones que estos suscitan, y escribir críticas o "
                "comentarios para un periódico escolar, un blog personal o "
                "colectivo, una red social, etc., adecuando el lenguaje al "
                "medio utilizado."
            ),
            codigo="ECA.5.3.7.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Asociar determinadas manifestaciones culturales y "
                "artísticas con formas de pensar, modas o movimientos "
                "estéticos del presente y del pasado, y elaborar carteles "
                "impresos o digitales que muestren la relación entre los "
                "distintos elementos."
            ),
            codigo="ECA.5.3.8.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Buscar información sobre distintas formas de expresión en "
                "el arte contemporáneo (arte de acción, body art, "
                "instalaciones, happening, video arte, acción poética, "
                "performance, etc.) y elaborar una presentación o cartel "
                "(impreso o digital) que reúna los datos más importantes y "
                "algunas imágenes o videos ilustrativos."
            ),
            codigo="ECA.5.3.9.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Programar y realizar un evento cultural (exposición, "
                "representación artística, fiesta, concurso gastronómico, "
                "festival de cortos, etc.) en la escuela o en su entorno, "
                "considerando los valores de su comunidad."
            ),
            codigo="ECA.5.3.10.",
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Investigar sobre los procesos formativos para dedicarse "
                "profesionalmente a distintos ámbitos del arte o la cultura "
                "y sobre la vida y el trabajo de algunos profesionales y "
                "elaborar videos con entrevistas breves o documentales que "
                "ilustren distintas opciones."
            ),
            codigo="ECA.5.3.11.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
        Destreza(
            description=(
                "Reconocer los materiales, las herramientas y las técnicas "
                "del grafiti y otras formas de arte urbano mediante la "
                "observación del entorno cotidiano o fotografías de estas "
                "representaciones en las ciudades, y crear una exposición "
                "virtual de imágenes relacionadas con el tema."
            ),
            codigo="ECA.5.3.12.",
            imprescindible=True,
            asignatura=educacion_cultural,
            subnivel=bachillerato,
            bloque=bloque3,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0036_auto_20180809_1601'),
    ]

    operations = [
        migrations.RunPython(create_destrezas)
    ]
