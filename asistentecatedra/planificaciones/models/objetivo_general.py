from .area import Area
from django.db import models


class ObjetivoGeneralManager(models.Manager):
    def get_objetivos_generales_by_asignatura_cursos(
            self, asignatura_id, cursos_id):
        """Obtener el objetivo por asignatura y cursos"""
        objetivos_generales = super().get_queryset().none()
        for idx, curso_id in enumerate(cursos_id):
            objetivos_generales_query = super().get_queryset().filter(
                area__asignaturas__id=asignatura_id,
                unidades__curso__id=curso_id
            ).order_by('pk', 'codigo').distinct('pk')
            objetivos_generales = objetivos_generales | \
                objetivos_generales_query

        return objetivos_generales


class ObjetivoGeneral(models.Model):
    description = models.TextField(max_length=420)
    codigo = models.CharField(max_length=12)
    area = models.ForeignKey(
        Area,
        related_name='objetivos_generales',
        on_delete=models.CASCADE
    )
    objects = ObjetivoGeneralManager()

    class Meta:
        db_table = 'objetivos_generales'
        verbose_name_plural = "objetivos generales"

    def __str__(self):
        return "{} - {}".format(self.codigo, self.description)
