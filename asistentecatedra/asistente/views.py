from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Libro
from .models import Pregunta


class HomeTemplateView(TemplateView):
    """Vista principal de la aplicación"""
    template_name = 'asistente/home.html'


class BibliotecaListView(ListView):
    """Biblioteca"""
    template_name = 'asistente/biblioteca.html'
    queryset = Libro.objects.get_libros_por_asignaturas()


class AyudaListView(ListView):
    """Ayuda"""
    template_name = 'asistente/ayuda.html'
    model = Pregunta


class PremiumTemplateView(TemplateView):
    """Vista de la pantalla para subscripción Premium"""
    template_name = 'asistente/premium.html'
