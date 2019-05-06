from django.db import models
from .subnivel import Subnivel


class Curso(models.Model):
    name = models.CharField(max_length=15)
    subnivel = models.ForeignKey(
        Subnivel,
        related_name='cursos',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'cursos'
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.name
