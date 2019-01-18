from django.db import models
from .destreza import Destreza
from .plan_clase import PlanClase
from .indicador import Indicador


class ElementoCurricular(models.Model):
    plan_clase = models.ForeignKey(
        PlanClase,
        related_name='elementos_curriculares',
        on_delete=models.CASCADE
    )
    destreza = models.ForeignKey(
        Destreza,
        related_name='elementos_curriculares',
        on_delete=models.SET_NULL,
        null=True
    )
    conocimientos_asociados = models.TextField(max_length=200)
    indicadores_logro = models.ManyToManyField(
        Indicador,
        related_name='elementos_curriculares'
    )
    actividades_evaluacion = models.TextField(max_length=200)

    class Meta:
        db_table = 'elementos_curriculares'
        verbose_name_plural = "elementos curriculares"
