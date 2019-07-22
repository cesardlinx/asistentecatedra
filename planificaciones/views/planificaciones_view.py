import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


logger = logging.getLogger(__name__)


class PlanificacionesTemplateView(LoginRequiredMixin, TemplateView):
    """Vista para elegir el tipo de planificación"""
    template_name = 'planificaciones/planificaciones.html'
