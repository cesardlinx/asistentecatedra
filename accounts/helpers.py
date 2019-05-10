import uuid
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from .tokens import account_token_generator


def send_confirmation_helper(user, domain):
    """Función para enviar correo de confirmación de email"""
    protocol = settings.PROTOCOL
    mail_subject = 'Asistente de Cátedra | '\
                   'Confirmar Correo Electrónico'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_token_generator.make_token(user)
    html_email_body = render_to_string('accounts/confirm_email.html', {
        'user': user,
        'protocol': protocol,
        'domain': domain,
        'uid': uid,
        'token': token,
    })
    text_email_body = strip_tags(html_email_body)
    to_email = user.email

    email = EmailMultiAlternatives(
        mail_subject, text_email_body, to=[to_email])
    email.attach_alternative(html_email_body, "text/html")
    email.send()


def get_photo_path(instance, filename):
    """Returns the path for the user's photo"""
    ext = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid.uuid4(), ext)
    location = 'users/user_{0}/photo/'.format(instance.pk)
    return os.path.join(location, filename)


def get_logo_path(instance, filename):
    """Returns the path for the user's institution logo"""
    ext = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid.uuid4(), ext)
    location = 'users/user_{0}/logo/'.format(instance.pk)
    return os.path.join(location, filename)
