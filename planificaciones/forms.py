from .models.curso import Curso
from .models.destreza import Destreza
from .models.indicador import Indicador
from .models.objetivo import Objetivo
from .models.asignatura import Asignatura
from .models.objetivo_general import ObjetivoGeneral
from .models.criterio_evaluacion import CriterioEvaluacion
from .models.plan_clase import PlanClase
from .models.plan_anual import PlanAnual
from .models.desarrollo_unidad import DesarrolloUnidad
from .models.unidad import Unidad
from .models.plan_unidad import PlanUnidad
from .models.plan_destrezas import PlanDestrezas
from .models.elemento_curricular import ElementoCurricular
from .models.proceso_didactico import ProcesoDidactico
from .models.actividad_aprendizaje import ActividadAprendizaje
from django import forms
from django.http import QueryDict
from django.forms import BaseInlineFormSet, inlineformset_factory
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
    fields=('destreza', 'conocimientos_asociados', 'indicadores_logro',
            'actividades_evaluacion'),
    widgets={
        'indicadores_logro': EnhancedCheckboxSelectMultiple,
    },
    formset=BaseElementoCurricularFormset,
    max_num=10,
    extra=1,
)


class PlanAnualForm(forms.ModelForm):
    """ModelForm para el Plan Anual"""
    class Meta:
        model = PlanAnual
        fields = [
            'name',
            'ano_lectivo',
            'docentes',
            'asignatura',
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


class PlanUnidadForm(forms.ModelForm):
    """ModelForm para el Plan de Unidad"""
    class Meta:
        model = PlanUnidad
        fields = [
            'name',
            'ano_lectivo',
            'docentes',
            'asignatura',
            'curso',
            'paralelos',
            'unidad',
            'objetivos',
            'objetivos_generales',
            'periodos',
            'tiempo',
            'necesidad_adaptacion',
            'adaptacion_curricular',
            'aprobado_por',
            'revisado_por',
        ]
        labels = {
            'name': 'Nombre de la Planificación de Unidad',
            'ano_lectivo': 'Año Lectivo',
            'docentes': 'Docente/s',
            'periodos': 'Períodos',
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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicialización de campos
        self.fields['curso'].queryset = Curso.objects.none()
        self.fields['unidad'].queryset = Unidad.objects.none()
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

                unidades = Unidad.objects\
                    .get_unidades_by_asignatura_curso(
                        asignatura_id, curso_id)

                self.fields['unidad'].queryset = unidades

            except (ValueError, TypeError):
                # invalid input from the client; ignore and fallback
                # to empty Unidad queryset
                pass

        elif self.instance.pk:
            asignatura_id = self.instance.asignatura.pk
            curso_id = self.instance.curso.pk

            unidades = Unidad.objects\
                .get_unidades_by_asignatura_curso(
                    asignatura_id, curso_id)

            self.fields['unidad'].queryset = unidades

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


class BaseActividadAprendizajeFormset(BaseInlineFormSet):
    """
    Clase que sirve de base para el inline formset
    de Actividades de Aprendizaje
    """

    def __init__(self, *args, **kwargs):
        """Inicializa los queryset de destrezas e indicadores en none
        se encarga de que reconozca los id provistos por el usuario
        en instancias"""
        super().__init__(*args, **kwargs)

        # Inicializa los queryset de los querysets en none
        # self.forms son el set de formularios del formset
        for idx, form in enumerate(self.forms):

            # La siguiente linea hace que todos los campos sean obligatorios
            form.empty_permitted = False

            form.fields['indicadores'].queryset = Indicador.objects\
                .none()
            form.fields['destrezas'].queryset = Destreza.objects\
                .none()
            form.fields['criterios_evaluacion'].queryset = CriterioEvaluacion.\
                objects.none()

            # Para convertir el id de destreza en una instancia de
            # Destreza en el formset
            if 'asignatura' in form.data and 'curso' in form.data:
                try:
                    asignatura_id = int(form.data.get('asignatura'))
                    curso_id = int(form.data.get('curso'))

                    cursos_id = [curso_id, ]

                    form.fields['destrezas'].queryset = Destreza.objects\
                        .get_destrezas_by_asignatura_cursos(
                            asignatura_id, cursos_id)

                except (ValueError, TypeError):
                    pass
            elif form.instance.pk:
                asignatura_id = form.instance.plan_anual.asignatura.pk
                curso_id = form.instance.plan_anual.curso.pk

                cursos_id = [curso_id, ]

                form.fields['destrezas'].queryset = Destreza.objects\
                    .get_destrezas_by_asignatura_cursos(
                    asignatura_id, cursos_id)

            # Para convertir el id de criterio en una instancia de
            # CriterioEvaluacion en el formset
            if 'actividades_aprendizaje-{}-destrezas'.format(idx) in form.data:
                try:
                    if isinstance(self.data, QueryDict):
                        destrezas_id = list(self.data.getlist(
                            'actividades_aprendizaje-{}-destrezas'
                            .format(idx)))
                    else:
                        destrezas_id = list(self.data.get(
                            'actividades_aprendizaje-{}-destrezas'
                            .format(idx)))

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
            if 'actividades_aprendizaje-{}-criterios_evaluacion'.format(idx)\
                    in form.data:
                try:
                    if isinstance(self.data, QueryDict):
                        criterios_id = list(self.data.getlist(
                            'actividades_aprendizaje-{}-criterios_evaluacion'
                            .format(idx)))
                    else:
                        criterios_id = list(self.data.get(
                            'actividades_aprendizaje-{}-criterios_evaluacion'
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


# Creación del formset para ActividadAprendizajeF
ActividadAprendizajeFormset = inlineformset_factory(
    PlanUnidad,
    ActividadAprendizaje,
    fields=('destrezas', 'criterios_evaluacion', 'estrategias_metodologicas',
            'recursos', 'indicadores', 'instrumentos_evaluacion'),
    widgets={
        'destrezas': EnhancedCheckboxSelectMultiple,
        'criterios_evaluacion': EnhancedCheckboxSelectMultiple,
        'indicadores': EnhancedCheckboxSelectMultiple,
    },
    formset=BaseActividadAprendizajeFormset,
    max_num=10,
    extra=1,
)


class PlanDestrezasForm(forms.ModelForm):
    """ModelForm para el Plan de Unidad"""
    class Meta:
        model = PlanDestrezas
        fields = [
            'name',
            'ano_lectivo',
            'docentes',
            'asignatura',
            'curso',
            'paralelos',
            'unidad',
            'objetivos',
            'objetivos_generales',
            'destrezas',
            'criterios_evaluacion',
            'indicadores',
            'periodos',
            'semana_inicio',
            'ejes_transversales',
            'estrategias_metodologicas',
            'recursos',
            'indicadores',
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
            'periodos': 'Períodos',
            'semana_inicio': 'Semana de Inicio',
            'indicadores': 'Indicadores de logro',
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
        self.fields['criterios_evaluacion'].queryset = \
            CriterioEvaluacion.objects.none()
        self.fields['indicadores'].queryset = Indicador.objects.none()

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

        # Para convertir el id de criterio en una instancia de
        # CriterioEvaluacion en el formset
        if 'destrezas' in self.data:
            try:
                if isinstance(self.data, QueryDict):
                    destrezas_id = list(self.data.getlist('destrezas'))
                else:
                    destrezas_id = list(self.data.get('destrezas'))

                self.fields['criterios_evaluacion'].queryset = \
                    CriterioEvaluacion.objects.get_criterios_by_destrezas(
                        destrezas_id
                )
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            destrezas = self.instance.destrezas.all()
            destrezas_id = [destreza.pk for destreza in destrezas]
            self.fields['criterios_evaluacion'].queryset = \
                CriterioEvaluacion.objects.get_criterios_by_destrezas(
                    destrezas_id
            )

        # Para convertir el id de indicador en una instancia de
        # Indicador en el formset
        if 'criterios_evaluacion' in self.data:
            try:
                if isinstance(self.data, QueryDict):
                    criterios_id = list(self.data
                                        .getlist('criterios_evaluacion'))
                else:
                    criterios_id = list(self.data
                                        .get('criterios_evaluacion'))

                self.fields['indicadores'].queryset = \
                    Indicador.objects.get_indicadores_by_criterios(
                        criterios_id
                )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            criterios = self.instance.criterios_evaluacion.all()

            criterios_id = [criterio.pk for criterio in criterios]

            self.fields['indicadores'].queryset = \
                Indicador.objects.get_indicadores_by_criterios(
                    criterios_id
            )
