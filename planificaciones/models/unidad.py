from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .asignatura import Asignatura
from .curso import Curso
from .objetivo_general import ObjetivoGeneral
from .objetivo import Objetivo
from django.utils.text import Truncator


class UnidadManager(models.Manager):
    def get_unidades_by_asignatura_curso(self, asignatura_id, curso_id):
        unidades = super().get_queryset().filter(
            asignatura__id=asignatura_id,
            curso__id=curso_id,
        ).distinct('pk')
        return unidades


class Unidad(models.Model):
    numero_unidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    titulo = models.CharField(max_length=400)
    curso = models.ForeignKey(
        Curso,
        related_name='unidades',
        on_delete=models.CASCADE
    )
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='unidades',
        on_delete=models.CASCADE
    )
    objetivos_generales = models.ManyToManyField(
        ObjetivoGeneral,
        related_name='unidades',
        blank=True,
    )
    objetivos = models.ManyToManyField(
        Objetivo,
        related_name='unidades',
        blank=True,
    )
    objects = UnidadManager()

    class Meta:
        db_table = 'unidades'
        verbose_name_plural = "unidades"

    def __str__(self):
        truncated_titulo = Truncator(self.titulo)
        return "{} - {}".format(self.numero_unidad, truncated_titulo.chars(30))
