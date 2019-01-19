from django.shortcuts import render
from .models import Libro


def home(request):
    """Vista principal de la aplicación"""
    return render(request, 'asistente/home.html')


def biblioteca(request):
    """Biblioteca"""
    context = Libro.objects.get_libros_por_asignaturas()
    return render(request, 'asistente/biblioteca.html', context)


def ayuda(request):
    """Ayuda"""
    return render(request, 'asistente/ayuda.html')


def premium(request):
    """Vista de la pantalla para subscripción Premium"""
    return render(request, 'asistente/premium.html')
