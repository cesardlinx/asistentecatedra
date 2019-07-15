from planificaciones.models.destreza import Destreza
from planificaciones.models.indicador import Indicador
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.criterio_evaluacion import CriterioEvaluacion
from planificaciones.models.plan_anual import PlanAnual
from planificaciones.models.desarrollo_unidad import DesarrolloUnidad
from planificaciones.models.unidad import Unidad
from django.http import QueryDict
from django.forms import BaseInlineFormSet, inlineformset_factory
from planificaciones.widgets import EnhancedCheckboxSelectMultiple


class BaseDesarrolloUnidadFormset(BaseInlineFormSet):
    """
    Clase que sirve de base para el inline formset de Desarrollo de Unidad
    """

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

            form.fields['unidad'].queryset = Unidad.objects.none()
            form.fields['unidad'].empty_label = 'Elija una unidad.'

            form.fields['indicadores'].queryset = Indicador.objects\
                .none()
            form.fields['destrezas'].queryset = Destreza.objects\
                .none()
            form.fields['criterios_evaluacion'].queryset = CriterioEvaluacion.\
                objects.none()
            form.fields['objetivos'].queryset = Objetivo.objects\
                .none()
            form.fields['objetivos_generales'].queryset = ObjetivoGeneral.\
                objects.none()

            # Para convertir el id de destreza en una instancia de
            # Destreza en el formset
            if 'asignatura' in form.data and 'curso' in form.data:
                try:
                    asignatura_id = int(form.data.get('asignatura'))
                    curso_id = int(form.data.get('curso'))

                    cursos_id = [curso_id, ]

                    form.fields['unidad'].queryset = Unidad.objects\
                        .get_unidades_by_asignatura_curso(
                            asignatura_id, curso_id)
                    form.fields['destrezas'].queryset = Destreza.objects\
                        .get_destrezas_by_asignatura_cursos(
                            asignatura_id, cursos_id)

                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                asignatura_id = form.instance.plan_anual.asignatura.pk
                curso_id = form.instance.plan_anual.curso.pk

                cursos_id = [curso_id, ]

                form.fields['unidad'].queryset = Unidad.objects\
                    .get_unidades_by_asignatura_curso(
                    asignatura_id, curso_id)
                form.fields['destrezas'].queryset = Destreza.objects\
                    .get_destrezas_by_asignatura_cursos(
                    asignatura_id, cursos_id)

            # Para convertir el id de objetivo en una instancia de Objetivo
            # u ObjetivoGeneral en el formset
            if 'desarrollo_unidades-{}-unidad'.format(idx) in form.data:
                try:
                    unidad_id = int(form.data.get(
                        'desarrollo_unidades-{}-unidad'.format(idx)))
                    unidad = Unidad.objects.get(pk=unidad_id)
                    form.fields['objetivos'].queryset = unidad.objetivos.all()
                    form.fields['objetivos_generales'].queryset = unidad.\
                        objetivos_generales.all()

                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                unidad_id = form.instance.unidad.pk
                unidad = Unidad.objects.get(pk=unidad_id)
                form.fields['objetivos'].queryset = unidad.objetivos.all()
                form.fields['objetivos_generales'].queryset = unidad.\
                    objetivos_generales.all()

            # Para convertir el id de criterio en una instancia de
            # CriterioEvaluacion en el formset
            if 'desarrollo_unidades-{}-destrezas'.format(idx) in form.data:
                try:
                    if isinstance(self.data, QueryDict):
                        destrezas_id = list(self.data.getlist(
                            'desarrollo_unidades-{}-destrezas'.format(idx)))
                    else:
                        destrezas_id = list(self.data.get(
                            'desarrollo_unidades-{}-destrezas'.format(idx)))

                    form.fields['criterios_evaluacion'].queryset = \
                        CriterioEvaluacion.objects.get_criterios_by_destrezas(
                            destrezas_id
                    )
                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                destrezas = self.instance.destrezas.all()
                destrezas_id = [destreza.pk for destreza in destrezas]
                form.fields['criterios_evaluacion'].queryset = \
                    CriterioEvaluacion.objects.get_criterios_by_destrezas(
                        destrezas_id
                )

            # Para convertir el id de indicador en una instancia de
            # Indicador en el formset
            if 'desarrollo_unidades-{}-criterios_evaluacion'.format(idx)\
                    in form.data:
                try:
                    if isinstance(self.data, QueryDict):
                        criterios_id = list(self.data.getlist(
                            'desarrollo_unidades-{}-criterios_evaluacion'
                            .format(idx)))
                    else:
                        criterios_id = list(self.data.get(
                            'desarrollo_unidades-{}-criterios_evaluacion'
                            .format(idx)))

                    form.fields['indicadores'].queryset = \
                        Indicador.objects.get_indicadores_by_criterios(
                            criterios_id
                    )
                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                criterios = self.instance.criterios_evaluacion.all()

                criterios_id = [criterio.pk for criterio in criterios]

                form.fields['indicadores'].queryset = \
                    Indicador.objects.get_indicadores_by_criterios(
                        criterios_id
                )

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


# Creación del formset para DesarrolloUnidad
DesarrolloUnidadFormset = inlineformset_factory(
    PlanAnual,
    DesarrolloUnidad,
    fields=('unidad', 'objetivos', 'objetivos_generales', 'destrezas',
            'orientaciones_metodologicas', 'criterios_evaluacion',
            'indicadores', 'semanas'),
    widgets={
        'objetivos': EnhancedCheckboxSelectMultiple,
        'objetivos_generales': EnhancedCheckboxSelectMultiple,
        'destrezas': EnhancedCheckboxSelectMultiple,
        'criterios_evaluacion': EnhancedCheckboxSelectMultiple,
        'indicadores': EnhancedCheckboxSelectMultiple,
    },
    formset=BaseDesarrolloUnidadFormset,
    max_num=10,
    extra=1,
)
