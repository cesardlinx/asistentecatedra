from django.db import migrations


def create_criterios(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')
    CriterioEvaluacion = apps.get_model(
        'planificaciones', 'CriterioEvaluacion')

    # Asignaturas
    ingles = Asignatura.objects.get(name='Inglés')

    # Subniveles
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')

    CriterioEvaluacion.objects.bulk_create([
        # Inglés
        # Preparatoria
        CriterioEvaluacion(
            description=(
                "Identify and understand basic vocabulary, every-day words, "
                "including instructions."
            ),
            codigo="CE.EFL.1.1.",
            asignatura=ingles,
            subnivel=preparatoria
        ),
        CriterioEvaluacion(
            description=(
                "Follow short and simple instructions that include familiar "
                "vocabulary and identify key item of information in order to "
                "act upon them."
            ),
            codigo="CE.EFL.1.2.",
            asignatura=ingles,
            subnivel=preparatoria
        ),
        # Elemental
        CriterioEvaluacion(
            description=(
                "Differentiate between different living situations in a "
                "variety of surroundings and express curiosity about the "
                "world through simple questions."
            ),
            codigo="CE.EFL.2.1.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Catalog everyday objects and places in different cultures "
                "and recognize ways to act responsibly towards"
                "one’s environment and surroundings."
            ),
            codigo="CE.EFL.2.2.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Make use of basic personal information and expressions of "
                "politeness in order to introduce oneself and participate in "
                "a short conversation."
            ),
            codigo="CE.EFL.2.3.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Develop skills of collaboration by working together on "
                "projects and sharing materials while expressing personal "
                "preferences with peers."
            ),
            codigo="CE.EFL.2.4.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Model turn-taking and ways to express to others when "
                "something is not understood to improve comprehension and/or "
                "intelligibility in conversations."
            ),
            codigo="CE.EFL.2.5.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Listening for Meaning: Understand the main ideas in short "
                "simple spoken texts that include familiar vocabulary and "
                "are set in everyday contexts."
            ),
            codigo="CE.EFL.2.6.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Listening for Information: Follow short and simple spoken "
                "texts that include familiar vocabulary and are set in "
                "everyday contexts. Identify key items of information within "
                "the text, and record or act upon them."
            ),
            codigo="CE.EFL.2.7.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Production - Pronunciation: Produce individual words and "
                "short phrases clearly enough that other people can usually "
                "understand them easily."
            ),
            codigo="CE.EFL.2.8.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Production - Fluency: Utterances are sometimes produced "
                "slowly but use appropriate words and phrases to express "
                "basic ideas, initiate conversations and respond to "
                "questions, including some chunks of language and short "
                "sentences."
            ),
            codigo="CE.EFL.2.9.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Interaction – Interpersonal: Participate effectively in "
                "basic interpersonal interactions in everyday contexts, "
                "provided the interlocutor speaks slowly and clearly. "
                "(Example: requesting, introducing, responding, etc.)"
            ),
            codigo="CE.EFL.2.10.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Identify and understand individual every-day words, "
                "phrases, and sentences, including instructions."
            ),
            codigo="CE.EFL.2.11.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Understand the gist and details in short simple written "
                "texts(online or print)."
            ),
            codigo="CE.EFL.2.12.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Understand the content in a variety of well-known text "
                "types, both print and online, using the layout and artwork "
                "for support recognize typical signs and symbols found in "
                "the text types."
            ),
            codigo="CE.EFL.2.13.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Demonstrate familiarity with study resources (both print "
                "and digital). (Example: a picture dictionary, some "
                "flashcards of known words, or a word list.)"
            ),
            codigo="CE.EFL.2.14.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Learn to read graphs, diagrams, charts, and other kinds of "
                "graphic organizer. Demonstrate understanding of a text "
                "presented in the form of a graphic organizer(both print and "
                "digital)."
            ),
            codigo="CE.EFL.2.15.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Understand the main ideas in short simple written texts on "
                "cross-curricular subjects, both print and digital. "
                "(Example: art, science, music, math, history, etc.)"
            ),
            codigo="CE.EFL.2.16.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Write simple words, phrases, and sentences to demonstrate "
                "knowledge of spelling, punctuation, capitalization and "
                "handwriting / typography, and identify their meanings."
            ),
            codigo="CE.EFL.2.17.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Writing in order to perform controlled practice of "
                "vocabulary and grammar items."
            ),
            codigo="CE.EFL.2.18.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Convey some simple ideas, facts or opinions in a simple "
                "sentence or short paragraph, using basic vocabulary and "
                "structures."
            ),
            codigo="CE.EFL.2.19.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Complete a simple survey form or questionnaire by providing "
                "personal details. Write a variety of simple written text "
                "types, used in print or online, with appropriate layout and "
                "language. (Examples: message on a greeting card, name and "
                "address on an envelope, an email address, etc.)"
            ),
            codigo="CE.EFL.2.20.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Distinguish key information in stories and other "
                "age-appropriate literary texts, both oral and written."
            ),
            codigo="CE.EFL.2.21.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Describe and write about emotions and responses to literary "
                "texts through words and images, or other media(video, "
                "audio) on class or school bulletin boards and expand on "
                "ideas and responses to texts read/seen/heard in by "
                "participating in songs/chants, TPR activities and "
                "playground games."
            ),
            codigo="CE.EFL.2.22.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Display an affinity for a variety of literary texts by "
                "responding within a range of physical, cognitive, and "
                "attitudinal manners, and vary elements of a literary text "
                "to create a new text."
            ),
            codigo="CE.EFL.2.23.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Communicate ideas and experiences and create short original "
                "texts through a range of resources and other media, "
                "including ICT."
            ),
            codigo="CE.EFL.2.24.",
            asignatura=ingles,
            subnivel=elemental
        ),
        CriterioEvaluacion(
            description=(
                "Implement a range of creative thinking skills to show a "
                "respect for sharing and accepting different ideas in "
                "brainstorms and pair work."
            ),
            codigo="CE.EFL.2.25.",
            asignatura=ingles,
            subnivel=elemental
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0033_auto_20180809_1418'),
    ]

    operations = [
        migrations.RunPython(create_criterios)
    ]
