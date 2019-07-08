from django.db import models
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.destreza import Destreza
from planificaciones.models.indicador import Indicador
from planificaciones.models.plan_unidad import PlanUnidad


class ActividadAprendizaje(models.Model):
    plan_unidad = models.ForeignKey(
        PlanUnidad,
        related_name='actividades_aprendizaje',
        on_delete=models.CASCADE,
    )
    destrezas = models.ManyToManyField(
        Destreza,
        related_name='actividades_aprendizaje'
    )
    criterios_evaluacion = models.ManyToManyField(
        CriterioEvaluacion,
        related_name='actividades_aprendizaje'
    )
    estrategias_metodologicas = models.TextField(max_length=600)
    recursos = models.TextField(max_length=400)
    indicadores = models.ManyToManyField(
        Indicador,
        related_name='actividades_aprendizaje'
    )
    instrumentos_evaluacion = models.TextField(max_length=600)

    class Meta:
        db_table = 'actividades_aprendizaje'
        verbose_name_plural = "actividades de aprendizaje"
