from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignatura
    educacion_cultural = Asignatura.objects.get(
        name='Educación Cultural y Artística'
    )

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    media = Subnivel.objects.get(name='Básica Media')
    superior = Subnivel.objects.get(name='Básica Superior')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    CriterioEvaluacion.objects.bulk_create([
        # Preparatoria
        CriterioEvaluacion(
            description=(
                "Expresa libremente sus emociones con la experimentación de "
                "sonidos de la naturaleza y de la voz, del cuerpo en "
                "movimiento, en el juego simbólico, en la narración y en la "
                "plástica, para la representación de sus propias ideas."
            ),
            codigo="CE.ECA.1.1.",
            asignatura=educacion_cultural,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Se interesa por la observación y participación en "
                "manifestaciones culturales y artísticas del entorno "
                "próximo."
            ),
            codigo="CE.ECA.1.2.",
            asignatura=educacion_cultural,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Expresa emociones,vivencias e ideas a través de lacreación "
                "individual de sencillas producciones artísticas en "
                "si-tuaciones lúdicas."
            ),
            codigo="CE.ECA.1.3.",
            asignatura=educacion_cultural,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Participa en acciones y creaciones artísticas colectivas a "
                "través de juegos y otras actividades libres o dirigidas."
            ),
            codigo="CE.ECA.1.4.",
            asignatura=educacion_cultural,
            subnivel=preparatoria
        ),
        # Elemental
        CriterioEvaluacion(
            description=(
                "Reconoce y define los rasgos característicos del propio "
                "cuerpo y de los cuerpos de otras personas, representados en "
                "producciones artísticas propias y ajenas."
            ),
            codigo="CE.ECA.2.1.",
            asignatura=educacion_cultural,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Identifica, por medio de los sentidos, las cualidades de "
                "elementos naturales y artificiales, y utiliza esta "
                "información en la selección de los materiales adecuados "
                "para la creación o elaboración de productos de distintas "
                "características."
            ),
            codigo="CE.ECA.2.2.",
            asignatura=educacion_cultural,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Observa, compara y realiza representaciones y "
                "construcciones con elementos del entorno natural y "
                "artificial."
            ),
            codigo="CE.ECA.2.3.",
            asignatura=educacion_cultural,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Genera productos artísticos como forma de expresión, "
                "representación y comunicación de emociones, vivencias e "
                "ideas."
            ),
            codigo="CE.ECA.2.4.",
            asignatura=educacion_cultural,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Identifica, registra y describe manifestaciones y "
                "producciones culturales y artísticas del entorno próximo."
            ),
            codigo="CE.ECA.2.5.",
            asignatura=educacion_cultural,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Reconoce platos típicos de la zona y siente interés por "
                "probarlos y conocer los procesos de elaboración."
            ),
            codigo="CE.ECA.2.6.",
            asignatura=educacion_cultural,
            subnivel=elemental
        ),
        # Media
        CriterioEvaluacion(
            description=(
                "Reconoce y representa la propia identidad y la historia "
                "personal a través de distintas formas de expresión."
            ),
            codigo="CE.ECA.3.1.",
            asignatura=educacion_cultural,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Identifica el uso de materiales naturales y artificiales en "
                "obras artísticas, y los utiliza en procesos de "
                "interpretación y creación."
            ),
            codigo="CE.ECA.3.2.",
            asignatura=educacion_cultural,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Localiza y reelabora información sobre el patrimonio "
                "artístico y cultural siguiendo las indicaciones y pautas "
                "que se le ofrecen."
            ),
            codigo="CE.ECA.3.3.",
            asignatura=educacion_cultural,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Participa en experiencias de creación colectiva e "
                "interpretación, aplicando lo aprendido en procesos de "
                "observación y búsqueda de información sobre el teatro de "
                "sombras."
            ),
            codigo="CE.ECA.3.4.",
            asignatura=educacion_cultural,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Cuenta historias a través de la creación colectiva de "
                "eventos sonoros o dramáticos."
            ),
            codigo="CE.ECA.3.5.",
            asignatura=educacion_cultural,
            subnivel=media
        ),
        CriterioEvaluacion(
            description=(
                "Aprecia los elementos que integran el patrimonio artístico "
                "y cultural, como fundamento de la identidad de los pueblos "
                "y de las culturas, y colabora en su conservación y "
                "renovación."
            ),
            codigo="CE.ECA.3.6.",
            asignatura=educacion_cultural,
            subnivel=media
        ),
        # Superior
        CriterioEvaluacion(
            description=(
                "Reconoce artistas y obras del Ecuador y del ámbito "
                "internacional, y utiliza sus conocimientos y habilidades "
                "perceptivas y comunicativas para describirlos y expresar "
                "puntos de vista."
            ),
            codigo="CE.ECA.4.1.",
            asignatura=educacion_cultural,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Indaga sobre artistas, obras y manifestaciones culturales, "
                "analizando algunos de los factores históricos o sociales "
                "que los rodean organiza y presenta la información usando "
                "diferentes formatos."
            ),
            codigo="CE.ECA.4.2.",
            asignatura=educacion_cultural,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Identifica y describe las interacciones que se producen "
                "entre las distintas formas de expresión artística en "
                "performances, representaciones teatrales, instalaciones y "
                "otras manifestaciones, y utiliza esos conocimientos en "
                "creaciones propias."
            ),
            codigo="CE.ECA.4.3.",
            asignatura=educacion_cultural,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Utiliza técnicas y recursos de los distintos lenguajes "
                "artísticos en la elaboración de producciones originales y "
                "en la transformación o remezcla de creaciones "
                "preexistentes, y crea diarios personales o portafolios que "
                "recopilen de manera ordenada la propia trayectoria "
                "artística."
            ),
            codigo="CE.ECA.4.4.",
            asignatura=educacion_cultural,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Planifica, argumenta razonadamente y desarrolla proyectos "
                "de creación artística y eventos culturales locales."
            ),
            codigo="CE.ECA.4.5.",
            asignatura=educacion_cultural,
            subnivel=superior
        ),
        CriterioEvaluacion(
            description=(
                "Valora los medios audiovisuales y las tecnologías de la "
                "información y la comunicación como instrumentos de "
                "aprendizaje y producción cultural y artística, y los "
                "utiliza en procesos de recepción, búsqueda de información, "
                "creación y difusión de contenidos artísticos y culturales."
            ),
            codigo="CE.ECA.4.6.",
            asignatura=educacion_cultural,
            subnivel=superior
        ),
        # Bachillerato
        CriterioEvaluacion(
            description=(
                "Investiga y expresa puntos de vista sobre las "
                "manifestaciones artísticas y culturales, interpretando sus "
                "usos y funciones en la vida de las personas y las "
                "sociedades, y mostrando una actitud de interés y "
                "receptividad hacia las opiniones ajenas."
            ),
            codigo="CE.ECA.5.1.",
            asignatura=educacion_cultural,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Reconoce obras de diferentes artistas(femeninas y "
                "masculinos) y manifestaciones culturales del presente y del "
                "pasado, valorando la diversidad y la coexistencia de "
                "distintas formas de expresión, y colabora en su "
                "conservación y renovación."
            ),
            codigo="CE.ECA.5.2.",
            asignatura=educacion_cultural,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Planifica, desarrolla y evalúa individualmente y en grupo "
                "procesos de creación artística en los que se expresen, "
                "comuniquen y representen ideas, vivencias y emociones."
            ),
            codigo="CE.ECA.5.3.",
            asignatura=educacion_cultural,
            subnivel=bachillerato
        ),
        CriterioEvaluacion(
            description=(
                "Valora el uso de medios audiovisuales y recursos "
                "tecnológicos en la creación artística, y utiliza estos "
                "medios para la creación, producción y difusión de obras "
                "propias."
            ),
            codigo="CE.ECA.5.4.",
            asignatura=educacion_cultural,
            subnivel=bachillerato
        )
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0025_auto_20180807_0933'),
    ]

    operations = [
        migrations.RunPython(
            create_criterios, reverse_code=migrations.RunPython.noop)
    ]
