import pytest
from django.urls import reverse, resolve
from mixer.backend.django import mixer

from planificaciones.models.plan_clase import PlanClase
from planificaciones.models.plan_anual import PlanAnual
from planificaciones.models.plan_unidad import PlanUnidad
from planificaciones.models.plan_destrezas import PlanDestrezas

from planificaciones.views.planificaciones_view import \
    PlanificacionesTemplateView
from planificaciones.views.plan_clase_views import (
    PlanClaseListView, plan_clase_create, plan_clase_update,
    PlanClaseDeleteView, PlanClaseDuplicateView, PlanClasePdfView)
from planificaciones.views.plan_anual_views import (
    PlanAnualListView, PlanAnualCreateView, PlanAnualUpdateView,
    PlanAnualDeleteView, PlanAnualDuplicateView, PlanAnualPdfView)
from planificaciones.views.plan_unidad_views import (
    PlanUnidadListView, PlanUnidadCreateView, PlanUnidadUpdateView,
    PlanUnidadDeleteView, PlanUnidadDuplicateView, PlanUnidadPdfView)
from planificaciones.views.plan_destrezas_views import (
    PlanDestrezasListView, PlanDestrezasCreateView, PlanDestrezasUpdateView,
    PlanDestrezasDeleteView, PlanDestrezasDuplicateView)
from planificaciones.views.ajax_views import (
    LoadCursosView, LoadDestrezasView,
    LoadObjetivosView, LoadUnidadesView)

pytestmark = pytest.mark.django_db


class TestPlanificacionesUrls:
    def test_planificaciones(self):
        path = reverse('planificaciones')
        view = resolve(path)
        assert view.func.view_class == PlanificacionesTemplateView, \
            'Should resolve to the view PlanificacionesTemplateView'


