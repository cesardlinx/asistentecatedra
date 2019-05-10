import pytest
from mixer.backend.django import mixer
from asistente.models import Pregunta
from asistente.models import Libro
from planificaciones.models.asignatura import Asignatura
from django.core.files import File
from django.db.models.signals import pre_delete
from accounts.tests.conftest import clean_test_files
from django.test import TestCase
pytestmark = pytest.mark.django_db


class TestLibro(TestCase):
    def test_model(self):
        libro = mixer.blend('asistente.Libro', archivo='libros/test_book.pdf')
        libro2 = mixer.blend('asistente.Libro')
        assert isinstance(libro, Libro), 'Should be an instance of Libro'
        assert isinstance(libro.archivo, File), \
            'The field archivo should be an instance of File'
        assert libro.filename() == 'test_book', \
            'The filename method should return the filename'
        assert libro2.filename() == 'El archivo no es un pdf', \
            'The filename method should return the filename only for pdfs'
        assert str(libro) == libro.name, \
            'The string representation should be the name'
        assert libro._meta.db_table == 'libros', \
            'The table should be named "libros"'
        assert libro._meta.verbose_name_plural == 'libros', \
            'The plural name should be "libros"'

    def test_get_libros_por_asignaturas(self):
        asignatura = mixer.blend(Asignatura, name='Matemática')
        libro = mixer.blend('asistente.Libro', asignatura=asignatura)
        libros = Libro.objects.get_libros_por_asignaturas()
        assert libro in libros['asignaturas']['matematica']['libros'], \
            'Should get libros by asignaturas'

    def test_pre_delete_signal(self):
        self.signal_was_called = False

        def handler(sender, instance, **kwargs):
            self.signal_was_called = True

        pre_delete.connect(handler)

        libro = mixer.blend('asistente.Libro')
        libro.delete()

        assert self.signal_was_called is True, \
            'Should call the pre_delete signal'

    def tearDown(self):
        clean_test_files()


class TestPregunta(TestCase):
    def test_model(self):
        pregunta = mixer.blend('asistente.Pregunta')
        assert isinstance(pregunta, Pregunta), \
            'Should be an instance of Pregunta'
        assert str(pregunta) == pregunta.question, \
            'The string representation should be the question'
        assert pregunta._meta.db_table == 'preguntas', \
            'The table should be named "preguntas"'
        assert pregunta._meta.verbose_name_plural == 'preguntas', \
            'The plural name should be "preguntas"'

    def tearDown(self):
        clean_test_files()
