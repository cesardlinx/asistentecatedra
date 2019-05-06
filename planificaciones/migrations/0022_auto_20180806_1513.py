from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    estudios_sociales = Asignatura.objects.get(name='Estudios Sociales')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')

    Objetivo.objects.bulk_create([
        # Preparatoria
        Objetivo(
            description=(
                "Desarrollar su autonomía mediante el reconocimiento de su "
                "identidad en el desempeño de las actividades cotidianas, "
                "individuales y colectivas, para fomentar la seguridad, la "
                "confianza en sí mismo, el respeto, la integración y "
                "sociabilización con sus compañeros."
            ),
            codigo='O.CS.1.1.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Relacionar la historia personal con la de sus compañeros "
                "comprender semejanzas y diferencias."
            ),
            codigo='O.CS.1.2.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Distinguir elementos de la realidad y la fantasía en "
                "relatos históricos que combinan hechos reales y fantásticos "
                "a la vez, para despertar el interés en ellos y en nuestras "
                "tradiciones."
            ),
            codigo='O.CS.1.3.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Ubicar elementos de su entorno inmediato por medio de la "
                "observación y de información dada oralmente, con el fin de "
                "comprender la realidad de su medio."
            ),
            codigo='O.CS.1.4.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Aplicar las funciones básicas de orientación temporal y "
                "espacial, para resolver problemas de la vida cotidiana."
            ),
            codigo='O.CS.1.5.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Respetar la diversidad de su entorno social y natural con "
                "el fin de aprender a convivir en armonía."
            ),
            codigo='O.CS.1.6.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Acceder a los medios de comunicación y las TIC valorando su "
                "utilidad, beneficios y riesgos."
            ),
            codigo='O.CS.1.7.',
            subnivel=preparatoria,
            asignatura=estudios_sociales
        ),
        # Elemental
        Objetivo(
            description=(
                "Descubrir y apreciar el entorno natural, cultural y social, "
                "local, provincial y nacional, identificando los símbolos "
                "asociados a la riqueza del patrimonio, como medio para "
                "construir el sentido de la identidad y unidad nacional."
            ),
            codigo='O.CS.2.1.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Distinguir en la vida cotidiana los cambios y "
                "transformaciones de procesos y acontecimientos próximos al "
                "entorno, relacionándolos con períodos cortos y largos, para "
                "ampliar la concepción del tiempo."
            ),
            codigo='O.CS.2.2.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Identificar, diferenciar y describir las características "
                "geográficas, políticas, administrativas, económicas y "
                "sociales de la provincia empleando herramientas "
                "cartográficas, para fortalecer su identidad local y "
                "desenvolverse en el entorno natural y social; considerando "
                "posibles riesgos naturales y medidas de seguridad, "
                "prevención y control."
            ),
            codigo='O.CS.2.3.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Reconocer al Ecuador como parte integrante de América y el "
                "mundo, a través del estudio de las características comunes "
                "que lo vinculan a la región y al planeta, en función de "
                "valorar sus aportes y potencialidades, mediante el uso de "
                "diversas fuentes."
            ),
            codigo='O.CS.2.4.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Analizar las características y el funcionamiento de las "
                "diferentes formas de organización social, especialmente de "
                "la unidad social, especialmente de la unidad social básica "
                "familiar en los escenarios locales más cercanos: el barrio, "
                "la escuela, la comunidad, el cantón y la provincia."
            ),
            codigo='O.CS.2.5.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Explicar las formas de convivencia dentro de la comunidad, "
                "con base en el cumplimiento de responsabilidades y el "
                "ejercicio de derechos, por medio de acuerdos y compromisos, "
                "con el fin de propender al cuidado de la naturaleza, el "
                "espacio público y la democracia, desde sus roles sociales "
                "respectivos."
            ),
            codigo='O.CS.2.6.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Reconocer la utilidad de los medios de comunicación y las "
                "TIC como fuentes de información para el análisis de "
                "problemáticas cotidianas."
            ),
            codigo='O.CS.2.7.',
            subnivel=elemental,
            asignatura=estudios_sociales
        ),
        # Media
        Objetivo(
            description=(
                "Comprender y valorar el proceso de Independencia y el "
                "legado originario que aportaron las sociedades aborígenes "
                "como fundamentos para la construcción de la identidad "
                "nacional."
            ),
            codigo='O.CS.3.1.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Interpretar en forma crítica el desarrollo histórico del "
                "Ecuador desde sus raíces aborígenes hasta el presente, "
                "subrayando los procesos económicos, políticos, sociales, "
                "étnicos y culturales, el papel de los actores colectivos, "
                "las regiones y la dimensión internacional, de modo que se "
                "pueda comprender y construir su identidad y la unidad en la "
                "diversidad."
            ),
            codigo='O.CS.3.2.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Ubicar al Ecuador en el espacio Andino y estudiar su "
                "relieve, clima y división territorial, con énfasis en las "
                "provincias, para construir una identidad nacional arraigada "
                "en los valores y necesidades de los territorios locales, "
                "especialmente las relacionadas con posibles riesgos "
                "naturales y medidas de seguridad, prevención y control."
            ),
            codigo='O.CS.3.3.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Analizar la estructura político administrativa del Ecuador "
                "en relación con la diversidad de la población, los procesos "
                "migratorios y la atención y acceso a los servicios "
                "públicos."
            ),
            codigo='O.CS.3.4.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Plantear las condiciones de convivencia y responsabilidad "
                "social entre personas iguales y diversas, con derechos y "
                "deberes, en el marco de una organización social justa y "
                "equitativa."
            ),
            codigo='O.CS.3.5.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Asumir una actitud comprometida con la conservación de la "
                "diversidad, el medioambiente y los espacios naturales "
                "protegidos frente a las amenazas del calentamiento global y "
                "el cambio climático."
            ),
            codigo='O.CS.3.6.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Investigar problemas cotidianos de índole social y "
                "económica como medio para desarrollar el pensamiento "
                "crítico, empleando fuentes fiables y datos estadísticos, "
                "ampliando la información con medios de comunicación y TIC."
            ),
            codigo='O.CS.3.7.',
            subnivel=media,
            asignatura=estudios_sociales
        ),
        # Superior
        Objetivo(
            description=(
                "Identificar y explicar las diferentes expresiones "
                "culturales a través de la observación e interpretación de "
                "sus diversas manifestaciones para valorar su sentido y "
                "aporte a la configuración de nuestra identidad."
            ),
            codigo='O.CS.4.1.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Desarrollar una visión general de varios procesos "
                "históricos de la humanidad, desde sus orígenes hasta el "
                "siglo XX, especialmente la evolución de los pueblos "
                "aborígenes de América, la conquista y colonización de "
                "América Latina, su independencia y vida republicana, en el "
                "contexto de los imperios coloniales y el imperialismo, para "
                "determinar su papel en el marco histórico mundial."
            ),
            codigo='O.CS.4.2.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Establecer las características del planeta Tierra, su "
                "formación, la ubicación de los continentes, océanos y "
                "mares, mediante el uso de herramientas cartográficas que "
                "permitan determinar su importancia en la gestión de "
                "recursos y la prevención de desastres naturales."
            ),
            codigo='O.CS.4.3.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Analizar la realidad nacional del Ecuador en sus diversas "
                "dimensiones, destacando sus recursos naturales y sectores "
                "económicos, agricultura y ganadería, industria, comercio y "
                "servicios, así como el papel del Estado en relación con la "
                "economía, la migración, y los conflictos por la "
                "distribución de la riqueza en América Latina y el mundo."
            ),
            codigo='O.CS.4.4.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Determinar los parámetros y las condiciones de desarrollo "
                "humano integral y calidad de vida en el mundo, a través del "
                "conocimiento de los principales indicadores demográficos y "
                "socioeconómicos, para estimular una conciencia solidaria y "
                "comprometida con nuestra realidad."
            ),
            codigo='O.CS.4.5.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Comprender la naturaleza de la democracia, la ciudadanía y "
                "los movimientos sociales, con sus inherentes derechos y "
                "deberes ciudadanos, los derechos humanos, el papel de la "
                "Constitución y la estructura básica del Estado ecuatoriano, "
                "para estimular una práctica ciudadana crítica y "
                "comprometida."
            ),
            codigo='O.CS.4.6.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Propiciar la construcción de un Ecuador justo e "
                "intercultural, con base en el respeto a las diversidades en "
                "un gran proyecto de unidad nacional, bajo la premisa de una "
                "seria crítica a toda forma de discriminación y exclusión "
                "social."
            ),
            codigo='O.CS.4.7.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
        Objetivo(
            description=(
                "Producir análisis críticos estructurados y fundamentados "
                "sobre problemáticas complejas de índole global, regional y "
                "nacional, empleando fuentes fiables, relacionando "
                "indicadores socioeconómicos y demográficos y contrastando "
                "información de los medios de comunicación y las TIC."
            ),
            codigo='O.CS.4.8.',
            subnivel=superior,
            asignatura=estudios_sociales
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0021_auto_20180806_1401'),
    ]

    operations = [
        migrations.RunPython(
            create_objetivos, reverse_code=migrations.RunPython.noop)
    ]
