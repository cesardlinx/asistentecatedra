from django.db import models
from django.contrib.auth.models import User
from .asignatura import Asignatura
from .curso import Curso


class Planificacion(models.Model):
    name = models.CharField(max_length=40)
    fecha = models.DateField()
    asignatura = models.ForeignKey(
        Asignatura,
        related_name='planes_clase',
        on_delete=models.SET_NULL,
        null=True
    )
    cursos = models.ManyToManyField(
        Curso,
        related_name='planes_clase',
    )
    elaborado_por = models.ForeignKey(
        User,
        related_name='planes_clase',
        on_delete=models.CASCADE
    )
    aprobado_por = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    observaciones = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True
