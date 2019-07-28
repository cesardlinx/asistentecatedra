import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DeleteView
from django.views.generic.list import ListView

from planificaciones.forms.elemento_curricular_formset import \
    ElementoCurricularFormset
from planificaciones.forms.plan_clase_form import PlanClaseForm

from planificaciones.models.elemento_curricular import ElementoCurricular
from planificaciones.models.plan_clase import PlanClase

logger = logging.getLogger(__name__)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Planes de Clase'
        context['type'] = 'clase'
        return context


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
        'title': 'Nuevo Plan de Clase'
    }
    return render(request, 'planificaciones/forms/plan_clase_form.html',
                  context)


@login_required
def plan_clase_update(request, pk, slug):
    """Vista para la edición de planes de clase"""
    plan_clase = get_object_or_404(PlanClase, pk=pk, slug=slug)

    # Checks if the plan belongs to the user
    if plan_clase.elaborado_por != request.user:
        return redirect('plan_clase_list')

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
        'title': 'Plan de Clase: {}'.format(plan_clase.name)
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
        plan_clase = get_object_or_404(PlanClase, pk=kwargs['pk'])

        # Checks if the plan belongs to the user
        if plan_clase.elaborado_por != request.user:
            return redirect('plan_clase_list')

        messages.success(request, 'Plan de clase eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class PlanClaseDuplicateView(LoginRequiredMixin, View):
    """Vista para realizar una copia de un plan de clase"""

    def post(self, request, *args, **kwargs):
        plan_clase = get_object_or_404(PlanClase, pk=kwargs['pk'])
        # Checks if the plan belongs to the user
        if plan_clase.elaborado_por != request.user:
            return redirect('plan_clase_list')

        with transaction.atomic():
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
                procesos = elemento.procesos_didacticos.all()
                elemento.pk = None
                elemento.plan_clase = plan_clase
                elemento.save()
                for proceso in procesos:
                    proceso.pk = None
                    proceso.elemento_curricular = elemento
                    proceso.save()
        messages.success(request, 'Plan de clase duplicado exitosamente.')
        return redirect('plan_clase_list')
