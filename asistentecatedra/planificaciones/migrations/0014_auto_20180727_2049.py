from django.db import migrations


def create_objetivos_extranjera(apps, schema_editor):
    Area = apps.get_model('planificaciones', 'Area')
    ObjetivoGeneral = apps.get_model('planificaciones', 'ObjetivoGeneral')

    # Area
    lengua_extranjera = Area.objects.get(name='Lengua Extranjera')

    ObjetivoGeneral.objects.bulk_create([
        ObjetivoGeneral(
            description=(
                "Encounter socio-cultural aspects of their own and other "
                "countries in a thoughtful and inquisitive manner, maturely, "
                "and openly experiencing other cultures and languages from "
                "the secure standpoint of their own national and cultural "
                "identity."
            ),
            codigo="OG.EFL.1.",
            area=lengua_extranjera
        ),
        ObjetivoGeneral(
            description=(
                "Draw on this established propensity for curiosity and "
                "tolerance towards different cultures to comprehend the role "
                "of diversity in building an intercultural and multinational "
                "society."
            ),
            codigo="OG.EFL.2.",
            area=lengua_extranjera
        ),
        ObjetivoGeneral(
            description=(
                "Access greater flexibility of mind, creativity, enhanced "
                "linguistic intelligence, and critical thinking skills "
                "through an appreciation of liguistic differences. Enjoy an "
                "enriched perspective of their own language use for "
                "communication and learning."
            ),
            codigo="OG.EFL.3.",
            area=lengua_extranjera
        ),
        ObjetivoGeneral(
            description=(
                "Deploy a range of learning strategies, thereby increasing "
                "disposition and ability to independently access further "
                "(language) learning and practice opportunities. Respect "
                "themselves and others within the communication process, "
                "cultivating habits of honesty and integrity into "
                "responsible academic behavior."
            ),
            codigo="OG.EFL.4.",
            area=lengua_extranjera
        ),
        ObjetivoGeneral(
            description=(
                "Directly access the main points and important details of "
                "up-to-date English language texts, such as those published "
                "on the web, for professional or general investigation, "
                "through the efficient use of ICT and reference tools where "
                "required."
            ),
            codigo="OG.EFL.5.",
            area=lengua_extranjera
        ),
        ObjetivoGeneral(
            description=(
                "Through selected media, participate in reasonably extended "
                "spoken or written dialogue with peers from different "
                "backgrounds on work, study or general topics of common "
                "interest, expressing ideas and opinions effectively and "
                "appropriately."
            ),
            codigo="OG.EFL.6.",
            area=lengua_extranjera
        ),
        ObjetivoGeneral(
            description=(
                "Interact quite clearly, confidently, and appropriately in a "
                "range of formal and informal social situations with a "
                "limited but effective command of the spoken laguage (CEFR "
                "B1 level)."
            ),
            codigo="OG.EFL.7.",
            area=lengua_extranjera
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0013_auto_20180727_2035'),
    ]

    operations = [
        migrations.RunPython(create_objetivos_extranjera)
    ]
