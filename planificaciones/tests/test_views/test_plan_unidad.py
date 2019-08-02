from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError
from django.http.response import Http404
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from testfixtures import LogCapture

from accounts.tests.conftest import add_middleware_to_request
from planificaciones.models.plan_unidad import PlanUnidad
from planificaciones.models.actividad_aprendizaje import ActividadAprendizaje
from planificaciones.tests.planificaciones_testcase import \
    PlanificacionesTestCase

from planificaciones.views.plan_unidad_views import (
    PlanUnidadListView, PlanUnidadCreateView, PlanUnidadUpdateView,
    PlanUnidadDeleteView, PlanUnidadDuplicateView, PlanUnidadPdfView)

User = get_user_model()
pytestmark = pytest.mark.django_db


class PlanUnidadTestCase(PlanificacionesTestCase):
    def setUp(self):
        """Creates data for testing Planes de Unidad"""
        super().setUp()

        self.mock_stripe = patch('accounts.models.stripe')
        stripe = self.mock_stripe.start()
        stripe.Customer.create.return_value = {'id': '12345'}

        self.logger = LogCapture()

        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='David',
            last_name='Padilla',
            institution='Colegio Benalcazar',
            is_premium=True
        )

        self.data = {
            'name': 'Plan de Unidad1',
            'ano_lectivo': '2019-2020',
            'docentes': 'David Padilla',
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            'paralelos': 'A y C',
            'unidad': self.unidad_1.id,
            'objetivos': [self.objetivo_1.id, self.objetivo_2.id],
            'objetivos_generales': [self.general_1.id, self.general_2.id],
            'periodos': 20,
            'tiempo': 20,

            # Formset Elementos curriculares 1
            'actividades_aprendizaje-TOTAL_FORMS': '2',
            'actividades_aprendizaje-INITIAL_FORMS': '0',
            'actividades_aprendizaje-MIN_NUM_FORMS': '0',
            'actividades_aprendizaje-MAX_NUM_FORMS': '1000',
            'actividades_aprendizaje-0-destrezas': [
                self.destreza_1.id, self.destreza_2.id],
            'actividades_aprendizaje-0-estrategias_metodologicas':
            'lorem ipsum',
            'actividades_aprendizaje-0-recursos': 'lorem ipsum',
            'actividades_aprendizaje-0-instrumentos_evaluacion': 'lorem ipsum',

            'actividades_aprendizaje-1-destrezas': [
                self.destreza_1.id, self.destreza_2.id],
            'actividades_aprendizaje-1-estrategias_metodologicas':
            'lorem ipsum',
            'actividades_aprendizaje-1-recursos': 'lorem ipsum',
            'actividades_aprendizaje-1-instrumentos_evaluacion': 'lorem ipsum',
        }

        self.plan_unidad = mixer.blend(PlanUnidad, elaborado_por=self.user)

        another_user = mixer.blend(User, is_premium=True)
        self.another_plan = mixer.blend(PlanUnidad, elaborado_por=another_user)

        self.common_user = mixer.blend(User)

    def tearDown(self):
        self.logger.uninstall()


