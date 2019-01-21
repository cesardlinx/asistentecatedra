from .models.curso import Curso
from .models.destreza import Destreza
from .models.indicador import Indicador
from .models.objetivo import Objetivo
from .models.asignatura import Asignatura
from .models.objetivo_general import ObjetivoGeneral
from .models.plan_clase import PlanClase
from .models.elemento_curricular import ElementoCurricular
from .models.proceso_didactico import ProcesoDidactico
from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory


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
            'numero_plan': 'Número de Plan de Clase',
            'objetivos': 'Objetivos de la unidad',
            'numero_estudiantes': 'Número de estudiantes',
            'periodo': 'Período',
            'metodologia': 'Metodología',
            'tecnica': 'Técnica',
            'contenido_cientifico': 'Contenido Científico',
            'material_didactico': 'Material Didáctico',
            'instrumento_evaluacion': 'Instrumento de Evaluación',
        }
        widgets = {
            'fecha': forms.TextInput,
            'cursos': forms.CheckboxSelectMultiple,
            'objetivos': forms.CheckboxSelectMultiple,
            'objetivos_generales': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Placeholders de campos
        # self.fields['name'].widget.attrs.update(
        #     {'placeholder': 'Nombre del Plan de Clase'})
        # self.fields['numero_plan'].widget.attrs.update(
        #     {'placeholder': 'Número de Plan de Clase'})
        # self.fields['fecha'].widget.attrs.update(
        #     {'placeholder': 'Fecha'})
        # self.fields['paralelos'].widget.attrs.update(
        #     {'placeholder': 'Paralelos'})
        # self.fields['numero_estudiantes'].widget.attrs.update(
        #     {'placeholder': 'Número de Estudiantes'})
        # self.fields['tema'].widget.attrs.update(
        #     {'placeholder': 'Tema'})
        # self.fields['periodos'].widget.attrs.update(
        #     {'placeholder': 'Períodos'})
        # self.fields['metodologia'].widget.attrs.update(
        #     {'placeholder': 'Metodología'})
        # self.fields['tecnica'].widget.attrs.update(
        #     {'placeholder': 'Técnica'})
        # self.fields['bibliografia'].widget.attrs.update(
        #     {'placeholder': 'Bibliografía'})

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
            self.fields['cursos'].queryset = Curso.objects\
                .get_cursos_by_asignatura(asignatura_id)

        # Para convertir el id de objetivo en una instancia de
        # Objetivo en el form
        if 'asignatura' in self.data and 'cursos' in self.data:
            try:
                asignatura_id = int(self.data.get('asignatura'))
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
            cursos_id = []

            for curso in cursos:
                cursos_id.append(curso.pk)

            objetivos = Objetivo.objects.get_objetivos_by_asignatura_cursos(
                asignatura_id, cursos_id)

            objetivos_generales = ObjetivoGeneral.objects\
                .get_objetivos_generales_by_asignatura_cursos(
                    asignatura_id, cursos_id)

            self.fields['objetivos'].queryset = objetivos
            self.fields['objetivos_generales'].queryset = objetivos_generales


"""Creación de formsets para Elemento Curricular y para Proceso Didáctico"""


class BaseProcesoDidacticoFormset(BaseInlineFormSet):
    """Clase que sirve de base para el inline formset de Proceso Didáctico"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Hace que todos los campos sean obligatorios
        for form in self.forms:
            form.empty_permitted = False

    def total_form_count(self):
        """Añade un formulario extra solo cuando no hay datos"""
        if self.data or self.files:
            return self.management_form.cleaned_data['TOTAL_FORMS']
        else:
            if self.initial_form_count() > 0:
                total_forms = self.initial_form_count()
            else:
                total_forms = self.initial_form_count() + self.extra
            # Limite de max_num
            if total_forms > self.max_num > 0:
                total_forms = self.max_num
            return total_forms


ProcesoDidacticoFormset = inlineformset_factory(
    ElementoCurricular,
    ProcesoDidactico,
    fields=('name', 'description', 'tiempo', 'recursos'),
    formset=BaseProcesoDidacticoFormset,
    extra=1
)


class BaseElementoCurricularFormset(BaseInlineFormSet):
    """Clase que sirve de base para el inline formset de Elemento Curricular"""
    def __init__(self, *args, **kwargs):
        """Inicializa los queryset de destrezas e indicadores en none
        se encarga de que reconozca los id provistos por el usuario
        en instancias"""
        super().__init__(*args, **kwargs)

        # Inicializa los queryset de las destrezas e indicadores en none
        # self.forms son el set de formularios del formset
        for idx, form in enumerate(self.forms):

            # La siguiente linea hace que todos los campos sean obligatorios
            form.empty_permitted = False

            form.fields['destreza'].queryset = Destreza.objects.none()
            form.fields['destreza'].empty_label = 'Elija una destreza.'

            form.fields['indicadores_logro'].queryset = Indicador.objects\
                .none()

            # Para convertir el id de destreza en una instancia de
            # Destreza en el formset
            if 'asignatura' in form.data and 'cursos' in form.data:
                try:
                    asignatura_id = int(form.data.get('asignatura'))
                    cursos_id = list(form.data.get('cursos'))
                    form.fields['destreza'].queryset = Destreza.objects\
                        .get_destrezas_by_asignatura_cursos(
                            asignatura_id, cursos_id)
                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                asignatura_id = form.instance.plan_clase.asignatura.pk
                cursos = form.instance.plan_clase.cursos.all()
                cursos_id = []

                for curso in cursos:
                    cursos_id.append(curso.pk)

                # for_print = Destreza.objects\
                #     .get_destrezas_by_asignatura_cursos(
                #         asignatura_id, cursos_id)

                form.fields['destreza'].queryset = Destreza.objects\
                    .get_destrezas_by_asignatura_cursos(
                        asignatura_id, cursos_id)

            # Para convertir el id de indicador en una instancia de Indicador
            # en el formset
            if 'elementos_curriculares-{}-destreza'.format(idx) in form.data:
                try:
                    destreza_id = int(form.data.get(
                        'elementos_curriculares-{}-destreza'.format(idx)))
                    form.fields['indicadores_logro'].queryset = Indicador\
                        .objects.get_indicadores_by_destreza(destreza_id)
                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                destreza_id = form.instance.destreza.pk

                form.fields['indicadores_logro'].queryset = Indicador.objects\
                    .get_indicadores_by_destreza(destreza_id)

    def add_fields(self, form, index):
        """Se crea el formset anidado con ProcesoDidacticoFormset"""
        # allow the super class to create the fields as usual
        super(BaseElementoCurricularFormset, self).add_fields(form, index)

        # store the formset in the .nested property
        form.nested = ProcesoDidacticoFormset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='proceso-%s-%s' % (
                form.prefix,
                ProcesoDidacticoFormset.get_default_prefix()),)

    def is_valid(self):
        """
        Define la validación para el formset BaseElementoCurricularFormset
        """
        result = super(BaseElementoCurricularFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    # cada form válido si lo es también su nested formset
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):
        """Define el guardado del formset"""
        result = super(BaseElementoCurricularFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result

    def total_form_count(self):
        """
        Añade un formulario extra (inicial) solo cuando no hay datos
        """
        if self.data or self.files:
            return self.management_form.cleaned_data['TOTAL_FORMS']
        else:
            if self.initial_form_count() > 0:
                total_forms = self.initial_form_count()
            else:
                total_forms = self.initial_form_count() + self.extra
            # Limite de max_num
            if total_forms > self.max_num > 0:
                total_forms = self.max_num
            return total_forms


# Creación del formset para ElementoCurricular
ElementoCurricularFormset = inlineformset_factory(  # TODO: Añadir un límite
    PlanClase,
    ElementoCurricular,
    fields=('destreza', 'conocimientos_asociados', 'indicadores_logro',
            'actividades_evaluacion'),
    widgets={
        'indicadores_logro': forms.CheckboxSelectMultiple,
    },
    formset=BaseElementoCurricularFormset,
    extra=1,
)
