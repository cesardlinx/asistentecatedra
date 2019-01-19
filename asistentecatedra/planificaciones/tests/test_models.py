import pytest
from mixer.backend.django import mixer
from django.utils.text import Truncator
from django.contrib.auth.models import User
from planificaciones.models.area import Area
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.bloque_curricular import BloqueCurricular
from planificaciones.models.nivel import Nivel
from planificaciones.models.subnivel import Subnivel
from planificaciones.models.curso import Curso
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.unidad import Unidad
from planificaciones.models.destreza import Destreza
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.indicador import Indicador
from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.elemento_curricular import ElementoCurricular
from planificaciones.models.proceso_didactico import ProcesoDidactico
pytestmark = pytest.mark.django_db


class TestArea:
    def test_model(self):
        area = mixer.blend(Area)
        assert isinstance(area, Area)
        assert str(area) == area.name
        assert area._meta.db_table == 'areas'
        assert area._meta.verbose_name_plural == 'áreas'


class TestAsignatura:
    def test_model(self):
        asignatura = mixer.blend(Asignatura)
        assert isinstance(asignatura, Asignatura)
        assert isinstance(asignatura.area, Area)
        assert str(asignatura) == asignatura.name
        assert asignatura._meta.db_table == 'asignaturas'
        assert asignatura._meta.verbose_name_plural == 'asignaturas'


class TestBloqueCurricular:
    def test_model(self):
        bloque = mixer.blend(BloqueCurricular)
        assert isinstance(bloque, BloqueCurricular)
        assert isinstance(bloque.asignatura, Asignatura)
        assert str(bloque) == bloque.name
        assert bloque._meta.db_table == 'bloques_curriculares'
        assert bloque._meta.verbose_name_plural == 'bloques curriculares'


class TestNivel:
    def test_model(self):
        nivel = mixer.blend(Nivel)
        assert isinstance(nivel, Nivel)
        assert str(nivel) == nivel.name
        assert nivel._meta.db_table == 'niveles'
        assert nivel._meta.verbose_name_plural == 'niveles'


class TestSubnivel:
    def test_model(self):
        subnivel = mixer.blend(Subnivel)
        assert isinstance(subnivel, Subnivel)
        assert isinstance(subnivel.nivel, Nivel)
        assert str(subnivel) == subnivel.name
        assert subnivel._meta.db_table == 'subniveles'
        assert subnivel._meta.verbose_name_plural == 'subniveles'


class TestCurso:
    def test_model(self):
        curso = mixer.blend(Curso)
        assert isinstance(curso, Curso)
        assert isinstance(curso.subnivel, Subnivel)
        assert str(curso) == curso.name
        assert curso._meta.db_table == 'cursos'
        assert curso._meta.verbose_name_plural == 'cursos'


class TestObjetivoGeneral:
    def test_model(self):
        objetivo = mixer.blend(ObjetivoGeneral)
        assert isinstance(objetivo, ObjetivoGeneral)
        assert isinstance(objetivo.area, Area)
        assert str(objetivo) == "{} - {}".format(objetivo.codigo,
                                                 objetivo.description)
        assert objetivo._meta.db_table == 'objetivos_generales'
        assert objetivo._meta.verbose_name_plural == 'objetivos generales'

    def test_get_objetivos_generales_by_asignatura_cursos(self):
        unidad = mixer.blend(Unidad)
        objetivo = mixer.blend(ObjetivoGeneral, area=unidad.asignatura.area)
        unidad.objetivos_generales.add(objetivo)
        objetivos = ObjetivoGeneral\
            .objects.get_objetivos_generales_by_asignatura_cursos(
                unidad.asignatura.id, [unidad.curso.id, ])
        assert objetivo in objetivos


class TestObjetivo:
    def test_model(self):
        objetivo = mixer.blend(Objetivo)
        assert isinstance(objetivo, Objetivo)
        assert isinstance(objetivo.subnivel, Subnivel)
        assert isinstance(objetivo.asignatura, Asignatura)
        assert str(objetivo) == "{} - {}".format(objetivo.codigo,
                                                 objetivo.description)
        assert objetivo._meta.db_table == 'objetivos'
        assert objetivo._meta.verbose_name_plural == 'objetivos'

    def test_get_objetivos_by_asignatura_cursos(self):
        objetivo = mixer.blend(Objetivo)
        unidad = mixer.blend(Unidad, asignatura=objetivo.asignatura)
        unidad.objetivos.add(objetivo)
        objetivos = Objetivo.objects.get_objetivos_by_asignatura_cursos(
            unidad.asignatura.id, [unidad.curso.id, ])
        assert objetivo in objetivos


