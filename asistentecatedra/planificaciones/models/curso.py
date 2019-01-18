from django.db import models
from .subnivel import Subnivel
from .asignatura import Asignatura


class CursoManager(models.Manager):
    def get_cursos_by_asignatura(self, asignatura_id):
        """Obtiene los cursos de acuerdo al id de asignatura"""
        asignatura = Asignatura.objects.get(pk=asignatura_id)

        asignaturas_basico = (
            'Estudios Sociales',
            'Ciencias Naturales'
        )

        asignaturas_bachillerato = (
            'Física',
            'Química',
            'Biología',
            'Historia'
        )

        asignaturas_bachillerato2 = (
            'Educación para la Ciudadanía',
            'Filosofía',
            'Emprendimiento y Gestión'
        )

        if asignatura.name in asignaturas_bachillerato:
            return super().get_queryset()[10:]
        elif asignatura.name in asignaturas_bachillerato2:
            return super().get_queryset()[10:12]
        elif asignatura.name in asignaturas_basico:
            return super().get_queryset()[:10]
        else:
            return super().get_queryset()


class Curso(models.Model):
    name = models.CharField(max_length=15)
    subnivel = models.ForeignKey(
        Subnivel,
        related_name='cursos',
        on_delete=models.CASCADE
    )
    objects = CursoManager()

    class Meta:
        db_table = 'cursos'
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.name


