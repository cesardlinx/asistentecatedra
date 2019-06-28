import pytest
from django.urls import reverse, resolve
from planificaciones import views
from mixer.backend.django import mixer
from planificaciones.models.plan_clase import PlanClase
pytestmark = pytest.mark.django_db


class TestPlanificacionesUrls:
    def test_planificaciones(self):
        path = reverse('planificaciones')
        view = resolve(path)
        assert view.func.view_class == views.PlanificacionesTemplateView, \
            'Should resolve to the view PlanificacionesTemplateView'

    def test_plan_clase_list(self):
        path = reverse('plan_clase_list')
        view = resolve(path)
        assert view.func.view_class == views.PlanClaseListView, \
            'Should resolve to the view PlanClaseListView'

    def test_plan_clase_create(self):
        path = reverse('plan_clase_create')
        view = resolve(path)
        assert view.func == views.plan_clase_create, \
            'Should resolve to the view plan_clase_create'

    def test_plan_clase_update(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func == views.plan_clase_update, \
            'Should resolve to the view plan_clase_update'

    def test_plan_clase_delete(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanClaseDeleteView, \
            'Should resolve to the view PlanClaseDeleteView'

    def test_ajax_load_cursos(self):
        path = reverse('ajax_load_cursos')
        view = resolve(path)
        assert view.func == views.load_cursos, \
            'Should resolve to the view load_cursos'

    def test_ajax_load_objetivos(self):
        path = reverse('ajax_load_objetivos')
        view = resolve(path)
        assert view.func == views.load_objetivos, \
            'Should resolve to the view load_objetivos'

    def test_ajax_load_destrezas(self):
        path = reverse('ajax_load_destrezas')
        view = resolve(path)
        assert view.func == views.load_destrezas, \
            'Should resolve to the view load_destrezas'

    def test_ajax_load_indicadores(self):
        path = reverse('ajax_load_indicadores')
        view = resolve(path)
        assert view.func == views.load_indicadores, \
            'Should resolve to the view load_indicadores'
