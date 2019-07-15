from planificaciones.models.curso import Curso
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.plan_clase import PlanClase
from django import forms
from django.http import QueryDict
from planificaciones.widgets import EnhancedCheckboxSelectMultiple


class PlanClaseForm(forms.ModelForm):
    """ModelForm para el Plan de Clase"""
    class Meta:
        model = PlanClase
        fields = [
            'name',
            'numero_plan',
            'fecha',
            'asignatura',
            'cursos',
            'paralelos',
            'numero_estudiantes',
            'tema',
            'periodos',
            'metodologia',
            'tecnica',
            'objetivos',
            'objetivos_generales',
            'bibliografia',
            'contenido_cientifico',
            'material_didactico',
            'instrumento_evaluacion',
            'observaciones',
            'aprobado_por',
        ]
        labels = {
            'name': 'Nombre del Plan de Clase',
            'numero_plan': 'Número de Plan de Clase (opcional)',
            'objetivos': 'Objetivos de la unidad',
            'numero_estudiantes': 'Número de estudiantes',
            'periodo': 'Período',
            'metodologia': 'Metodología',
            'tecnica': 'Técnica',
            'contenido_cientifico': 'Contenido Científico',
            'material_didactico': 'Material Didáctico',
            'instrumento_evaluacion': 'Instrumento de Evaluación',
            'observaciones': 'Observaciones (opcional)',
            'aprobado_por': 'Aprobado por (opcional)',
        }
        widgets = {
            'numero_plan': forms.TextInput,
            'fecha': forms.TextInput,
            'cursos': EnhancedCheckboxSelectMultiple(
                attrs={'li_class': 'inline-list-item'}),
            'objetivos': EnhancedCheckboxSelectMultiple,
            'objetivos_generales': EnhancedCheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicialización de campos
        self.fields['cursos'].queryset = Curso.objects.none()
        self.fields['objetivos'].queryset = Objetivo.objects.none()
        self.fields['objetivos_generales'].queryset = ObjetivoGeneral.objects\
            .none()

        # Default Option for select fields
        self.fields['asignatura'].empty_label = 'Elija una asignatura.'

        # Queryset para campos ajax en caso de existir datos post
        # en el formulario
        # Esto hace que el formulario tome los pk
        # y los pueda convertir a instancias

        # Para convertir el id de curso en una instancia de Curso en el form
        if 'asignatura' in self.data:
            try:
                asignatura_id = int(self.data.get('asignatura'))
                asignatura = Asignatura.objects.get(pk=asignatura_id)
                self.fields['cursos'].queryset = asignatura.cursos.all()

            except (ValueError, TypeError):
                # invalid input from the client; ignore and
                # fallback to empty Cursos queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            asignatura = Asignatura.objects.get(pk=asignatura_id)
            self.fields['cursos'].queryset = asignatura.cursos.all()

        # Para convertir el id de objetivo en una instancia de
        # Objetivo en el form
        if 'asignatura' in self.data and 'cursos' in self.data:
            try:
                asignatura_id = int(self.data.get('asignatura'))

                if isinstance(self.data, QueryDict):
                    cursos_id = list(self.data.getlist('cursos'))
                else:
                    cursos_id = list(self.data.get('cursos'))

                objetivos = Objetivo.objects\
                    .get_objetivos_by_asignatura_cursos(
                        asignatura_id, cursos_id)

                objetivos_generales = ObjetivoGeneral.objects\
                    .get_objetivos_generales_by_asignatura_cursos(
                        asignatura_id, cursos_id)

                self.fields['objetivos'].queryset = objetivos
                self.fields['objetivos_generales']\
                    .queryset = objetivos_generales

            except (ValueError, TypeError):
                # invalid input from the client; ignore and fallback
                # to empty Objetivos queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            cursos = self.instance.cursos.all()

            cursos_id = [curso.pk for curso in cursos]

            objetivos = Objetivo.objects.get_objetivos_by_asignatura_cursos(
                asignatura_id, cursos_id)

            objetivos_generales = ObjetivoGeneral.objects\
                .get_objetivos_generales_by_asignatura_cursos(
                    asignatura_id, cursos_id)

            self.fields['objetivos'].queryset = objetivos
            self.fields['objetivos_generales'].queryset = objetivos_generales
