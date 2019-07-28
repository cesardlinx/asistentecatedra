from planificaciones.models.destreza import Destreza
from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.elemento_curricular import ElementoCurricular
from planificaciones.models.proceso_didactico import ProcesoDidactico
from django.http import QueryDict
from django.forms import BaseInlineFormSet, inlineformset_factory


"""Creación de formsets para Elemento Curricular y para Proceso Didáctico"""


class BaseProcesoDidacticoFormset(BaseInlineFormSet):
    """Clase que sirve de base para el inline formset de Proceso Didáctico"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Hace que todos los campos sean obligatorios
        for form in self.forms:
            form.empty_permitted = False

    def total_form_count(self):
        """
        Return the total number of forms in this FormSet.
        Also adds an initial extra form only if there is no instance attached
        """
        if self.is_bound:
            return super().total_form_count()
        else:

            initial_forms = self.initial_form_count()

            # Considers the extra fields only if there is no instance
            if self.instance.pk:
                total_forms = max(initial_forms, self.min_num)
            else:
                total_forms = max(initial_forms, self.min_num) + self.extra
            # Allow all existing related objects/inlines to be displayed,
            # but don't allow extra beyond max_num.
            if initial_forms > self.max_num >= 0:
                total_forms = initial_forms
            elif total_forms > self.max_num >= 0:
                total_forms = self.max_num
        return total_forms


ProcesoDidacticoFormset = inlineformset_factory(
    ElementoCurricular,
    ProcesoDidactico,
    fields=('name', 'description', 'tiempo', 'recursos'),
    formset=BaseProcesoDidacticoFormset,
    max_num=10,
    extra=1
)


class BaseElementoCurricularFormset(BaseInlineFormSet):
    """Clase que sirve de base para el inline formset de Elemento Curricular"""

    def __init__(self, *args, **kwargs):
        """Inicializa los queryset de destrezas en none
        se encarga de que reconozca los id provistos por el usuario
        en instancias"""
        super().__init__(*args, **kwargs)

        # Inicializa los queryset de las destrezas en none
        # self.forms son el set de formularios del formset
        for idx, form in enumerate(self.forms):

            # La siguiente linea hace que todos los campos sean obligatorios
            form.empty_permitted = False

            form.fields['destreza'].queryset = Destreza.objects.none()
            form.fields['destreza'].empty_label = 'Elija una destreza.'

            # Para convertir el id de destreza en una instancia de
            # Destreza en el formset
            if 'asignatura' in form.data and 'cursos' in form.data:
                try:
                    asignatura_id = int(form.data.get('asignatura'))

                    if isinstance(self.data, QueryDict):
                        cursos_id = list(self.data.getlist('cursos'))
                    else:
                        cursos_id = list(self.data.get('cursos'))

                    form.fields['destreza'].queryset = Destreza.objects\
                        .get_destrezas_by_asignatura_cursos(
                            asignatura_id, cursos_id)
                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                asignatura_id = form.instance.plan_clase.asignatura.pk
                cursos = form.instance.plan_clase.cursos.all()

                cursos_id = [curso.pk for curso in cursos]

                form.fields['destreza'].queryset = Destreza.objects\
                    .get_destrezas_by_asignatura_cursos(
                        asignatura_id, cursos_id)

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
        Return the total number of forms in this FormSet.
        Also adds an initial extra form only if there is no instance attached
        """
        if self.is_bound:
            return super().total_form_count()
        else:
            initial_forms = self.initial_form_count()

            # Considers the extra fields only if there is no instance
            if self.instance.pk:
                total_forms = max(initial_forms, self.min_num)
            else:
                total_forms = max(initial_forms, self.min_num) + self.extra
            # Allow all existing related objects/inlines to be displayed,
            # but don't allow extra beyond max_num.
            if initial_forms > self.max_num >= 0:
                total_forms = initial_forms
            elif total_forms > self.max_num >= 0:
                total_forms = self.max_num
        return total_forms


# Creación del formset para ElementoCurricular
ElementoCurricularFormset = inlineformset_factory(
    PlanClase,
    ElementoCurricular,
    fields=('destreza', 'conocimientos_asociados',
            'actividades_evaluacion'),
    formset=BaseElementoCurricularFormset,
    max_num=10,
    extra=1,
)
