import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from planificaciones.forms import ElementoCurricularFormset, PlanClaseForm
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.curso import Curso
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.indicador import Indicador
from planificaciones.models.destreza import Destreza
from planificaciones.models.unidad import Unidad
from planificaciones.models.subnivel import Subnivel
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from django.core.exceptions import ValidationError
pytestmark = pytest.mark.django_db


class TestPlanClase(TestCase):
    def setUp(self):
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
        unidad_1.objetivos.add(self.objetivo_1)
        unidad_2.objetivos.add(self.objetivo_2)
        self.destreza = mixer.blend(Destreza, asignatura=self.asignatura,
                                    subnivel=subnivel)
        criterio = mixer.blend(CriterioEvaluacion, asignatura=self.asignatura,
                               subnivel=subnivel)
        criterio.destrezas.add(self.destreza)
        self.indicador_1 = mixer.blend(Indicador, criterio_evaluacion=criterio)
        self.indicador_2 = mixer.blend(Indicador, criterio_evaluacion=criterio)


class TestPlanClaseForm(TestPlanClase):

    def setUp(self):
        super().setUp()
        self.data = {
            'name': 'Plan de Clase1',
            'numero_plan': 2,
            'fecha': '2019-01-20',
            'asignatura': self.asignatura.id,
            'cursos': [str(self.curso_1.id), str(self.curso_2.id)],
            'paralelos': 'A y C',
            'numero_estudiantes': '23',
            'tema': 'Tema del plan',
            'periodos': 'Períodos del plan',
            'metodologia': 'Metodología del plan de clase',
            'tecnica': 'Tecnica usada',
            'objetivos': [str(self.objetivo_1.id), str(self.objetivo_2.id)],
            'bibliografia': 'Lorem ipsum dolor sit amet.',
            'contenido_cientifico': 'Lorem ipsum dolor sit amet.',
            'material_didactico': 'Lorem ipsum dolor sit amet.',
            'instrumento_evaluacion': 'Lorem ipsum dolor sit amet.',
            'instrumento_evaluacion': 'Lorem ipsum dolor sit amet.',
        }

    def test_valid_data(self):
        form = PlanClaseForm(self.data)
        assert form.is_valid() is True, 'The form should be valid'

    def test_empty_data(self):
        form = PlanClaseForm({})
        assert form.is_valid() is False, 'The form should be invalid'

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        form = PlanClaseForm(data)
        assert form.is_valid() is False, 'The form should be invalid'


class TestElementoCurricularFormset(TestPlanClase):

    def setUp(self):
        super().setUp()
        self.data = {
            'asignatura': self.asignatura.id,
            'cursos': [self.curso_1.id, self.curso_2.id],
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
            'MAX_NUM_FORMS': '10',
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
            'MAX_NUM_FORMS': '10',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'name': 'lorem',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'description': 'lorem ipsum',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'tiempo': 'lorem ipsum',
            'proceso-elementos_curriculares-1-procesos_didacticos-0-'\
            'recursos': 'lorem ipsum',
        }

    def test_valid_data(self):
        formset = ElementoCurricularFormset(self.data)
        assert formset.is_valid() is True, 'The formset should be valid'

    def test_empty_data(self):
        with pytest.raises(ValidationError,
                           match='Los datos de ManagementForm faltan o han '
                                 'sido manipulados'):
            formset = ElementoCurricularFormset({})
            formset.is_valid()

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        data['elementos_curriculares-0-destreza'] = 'lorem ipsum'
        formset = ElementoCurricularFormset(data)
        assert formset.is_valid() is False, 'The formset should be invalid'
