import re
import collections
from django.db import models
from planificaciones.models.curso import Curso
from planificaciones.models.asignatura import Asignatura
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class LibroManager(models.Manager):
    def get_libros_por_asignaturas(self):
        """Regresa un diccionario con los libros clasificados por asignatura"""
        result = {
            'asignaturas': {
                'matematica': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Matemática'),
                    'nombre': 'Matemática'
                },
                'literatura': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Lengua y Literatura'),
                    'nombre': 'Lengua y Literatura'
                },
                'naturales': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Ciencias Naturales'),
                    'nombre': 'Ciencias Naturales'
                },
                'sociales': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Estudios Sociales'),
                    'nombre': 'Estudios Sociales'
                },
                'fisica': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Física'),
                    'nombre': 'Física'
                },
                'quimica': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Química'),
                    'nombre': 'Química'
                },
                'biologia': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Biología'),
                    'nombre': 'Biología'
                },
                'historia': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Historia'),
                    'nombre': 'Historia'
                },
                'ciudadania': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Educación para la Ciudadanía'),
                    'nombre': 'Educación para la Ciudadanía'
                },
                'emprendimiento': {
                    'libros': super().get_queryset().filter(
                        asignatura__name='Emprendimiento y Gestión'),
                    'nombre': 'Emprendimiento y Gestión'
                }
            }
        }

        return collections.OrderedDict(sorted(result.items()))


class Libro(models.Model):
    name = models.CharField(max_length=30)
    archivo = models.FileField(
        upload_to='libros/',
        null=True,
        verbose_name='',
        validators=[FileExtensionValidator(['pdf'])]
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='libros'
    )
    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='libros',
        null=True,
        blank=True
    )
    objects = LibroManager()

    class Meta:
        db_table = 'libros'
        verbose_name_plural = 'libros'

    def filename(self):
        match = re.search(r'libros\/(.+)\.pdf', self.archivo.name)

        if match:
            return match.group(1)

        return 'El archivo no es un pdf'

    def __str__(self):
        return self.name

# Para que caundo se borre la instancia, se elimine también el archivo
# Receive the pre_delete signal and delete the file associated with the model
# instance.


@receiver(pre_delete, sender=Libro)
def libro_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.archivo.delete(False)


class Pregunta(models.Model):
    question = models.CharField(max_length=92)
    answer = models.CharField(max_length=200)

    class Meta:
        db_table = 'preguntas'
        verbose_name_plural = 'preguntas'

    def __str__(self):
        return self.question
