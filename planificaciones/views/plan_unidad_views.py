import logging

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DeleteView, DetailView
from django.views.generic.list import ListView
from django_xhtml2pdf.views import PdfMixin

from planificaciones.forms.actividad_aprendizaje_formset import \
    ActividadAprendizajeFormset
from planificaciones.forms.plan_unidad_form import PlanUnidadForm
from planificaciones.mixins import UserIsPremiumMixin
from planificaciones.models.actividad_aprendizaje import ActividadAprendizaje
from planificaciones.models.plan_unidad import PlanUnidad

logger = logging.getLogger(__name__)


""" PLANES DE UNIDAD"""


class PlanUnidadListView(UserIsPremiumMixin, ListView):
    """Vista para listado de planes de unidad"""
    template_name = 'planificaciones/planificacion_list.html'
    ordering = '-updated_at'
    context_object_name = 'planes'

    def get_queryset(self):
        queryset = PlanUnidad.objects.filter(elaborado_por=self.request.user)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Planificaciones de Unidad Didáctica'
        context['type'] = 'unidad'
        return context


class PlanUnidadCreateView(UserIsPremiumMixin, View):
    """Vista para la creación de planes de unidad"""

    def get(self, request, *args, **kwargs):
        form = PlanUnidadForm()
        actividades_formset = ActividadAprendizajeFormset(
            prefix='actividades_aprendizaje')

        context = {
            'form': form,
            'actividades_formset': actividades_formset,
            'title': 'Nuevo Plan de Unidad'
        }
        return render(request, 'planificaciones/forms/plan_unidad_form.html',
                      context)

    def post(self, request, *args, **kwargs):

        form = PlanUnidadForm(request.POST)
        actividades_formset = ActividadAprendizajeFormset(
            request.POST, prefix='actividades_aprendizaje')

        if form.is_valid() and actividades_formset.is_valid():

            with transaction.atomic():
                plan_unidad = form.save(commit=False)
                plan_unidad.elaborado_por = request.user
                plan_unidad.save()
                form._save_m2m()
                # Almacenado del formset
                actividades_formset.instance = plan_unidad
                actividades_formset.save()
                logger.info('Plan de unidad created for the user: {}.'
                            .format(request.user.email))
                messages.success(request,
                                 'Plan de Unidad creado exitosamente.')
                return redirect('plan_unidad_list')
        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

        context = {
            'form': form,
            'actividades_formset': actividades_formset,
            'title': 'Nuevo Plan de Unidad'
        }
        return render(request, 'planificaciones/forms/plan_unidad_form.html',
                      context)


class PlanUnidadUpdateView(UserIsPremiumMixin, View):
    """Vista para la edición de planes de unidad"""

    def get(self, request, *args, **kwargs):
        plan_unidad = get_object_or_404(PlanUnidad, pk=kwargs['pk'],
                                        slug=kwargs['slug'])
        # Checks if the plan belongs to the user
        if plan_unidad.elaborado_por != request.user:
            return redirect('plan_unidad_list')

        form = PlanUnidadForm(instance=plan_unidad)
        actividades_formset = ActividadAprendizajeFormset(
            instance=plan_unidad)

        context = {
            'form': form,
            'actividades_formset': actividades_formset,
            'title': 'Plan de Unidad: {}'.format(plan_unidad.name)
        }
        return render(request, 'planificaciones/forms/plan_unidad_form.html',
                      context)

    def post(self, request, *args, **kwargs):
        plan_unidad = get_object_or_404(PlanUnidad, pk=kwargs['pk'],
                                        slug=kwargs['slug'])
        # Checks if the plan belongs to the user
        if plan_unidad.elaborado_por != request.user:
            return redirect('plan_unidad_list')

        form = PlanUnidadForm(request.POST, instance=plan_unidad)
        actividades_formset = ActividadAprendizajeFormset(
            request.POST, instance=plan_unidad)
        if form.is_valid() and actividades_formset.is_valid():

            with transaction.atomic():
                plan_unidad = form.save(commit=False)
                plan_unidad.updated_at = timezone.now()
                plan_unidad.save()
                actividades_formset.save()
                form._save_m2m()
                logger.info('Plan de unidad updated for the user: {}.'
                            .format(request.user.email))
                messages.success(
                    request, 'Plan de Unidad actualizado exitosamente.')
                return redirect('plan_unidad_list')

        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

        context = {
            'form': form,
            'actividades_formset': actividades_formset,
            'title': 'Plan de Unidad: {}'.format(plan_unidad.name)
        }
        return render(request, 'planificaciones/forms/plan_unidad_form.html',
                      context)


class PlanUnidadDeleteView(UserIsPremiumMixin, DeleteView):
    """Vista para borrar un plan de unidad"""
    model = PlanUnidad
    success_url = reverse_lazy('plan_unidad_list')

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def delete(self, request, *args, **kwargs):
        plan_unidad = get_object_or_404(PlanUnidad, pk=kwargs['pk'])

        # Checks if the plan belongs to the user
        if plan_unidad.elaborado_por != request.user:
            return redirect('plan_unidad_list')

        messages.success(request, 'Plan de Unidad eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class PlanUnidadDuplicateView(UserIsPremiumMixin, View):
    """Vista para realizar una copia de un plan de unidad"""

    def post(self, request, *args, **kwargs):
        plan_unidad = get_object_or_404(PlanUnidad, pk=kwargs['pk'])
        # Checks if the plan belongs to the user
        if plan_unidad.elaborado_por != request.user:
            return redirect('plan_unidad_list')

        with transaction.atomic():
            actividades_aprendizaje = ActividadAprendizaje.objects.filter(
                plan_unidad=plan_unidad
            )
            objetivos_old = plan_unidad.objetivos.all()
            objetivos_generales_old = plan_unidad\
                .objetivos_generales.all()
            plan_unidad.pk = None
            plan_unidad.id = None
            new_name = '{} (copia)'.format(plan_unidad.name)
            counter = 1
            while PlanUnidad.objects.filter(name=new_name).exists():
                counter += 1
                new_name = '{0} (copia {1})'.format(plan_unidad.name, counter)
            plan_unidad.name = new_name
            plan_unidad.save()
            plan_unidad.objetivos.set(objetivos_old)
            plan_unidad.objetivos_generales.set(objetivos_generales_old)

            for actividad_aprendizaje in actividades_aprendizaje:
                destrezas = actividad_aprendizaje.destrezas.all()
                actividad_aprendizaje.pk = None
                actividad_aprendizaje.plan_unidad = plan_unidad
                actividad_aprendizaje.save()
                actividad_aprendizaje.destrezas.set(destrezas)

        messages.success(request, 'Plan de Unidad duplicado exitosamente.')
        return redirect('plan_unidad_list')


class PlanUnidadPdfView(UserIsPremiumMixin, PdfMixin, DetailView):
    model = PlanUnidad
    template_name = "planificaciones/pdfs/plan_unidad_pdf.html"
    context_object_name = 'plan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['school_logo'] = self.request.user.get_logo
        context['school_name'] = self.request.user.institution
        if self.object.asignatura.name == 'Lengua y Literatura':
            context['subunidades'] = self.object.unidad.titulo.split(';')
        return context
