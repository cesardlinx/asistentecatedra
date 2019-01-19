from .criterio_evaluacion import CriterioEvaluacion
from django.db import models


class IndicadorManager(models.Manager):
    def get_indicadores_by_destreza(self, destreza_id):
        indicadores = super().get_queryset().filter(
            criterio_evaluacion__destrezas__id=destreza_id
        ).distinct('codigo')
        return indicadores


class Indicador(models.Model):
    description = models.TextField(max_length=700)
    codigo = models.CharField(max_length=15)
    criterio_evaluacion = models.ForeignKey(
        CriterioEvaluacion,
        related_name='indicadores',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    objects = IndicadorManager()

    class Meta:
        db_table = 'indicadores'
        verbose_name_plural = "indicadores"

    def __str__(self):
        return "{} - {}".format(self.codigo, self.description)
