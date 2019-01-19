import pytest
from mixer.backend.django import mixer
from asistente.models import Pregunta
from asistente.models import Libro
from planificaciones.models.asignatura import Asignatura
from django.core.files import File
from django.db.models.signals import pre_delete
pytestmark = pytest.mark.django_db


class TestLibro(object):
    def test_model(self):
        libro = mixer.blend('asistente.Libro', archivo='libros/test_book.pdf')
        libro2 = mixer.blend('asistente.Libro')
        assert isinstance(libro, Libro)
        assert isinstance(libro.archivo, File)
        assert libro.filename() == 'test_book'
        assert libro2.filename() == 'El archivo no es un pdf'
        assert str(libro) == libro.name
        assert libro._meta.db_table == 'libros'
        assert libro._meta.verbose_name_plural == 'libros'

    def test_get_libros_por_asignaturas(self):
        asignatura = mixer.blend(Asignatura, name='Matemática')
        libro = mixer.blend('asistente.Libro', asignatura=asignatura)
        libros = Libro.objects.get_libros_por_asignaturas()
        assert libro in libros['asignaturas']['matematica']['libros']

    def test_pre_delete_signal(self):
        self.signal_was_called = False

        def handler(sender, instance, **kwargs):
            self.signal_was_called = True

        pre_delete.connect(handler)

        libro = mixer.blend('asistente.Libro')
        libro.delete()

        assert self.signal_was_called is True


class TestPregunta:
    def test_model(self):
        pregunta = mixer.blend('asistente.Pregunta')
        assert isinstance(pregunta, Pregunta)
        assert str(pregunta) == pregunta.question
        assert pregunta._meta.db_table == 'preguntas'
        assert pregunta._meta.verbose_name_plural == 'preguntas'
