from django.db import models
from .area import Area


class Asignatura(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(
        Area,
        related_name='asignaturas',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'asignaturas'
        verbose_name_plural = "asignaturas"

    def __str__(self):
        return self.name


