import json
import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from planificaciones.forms.plan_clase_form import PlanClaseForm
from planificaciones.forms.plan_anual_form import PlanAnualForm
from planificaciones.forms.elemento_curricular_formset import \
    ElementoCurricularFormset
from planificaciones.forms.desarrollo_unidad_formset import \
    DesarrolloUnidadFormset
from .models.asignatura import Asignatura
from .models.destreza import Destreza
from .models.unidad import Unidad
from .models.elemento_curricular import ElementoCurricular
from .models.desarrollo_unidad import DesarrolloUnidad
from .models.indicador import Indicador
from .models.objetivo import Objetivo
from .models.objetivo_general import ObjetivoGeneral
from .models.criterio_evaluacion import CriterioEvaluacion
from .models.plan_clase import PlanClase
from .models.plan_anual import PlanAnual

logger = logging.getLogger(__name__)


class PlanificacionesTemplateView(LoginRequiredMixin, TemplateView):
    """Vista para elegir el tipo de planificación"""
    template_name = 'planificaciones/planificaciones.html'


""" PLANES DE CLASE"""


class PlanClaseListView(LoginRequiredMixin, ListView):
    """Vista para listado de planes de clase"""
    template_name = 'planificaciones/planificacion_list.html'
    ordering = '-updated_at'
    context_object_name = 'planes'

    def get_queryset(self):
        queryset = PlanClase.objects.filter(elaborado_por=self.request.user)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


@login_required
def plan_clase_create(request):
    """Vista para la creación de planes de clase"""
    if request.method == 'GET':
        form = PlanClaseForm()
        elementos_formset = ElementoCurricularFormset()
    elif request.method == 'POST':
        form = PlanClaseForm(request.POST)
        elementos_formset = ElementoCurricularFormset(
            request.POST)

        if form.is_valid() and elementos_formset.is_valid():

            with transaction.atomic():
                plan_clase = form.save(commit=False)
                plan_clase.elaborado_por = request.user
                plan_clase.save()
                form._save_m2m()
                # Almacenado del formset
                elementos_formset.instance = plan_clase
                elementos_formset.save()
                logger.info('Plan de clase created for the user: {}.'
                            .format(request.user.email))
                messages.success(request,
                                 'Plan de clase creado exitosamente.')
                return redirect('plan_clase_list')
        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

    context = {
        'form': form,
        'elementos_formset': elementos_formset,
    }
    return render(request, 'planificaciones/forms/plan_clase_form.html',
                  context)


@login_required
def plan_clase_update(request, pk, slug):
    """Vista para la edición de planes de clase"""
    plan_clase = get_object_or_404(PlanClase, pk=pk, slug=slug)

    if request.method == 'GET':
        form = PlanClaseForm(instance=plan_clase)
        elementos_formset = ElementoCurricularFormset(
            instance=plan_clase)
    elif request.method == 'POST':
        form = PlanClaseForm(request.POST, instance=plan_clase)
        elementos_formset = ElementoCurricularFormset(
            request.POST, instance=plan_clase)
        if form.is_valid() and elementos_formset.is_valid():

            with transaction.atomic():
                plan_clase = form.save(commit=False)
                plan_clase.updated_at = timezone.now()
                plan_clase.save()
                elementos_formset.save()
                form._save_m2m()
                logger.info('Plan de clase updated for the user: {}.'
                            .format(request.user.email))
                messages.success(
                    request, 'Plan de clase actualizado exitosamente.')
                return redirect('plan_clase_list')

        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

    context = {
        'form': form,
        'elementos_formset': elementos_formset,
    }
    return render(request, 'planificaciones/forms/plan_clase_form.html',
                  context)


class PlanClaseDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para borrar un plan de clase"""
    model = PlanClase
    success_url = reverse_lazy('plan_clase_list')

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Plan de clase eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class PlanClaseDuplicateView(LoginRequiredMixin, View):
    """Vista para realizar una copia de un plan de clase"""
    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            plan_clase = PlanClase.objects.get(pk=kwargs['pk'])
            elementos = ElementoCurricular.objects.filter(
                plan_clase=plan_clase
            )
            objetivos_old = plan_clase.objetivos.all()
            objetivos_generales_old = plan_clase.objetivos_generales.all()
            cursos_old = plan_clase.cursos.all()
            plan_clase.pk = None
            plan_clase.id = None
            new_name = '{} (copia)'.format(plan_clase.name)
            counter = 1
            while PlanClase.objects.filter(name=new_name).exists():
                counter += 1
                new_name = '{0} (copia {1})'.format(plan_clase.name, counter)
            plan_clase.name = new_name
            plan_clase.save()
            plan_clase.objetivos.set(objetivos_old)
            plan_clase.objetivos_generales.set(objetivos_generales_old)
            plan_clase.cursos.set(cursos_old)

            for elemento in elementos:
                indicadores = elemento.indicadores.all()
                procesos = elemento.procesos_didacticos.all()
                elemento.pk = None
                elemento.plan_clase = plan_clase
                elemento.save()
                elemento.indicadores.set(indicadores)
                for proceso in procesos:
                    proceso.pk = None
                    proceso.elemento_curricular = elemento
                    proceso.save()
        messages.success(request, 'Plan de clase duplicado exitosamente.')
        return redirect('plan_clase_list')


""" PLANES ANUALES"""


class PlanAnualListView(LoginRequiredMixin, ListView):
    """Vista para listado de planes anuales"""
    template_name = 'planificaciones/planificacion_list.html'
    ordering = '-updated_at'
    context_object_name = 'planes'

    def get_queryset(self):
        queryset = PlanAnual.objects.filter(elaborado_por=self.request.user)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


@login_required
def plan_anual_create(request):
    """Vista para la creación de planes anuales"""
    if request.method == 'GET':
        form = PlanAnualForm()
        unidades_formset = DesarrolloUnidadFormset(
            prefix='desarrollo_unidades')
    elif request.method == 'POST':
        form = PlanAnualForm(request.POST)
        unidades_formset = DesarrolloUnidadFormset(
            request.POST, prefix='desarrollo_unidades')

        if form.is_valid() and unidades_formset.is_valid():

            with transaction.atomic():
                plan_anual = form.save(commit=False)
                plan_anual.elaborado_por = request.user
                plan_anual.save()
                form._save_m2m()
                # Almacenado del formset
                unidades_formset.instance = plan_anual
                unidades_formset.save()
                logger.info('Plan anual created for the user: {}.'
                            .format(request.user.email))
                messages.success(request,
                                 'Plan Anual creado exitosamente.')
                return redirect('plan_anual_list')
        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

    context = {
        'form': form,
        'unidades_formset': unidades_formset,
    }
    return render(request, 'planificaciones/forms/plan_anual_form.html',
                  context)


@login_required
def plan_anual_update(request, pk, slug):
    """Vista para la edición de planes anuales"""
    plan_anual = get_object_or_404(PlanAnual, pk=pk, slug=slug)

    if request.method == 'GET':
        form = PlanAnualForm(instance=plan_anual)
        unidades_formset = DesarrolloUnidadFormset(
            instance=plan_anual)
    elif request.method == 'POST':
        form = PlanAnualForm(request.POST, instance=plan_anual)
        unidades_formset = DesarrolloUnidadFormset(
            request.POST, instance=plan_anual)
        if form.is_valid() and unidades_formset.is_valid():

            with transaction.atomic():
                plan_anual = form.save(commit=False)
                plan_anual.updated_at = timezone.now()
                plan_anual.save()
                unidades_formset.save()
                form._save_m2m()
                logger.info('Plan Anual updated for the user: {}.'
                            .format(request.user.email))
                messages.success(
                    request, 'Plan Anual actualizado exitosamente.')
                return redirect('plan_anual_list')

        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

    context = {
        'form': form,
        'unidades_formset': unidades_formset,
    }
    return render(request, 'planificaciones/forms/plan_anual_form.html',
                  context)


class PlanAnualDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para borrar un plan de anual"""
    model = PlanAnual
    success_url = reverse_lazy('plan_anual_list')

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Plan Anual eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class PlanAnualDuplicateView(LoginRequiredMixin, View):
    """Vista para realizar una copia de un plan de anual"""

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            plan_anual = PlanAnual.objects.get(pk=kwargs['pk'])
            desarrollo_unidades = DesarrolloUnidad.objects.filter(
                plan_anual=plan_anual
            )
            objetivos_old = plan_anual.objetivos_curso.all()
            objetivos_generales_old = plan_anual\
                .objetivos_generales_curso.all()
            objetivos_area_old = plan_anual.objetivos_generales.all()
            plan_anual.pk = None
            plan_anual.id = None
            new_name = '{} (copia)'.format(plan_anual.name)
            counter = 1
            while PlanAnual.objects.filter(name=new_name).exists():
                counter += 1
                new_name = '{0} (copia {1})'.format(plan_anual.name, counter)
            plan_anual.name = new_name
            plan_anual.save()
            plan_anual.objetivos_curso.set(objetivos_old)
            plan_anual.objetivos_generales_curso.set(objetivos_generales_old)
            plan_anual.objetivos_generales.set(objetivos_area_old)

            for desarrollo_unidad in desarrollo_unidades:
                destrezas = desarrollo_unidad.destrezas.all()
                criterios = desarrollo_unidad.criterios_evaluacion.all()
                indicadores = desarrollo_unidad.indicadores.all()
                desarrollo_unidad.pk = None
                desarrollo_unidad.plan_anual = plan_anual
                desarrollo_unidad.save()
                desarrollo_unidad.destrezas.set(destrezas)
                desarrollo_unidad.criterios_evaluacion.set(criterios)
                desarrollo_unidad.indicadores.set(indicadores)

        messages.success(request, 'Plan Anual duplicado exitosamente.')
        return redirect('plan_anual_list')


