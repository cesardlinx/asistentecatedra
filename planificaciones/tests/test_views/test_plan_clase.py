import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError
from django.http.response import Http404
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer
from testfixtures import LogCapture

from planificaciones import views
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.curso import Curso
from planificaciones.models.destreza import Destreza
from planificaciones.models.elemento_curricular import ElementoCurricular
from planificaciones.models.indicador import Indicador
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.proceso_didactico import ProcesoDidactico
from planificaciones.models.subnivel import Subnivel
from planificaciones.models.unidad import Unidad
from accounts.tests.conftest import add_middleware_to_request

User = get_user_model()
pytestmark = pytest.mark.django_db


class PlanClaseTestCase(TestCase):
    def setUp(self):
        """Creates data for testing Planes de Clase"""

        self.logger = LogCapture()

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

        self.data = {
            'name': 'Plan de Clase1',
            'numero_plan': 2,
            'fecha': '2019-01-20',
            'asignatura': self.asignatura.id,
            'cursos': [self.curso_1.id, self.curso_2.id],
            'paralelos': 'A y C',
            'numero_estudiantes': '23',
            'tema': 'Tema del plan',
            'periodos': 'Períodos del plan',
            'metodologia': 'Metodología del plan de clase',
            'tecnica': 'Tecnica usada',
            'objetivos': [self.objetivo_1.id, self.objetivo_2.id],
            'bibliografia': 'Lorem ipsum dolor sit amet.',
            'contenido_cientifico': 'Lorem ipsum dolor sit amet.',
            'material_didactico': 'Lorem ipsum dolor sit amet.',
            'instrumento_evaluacion': 'Lorem ipsum dolor sit amet.',
            'instrumento_evaluacion': 'Lorem ipsum dolor sit amet.',
            # Formset Elementos curriculares 1
            'elementos_curriculares-TOTAL_FORMS': '2',
            'elementos_curriculares-INITIAL_FORMS': '0',
            'elementos_curriculares-MIN_NUM_FORMS': '0',
            'elementos_curriculares-MAX_NUM_FORMS': '1000',
            'elementos_curriculares-0-destreza': self.destreza.id,
            'elementos_curriculares-0-conocimientos_asociados': 'lorem ipsum',
            'elementos_curriculares-0-indicadores_logro': [
                self.indicador_1.id, self.indicador_2.id],
            'elementos_curriculares-0-actividades_evaluacion': 'lorem ipsum',
            'elementos_curriculares-1-destreza': self.destreza.id,
            'elementos_curriculares-1-conocimientos_asociados': 'lorem ipsum',
            'elementos_curriculares-1-indicadores_logro': [
                self.indicador_1.id, self.indicador_2.id],
            'elementos_curriculares-1-actividades_evaluacion': 'lorem ipsum',

            # Formset Procesos didacticos
            'proceso-elementos_curriculares-0-procesos_didacticos-'\
            'TOTAL_FORMS': '2',
            'proceso-elementos_curriculares-0-procesos_didacticos-'\
            'INITIAL_FORMS': '0',
            'proceso-elementos_curriculares-0-procesos_didacticos-'\
            'MIN_NUM_FORMS': '0',
            'proceso-elementos_curriculares-0-procesos_didacticos-'\
            'MAX_NUM_FORMS': '1000',
            'proceso-elementos_curriculares-0-procesos_didacticos-0-'\
            'name': 'lorem',
            'proceso-elementos_curriculares-0-procesos_didacticos-0-'\
            'description': 'lorem ipsum',
            'proceso-elementos_curriculares-0-procesos_didacticos-0-'\
            'tiempo': 'lorem ipsum',
            'proceso-elementos_curriculares-0-procesos_didacticos-0-'\
            'recursos': 'lorem ipsum',

            'proceso-elementos_curriculares-0-procesos_didacticos-1-'\
            'name': 'lorem',
            'proceso-elementos_curriculares-0-procesos_didacticos-1-'\
            'description': 'lorem ipsum',
            'proceso-elementos_curriculares-0-procesos_didacticos-1-'\
            'tiempo': 'lorem ipsum',
            'proceso-elementos_curriculares-0-procesos_didacticos-1-'\
            'recursos': 'lorem ipsum',

            'proceso-elementos_curriculares-1-procesos_didacticos-'\
            'TOTAL_FORMS': '1',
            'proceso-elementos_curriculares-1-procesos_didacticos-'\
            'INITIAL_FORMS': '0',
            'proceso-elementos_curriculares-1-procesos_didacticos-'\
            'MIN_NUM_FORMS': '0',
            'proceso-elementos_curriculares-1-procesos_didacticos-'\
            'MAX_NUM_FORMS': '1000',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'name': 'lorem',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'description': 'lorem ipsum',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'tiempo': 'lorem ipsum',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'recursos': 'lorem ipsum',
        }

    def tearDown(self):
        self.logger.uninstall()


