from django.db import migrations


def create_objetivos_edfisica(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    educacion_fisica = Area.objects.get(name='Educación Física')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Participar autónomamente en diversas prácticas corporales, "
                "disponiendo de conocimientos (corporales, conceptuales, "
                "emocionales, motrices entre otros) que le permitan hacerlo "
                "de manera saludable, segura y placentera a lo largo de su "
                "vida."
            ),
            codigo="OG.EF.1.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Asociar y transferir conocimientos de otros campos "
                "disciplinares, para optimizar su desempeño en las prácticas "
                "corporales."
            ),
            codigo="OG.EF.2.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Resolver de manera eficaz las situaciones presentes en las "
                "prácticas corporales (deportes, danzas, juegos, entre "
                "otras), teniendo claridad sobre sus objetivos, lógicas e "
                "implicaciones, según los niveles de participación en los "
                "que se invlucre (recreativo, federativo, de alto "
                "rendimiento, etc.)."
            ),
            codigo="OG.EF.3.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Profundizar en el desarrollo psicomotriz y la mejora de la "
                "condición física de modo seguro y saludable, de acuerdo a "
                "las necesidades individuales y colectivas del educando en "
                "función de las prácticas corporales que elija."
            ),
            codigo="OG.EF.4.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Posicionarse críticamente frente a los discursos y "
                "representaciones sociales sobre cuerpo y salud, para tomar "
                "decisiones acordes a sus intereses y necesidades."
            ),
            codigo="OG.EF.5.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Utilizar los aprendizajes adquiridos en Educación Física "
                "para tomar decisiones sobre la consntrucción, cuidado y "
                "mejora de su salud y bienestar, acorde a sus intereses y "
                "necesidades."
            ),
            codigo="OG.EF.6.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Acordar y consensuar con otros para compartir prácticas "
                "corporales, reconociendo y respetando diferencias "
                "individuales y culturales."
            ),
            codigo="OG.EF.7.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Participar de manera segura, placentera, saludable y "
                "sustentable en prácticas corporales en diversos "
                "contextos/ambientes, asegurando su respeto y preservación."
            ),
            codigo="OG.EF.8.",
            area=educacion_fisica
        ),
        ObjetivoGeneral(
            description=(
                "Reconocer que los sentidos y significados de las prácticas "
                "corporales enriquecen el patrimonio cultural y favorecen la "
                "construcción de la identidad del estado ecuatoriano"
            ),
            codigo="OG.EF.9.",
            area=educacion_fisica
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0008_auto_20180727_1840'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_edfisica)
    ]
