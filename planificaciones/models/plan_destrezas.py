from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.destreza import Destreza
from planificaciones.models.indicador import Indicador
from planificaciones.models.planificacion import Planificacion
from planificaciones.models.unidad import Unidad

from .asignatura import Asignatura
from .curso import Curso
from .objetivo import Objetivo
from .objetivo_general import ObjetivoGeneral


class PlanDestrezas(Planificacion):
    ano_lectivo = models.CharField(max_length=9)
    unidad = models.ForeignKey(
        Unidad,
        related_name='planes_destrezas',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    curso = models.ForeignKey(
        Curso,
        related_name='planes_destrezas',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='planes_destrezas',
        on_delete=models.SET_NULL,
        null=True
    )
    periodos = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 41)],
        default=1,
        validators=[
            MaxValueValidator(40)]
    )
    semana_inicio = models.CharField(max_length=60)
    ejes_transversales = models.TextField(max_length=255)
    destrezas = models.ManyToManyField(
        Destreza,
        related_name='planes_destrezas',
    )
    objetivos = models.ManyToManyField(
        Objetivo,
        related_name='planes_destrezas',
        blank=True
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='planes_destrezas',
        blank=True
    )
    estrategias_metodologicas = models.TextField(max_length=700)
    recursos = models.TextField(max_length=500)
    actividades_evaluacion = models.TextField(max_length=600)
    necesidad_adaptacion = models.TextField(max_length=600,
                                            blank=True, null=True)
    adaptacion_curricular = models.TextField(max_length=600,
                                             blank=True, null=True)
    elaborado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='planes_destrezas',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'planes_destrezas'
        verbose_name_plural = "planes de destrezas"

    def get_absolute_url(self):
        return reverse('plan_destrezas_pdf', kwargs={'pk': self.pk})

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

    def get_update_url(self):
        return reverse('plan_destrezas_update',
                       kwargs={'pk': self.pk, 'slug': self.slug})

    def get_duplicate_url(self):
        return reverse('plan_destrezas_duplicate',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('plan_destrezas_delete',
                       kwargs={'pk': self.pk})
