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
from .forms import ElementoCurricularFormset, PlanClaseForm
from .models.asignatura import Asignatura
from .models.destreza import Destreza
from .models.elemento_curricular import ElementoCurricular
from .models.indicador import Indicador
from .models.objetivo import Objetivo
from .models.objetivo_general import ObjetivoGeneral
from .models.plan_clase import PlanClase

logger = logging.getLogger(__name__)


class PlanificacionesTemplateView(LoginRequiredMixin, TemplateView):
    """Vista para elegir el tipo de planificación"""
    template_name = 'planificaciones/planificaciones.html'


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
                indicadores = elemento.indicadores_logro.all()
                procesos = elemento.procesos_didacticos.all()
                elemento.pk = None
                elemento.plan_clase = plan_clase
                elemento.save()
                elemento.indicadores_logro.set(indicadores)
                for proceso in procesos:
                    proceso.pk = None
                    proceso.elemento_curricular = elemento
                    proceso.save()
        messages.success(request, 'Plan de clase duplicado exitosamente.')
        return redirect('plan_clase_list')


@login_required
def load_cursos(request):
    """Regresa los cursos por asignatura si la solicitud fue via ajax"""
    asignatura_id = request.GET.get('asignatura')
    if request.is_ajax():
        asignatura = Asignatura.objects.get(pk=asignatura_id)
        cursos = asignatura.cursos.all()
        context = {'cursos': cursos}
        return render(
            request, 'planificaciones/ajax/cursos_checklist_options.html',
            context)
    else:
        return HttpResponse('')


@login_required
def load_objetivos(request):
    """Regresa los objetivos por asignatura y cursos si la solicitud
    fue via ajax"""
    response = {}
    asignatura_id = request.GET.get('asignatura')
    cursos_id = request.GET.getlist('cursos[]')

    if asignatura_id and cursos_id and request.is_ajax():
        objetivos = Objetivo.objects.get_objetivos_by_asignatura_cursos(
            asignatura_id, cursos_id)
        objetivos_generales = ObjetivoGeneral.objects\
            .get_objetivos_generales_by_asignatura_cursos(
                asignatura_id, cursos_id)

        list_objetivos = []
        list_objetivos_generales = []
        for objetivo in objetivos:
            list_objetivos.append(model_to_dict(objetivo))

        for objetivo_general in objetivos_generales:
            list_objetivos_generales.append(model_to_dict(objetivo_general))

        response['objetivos'] = list_objetivos
        response['objetivos_generales'] = list_objetivos_generales

        return JsonResponse(json.dumps(response), status=200, safe=False)
    else:
        return JsonResponse(json.dumps({'allowed': False}), status=200,
                            safe=False)


@login_required
def load_destrezas(request):
    """Regresa las destrezas por asignatura y cursos si la solicitud
    fue via ajax"""
    asignatura_id = request.GET.get('asignatura')
    cursos_id = request.GET.getlist('cursos[]')

    if asignatura_id and cursos_id and request.is_ajax():
        destrezas = Destreza.objects.get_destrezas_by_asignatura_cursos(
            asignatura_id, cursos_id)
        context = {'destrezas': destrezas}
        return render(
            request, 'planificaciones/ajax/destrezas_select_options.html',
            context)
    else:
        return HttpResponse('<option>---------</option>')


@login_required
def load_indicadores(request):
    """Regresa los indicadores por destreza si la solicitud fue via ajax"""
    destreza_id = request.GET.get('destreza')
    numero_fila = request.GET.get('numero_fila')

    if destreza_id and request.is_ajax():
        indicadores = Indicador.objects.get_indicadores_by_destreza(
            destreza_id)
        context = {'indicadores': indicadores, 'numero_fila': numero_fila}
        return render(
            request, 'planificaciones/ajax/indicadores_checklist_options.html',
            context)
    else:
        return HttpResponse('')
