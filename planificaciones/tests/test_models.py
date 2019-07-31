import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import Truncator
from mixer.backend.django import mixer

from planificaciones.models.actividad_aprendizaje import ActividadAprendizaje
from planificaciones.models.area import Area
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.bloque_curricular import BloqueCurricular
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.curso import Curso
from planificaciones.models.desarrollo_unidad import DesarrolloUnidad
from planificaciones.models.destreza import Destreza
from planificaciones.models.elemento_curricular import ElementoCurricular
from planificaciones.models.indicador import Indicador
from planificaciones.models.nivel import Nivel
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.plan_anual import PlanAnual
from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.plan_destrezas import PlanDestrezas
from planificaciones.models.plan_unidad import PlanUnidad
from planificaciones.models.planificacion import Planificacion
from planificaciones.models.proceso_didactico import ProcesoDidactico
from planificaciones.models.subnivel import Subnivel
from planificaciones.models.unidad import Unidad

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestArea:
    def test_model(self):
        area = mixer.blend(Area)
        assert isinstance(area, Area), 'Should be an instance of Area'
        assert str(area) == area.name, \
            'The string representation should be the name'
        assert area._meta.db_table == 'areas', \
            'The table should be named "areas"'
        assert area._meta.verbose_name_plural == 'áreas', \
            'The plural name should be "áreas"'


class TestAsignatura:
    def test_model(self):
        asignatura = mixer.blend(Asignatura)
        assert isinstance(asignatura, Asignatura), \
            'Should be an instance of Asignatura'
        assert isinstance(asignatura.area, Area), \
            'The field area should be an instance of Area'
        assert str(asignatura) == asignatura.name, \
            'The string representation should be the name'
        assert asignatura._meta.db_table == 'asignaturas', \
            'The table should be named "asignaturas"'
        assert asignatura._meta.verbose_name_plural == 'asignaturas', \
            'The plural name should be "asignaturas"'


class TestBloqueCurricular:
    def test_model(self):
        bloque = mixer.blend(BloqueCurricular)
        assert isinstance(bloque, BloqueCurricular), \
            'Should be an instance of BloqueCurricular'
        assert isinstance(bloque.asignatura, Asignatura), \
            'The field asignatura should be an instance of Asignatura'
        assert str(bloque) == bloque.name, \
            'The string representation should be the name'
        assert bloque._meta.db_table == 'bloques_curriculares', \
            'The table should be named "bloques_curriculares"'
        assert bloque._meta.verbose_name_plural == 'bloques curriculares', \
            'The plural name should be "bloques curriculares"'


class TestNivel:
    def test_model(self):
        nivel = mixer.blend(Nivel)
        assert isinstance(nivel, Nivel), \
            'Should be an instance of Nivel'
        assert str(nivel) == nivel.name, \
            'The string representation should be the name'
        assert nivel._meta.db_table == 'niveles', \
            'The table should be named "niveles"'
        assert nivel._meta.verbose_name_plural == 'niveles', \
            'The plural name should be "niveles"'


class TestSubnivel:
    def test_model(self):
        subnivel = mixer.blend(Subnivel)
        assert isinstance(subnivel, Subnivel), \
            'Should be an instance of Subnivel'
        assert isinstance(subnivel.nivel, Nivel), \
            'The field nivel should be an instance of Nivel'
        assert str(subnivel) == subnivel.name, \
            'The string representation should be the name'
        assert subnivel._meta.db_table == 'subniveles', \
            'The table should be named "subniveles"'
        assert subnivel._meta.verbose_name_plural == 'subniveles', \
            'The plural name should be "subniveles"'


class TestCurso:
    def test_model(self):
        curso = mixer.blend(Curso)
        assert isinstance(curso, Curso), \
            'Should be an instance of Curso'
        assert isinstance(curso.subnivel, Subnivel), \
            'The field subnivel should be an instance of Subnivel'
        assert str(curso) == curso.name, \
            'The string representation should be the name'
        assert curso._meta.db_table == 'cursos', \
            'The table should be named "cursos"'
        assert curso._meta.verbose_name_plural == 'cursos', \
            'The plural name should be "cursos"'