class TestPlanClaseListView(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PlanClaseListView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanClaseListView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert 'planificaciones/planificacion_list.html' in \
            response.template_name, \
            'Template should be the one for listing planning'


class TestPlanClaseCreateView(PlanClaseTestCase):
    """Prueba la vista para la creación de planes de clase"""

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.plan_clase_create(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.plan_clase_create(request)
        assert response.status_code == 200, 'Authenticated user can access'
        # Tempĺate Testing
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="numero_plan"')
        self.assertContains(response, 'name="fecha"')
        self.assertContains(response, 'name="asignatura"')
        self.assertContains(response, 'id="id_cursos"')
        self.assertContains(response, 'name="paralelos"')
        self.assertContains(response, 'name="numero_estudiantes"')
        self.assertContains(response, 'name="tema"')
        self.assertContains(response, 'name="periodos"')
        self.assertContains(response, 'name="metodologia"')
        self.assertContains(response, 'name="tecnica"')
        self.assertContains(response, 'id="id_objetivos"')
        self.assertContains(response, 'id="id_objetivos_generales"')
        self.assertContains(response, 'name="bibliografia"')
        self.assertContains(response, 'name="contenido_cientifico"')
        self.assertContains(response, 'name="material_didactico"')
        self.assertContains(response, 'name="instrumento_evaluacion"')
        self.assertContains(response, 'name="observaciones"')
        self.assertContains(response, 'name="aprobado_por"')

    def test_post_success(self):
        """Prueba la creación de planes de clase"""
        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        response = views.plan_clase_create(request)
        assert response.status_code == 302, 'Should redirect to success view'
        plan = PlanClase.objects.last()
        elemento = ElementoCurricular.objects.last()
        proceso = ProcesoDidactico.objects.last()
        assert plan.name == 'Plan de Clase1', 'Should create a Plan de Clase'
        assert proceso.elemento_curricular == elemento, \
            'El proceso debe pertencer al elemento curricular'
        assert elemento.plan_clase == plan, \
            'el elemento curricular debe pertenecer al plan de clase'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan de clase created for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan de Clase is created.'

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""
        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.plan_clase_create(request)

        assert response.status_code == 200, 'Should get a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises ValidationError
        with pytest.raises(ValidationError):
            views.plan_clase_create(request)


class TestPlanClaseUpdateView(PlanClaseTestCase):

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)
        self.plan_clase = mixer.blend(PlanClase)

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.plan_clase_update(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        elemento = mixer.blend(ElementoCurricular, plan_clase=self.plan_clase)
        mixer.blend(ProcesoDidactico, elemento_curricular=elemento)
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.plan_clase_update(
            request, pk=self.plan_clase.pk, slug=self.plan_clase.slug)
        assert response.status_code == 200, 'Authenticated user can access'
        # Tempĺate Testing
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="numero_plan"')
        self.assertContains(response, 'name="fecha"')
        self.assertContains(response, 'name="asignatura"')
        self.assertContains(response, 'id="id_cursos"')
        self.assertContains(response, 'name="paralelos"')
        self.assertContains(response, 'name="numero_estudiantes"')
        self.assertContains(response, 'name="tema"')
        self.assertContains(response, 'name="periodos"')
        self.assertContains(response, 'name="metodologia"')
        self.assertContains(response, 'name="tecnica"')
        self.assertContains(response, 'id="id_objetivos"')
        self.assertContains(response, 'id="id_objetivos_generales"')
        self.assertContains(response, 'name="bibliografia"')
        self.assertContains(response, 'name="contenido_cientifico"')
        self.assertContains(response, 'name="material_didactico"')
        self.assertContains(response, 'name="instrumento_evaluacion"')
        self.assertContains(response, 'name="observaciones"')
        self.assertContains(response, 'name="aprobado_por"')

    def test_post_success(self):
        """Prueba la actualización de planes de clase"""
        assert self.plan_clase.name != 'Plan de Clase1', \
            'El plan inicialmente tiene un nombre diferente'
        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        response = views.plan_clase_update(
            request, pk=self.plan_clase.pk, slug=self.plan_clase.slug)
        assert response.status_code == 302, 'Should redirect to success view'
        self.plan_clase.refresh_from_db()
        assert self.plan_clase.name == 'Plan de Clase1', \
            'Debe actualizar el plan de clase'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan de clase updated for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan de Clase is updated.'

    def test_invalid_plan(self):
        """Tests the view when sending invalid data about a plan"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises 404 Error
        with pytest.raises(Http404):
            views.plan_clase_update(request, pk=1, slug='test')

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""

        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.plan_clase_update(
            request, pk=self.plan_clase.pk, slug=self.plan_clase.slug)

        assert response.status_code == 200, 'Should get a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        plan = mixer.blend(PlanClase)
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises ValidationError
        with pytest.raises(ValidationError):
            views.plan_clase_update(request, pk=plan.pk, slug=plan.slug)
