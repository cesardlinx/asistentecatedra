from django.core.validators import MaxValueValidator
from django.db import models

from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.destreza import Destreza
from planificaciones.models.indicador import Indicador
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.plan_anual import PlanAnual
from planificaciones.models.unidad import Unidad


class DesarrolloUnidad(models.Model):
    plan_anual = models.ForeignKey(
        PlanAnual,
        related_name='desarrollo_unidades',
        on_delete=models.CASCADE,
    )
    unidad = models.ForeignKey(
        Unidad,
        related_name='desarrollo_unidades',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    objetivos = models.ManyToManyField(
        Objetivo,
        related_name='desarrollo_unidades',
        blank=True
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='desarrollo_unidades',
        blank=True
    )
    destrezas = models.ManyToManyField(
        Destreza,
        related_name='desarrollo_unidades',
    )
    orientaciones_metodologicas = models.TextField(max_length=700)
    semanas = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 9)],
        default=1,
        validators=[
            MaxValueValidator(8)]
    )

    class Meta:
        db_table = 'desarrollo_unidades'
        verbose_name_plural = "desarrollo de unidades"

    @property
    def criterios_evaluacion(self):
        destrezas_id = [destreza.id for destreza in self.destrezas.all()]
        return CriterioEvaluacion.objects\
            .get_criterios_by_destrezas(destrezas_id)

    @property
    def indicadores(self):
        indicadores = Indicador.objects.none()
        for destreza in self.destrezas.all():
            indicadores_destreza = Indicador.objects.\
                get_indicadores_by_destreza(destreza.id)
            indicadores = indicadores | indicadores_destreza

        return indicadores
