from django.test import TestCase
from mixer.backend.django import mixer
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


class PlanificacionesTestCase(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)
        subnivel = mixer.blend(Subnivel)
        self.curso_1 = mixer.blend(Curso, subnivel=subnivel)
        self.curso_2 = mixer.blend(Curso, subnivel=subnivel)
        self.asignatura = mixer.blend(Asignatura)
        self.asignatura.cursos.add(self.curso_1, self.curso_2)

        self.unidad_1 = mixer.blend(Unidad, curso=self.curso_1,
                                    asignatura=self.asignatura)
        self.unidad_2 = mixer.blend(Unidad, curso=self.curso_2,
                                    asignatura=self.asignatura)
        self.objetivo_1 = mixer.blend(Objetivo, asignatura=self.asignatura)
        self.objetivo_2 = mixer.blend(Objetivo, asignatura=self.asignatura)
        self.general_1 = mixer.blend(ObjetivoGeneral,
                                     area=self.asignatura.area)
        self.general_2 = mixer.blend(ObjetivoGeneral,
                                     area=self.asignatura.area)

        self.unidad_1.objetivos.set([self.objetivo_1, self.objetivo_2])
        self.unidad_1.objetivos_generales.set([self.general_1, self.general_2])

        self.unidad_2.objetivos.set([self.objetivo_1, self.objetivo_2])
        self.unidad_2.objetivos_generales.set([self.general_1, self.general_2])

        self.destreza_1 = mixer.blend(Destreza, asignatura=self.asignatura,
                                      subnivel=subnivel)
        self.destreza_2 = mixer.blend(Destreza, asignatura=self.asignatura,
                                      subnivel=subnivel)
        self.criterio_1 = mixer.blend(CriterioEvaluacion,
                                      asignatura=self.asignatura,
                                      subnivel=subnivel)
        self.criterio_1.destrezas.add(self.destreza_1)
        self.indicador_1 = mixer.blend(Indicador,
                                       criterio_evaluacion=self.criterio_1)
        self.indicador_2 = mixer.blend(Indicador,
                                       criterio_evaluacion=self.criterio_1)

        self.criterio_2 = mixer.blend(CriterioEvaluacion,
                                      asignatura=self.asignatura,
                                      subnivel=subnivel)
        self.criterio_2.destrezas.add(self.destreza_2)
        self.indicador_3 = mixer.blend(Indicador,
                                       criterio_evaluacion=self.criterio_2)
        self.indicador_4 = mixer.blend(Indicador,
                                       criterio_evaluacion=self.criterio_2)
