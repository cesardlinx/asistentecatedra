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
from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.elemento_curricular import ElementoCurricular
from planificaciones.models.proceso_didactico import ProcesoDidactico
from django.core.exceptions import ValidationError
from django.http.response import Http404
pytestmark = pytest.mark.django_db


class PlanClaseTestCase(TestCase):
    def setUp(self):
        """Creates data for testing Planes de Clase"""
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


class PlanClaseTestCaseCreateView(PlanClaseTestCase):
    """Prueba la vista para la creación de planes de clase"""

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend('auth.User')

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

    def test_post(self):
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

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises ValidationError
        with pytest.raises(ValidationError):
            views.plan_clase_create(request)


class PlanClaseTestCaseUpdateView(PlanClaseTestCase):

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend('auth.User')

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.plan_clase_update(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        plan = mixer.blend(PlanClase)
        elemento = mixer.blend(ElementoCurricular, plan_clase=plan)
        mixer.blend(ProcesoDidactico, elemento_curricular=elemento)
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.plan_clase_update(request, pk=plan.pk, slug=plan.slug)
        assert response.status_code == 200, 'Authenticated user can access'

    def test_post(self):
        """Prueba la actualización de planes de clase"""
        plan = mixer.blend(PlanClase)
        assert plan.name != 'Plan de Clase1', \
            'El plan inicialmente tiene un nombre diferente'
        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        resp = views.plan_clase_update(request, pk=plan.pk, slug=plan.slug)
        assert resp.status_code == 302, 'Should redirect to success view'
        plan.refresh_from_db()
        assert plan.name == 'Plan de Clase1', \
            'Debe actualizar el plan de clase'

    def test_invalid_plan(self):
        """Tests the view when sending invalid data about a plan"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises 404 Error
        with pytest.raises(Http404):
            views.plan_clase_update(request, pk=1, slug='test')

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""
        plan = mixer.blend(PlanClase)
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises ValidationError
        with pytest.raises(ValidationError):
            views.plan_clase_update(request, pk=plan.pk, slug=plan.slug)
