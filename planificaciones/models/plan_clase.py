from .objetivo import Objetivo
from .objetivo_general import ObjetivoGeneral
from .planificacion import Planificacion
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator, MinLengthValidator, \
    MinValueValidator
from django.db import models
from .curso import Curso
from django.urls import reverse
from .asignatura import Asignatura
from django.conf import settings


class PlanClase(Planificacion):
    numero_plan = models.IntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    fecha = models.DateField()
    cursos = models.ManyToManyField(
        Curso,
        related_name='planes_clase',
    )
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='planes_clase',
        on_delete=models.SET_NULL,
        null=True
    )
    objetivos = models.ManyToManyField(
        Objetivo,
        related_name='planes_clase',
        blank=True
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='planes_clase',
        blank=True
    )
    numero_estudiantes = models.CharField(max_length=10)
    tema = models.CharField(max_length=200, validators=[MinLengthValidator(4)])
    periodos = models.CharField(max_length=20)
    metodologia = models.TextField(
        max_length=200, validators=[MinLengthValidator(4)])
    tecnica = models.CharField(
        max_length=100, validators=[MinLengthValidator(4)])
    bibliografia = RichTextField(config_name='basic')
    contenido_cientifico = RichTextUploadingField()
    material_didactico = RichTextUploadingField()
    instrumento_evaluacion = RichTextUploadingField()
    elaborado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='planes_clase',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'planes_clase'
        verbose_name_plural = "planes de clase"

    def get_absolute_url(self):
        return reverse('plan_clase_pdf', kwargs={'pk': self.pk})
