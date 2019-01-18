from django.db import models
from .elemento_curricular import ElementoCurricular


class ProcesoDidactico(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    tiempo = models.CharField(max_length=11)
    recursos = models.TextField(max_length=200)
    elemento_curricular = models.ForeignKey(
        ElementoCurricular,
        related_name='procesos_didacticos',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'procesos_didacticos'
        verbose_name_plural = "procesos didácticos"

    def __str__(self):
        return self.name


