import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.api import get_messages
from django.core import mail
from django.test import RequestFactory, TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from accounts.tests.conftest import clean_test_files
from asistente import views
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.curso import Curso
from testfixtures import LogCapture

User = get_user_model()

pytestmark = pytest.mark.django_db


class TestHomeView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.HomeTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/home.html' in \
            response.template_name, \
            'Home template should be rendered in the view'


class TestBibliotecaView(TestCase):
    def setUp(self):
        """Response creation"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        self.response = views.BibliotecaListView.as_view()(request)

    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        assert self.response.status_code == 200, \
            'Should be callable by anonymous'
        assert 'asistente/biblioteca.html' in \
            self.response.template_name, \
            'Premium template should be rendered in the view'

    def test_get(self):
        curso = mixer.blend(Curso, name="2° EGB")
        asignatura = mixer.blend(Asignatura, name='Matemática')
        libro = mixer.blend('asistente.Libro', asignatura=asignatura,
                            curso=curso)
        self.assertContains(self.response, libro.curso)

    def tearDown(self):
        clean_test_files()


class TestAboutView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.AboutTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/about.html' in \
            response.template_name, \
            'About template should be rendered in the view'


class TestAyudaView(TestCase):
    def setUp(self):
        """Response Creation"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        self.response = views.AyudaListView.as_view()(request)

    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        assert self.response.status_code == 200, \
            'Should be callable by anonymous'
        assert 'asistente/ayuda.html' in \
            self.response.template_name, \
            'Ayuda template should be rendered in the view'

    def test_get(self):
        pregunta = mixer.blend('asistente.Pregunta')
        self.assertContains(self.response, pregunta.question)
        self.assertContains(self.response, pregunta.answer)


class TestContactView(TestCase):
    def setUp(self):
        self.logger = LogCapture()

    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.ContactView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/contacto.html' in \
            response.template_name, \
            'Contact template should be rendered in the view'

    def test_email_sent_when_valid_data(self):
        """Test app sends email"""
        response = self.client.post(reverse('contacto'), {
            'name': 'some user',
            'email': 'someuser@tester.com',
            'subject': 'Questions',
            'message': 'I have a lot of questions'
        }, follow=True)

        assert response.status_code == 200, 'Should be successful'
        self.assertRedirects(response, reverse('home'))

        assert len(mail.outbox) == 1, 'should send the email'
        email = mail.outbox[0]
        assert settings.SUPERUSER_EMAIL in email.to, 'my email should be here'
        assert 'someuser@tester.com' in email.body, \
               'the email from the person should be here'
        assert 'Questions' in email.subject, 'the subject must appear'
        assert 'I have a lot of questions' in email.body, \
               'the text must appear'

        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1, 'There should be one message'
        assert 'Tu mensaje ha sido enviado exitosamente.'\
               == messages[0].message, \
               'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'There should be a success message.'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Message from someuser@tester.com sent' in str(self.logger), \
            'Log from confirmation sending'

    def test_email_sent_when_invalid_data(self):
        """Test app wont send email"""
        response = self.client.post(reverse('contacto'), {
            'name': 'some user',
            'email': 'someuser',
            'subject': 'Questions',
            'message': 'I have a lot of questions'
        }, follow=True)

        assert response.status_code == 200, 'Should be successful'

        assert len(mail.outbox) == 0, 'should send the email'

        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1, 'There should be one message'
        assert 'Ha habido un error y tu mensaje no ha sido enviado.'\
               == messages[0].message, \
               'Should return a success message'
        assert messages[0].tags == 'alert-danger', \
            'There should be an error message.'

        assert 'ERROR' in str(self.logger), 'Should return an info log'
        assert 'Error trying to send message from someuser' in \
            str(self.logger), 'Log from error in sending'

    def tearDown(self):
        self.logger.uninstall()


class TestCondicionesView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.CondicionesTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/condiciones.html' in \
            response.template_name, \
            'Condiciones template should be rendered in the view'


class TestPrivacidadView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PrivacidadTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/privacidad.html' in \
            response.template_name, \
            'Privacidad template should be rendered in the view'


class TestCookiesView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.CookiesTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/cookies.html' in \
            response.template_name, \
            'Cookies template should be rendered in the view'


class TestErrorViews(TestCase):
    def test_404_handler(self):
        response = self.client.get('/something/')
        assert response.status_code == 404, 'Should return a 404 error'
        assert response.templates[0].name == 'asistente/errors/404.html', \
            'Should return the 404.html template'
