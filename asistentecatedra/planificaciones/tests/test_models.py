import pytest
from mixer.backend.django import mixer
from django.utils.text import Truncator
from django.contrib.auth import get_user_model
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
        assert str(unidad) == '{} {} {}'.format(
            unidad.numero_unidad,
            unidad.curso,
            unidad.asignatura
        ), 'The representation should be numero de unidad, curso y asignatura'
        assert unidad._meta.db_table == 'unidades', \
            'The table should be named "unidades"'
        assert unidad._meta.verbose_name_plural == 'unidades', \
            'The plural name should be "unidades"'


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
            truncated_description.chars(50)
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
        truncated_description = Truncator(criterio.description)
        assert str(criterio) == '{} - {}'.format(
            criterio.codigo,
            truncated_description.chars(50)
        ), 'The representation should be codigo and a truncated description'
        assert criterio._meta.db_table == 'criterios_evaluacion', \
            'The table should be named "criterios_evaluacion"'
        assert criterio._meta.verbose_name_plural == 'criterios de evaluación'


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
        url = '/planificaciones/plan_clase/update/{}/{}/'.format(
            planificacion.id, planificacion.slug)
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
