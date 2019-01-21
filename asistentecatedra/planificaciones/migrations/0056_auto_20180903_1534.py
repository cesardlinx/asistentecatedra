from django.db import migrations


def create_indicadores(apps, schema_editor):
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion'
    )
    Indicador = apps.get_model('planificaciones', 'Indicador')

    # Criterios de evaluación
    criterio_historia_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.1.")
    criterio_historia_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.2.")
    criterio_historia_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.3.")
    criterio_historia_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.4.")
    criterio_historia_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.5.")
    criterio_historia_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.6.")
    criterio_historia_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.7.")
    criterio_historia_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.8.")
    criterio_historia_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.9.")
    criterio_historia_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.10.")
    criterio_historia_5_11 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.11.")
    criterio_historia_5_12 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.12.")
    criterio_historia_5_13 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.13.")
    criterio_historia_5_14 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.14.")
    criterio_historia_5_15 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.15.")
    criterio_historia_5_16 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.16.")
    criterio_historia_5_17 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.17.")
    criterio_historia_5_18 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.18.")
    criterio_historia_5_19 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.19.")
    criterio_historia_5_20 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.20.")
    criterio_historia_5_21 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.H.5.21.")
    criterio_ciudadania_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.1.")
    criterio_ciudadania_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.2.")
    criterio_ciudadania_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.3.")
    criterio_ciudadania_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.4.")
    criterio_ciudadania_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.5.")
    criterio_ciudadania_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.6.")
    criterio_ciudadania_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.7.")
    criterio_ciudadania_5_8 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.8.")
    criterio_ciudadania_5_9 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.9.")
    criterio_ciudadania_5_10 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.EC.5.10.")
    criterio_filosofia_5_1 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.1.")
    criterio_filosofia_5_2 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.2.")
    criterio_filosofia_5_3 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.3.")
    criterio_filosofia_5_4 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.4.")
    criterio_filosofia_5_5 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.5.")
    criterio_filosofia_5_6 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.6.")
    criterio_filosofia_5_7 = CriterioEvaluacion.objects.get(
        codigo="CE.CS.F.5.7.")

    Indicador.objects.bulk_create([
        # Historia
        Indicador(
            description=(
                "Contrasta los conceptos de historia e historiografía, "
                "mediante el uso técnico y ético de diversas fuentes, "
                "relativizando los diversos enfoques, con el fin de "
                "diferenciar la realidad de la construcción intelectual. "
                "(J.2., J.3., I.2.)"
            ),
            codigo="I.CS.H.5.1.1.",
            criterio_evaluacion=criterio_historia_5_1
        ),
        Indicador(
            description=(
                "Examina el término “cultura” como producción material y "
                "simbólica, empleando y relativizando fuentes y enfoques. "
                "(J.3., I.2.)"
            ),
            codigo="I.CS.H.5.1.2.",
            criterio_evaluacion=criterio_historia_5_1
        ),
        Indicador(
            description=(
                "Explica la importancia y función del trabajo colectivo y "
                "solidario, y la elaboración de herramientas como condición "
                "en la transformación biológica y social del ser humano y "
                "posterior revolución neolítica. (I.2.)"
            ),
            codigo="I.CS.H.5.2.1.",
            criterio_evaluacion=criterio_historia_5_2
        ),
        Indicador(
            description=(
                "Compara las características esenciales del Paleolítico "
                "(modo de producción, relaciones sociales, materias primas y "
                "herramientas y la producción de arte rupestre) con la "
                "revolución neolítica. (I.2.)"
            ),
            codigo="I.CS.H.5.2.2.",
            criterio_evaluacion=criterio_historia_5_2
        ),
        Indicador(
            description=(
                "Explica el impacto de la revolución neolítica en la "
                "transformación de la sociedad humana, destacando la "
                "domesticación de plantas y animales en la producción de "
                "excedentes, la división y especialización del trabajo. "
                "(J.4., I.2.)"
            ),
            codigo="I.CS.H.5.2.3.",
            criterio_evaluacion=criterio_historia_5_2
        ),
        Indicador(
            description=(
                "Explica las circunstancias que marcaron la transición de la "
                "comunidad primitiva a la sociedad dividida en clases y la "
                "existencia de castas, evaluando el papel de la educación y "
                "la división de trabajo en ella. (J.1., J.3.)"
            ),
            codigo="I.CS.H.5.3.1.",
            criterio_evaluacion=criterio_historia_5_3
        ),
        Indicador(
            description=(
                "Analiza las causas y circunstancias que originaron la "
                "crisis de la comunidad matriarcal, la propiedad privada "
                "sobre los medios de producción y la transformación de la "
                "concepción del ser humano como cosa o mercancía. (J.1., "
                "J.3.)"
            ),
            codigo="I.CS.H.5.3.2.",
            criterio_evaluacion=criterio_historia_5_3
        ),
        Indicador(
            description=(
                "Analiza el rol y la influencia de la mujer en los "
                "diferentes tiempos y espacios, destacando su papel en la "
                "sociedad primitiva, sociedad del Medio Oriente, Roma y "
                "Grecia antigua y la Colonia, y su protagonismo en Atenas y "
                "Esparta. (J.4., I.2.)"
            ),
            codigo="I.CS.H.5.4.1.",
            criterio_evaluacion=criterio_historia_5_4
        ),
        Indicador(
            description=(
                "Examina la diversidad de pensamiento en la concepción y "
                "protagonismo de la mujer, destacando el pensamiento "
                "judeocristiano, la cacería de “brujas”, y el rol de la "
                "mujer en la sociedad islámica, valorando el protagonismo "
                "sociopolítico de Dolores Cacuango, Tránsito Amaguaña y "
                "Rigoberta Menchú en los procesos de liberación de Ecuador y "
                "América Latina. (J.4., I.2.)"
            ),
            codigo="I.CS.H.5.4.2.",
            criterio_evaluacion=criterio_historia_5_4
        ),
        Indicador(
            description=(
                "Describe los aportes tecnológicos, económicos y científicos "
                "de las culturas de Mesopotamia, Egipto, China y la India y "
                "su impacto en el mundo contemporáneo.(J.1., J.4., I.1.)"
            ),
            codigo="I.CS.H.5.5.1.",
            criterio_evaluacion=criterio_historia_5_5
        ),
        Indicador(
            description=(
                "Distingue el alcance e influencia de la civilización griega "
                "en los imperios romano y bizantino, en la Europa del "
                "Renacimiento y en la cultura occidental; así como las "
                "limitaciones de la democracia y la ciudadanía y su relación "
                "con los postulados básicos del derecho romano y derecho "
                "anglosajón. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.6.1.",
            criterio_evaluacion=criterio_historia_5_6
        ),
        Indicador(
            description=(
                "Analiza los problemas de la expansión imperial romana, las "
                "causas de su decadencia y caída, sus diferencias en cuanto "
                "al arte y la cultura entre el Imperio romano de Occidente y "
                "de Oriente, reconociendo las contribuciones del derecho "
                "romano al sistema jurídico. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.6.2.",
            criterio_evaluacion=criterio_historia_5_6
        ),
        Indicador(
            description=(
                "Analiza las características principales del monoteísmo y la "
                "concepción lineal del tiempo; y el derecho romano y su "
                "relación con el sistema jurídico ecuatoriano. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.6.3.",
            criterio_evaluacion=criterio_historia_5_6
        ),
        Indicador(
            description=(
                "Describe los procesos de expansión y cambios que trajeron "
                "consigo el islamismo y el cristianismo, y las motivaciones "
                "económicas de las cruzadas en la Edad Media.(I.2.)"
            ),
            codigo="I.CS.H.5.7.1.",
            criterio_evaluacion=criterio_historia_5_7
        ),
        Indicador(
            description=(
                "Analiza la influencia del Imperio bizantino en la cultura, "
                "la religión y la legislación, y los principales aportes "
                "culturales del medioevo. (J.2., I.2.)"
            ),
            codigo="I.CS.H.5.7.2.",
            criterio_evaluacion=criterio_historia_5_7
        ),
        Indicador(
            description=(
                "Examina el papel de la Iglesia en la formación de las "
                "universidades y la difusión de la cultura y el arte "
                "(romántico y gótico) en el contexto del Imperio carolingio, "
                "destacando los aportes artísticos y culturales del medioevo "
                "(arquitectura, pintura y escultura). (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.7.3.",
            criterio_evaluacion=criterio_historia_5_7
        ),
        Indicador(
            description=(
                "Discute el concepto de “yihad” en la cultura islámica, en "
                "función de comprender los antecedentes históricos del "
                "conflicto judío-palestino. (I.2.)"
            ),
            codigo="I.CS.H.5.8.1.",
            criterio_evaluacion=criterio_historia_5_8
        ),
        Indicador(
            description=(
                "Analiza el origen, la expansión y los principios "
                "fundamentales del Islam y su relación en el conflicto entre "
                "judíos y palestinos. (I.2.)"
            ),
            codigo="I.CS.H.5.8.2.",
            criterio_evaluacion=criterio_historia_5_8
        ),
        Indicador(
            description=(
                "Discute los principios comunes que comparten el islamismo, "
                "el cristianismo y el judaísmo, su relación con los posibles "
                "antecedentes históricos del conflicto entre judíos y "
                "palestinos y reconoce la influencia de la civilización "
                "árabe en el arte y la cultura. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.8.3.",
            criterio_evaluacion=criterio_historia_5_8
        ),
        Indicador(
            description=(
                "Analiza las condiciones de surgimiento del Renacimiento y "
                "su contribución al desarrollo del pensamiento humanista y "
                "científico del mundo, destacando la relación entre "
                "humanismo renacentista y el pensamiento ilustrado. (J.1., "
                "J.3.)"
            ),
            codigo="I.CS.H.5.9.1.",
            criterio_evaluacion=criterio_historia_5_9
        ),
        Indicador(
            description=(
                "Examina los principales representantes y postulados de la "
                "Ilustración y su relación con el humanismo renacentista. "
                "(I.2.)"
            ),
            codigo="I.CS.H.5.9.2.",
            criterio_evaluacion=criterio_historia_5_9
        ),
        Indicador(
            description=(
                "Explica las motivaciones y conflictos entre la Reforma "
                "Protestante y la Contrarreforma católica y su impacto en el "
                "pensamiento renacentista y en la Ilustración. (I.2.)"
            ),
            codigo="I.CS.H.5.9.3.",
            criterio_evaluacion=criterio_historia_5_9
        ),
        Indicador(
            description=(
                "Analiza las causas y consecuencias de la Revolución "
                "francesa considerando el proyecto napoleónico y su "
                "vinculación con el humanismo renacentista y la Ilustración. "
                "(I.2.)"
            ),
            codigo="I.CS.H.5.9.4.",
            criterio_evaluacion=criterio_historia_5_9
        ),
        Indicador(
            description=(
                "Examina el contexto de origen de los movimientos obreros, "
                "feministas, indígenas, ecologistas y ecofeministas a partir "
                "del estudio de sus reivindicaciones y propuestas frente al "
                "modelo capitalista de producción. (J.1., I.2.,S.1.)"
            ),
            codigo="I.CS.H.5.10.1.",
            criterio_evaluacion=criterio_historia_5_10
        ),
        Indicador(
            description=(
                "Examina el papel que cumplen los movimientos artísticos, "
                "las diversas expresiones de arte, los medios de "
                "comunicación impresos y audiovisuales en las relaciones de "
                "poder y conflictos sociales. (J.1., J.3., I.2.)"
            ),
            codigo="I.CS.H.5.10.2.",
            criterio_evaluacion=criterio_historia_5_10
        ),
        Indicador(
            description=(
                "Analiza las producciones intelectuales más significativas "
                "de las culturas aborígenes, sus formas de vida y "
                "organización social, sus edificaciones arquitectónicas y la "
                "vinculación existente entre la arquitectura y astronomía. "
                "(I.2.)"
            ),
            codigo="I.CS.H.5.11.1.",
            criterio_evaluacion=criterio_historia_5_11
        ),
        Indicador(
            description=(
                "Explica los principios de organización e intercambio social "
                "de los pobladores nativos y sus destrezas arquitectónicas "
                "incaicas, distinguiendo los diseños y funciones "
                "arquitectónicas de mayas, aztecas e incas. (J.4., I.2.)"
            ),
            codigo="I.CS.H.5.11.2.",
            criterio_evaluacion=criterio_historia_5_11
        ),
        Indicador(
            description=(
                "Relaciona la organización y diversidad productiva de los "
                "pisos ecológicos con la distribución demográfica dispersa, "
                "destacando la creatividad de mayas, aztecas e incas. (I.2.)"
            ),
            codigo="I.CS.H.5.11.3.",
            criterio_evaluacion=criterio_historia_5_11
        ),
        Indicador(
            description=(
                "Evalúa el impacto de la conquista en los aspectos "
                "ecológicos, culturales y sociales como resultado de la "
                "inserción de la evangelización, las relaciones de "
                "explotación a personas a través de haciendas y "
                "plantaciones, distinguiendo las semejanzas y diferencias "
                "entre estas últimas. (I.2.)"
            ),
            codigo="I.CS.H.5.12.1.",
            criterio_evaluacion=criterio_historia_5_12
        ),
        Indicador(
            description=(
                "Examina las configuraciones económicas en el tiempo de la "
                "Colonia, mediante el análisis del papel asignado a la mita "
                "y a las formas de extracción de riqueza (hacienda y a la "
                "plantación), destacando sus semejanzas y diferencias. "
                "(I.2., S.1.)"
            ),
            codigo="I.CS.H.5.12.2.",
            criterio_evaluacion=criterio_historia_5_12
        ),
        Indicador(
            description=(
                "Relaciona los antecedentes históricos de la comunidad "
                "afrodescendiente de Esmeraldas y El Chota con el tráfico de "
                "personas esclavizadas en el tiempo de la Colonia, y los "
                "elementos culturales integrados como resultado de su "
                "traslado ds, considerando los factores de producción en la "
                "hacienda y en la plantación. (J.4., I.2.)"
            ),
            codigo="I.CS.H.5.12.3.",
            criterio_evaluacion=criterio_historia_5_12
        ),
        Indicador(
            description=(
                "Describe el desarrollo histórico del proceso de conquista y "
                "colonización portuguesa, considerando el papel de los "
                "“bandeirantes” en los diferentes ciclos económicos "
                "relacionados con la esclavitud, la caña de azúcar y el oro. "
                "(J.1.)"
            ),
            codigo="I.CS.H.5.13.1.",
            criterio_evaluacion=criterio_historia_5_13
        ),
        Indicador(
            description=(
                "Analiza la relación económica entre el sistema latifundista "
                "y los “bandeirantes” a partir de la comparación de los "
                "procesos de colonización hispánico, portugués y anglosajón "
                "y su relación con la mano de obra esclava. (I.2.)"
            ),
            codigo="I.CS.H.5.13.2.",
            criterio_evaluacion=criterio_historia_5_13
        ),
        Indicador(
            description=(
                "Analiza las características del mestizaje y el sincretismo "
                "cultural en las obras de arte colonial hispanoamericano y "
                "lo compara con las características del arte barroco y "
                "mudéjar. (I.2.)"
            ),
            codigo="I.CS.H.5.14.1.",
            criterio_evaluacion=criterio_historia_5_14
        ),
        Indicador(
            description=(
                "Examina el papel de los conventos, misiones, procesos de "
                "educación y uso del arte colonial en el proceso de "
                "consolidación y expansión religiosa de la Colonia, "
                "considerando la función social del arte barroco y mudéjar. "
                "(J.1., I.2.)"
            ),
            codigo="I.CS.H.5.14.2.",
            criterio_evaluacion=criterio_historia_5_14
        ),
        Indicador(
            description=(
                "Relaciona los procesos de lucha de castas, clases y "
                "estamentos de la Colonia con las motivaciones de las "
                "sublevaciones indígenas, destacando el papel de Julián "
                "Apaza Nina (Túpac Katari), José Gabriel Condorcanqui "
                "Noguera (Túpac Amaru II) y Fernando Daquilema, y las "
                "contrasta con las razones por las qué Francisco Villa y "
                "Emiliano Zapata carecieron de un proyecto político. (J.1., "
                "I.2.)"
            ),
            codigo="I.CS.H.5.15.1.",
            criterio_evaluacion=criterio_historia_5_15
        ),
        Indicador(
            description=(
                "Analiza las motivaciones y propuestas de cambio de los "
                "actores individuales y colectivos que primaron en la "
                "Revolución mexicana, y su posterior influencia en "
                "movimientos de liberación en América Latina (Tupamaros, "
                "EZLN, FARC, ELN, Sendero Luminoso). (J.1., J.3., I.2.)"
            ),
            codigo="I.CS.H.5.15.2.",
            criterio_evaluacion=criterio_historia_5_15
        ),
        Indicador(
            description=(
                "Analiza el impacto social y económico de la Revolución "
                "cubana, destacando el embargo económico norteamericano y el "
                "liderazgo de Ernesto Guevara de la Serna y Fidel Castro. "
                "(J.1., I.2., S4)"
            ),
            codigo="I.CS.H.5.15.3.",
            criterio_evaluacion=criterio_historia_5_15
        ),
        Indicador(
            description=(
                "Explica los procesos de independencia política liberales "
                "criollos, marcados por su dependencia económica externa y "
                "sus proyectos nacionales con base social excluyente. (J.1.)"
            ),
            codigo="I.CS.H.5.16.1.",
            criterio_evaluacion=criterio_historia_5_16
        ),
        Indicador(
            description=(
                "Relaciona las diversas oleadas migratorias a América Latina "
                "con las revoluciones liberales y los alcances y "
                "limitaciones de sus proyectos nacionales, destacando sus "
                "aportes al desarrollo económico y cultural de la región. "
                "(J.1.,J.3.)"
            ),
            codigo="I.CS.H.5.16.2.",
            criterio_evaluacion=criterio_historia_5_16
        ),
        Indicador(
            description=(
                "Explica los alcances y limitaciones de las revoluciones "
                "liberales, en relación con las causas de la Gran Depresión "
                "en la economía latinoamericana y ecuatoriana y las "
                "propuestas de la CEPAL en función de un desarrollo "
                "autónomo. (J.1., J.3., I.2.)"
            ),
            codigo="I.CS.H.5.16.3.",
            criterio_evaluacion=criterio_historia_5_16
        ),
        Indicador(
            description=(
                "Examina el proceso de la “Revolución Ciudadana” en relación "
                "con la dependencia petrolera y la crisis de la deuda "
                "externa, reconociendo su impacto en la educación, salud y "
                "vivienda. (J.1.)"
            ),
            codigo="I.CS.H.5.17.1.",
            criterio_evaluacion=criterio_historia_5_17
        ),
        Indicador(
            description=(
                "Explica las causas del feriado bancario, del proceso de la "
                "dolarización y su relación con la masiva migración de los "
                "años 90 y la situación política actual. (J.3.,I.2.)"
            ),
            codigo="I.CS.H.5.17.2.",
            criterio_evaluacion=criterio_historia_5_17
        ),
        Indicador(
            description=(
                "Discute los efectos de los proyectos políticos y económicos "
                "de los últimos gobiernos (Bucaram, Mahuad y Gutiérrez), en "
                "función de las propuestas de educación, salud y vivienda. "
                "(J.1., I.2.)"
            ),
            codigo="I.CS.H.5.17.3.",
            criterio_evaluacion=criterio_historia_5_17
        ),
        Indicador(
            description=(
                "Explica la transición entre el sistema esclavista y el "
                "feudal, sus características económicas, sociales y "
                "políticas en Europa, subrayando la estructura de la "
                "sociedad y las formas modernas de esclavitud. (J.1., J.3.)"
            ),
            codigo="I.CS.H.5.18.1.",
            criterio_evaluacion=criterio_historia_5_18
        ),
        Indicador(
            description=(
                "Discute las características del sistema productivo de la "
                "América precolombina y del mercantilismo de Europa, "
                "considerando las diversas teorías y sistemas económicos "
                "adoptados en la América colonial, destacando diferencias y "
                "similitudes. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.18.2.",
            criterio_evaluacion=criterio_historia_5_18
        ),
        Indicador(
            description=(
                "Examina el proceso de acumulación originaria de capital "
                "(manufactura, personas esclavizadas y materias primas en "
                "Europa, África y América) en relación con el sistema "
                "económico que introdujo España en la América colonial. "
                "(J.1., I.2.)"
            ),
            codigo="I.CS.H.5.18.3.",
            criterio_evaluacion=criterio_historia_5_18
        ),
        Indicador(
            description=(
                "Explica la evolución e impacto económico y social que "
                "trajeron consigo las revoluciones industriales, "
                "relacionando estos acontecimientos con las principales "
                "características del liberalismo. (J.1., J.3., I.2.)"
            ),
            codigo="I.CS.H.5.19.1.",
            criterio_evaluacion=criterio_historia_5_19
        ),
        Indicador(
            description=(
                "Explica las características y relación entre el "
                "capitalismo, imperialismo, librecambismo y liberalismo, "
                "destacando el impacto de los procesos liberales más "
                "importantes (Independencia de los EE.UU, Revolución "
                "francesa e independencias hispanoamericanas).(J.1., J.4., "
                "I.2.)"
            ),
            codigo="I.CS.H.5.19.2.",
            criterio_evaluacion=criterio_historia_5_19
        ),
        Indicador(
            description=(
                "Explica las características del socialismo, el contexto "
                "histórico del aparecimiento de sus ideas y de las grandes "
                "revoluciones socialistas en relación con la crisis del "
                "socialismo real en la Unión Soviética y las reformas de la "
                "República Popular China. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.20.1.",
            criterio_evaluacion=criterio_historia_5_20
        ),
        Indicador(
            description=(
                "Examina el protagonismo de América Latina en el contexto de "
                "la Guerra Fría, y su actitud frente a la caída del "
                "socialismo real y la emergencia del neoliberalismo, con sus "
                "medidas y políticas económicas en el contexto de la "
                "globalización y el conflicto entre homogeneización y "
                "defensa de la identidad local y regional. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.20.2.",
            criterio_evaluacion=criterio_historia_5_20
        ),
        Indicador(
            description=(
                "Discute las causas de la crisis de los años ochenta en "
                "América Latina, sus principales retos y sus proyectos "
                "progresistas, considerando su relación con los principales "
                "postulados del socialismo del siglo XXI y del socialismo "
                "clásico. (J.1., I.2.)"
            ),
            codigo="I.CS.H.5.20.3.",
            criterio_evaluacion=criterio_historia_5_20
        ),
        Indicador(
            description=(
                "Explica y compara los orígenes y características de las "
                "distintas escuelas económicas fisiocrática, clásica, "
                "marxista, neoclásica, de Chicago, keynesiana, "
                "estructuralista y neoliberal, en función de elaborar un "
                "modelo económico de satisfacción de las necesidades de la "
                "mayoría de la población de América Latina y el "
                "Ecuador.(J.1., J.4., I.2.)"
            ),
            codigo="I.CS.H.5.21.1.",
            criterio_evaluacion=criterio_historia_5_21
        ),
        # Educación para la ciudadanía
        Indicador(
            description=(
                "Analiza el origen y evolución histórica de “ciudadanía” y "
                "“derechos” y los efectos que trae consigo la concepción de "
                "estos términos en la relación entre individuo y sociedad. "
                "(J.3.)"
            ),
            codigo="I.CS.EC.5.1.1.",
            criterio_evaluacion=criterio_ciudadania_5_1
        ),
        Indicador(
            description=(
                "Analiza los procesos históricos que propiciaron la "
                "Declaración de los Derechos del Hombre y del Ciudadano, la "
                "Declaración de los Derechos de la Mujer y la Ciudadana, la "
                "Declaración Universal de los Derechos Humanos y la relación "
                "entre individuo, sociedad y poder político. (J.3., S.1.)"
            ),
            codigo="I.CS.EC.5.1.2.",
            criterio_evaluacion=criterio_ciudadania_5_1
        ),
        Indicador(
            description=(
                "Explica las diferentes generaciones de derechos y el "
                "contexto histórico de su surgimiento, reconociendo la "
                "relación entre individuo, sociedad y poder político en cada "
                "una de las generaciones. (J.1., J.3.)"
            ),
            codigo="I.CS.EC.5.1.3.",
            criterio_evaluacion=criterio_ciudadania_5_1
        ),
        Indicador(
            description=(
                "Examina la igualdad natural de los seres humanos, su "
                "traducción jurídica como base para la protección frente a "
                "la arbitrariedad del poder y su expresión en todos los "
                "ámbitos. (J.1., J.2., J.3., S.1.)"
            ),
            codigo="I.CS.EC.5.2.1.",
            criterio_evaluacion=criterio_ciudadania_5_2
        ),
        Indicador(
            description=(
                "Argumenta que la igualdad natural de los seres humanos está "
                "dirigida a todos los grupos sociales, como generador de "
                "igualdad de opciones y oportunidades, considerando al "
                "sufragio universal como condición de participación "
                "igualitaria. (J.1., J.3., S.1.)"
            ),
            codigo="I.CS.EC.5.2.2.",
            criterio_evaluacion=criterio_ciudadania_5_2
        ),
        Indicador(
            description=(
                "Ejemplifica el origen de la democracia moderna y la "
                "alternabilidad, sus contradicciones (soberanía del pueblo y "
                "democracia para todos) y sus limitaciones (corrupción, "
                "persistencia de la exclusión social y surgimiento de nuevas "
                "élites) y la concepción natural y hereditaria del poder, "
                "destacando el significado y rol de la ciudadanía. (J.1., "
                "J.3.)"
            ),
            codigo="I.CS.EC.5.3.1.",
            criterio_evaluacion=criterio_ciudadania_5_3
        ),
        Indicador(
            description=(
                "Examina la definición, límites y dificultades de la "
                "democracia representativa y deliberativa reconociendo la "
                "posible complementariedad entre ellas y el rol de la "
                "ciudadanía. (J.1., J.2., J.3., I.2.)"
            ),
            codigo="I.CS.EC.5.3.2.",
            criterio_evaluacion=criterio_ciudadania_5_3
        ),
        Indicador(
            description=(
                "Contrasta las características de los derechos civiles, los "
                "derechos políticos y la representación política en la "
                "democracia social y en la democracia política. (J.1., J.3., "
                "I.1.)"
            ),
            codigo="I.CS.EC.5.4.1.",
            criterio_evaluacion=criterio_ciudadania_5_4
        ),
        Indicador(
            description=(
                "Analiza los procesos de legitimidad y representación "
                "política, partiendo del análisis de la deliberación y la "
                "implementación de mecanismos de control para el "
                "afianzamiento de los sistemas democráticos representativos. "
                "(J.1., J.2.)"
            ),
            codigo="I.CS.EC.5.4.2.",
            criterio_evaluacion=criterio_ciudadania_5_4
        ),
        Indicador(
            description=(
                "Argumenta las ventajas y limitaciones de la democracia "
                "deliberativa, democracia social y democracia política, "
                "analizando la necesidad de contar con mecanismos de "
                "deliberación pública. (I.2.)"
            ),
            codigo="I.CS.EC.5.4.3.",
            criterio_evaluacion=criterio_ciudadania_5_4
        ),
        Indicador(
            description=(
                "Ejemplifica la democracia como una experiencia social que "
                "puede llevarse a cabo en los diferentes espacios cotidianos "
                "mediante mecanismos de expresión y deliberación como forma "
                "de consenso y disenso. (J.1., S.1.,S4)"
            ),
            codigo="I.CS.EC.5.5.1.",
            criterio_evaluacion=criterio_ciudadania_5_5
        ),
        Indicador(
            description=(
                "Analiza el desarrollo de la democracia en el país "
                "identificando los procesos inclusivos, los alcances, "
                "limitaciones o dificultades en la resolución de demandas y "
                "expectativas sociales, reconociendo el derecho ciudadano de "
                "exigir la rendición de cuentas y/o la revocatoria del "
                "mandato. (J.1., J.2., I.2.)"
            ),
            codigo="I.CS.EC.5.6.1.",
            criterio_evaluacion=criterio_ciudadania_5_6
        ),
        Indicador(
            description=(
                "Examina la cultura nacional fundamentada en la "
                "plurinacionalidad, valorando los aportes de cada cultura y "
                "sus luchas sociales y políticas por el cumplimiento de los "
                "derechos sociales en pos de una sociedad intercultural y la "
                "armonía social. (J.1., S.2.)"
            ),
            codigo="I.CS.EC.5.7.1.",
            criterio_evaluacion=criterio_ciudadania_5_7
        ),
        Indicador(
            description=(
                "Explica la evolución histórica del Estado como forma de "
                "control social, identificando los mecanismos e "
                "instituciones que emplea para ejercer dicho control, y las "
                "funciones que lo diferencian de nacI.CS.EC.5.10.1. Examina "
                "las formas y postulados del republicanismo en contraste con "
                "otras formas de comprender la democracia, partiendo del "
                "análisis de casos. (J.1., I.4.)ión y gobierno. (J.1., J.3.)"
            ),
            codigo="I.CS.EC.5.8.1.",
            criterio_evaluacion=criterio_ciudadania_5_8
        ),
        Indicador(
            description=(
                "Examina la evolución y la necesidad de las Asambleas "
                "Constituyentes, reconociendo al pueblo como sujeto de ellas "
                "y a sus instrumentos jurídicos como expresión política de "
                "la sociedad. (J.1., J.3.)"
            ),
            codigo="I.CS.EC.5.9.1.",
            criterio_evaluacion=criterio_ciudadania_5_9
        ),
        Indicador(
            description=(
                "Reconoce la progresión de los derechos de ciudadanía "
                "mediante el análisis de las cartas constitucionales y de la "
                "Constitución de la República del Ecuador de 2008. (J.1., "
                "J.3.)"
            ),
            codigo="I.CS.EC.5.9.2.",
            criterio_evaluacion=criterio_ciudadania_5_9
        ),
        Indicador(
            description=(
                "Examina las formas y postulados del republicanismo en "
                "contraste con otras formas de comprender la democracia, "
                "partiendo del análisis de casos. (J.1., I.4.)"
            ),
            codigo="I.CS.EC.5.10.1.",
            criterio_evaluacion=criterio_ciudadania_5_10
        ),
        # Filosofía
        Indicador(
            description=(
                "Analiza el origen del pensamiento filosófico como crítica "
                "al pensamiento mítico, como la búsqueda del orden y la "
                "armonía, y como esfuerzo para explicar los fenómenos "
                "sociales y naturales, a partir de la reflexión en torno a "
                "problemas concretos, y la elaboración de preguntas "
                "complejas en función de ensayar respuestas significativas. "
                "(I.2.)"
            ),
            codigo="I.CS.F.5.1.1.",
            criterio_evaluacion=criterio_filosofia_5_1
        ),
        Indicador(
            description=(
                "Analiza las contribuciones del pensamiento filosófico en "
                "las diversas producciones del pensamiento humano en "
                "contraste con otras disciplinas, reconociendo la tendencia "
                "filosófica en cuanto a lo absoluto, hechos factuales y "
                "pensamiento cotidiano. (I.2.)"
            ),
            codigo="I.CS.F.5.1.2.",
            criterio_evaluacion=criterio_filosofia_5_1
        ),
        Indicador(
            description=(
                "Compara las desigualdades de la democracia griega con la "
                "actual, a partir del análisis del caso de intolerancia e "
                "irracionalidad que sufrió la pensadora Hipatia, "
                "representante de la escuela neoplatónica, y de la carencia "
                "de la persuasión y la deliberación en el ejercicio de la "
                "ciudadanía a través de conceptos fundamentales sobre la "
                "comunidad, el quehacer y formas políticas. (J.1., J.4., "
                "S.1.)"
            ),
            codigo="I.CS.F.5.2.1.",
            criterio_evaluacion=criterio_filosofia_5_2
        ),
        Indicador(
            description=(
                "Examina la importancia del método socrático y el diálogo "
                "racional y estructurado en la experiencia comunicativa del "
                "ser humano como “animal político”, en función de dilucidar "
                "las relaciones de poder que legitima una u otra posición "
                "filosófica. (J.3.)"
            ),
            codigo="I.CS.F.5.2.2.",
            criterio_evaluacion=criterio_filosofia_5_2
        ),
        Indicador(
            description=(
                "Diferencia la verdad de la validez en la formación de "
                "conceptos y teorías en las ciencias formales y fácticas, "
                "aplicándolas al análisis de discursos y editoriales de "
                "prensa de líderes políticos. (I.2., I.4.)"
            ),
            codigo="I.CS.F.5.3.1.",
            criterio_evaluacion=criterio_filosofia_5_3
        ),
        Indicador(
            description=(
                "Comprende y aplica las estructuras y principios de la "
                "argumentación lógica y lógica simbólica, evitando falacias, "
                "paradojas y contradicciones, estableciendo las tesis "
                "centrales y secundarias en la construcción de un discurso "
                "coherente y riguroso. (I.1.)"
            ),
            codigo="I.CS.F.5.4.1.",
            criterio_evaluacion=criterio_filosofia_5_4
        ),
        Indicador(
            description=(
                "Diferencia las falacias de las paradojas, comprendiendo y "
                "aplicando los principios de la argumentación y "
                "deliberación, en el análisis de textos académicos y de "
                "prensa. (J.3.)"
            ),
            codigo="I.CS.F.5.4.2.",
            criterio_evaluacion=criterio_filosofia_5_4
        ),
        Indicador(
            description=(
                "Compara las características del pensamiento filosófico "
                "occidental y latinoamericano, con sus nuevas concepciones, "
                "identificando sus preocupaciones esenciales (“yo” – "
                "“nosotros”; “objetividad” – “subjetividad”; “libertad” – "
                "“liberación”), su contexto histórico, su identidad, cultura "
                "y las características de sus productos intelectuales "
                "específicos (el ensayo y el tratado), discutiendo desde el "
                "método socrático el Sumak Kawsay como proyecto utópico "
                "posible en la construcción del “ser” latinoamericano. "
                "(J.3.)"
            ),
            codigo="I.CS.F.5.5.1.",
            criterio_evaluacion=criterio_filosofia_5_5
        ),
        Indicador(
            description=(
                "Comprende los fundamentos filosóficos de la ética, las "
                "nociones del bien y el mal, las nociones cristianas de la "
                "virtud y el pecado y las reflexiones del kantismo y el "
                "utilitarismo, mediante el análisis de casos reales del "
                "sistema político y la sociedad. (J.1., J.3., I.4.)"
            ),
            codigo="I.CS.F.5.6.1.",
            criterio_evaluacion=criterio_filosofia_5_6
        ),
        Indicador(
            description=(
                "Discute las virtudes platónicas y aristotélicas a partir de "
                "la reflexión en torno a las corrientes sobre el bien y el "
                "mal, destacando la formación de una opinión argumentada en "
                "casos de la vida cotidiana. (J.2., I.2., S.1.)"
            ),
            codigo="I.CS.F.5.6.2.",
            criterio_evaluacion=criterio_filosofia_5_6
        ),
        Indicador(
            description=(
                "Discute los significados de estética, belleza, felicidad y "
                "placer a partir de las reflexiones de Epicuro y Onfray, "
                "relacionándolos con las acciones de la sociedad moderna. "
                "(J.4., S4)"
            ),
            codigo="I.CS.F.5.7.1.",
            criterio_evaluacion=criterio_filosofia_5_7
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0055_auto_20180903_1439'),
    ]

    operations = [
        migrations.RunPython(create_indicadores,
                             reverse_code=migrations.RunPython.noop)
    ]