class TestPlanUnidadListView(PlanUnidadTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanUnidadListView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanUnidadListView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadListView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert 'planificaciones/planificacion_list.html' in \
            response.template_name, \
            'Template should be the one for listing planning'
        assert self.plan_unidad.name in response.rendered_content, \
            'Should contain the unit plan name'
        assert self.another_plan.name not in response.rendered_content, \
            'Should not contain others users plans'


class TestPlanUnidadCreateView(PlanUnidadTestCase):
    """Prueba la vista para la creación de planes de unidad"""

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanUnidadCreateView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanUnidadCreateView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadCreateView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        # Tempĺate Testing
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="ano_lectivo"')
        self.assertContains(response, 'name="docentes"')
        self.assertContains(response, 'name="asignatura"')
        self.assertContains(response, 'name="curso"')
        self.assertContains(response, 'name="paralelos"')
        self.assertContains(response, 'name="unidad"')
        self.assertContains(response, 'id="id_objetivos"')
        self.assertContains(response, 'id="id_objetivos_generales"')
        self.assertContains(response, 'name="periodos"')
        self.assertContains(response, 'name="tiempo"')
        self.assertContains(response, 'name="necesidad_adaptacion"')
        self.assertContains(response, 'name="adaptacion_curricular"')
        self.assertContains(response, 'name="aprobado_por"')
        self.assertContains(response, 'name="revisado_por"')

        # The title should be Nuevo Plan de Unidad
        self.assertContains(response, 'Nuevo Plan de Unidad')

    def test_post_success(self):
        """Prueba la creación de planes de unidad"""
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_unidad_create')
        response = self.client.post(url, self.data, follow=True)
        assert response.status_code == 200, 'Should return a success response'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Unidad creado exitosamente.', \
            'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_unidad_list'))

        self.plan_unidad.refresh_from_db()

        plan = PlanUnidad.objects.last()
        actividad_aprendizaje = ActividadAprendizaje.objects.last()
        assert plan.name == 'Plan de Unidad1', 'Should create a Plan de Unidad'
        assert actividad_aprendizaje.plan_unidad == plan, \
            'el elemento curricular debe pertenecer al plan de unidad'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan de unidad created for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan de Unidad is created.'

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""
        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanUnidadCreateView.as_view()(request)

        assert response.status_code == 200, 'Should get a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises ValidationError
        with pytest.raises(ValidationError):
            PlanUnidadCreateView.as_view()(request)


class TestPlanUnidadUpdateView(PlanUnidadTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanUnidadUpdateView.as_view()(
            request, pk=self.plan_unidad.pk, slug=self.plan_unidad.slug)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanUnidadUpdateView.as_view()(
            request, pk=self.plan_unidad.pk, slug=self.plan_unidad.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get_when_user_doesnt_own_plan(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadUpdateView.as_view()(
            request, pk=self.another_plan.pk, slug=self.another_plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_unidad_list')

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanUnidadUpdateView.as_view()(
            request, pk=self.another_plan.pk, slug=self.another_plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_unidad_list')

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        mixer.blend(ActividadAprendizaje, plan_unidad=self.plan_unidad)
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadUpdateView.as_view()(
            request, pk=self.plan_unidad.pk, slug=self.plan_unidad.slug)
        assert response.status_code == 200, 'Authenticated user can access'
        # Tempĺate Testing
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="ano_lectivo"')
        self.assertContains(response, 'name="docentes"')
        self.assertContains(response, 'name="asignatura"')
        self.assertContains(response, 'name="curso"')
        self.assertContains(response, 'name="paralelos"')
        self.assertContains(response, 'name="unidad"')
        self.assertContains(response, 'id="id_objetivos"')
        self.assertContains(response, 'id="id_objetivos_generales"')
        self.assertContains(response, 'name="periodos"')
        self.assertContains(response, 'name="tiempo"')
        self.assertContains(response, 'name="necesidad_adaptacion"')
        self.assertContains(response, 'name="adaptacion_curricular"')
        self.assertContains(response, 'name="aprobado_por"')
        self.assertContains(response, 'name="revisado_por"')

        # The title should be the planning name
        self.assertContains(response,
                            'Plan de Unidad: {}'.format(self.plan_unidad.name))

    def test_post_success(self):
        """Prueba la actualización de planes de unidad"""
        assert self.plan_unidad.name != 'Plan de Unidad1', \
            'El plan inicialmente tiene un nombre diferente'
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_unidad_update', kwargs={
            'pk': self.plan_unidad.pk, 'slug': self.plan_unidad.slug})
        response = self.client.post(url, self.data, follow=True)
        assert response.status_code == 200, 'Should return a success response'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Unidad actualizado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_unidad_list'))

        self.plan_unidad.refresh_from_db()
        assert self.plan_unidad.name == 'Plan de Unidad1', \
            'Debe actualizar el plan de unidad'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan de unidad updated for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan de Unidad is updated.'

    def test_invalid_plan(self):
        """Tests the view when sending invalid data about a plan"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises 404 Error
        with pytest.raises(Http404):
            PlanUnidadUpdateView.as_view()(request, pk=1, slug='test')

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""

        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanUnidadUpdateView.as_view()(
            request, pk=self.plan_unidad.pk, slug=self.plan_unidad.slug)

        assert response.status_code == 200, 'Should get a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        plan = mixer.blend(PlanUnidad)
        request = RequestFactory().post('/', data={})
        request.user = self.user
        response = PlanUnidadUpdateView.as_view()(
            request, pk=plan.pk, slug=plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_unidad_list')


class TestPlanUnidadDeleteView(PlanUnidadTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanUnidadDeleteView.as_view()(request,
                                                  pk=self.plan_unidad.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanUnidadDeleteView.as_view()(request,
                                                  pk=self.plan_unidad.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanUnidadDeleteView.as_view()(
            request,
            pk=self.another_plan.pk
        )
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_unidad_list')
        # It should still exist
        self.plan_unidad.refresh_from_db()

    def test_get(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadDeleteView.as_view()(request,
                                                  pk=self.plan_unidad.pk)
        assert response.status_code == 405, \
            'Should return a not allowed response'

    def test_delete_success(self):
        """Tests when a successful class plan is deleted"""
        actividad_aprendizaje = mixer.blend(ActividadAprendizaje,
                                            plan_unidad=self.plan_unidad)

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_unidad_delete', kwargs={'pk': self.plan_unidad.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Unidad eliminado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_unidad_list'))

        # The instances should no longer exist in database
        with pytest.raises(PlanUnidad.DoesNotExist):
            PlanUnidad.objects.get(pk=self.plan_unidad.pk)
        with pytest.raises(ActividadAprendizaje.DoesNotExist):
            ActividadAprendizaje.objects.get(pk=actividad_aprendizaje.pk)


class TestPlanUnidadDuplicateView(PlanUnidadTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanUnidadDuplicateView.as_view()(
            request, pk=self.plan_unidad.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanUnidadDuplicateView.as_view()(
            request, pk=self.plan_unidad.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadDuplicateView.as_view()(
            request, pk=self.plan_unidad.pk)
        assert response.status_code == 405, \
            'Should return a not allowed response'

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanUnidadDuplicateView.as_view()(
            request, pk=self.another_plan.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_unidad_list')
        copias = PlanUnidad.objects.filter(name='{} (copia)'.format(
            self.another_plan.name))
        assert len(copias) == 0, 'Should be no copies'

    def test_success_plan_duplication(self):
        """Tests a plan has been successfuly duplicated"""

        self.plan_unidad.objetivos.set(
            [self.objetivo_1, self.objetivo_2])
        self.plan_unidad.objetivos_generales.set(
            [self.general_1, self.general_2])

        actividad_aprendizaje_1 = mixer.blend(ActividadAprendizaje,
                                              plan_unidad=self.plan_unidad)
        actividad_aprendizaje_1.destrezas.set(
            [self.destreza_1, self.destreza_2])

        actividad_aprendizaje_2 = mixer.blend(ActividadAprendizaje,
                                              plan_unidad=self.plan_unidad)
        actividad_aprendizaje_2.destrezas.set(
            [self.destreza_1, self.destreza_2])

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_unidad_duplicate',
                      kwargs={'pk': self.plan_unidad.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'

        # Test success message
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Unidad duplicado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_unidad_list'))

        # Test plan de unidad
        plan_unidad_new = PlanUnidad.objects.last()
        actividad_aprendizaje_new = ActividadAprendizaje.objects.last()
        assert self.plan_unidad.pk != plan_unidad_new.pk, \
            'Should be another instance'
        assert plan_unidad_new.name == '{} (copia)'.format(
            self.plan_unidad.name), 'Should have a new name'
        assert plan_unidad_new.curso == self.plan_unidad.curso, \
            'Should have the same property values'
        # Debe tener igual todos los campos many to many al original
        assert plan_unidad_new.objetivos.first() == self.objetivo_1
        assert plan_unidad_new.objetivos.last() == self.objetivo_2
        assert plan_unidad_new.objetivos_generales.first() == self.general_1
        assert plan_unidad_new.objetivos_generales.last() == self.general_2

        assert self.plan_unidad.updated_at != plan_unidad_new.updated_at, \
            'The updated_at field should not be copied'

        # Tests elemento curricular
        actividad_aprendizaje_new = plan_unidad_new.actividades_aprendizaje.\
            first()

        assert actividad_aprendizaje_new.pk != actividad_aprendizaje_1.pk, \
            'Should be another instance'
        assert actividad_aprendizaje_new.plan_unidad == plan_unidad_new

        # Debe tener igual todos los campos many to many
        # al desarrollo de unidad original
        assert actividad_aprendizaje_new.destrezas.first() == \
            self.destreza_1
        assert actividad_aprendizaje_new.destrezas.last() == self.destreza_2

        # Test second duplication

        request = RequestFactory().post('/', {})
        request.user = self.user
        request = add_middleware_to_request(request)

        PlanUnidadDuplicateView.as_view()(request,
                                          pk=self.plan_unidad.pk)

        plan_unidad_new = PlanUnidad.objects.last()
        assert plan_unidad_new.name == '{} (copia 2)'.format(
            self.plan_unidad.name)
        assert plan_unidad_new.curso == self.plan_unidad.curso

        # Test third duplication

        PlanUnidadDuplicateView.as_view()(request,
                                          pk=self.plan_unidad.pk)

        plan_unidad_new = PlanUnidad.objects.last()
        assert plan_unidad_new.name == '{} (copia 3)'.format(
            self.plan_unidad.name)
        assert plan_unidad_new.curso == self.plan_unidad.curso

    def test_when_name_too_long(self):
        """Tests a plan with a name too long has been duplicated"""

        self.plan_unidad.objetivos.set(
            [self.objetivo_1, self.objetivo_2])
        self.plan_unidad.objetivos_generales.set(
            [self.general_1, self.general_2])

        self.plan_unidad.name = \
            'lorem ipsum dolor.sit amet (copia) (cop... (copia)'
        self.plan_unidad.save()

        actividad_aprendizaje_1 = mixer.blend(ActividadAprendizaje,
                                              plan_unidad=self.plan_unidad)
        actividad_aprendizaje_1.destrezas.set(
            [self.destreza_1, self.destreza_2])

        actividad_aprendizaje_2 = mixer.blend(ActividadAprendizaje,
                                              plan_unidad=self.plan_unidad)
        actividad_aprendizaje_2.destrezas.set(
            [self.destreza_1, self.destreza_2])

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_unidad_duplicate',
                      kwargs={'pk': self.plan_unidad.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'


class TestPlanUnidadPdfView(PlanUnidadTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanUnidadPdfView.as_view()(
            request, pk=self.plan_unidad.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanUnidadPdfView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        response = PlanUnidadPdfView.as_view()(
            request, pk=self.another_plan.pk)
        assert response.status_code == 405, 'Should return a Not Allowed'

    def test_get_pdf(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanUnidadPdfView.as_view()(
            request, pk=self.plan_unidad.pk)
        assert response.status_code == 200, \
            'Should return a not allowed response'
        assert response.template_name[0] == \
            'planificaciones/pdfs/plan_unidad_pdf.html'
        assert response._headers.get(
            'content-type') == ('Content-Type', 'application/pdf'), \
            'Should return a pdf'
        assert self.plan_unidad.name in response.rendered_content, \
            'Should show info about the "plan unidad"'
