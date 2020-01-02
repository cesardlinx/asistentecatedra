import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .forms import ContactForm
from .models import Libro, Pregunta

User = get_user_model()

# Get an instance of a logger
logger = logging.getLogger(__name__)


class HomeTemplateView(TemplateView):
    """Vista principal de la aplicación"""
    template_name = 'asistente/home.html'


class BibliotecaListView(ListView):
    """Biblioteca"""
    model = Libro
    template_name = 'asistente/biblioteca.html'

    def get_context_data(self, **kwargs):
        return Libro.objects.get_libros_por_asignaturas()


class AyudaListView(ListView):
    """Ayuda"""
    template_name = 'asistente/ayuda.html'
    model = Pregunta
    context_object_name = 'preguntas'


class AboutTemplateView(TemplateView):
    """Vista para la seccion acerca de"""
    template_name = 'asistente/about.html'


class ContactView(FormView):
    """Contacto"""
    form_class = ContactForm
    template_name = 'asistente/contacto.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Email sending
        mail_subject = form.cleaned_data['subject']
        html_email_body = render_to_string(
            'asistente/emails/contact_email.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message']
            }
        )
        text_email_body = strip_tags(html_email_body)
        to_email = settings.SUPERUSER_EMAIL

        email = EmailMultiAlternatives(
            mail_subject, text_email_body, to=[to_email])
        email.attach_alternative(html_email_body, "text/html")
        email.send(fail_silently=True)

        messages.success(
            self.request, 'Tu mensaje ha sido enviado exitosamente.')
        logger.info('Message from {} sent'.format(
            form.cleaned_data['email']))

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Ha habido un error y tu mensaje no ha sido enviado.')
        logger.error('Error trying to send message from {}.'.format(
            form.data['email']))
        return super().form_invalid(form)


class CondicionesTemplateView(TemplateView):
    """Vista para los términos y condiciones"""
    template_name = 'asistente/condiciones.html'


class PrivacidadTemplateView(TemplateView):
    """Vista para el aviso de privacidad"""
    template_name = 'asistente/privacidad.html'


class CookiesTemplateView(TemplateView):
    """Vista para el aviso de manejo de cookies"""
    template_name = 'asistente/cookies.html'


def handler404(request, exception, template_name='asistente/errors/404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response


def handler500(request, template_name='asistente/errors/500.html'):
    response = render(request, template_name)
    response.status_code = 500
    return response
