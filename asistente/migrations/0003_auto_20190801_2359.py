from django.db import migrations


def create_questions(apps, schema_editor):
    """Función para crear las preguntas del FAQ"""
    Pregunta = apps.get_model('asistente', 'Pregunta')

    # Preguntas
    Pregunta.objects.bulk_create([
        Pregunta(
            question='¿Es gratis crear un usuario en Asistente de Cátedra?',
            answer=(
                "Cualquier persona puede crear un usuario en Asistente de "
                "Cátedra de manera completamente gratuita."
            )
        ),
        Pregunta(
            question='¿Qué planificaciones puedo realizar sin pagar?',
            answer=(
                "Asistente de Cátedra te permite la creación de planes de "
                "clase sin ningun costo a modo de ayuda ya que este tipo de "
                "planificación es la más requerida y usada."
            )
        ),
        Pregunta(
            question='¿Por qué habría de comparar una subscripción?',
            answer=(
                "Una subscripción te permite el uso completo de la aplicación "
                "para la realización de cualquier tipo de planificación."
            )
        ),
        Pregunta(
            question='¿Es necesario que confirme mi correo electrónico?',
            answer=(
                "No es necesario que confirmes tu cuenta para comenzar a "
                "usar la aplicación, sin embargo el confirmar tu cuenta te "
                "permite el poder agregar el nombre y "
                "logo de la institución en donde trabajar a tus "
                "planificaciones."
            )
        ),
        Pregunta(
            question='¿Como puedo confirmar mi correo electrónico?',
            answer=(
                "El momento de registrarte debió llegar un email a tu correo, "
                "haz click en el enlace provisto y tu correo será "
                "confirmado automáticamente. Si no recibiste el correo puedes "
                "ir al menú que aparece sobre tu nombre y dar sobre la opción "
                "Confirmar correo."
            )
        ),
        Pregunta(
            question='¿Dónde agrego el nombre y logo de mi institución?',
            answer=(
                "El momento que ya has confirmado tu correo, puedes ir a tu "
                "perfil y agregar allí tanto el nombre como el logo de la "
                "institución donde trabajas, la misma que será agregada "
                "a las planificaciones que realices de forma automática."
            )
        ),
        Pregunta(
            question=(
                '¿Puedo usar Asistente de Cátedra desde un dispositivo móvil?'
            ),
            answer=(
                "¡Por supuesto! puedes ingresar desde cualquier dispositvo "
                "ingresando desde tu navegador, ya que por el momento no "
                "disponemos de una aplicación móvil."
            )
        ),
        Pregunta(
            question='¿Dónde puedo obtener mayor información sobre la app?',
            answer=(
                "Puedes mantenerte informado y al mismo tiempo ser parte "
                "de nuestra comunidad tanto en nuestro gurpo de Facebook como "
                "en Twitter."
            )
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('asistente', '0002_auto_20181228_1911'),
    ]

    operations = [
        migrations.RunPython(
            create_questions, reverse_code=migrations.RunPython.noop)
    ]
