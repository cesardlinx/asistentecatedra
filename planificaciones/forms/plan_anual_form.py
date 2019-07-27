from planificaciones.models.curso import Curso
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.plan_anual import PlanAnual
from django import forms
from planificaciones.widgets import EnhancedCheckboxSelectMultiple


class PlanAnualForm(forms.ModelForm):
    """ModelForm para el Plan Anual"""
    class Meta:
        model = PlanAnual
        fields = [
            'name',
            'ano_lectivo',
            'asignatura',
            'docentes',
            'curso',
            'paralelos',
            'carga_horaria',
            'semanas_trabajo',
            'semanas_imprevistos',
            'objetivos_generales',
            'objetivos_curso',
            'objetivos_generales_curso',
            'ejes_transversales',
            'bibliografia',
            'aprobado_por',
            'revisado_por',
        ]
        labels = {
            'name': 'Nombre de la Planificación Anual',
            'ano_lectivo': 'Año Lectivo',
            'docentes': 'Docente/s',
            'carga_horaria': 'Carga horaria semanal',
            'semanas_trabajo': 'Número de semanas de trabajo',
            'semanas_imprevistos': 'Número de semanas para imprevistos',
            'objetivos_generales': 'Objetivos del Área',
            'aprobado_por': 'Aprobado por (opcional)',
            'revisado_por': 'Revisado por (opcional)',
        }
        widgets = {
            'objetivos_generales': EnhancedCheckboxSelectMultiple,
            'objetivos_curso': EnhancedCheckboxSelectMultiple,
            'objetivos_generales_curso': EnhancedCheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicialización de campos
        self.fields['curso'].queryset = Curso.objects.none()
        self.fields['objetivos_generales'].queryset = ObjetivoGeneral.objects\
            .none()
        self.fields['objetivos_curso'].queryset = Objetivo.objects.none()
        self.fields['objetivos_generales_curso'].queryset = \
            ObjetivoGeneral.objects.none()

        # Default Option for select fields
        self.fields['asignatura'].empty_label = 'Elija una asignatura.'
        self.fields['curso'].empty_label = 'Elija un curso.'

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
                self.fields['objetivos_generales'].queryset = \
                    asignatura.area.objetivos_generales.all()

            except (ValueError, TypeError):
                # invalid input from the client; ignore and
                # fallback to empty Cursos queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            asignatura = Asignatura.objects.get(pk=asignatura_id)
            self.fields['curso'].queryset = asignatura.cursos.all()
            self.fields['objetivos_generales'].queryset = \
                asignatura.area.objetivos_generales.all()

        # Para convertir el id de objetivo en una instancia de
        # Objetivo en el form
        if 'asignatura' in self.data and 'curso' in self.data:
            try:
                asignatura_id = int(self.data.get('asignatura'))
                curso_id = int(self.data.get('curso'))

                cursos_id = [curso_id, ]

                objetivos = Objetivo.objects\
                    .get_objetivos_by_asignatura_cursos(
                        asignatura_id, cursos_id)

                objetivos_generales = ObjetivoGeneral.objects\
                    .get_objetivos_generales_by_asignatura_cursos(
                        asignatura_id, cursos_id)

                self.fields['objetivos_curso'].queryset = objetivos
                self.fields['objetivos_generales_curso']\
                    .queryset = objetivos_generales

            except (ValueError, TypeError):
                # invalid input from the client; ignore and fallback
                # to empty Objetivos queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            curso_id = self.instance.curso.pk

            cursos_id = [curso_id, ]

            objetivos = Objetivo.objects.get_objetivos_by_asignatura_cursos(
                asignatura_id, cursos_id)

            objetivos_generales = ObjetivoGeneral.objects\
                .get_objetivos_generales_by_asignatura_cursos(
                    asignatura_id, cursos_id)

            self.fields['objetivos_curso'].queryset = objetivos
            self.fields['objetivos_generales_curso'].queryset = \
                objetivos_generales
