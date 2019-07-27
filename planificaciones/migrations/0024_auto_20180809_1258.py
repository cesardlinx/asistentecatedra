from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )

    # Asignaturas
    fisica = Asignatura.objects.get(name='Física')
    biologia = Asignatura.objects.get(name='Biología')
    quimica = Asignatura.objects.get(name='Química')

    # bachillerato
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    CriterioEvaluacion.objects.bulk_create([
        # Física
        CriterioEvaluacion(
            description=(
                "Obtener las magnitudes cinemáticas(posición, velocidad, "
                "velocidad media e instantánea, aceleración, aceleración "
                "media e instantánea y desplazamiento) de un objeto que se "
                "mueve a lo largo de una trayectoria rectilínea del "
                "Movimiento Rectilíneo Uniforme y Rectilíneo Uniformemente "
                "Variado, según corresponda, elaborando tablas y gráficas en "
                "un sistema de referencia establecido."
            ),
            codigo="CE.CN.F.5.1.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Determina mediante representaciones gráficas de un objeto, "
                "que se mueve en dos dimensiones: la posición, la "
                "trayectoria, el vector posición, el vector desplazamiento, "
                "la velocidad promedio, la aceleración promedio, y establece "
                "la relación entre magnitudes escalares y vectoriales."
            ),
            codigo="CE.CN.F.5.2.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Determina mediante representaciones gráficas de un punto "
                "situado en un objeto, que gira alrededor de un eje, las "
                "características y las relaciones entre las cuatro "
                "magnitudes de la cinemática del movimiento "
                "circular(posición angular, velocidad angular, aceleración "
                "angular y tiempo) con sus análogas en el MRU y el MCU."
            ),
            codigo="CE.CN.F.5.3.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Elabora diagramas de cuerpo libre y resuelve problemas para "
                "reconocer los sistemas inerciales y los no inerciales, la "
                "vinculación de la masa del objeto con su velocidad, el "
                "principio de conservación de la cantidad de movimiento "
                "lineal, aplicando las leyes de Newton(con sus limitaciones "
                "de aplicación) y determinando el centro de masa para un "
                "sistema simple de dos cuerpos."
            ),
            codigo="CE.CN.F.5.4.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Determina el peso y analiza el lanzamiento vertical y caída "
                "libre(considerando y sin considerar la resistencia del "
                "aire) de un objeto en función de la intensidad del campo "
                "gravitatorio."
            ),
            codigo="CE.CN.F.5.5.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analizar la velocidad, ángulo de lanzamiento, aceleración, "
                "alcance, altura máxima, tiempo de vuelo, aceleración normal "
                "y centrípeta en el movimiento de proyectiles, en función de "
                "la naturaleza vectorial de la segunda ley de Newton."
            ),
            codigo="CE.CN.F.5.6.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta desde la experimentación y la observación de "
                "fenómenos la ley de Hooke (fuerza que ejerce un resorte es "
                "proporcional a la deformación que experimenta), "
                "estableciendo su modelo matemático y su importancia para la "
                "vida cotidiana."
            ),
            codigo="CE.CN.F.5.7.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta, experimentalmente, las magnitudes que "
                "intervienen en el MAS cuando un resorte se comprime o "
                "estira (sin considerar las fuerzas de fricción), a partir "
                "de las fuerzas involucradas en MCU (la fuerza centrífuga es "
                "una fuerza ficticia) y la conservación de la energía "
                "mecánica cuando el resorte está en posición horizontal o "
                "suspendido verticalmente, mediante la identificación de las "
                "energías que intervienen en cada caso."
            ),
            codigo="CE.CN.F.5.8.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta, mediante la experimentación y análisis del "
                "modelo de gas de electrones, el origen atómico de la carga "
                "eléctrica, el tipo de materiales según su capacidad de "
                "conducción de carga, la relación de masa entre protón y "
                "electrón e identifica aparatos de uso cotidiano que separan "
                "cargas eléctricas."
            ),
            codigo="CE.CN.F.5.9.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Resuelve problemas de aplicación de la ley de Coulomb "
                "usando el principio de superposición, y argumenta los "
                "efectos de las líneas de campo alrededor de una carga "
                "puntual en demostraciones con material concreto, la "
                "diferencia de potencial eléctrico, la corriente eléctrica y "
                "estableciendo, además, las transformaciones de energía que "
                "pueden darse en un circuito alimentado por una batería "
                "eléctrica."
            ),
            codigo="CE.CN.F.5.10.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Demostrar mediante la experimentación el voltaje, la "
                "intensidad de corriente eléctrica, la resistencia "
                "(considerando su origen atómico-molecular) y la potencia "
                "(comprendiendo el calentamiento de Joule), en circuitos "
                "sencillos alimentados por baterías o fuentes de corriente "
                "continua (considerando su resistencia interna)."
            ),
            codigo="CE.CN.F.5.11.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Establece la relación existente entre magnetismo y "
                "electricidad, mediante la comprensión del funcionamiento de "
                "un motor eléctrico, el campo magnético próximo a un "
                "conductor rectilíneo largo y la ley de Ampère."
            ),
            codigo="CE.CN.F.5.12.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Determina mediante ejercicios de aplicación, el trabajo "
                "mecánico con fuerzas constantes, la energía mecánica, la "
                "conservación de energía, la potencia y el trabajo negativo "
                "producido por las fuerzas de fricción al mover un objeto, a "
                "lo largo de cualquier trayectoria cerrada."
            ),
            codigo="CE.CN.F.5.13.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza la temperatura como energía cinética promedio de "
                "sus partículas y experimenta la ley cero de la "
                "termodinámica(usando conceptos de calor especifico, cambio "
                "de estado, calor latente y temperatura de equilibrio), la "
                "transferencia de calor(por conducción, convección y "
                "radiación), el trabajo mecánico producido por la energía "
                "térmica de un sistema y las pérdidas de energía en forma de "
                "calor hacia el ambiente y disminución del orden, que tienen "
                "lugar durante los procesos de transformación de energía."
            ),
            codigo="CE.CN.F.5.14.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica los elementos de una onda, sus propiedades, tipos y "
                "fenómenos relacionados con la reflexión, refracción, la "
                "formación de imágenes en lentes y espejos, el efecto "
                "Doppler y la descomposición de la luz, reconociendo la "
                "dualidad onda partícula de la luz y sus aplicaciones en la "
                "trasmisión de energía e información en los equipos de uso "
                "diario."
            ),
            codigo="CE.CN.F.5.15.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica los campos eléctricos generados en las proximidades "
                "de flujos magnéticos variables, los campos magnéticos "
                "generados en las proximidades de flujos eléctricos "
                "variables, el mecanismo de la radiación electromagnética "
                "por medio de la observación de videos(mostrando el "
                "funcionamiento de aparatos de uso cotidiano) y "
                "ejemplificando los avances de la mecatrónica al servicio de "
                "la sociedad."
            ),
            codigo="CE.CN.F.5.16.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta las tres leyes de Kepler y la ley de gravitación "
                "universal de Newton (a partir de las observaciones de Tycho "
                "Brahe al planeta Marte y el concepto de campo "
                "gravitacional), y las semejanzas y diferencias entre el "
                "movimiento de la Luna y los satélites artificiales "
                "(mediante el uso de simuladores)."
            ),
            codigo="CE.CN.F.5.17.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica los límites del Sistema Solar(el cinturón de Kuiper "
                "y la nube de Oort) reconociendo que esta zona contiene "
                "asteroides, cometas y meteoritos y su ubicación dentro de "
                "la Vía Láctea."
            ),
            codigo="CE.CN.F.5.18.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica los fenómenos de radiación del cuerpo negro, efecto "
                "fotoeléctrico, la radiación electromagnética (considerando "
                "la luz como partículas), el principio de incertidumbre de "
                "Heisenberg, el comportamiento ondulatorio de las partículas "
                "y la dualidad onda partícula a escala atómica (mediante los "
                "experimentos de difracción de la luz y de la doble "
                "rendija), y cómo el electromagnetismo, la mecánica cuántica "
                "y la nanotecnología han incidido en la sociedad."
            ),
            codigo="CE.CN.F.5.19.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Fundamenta las cuatro fuerzas de la naturaleza: "
                "electromagnética (mantiene unidos electrones y núcleo "
                "atómico), nuclear fuerte (mantiene unidos en el núcleo a "
                "los protones y neutrones), nuclear débil (responsable de la "
                "desintegración radioactiva, estableciendo que hay tres "
                "formas comunes de desintegración radiactiva: alfa, beta y "
                "gamma), y, finalmente gravitacional, valorando los efectos "
                "que tiene la tecnología en la revolución industrial."
            ),
            codigo="CE.CN.F.5.20.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta mediante el modelo estándar, que los protones y "
                "neutrones no son partículas elementales, analizando las "
                "características (masa, carga, espín) de las partículas "
                "elementales del átomo, distinguiendo partículas reales: "
                "leptones (electrón, neutrino del electrón, muon, neutrino "
                "del muon, tau y neutrino del tau), quarks (up, down, charm, "
                "strange, bottom y top), hadrones (bariones formados por "
                "tres quarks, mesones formados por pares quark-antiquark) y "
                "el efecto de las cuatro fuerzas fundamentales "
                "(electromagnética, nuclear fuerte y débil), mediante "
                "partículas virtuales o “cuantos del campo de fuerza” "
                "(gravitones, fotones, gluones y bosones) distinguiendo en "
                "estos últimos al bosón de Higgs."
            ),
            codigo="CE.CN.F.5.21.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta el modelo estándar “Lambda-CDM” como una "
                "explicación a todo lo observado en el Universo, a excepción "
                "de la gravedad, la materia y energía oscura, las "
                "características y efectos de estas últimas (al tener un "
                "mayor porcentaje de presencia en el Universo)."
            ),
            codigo="CE.CN.F.5.22.",
            asignatura=fisica,
            subnivel=bachillerato
        ),
        # Biología
        CriterioEvaluacion(
            description=(
                "Argumenta el origen de la vida, desde el análisis de las "
                "teorías de la abiogénesis, la identificación de los "
                "elementos y compuestos de la Tierra primitiva y la "
                "importancia de las moléculas y macromoléculas que "
                "constituyen la materia viva."
            ),
            codigo="CE.CN.B.5.1.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Cuestiona con fundamentos científicos la evolución de las "
                "especies desde el análisis de las diferentes teorías "
                "(teorías de la endosimbiosis, selección natural y sintética "
                "de la evolución), el reconocimiento de los biomas del mundo "
                "como evidencia de procesos evolutivos y la necesidad de "
                "clasificar taxonómicamente a las especies."
            ),
            codigo="CE.CN.B.5.2.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta la importancia del ADN como portador de la "
                "información genética transmisor de la herencia, "
                "comprendiendo su estructura, función, proceso de "
                "transcripción y traducción del ARN, las causas y "
                "consecuencias de la alteración genética y cromosómica."
            ),
            codigo="CE.CN.B.5.3.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta la importancia de la transmisión de la "
                "información genética en función de la comprensión de su "
                "desarrollo histórico, el análisis de patrones de "
                "cruzamiento y los principios no mendelianos, la teoría "
                "cromosómica y las leyes de Mendel."
            ),
            codigo="CE.CN.B.5.4.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta con fundamento científico el valor de la "
                "biodiversidad a partir del análisis de los patrones de "
                "evolución de las especies, su importancia social, económica "
                "y ambiental, los efectos de las actividades humanas, el "
                "reconocimiento de los modelos de desarrollo económico, los "
                "avances tecnológicos, y las estrategias y políticas "
                "enfocadas al desarrollo sostenible."
            ),
            codigo="CE.CN.B.5.5.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta desde la sustentación científica los tipos de "
                "organización y función de las estructuras de las células "
                "eucariotas(animal y vegetal), los procesos de anabolismo y "
                "catabolismo desde el análisis de la fotosíntesis y "
                "respiración celular, los efectos que produce la "
                "proliferación celular alterada y la influencia de la "
                "ingeniería genética en la alimentación y salud de los seres "
                "humanos."
            ),
            codigo="CE.CN.B.5.6.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta con fundamentos que las especies animales y "
                "vegetales están constituidas por órganos, aparatos y "
                "sistemas que tienen estructuras y funciones diferentes, que "
                "se relacionan entre sí para una adecuada función del "
                "organismo, y que cada especie tiene un menor o mayor grado "
                "de complejidad según su evolución."
            ),
            codigo="CE.CN.B.5.7.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Promueve planes de salud integral e investigaciones de "
                "campo bajo la comprensión crítica y reflexiva de los "
                "efectos que producen las enfermedades y desórdenes que "
                "alteran los sistemas nervioso y endocrino, como producto de "
                "inadecuadas prácticas de vida, y reconoce la importancia de "
                "los programas de salud pública y el aporte de la "
                "Biotecnología al campo de la Medicina y la Agricultura."
            ),
            codigo="CE.CN.B.5.8.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta con fundamentos los procesos que se realizan en "
                "las plantas (transporte, provisión de nutrientes, excreción "
                "de desechos, mecanismos de regulación del crecimiento, "
                "desarrollo vegetal, reproducción) desde la identificación "
                "de sus estructuras, función y factores que determinan la "
                "actividad."
            ),
            codigo="CE.CN.B.5.9.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta los riesgos de una maternidad/paternidad "
                "prematura, según su proyecto de vida, partiendo del "
                "análisis crítico y reflexivo de la salud sexual y "
                "reproductiva (fecundación/concepción, desarrollo "
                "embrionario y fetal, parto, aborto, formas de promoción, "
                "prevención y protección) y sus implicaciones."
            ),
            codigo="CE.CN.B.5.10.",
            asignatura=biologia,
            subnivel=bachillerato
        ),
        # Quimica
        CriterioEvaluacion(
            description=(
                "Explica las propiedades y las leyes de los gases, reconoce "
                "los gases más cotidianos, identifica los procesos físicos y "
                "su incidencia en la salud y en el ambiente."
            ),
            codigo="CE.CN.Q.5.1.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza la estructura del átomo en función de la "
                "comparación de las teorías atómicas de Bohr (explica los "
                "espectros de los elementos químicos), Demócrito, Dalton, "
                "Thompson y Rutherford y realiza ejercicios de la "
                "configuración electrónica desde el modelo mecánico-cuántico "
                "de la materia."
            ),
            codigo="CE.CN.Q.5.2.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza la estructura electrónica de los átomos a partir de "
                "la posición en la tabla periódica, la variación periódica y "
                "sus propiedades físicas y químicas, por medio de "
                "experimentos sencillos."
            ),
            codigo="CE.CN.Q.5.3.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta con fundamento científico que los átomos se unen "
                "debido a diferentes tipos de enlaces y fuerzas "
                "intermoleculares y que tienen la capacidad de relacionarse "
                "de acuerdo a sus propiedades al ceder o ganar electrones."
            ),
            codigo="CE.CN.Q.5.4.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Plantea, mediante el trabajo cooperativo, la formación de "
                "posibles compuestos químicos binarios y ternarios (óxidos, "
                "hidróxidos, ácidos, sales e hidruros) de acuerdo a su "
                "afinidad, enlace químico, número de oxidación, composición, "
                "formulación y nomenclatura."
            ),
            codigo="CE.CN.Q.5.5.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Deduce la posibilidad de que se efectúen las reacciones "
                "químicas de acuerdo a la transferencia de energía y a la "
                "presencia de diferentes catalizadores clasifica los tipos "
                "de reacciones y reconoce los estados de oxidación de los "
                "elementos y compuestos, y la actividad de los metales y "
                "efectúa la igualación de reacciones químicas con distintos "
                "métodos, cumpliendo con la ley de la conservación de la "
                "masa y la energía para balancear las ecuaciones."
            ),
            codigo="CE.CN.Q.5.6.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta la estructura del átomo de carbono y demuestra "
                "que es un átomo excepcional, que tiene la capacidad de "
                "unirse consigo mismo con diferentes enlaces entre "
                "carbono-carbono, formando así moléculas orgánicas con "
                "propiedades físicas y químicas diversas, que se representan "
                "mediante fórmulas que indican los tipos de enlace que la "
                "conforman."
            ),
            codigo="CE.CN.Q.5.7.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Distingue los hidrocarburos según su composición, su "
                "estructura y el tipo de enlace que une a los átomos de "
                "carbono clasifica los hidrocarburos alifáticos, alcanos, "
                "alquenos y alquinos por su estructura molecular y sus "
                "propiedades físicas y químicas en algunos productos de uso "
                "cotidiano(gas doméstico, kerosene, velas, eteno, "
                "acetileno), así como también los compuestos aromáticos, "
                "particularmente del benceno, a partir del análisis de su "
                "estructura molecular, propiedades físicas y comportamiento "
                "químico."
            ),
            codigo="CE.CN.Q.5.8.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica las series homólogas a partir de la estructura de "
                "los compuestos orgánicos y del tipo de grupo funcional que "
                "poseen las propiedades físicas y químicas de los compuestos "
                "oxigenados(alcoholes, aldehídos, ácidos, cetonas y éteres), "
                "basándose en el comportamiento de los grupos funcionales "
                "que forman parte de la molécula y que determinan la "
                "reactividad y las propiedades químicas de los compuestos y "
                "los principios en los que se basa la nomenclatura de los "
                "compuestos orgánicos, fórmulas empíricas, moleculares, "
                "semidesarrolladas y desarrolladas, y las diferentes clases "
                "de isomería, resaltando sus principales características y "
                "explicando la actividad de los isómeros mediante la "
                "interpretación de imágenes, ejemplos típicos y lecturas "
                "científicas."
            ),
            codigo="CE.CN.Q.5.9.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta mediante la experimentación el cumplimiento de "
                "las leyes de transformación de la materia, realizando "
                "cálculos de masa molecular de compuestos simples a partir "
                "de la masa atómica y el número de Avogadro, para determinar "
                "la masa molar y la composición porcentual de los compuestos "
                "químicos."
            ),
            codigo="CE.CN.Q.5.10.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Analiza las características de los sistemas dispersos según "
                "su estado de agregación y compara las disoluciones de "
                "diferente concentración en las soluciones de uso cotidiano "
                "a través de la experimentación sencilla."
            ),
            codigo="CE.CN.Q.5.11.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Explica la importancia de las reacciones ácido-base en la "
                "vida cotidiana, repecto al significado de la acidez, la "
                "forma de su determinación y su importancia en diferentes "
                "ámbitos de la vida y la determinación del pH a través de la "
                "medición de este parámetro en varias soluciones de uso "
                "diario y experimenta el proceso de desalinización en su "
                "hogar o en su comunidad como estrategia de obtención de "
                "agua dulce."
            ),
            codigo="CE.CN.Q.5.12.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Valora el origen y la composición del petróleo y su "
                "importancia como fuente de energía y materia prima para la "
                "elaboración de una gran cantidad de productos comunica la "
                "importancia de los polímeros artificiales en sustitución de "
                "productos naturales en la industria y su aplicabilidad en "
                "la vida cotidiana explica los símbolos que indican la "
                "presencia de los compuestos aromáticos y aplica las medidas "
                "de seguridad recomendadas para su manejo y comprende la "
                "importancia para el ser humano de alcoholes, aldehídos, "
                "cetonas, éteres, ácidos carboxílicos grasos y ésteres, de "
                "amidas y aminas, de glúcidos, lípidos, proteínas y "
                "aminoácidos, en la vida diaria, en la industria, en la "
                "medicina, así como las alteraciones para la salud que "
                "pueden causar la deficiencia o el exceso de su consumo."
            ),
            codigo="CE.CN.Q.5.13.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Argumenta la importancia de los biomateriales en la vida "
                "cotidiana, identifica la toxicidad y permanencia de los "
                "contaminantes ambientales y los factores que inciden en la "
                "velocidad de la corrosión de los materiales y comunica "
                "métodos y prácticas de prevención para una mejor calidad de "
                "vida."
            ),
            codigo="CE.CN.Q.5.14.",
            asignatura=quimica,
            subnivel=bachillerato
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0023_auto_20180808_1947'),
    ]

    operations = [
        migrations.RunPython(
            create_criterios, reverse_code=migrations.RunPython.noop)
    ]
