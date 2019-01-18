from .asignatura import Asignatura
from .subnivel import Subnivel
from django.db import models


class ObjetivoManager(models.Manager):
    def get_objetivos_by_asignatura_cursos(self, asignatura_id, cursos_id):
        """Obtener el objetivo por asignatura y cursos"""
        objetivos = super().get_queryset().none()
        for idx, curso_id in enumerate(cursos_id):
            objetivos_query = super().get_queryset().filter(
                asignatura__id=asignatura_id,
                unidades__curso__id=curso_id
            ).order_by('pk', 'codigo').distinct('pk')
            objetivos = objetivos | objetivos_query

        return objetivos


class Objetivo(models.Model):
    description = models.TextField(max_length=620)
    codigo = models.CharField(max_length=12)
    subnivel = models.ForeignKey(
        Subnivel,
        related_name='objetivos',
        on_delete=models.CASCADE
    )
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='objetivos',
        on_delete=models.CASCADE
    )
    objects = ObjetivoManager()

    class Meta:
        db_table = 'objetivos'
        verbose_name_plural = "objetivos"

    def __str__(self):
        return "{} - {}".format(self.codigo, self.description)