class TestObjetivoGeneral:
    def test_model(self):
        objetivo = mixer.blend(ObjetivoGeneral)
        assert isinstance(objetivo, ObjetivoGeneral), \
            'Should be an instance of ObjetivoGeneral'
        assert isinstance(objetivo.area, Area), \
            'The field area should be an instance of Area'
        assert str(objetivo) == "{} - {}".format(
            objetivo.codigo,
            objetivo.description
        ), 'The string representation should be codigo plus descripcion'
        assert objetivo._meta.db_table == 'objetivos_generales', \
            'The table should be named "objetivos_generales"'
        assert objetivo._meta.verbose_name_plural == 'objetivos generales', \
            'The plural name should be "objetivos generales"'

    def test_get_objetivos_generales_by_asignatura_cursos(self):
        unidad = mixer.blend(Unidad)
        objetivo = mixer.blend(ObjetivoGeneral, area=unidad.asignatura.area)
        unidad.objetivos_generales.add(objetivo)
        objetivos = ObjetivoGeneral\
            .objects.get_objetivos_generales_by_asignatura_cursos(
                unidad.asignatura.id, [unidad.curso.id, ])
        assert objetivo in objetivos, \
            'Should get objetivos generales by asignatura and cursos'


class TestObjetivo:
    def test_model(self):
        objetivo = mixer.blend(Objetivo)
        assert isinstance(objetivo, Objetivo), \
            'Should be an instance of Objetivo'
        assert isinstance(objetivo.subnivel, Subnivel), \
            'The field subnivel should be an instance of Subnivel'
        assert isinstance(objetivo.asignatura, Asignatura), \
            'The field asignatura should be an instance of Asignatura'
        assert str(objetivo) == "{} - {}".format(
            objetivo.codigo,
            objetivo.description
        ), 'The string representation should be codigo and description'
        assert objetivo._meta.db_table == 'objetivos', \
            'The table should be named "objetivos"'
        assert objetivo._meta.verbose_name_plural == 'objetivos', \
            'The plural name should be "objetivos"'

    def test_get_objetivos_by_asignatura_cursos(self):
        objetivo = mixer.blend(Objetivo)
        unidad = mixer.blend(Unidad, asignatura=objetivo.asignatura)
        unidad.objetivos.add(objetivo)
        objetivos = Objetivo.objects.get_objetivos_by_asignatura_cursos(
            unidad.asignatura.id, [unidad.curso.id, ])
        assert objetivo in objetivos, \
            'Should get objetivos by asignatura and cursos'


class TestUnidad:
    def test_model(self):
        unidad = mixer.blend(Unidad)
        assert isinstance(unidad, Unidad), \
            'Should be an instance of Unidad'
        assert isinstance(unidad.curso, Curso), \
            'The field curso should be an instance of Curso'
        assert isinstance(unidad.asignatura, Asignatura), \
            'The field asignatura should be an instance of Asignatura'
        truncated_titulo = Truncator(unidad.titulo)
        assert str(unidad) == '{} - {}'.format(
            unidad.numero_unidad,
            truncated_titulo.chars(30),
        ), 'The representation should be numero de unidad y el título'
        assert unidad._meta.db_table == 'unidades', \
            'The table should be named "unidades"'
        assert unidad._meta.verbose_name_plural == 'unidades', \
            'The plural name should be "unidades"'

    def test_get_unidades_by_asignatura_curso(self):
        curso = mixer.blend(Curso)
        asignatura = mixer.blend(Asignatura)
        unidad = mixer.blend(Unidad, curso=curso, asignatura=asignatura)

        unidades = Unidad.objects.get_unidades_by_asignatura_curso(
            asignatura.id, curso.id)
        assert unidad in unidades, \
            'Should get unidades by asignatura and cursos'


class TestDestreza:
    def test_model(self):
        bloque = mixer.blend(BloqueCurricular)
        destreza = mixer.blend(Destreza, bloque=bloque)
        assert isinstance(destreza, Destreza), \
            'Should be an instance of Destreza'
        assert isinstance(destreza.asignatura, Asignatura), \
            'The field asignatura should be an instance of Asignatura'
        assert isinstance(destreza.subnivel, Subnivel), \
            'The field subnivel should be an instance of Subnivel'
        assert isinstance(destreza.bloque, BloqueCurricular), \
            'The field bloque should be an instance of BloqueCurricular'
        truncated_description = Truncator(destreza.description)
        assert str(destreza) == '{} - {}'.format(
            destreza.codigo,
            truncated_description.chars(110)
        ), 'The representation should be codigo and a truncated description'
        assert destreza._meta.db_table == 'destrezas', \
            'The table should be named "destrezas"'
        assert destreza._meta.verbose_name_plural == 'destrezas', \
            'The plural name should be "destrezas"'

    def test_get_destrezas_by_asignatura_cursos(self):
        destreza = mixer.blend(Destreza)
        curso = mixer.blend(Curso, subnivel=destreza.subnivel)
        destrezas = Destreza.objects.get_destrezas_by_asignatura_cursos(
            destreza.asignatura.id, [curso.id, ])
        assert destreza in destrezas, \
            'Should get destrezas by asignatura and cursos'


