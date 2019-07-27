from .asignatura import Asignatura
from .bloque_curricular import BloqueCurricular
from .subnivel import Subnivel
from django.db import models
from django.utils.text import Truncator


class DestrezaManager(models.Manager):
    def get_destrezas_by_asignatura_cursos(self, asignatura_id, cursos_id):

        destrezas = super().get_queryset().none()
        for idx, curso_id in enumerate(cursos_id):
            destrezas_query = super().get_queryset().filter(
                asignatura__id=asignatura_id,
                subnivel__cursos__id=curso_id
            ).order_by('pk', 'codigo').distinct('pk')
            destrezas = destrezas | destrezas_query

        return destrezas


class Destreza(models.Model):
    description = models.TextField(max_length=400)
    codigo = models.CharField(max_length=15)
    imprescindible = models.BooleanField(default=False)
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='destrezas',
        on_delete=models.CASCADE
    )
    subnivel = models.ForeignKey(
        Subnivel,
        related_name='destrezas',
        on_delete=models.CASCADE
    )
    bloque = models.ForeignKey(
        BloqueCurricular,
        related_name='destrezas',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    objects = DestrezaManager()

    class Meta:
        db_table = 'destrezas'
        verbose_name_plural = "destrezas"

    def __str__(self):
        truncated_description = Truncator(self.description)
        return "{} - {}".format(self.codigo, truncated_description.chars(110))
