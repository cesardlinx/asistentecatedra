from .asignatura import Asignatura
from .destreza import Destreza
from .objetivo_general import ObjetivoGeneral
from .subnivel import Subnivel
from django.db import models


class CriterioManager(models.Manager):
    def get_criterios_by_destrezas(self, destrezas_id):

        criterios = super().get_queryset().none()
        for idx, destreza_id in enumerate(destrezas_id):
            criterios_query = super().get_queryset().filter(
                destrezas__id=destreza_id
            ).order_by('pk', 'codigo').distinct('pk')
            criterios = criterios | criterios_query

        return criterios


class CriterioEvaluacion(models.Model):
    description = models.TextField(max_length=700)
    codigo = models.CharField(max_length=15)
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='criterios_evaluacion',
        on_delete=models.CASCADE
    )
    subnivel = models.ForeignKey(
        Subnivel,
        related_name='criterios_evaluacion',
        on_delete=models.CASCADE
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='criterios_evaluacion'
    )
    destrezas = models.ManyToManyField(
        Destreza,
        related_name='criterios_evaluacion',
    )
    objects = CriterioManager()

    class Meta:
        db_table = 'criterios_evaluacion'
        verbose_name_plural = "criterios de evaluación"

    def __str__(self):
        return "{} - {}".format(self.codigo, self.description)
