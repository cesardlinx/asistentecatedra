import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from asistente import views
from mixer.backend.django import mixer
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.curso import Curso
from accounts.tests.conftest import clean_test_files

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


class TestPremiumView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PremiumTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/premium.html' in \
            response.template_name, \
            'Premium template should be rendered in the view'
