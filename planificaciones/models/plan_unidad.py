from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

from planificaciones.models.planificacion import Planificacion
from planificaciones.models.unidad import Unidad

from .asignatura import Asignatura
from .curso import Curso
from .objetivo import Objetivo
from .objetivo_general import ObjetivoGeneral


class PlanUnidad(Planificacion):
    ano_lectivo = models.CharField(max_length=9)
    unidad = models.ForeignKey(
        Unidad,
        related_name='planes_unidad',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    curso = models.ForeignKey(
        Curso,
        related_name='planes_unidad',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='planes_unidad',
        on_delete=models.SET_NULL,
        null=True
    )
    periodos = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 41)],
        default=1,
        validators=[
            MaxValueValidator(40)]
    )
    tiempo = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 41)],
        default=1,
        validators=[
            MaxValueValidator(40)]
    )
    objetivos = models.ManyToManyField(
        Objetivo,
        related_name='planes_unidad',
        blank=True
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='planes_unidad',
        blank=True
    )
    necesidad_adaptacion = models.TextField(max_length=600,
                                            blank=True, null=True)
    adaptacion_curricular = models.TextField(max_length=600,
                                             blank=True, null=True)
    elaborado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='planes_unidad',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'planes_unidad'
        verbose_name_plural = "planes de unidad"

    def get_absolute_url(self):
        return reverse('plan_unidad_pdf', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('plan_unidad_update',
                       kwargs={'pk': self.pk, 'slug': self.slug})

    def get_duplicate_url(self):
        return reverse('plan_unidad_duplicate',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('plan_unidad_delete',
                       kwargs={'pk': self.pk})