class TestCriterioEvaluacion:
    def test_model(self):
        criterio = mixer.blend(CriterioEvaluacion)
        assert isinstance(criterio, CriterioEvaluacion), \
            'Should be an instance of CriterioEvaluacion'
        assert isinstance(criterio.asignatura, Asignatura), \
            'The field asignatura should be an instance of Asignatura'
        assert isinstance(criterio.subnivel, Subnivel), \
            'The field subnivel should be an instance of Subnivel'
        assert str(criterio) == '{} - {}'.format(
            criterio.codigo,
            criterio.description
        ), 'The representation should be codigo and a truncated description'
        assert criterio._meta.db_table == 'criterios_evaluacion', \
            'The table should be named "criterios_evaluacion"'
        assert criterio._meta.verbose_name_plural == 'criterios de evaluación'

    def test_get_criterios_by_destrezas(self):
        destreza_1 = mixer.blend(Destreza)
        destreza_2 = mixer.blend(Destreza)
        criterio_1 = mixer.blend(CriterioEvaluacion)
        criterio_2 = mixer.blend(CriterioEvaluacion)
        criterio_1.destrezas.add(destreza_1)
        criterio_2.destrezas.add(destreza_2)

        criterios = CriterioEvaluacion.objects.get_criterios_by_destrezas(
            [destreza_1.pk, destreza_2.pk])
        # Should get the "criterios de evaluacion" by "destreza"
        assert criterio_1 in criterios
        assert criterio_2 in criterios


class TestIndicador:
    def test_model(self):
        criterio = mixer.blend(CriterioEvaluacion)
        indicador = mixer.blend(Indicador, criterio_evaluacion=criterio)
        assert isinstance(indicador, Indicador), \
            'Should be an instance of Indicador'
        assert isinstance(indicador.criterio_evaluacion, CriterioEvaluacion), \
            'The field criterio_evaluacion should be an instance of ' \
            'CriterioEvaluacion'
        assert str(indicador) == '{} - {}'.format(
            indicador.codigo,
            indicador.description
        ), 'The representation should be codigo and description'
        assert indicador._meta.db_table == 'indicadores', \
            'The table should be named "indicadores"'
        assert indicador._meta.verbose_name_plural == 'indicadores', \
            'The plural name should be "indicadores"'

    def test_get_indicadores_by_destreza(self):
        destreza = mixer.blend(Destreza)
        criterio = mixer.blend(CriterioEvaluacion)
        criterio.destrezas.add(destreza)
        indicador = mixer.blend(Indicador, criterio_evaluacion=criterio)
        indicadores = Indicador.objects.get_indicadores_by_destreza(
            destreza.id)
        assert indicador in indicadores, \
            'Should get indicadores by destreza'

    def test_get_indicadores_by_criterios(self):
        criterio_1 = mixer.blend(CriterioEvaluacion)
        criterio_2 = mixer.blend(CriterioEvaluacion)
        indicador_1 = mixer.blend(Indicador, criterio_evaluacion=criterio_1)
        indicador_2 = mixer.blend(Indicador, criterio_evaluacion=criterio_2)

        indicadores = Indicador.objects.get_indicadores_by_criterios(
            [criterio_1.pk, criterio_2.pk])
        # Should get the "indicadores" by "criterios de evaluación"
        assert indicador_1 in indicadores
        assert indicador_2 in indicadores


class TestPlanClase:
    def test_model(self):
        planificacion = mixer.blend(PlanClase)
        assert isinstance(planificacion, PlanClase), \
            'Should be an instance of PlanClase'
        assert isinstance(planificacion.elaborado_por, User), \
            'The field elaborado_por should be an instance of User'
        assert isinstance(planificacion.asignatura, Asignatura), \
            'The field asignatura should be an instance of Asignatura'
        assert str(planificacion) == planificacion.name, \
            'The string representation should be the name'
        assert planificacion._meta.db_table == 'planes_clase', \
            'The table should be named "planes_clase"'
        assert planificacion._meta.verbose_name_plural == 'planes de clase', \
            'The plural name should be "planes de clase"'

    def test_get_absolute_url(self):
        planificacion = mixer.blend(PlanClase)
        url = reverse('plan_clase_pdf', kwargs={'pk': planificacion.pk})
        assert url == planificacion.get_absolute_url(), \
            'Should get url of updating plan de clase'


