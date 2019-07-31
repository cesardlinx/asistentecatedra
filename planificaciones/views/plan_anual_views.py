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

from planificaciones.forms.desarrollo_unidad_formset import \
    DesarrolloUnidadFormset
from planificaciones.forms.plan_anual_form import PlanAnualForm
from planificaciones.mixins import UserIsPremiumMixin
from planificaciones.models.desarrollo_unidad import DesarrolloUnidad
from planificaciones.models.plan_anual import PlanAnual

logger = logging.getLogger(__name__)


""" PLANES ANUALES"""


class PlanAnualListView(UserIsPremiumMixin, ListView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Planificaciones Curriculares Anuales'
        context['type'] = 'anual'
        return context


class PlanAnualCreateView(UserIsPremiumMixin, View):
    """Vista para la creación de planes anuales"""

    def get(self, request, *args, **kwargs):
        form = PlanAnualForm()
        unidades_formset = DesarrolloUnidadFormset(
            prefix='desarrollo_unidades')

        context = {
            'form': form,
            'unidades_formset': unidades_formset,
            'title': 'Nuevo Plan Anual'
        }
        return render(request, 'planificaciones/forms/plan_anual_form.html',
                      context)

    def post(self, request, *args, **kwargs):
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
            'title': 'Nuevo Plan Anual'
        }
        return render(request, 'planificaciones/forms/plan_anual_form.html',
                      context)


class PlanAnualUpdateView(UserIsPremiumMixin, View):
    """Vista para la edición de planes anuales"""

    def get(self, request, *args, **kwargs):
        plan_anual = get_object_or_404(PlanAnual, pk=kwargs['pk'],
                                       slug=kwargs['slug'])
        # Checks if the plan belongs to the user
        if plan_anual.elaborado_por != request.user:
            return redirect('plan_anual_list')

        form = PlanAnualForm(instance=plan_anual)
        unidades_formset = DesarrolloUnidadFormset(
            instance=plan_anual)

        context = {
            'form': form,
            'unidades_formset': unidades_formset,
            'title': 'Plan Anual: {}'.format(plan_anual.name)
        }
        return render(request, 'planificaciones/forms/plan_anual_form.html',
                      context)

    def post(self, request, *args, **kwargs):
        plan_anual = get_object_or_404(PlanAnual, pk=kwargs['pk'],
                                       slug=kwargs['slug'])
        # Checks if the plan belongs to the user
        if plan_anual.elaborado_por != request.user:
            return redirect('plan_anual_list')

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
            'title': 'Plan Anual: {}'.format(plan_anual.name)
        }
        return render(request, 'planificaciones/forms/plan_anual_form.html',
                      context)


class PlanAnualDeleteView(UserIsPremiumMixin, DeleteView):
    """Vista para borrar un plan anual"""
    model = PlanAnual
    success_url = reverse_lazy('plan_anual_list')

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def delete(self, request, *args, **kwargs):
        plan_anual = get_object_or_404(PlanAnual, pk=kwargs['pk'])

        # Checks if the plan belongs to the user
        if plan_anual.elaborado_por != request.user:
            return redirect('plan_anual_list')

        messages.success(request, 'Plan Anual eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class PlanAnualDuplicateView(UserIsPremiumMixin, View):
    """Vista para realizar una copia de un plan anual"""

    def post(self, request, *args, **kwargs):
        plan_anual = get_object_or_404(PlanAnual, pk=kwargs['pk'])
        # Checks if the plan belongs to the user
        if plan_anual.elaborado_por != request.user:
            return redirect('plan_anual_list')

        with transaction.atomic():
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
                desarrollo_unidad.pk = None
                desarrollo_unidad.plan_anual = plan_anual
                desarrollo_unidad.save()
                desarrollo_unidad.destrezas.set(destrezas)

        messages.success(request, 'Plan Anual duplicado exitosamente.')
        return redirect('plan_anual_list')


class PlanAnualPdfView(UserIsPremiumMixin, PdfMixin, DetailView):
    model = PlanAnual
    template_name = "planificaciones/pdfs/plan_anual_pdf.html"
    context_object_name = 'plan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['school_logo'] = self.request.user.get_logo
        context['school_name'] = self.request.user.institution
        ejes_transversales = self.object.ejes_transversales.split('\n')
        ejes_transversales = [eje.strip() for eje in ejes_transversales]
        context['ejes_transversales'] = ejes_transversales
        return context
