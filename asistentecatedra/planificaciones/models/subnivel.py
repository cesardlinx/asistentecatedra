from django.db import models
from .nivel import Nivel


class Subnivel(models.Model):
    name = models.CharField(max_length=30)
    nivel = models.ForeignKey(
        Nivel,
        related_name='subniveles',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'subniveles'
        verbose_name_plural = "subniveles"

    def __str__(self):
        return self.name


