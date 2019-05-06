from django.contrib import admin
from .models import Libro
from .models import Pregunta

admin.site.register(Libro)
admin.site.register(Pregunta)
