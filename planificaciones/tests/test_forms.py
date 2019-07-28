import pytest
from planificaciones.forms.elemento_curricular_formset import \
    ElementoCurricularFormset
from planificaciones.forms.desarrollo_unidad_formset import \
    DesarrolloUnidadFormset
from planificaciones.forms.actividad_aprendizaje_formset import \
    ActividadAprendizajeFormset
from planificaciones.forms.plan_destrezas_form import PlanDestrezasForm
from planificaciones.forms.plan_anual_form import PlanAnualForm
from planificaciones.forms.plan_unidad_form import PlanUnidadForm
from planificaciones.forms.plan_clase_form import PlanClaseForm
from .planificaciones_testcase import PlanificacionesTestCase

from django.core.exceptions import ValidationError
pytestmark = pytest.mark.django_db


class TestPlanClaseForm(PlanificacionesTestCase):

    def setUp(self):
        super().setUp()
        self.data = {
            'name': 'Plan de Clase1',
            'docentes': 'David',
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


class TestElementoCurricularFormset(PlanificacionesTestCase):

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
            'elementos_curriculares-0-destreza': self.destreza_1.id,
            'elementos_curriculares-0-conocimientos_asociados': 'lorem ipsum',
            'elementos_curriculares-0-actividades_evaluacion': 'lorem ipsum',
            'elementos_curriculares-1-destreza': self.destreza_1.id,
            'elementos_curriculares-1-conocimientos_asociados': 'lorem ipsum',
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


class TestPlanAnualForm(PlanificacionesTestCase):

    def setUp(self):
        super().setUp()
        self.data = {
            'name': 'Plan de Anual1',
            'ano_lectivo': '2019-2020',
            'docentes': 'David Padilla, Tatiana Carpio',
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            'paralelos': 'A y C',
            'carga_horaria': 20,
            'semanas_trabajo': 10,
            'semanas_imprevistos': 2,
            'objetivos_generales': [str(self.general_1.id),
                                    str(self.general_2.id)],
            'objetivos_curso': [str(self.objetivo_1.id),
                                str(self.objetivo_2.id)],
            'objetivos_generales_curso': [str(self.general_1.id),
                                          str(self.general_2.id)],
            'ejes_transversales': 'Lorem ipsum dolor sit amet.',
            'bibliografia': 'Lorem ipsum dolor sit amet.',
            'observaciones': 'Tecnica usada',
        }

    def test_valid_data(self):
        form = PlanAnualForm(self.data)
        assert form.is_valid() is True, 'The form should be valid'

    def test_empty_data(self):
        form = PlanAnualForm({})
        assert form.is_valid() is False, 'The form should be invalid'

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        form = PlanAnualForm(data)
        assert form.is_valid() is False, 'The form should be invalid'


class TestDesarrolloUnidadFormset(PlanificacionesTestCase):

    def setUp(self):
        super().setUp()
        self.data = {
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            # Formset Desarrollo Unidad 1
            'desarrollo_unidades-TOTAL_FORMS': '2',
            'desarrollo_unidades-INITIAL_FORMS': '0',
            'desarrollo_unidades-MIN_NUM_FORMS': '0',
            'desarrollo_unidades-MAX_NUM_FORMS': '1000',
            'desarrollo_unidades-0-unidad': self.unidad_1.id,
            'desarrollo_unidades-0-objetivos': [self.objetivo_1.id,
                                                self.objetivo_2.id],
            'desarrollo_unidades-0-objetivos_generales': [self.general_1.id,
                                                          self.general_2.id],
            'desarrollo_unidades-0-destrezas': [self.destreza_1.id,
                                                self.destreza_2.id],
            'desarrollo_unidades-0-orientaciones_metodologicas': 'lorem ipsum',
            'desarrollo_unidades-0-semanas': 7,

            # Formset Desarrollo Unidad 2
            'desarrollo_unidades-1-unidad': self.unidad_1.id,
            'desarrollo_unidades-1-objetivos': [self.objetivo_1.id,
                                                self.objetivo_2.id],
            'desarrollo_unidades-1-objetivos_generales': [self.general_1.id,
                                                          self.general_2.id],
            'desarrollo_unidades-1-destrezas': [self.destreza_1.id,
                                                self.destreza_2.id],
            'desarrollo_unidades-1-orientaciones_metodologicas': 'lorem ipsum',
            'desarrollo_unidades-1-semanas': 8,
        }

    def test_valid_data(self):
        formset = DesarrolloUnidadFormset(self.data)
        assert formset.is_valid() is True, 'The formset should be valid'

    def test_empty_data(self):
        with pytest.raises(ValidationError,
                           match='Los datos de ManagementForm faltan o han '
                                 'sido manipulados'):
            formset = DesarrolloUnidadFormset({})
            formset.is_valid()

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        data['desarrollo_unidades-0-unidad'] = 'lorem ipsum'
        formset = DesarrolloUnidadFormset(data)
        assert formset.is_valid() is False, 'The formset should be invalid'


class TestPlanUnidadForm(PlanificacionesTestCase):

    def setUp(self):
        super().setUp()
        self.data = {
            'name': 'Plan de Unidad1',
            'ano_lectivo': '2019-2020',
            'docentes': 'David Padilla, Tatiana Carpio',
            'unidad': self.unidad_1.id,
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            'paralelos': 'A y C',
            'periodos': 20,
            'tiempo': 20,
            'objetivos': [str(self.objetivo_1.id),
                          str(self.objetivo_2.id)],
            'objetivos_generales': [str(self.general_1.id),
                                    str(self.general_2.id)],
            'necesidad_adaptacion': 'Lorem ipsum dolor sit amet.',
            'adaptacion-curricular': 'Lorem ipsum dolor sit amet.',
        }

    def test_valid_data(self):
        form = PlanUnidadForm(self.data)
        assert form.is_valid() is True, 'The form should be valid'

    def test_empty_data(self):
        form = PlanUnidadForm({})
        assert form.is_valid() is False, 'The form should be invalid'

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        form = PlanUnidadForm(data)
        assert form.is_valid() is False, 'The form should be invalid'


class TestActividadesAprendizajeFormset(PlanificacionesTestCase):

    def setUp(self):
        super().setUp()
        self.data = {
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            # Formset Actividades Aprendizaje 1
            'actividades_aprendizaje-TOTAL_FORMS': '2',
            'actividades_aprendizaje-INITIAL_FORMS': '0',
            'actividades_aprendizaje-MIN_NUM_FORMS': '0',
            'actividades_aprendizaje-MAX_NUM_FORMS': '1000',
            'actividades_aprendizaje-0-destrezas': [self.destreza_1.id,
                                                    self.destreza_2.id],
            'actividades_aprendizaje-0-estrategias_metodologicas': 'lorem ips',
            'actividades_aprendizaje-0-recursos': 'lorem ipsum',
            'actividades_aprendizaje-0-instrumentos_evaluacion': 'lorem ipsum',
            # Formset Actividades Aprendizaje 2
            'actividades_aprendizaje-1-destrezas': [
                self.destreza_1.id,
                self.destreza_2.id
            ],
            'actividades_aprendizaje-1-estrategias_metodologicas': 'lorem ips',
            'actividades_aprendizaje-1-recursos': 'lorem ipsum',
            'actividades_aprendizaje-1-instrumentos_evaluacion': 'lorem ipsum',
        }

    def test_valid_data(self):
        formset = ActividadAprendizajeFormset(self.data)
        assert formset.is_valid() is True, 'The formset should be valid'

    def test_empty_data(self):
        with pytest.raises(ValidationError,
                           match='Los datos de ManagementForm faltan o han '
                                 'sido manipulados'):
            formset = ActividadAprendizajeFormset({})
            formset.is_valid()

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        data['actividades_aprendizaje-0-destrezas'] = 'lorem ipsum'
        formset = ActividadAprendizajeFormset(data)
        assert formset.is_valid() is False, 'The formset should be invalid'


class TestPlanDestrezasForm(PlanificacionesTestCase):

    def setUp(self):
        super().setUp()
        self.data = {
            'name': 'Plan de Unidad1',
            'ano_lectivo': '2019-2020',
            'docentes': 'David Padilla, Tatiana Carpio',
            'unidad': self.unidad_1.id,
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            'paralelos': 'A y C',
            'periodos': 20,
            'semana_inicio': 'lorem ipsum dolor sit amet.',
            'ejes_transversales': 'lorem ipsum dolor sit amet.',
            'objetivos': [str(self.objetivo_1.id),
                          str(self.objetivo_2.id)],
            'objetivos_generales': [str(self.general_1.id),
                                    str(self.general_2.id)],
            'destrezas': [str(self.destreza_1.id),
                          str(self.destreza_2.id)],
            'estrategias_metodologicas': 'lorem ipsum',
            'recursos': 'lorem ipsum',
            'actividades_evaluacion': 'lorem ipsum',
            'necesidad_adaptacion': 'Lorem ipsum dolor sit amet.',
            'adaptacion-curricular': 'Lorem ipsum dolor sit amet.',
        }

    def test_valid_data(self):
        form = PlanDestrezasForm(self.data)
        assert form.is_valid() is True, 'The form should be valid'

    def test_empty_data(self):
        form = PlanDestrezasForm({})
        assert form.is_valid() is False, 'The form should be invalid'

    def test_invalid_data(self):
        data = self.data
        data['asignatura'] = 'lorem ipsum'
        form = PlanDestrezasForm(data)
        assert form.is_valid() is False, 'The form should be invalid'