class TestElementoCurricular:
    def test_model(self):
        elemento = mixer.blend(ElementoCurricular)
        assert isinstance(elemento, ElementoCurricular), \
            'Should be an instance of ElementoCurricular'
        assert isinstance(elemento.plan_clase, PlanClase), \
            'The field plan_clase should be an instance of PlanClase'
        assert isinstance(elemento.destreza, Destreza), \
            'The field destreza should be an instance of Destreza'
        assert str(elemento) == 'Destreza: {}'.format(
            elemento.destreza.codigo), \
            "The string representation should be the destreza's code"
        assert elemento._meta.db_table == 'elementos_curriculares', \
            'The table should be named "elementos_curriculares"'
        assert elemento._meta.verbose_name_plural == 'elementos curriculares',\
            'The plural name should be "elementos curriculares"'

    def test_indicadores_property(self):
        destreza = mixer.blend(Destreza)
        elemento_curricular = mixer.blend(ElementoCurricular,
                                          destreza=destreza)
        criterio = mixer.blend(CriterioEvaluacion)
        indicador_1 = mixer.blend(Indicador)
        indicador_2 = mixer.blend(Indicador)
        criterio.indicadores.set([indicador_1, indicador_2])
        destreza.criterios_evaluacion.set([criterio, ])

        assert indicador_1 in elemento_curricular.indicadores
        assert indicador_2 in elemento_curricular.indicadores


class TestProcesoDidactico:
    def test_model(self):
        proceso = mixer.blend(ProcesoDidactico)
        assert isinstance(proceso, ProcesoDidactico), \
            'Should be an instance of ProcesoDidactico'
        assert isinstance(proceso.elemento_curricular, ElementoCurricular), \
            'The field plan_clase should be an instance of ElementoCurricular'
        assert str(proceso) == proceso.name, \
            'The string representation should be the name'
        assert proceso._meta.db_table == 'procesos_didacticos', \
            'The table should be named "procesos_didacticos"'
        assert proceso._meta.verbose_name_plural == 'procesos didácticos', \
            'The plural name should be "procesos didácticos"'


class TestPlanAnual(TestCase):
    def setUp(self):
        self.plan = mixer.blend(
            PlanAnual,
            carga_horaria=8,
            semanas_trabajo=5,
            semanas_imprevistos=2
        )

    def test_model(self):
        assert isinstance(self.plan, PlanAnual), \
            'Should be an instance of PlanAnual'
        assert isinstance(self.plan, Planificacion), \
            'Should be an instance of Planificacion'
        assert isinstance(self.plan.asignatura, Asignatura), \
            'Should be an instance of Asignatura'
        assert self.plan._meta.db_table == 'planes_anuales', \
            'The table should be named "planes_anuales"'
        assert self.plan._meta.verbose_name_plural == 'planes anuales', \
            'The plural name should be "planes anuales"'

    def test_property_total_semanas(self):
        assert self.plan.total_semanas == self.plan.semanas_trabajo + \
            self.plan.semanas_imprevistos, 'Should equal the sum'

    def test_property_total_periodos(self):
        assert self.plan.total_periodos == self.plan.carga_horaria * \
            self.plan.semanas_trabajo, 'Should equal the product'

    def test_get_absolute_url(self):
        planificacion = mixer.blend(PlanAnual)
        url = reverse('plan_anual_pdf', kwargs={'pk': planificacion.pk})
        assert url == planificacion.get_absolute_url(), \
            'Should get url of updating plan anual'


class TestDesarrolloUnidad:
    def test_model(self):
        desarrollo_unidad = mixer.blend(DesarrolloUnidad)
        assert isinstance(desarrollo_unidad, DesarrolloUnidad)
        assert isinstance(desarrollo_unidad.plan_anual, PlanAnual)
        assert isinstance(desarrollo_unidad.unidad, Unidad)
        assert desarrollo_unidad._meta.db_table == 'desarrollo_unidades', \
            'The table should be named "desarrollo_unidades"'
        assert desarrollo_unidad._meta.verbose_name_plural == \
            'desarrollo de unidades', \
            'The plural name should be "desarrollo de unidades"'

    def test_criterios_evaluacion_property(self):
        desarrollo_unidad = mixer.blend(DesarrolloUnidad)
        destreza = mixer.blend(Destreza)
        criterio_1 = mixer.blend(CriterioEvaluacion)
        criterio_2 = mixer.blend(CriterioEvaluacion)
        destreza.criterios_evaluacion.set([criterio_1, criterio_2])
        desarrollo_unidad.destrezas.set([destreza, ])

        assert criterio_1 in desarrollo_unidad.criterios_evaluacion
        assert criterio_2 in desarrollo_unidad.criterios_evaluacion


