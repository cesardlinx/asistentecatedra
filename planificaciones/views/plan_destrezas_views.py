import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DeleteView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django_xhtml2pdf.views import PdfMixin

from planificaciones.forms.plan_destrezas_form import PlanDestrezasForm
from planificaciones.models.plan_destrezas import PlanDestrezas

logger = logging.getLogger(__name__)


""" PLANES DE DESTREZAS"""


class PlanDestrezasListView(LoginRequiredMixin, ListView):
    """Vista para listado de planes de destrezas"""
    template_name = 'planificaciones/planificacion_list.html'
    ordering = '-updated_at'
    context_object_name = 'planes'
    paginate_by = 10

    def get_queryset(self):
        queryset = PlanDestrezas.objects.filter(
            elaborado_por=self.request.user)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Planificación de Destrezas'
        context['type'] = 'destrezas'
        return context


class PlanDestrezasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'planificaciones/forms/plan_destrezas_form.html'
    form_class = PlanDestrezasForm

    def form_valid(self, form):
        with transaction.atomic():
            plan_destrezas = form.save(commit=False)
            plan_destrezas.elaborado_por = self.request.user
            plan_destrezas.save()
            form._save_m2m()

        logger.info('Plan de destrezas created for the user: {}.'
                    .format(self.request.user.email))
        messages.success(self.request,
                         'Plan de Destrezas creado exitosamente.')
        return redirect('plan_destrezas_list')

    def form_invalid(self, form):
        messages.error(self.request,
                       'Por favor corrija los campos resaltados en rojo.')

        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Plan de Destrezas'
        return context


class PlanDestrezasUpdateView(LoginRequiredMixin, View):
    """Vista para la edición de planes de destrezas"""

    def get(self, request, *args, **kwargs):
        plan_destrezas = get_object_or_404(PlanDestrezas, pk=kwargs['pk'],
                                           slug=kwargs['slug'])
        # Checks if the plan belongs to the user
        if plan_destrezas.elaborado_por != request.user:
            return redirect('plan_destrezas_list')

        form = PlanDestrezasForm(instance=plan_destrezas)

        context = {
            'form': form,
            'title': 'Plan de Destrezas: {}'.format(plan_destrezas.name)
        }
        return render(request,
                      'planificaciones/forms/plan_destrezas_form.html',
                      context)

    def post(self, request, *args, **kwargs):
        plan_destrezas = get_object_or_404(PlanDestrezas, pk=kwargs['pk'],
                                           slug=kwargs['slug'])
        # Checks if the plan belongs to the user
        if plan_destrezas.elaborado_por != request.user:
            return redirect('plan_destrezas_list')

        form = PlanDestrezasForm(request.POST, instance=plan_destrezas)

        if form.is_valid():

            with transaction.atomic():
                plan_destrezas = form.save(commit=False)
                plan_destrezas.updated_at = timezone.now()
                plan_destrezas.save()
                form._save_m2m()
                logger.info('Plan de destrezas updated for the user: {}.'
                            .format(request.user.email))
                messages.success(
                    request, 'Plan de Destrezas actualizado exitosamente.')
                return redirect('plan_destrezas_list')

        messages.error(request,
                       'Por favor corrija los campos resaltados en rojo.')

        context = {
            'form': form,
            'title': 'Plan de Destrezas: {}'.format(plan_destrezas.name)
        }
        return render(request,
                      'planificaciones/forms/plan_destrezas_form.html',
                      context)


class PlanDestrezasDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para borrar un plan de destrezas"""
    model = PlanDestrezas
    success_url = reverse_lazy('plan_destrezas_list')

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def delete(self, request, *args, **kwargs):
        plan_destrezas = get_object_or_404(PlanDestrezas, pk=kwargs['pk'])

        # Checks if the plan belongs to the user
        if plan_destrezas.elaborado_por != request.user:
            return redirect('plan_destrezas_list')

        messages.success(request, 'Plan de Destrezas eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


class PlanDestrezasDuplicateView(LoginRequiredMixin, View):
    """Vista para realizar una copia de un plan de destrezas"""

    def post(self, request, *args, **kwargs):
        plan_destrezas = get_object_or_404(PlanDestrezas, pk=kwargs['pk'])
        # Checks if the plan belongs to the user
        if plan_destrezas.elaborado_por != request.user:
            return redirect('plan_destrezas_list')

        with transaction.atomic():
            objetivos_old = plan_destrezas.objetivos.all()
            objetivos_generales_old = plan_destrezas\
                .objetivos_generales.all()
            destrezas_old = plan_destrezas\
                .destrezas.all()
            plan_destrezas.pk = None
            plan_destrezas.id = None
            new_name = '{} (copia)'.format(plan_destrezas.name[:42])
            counter = 1
            while PlanDestrezas.objects.filter(name=new_name).exists():
                counter += 1
                tail_name = '(copia {})'.format(counter)
                new_name = '{0} {1}'.format(
                    plan_destrezas.name[:49 - len(tail_name)], tail_name)
            plan_destrezas.name = new_name
            plan_destrezas.save()
            plan_destrezas.objetivos.set(objetivos_old)
            plan_destrezas.objetivos_generales.set(objetivos_generales_old)
            plan_destrezas.destrezas.set(destrezas_old)

        messages.success(request, 'Plan de Destrezas duplicado exitosamente.')
        return redirect('plan_destrezas_list')


class PlanDestrezasPdfView(LoginRequiredMixin, PdfMixin, DetailView):
    model = PlanDestrezas
    template_name = "planificaciones/pdfs/plan_destrezas_pdf.html"
    context_object_name = 'plan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['school_logo'] = self.request.user.get_logo
        context['school_name'] = self.request.user.institution
        if self.object.asignatura.name == 'Lengua y Literatura':
            context['subunidades'] = self.object.unidad.titulo.split(';')
        return context
