from django.db import migrations


def create_unidades(apps, schema_editor):
    Unidad = apps.get_model('planificaciones', 'Unidad')
    Curso = apps.get_model('planificaciones', 'Curso')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')

    # Cursos
    segundo_egb = Curso.objects.get(name="2° EGB")
    tercero_egb = Curso.objects.get(name="3° EGB")
    cuarto_egb = Curso.objects.get(name="4° EGB")
    quinto_egb = Curso.objects.get(name="5° EGB")
    sexto_egb = Curso.objects.get(name="6° EGB")
    septimo_egb = Curso.objects.get(name="7° EGB")
    octavo_egb = Curso.objects.get(name="8° EGB")
    noveno_egb = Curso.objects.get(name="9° EGB")
    decimo_egb = Curso.objects.get(name="10° EGB")
    primero_bgu = Curso.objects.get(name="1° BGU")
    segundo_bgu = Curso.objects.get(name="2° BGU")
    tercero_bgu = Curso.objects.get(name="3° BGU")

    # Asignaturas
    lengua_literatura = Asignatura.objects.get(
        name="Lengua y Literatura")
    matematica = Asignatura.objects.get(name="Matemática")
    ciencias_naturales = Asignatura.objects.get(
        name="Ciencias Naturales")
    biologia = Asignatura.objects.get(name="Biología")
    quimica = Asignatura.objects.get(name="Química")
    fisica = Asignatura.objects.get(name="Física")
    estudios_sociales = Asignatura.objects.get(
        name="Estudios Sociales")
    historia = Asignatura.objects.get(name="Historia")
    filosofia = Asignatura.objects.get(name="Filosofía")
    educacion_ciudadania = Asignatura.objects.get(
        name="Educación para la Ciudadanía")
    emprendimiento_gestion = Asignatura.objects.get(
        name="Emprendimiento y Gestión"
    )

    # Añade los cursos a las Asignaturas

    lengua_literatura.cursos.add(
        segundo_egb,
        tercero_egb,
        cuarto_egb,
        quinto_egb,
        sexto_egb,
        septimo_egb,
        octavo_egb,
        noveno_egb,
        decimo_egb,
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )
    matematica.cursos.add(
        segundo_egb,
        tercero_egb,
        cuarto_egb,
        quinto_egb,
        sexto_egb,
        septimo_egb,
        octavo_egb,
        noveno_egb,
        decimo_egb,
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )
    ciencias_naturales.cursos.add(
        segundo_egb,
        tercero_egb,
        cuarto_egb,
        quinto_egb,
        sexto_egb,
        septimo_egb,
        octavo_egb,
        noveno_egb,
        decimo_egb,
    )
    estudios_sociales.cursos.add(
        segundo_egb,
        tercero_egb,
        cuarto_egb,
        quinto_egb,
        sexto_egb,
        septimo_egb,
        octavo_egb,
        noveno_egb,
        decimo_egb,
    )
    biologia.cursos.add(
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )
    quimica.cursos.add(
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )
    fisica.cursos.add(
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )
    historia.cursos.add(
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )
    filosofia.cursos.add(
        primero_bgu,
        segundo_bgu,
    )
    educacion_ciudadania.cursos.add(
        primero_bgu,
        segundo_bgu,
    )
    emprendimiento_gestion.cursos.add(
        primero_bgu,
        segundo_bgu,
        tercero_bgu
    )

    # Añade las unidades

    Unidad.objects.bulk_create([
        # Lengua y literatura
        # 2do EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: Descubro la intención del texto\n",
                "Comunicación Oral: Sucedió en la ventana\n",
                "Escritura: Reconozco los fonemas\n",
                "Lectura: ¡Me gusta leer!\n",
                "Literatura: Leo y me divierto"
            ),
            curso=segundo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Descubro la intención del texto\n",
                "Comunicación Oral: Me presento\n",
                "Escritura: Reconozco las grafías\n",
                "Lectura: ¡Me gusta leer!\n",
                "Literatura: Leo y me divierto"
            ),
            curso=segundo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: ¡Hablamos muchas lenguas!\n",
                "Comunicación Oral: Comunico mis ideas\n",
                "Escritura: Reconozco los fonemas y sus grafías\n",
                "Lectura: Leo para conocer más\n",
                "Literatura: ¡Es la hora del evento!"
            ),
            curso=segundo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: El kichwa enriquece ",
                "la concepción del mundo\n",
                "Comunicación Oral: Desarrollo la conciencia lingüística\n",
                "Escritura: Reconozco los fonemas y sus grafías\n",
                "Lectura: Leo para aprender\n",
                "Literatura: ¡Es la hora del evento!"
            ),
            curso=segundo_egb,
            asignatura=lengua_literatura,
        ),
        # 3ro EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: ¿Por qué leo?\n",
                "Comunicación Oral: Narro mis experiencias\n",
                "Lectura: Leo para aprender\n",
                "Escritura: ¡Aprendo a describir!\n",
                "Literatura: Leo y disfruto"
            ),
            curso=tercero_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Muchas razones para leer y escribir\n",
                "Comunicación Oral: Escucho con atención\n",
                "Lectura: Leo para aprender\n",
                "Escritura: ¡Aprendo a describir!\n",
                "Literatura: Leo y disfruto"
            ),
            curso=tercero_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: Aprendo nuevos idiomas\n",
                "Comunicación Oral: Aprendo a pedir y dar información\n",
                "Lectura: Leo para informarme\n",
                "Escritura: Aprendo a escribir carteles\n",
                "Literatura: Leo y disfruto"
            ),
            curso=tercero_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: Las lenguas originarias ",
                "enriquecen mi mundo\n",
                "Comunicación Oral: Aprendo a dar información\n",
                "Lectura: Llegan las noticias\n",
                "Escritura: ¡A escribir carteles!\n",
                "Literatura: ¡Vivan los cuentos!"
            ),
            curso=tercero_egb,
            asignatura=lengua_literatura,
        ),
        # 4to EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: Para qué leemos\n",
                "Comunicación Oral: Aprendo a usar las palabras correctas\n",
                "Lectura: Leo para conocer más\n",
                "Escritura: Descripción de personas\n",
                "Literatura: ¡Es hora de leer y escribir cuentos!"
            ),
            curso=cuarto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Los textos y su intención comunicativa\n",
                "Comunicación Oral: Expongo oralmente\n",
                "Lectura: ¡Leemos para conocer más!\n",
                "Escritura: Escribimos autorretratos\n",
                "Literatura: ¡A leer más cuentos!"
            ),
            curso=cuarto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: Diferentes lenguas del Ecuador\n",
                "Comunicación Oral: Sigo instrucciones\n",
                "Lectura: Leo para aprender\n",
                "Escritura: La descripción\n",
                "Literatura: Disfruto de la poesía"
            ),
            curso=cuarto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: La tradición oral de ",
                "los pueblos originarios\n",
                "Comunicación Oral: Expreso mis sentimientos\n",
                "Lectura: Leo para hacer las cosas bien\n",
                "Escritura: Aprendo a narrar\n",
                "Literatura: ¡La literatura te da alas!"
            ),
            curso=cuarto_egb,
            asignatura=lengua_literatura,
        ),
        # 5to EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: Los textos tienen ",
                "una intención comunicativa\n",
                "Comunicación Oral: ¡A conversar!\n",
                "Lectura: Leo para informarme y aprender\n",
                "Escritura: ¡Es hora de escribir!\n",
                "Literatura: ¡Es la hora de los cuentos populares!"
            ),
            curso=quinto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Los textos conservan ",
                "y transmiten la cultura\n",
                "Comunicación Oral: ¡Soy un narrador!\n",
                "Lectura: Leo para conocer mejor mi país\n",
                "Escritura: Mejoro mi habilidad para escribir\n",
                "Literatura: Disfruto las leyendas de mi país"
            ),
            curso=quinto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: Indago la variedad ",
                "lingüística de mi país\n",
                "Comunicación Oral: El diálogo y sus formas\n",
                "Lectura: Aprendo más sobre la megadiversidad del Ecuador\n",
                "Escritura: Creo imágenes y fotografías con palabras\n",
                "Literatura: Amorfinos, coplas y otros tesoros, la poesía "
                "popular de mi país"
            ),
            curso=quinto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: La tradición oral de\n",
                "Comunicación Oral: Expreso mis sentimientos\n",
                "Lectura: Leo para hacer las cosas bien\n",
                "Escritura: Aprendo a narrar\n",
                "Literatura: ¡La literatura te da alas!"
            ),
            curso=quinto_egb,
            asignatura=lengua_literatura,
        ),
        # 6to EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: El mundo y sus diferentes lenguas\n",
                "Comunicación Oral: ¡A construir ideas, opiniones "
                "y puntos de vista!\n",
                "Lectura: ¡Leo para informarme y aprender!\n",
                "Escritura: ¡Es hora de escribir!\n",
                "Literatura: ¡El mundo de los cuentos!"
            ),
            curso=sexto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Las lenguas se escriben\n",
                "Comunicación Oral: Exposición oral\n",
                "Lectura: Leo para aprender del pasado\n",
                "Escritura: ¡A escribir relatos históricos!\n",
                "Literatura: Refranes y fábulas"
            ),
            curso=sexto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: Las funciones del lenguaje \n",
                "Comunicación Oral: Las cosas que hacemos con las palabras\n",
                "Lectura: Leo y desarrollo mi pensamiento crítico\n",
                "Escritura: Aprendo a resumir\n",
                "Literatura: Disfruto de la literatura ecuatoriana"
            ),
            curso=sexto_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: Los textos tienen "
                "una intención comunicativa\n",
                "Comunicación Oral: ¿Quiénes cambian la historia?\n"
                "Lectura: Leo y desarrollo mi pensamiento crítico\n",
                "Escritura: Campaña en contra de la violencia\n",
                "Literatura: La literatura pinta la realidad"
            ),
            curso=sexto_egb,
            asignatura=lengua_literatura,
        ),
        # 7mo EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: La lengua escrita\n"
                "Comunicación Oral: Hago una exposición\n"
                "Lectura: ¡Leo para informarme y aprender!\n",
                "Escritura: ¡Es hora de escribir!\n",
                "Literatura: ¡Conozco mi país mediante sus leyendas!"
            ),
            curso=septimo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: El castellano se enriquece con "
                "las lenguas originarias\n"
                "Comunicación Oral: Sugerir, persuadir, convencer\n"
                "Lectura: Leo y aprendo de la vida de "
                "personajes importantes\n",
                "Escritura: ¡Me toca a mí!\n",
                "Literatura: Narro con palabras e imágenes"
            ),
            curso=septimo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: La escritura en el tiempo\n"
                "Comunicación Oral: ¡Participo en un coloquio!\n"
                "Lectura: Dialogamos por escrito\n",
                "Escritura: ¡Escribo para convencer!\n",
                "Literatura: La poesía"
            ),
            curso=septimo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: La comunicación humana\n"
                "Comunicación Oral: Describo de manera oral\n"
                "Lectura: ¡Leo y sigo instrucciones!\n",
                "Escritura: Escribo instrucciones\n",
                "Literatura: ¡Vamos al teatro!"
            ),
            curso=septimo_egb,
            asignatura=lengua_literatura,
        ),
        # 8vo EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: Una imágen vale más que mil palabras\n"
                "Literatura: Relatos de viajes y aventuras\n"
                "Lectura: Preguntas para conocer más\n",
                "Escritura: Entrevistas\n",
                "Comunicación Oral: La discusión"
            ),
            curso=octavo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Diversas culturas, diversos escritores\n"
                "Literatura: Misterios y acertijos\n"
                "Lectura: ¿Como me entero de lo que sucede en el mundo?\n",
                "Escritura: Noticias\n",
                "Comunicación Oral: Noticias en la radio"
            ),
            curso=octavo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: Los primeros escritos de la humanidad\n"
                "Literatura: Entre fantasmas y aparecidos\n"
                "Lectura: Más que una noticia\n",
                "Escritura: Informar con profundidad\n",
                "Comunicación Oral: El panel: Analizar un tema "
                "desde diversas perspectivas"
            ),
            curso=octavo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: Diferentes, pero iguales "
                "(la igualdad es la diferencia)\n"
                "Literatura: Viajes a mundos desconocidos\n"
                "Lectura: Contar la realidad con recursos literarios\n",
                "Escritura: Relato hechos de la realidad\n",
                "Comunicación Oral: Pongo atención en lo que digo..."
            ),
            curso=octavo_egb,
            asignatura=lengua_literatura,
        ),
        # 9no EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: De la escritura cuneiforme "
                "al alfabeto latino\n"
                "Literatura: Relatos sobre dioses y héroes\n"
                "Lectura: Los lectores opinan\n",
                "Escritura: Escribo para opinar\n",
                "Comunicación Oral: Conversatorio"
            ),
            curso=noveno_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: Expansión del latín en Europa\n"
                "Literatura: La poesía: ritmo y sensibilidad\n"
                "Lectura: La ciencia al alcance de todos\n",
                "Escritura: Escribo sobre ciencia\n",
                "Comunicación Oral: Exponemos sobre temas científicos"
            ),
            curso=noveno_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: De la escritura normal a la mecánica\n"
                "Literatura: La poesía: ideas múltiples y riqueza expresiva\n"
                "Lectura: Comentarios sobre obras artísticas\n",
                "Escritura: Escribo comentarios sobre obras artísticas\n",
                "Comunicación Oral: Exponemos sobre temas científicos"
            ),
            curso=noveno_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: Un mismo idioma, "
                "distintas formas de hablar\n"
                "Literatura: Un mundo lleno de poesía\n"
                "Lectura: Opiniones sobre sucesos de interés público\n",
                "Escritura: Expreso mi opinión sobre temas de la realidad\n",
                "Comunicación Oral: Los programas de entretenimiento, "
                "¿solo entretienen?"
            ),
            curso=noveno_egb,
            asignatura=lengua_literatura,
        ),
        # 10mo EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Lengua y Cultura: De la oralidad a la escritura\n"
                "Literatura: El teatro y sus orígenes\n"
                "Lectura: ¡Nos informamos!\n",
                "Escritura: Escribo para informar\n",
                "Comunicación Oral: Leer para comunicar"
            ),
            curso=decimo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo=(
                "Lengua y Cultura: La presencia afroecuatoriana "
                "y su tradición oral\n"
                "Literatura: Genero dramático: La tragedia, "
                "la comedia y otros subgéneros\n"
                "Lectura: Publicidad y propaganda\n",
                "Escritura: Escribo para convencer\n",
                "Comunicación Oral: La conferencia"
            ),
            curso=decimo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "Lengua y Cultura: Orígenes, transformaciones y variantes "
                "de la lengua española\n"
                "Literatura: El cuento ecuatoriano contemporáneo\n"
                "Lectura: Leo para conocer y aprender\n",
                "Escritura: Escribo para exponer, explicar, informar,...\n",
                "Comunicación Oral: La defensa de un punto de vista"
            ),
            curso=decimo_egb,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo=(
                "Lengua y Cultura: Lenguas en contacto\n"
                "Literatura: El cuento latinoamericano contemporáneo\n"
                "Lectura: Leo para comprender\n",
                "Escritura: ¡A escribir monografías!\n",
                "Comunicación Oral: Juego de roles"
            ),
            curso=decimo_egb,
            asignatura=lengua_literatura,
        ),
        # 1 BGU
        Unidad(
            numero_unidad=1,
            titulo="La sociedad del futuro",
            curso=primero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Las crisis modernas",
            curso=primero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Una lengua dinámica",
            curso=primero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Nuevos recursos",
            curso=primero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Lengua e identidad",
            curso=primero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=6,
            titulo="La dialéctica de la lengua",
            curso=primero_bgu,
            asignatura=lengua_literatura,
        ),
        # 2 BGU
        Unidad(
            numero_unidad=1,
            titulo="Lectores cibernéticos",
            curso=segundo_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Raíces poéticas",
            curso=segundo_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Costumbres",
            curso=segundo_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Evasión",
            curso=segundo_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Estereotipos",
            curso=segundo_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Otros lenguajes",
            curso=segundo_bgu,
            asignatura=lengua_literatura,
        ),
        # 3 BGU
        Unidad(
            numero_unidad=1,
            titulo="Poesía del siglo XIX",
            curso=tercero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La narrativa ecuatoriana del siglo XIX",
            curso=tercero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Literatura ecuatoriana del siglo XIX y XX",
            curso=tercero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Poetas de la segunda mitad del siglo XX",
            curso=tercero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Narradores del siglo XX",
            curso=tercero_bgu,
            asignatura=lengua_literatura,
        ),
        Unidad(
            numero_unidad=6,
            titulo=(
                "Literatura de finales del siglo XX "
                "y principios del siglo XXI"
            ),
            curso=tercero_bgu,
            asignatura=lengua_literatura,
        ),
        # Ciencias naturales
        # 2do EGB
        Unidad(
            numero_unidad=1,
            titulo="Mi cuerpo",
            curso=segundo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="El mundo que me rodea",
            curso=segundo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Los ciclos naturales",
            curso=segundo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="La bóveda celeste",
            curso=segundo_egb,
            asignatura=ciencias_naturales,
        ),
        # 3ro EGB
        Unidad(
            numero_unidad=1,
            titulo="Nuestro planeta y sus vecinos",
            curso=tercero_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="El sol, fuente de vida",
            curso=tercero_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Fuerzas, materia y mezclas",
            curso=tercero_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Observación astronómica: La Luna",
            curso=tercero_egb,
            asignatura=ciencias_naturales,
        ),
        # 4to EGB
        Unidad(
            numero_unidad=1,
            titulo="Fuerzas físicas y materia",
            curso=cuarto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Recursos naturales",
            curso=cuarto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Recursos renovables y no renovables",
            curso=cuarto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Recursos estratégicos: suelo y agua",
            curso=cuarto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Ecuador biodiverso",
            curso=cuarto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Mi cuerpo: alimentación y cuidados",
            curso=cuarto_egb,
            asignatura=ciencias_naturales,
        ),
        # 5to EGB
        Unidad(
            numero_unidad=1,
            titulo="Seres bióticos y abióticos",
            curso=quinto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Cuerpo humano y salud",
            curso=quinto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Diversidad natural",
            curso=quinto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El universo y el planeta Tierra",
            curso=quinto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Entorno y relieve",
            curso=quinto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="La materia",
            curso=quinto_egb,
            asignatura=ciencias_naturales,
        ),
        # 6to EGB
        Unidad(
            numero_unidad=1,
            titulo="Vida natural",
            curso=sexto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Ser humano y salud",
            curso=sexto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Diversidad biológica",
            curso=sexto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Hidrósfera y biósfera",
            curso=sexto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Transformación de la materia y energía",
            curso=sexto_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Fuerza, electricidad y magnetismo",
            curso=sexto_egb,
            asignatura=ciencias_naturales,
        ),
        # 7mo EGB
        Unidad(
            numero_unidad=1,
            titulo="Los seres vivos",
            curso=septimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Fisiología humana",
            curso=septimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Ecosistemas",
            curso=septimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El planeta Tierra",
            curso=septimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Materia y energía",
            curso=septimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Fuerzas y máquinas",
            curso=septimo_egb,
            asignatura=ciencias_naturales,
        ),
        # 8vo EGB
        Unidad(
            numero_unidad=1,
            titulo="Los seres vivos",
            curso=octavo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La reproducción",
            curso=octavo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="La nutrición en los seres vivos",
            curso=octavo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El ambiente de los seres vivos",
            curso=octavo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Movimiento y fuerza",
            curso=octavo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="El orígen del universo y los ciclos geoquímicos",
            curso=octavo_egb,
            asignatura=ciencias_naturales,
        ),
        # 9no EGB
        Unidad(
            numero_unidad=1,
            titulo=(
                "Niveles de organización en los seres vivos y su "
                "interacción con el medioambiente"
            ),
            curso=noveno_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Cambios en los seres vivos",
            curso=noveno_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="La fuerza de la gravedad",
            curso=noveno_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Nuestro universo",
            curso=noveno_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Acción del ser humano sobre la naturaleza",
            curso=noveno_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Nuestro planeta",
            curso=noveno_egb,
            asignatura=ciencias_naturales,
        ),
        # 10mo EGB
        Unidad(
            numero_unidad=1,
            titulo="La clasificación de los seres vivos",
            curso=decimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La reproducción en los seres vivos",
            curso=decimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="El sistema inmunitario y los virus",
            curso=decimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El origen de la vida en la tierra y la evolución",
            curso=decimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="cambios en la Tierra",
            curso=decimo_egb,
            asignatura=ciencias_naturales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Los fluidos",
            curso=decimo_egb,
            asignatura=ciencias_naturales,
        ),
        # Estudios sociales
        # 2do EGB
        Unidad(
            numero_unidad=1,
            titulo="Soy parte de una familia que me ama y me protege",
            curso=segundo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La escuela y mis compañeros",
            curso=segundo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="¡Qué lindo es vivir en comunidad!",
            curso=segundo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Conozco mi comunidad",
            curso=segundo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="El trabajo es la comunidad",
            curso=segundo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Mi patria, el Ecuador",
            curso=segundo_egb,
            asignatura=estudios_sociales,
        ),
        # 3ro EGB
        Unidad(
            numero_unidad=1,
            titulo="Nos orientamos",
            curso=tercero_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Las irregularidades de la Tierra",
            curso=tercero_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Organización administrativa del Ecuador",
            curso=tercero_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Mi país diverso",
            curso=tercero_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Un viaje por el Ecuador",
            curso=tercero_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Conozcamos al Ecuador",
            curso=tercero_egb,
            asignatura=estudios_sociales,
        ),
        # 4to EGB
        Unidad(
            numero_unidad=1,
            titulo="Los mapas nos ayudan a ubicarnos en el espacio",
            curso=cuarto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Mi país Ecuador, es megadiverso",
            curso=cuarto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="¿Quiénes somos los ecuatorianos?",
            curso=cuarto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El Ecuador y sus provincias",
            curso=cuarto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="La provincia donde vivo",
            curso=cuarto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Todos tenemos los mismos derechos y obligaciones",
            curso=cuarto_egb,
            asignatura=estudios_sociales,
        ),
        # 5to EGB
        Unidad(
            numero_unidad=1,
            titulo="Época aborigen",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Época colonial A",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Época colonial B",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="La independencia",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Relieves del Ecuador",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Suelos, agua y climas",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=7,
            titulo="Convivir con la Tierra",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=8,
            titulo="Problemas ambientales del Ecuador",
            curso=quinto_egb,
            asignatura=estudios_sociales,
        ),
        # 6to EGB
        Unidad(
            numero_unidad=1,
            titulo="Ecuador: Primer período republicano A",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Ecuador: Primer período republicano B",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Ecuador: Segundo período republicano A",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Ecuador: Segundo período republicano B",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Orígen y diversidad de la población ecuatoriana",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Los pobladores del Ecuador",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=7,
            titulo="Sociedad organizada",
            curso=sexto_egb,
            asignatura=estudios_sociales,
        ),
        # 7mo EGB
        Unidad(
            numero_unidad=1,
            titulo="Ecuador: Tercer período republicano A",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Ecuador: Tercer período republicano B",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Ecuador a inicios del siglo XXI",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="La población del Ecuador en cifras",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="División territorial",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Provincias del Ecuador",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=7,
            titulo="Igualdad y diversidad",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=8,
            titulo="Confesiones religiosas y laicismo",
            curso=septimo_egb,
            asignatura=estudios_sociales,
        ),
        # 8vo EGB
        Unidad(
            numero_unidad=1,
            titulo="Los orígenes",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Grandes imperios antiguos",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="La edad media",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Época aborígen en América",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Nuestro planeta",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Los continentes",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=7,
            titulo="El continente americano",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=8,
            titulo="Cultura y diversidad",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=9,
            titulo="Comunicación",
            curso=octavo_egb,
            asignatura=estudios_sociales,
        ),
        # 9no EGB
        Unidad(
            numero_unidad=1,
            titulo="Conquista y colonización de América",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Cambios en el mundo",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="La independencia latinoamericana",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="América latina y el mundo en el siglo XIX",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Economía del Ecuador",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Desarrollo humano",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=7,
            titulo="Democracia y ciudadanía",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=8,
            titulo="Derechos y deberes",
            curso=noveno_egb,
            asignatura=estudios_sociales,
        ),
        # 10mo EGB
        Unidad(
            numero_unidad=1,
            titulo="América Latina y el sistema mundial",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La segunda mitad del siglo XX",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Dictaduras y democracia",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=4,
            titulo="La población del mundo",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Movilidad de la población mundial",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Ecuador y su relación con el mundo",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=7,
            titulo="Democracia y participación",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        Unidad(
            numero_unidad=8,
            titulo="Estructura del Estado",
            curso=decimo_egb,
            asignatura=estudios_sociales,
        ),
        # Matemáticas
        # 2do EGB
        Unidad(
            numero_unidad=1,
            titulo="Creciendo en familia",
            curso=segundo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Mi tierra de leyendas",
            curso=segundo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Mi escuela, mi segundo hogar",
            curso=segundo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Mi propia receta",
            curso=segundo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Mis amigos y mi entorno",
            curso=segundo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Mi vida diaria",
            curso=segundo_egb,
            asignatura=matematica,
        ),
        # 3ro EGB
        Unidad(
            numero_unidad=1,
            titulo="Cuido el medio ambiente",
            curso=tercero_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Me alimento nutritivamente",
            curso=tercero_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Soy un ser vivo",
            curso=tercero_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Mi comunidad",
            curso=tercero_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Mi Ecuador organizado",
            curso=tercero_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Conociendo más de mi país",
            curso=tercero_egb,
            asignatura=matematica,
        ),
        # 4to EGB
        Unidad(
            numero_unidad=1,
            titulo="Un universo de números",
            curso=cuarto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Ecuador nutritivo",
            curso=cuarto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="¡Cuidemos el agua!",
            curso=cuarto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="¡El clima se altera!",
            curso=cuarto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Ecuador en crecimiento",
            curso=cuarto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="La vida es un ciclo",
            curso=cuarto_egb,
            asignatura=matematica,
        ),
        # 5to EGB
        Unidad(
            numero_unidad=1,
            titulo="Ecuador recicla",
            curso=quinto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Un universo de números",
            curso=quinto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="El agua se comparte",
            curso=quinto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Tu problema es mi problema",
            curso=quinto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Mi entorno natural",
            curso=quinto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Latinoamérica soy yo",
            curso=quinto_egb,
            asignatura=matematica,
        ),
        # 6to EGB
        Unidad(
            numero_unidad=1,
            titulo="Organizados procedemos mejor",
            curso=sexto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Mi salud es importante",
            curso=sexto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Ciudadanía, democracia y participación social",
            curso=sexto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="La interculturalidad enriquece a nuestro país",
            curso=sexto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Mi Ecuador biodiverso",
            curso=sexto_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo=("Respeto la diversidad de identidades, ",
                    "necesidades y capacidades"),
            curso=sexto_egb,
            asignatura=matematica,
        ),
        # 7mo EGB
        Unidad(
            numero_unidad=1,
            titulo="Organizados es mejor",
            curso=septimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Juntos por una cultura de paz",
            curso=septimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="¡Que vivan los derechos humanos!",
            curso=septimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Iguales en las diferencias",
            curso=septimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Me alimento sanamente para cuidar mi salud",
            curso=septimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="¡Cuido mi cuerpo!",
            curso=septimo_egb,
            asignatura=matematica,
        ),
        # 8vo EGB
        Unidad(
            numero_unidad=1,
            titulo="Números enteros",
            curso=octavo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Números racionales",
            curso=octavo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Cuerpos geométricos y figuras planas",
            curso=octavo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Semejanza y medición",
            curso=octavo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Estadística y probabilidad",
            curso=octavo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Leyes de la lógica y funciones",
            curso=octavo_egb,
            asignatura=matematica,
        ),
        # 9no EGB
        Unidad(
            numero_unidad=1,
            titulo="Números reales",
            curso=noveno_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Polinomios",
            curso=noveno_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Factorización y ecuaciones",
            curso=noveno_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Conjuntos y funciones lineales",
            curso=noveno_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Geometría y medida",
            curso=noveno_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Estadística y probabilidad",
            curso=noveno_egb,
            asignatura=matematica,
        ),
        # 10mo EGB
        Unidad(
            numero_unidad=1,
            titulo="Números reales",
            curso=decimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Funciones lineales",
            curso=decimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Sistemas de ecuaciones lineales",
            curso=decimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Funciones y ecuaciones cuadráticas",
            curso=decimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Razones trigonométricas",
            curso=decimo_egb,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Estadística y probabilidad",
            curso=decimo_egb,
            asignatura=matematica,
        ),
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Los números reales",
            curso=primero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Funciones reales y racionales",
            curso=primero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Límite y derivadas de funciones",
            curso=primero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Vectores",
            curso=primero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Elementos del plano",
            curso=primero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="El proceso estadístico",
            curso=primero_bgu,
            asignatura=matematica,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="Funciones",
            curso=segundo_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Funciones Trigonométricas",
            curso=segundo_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Derivadas de funciones reales",
            curso=segundo_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Vectores en R2",
            curso=segundo_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Cónicas",
            curso=segundo_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Estadística y probabilidad",
            curso=segundo_bgu,
            asignatura=matematica,
        ),
        # 3ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Funciones y límites",
            curso=tercero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Derivadas e Integrales",
            curso=tercero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Álgebra Lineal",
            curso=tercero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Vectores en el espacio",
            curso=tercero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Geometría en el espacio",
            curso=tercero_bgu,
            asignatura=matematica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Probabilidad",
            curso=tercero_bgu,
            asignatura=matematica,
        ),
        # Física
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Movimiento",
            curso=primero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Fuerzas",
            curso=primero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Electricidad y magnetismo",
            curso=primero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Energía",
            curso=primero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Energía térmica",
            curso=primero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Ondas: el sonido y la luz",
            curso=primero_bgu,
            asignatura=fisica,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="El movimiento",
            curso=segundo_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Fuerzas en la naturaleza",
            curso=segundo_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Trabajo y energía",
            curso=segundo_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Termodinámica",
            curso=segundo_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Corriente eléctrica",
            curso=segundo_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Movimiento armónico simple",
            curso=segundo_bgu,
            asignatura=fisica,
        ),
        # 3ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Mecánica I",
            curso=tercero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Mecánica II",
            curso=tercero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Campos eléctricos y magnéticos",
            curso=tercero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Electromagnetismo",
            curso=tercero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Física moderna I",
            curso=tercero_bgu,
            asignatura=fisica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Física moderna II",
            curso=tercero_bgu,
            asignatura=fisica,
        ),
        # Química
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Modelo atómico",
            curso=primero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Los átomos y la tabla periódica",
            curso=primero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="El enlace químico",
            curso=primero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Formación de compuestos químicos",
            curso=primero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Las reacciones químicas y sus ecuaciones",
            curso=primero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Química de disoluciones y sistemas dispersos",
            curso=primero_bgu,
            asignatura=quimica,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="Reacciones químicas y sus ecuaciones",
            curso=segundo_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Soluciones acuosas y sus reacciones",
            curso=segundo_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Disoluciones",
            curso=segundo_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Gases",
            curso=segundo_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Cinética y equilibrio químico",
            curso=segundo_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Ácidos y bases",
            curso=segundo_bgu,
            asignatura=quimica,
        ),
        # 3ro BGU
        Unidad(
            numero_unidad=1,
            titulo="El carbono",
            curso=tercero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Hidrocarburos de cadena abierta",
            curso=tercero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Hidrocarburos de cadena cerrada",
            curso=tercero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Compuestos oxigenados",
            curso=tercero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Compuestos nitrogenados y de interés biológico",
            curso=tercero_bgu,
            asignatura=quimica,
        ),
        Unidad(
            numero_unidad=6,
            titulo="La química del petróleo y el impacto ambiental",
            curso=tercero_bgu,
            asignatura=quimica,
        ),
        # Biología
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Orígen de la vida",
            curso=primero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Biomoléculas orgánicas y metabolismo",
            curso=primero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Evolución de la vida",
            curso=primero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Clasificación de los seres vivos",
            curso=primero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Biología celular",
            curso=primero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Sistema digestivo y nutrición",
            curso=primero_bgu,
            asignatura=biologia,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="La base de la vida",
            curso=segundo_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="El ciclo celular",
            curso=segundo_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Genética",
            curso=segundo_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Histología y fisiología vegetal",
            curso=segundo_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Fisiología animal",
            curso=segundo_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Anatomía y fisiología humana",
            curso=segundo_bgu,
            asignatura=biologia,
        ),
        # 3ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Seres vivos y su ambiente",
            curso=tercero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Ecología y crecimiento poblacional de los seres humanos",
            curso=tercero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Anatomía y fisiología de los seres vivos",
            curso=tercero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Reproducción en seres vivos",
            curso=tercero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Relaciones humanas y salud sexual",
            curso=tercero_bgu,
            asignatura=biologia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Recursos naturales y educación ambiental",
            curso=tercero_bgu,
            asignatura=biologia,
        ),
        # Historia
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Cultura y trabajo en la historia",
            curso=primero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="El orígen de la humanidad",
            curso=primero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Civilizaciones fluviales de la Antigüedad",
            curso=primero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Grecia, la cuna de Occidente",
            curso=primero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="La civilización romana",
            curso=primero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="El judaísmo, su influencia en Occidente",
            curso=primero_bgu,
            asignatura=historia,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="Fin del Imperio: de Occidente a Oriente",
            curso=segundo_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="El cristianismo",
            curso=segundo_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="El islam",
            curso=segundo_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El surgimiento de la Modernidad",
            curso=segundo_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Teorías y sistemas económicos",
            curso=segundo_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Sociedad y poder en el siglo XX",
            curso=segundo_bgu,
            asignatura=historia,
        ),
        # 3ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Cultura y vida de los pueblos precolombinos",
            curso=tercero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="El choque cultural en la conquista de América",
            curso=tercero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="El sistema colonial en los siglos XVI y XVII",
            curso=tercero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="La cultura en la Colonia",
            curso=tercero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Búsqueda de la identidad latinoamericana",
            curso=tercero_bgu,
            asignatura=historia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="El neoliberalismo en América Latina",
            curso=tercero_bgu,
            asignatura=historia,
        ),
        # Educación para la ciudadanía
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Ciudadanía y derechos",
            curso=primero_bgu,
            asignatura=educacion_ciudadania,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La democracia moderna",
            curso=primero_bgu,
            asignatura=educacion_ciudadania,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "La democracia y la construcción de un Estado plurinacional"),
            curso=primero_bgu,
            asignatura=educacion_ciudadania,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El Estado y su organización",
            curso=primero_bgu,
            asignatura=educacion_ciudadania,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="Ciudadanía y derechos",
            curso=segundo_bgu,
            asignatura=educacion_ciudadania,
        ),
        Unidad(
            numero_unidad=2,
            titulo="La democracia moderna",
            curso=segundo_bgu,
            asignatura=educacion_ciudadania,
        ),
        Unidad(
            numero_unidad=3,
            titulo=(
                "La democracia y la construcción de un Estado plurinacional"),
            curso=segundo_bgu,
            asignatura=educacion_ciudadania,
        ),
        Unidad(
            numero_unidad=4,
            titulo="El Estado y su organización",
            curso=segundo_bgu,
            asignatura=educacion_ciudadania,
        ),
        # Filosofía
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Filosofía antigua y medieval",
            curso=primero_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Filosofía moderna",
            curso=primero_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Filosofía contemporanea",
            curso=primero_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Ética",
            curso=primero_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Filosofía y política",
            curso=primero_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="Filosofía y estética",
            curso=primero_bgu,
            asignatura=filosofia,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="Lógica aristotélica",
            curso=segundo_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Lógica moderna de clases",
            curso=segundo_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Teoría del conocimiento",
            curso=segundo_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Introducción a la filosofía latinoamericana",
            curso=segundo_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=5,
            titulo="Del yo al nosotros",
            curso=segundo_bgu,
            asignatura=filosofia,
        ),
        Unidad(
            numero_unidad=6,
            titulo="El tratado europeo y el ensayo latinoamericano",
            curso=segundo_bgu,
            asignatura=filosofia,
        ),
        # Emprendimiento
        # 1ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Conceptos financieros",
            curso=primero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Contabilidad básica",
            curso=primero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Requisitos legales para el emprendimiento",
            curso=primero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Obligaciones legales",
            curso=primero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        # 2do BGU
        Unidad(
            numero_unidad=1,
            titulo="Diseño e investigación de campo",
            curso=segundo_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Estadística aplicada al mercadeo y a las ventas",
            curso=segundo_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Diseño e investigación de campo",
            curso=segundo_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Economía aplicada al emprendimiento",
            curso=segundo_bgu,
            asignatura=emprendimiento_gestion,
        ),
        # 3ro BGU
        Unidad(
            numero_unidad=1,
            titulo="Diseño e investigación de campo",
            curso=tercero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=2,
            titulo="Estadística aplicada al mercadeo y a las ventas",
            curso=tercero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=3,
            titulo="Diseño e investigación de campo",
            curso=tercero_bgu,
            asignatura=emprendimiento_gestion,
        ),
        Unidad(
            numero_unidad=4,
            titulo="Economía aplicada al emprendimiento",
            curso=tercero_bgu,
            asignatura=emprendimiento_gestion,
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0012_auto_20180727_2105'),
    ]

    operations = [
        migrations.RunPython(create_unidades,
                             reverse_code=migrations.RunPython.noop)
    ]
