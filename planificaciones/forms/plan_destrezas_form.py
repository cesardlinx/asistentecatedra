from planificaciones.models.curso import Curso
from planificaciones.models.destreza import Destreza
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.unidad import Unidad
from planificaciones.models.plan_destrezas import PlanDestrezas
from django import forms
from planificaciones.widgets import EnhancedCheckboxSelectMultiple


class PlanDestrezasForm(forms.ModelForm):
    """ModelForm para el Plan de Unidad"""
    class Meta:
        model = PlanDestrezas
        fields = [
            'name',
            'ano_lectivo',
            'asignatura',
            'docentes',
            'curso',
            'paralelos',
            'unidad',
            'objetivos',
            'objetivos_generales',
            'destrezas',
            'periodos',
            'semana_inicio',
            'ejes_transversales',
            'estrategias_metodologicas',
            'recursos',
            'actividades_evaluacion',
            'necesidad_adaptacion',
            'adaptacion_curricular',
            'aprobado_por',
            'revisado_por',
        ]
        labels = {
            'name': 'Nombre de la Planificación de Unidad',
            'ano_lectivo': 'Año Lectivo',
            'docentes': 'Docente/s',
            'objetivos': 'Objetivos de Unidad',
            'periodos': 'Períodos',
            'semana_inicio': 'Semana de Inicio',
            'actividades_evaluacion': 'Actividades de Evaluación',
            'necesidad_adaptacion': 'Especificación de la necesidad '
                                    'educativa (opcional)',
            'adaptacion_curricular': 'Especificación de la adaptación a ser '
                                     'aplicada (opcional)',
            'aprobado_por': 'Aprobado por (opcional)',
            'revisado_por': 'Revisado por (opcional)',
        }
        widgets = {
            'objetivos': EnhancedCheckboxSelectMultiple,
            'objetivos_generales': EnhancedCheckboxSelectMultiple,
            'destrezas': EnhancedCheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicialización de campos
        self.fields['curso'].queryset = Curso.objects.none()
        self.fields['unidad'].queryset = Unidad.objects.none()
        self.fields['objetivos'].queryset = Objetivo.objects.none()
        self.fields['objetivos_generales'].queryset = ObjetivoGeneral.objects\
            .none()
        self.fields['destrezas'].queryset = Destreza.objects.none()

        # Default Option for select fields
        self.fields['asignatura'].empty_label = 'Elija una asignatura.'
        self.fields['curso'].empty_label = 'Elija un curso.'
        self.fields['unidad'].empty_label = 'Elija una unidad.'

        # Queryset para campos ajax en caso de existir datos post
        # en el formulario
        # Esto hace que el formulario tome los pk
        # y los pueda convertir a instancias

        # Para convertir el id de curso en una instancia de Curso en el form
        if 'asignatura' in self.data:
            try:
                asignatura_id = int(self.data.get('asignatura'))
                asignatura = Asignatura.objects.get(pk=asignatura_id)
                self.fields['curso'].queryset = asignatura.cursos.all()

            except (ValueError, TypeError):
                # invalid input from the client; ignore and
                # fallback to empty Cursos queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            asignatura = Asignatura.objects.get(pk=asignatura_id)
            self.fields['curso'].queryset = asignatura.cursos.all()

        # Para convertir el id de unidad en una instancia de
        # Unidad en el form
        if 'asignatura' in self.data and 'curso' in self.data:
            try:
                asignatura_id = int(self.data.get('asignatura'))
                curso_id = int(self.data.get('curso'))

                cursos_id = [curso_id, ]

                unidades = Unidad.objects\
                    .get_unidades_by_asignatura_curso(
                        asignatura_id, curso_id)
                destrezas = Destreza.objects\
                    .get_destrezas_by_asignatura_cursos(
                        asignatura_id, cursos_id)

                self.fields['unidad'].queryset = unidades
                self.fields['destrezas'].queryset = destrezas

            except (ValueError, TypeError):
                # invalid input from the client; ignore and fallback
                # to empty Unidad queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            curso_id = self.instance.curso.pk

            cursos_id = [curso_id, ]

            unidades = Unidad.objects\
                .get_unidades_by_asignatura_curso(
                    asignatura_id, curso_id)
            destrezas = Destreza.objects\
                .get_destrezas_by_asignatura_cursos(
                    asignatura_id, cursos_id)

            self.fields['unidad'].queryset = unidades
            self.fields['destrezas'].queryset = destrezas

        # Para convertir el id de objetivo en una instancia de
        # Objetivo en el form
        if 'unidad' in self.data:
            try:
                unidad_id = int(self.data.get('unidad'))
                unidad = Unidad.objects.get(pk=unidad_id)

                self.fields['objetivos'].queryset = unidad.objetivos.all()
                self.fields['objetivos_generales']\
                    .queryset = unidad.objetivos_generales.all()

            except (ValueError, TypeError):
                # invalid input from the client; ignore and fallback
                # to empty Objetivos queryset
                pass

        elif self.instance.pk:
            unidad_id = self.instance.unidad.pk
            unidad = Unidad.objects.get(pk=unidad_id)

            self.fields['objetivos'].queryset = unidad.objetivos.all()
            self.fields['objetivos_generales']\
                .queryset = unidad.objetivos_generales.all()
