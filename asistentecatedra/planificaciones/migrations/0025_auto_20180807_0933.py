from django.db import migrations


def create_objetivos(apps, schema_editor):
    Objetivo = apps.get_model('planificaciones', 'Objetivo')
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    ingles = Asignatura.objects.get(name='Inglés')

    # Subniveles
    elemental = Subnivel.objects.get(name='Básica Elemental')

    Objetivo.objects.bulk_create([
        # Elemental
        Objetivo(
            description=(
                "Identify some main ideas an details of written texts, in "
                "order to develop an approach of critical inquiry to written "
                "and oral texts."
            ),
            codigo='O.EFL.2.1.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Assess and appreciate English as an international language, "
                "as well as the five aspects of English that contribute to "
                "communicative competence."
            ),
            codigo='O.EFL.2.2.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Independently read level-appropriate texts in English for "
                "pure enjoyment/entertainment and to access information."
            ),
            codigo='O.EFL.2.3.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Develop creative and critical thinking skills to foster "
                "problem-solving and independent learning using both spoken "
                "and written English."
            ),
            codigo='O.EFL.2.4.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Use in-class library resources and explore the use of ICT "
                "to enrich competences in the four skills."
            ),
            codigo='O.EFL.2.5.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Write short descriptive and informative texts and use them "
                "as a means of communication and written expression of "
                "thought."
            ),
            codigo='O.EFL.2.6.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Appreciate the use of English language through spoken and "
                "written literary texts such as poems, rhymes, chants, "
                "riddles and songs, in order to foster imagination, "
                "curiosity and memory, while developing a taste for "
                "literature."
            ),
            codigo='O.EFL.2.7.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Demonstrate a living relationship with the English language "
                "through interaction with written and spoken texts, in order "
                "to explore creative writing as an outlet to personal "
                "expression."
            ),
            codigo='O.EFL.2.8.',
            subnivel=elemental,
            asignatura=ingles
        ),
        Objetivo(
            description=(
                "Be able to interact in English in a simple way using basic "
                "expressions and short phrases in familiar contexts to "
                "satisfy needs of a concrete type, provided others talk "
                "slowly and clearly and are prepared to help."
            ),
            codigo='O.EFL.2.9.',
            subnivel=elemental,
            asignatura=ingles
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0024_auto_20180806_1838'),
    ]

    operations = [
        migrations.RunPython(
            create_objetivos, reverse_code=migrations.RunPython.noop)
    ]