class TestUnidad:
    def test_model(self):
        unidad = mixer.blend(Unidad)
        assert isinstance(unidad, Unidad)
        assert isinstance(unidad.curso, Curso)
        assert isinstance(unidad.asignatura, Asignatura)
        assert str(unidad) == '{} {} {}'.format(
            unidad.numero_unidad, unidad.curso, unidad.asignatura)
        assert unidad._meta.db_table == 'unidades'
        assert unidad._meta.verbose_name_plural == 'unidades'


class TestDestreza:
    def test_model(self):
        bloque = mixer.blend(BloqueCurricular)
        destreza = mixer.blend(Destreza, bloque=bloque)
        assert isinstance(destreza, Destreza)
        assert isinstance(destreza.asignatura, Asignatura)
        assert isinstance(destreza.subnivel, Subnivel)
        assert isinstance(destreza.bloque, BloqueCurricular)
        truncated_description = Truncator(destreza.description)
        assert str(destreza) == '{} - {}'.format(
            destreza.codigo, truncated_description.chars(50))
        assert destreza._meta.db_table == 'destrezas'
        assert destreza._meta.verbose_name_plural == 'destrezas'

    def test_get_destrezas_by_asignatura_cursos(self):
        destreza = mixer.blend(Destreza)
        curso = mixer.blend(Curso, subnivel=destreza.subnivel)
        destrezas = Destreza.objects.get_destrezas_by_asignatura_cursos(
            destreza.asignatura.id, [curso.id, ])
        assert destreza in destrezas


class TestCriterioEvaluacion:
    def test_model(self):
        criterio = mixer.blend(CriterioEvaluacion)
        assert isinstance(criterio, CriterioEvaluacion)
        assert isinstance(criterio.asignatura, Asignatura)
        assert isinstance(criterio.subnivel, Subnivel)
        truncated_description = Truncator(criterio.description)
        assert str(criterio) == '{} - {}'.format(
            criterio.codigo, truncated_description.chars(50))
        assert criterio._meta.db_table == 'criterios_evaluacion'
        assert criterio._meta.verbose_name_plural == 'criterios de evaluación'


class TestIndicador:
    def test_model(self):
        criterio = mixer.blend(CriterioEvaluacion)
        indicador = mixer.blend(Indicador, criterio_evaluacion=criterio)
        assert isinstance(indicador, Indicador)
        assert isinstance(indicador.criterio_evaluacion, CriterioEvaluacion)
        assert str(indicador) == '{} - {}'.format(indicador.codigo,
                                                  indicador.description)
        assert indicador._meta.db_table == 'indicadores'
        assert indicador._meta.verbose_name_plural == 'indicadores'

    def test_get_indicadores_by_destreza(self):
        destreza = mixer.blend(Destreza)
        criterio = mixer.blend(CriterioEvaluacion)
        criterio.destrezas.add(destreza)
        indicador = mixer.blend(Indicador, criterio_evaluacion=criterio)
        indicadores = Indicador.objects.get_indicadores_by_destreza(
            destreza.id)
        assert indicador in indicadores


class TestPlanClase:
    def test_model(self):
        planificacion = mixer.blend(PlanClase)
        assert isinstance(planificacion, PlanClase)
        assert isinstance(planificacion.elaborado_por, User)
        assert isinstance(planificacion.asignatura, Asignatura)
        assert str(planificacion) == planificacion.name
        assert planificacion._meta.db_table == 'planes_clase'
        assert planificacion._meta.verbose_name_plural == 'planes de clase'

    def test_get_absolute_url(self):
        planificacion = mixer.blend(PlanClase)
        url = '/planificaciones/plan_clase/update/{}/{}/'.format(
            planificacion.id, planificacion.slug)
        assert url == planificacion.get_absolute_url()


class TestElementoCurricular:
    def test_model(self):
        elemento = mixer.blend(ElementoCurricular)
        assert isinstance(elemento, ElementoCurricular)
        assert isinstance(elemento.plan_clase, PlanClase)
        assert isinstance(elemento.destreza, Destreza)
        assert str(elemento) == 'Destreza: {}'.format(elemento.destreza.codigo)
        assert elemento._meta.db_table == 'elementos_curriculares'
        assert elemento._meta.verbose_name_plural == 'elementos curriculares'


class TestProcesoDidactico:
    def test_model(self):
        proceso = mixer.blend(ProcesoDidactico)
        assert isinstance(proceso, ProcesoDidactico)
        assert isinstance(proceso.elemento_curricular, ElementoCurricular)
        assert str(proceso) == proceso.name
        assert proceso._meta.db_table == 'procesos_didacticos'
        assert proceso._meta.verbose_name_plural == 'procesos didácticos'