class TestPlanClaseUrls:
    def test_plan_clase_list(self):
        path = reverse('plan_clase_list')
        view = resolve(path)
        assert view.func.view_class == PlanClaseListView, \
            'Should resolve to the view PlanClaseListView'

    def test_plan_clase_create(self):
        path = reverse('plan_clase_create')
        view = resolve(path)
        assert view.func == plan_clase_create, \
            'Should resolve to the view plan_clase_create'

    def test_plan_clase_update(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func == plan_clase_update, \
            'Should resolve to the view plan_clase_update'

    def test_plan_clase_delete(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanClaseDeleteView, \
            'Should resolve to the view PlanClaseDeleteView'

    def test_plan_clase_duplicate(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanClaseDuplicateView, \
            'Should resolve to the view PlanClaseDuplicateView'


class TestPlanAnualUrls:
    def test_plan_anual_list(self):
        path = reverse('plan_anual_list')
        view = resolve(path)
        assert view.func.view_class == PlanAnualListView, \
            'Should resolve to the view PlanAnualListView'

    def test_plan_anual_create(self):
        path = reverse('plan_anual_create')
        view = resolve(path)
        assert view.func.view_class == PlanAnualCreateView, \
            'Should resolve to the view PlanAnualCreateView'

    def test_plan_anual_update(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func.view_class == PlanAnualUpdateView, \
            'Should resolve to the view PlanAnualUpdateView'

    def test_plan_anual_delete(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanAnualDeleteView, \
            'Should resolve to the view PlanAnualDeleteView'

    def test_plan_anual_duplicate(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanAnualDuplicateView, \
            'Should resolve to the view PlanAnualDuplicateView'


class TestPlanUnidadUrls:
    def test_plan_unidad_list(self):
        path = reverse('plan_unidad_list')
        view = resolve(path)
        assert view.func.view_class == PlanUnidadListView, \
            'Should resolve to the view PlanUnidadListView'

    def test_plan_unidad_create(self):
        path = reverse('plan_unidad_create')
        view = resolve(path)
        assert view.func.view_class == PlanUnidadCreateView, \
            'Should resolve to the view PlanUnidadCreateView'

    def test_plan_unidad_update(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func.view_class == PlanUnidadUpdateView, \
            'Should resolve to the view PlanUnidadUpdateView'

    def test_plan_unidad_delete(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanUnidadDeleteView, \
            'Should resolve to the view PlanUnidadDeleteView'

    def test_plan_unidad_duplicate(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanUnidadDuplicateView, \
            'Should resolve to the view PlanUnidadDuplicateView'


class TestPlanDestrezasUrls:
    def test_plan_destrezas_list(self):
        path = reverse('plan_destrezas_list')
        view = resolve(path)
        assert view.func.view_class == PlanDestrezasListView, \
            'Should resolve to the view PlanDestrezasListView'

    def test_plan_destrezas_create(self):
        path = reverse('plan_destrezas_create')
        view = resolve(path)
        assert view.func.view_class == PlanDestrezasCreateView, \
            'Should resolve to the view PlanDestrezasCreateView'

    def test_plan_destrezas_update(self):
        plan = mixer.blend(PlanDestrezas)
        path = reverse('plan_destrezas_update', kwargs={
            'pk': plan.id,
            'slug': plan.slug
        })
        view = resolve(path)
        assert view.func.view_class == PlanDestrezasUpdateView, \
            'Should resolve to the view PlanDestrezasUpdateView'

    def test_plan_destrezas_delete(self):
        plan = mixer.blend(PlanDestrezas)
        path = reverse('plan_destrezas_delete', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanDestrezasDeleteView, \
            'Should resolve to the view PlanDestrezasDeleteView'

    def test_plan_destrezas_duplicate(self):
        plan = mixer.blend(PlanDestrezas)
        path = reverse('plan_destrezas_duplicate', kwargs={
            'pk': plan.id
        })
        view = resolve(path)
        assert view.func.view_class == PlanDestrezasDuplicateView, \
            'Should resolve to the view PlanDestrezasDuplicateView'


class TestAjaxUrls:
    def test_ajax_load_cursos(self):
        path = reverse('ajax_load_cursos', kwargs={'template': 'select'})
        view = resolve(path)
        assert view.func.view_class == LoadCursosView, \
            'Should resolve to the view LoadCursosView'

    def test_ajax_load_unidades(self):
        path = reverse('ajax_load_unidades')
        view = resolve(path)
        assert view.func.view_class == LoadUnidadesView, \
            'Should resolve to the view LoadUnidadesView'

    def test_ajax_load_objetivos(self):
        path = reverse('ajax_load_objetivos', kwargs={'option': 'area'})
        view = resolve(path)
        assert view.func.view_class == LoadObjetivosView, \
            'Should resolve to the view LoadObjetivosView'

    def test_ajax_load_destrezas(self):
        path = reverse('ajax_load_destrezas',
                       kwargs={'template': 'select'})
        view = resolve(path)
        assert view.func.view_class == LoadDestrezasView, \
            'Should resolve to the view LoadDestrezasView'


class TestPdfUrls:
    def test_plan_clase_pdf(self):
        plan = mixer.blend(PlanClase)
        path = reverse('plan_clase_pdf',
                       kwargs={'pk': plan.pk})
        view = resolve(path)
        assert view.func.view_class == PlanClasePdfView, \
            'Should resolve to the view PlanClasePdfView'

    def test_plan_anual_pdf(self):
        plan = mixer.blend(PlanAnual)
        path = reverse('plan_anual_pdf',
                       kwargs={'pk': plan.pk})
        view = resolve(path)
        assert view.func.view_class == PlanAnualPdfView, \
            'Should resolve to the view PlanAnualPdfView'

    def test_plan_unidad_pdf(self):
        plan = mixer.blend(PlanUnidad)
        path = reverse('plan_unidad_pdf',
                       kwargs={'pk': plan.pk})
        view = resolve(path)
        assert view.func.view_class == PlanUnidadPdfView, \
            'Should resolve to the view PlanUnidadPdfView'