""" PLANES DE UNIDAD"""


class PlanUnidadListView(ListView):
    pass


def plan_unidad_create(request):
    pass


def plan_unidad_update(request):
    pass


class PlanUnidadDeleteView(DeleteView):
    pass


class PlanUnidadDuplicateView(View):
    pass


""" PLANES DE DESTREZAS"""


class PlanDestrezasListView(ListView):
    pass


def plan_destrezas_create(request):
    pass


def plan_destrezas_update(request):
    pass


class PlanDestrezasDeleteView(DeleteView):
    pass


class PlanDestrezasDuplicateView(View):
    pass


""" VISTAS AJAX """


class LoadCursosView(LoginRequiredMixin, View):
    """
    Regresa todos los cursos por asignatura
    """
    def get(self, request, *args, **kwargs):
        template = kwargs['template']
        asignatura_id = request.GET.get('asignatura')
        if request.is_ajax():
            asignatura = Asignatura.objects.get(pk=asignatura_id)
            cursos = asignatura.cursos.all()
            context = {'cursos': cursos}
            if template == 'checklist':
                return render(
                    request,
                    'planificaciones/ajax/cursos_checklist_options.html',
                    context)
            elif template == 'select':
                return render(
                    request, 'planificaciones/ajax/cursos_select_options.html',
                    context)
            else:
                return HttpResponse('')

        else:
            return HttpResponse('')


class LoadUnidadesView(LoginRequiredMixin, View):
    """
    Regresa las unidades por curso y asignatura
    """
    def get(self, request, *args, **kwargs):
        asignatura_id = request.GET.get('asignatura')
        curso_id = request.GET.get('curso')
        if request.is_ajax():
            unidades = Unidad.objects.filter(curso__id=curso_id,
                                             asignatura__id=asignatura_id)
            context = {'unidades': unidades}
            return render(
                request, 'planificaciones/ajax/unidades_select_options.html',
                context)
        else:
            return HttpResponse('')


