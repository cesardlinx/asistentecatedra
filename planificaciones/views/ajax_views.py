import json
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from planificaciones.models.asignatura import Asignatura
from planificaciones.models.destreza import Destreza
from planificaciones.models.objetivo import Objetivo
from planificaciones.models.objetivo_general import ObjetivoGeneral
from planificaciones.models.unidad import Unidad

logger = logging.getLogger(__name__)


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

        if request.is_ajax():
            asignatura_id = request.GET.get('asignatura')
            cursos_id = request.GET.getlist('cursos[]')
            curso_id = request.GET.get('curso')
            numero_fila = request.GET.get('numero_fila')
            formset_name = request.GET.get('formset_name')

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
