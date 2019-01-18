from django.contrib import admin
from .models.area import Area
from .models.asignatura import Asignatura
from .models.bloque_curricular import BloqueCurricular
from .models.criterio_evaluacion import CriterioEvaluacion
from .models.curso import Curso
from .models.destreza import Destreza
from .models.indicador import Indicador
from .models.nivel import Nivel
from .models.objetivo_general import ObjetivoGeneral
from .models.objetivo import Objetivo
from .models.proceso_didactico import ProcesoDidactico
from .models.subnivel import Subnivel
from .models.unidad import Unidad

admin.site.register(Area)
admin.site.register(Asignatura)
admin.site.register(BloqueCurricular)
admin.site.register(CriterioEvaluacion)
admin.site.register(Curso)
admin.site.register(Destreza)
admin.site.register(Indicador)
admin.site.register(Nivel)
admin.site.register(ObjetivoGeneral)
admin.site.register(Objetivo)
admin.site.register(ProcesoDidactico)
admin.site.register(Subnivel)
admin.site.register(Unidad)