class LoadObjetivosView(LoginRequiredMixin, View):
    """
    Regresa los objetivos por curso y asignatura
    si se lo llama con el parámetro curso
    """
    def get(self, request, *args, **kwargs):
        option = kwargs['option']
        response = {}
        asignatura_id = request.GET.get('asignatura')
        cursos_id = request.GET.getlist('cursos[]')
        curso_id = request.GET.get('curso')
        unidad_id = request.GET.get('unidad')

        if request.is_ajax():
            if curso_id and not cursos_id:
                cursos_id = [curso_id, ]

            if option == 'area' and asignatura_id:
                # Only general objectives
                asignatura = Asignatura.objects.get(pk=asignatura_id)
                objetivos_generales = ObjetivoGeneral.objects\
                    .filter(area=asignatura.area)

                response['objetivos_generales'] = [
                    model_to_dict(objetivo)
                    for objetivo in objetivos_generales]

                return JsonResponse(json.dumps(response),
                                    status=200, safe=False)

            elif option == 'curso' and asignatura_id and \
                    (curso_id or cursos_id):
                # only objectives based on signature and course
                objetivos = Objetivo.objects.\
                    get_objetivos_by_asignatura_cursos(asignatura_id,
                                                       cursos_id)
                objetivos_generales = ObjetivoGeneral.objects\
                    .get_objetivos_generales_by_asignatura_cursos(
                        asignatura_id, cursos_id)

                response['objetivos'] = [
                    model_to_dict(objetivo)
                    for objetivo in objetivos]
                response['objetivos_generales'] = [
                    model_to_dict(objetivo)
                    for objetivo in objetivos_generales]

                return JsonResponse(json.dumps(response),
                                    status=200, safe=False)

            elif option == 'unidad' and unidad_id:
                # return unit objectives
                unidad = Unidad.objects.get(pk=unidad_id)

                objetivos = unidad.objetivos.all()
                objetivos_generales = unidad.objetivos_generales.all()

                response['objetivos'] = [
                    model_to_dict(objetivo)
                    for objetivo in objetivos]
                response['objetivos_generales'] = [
                    model_to_dict(objetivo)
                    for objetivo in objetivos_generales]

                return JsonResponse(json.dumps(response),
                                    status=200, safe=False)

            else:
                return JsonResponse(json.dumps({'allowed': False}), status=200,
                                    safe=False)
        else:
            return JsonResponse(json.dumps({'allowed': False}), status=200,
                                safe=False)


class LoadDestrezasView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template = kwargs['template']
        formset_name = kwargs['formset']

        if request.is_ajax():
            asignatura_id = request.GET.get('asignatura')
            cursos_id = request.GET.getlist('cursos[]')
            curso_id = request.GET.get('curso')
            numero_fila = request.GET.get('numero_fila')

            if curso_id and not cursos_id:
                cursos_id = [curso_id, ]

            destrezas = Destreza.objects.get_destrezas_by_asignatura_cursos(
                asignatura_id, cursos_id)
            context = {'destrezas': destrezas,
                       'formset_name': formset_name,
                       'numero_fila': numero_fila}

            if template == 'checklist':
                return render(
                    request,
                    'planificaciones/ajax/destrezas_checklist_options.html',
                    context)
            elif template == 'select':
                return render(
                    request,
                    'planificaciones/ajax/destrezas_select_options.html',
                    context)
            else:
                return HttpResponse('')

        else:
            return HttpResponse('')


class LoadCriteriosView(LoginRequiredMixin, View):
    """
    Regresa los criterios de evaluación por destrezas
    """

    def get(self, request, *args, **kwargs):
        destrezas_id = request.GET.getlist('destrezas[]')
        formset_name = request.GET.get('formset_name')
        numero_fila = request.GET.get('numero_fila')

        if request.is_ajax():
            criterios = CriterioEvaluacion.objects.\
                get_criterios_by_destrezas(destrezas_id)
            context = {'criterios': criterios,
                       'formset_name': formset_name,
                       'numero_fila': numero_fila}
            return render(
                request,
                'planificaciones/ajax/criterios_checklist_options.html',
                context)
        else:
            return HttpResponse('')


class LoadIndicadoresView(LoginRequiredMixin, View):
    """
    Regresa los objetivos por curso y asignatura
    si se lo llama con el parámetro curso
    """

    def get(self, request, *args, **kwargs):
        option = kwargs['option']
        formset_name = kwargs['formset']
        destreza_id = request.GET.get('destreza')
        criterios_id = request.GET.getlist('criterios[]')
        numero_fila = request.GET.get('numero_fila')

        if request.is_ajax():
            if option == 'destreza' and destreza_id:
                # Indicadores por destrezas
                indicadores = Indicador.objects.get_indicadores_by_destreza(
                    destreza_id)
                context = {'indicadores': indicadores,
                           'numero_fila': numero_fila,
                           'formset_name': formset_name}
                return render(
                    request,
                    'planificaciones/ajax/indicadores_checklist_options.html',
                    context)

            elif option == 'criterio' and criterios_id:
                # Indicadores por criterios
                indicadores = Indicador.objects.get_indicadores_by_criterios(
                    criterios_id)
                context = {'indicadores': indicadores,
                           'numero_fila': numero_fila,
                           'formset_name': formset_name}
                return render(
                    request,
                    'planificaciones/ajax/indicadores_checklist_options.html',
                    context)
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')
