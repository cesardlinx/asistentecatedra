import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer

from accounts.tests.conftest import clean_test_files
from asistente import views
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.curso import Curso

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

    def test_premium_user_cant_access(self):
        """Tests that a premium user can't access"""
        user = mixer.blend(User, is_premium=True)
        request = RequestFactory().get('/')
        request.user = user
        response = views.PremiumTemplateView.as_view()(request)
        assert response.status_code == 302, 'User should be redirected'
        assert '/' == response.url, 'Should not be callable by premium user'


class TestChangePlanView:
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.ChangePlanListView.as_view()(request)
        assert response.status_code == 302, 'User should be redirected'
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_premium_user_access(self):
        """Tests that a not premium user can't access"""
        user = mixer.blend(User)
        request = RequestFactory().get('/')
        request.user = user
        response = views.ChangePlanListView.as_view()(request)
        assert response.status_code == 302, 'User should be redirected'
        assert 'premium' in response.url, \
            'Should not be callable by a not premium user'

    def test_perpetual_user_cant_access(self):
        """
        Tests that an authenticated premium user cant access the view
        if has a perpetual plan
        """
        plan = mixer.blend('accounts.Plan', plan_type='PAGO ÚNICO')
        user = mixer.blend(User, is_premium=True)

        mixer.blend(
            'accounts.Subscription',
            plan=plan,
            user=user,
            stripe_subscription_id='456789',
            active=True
        )

        request = RequestFactory().get('/')
        request.user = user
        response = views.ChangePlanListView.as_view()(request)
        assert response.status_code == 302, 'User should be redirected'
        assert '/' == response.url, \
            'Should not be callable by a not perpetual premium user'

    def test_premium_user_access(self):
        """Tests that an authenticated premium user can access the view"""
        user = mixer.blend(User, is_premium=True)
        request = RequestFactory().get('/')
        request.user = user
        response = views.ChangePlanListView.as_view()(request)
        assert response.status_code == 200, 'User should access the view'
        assert 'asistente/change_plan.html' in \
            response.template_name, \
            'Change Plan template should be rendered in the view'

