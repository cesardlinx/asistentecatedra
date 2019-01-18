from django.db import models
from .asignatura import Asignatura
from django.core.validators import MinValueValidator, MaxValueValidator


class BloqueCurricular(models.Model):
    numero_bloque = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    name = models.CharField(max_length=70)
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='bloques',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'bloques_curriculares'
        verbose_name_plural = "bloques curriculares"

    def __str__(self):
        return self.name


