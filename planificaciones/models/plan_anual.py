from django.db import models
from django.core.validators import MaxValueValidator
# from django.urls import reverse
from .asignatura import Asignatura
from django.conf import settings
from ckeditor.fields import RichTextField
from planificaciones.models.planificacion import Planificacion
from .curso import Curso
from .objetivo import Objetivo
from .objetivo_general import ObjetivoGeneral


class PlanAnual(Planificacion):
    ano_lectivo = models.CharField(max_length=9)
    curso = models.ForeignKey(
        Curso,
        related_name='planes_anuales',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='planes_anuales',
        on_delete=models.SET_NULL,
        null=True
    )
    carga_horaria = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 41)],
        default=1,
        validators=[
            MaxValueValidator(40)]
    )
    semanas_trabajo = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 41)],
        default=1,
        validators=[
            MaxValueValidator(40)]
    )
    semanas_imprevistos = models.PositiveIntegerField(
        choices=[(x, str(x)) for x in range(1, 41)],
        default=1,
        validators=[
            MaxValueValidator(40)]
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
    )
    objetivos_curso = models.ManyToManyField(
        Objetivo,
        related_name='planes_anuales',
        blank=True
    )
    objetivos_generales_curso = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='planes_anuales',
        blank=True
    )
    ejes_transversales = models.TextField(max_length=255)
    bibliografia = RichTextField(config_name='basic')
    elaborado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='planes_anuales',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'planes_anuales'
        verbose_name_plural = "planes anuales"

    def get_absolute_url(self):
        pass
        # kwargs = {'pk': self.pk, 'slug': self.slug}
        # return reverse('plan_anual_update', kwargs=kwargs)

    @property
    def total_semanas(self):
        return self.semanas_trabajo + self.semanas_imprevistos

    @property
    def total_periodos(self):
        return self.carga_horaria * self.semanas_trabajo
