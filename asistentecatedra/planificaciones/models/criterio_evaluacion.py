from .asignatura import Asignatura
from .destreza import Destreza
from .objetivo_general import ObjetivoGeneral
from .subnivel import Subnivel
from django.db import models
from django.utils.text import Truncator


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

    class Meta:
        db_table = 'criterios_evaluacion'
        verbose_name_plural = "criterios de evaluación"

    def __str__(self):
        truncated_description = Truncator(self.description)
        return "{} - {}".format(self.codigo, truncated_description.chars(50))