class TestPlanUnidad(TestCase):
    def setUp(self):
        self.plan = mixer.blend(PlanUnidad)

    def test_model(self):
        assert isinstance(self.plan, PlanUnidad), \
            'Should be instance of PlanUnidad'
        assert isinstance(self.plan.unidad, Unidad), \
            'Should be instance fo Unidad'

    def test_get_absolute_url(self):
        planificacion = mixer.blend(PlanUnidad)
        url = reverse('plan_unidad_pdf', kwargs={'pk': planificacion.pk})
        assert url == planificacion.get_absolute_url(), \
            'Should get url of updating plan de unidad'


class TestActividadAprendizaje:
    def test_model(self):
        actividad = mixer.blend(ActividadAprendizaje)
        assert isinstance(actividad, ActividadAprendizaje)
        assert isinstance(actividad.plan_unidad, PlanUnidad)
        assert actividad._meta.db_table == 'actividades_aprendizaje', \
            'The table should be named "actividades_aprendizaje"'
        assert actividad._meta.verbose_name_plural == \
            'actividades de aprendizaje', \
            'The plural name should be "actividades de aprendizaje"'

    def test_criterios_evaluacion_property(self):
        actividad = mixer.blend(ActividadAprendizaje)
        destreza = mixer.blend(Destreza)
        criterio_1 = mixer.blend(CriterioEvaluacion)
        criterio_2 = mixer.blend(CriterioEvaluacion)
        destreza.criterios_evaluacion.set([criterio_1, criterio_2])
        actividad.destrezas.set([destreza, ])

        assert criterio_1 in actividad.criterios_evaluacion
        assert criterio_2 in actividad.criterios_evaluacion

    def test_indicadores_property(self):
        actividad = mixer.blend(ActividadAprendizaje)
        destreza = mixer.blend(Destreza)
        criterio = mixer.blend(CriterioEvaluacion)
        indicador_1 = mixer.blend(Indicador)
        indicador_2 = mixer.blend(Indicador)
        criterio.indicadores.set([indicador_1, indicador_2])
        destreza.criterios_evaluacion.set([criterio, ])
        actividad.destrezas.set([destreza, ])

        assert indicador_1 in actividad.indicadores
        assert indicador_2 in actividad.indicadores


class TestPlanDestrezas(TestCase):
    def setUp(self):
        self.plan = mixer.blend(PlanDestrezas)

    def test_model(self):
        assert isinstance(self.plan, PlanDestrezas), \
            'Should be instance of PlanDestrezas'

    def test_get_absolute_url(self):
        planificacion = mixer.blend(PlanDestrezas)
        url = reverse('plan_destrezas_pdf', kwargs={'pk': planificacion.pk})
        assert url == planificacion.get_absolute_url(), \
            'Should get url of updating plan de destrezas'

    def test_criterios_evaluacion_property(self):
        plan_destrezas = mixer.blend(PlanDestrezas)
        destreza = mixer.blend(Destreza)
        criterio_1 = mixer.blend(CriterioEvaluacion)
        criterio_2 = mixer.blend(CriterioEvaluacion)
        destreza.criterios_evaluacion.set([criterio_1, criterio_2])
        plan_destrezas.destrezas.set([destreza, ])

        assert criterio_1 in plan_destrezas.criterios_evaluacion
        assert criterio_2 in plan_destrezas.criterios_evaluacion

    def test_indicadores_property(self):
        plan_destrezas = mixer.blend(PlanDestrezas)
        destreza = mixer.blend(Destreza)
        criterio = mixer.blend(CriterioEvaluacion)
        indicador_1 = mixer.blend(Indicador)
        indicador_2 = mixer.blend(Indicador)
        criterio.indicadores.set([indicador_1, indicador_2])
        destreza.criterios_evaluacion.set([criterio, ])
        plan_destrezas.destrezas.set([destreza, ])

        assert indicador_1 in plan_destrezas.indicadores
        assert indicador_2 in plan_destrezas.indicadores
