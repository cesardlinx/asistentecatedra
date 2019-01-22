import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ElementoCurricularFormset, PlanClaseForm
from .models.plan_clase import PlanClase
from .models.destreza import Destreza
from .models.indicador import Indicador
from .models.objetivo import Objetivo
from .models.asignatura import Asignatura
from .models.objetivo_general import ObjetivoGeneral
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class PlanificacionesTemplateView(LoginRequiredMixin, TemplateView):
    """Vista para elegir el tipo de planificación"""
    template_name = 'planificaciones/planificaciones.html'


class PlanClaseListView(LoginRequiredMixin, ListView):
    """Vista para listado de planes de clase"""
    template_name = 'planificaciones/planificacion_list.html'
    queryset = PlanClase.objects.all()
    context_object_name = 'planes'


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

            plan_clase = form.save(commit=False)
            plan_clase.elaborado_por = request.user
            plan_clase.save()
            form._save_m2m()

            if plan_clase:
                elementos_formset = ElementoCurricularFormset(
                    request.POST, instance=plan_clase)
                if elementos_formset.is_valid():
                    elemento_curricular = elementos_formset.save()
                    return redirect('home')

    context = {
        'form': form,
        'elementos_formset': elementos_formset,
    }
    return render(request, 'planificaciones/plan_clase_form.html', context)


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
            plan_clase = form.save(commit=False)
            plan_clase.updated_at = timezone.now()
            plan_clase.save()
            elementos_formset.save()
            form._save_m2m()
            return redirect('home')

    context = {
        'form': form,
        'elementos_formset': elementos_formset,
    }
    return render(request, 'planificaciones/plan_clase_form.html', context)


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
        return HttpResponse('Not Allowed.')


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
        return HttpResponse('Not Allowed.')
