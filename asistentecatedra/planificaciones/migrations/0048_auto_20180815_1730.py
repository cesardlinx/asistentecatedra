from django.db import migrations


def create_destrezas(apps, schema_editor):
    Asignatura = apps.get_model('planificaciones', 'Asignatura')
    Destreza = apps.get_model('planificaciones', 'Destreza')
    BloqueCurricular = apps.get_model('planificaciones', 'BloqueCurricular')
    Subnivel = apps.get_model('planificaciones', 'Subnivel')

    # Asignatura
    ingles = Asignatura.objects.get(name='Inglés')
    gestion = Asignatura.objects.get(name='Emprendimiento y Gestión')

    # Bloques Inglés
    bloque1_ingles = BloqueCurricular.objects.get(
        name="Communication and Cultural Awareness")
    bloque2_ingles = BloqueCurricular.objects.get(
        name="Oral Communication: (Listening and Speaking)")
    bloque3_ingles = BloqueCurricular.objects.get(name="Reading")
    bloque4_ingles = BloqueCurricular.objects.get(
        name="Writing")
    bloque5_ingles = BloqueCurricular.objects.get(
        name="Language through the Arts")

    # Bloques Emprendimiento y Gestión
    bloque1_emprendimiento = BloqueCurricular.objects.get(
        name="Planificación y control financiero del emprendimiento")
    bloque2_emprendimiento = BloqueCurricular.objects.get(
        name="Responsabilidad legal y social del emprendedor"
    )
    bloque3_emprendimiento = BloqueCurricular.objects.get(
        name="Investigación de mercado y estadística aplicada")
    bloque4_emprendimiento = BloqueCurricular.objects.get(
        name="Economía para la toma de decisiones")
    bloque5_emprendimiento = BloqueCurricular.objects.get(
        name="Formulación del proyecto de emprendimiento")
    bloque6_emprendimiento = BloqueCurricular.objects.get(
        name="Evaluación del proyecto de emprendimiento")

    # Subnivel
    preparatoria = Subnivel.objects.get(name='Básica Preparatoria')
    elemental = Subnivel.objects.get(name='Básica Elemental')
    bachillerato = Subnivel.objects.get(name='Bachillerato General Unificado')

    Destreza.objects.bulk_create([
        # Inglés
        # Preparatoria
        Destreza(
            description=(
                "Respond to simple questions about personal information in "
                "class using the following: example (What´s your name? I´m "
                "…, How old are you? I´m……, Where do you live? In …..)."
            ),
            codigo="EFL.1.1.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Identify key members of the family if there is visual "
                "support (mother, father, brother, sister, grandfather, "
                "grandmother)."
            ),
            codigo="EFL.1.1.2.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Follow simple instructions related to classroom activities "
                "(open your book, close your book, stand up, listen, sit "
                "down, be quiet, look, point, paint, cut, glue, circle)."
            ),
            codigo="EFL.1.1.3.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recognize familiar words, names, and objects at school "
                "(Backpack, book, chair, eraser, pencil, table, teacher, "
                "peer)."
            ),
            codigo="EFL.1.2.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Show understanding of some basic words about ¨MY HOUSE¨ if "
                "there is visual support (bedroom, kitchen, living room, bed, "
                "door, sofa)."
            ),
            codigo="EFL.1.2.2.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recognize basic vocabulary related to animals (bird, dog, "
                "cat, duck, fish, frog, tiger) when listening to the sounds "
                "or if there is visual support."
            ),
            codigo="EFL.1.3.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recognize the animals by doing the action when listening to "
                "the animal word …… (actions: fly, jump, swim, run)."
            ),
            codigo="EFL.1.3.2.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recognize basic vocabulary related to food (cake, apple, "
                "orange, banana, egg, milk, chips) if there is visual "
                "support."
            ),
            codigo="EFL.1.3.3.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Identify the numbers 0-9 when counting different objects in "
                "class."
            ),
            codigo="EFL.1.4.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recognize basic shapes (circle, square, triangle) using "
                "classroom objects."
            ),
            codigo="EFL.1.4.2.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Understand and use basic expressions to facilitate "
                "interpersonal interaction when playing. (It´s my turn, It´s "
                "your turn….., Let´s play, Ok, you start)."
            ),
            codigo="EFL.1.5.1.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Identify location of people, objects, animals, using: on, "
                "in, under when responding to simple questions. Example ( "
                "Where is the pencil? it´s on the table, What´s this? It´s "
                "a…)."
            ),
            codigo="EFL.1.5.2.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Use common values of giving, asking nicely, and sharing "
                "(Let´s share, please, thank you, pass me the….please, here "
                "´s a ….. for you)."
            ),
            codigo="EFL.1.5.3.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Exchange basic personal preferences with peers when "
                "expressing likes and dislikes ( I like …… ,I don´t like "
                "……..)."
            ),
            codigo="EFL.1.5.4.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Identify the basic colors (black, blue, red, white, yellow, "
                "green) when painting and drawing."
            ),
            codigo="EFL.1.6.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Sing along enunciating some of the words learned with "
                "rhythms, etc."
            ),
            codigo="EFL.1.6.2.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Clap, or sing along enunciating some of the animals "
                "learned."
            ),
            codigo="EFL.1.6.3.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Recognize basic vocabulary about ¨the body¨ (arm, eye, hand, "
                "nose, head, ear, leg, mouth, feet) by pointing to the parts "
                "of the body)."
            ),
            codigo="EFL.1.7.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Move and sing along using the vocabulary learned."
            ),
            codigo="EFL.1.7.2.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        Destreza(
            description=(
                "Respond to action words such as run, stop, jump, walk, up, "
                "and down."
            ),
            codigo="EFL.1.7.3.",
            asignatura=ingles,
            subnivel=preparatoria,
        ),
        # Elemental
        # Bloque 1
        Destreza(
            description=(
                "Exchange basic introductions and limited personal "
                "information in class using simple present tense in order to "
                "get to know their peers. (Example: where one lives or goes "
                "to school, etc.)"
            ),
            codigo="EFL.2.1.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Recognize the differences between where people live among "
                "the regions of the country in order to appreciate their own "
                "environment. (Example: house/apartment, country/city, etc.)"
            ),
            codigo="EFL.2.1.2.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Ask simple basic questions in class about the world beyond "
                "their own immediate environment in order to increase their "
                "understanding of different cultures."
            ),
            codigo="EFL.2.1.3.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Express curiosity about the world and other cultures by "
                "asking simple WH- questions in class after reading and/or "
                "participating in presentations or other group work."
            ),
            codigo="EFL.2.1.4.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Recognize ways to relate responsibly to one’s surroundings "
                "at home and at school by exhibiting responsible behaviors "
                "towards the environment. (Example: chores at home, "
                "recycling, etc.)"
            ),
            codigo="EFL.2.1.5.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Understand and use common expressions of politeness in "
                "class while working in pairs or groups on projects. "
                "(Example: please, sorry, thank you, etc.)"
            ),
            codigo="EFL.2.1.6.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Collaborate in a friendly manner by sharing classroom "
                "materials and personal objects while participating in games "
                "and activities in class and on the playground."
            ),
            codigo="EFL.2.1.7.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Exchange basic personal preferences with peers in order to "
                "express likes and dislikes."
            ),
            codigo="EFL.2.1.8.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Communicate to peers and teacher when something is not "
                "understood in class through the use of simple basic "
                "questions."
            ),
            codigo="EFL.2.1.9.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        Destreza(
            description=(
                "Recognize when to speak and when to listen while working in "
                "pairs or small groups in class by following classroom "
                "instructions and simple commands."
            ),
            codigo="EFL.2.1.10.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque1_ingles
        ),
        # Bloque 2
        Destreza(
            description=(
                "Understand meanings expressed in short dialogues on "
                "familiar topics, as well as basic spoken instructions and "
                "simple questions about self, people, animals or things, "
                "especially when spoken slowly and clearly. (Example: "
                "greetings, short phrases, basic range of classroom "
                "instructions, common personal information questions: What’s "
                "your name? How old are you? Where do you live? etc.)"
            ),
            codigo="EFL.2.2.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Infer who is speaking and what the situation is when "
                "listening to short simple texts, especially when "
                "accompanied by pictures or other visual aids, or sound "
                "effects.(Example: shopkeeper speaking to a customer who is "
                "buying some fruit.)"
            ),
            codigo="EFL.2.2.2.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Recognize familiar names, words, and short phrases about "
                "simple everyday topics whether heard in isolation or within "
                "short, simple spoken texts describing people and objects. "
                "(Example: vocabulary about self, family, friends and "
                "immediate surroundings at school and home, adjectives for "
                "color and size, etc.)"
            ),
            codigo="EFL.2.2.3.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Identify items of specific information within simple "
                "messages or from short and simple descriptions about "
                "familiar contexts, especially if visual support is "
                "provided. (Example: letters of the alphabet, numbers, "
                "prices and times, days, dates and months, etc.)"
            ),
            codigo="EFL.2.2.4.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Record key items of specific information from a heard "
                "message or description, either in written form or by "
                "drawing picture. (Example: letters of the alphabet, "
                "numbers, quantities, prices and times, days, dates and "
                "months, etc.)"
            ),
            codigo="EFL.2.2.5.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Enjoy extensive listening in English. (Example: listen to "
                "stories, watch short movies, experience song lyrics or "
                "poetry, etc.)"
            ),
            codigo="EFL.2.2.6.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Be comfortable taking meaning from spoken texts containing "
                "words or sections which are not understood. Be aware that "
                "understanding spoken texts does not require decoding every "
                "single word."
            ),
            codigo="EFL.2.2.7.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Imitate individual English language sounds, especially "
                "those phonemes which do not exist in the student’s own L1, "
                "both in"
                "isolation and within key vocabulary items. (Example: /ŋ/ /ð/ "
                "/ʌ/ /i:/ and in words like singing, these, up, sea, etc.)"
            ),
            codigo="EFL.2.2.8.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Spell out key vocabulary items using the English alphabet. "
                "(Example: names, colors, animals, possessions, etc.)"
            ),
            codigo="EFL.2.2.9.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Clap, move, chant or sing along with short authentic "
                "English language rhymes or songs, approximating English "
                "rhythm and intonation once familiar with the text. "
                "(Example: jump or clap in time to jump-rope rhymes, do the "
                "actions to action songs or short rhythmic poems, "
                "enunciating some of words in time with the rhythm, etc."
            ),
            codigo="EFL.2.2.10.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Produce simple, mainly isolated utterances using very short "
                "phrases and sometimes individual words, possibly with slow "
                "and/or hesitant delivery. (Example: words, phrases, and "
                "short sentences about people, animals, things, etc.)."
            ),
            codigo="EFL.2.2.11.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Respond to simple questions in quite a short time and "
                "initiate basic interaction spontaneously when there are "
                "opportunities to speak. Speech is produced a little less "
                "slowly and hesitantly."
            ),
            codigo="EFL.2.2.12.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Understand and use basic greetings, leave-taking "
                "expressions, and other simple everyday phrases to "
                "facilitate interpersonal interaction, to introduce others, "
                "and to name things. (Example: Thank-you, Can I help you? "
                "This is [name]. It’s a [item], etc.)"
            ),
            codigo="EFL.2.2.13.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Ask and answer basic personal information questions, as "
                "well as simple questions about other people, animals, and "
                "possessions, provided the interaction is slow and clear. "
                "(Example: Where do you live? Do you have a bicycle? What "
                "color is it? etc.)"
            ),
            codigo="EFL.2.2.14.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Exchange specific information with another person, provided "
                "they talk slowly and clearly and are prepared to help. "
                "(Example: factual information about colors, numbers, "
                "quantities, prices, times, size, etc.)"
            ),
            codigo="EFL.2.2.15.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "Say when they do not understand and ask for slower or "
                "clearer repetition where required. (Example: Sorry? Could "
                "you say that again, please? etc.)"
            ),
            codigo="EFL.2.2.16.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        Destreza(
            description=(
                "React appropriately to what others say using "
                "verbal/non-verbal back-channeling, or by asking further "
                "simple questions to extend the interaction. (Example: "
                "express interest using facial expression or simple words "
                "with appropriate intonation:"
                "Oh!, Yes! Thanks. And you? etc.)"
            ),
            codigo="EFL.2.2.17.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque2_ingles
        ),
        # Bloque 3
        Destreza(
            description=(
                "Demonstrate basic reading comprehension skills by "
                "identifying the meaning of individual words, phrases, and "
                "sentences, including simple written instructions."
            ),
            codigo="EFL.2.3.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Read a short simple text (online or print) and demonstrate "
                "understanding of the gist and some basic details of the "
                "content."
            ),
            codigo="EFL.2.3.2.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Understand most of the details of the content of a short "
                "simple text (online or print)."
            ),
            codigo="EFL.2.3.3.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Understand the content in simple short written "
                "environmental print text types, using artwork, symbols and "
                "layout for support. (Example: price tags, signs, notices "
                "(No eating, etc.), candy wrappers, etc.)"
            ),
            codigo="EFL.2.3.4.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Show the ability to use a simple learning resource. "
                "(Example: a small set of flashcards, a picture-based "
                "dictionary (online or print), or a simple word list)."
            ),
            codigo="EFL.2.3.5.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Understand the content of a simple graphic organizer "
                "(online or print). (Example, Venn Diagrams, charts, and "
                "labeled diagrams.)"
            ),
            codigo="EFL.2.3.6.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Read and understand the main ideas in a short simple text "
                "on a cross-curricular topic. (Example: art, music, history, "
                "etc.)"
            ),
            codigo="EFL.2.3.7.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Show understanding of some basic details in short simple "
                "cross-curricular texts by matching, labeling, and answering "
                "simple questions."
            ),
            codigo="EFL.2.3.8.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Identify the meaning of specific content-based words and "
                "phrases, with the aid of visual support."
            ),
            codigo="EFL.2.3.9.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        Destreza(
            description=(
                "Read a variety of simple text-types and graphic organizers "
                "used to present cross-curricular information (Example: "
                "instructions, graphs, diagrams, charts, plans or maps, "
                "etc.)"
            ),
            codigo="EFL.2.3.10.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque3_ingles
        ),
        # Bloque 4
        Destreza(
            description=(
                "Know how to spell simple English words correctly, "
                "demonstrating awareness of sound-letter relationships. "
                "(Example: sea, mean, bee, etc.)"
            ),
            codigo="EFL.2.4.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Make a simple learning resource, in order to record and "
                "practice new words. (Example: a picture dictionary, a word "
                "list, set of flashcards, etc.)."
            ),
            codigo="EFL.2.4.2.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Write simple words, phrases and sentences with correct use "
                "of standard writing mechanics. (Example: spelling, "
                "punctuation, capitalization, and writing by hand and/or on "
                "the computer."
            ),
            codigo="EFL.2.4.3.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Write simple words, phrases and sentences for controlled "
                "practice of language items."
            ),
            codigo="EFL.2.4.4.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Write simple sentences on familiar topics to communicate "
                "basic ideas."
            ),
            codigo="EFL.2.4.5.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Write a short simple paragraph to convey some simple facts "
                "about people, animals, places, things, yourself or others, "
                "with the support of a model text. (Example: where they "
                "live, what they do, etc.)"
            ),
            codigo="EFL.2.4.6.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Write a short simple paragraph to describe yourself or "
                "other people, animals, places and things, with limited "
                "support. (Example: by answering questions or using key "
                "words)."
            ),
            codigo="EFL.2.4.7.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Complete a basic survey or a questionnaire by providing "
                "personal details."
            ),
            codigo="EFL.2.4.8.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        Destreza(
            description=(
                "Write a variety of short simple text-types, commonly used "
                "in print and online, with appropriate language and layout. "
                "(Example: write a greeting on a birthday card, name and "
                "address on an envelope, a URL for a website, an email "
                "address, etc.)"
            ),
            codigo="EFL.2.4.9.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque4_ingles
        ),
        # Bloque 5
        Destreza(
            description=(
                "Identify key information such as events, characters, and "
                "objects in stories and other age-appropriate literary texts "
                "if there is visual support."
            ),
            codigo="EFL.2.5.1.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Express emotions and feelings using basic adjectives and "
                "related images through written work on the school or class "
                "bulletin board."
            ),
            codigo="EFL.2.5.2.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Use audio, video, and pictures to respond to a variety of "
                "literary texts through online or in-class ICT activities."
            ),
            codigo="EFL.2.5.3.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Listen to and read short narratives and/or other oral and "
                "written literary texts in class (with a preference for "
                "authentic texts) in order to stimulate imagination, "
                "curiosity, and a love for literature."
            ),
            codigo="EFL.2.5.4.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Apply ICT and/or other resources to communicate simple "
                "thoughts in small groups."
            ),
            codigo="EFL.2.5.5.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Generate and expand ideas by responding in a fun and "
                "playful manner to oral and written texts in order to "
                "increase enjoyment of the language through TPR, playground "
                "games, and songs and chants."
            ),
            codigo="EFL.2.5.6.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Create picture books and/or other graphic expressions in "
                "pairs in class by varying scenes, characters, or other "
                "elements of literary texts."
            ),
            codigo="EFL.2.5.7.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Produce short, creative texts using ICT and/or other "
                "resources at home or at school in order to recreate "
                "familiar scenes and themes."
            ),
            codigo="EFL.2.5.8.",
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        Destreza(
            description=(
                "Use creative thinking skills to learn how to share and "
                "respect all ideas through brainstorming activities and pair "
                "work in class."
            ),
            codigo="EFL.2.5.9.",
            imprescindible=True,
            asignatura=ingles,
            subnivel=elemental,
            bloque=bloque5_ingles
        ),
        # Emprendimiento y Gestión
        # Bloque 1
        Destreza(
            description=(
                "Describir y explicar los conceptos financieros básicos de "
                "un emprendimiento, como “ingresos”, “costos”, “gastos” e "
                "“inversión”, “punto de equilibrio” y sus proyecciones "
                "futuras como elemento fundamental para las proyecciones."
            ),
            codigo="EG.5.1.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Distinguir los diferentes tipos de costos y gastos de un "
                "emprendimiento para determinar detenidamente el capital de "
                "trabajo necesario para un emprendimiento."
            ),
            codigo="EG.5.1.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar la obligatoriedad jurídica de llevar "
                "contabilidad, de acuerdo a lo establecido por las normas "
                "tributarias, como elemento fundamental para determinar la "
                "forma de llevar la contabilidad."
            ),
            codigo="EG.5.1.3.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Deducir la importancia de la contabilidad como elemento de "
                "control financiero del emprendimiento."
            ),
            codigo="EG.5.1.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Explicar las principales normas contables, relacionadas con "
                "la partida doble, para establecer los impactos en las "
                "cuentas."
            ),
            codigo="EG.5.1.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Clasificar las principales cuentas contables con su "
                "respectivo nombre para personificarlas, mediante la "
                "determinación de la naturaleza de su función en los "
                "asientos contables, tales como caja, bancos, cuentas por "
                "cobrar, inventarios, activos fijos, depreciación, capital, "
                "cuentas por pagar, préstamos bancarios, capital."
            ),
            codigo="EG.5.1.6.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar los componentes básicos del activo, pasivo, "
                "patrimonio, ingresos, costos y gastos, de acuerdo con la "
                "normativa contable, para clasificar adecuadamente las "
                "cuentas contables."
            ),
            codigo="EG.5.1.7.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Interpretar las cuentas contables mediante la "
                "identificación de los cambios que causan las transacciones "
                "en los activos, pasivos y patrimonios, reflejados en la "
                "cuenta por partida doble."
            ),
            codigo="EG.5.1.8.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Elaborar un balance general básico mediante la aplicación "
                "de los principios, conceptos y técnicas contables y la "
                "normatividad vigente."
            ),
            codigo="EG.5.1.9.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        Destreza(
            description=(
                "Elaborar un estado de pérdidas y ganancias básico mediante "
                "la aplicación de las cuentas contables y la ecuación "
                "contable en un caso de estudio."
            ),
            codigo="EG.5.1.10.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque1_emprendimiento
        ),
        # Bloque 2
        Destreza(
            description=(
                "Elaborar un mapeo de los requisitos legales básicos para "
                "iniciar actividades de emprendimiento que permitan "
                "formalizarlo."
            ),
            codigo="EG.5.2.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar las obligaciones legales que debe cumplir un "
                "emprendedor como elemento fundamental para la operación del "
                "emprendimiento."
            ),
            codigo="EG.5.2.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y argumentar la importancia del pago de las "
                "obligaciones sociales y tributarias a la autoridad "
                "respectiva, como retribución de los servicios públicos "
                "utilizados e incentivos fiscales recibidos, para fomentar "
                "una cultura tributaria."
            ),
            codigo="EG.5.2.3.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar los conocimientos tributarios en el llenado de los "
                "formularios básicos del SRI (RISE, IVA e Impuesto a la "
                "Renta)."
            ),
            codigo="EG.5.2.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque2_emprendimiento
        ),
        # Bloque 3
        Destreza(
            description=(
                "Proponer y definir productos o servicios determinados por "
                "las necesidades de su entorno."
            ),
            codigo="EG.5.3.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y explicar los componentes del diseño de la "
                "investigación de campo para obtener información certera "
                "sobre el tema que se desee investigar o profundizar."
            ),
            codigo="EG.5.3.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Diseñar los instrumentos de investigación que se aplicarán "
                "para obtener información de campo que permita direccionar "
                "las ideas del emprendimiento."
            ),
            codigo="EG.5.3.3.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Ejecutar una investigación de campo entre los clientes "
                "potenciales/usuarios determinados, para establecer las "
                "necesidades de la zona geográfica, de tal manera que se "
                "determinen las ideas potenciales de emprendimiento."
            ),
            codigo="EG.5.3.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Describir los conocimientos estadísticos básicos para "
                "tabular los datos recabados en una investigación de campo."
            ),
            codigo="EG.5.3.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Presentar la información obtenida en una investigación de "
                "campo de forma resumida y concisa, en función de su "
                "utilidad para la toma de decisiones."
            ),
            codigo="EG.5.3.6.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Analizar estadísticamente la información de mercado (oferta "
                "y demanda) a partir de la representación gráfica de los "
                "datos procesados en tablas, gráficas, histogramas, cálculo "
                "de frecuencias, diagramas, estudios de medidas de tendencia "
                "central (media, mediana, moda)."
            ),
            codigo="EG.5.3.7.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        Destreza(
            description=(
                "Utilizar metodologías para interpretar datos estadísticos "
                "como fundamento para la toma de decisiones y la selección "
                "de las ideas de emprendimiento con mayor probabilidad de "
                "éxito."
            ),
            codigo="EG.5.3.8.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque3_emprendimiento
        ),
        # Bloque 4
        Destreza(
            description=(
                "Aplicar en un emprendimiento los elementos básicos de los "
                "principios de administración (planeación, organización, "
                "integración, dirección y control), para generar las "
                "habilidades directivas que el emprendedor requiere."
            ),
            codigo="EG.5.4.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Desarrollar criterios sobre administración para generar "
                "eficacia en los emprendimientos."
            ),
            codigo="EG.5.4.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar, valorar e implementar el concepto de "
                "“responsabilidad social” en el desarrollo de "
                "emprendimientos, como elemento fundamental para la "
                "generación de emprendimientos de carácter social."
            ),
            codigo="EG.5.4.3.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Analizar conceptos básicos de economía (“inflación”, "
                "“oferta”, “demanda”, “mercado”, “empleo”, etc.) con el fin "
                "de establecer su impacto en las decisiones relativas al "
                "emprendimiento."
            ),
            codigo="EG.5.4.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar principios básicos de microeconomía en el "
                "desarrollo de emprendimientos, como elemento para la toma "
                "de decisiones."
            ),
            codigo="EG.5.4.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        Destreza(
            description=(
                "Analizar y aplicar los conceptos de “ingresos y costos "
                "marginales” en un proyecto de emprendimiento (costos "
                "hundidos) y su impacto en la rentabilidad del mismo."
            ),
            codigo="EG.5.4.6.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque4_emprendimiento
        ),
        # Bloque 5
        Destreza(
            description=(
                "Determinar las necesidades de la zona geográfica y la forma "
                "en que el emprendimiento las satisfaría, como elemento "
                "fundamental para seleccionar una idea de negocio."
            ),
            codigo="EG.5.5.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Exponer, de forma sintética y sencilla, el bien o servicio "
                "seleccionado (idea de emprendimiento) y sus características "
                "principales, de tal manera que, en un lapso muy corto, se "
                "genere impacto entre quienes escuchan."
            ),
            codigo="EG.5.5.2.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Representar gráficamente la estructura organizacional y las "
                "principales funciones de las diferentes áreas del nuevo "
                "emprendimiento, para identificar los recursos humanos "
                "requeridos."
            ),
            codigo="EG.5.5.3.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Describir detalladamente el proceso operacional o "
                "productivo del nuevo emprendimiento con todos los "
                "componentes y recursos requeridos (humanos y materiales), "
                "para asegurar la fabricación de un producto o la generación "
                "de un servicio de alta calidad."
            ),
            codigo="EG.5.5.4.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Explicar detalladamente el proceso operacional o productivo "
                "del nuevo emprendimiento con todos los componentes y "
                "recursos requeridos (humanos y materiales), para asegurar "
                "la fabricación de un producto o la generación de un "
                "servicio de alta calidad."
            ),
            codigo="EG.5.5.4.1.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Determinar el monto de los bienes que el nuevo "
                "emprendimiento requiere, para establecer el valor de la "
                "inversión necesaria."
            ),
            codigo="EG.5.5.5.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Determinar el costo de producción de los bienes o el costo "
                "de los servicios como elemento fundamental para conocer los "
                "gastos que la operación requiere."
            ),
            codigo="EG.5.5.6.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Identificar los costos fijos y variables (directos e "
                "indirectos) en un ejercicio de bienes o servicios."
            ),
            codigo="EG.5.5.7.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y explicar de forma sencilla el segmento de "
                "mercado que se desea alcanzar y sus características, para "
                "establecer estrategias adecuadas para convertirlo en "
                "cliente/usuario."
            ),
            codigo="EG.5.5.8.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Establecer las variables de mercado (producto, precio, "
                "plaza, promoción y personalización) del nuevo "
                "emprendimiento, para satisfacer las necesidades del "
                "segmento de mercado seleccionado."
            ),
            codigo="EG.5.5.9.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Describir y explicar los mecanismos de comunicación "
                "(publicidad y promoción) que se implementará en el futuro "
                "emprendimiento, en función de la caracterización del "
                "segmento de mercado que se aspira alcanzar."
            ),
            codigo="EG.5.5.10.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar metodologías para elaborar una proyección de "
                "ingresos (incluyendo incrementos paulatinos y ciclicidad), "
                "considerando las unidades vendidas y los precios de venta, "
                "para establecer el monto de ingresos del nuevo "
                "emprendimiento."
            ),
            codigo="EG.5.5.11.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Utilizar metodologías para elaborar proyecciones de costos "
                "y gastos, que permitan establecer el monto necesario para "
                "cumplir con estas obligaciones de fondos futuros."
            ),
            codigo="EG.5.5.12.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Utilizar hojas electrónicas para realizar proyecciones "
                "utilizando las TIC de manera que se facilite su "
                "elaboración."
            ),
            codigo="EG.5.5.13.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Elaborar el plan de ingresos y egresos del futuro "
                "emprendimiento, que permita la evaluación cuantitativa del "
                "mismo."
            ),
            codigo="EG.5.5.14.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Calcular el margen de contribución del producto o servicio "
                "del emprendimiento."
            ),
            codigo="EG.5.5.15.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        Destreza(
            description=(
                "Calcular el punto de equilibrio de una empresa a partir de "
                "la identificación de costos unitarios."
            ),
            codigo="EG.5.5.16.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque5_emprendimiento
        ),
        # Bloque 6
        Destreza(
            description=(
                "Aplicar técnicas básicas para la evaluación financiera de "
                "un proyecto de emprendimiento (como análisis de "
                "rentabilidad, periodo de recuperación, tasa interna de "
                "retorno y valor actual neto) que permitan tomar decisiones "
                "sobre su implementación, tales como Análisis de "
                "Rentabilidad, Período de Recuperación, Tasa Interna de "
                "Retorno y Valor Actual Neto."
            ),
            codigo="EG.5.6.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque6_emprendimiento
        ),
        Destreza(
            description=(
                "Tomar decisiones sobre la implementación de un proyecto de "
                "emprendimiento basadas en las herramientas de análisis de "
                "rentabilidad, periodo de recuperación, tasa interna de "
                "retorno y valor actual neto."
            ),
            codigo="EG.5.6.1.1.",
            imprescindible=True,
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque6_emprendimiento
        ),
        Destreza(
            description=(
                "Aplicar metodologías para la evaluación cualitativa de un "
                "proyecto de emprendimiento (cobertura de necesidades y "
                "empleo generado) que permitan establecer su factibilidad, "
                "los riesgos existentes y medidas mitigantes propicias."
            ),
            codigo="EG.5.6.2.",
            asignatura=gestion,
            subnivel=bachillerato,
            bloque=bloque6_emprendimiento
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0047_auto_20180815_0902'),
    ]

    operations = [
        migrations.RunPython(
            create_destrezas, reverse_code=migrations.RunPython.noop)
    ]
