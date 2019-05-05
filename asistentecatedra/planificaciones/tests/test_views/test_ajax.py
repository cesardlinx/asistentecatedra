import pytest
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from planificaciones import views
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.curso import Curso
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.indicador import Indicador
from planificaciones.models.destreza import Destreza
from planificaciones.models.unidad import Unidad
from planificaciones.models.subnivel import Subnivel
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from django.contrib.auth import get_user_model
User = get_user_model()

pytestmark = pytest.mark.django_db


class AjaxTestCase(TestCase):
    def setUp(self):
        """Creates data for testing Ajax views"""
        subnivel = mixer.blend(Subnivel)
        self.curso_1 = mixer.blend(Curso, subnivel=subnivel)
        self.curso_2 = mixer.blend(Curso, subnivel=subnivel)
        self.asignatura = mixer.blend(Asignatura)
        self.asignatura.cursos.add(self.curso_1, self.curso_2)
        unidad_1 = mixer.blend(Unidad, curso=self.curso_1,
                               asignatura=self.asignatura)
        unidad_2 = mixer.blend(Unidad, curso=self.curso_2,
                               asignatura=self.asignatura)
        self.objetivo_1 = mixer.blend(Objetivo, asignatura=self.asignatura)
        self.objetivo_2 = mixer.blend(Objetivo, asignatura=self.asignatura)
        self.objetivo_general = mixer.blend(ObjetivoGeneral,
                                            area=self.asignatura.area)
        unidad_1.objetivos.add(self.objetivo_1)
        unidad_2.objetivos.add(self.objetivo_2)
        unidad_1.objetivos_generales.add(self.objetivo_general)
        self.destreza = mixer.blend(Destreza, asignatura=self.asignatura,
                                    subnivel=subnivel)
        criterio = mixer.blend(CriterioEvaluacion, asignatura=self.asignatura,
                               subnivel=subnivel)
        criterio.destrezas.add(self.destreza)
        self.indicador_1 = mixer.blend(Indicador, criterio_evaluacion=criterio)
        self.indicador_2 = mixer.blend(Indicador, criterio_evaluacion=criterio)


class TestLoadCursosView(AjaxTestCase):

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = views.load_cursos(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.load_cursos(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(response, 'Not Allowed')

    def test_auth_user(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/',
                                       {'asignatura': self.asignatura.id},
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.user
        response = views.load_cursos(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, 'value="{}"'.format(self.curso_1.id))
        self.assertContains(
            response, 'value="{}"'.format(self.curso_2.id))


class TestLoadObjetivosView(AjaxTestCase):

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = views.load_objetivos(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.load_objetivos(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(response, '{\\"allowed\\": false}')

    def test_auth_user(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'cursos[]': [self.curso_1.id, self.curso_2.id]
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = views.load_objetivos(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, self.objetivo_1.codigo)
        self.assertContains(
            response, self.objetivo_2.codigo)
        self.assertContains(
            response, self.objetivo_general.codigo)


class TestLoadDestrezasView(AjaxTestCase):

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = views.load_destrezas(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.load_destrezas(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert str(response.content) == "b'<option>---------</option>'"

    def test_auth_user(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'cursos[]': [self.curso_1.id, self.curso_2.id]
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = views.load_destrezas(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, self.destreza.codigo)


class TestLoadIndicadoresView(AjaxTestCase):

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = views.load_indicadores(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.load_indicadores(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(response, 'Not Allowed')

    def test_auth_user(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get(
            '/',
            {
                'destreza': self.destreza.id,
                'numero_fila': 0
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = views.load_indicadores(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, self.indicador_1.codigo)
        self.assertContains(
            response, self.indicador_2.codigo)
