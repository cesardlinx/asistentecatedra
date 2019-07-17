import pytest
from django.urls import reverse, resolve
from planificaciones import views
from mixer.backend.django import mixer
from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.plan_anual import PlanAnual
from planificaciones.models.plan_unidad import PlanUnidad
from planificaciones.models.plan_destrezas import PlanDestrezas
pytestmark = pytest.mark.django_db


class TestPlanificacionesUrls:
    def test_planificaciones(self):
        path = reverse('planificaciones')
        view = resolve(path)
        assert view.func.view_class == views.PlanificacionesTemplateView, \
            'Should resolve to the view PlanificacionesTemplateView'


class TestPlanClaseUrls:
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

    def test_plan_clase_duplicate(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanClaseDuplicateView, \
            'Should resolve to the view PlanClaseDuplicateView'


class TestPlanAnualUrls:
    def test_plan_anual_list(self):
        path = reverse('plan_anual_list')
        view = resolve(path)
        assert view.func.view_class == views.PlanAnualListView, \
            'Should resolve to the view PlanAnualListView'

    def test_plan_anual_create(self):
        path = reverse('plan_anual_create')
        view = resolve(path)
        assert view.func == views.plan_anual_create, \
            'Should resolve to the view plan_anual_create'

    def test_plan_anual_update(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func == views.plan_anual_update, \
            'Should resolve to the view plan_anual_update'

    def test_plan_anual_delete(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanAnualDeleteView, \
            'Should resolve to the view PlanAnualDeleteView'

    def test_plan_anual_duplicate(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanAnualDuplicateView, \
            'Should resolve to the view PlanAnualDuplicateView'


class TestPlanUnidadUrls:
    def test_plan_unidad_list(self):
        path = reverse('plan_unidad_list')
        view = resolve(path)
        assert view.func.view_class == views.PlanUnidadListView, \
            'Should resolve to the view PlanUnidadListView'

    def test_plan_unidad_create(self):
        path = reverse('plan_unidad_create')
        view = resolve(path)
        assert view.func == views.plan_unidad_create, \
            'Should resolve to the view plan_unidad_create'

    def test_plan_unidad_update(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func == views.plan_unidad_update, \
            'Should resolve to the view plan_unidad_update'

    def test_plan_unidad_delete(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanUnidadDeleteView, \
            'Should resolve to the view PlanUnidadDeleteView'

    def test_plan_unidad_duplicate(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanUnidadDuplicateView, \
            'Should resolve to the view PlanUnidadDuplicateView'


class TestPlanDestrezasUrls:
    def test_plan_destrezas_list(self):
        path = reverse('plan_destrezas_list')
        view = resolve(path)
        assert view.func.view_class == views.PlanDestrezasListView, \
            'Should resolve to the view PlanDestrezasListView'

    def test_plan_destrezas_create(self):
        path = reverse('plan_destrezas_create')
        view = resolve(path)
        assert view.func == views.plan_destrezas_create, \
            'Should resolve to the view plan_destrezas_create'

    def test_plan_destrezas_update(self):
        plan = mixer.blend(PlanDestrezas)
        path = reverse('plan_destrezas_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func == views.plan_destrezas_update, \
            'Should resolve to the view plan_destrezas_update'

    def test_plan_destrezas_delete(self):
        plan = mixer.blend(PlanDestrezas)
        path = reverse('plan_destrezas_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanDestrezasDeleteView, \
            'Should resolve to the view PlanDestrezasDeleteView'

    def test_plan_destrezas_duplicate(self):
        plan = mixer.blend(PlanDestrezas)
        path = reverse('plan_destrezas_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == views.PlanDestrezasDuplicateView, \
            'Should resolve to the view PlanDestrezasDuplicateView'


class TestAjaxUrls:
    def test_ajax_load_cursos(self):
        path = reverse('ajax_load_cursos', kwargs={'template': 'select'})
        view = resolve(path)
        assert view.func.view_class == views.LoadCursosView, \
            'Should resolve to the view load_cursos'

    def test_ajax_load_unidades(self):
        path = reverse('ajax_load_unidades')
        view = resolve(path)
        assert view.func.view_class == views.LoadUnidadesView, \
            'Should resolve to the view load_unidades'

    def test_ajax_load_objetivos(self):
        path = reverse('ajax_load_objetivos', kwargs={'option': 'area'})
        view = resolve(path)
        assert view.func.view_class == views.LoadObjetivosView, \
            'Should resolve to the view load_objetivos'

    def test_ajax_load_destrezas(self):
        path = reverse('ajax_load_destrezas',
                       kwargs={'template': 'select', 'formset': 'somename'})
        view = resolve(path)
        assert view.func.view_class == views.LoadDestrezasView, \
            'Should resolve to the view load_destrezas'

    def test_ajax_load_criterios(self):
        path = reverse('ajax_load_criterios')
        view = resolve(path)
        assert view.func.view_class == views.LoadCriteriosView, \
            'Should resolve to the view load_criterios'

    def test_ajax_load_indicadores(self):
        path = reverse('ajax_load_indicadores',
                       kwargs={'option': 'destreza', 'formset': 'somename'})
        view = resolve(path)
        assert view.func.view_class == views.LoadIndicadoresView, \
            'Should resolve to the view load_indicadores'

