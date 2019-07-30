from django.db import models

from planificaciones.models.indicador import Indicador

from .destreza import Destreza
from .plan_clase import PlanClase


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
        null=True,
        blank=False
    )
    conocimientos_asociados = models.TextField(max_length=200)
    actividades_evaluacion = models.TextField(max_length=200)

    class Meta:
        db_table = 'elementos_curriculares'
        verbose_name_plural = "elementos curriculares"

    def __str__(self):
        return 'Destreza: {}'.format(self.destreza.codigo)

    @property
    def indicadores(self):
        indicadores = Indicador.objects.\
            get_indicadores_by_destreza(self.destreza.id)
        return indicadores
