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
from planificaciones import views
from planificaciones.models.plan_destrezas import PlanDestrezas
from planificaciones.tests.planificaciones_testcase import \
    PlanificacionesTestCase

User = get_user_model()
pytestmark = pytest.mark.django_db


class PlanDestrezasTestCase(PlanificacionesTestCase):
    def setUp(self):
        """Creates data for testing Planes de Destrezas"""
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
            'name': 'Plan de Destrezas1',
            'ano_lectivo': '2019-2020',
            'docentes': 'David Padilla',
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            'paralelos': 'A y C',
            'unidad': self.unidad_1.id,
            'objetivos': [self.objetivo_1.id, self.objetivo_2.id],
            'objetivos_generales': [self.general_1.id, self.general_2.id],
            'destrezas': [self.destreza_1.id, self.destreza_2.id],
            'criterios_evaluacion': [self.criterio_1.id, self.criterio_2.id],
            'periodos': 20,
            'semana_inicio': 'lorem ipsum dolor sit amet',
            'ejes_transversales': 'Lorem ipsum dolor sit amet.',
            'estrategias_metodologicas': 'Lorem ipsum dolor sit amet.',
            'recursos': 'Lorem ipsum dolor sit amet.',
            'indicadores': [self.indicador_1.id, self.indicador_2.id],
            'actividades_evaluacion': 'Lorem ipsum dolor sit amet.',
        }

        self.plan_destrezas = mixer.blend(PlanDestrezas,
                                          elaborado_por=self.user)

        another_user = mixer.blend(User, is_premium=True)
        self.another_plan = mixer.blend(PlanDestrezas,
                                        elaborado_por=another_user)

        self.common_user = mixer.blend(User)

    def tearDown(self):
        self.logger.uninstall()


class TestPlanDestrezasListView(PlanDestrezasTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PlanDestrezasListView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = views.PlanDestrezasListView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanDestrezasListView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert 'planificaciones/planificacion_list.html' in \
            response.template_name, \
            'Template should be the one for listing planning'
        assert self.plan_destrezas.name in response.rendered_content, \
            'Should contain the unit plan name'
        assert self.another_plan.name not in response.rendered_content, \
            'Should not contain others users plans'


class TestPlanDestrezasCreateView(PlanDestrezasTestCase):
    """Prueba la vista para la creación de planes de destreza"""

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PlanDestrezasCreateView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = views.PlanDestrezasCreateView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanDestrezasCreateView.as_view()(request)
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
        self.assertContains(response, 'id="id_destrezas"')
        self.assertContains(response, 'id="id_criterios_evaluacion"')
        self.assertContains(response, 'id="id_indicadores"')
        self.assertContains(response, 'name="periodos"')
        self.assertContains(response, 'name="semana_inicio"')
        self.assertContains(response, 'name="ejes_transversales"')
        self.assertContains(response, 'name="estrategias_metodologicas"')
        self.assertContains(response, 'name="recursos"')
        self.assertContains(response, 'name="actividades_evaluacion"')
        self.assertContains(response, 'name="necesidad_adaptacion"')
        self.assertContains(response, 'name="adaptacion_curricular"')
        self.assertContains(response, 'name="aprobado_por"')
        self.assertContains(response, 'name="revisado_por"')

    def test_post_success(self):
        """Prueba la creación de planes de destreza"""
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_destrezas_create')
        response = self.client.post(url, self.data, follow=True)
        assert response.status_code == 200, 'Should return a success response'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Destrezas creado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_destrezas_list'))

        self.plan_destrezas.refresh_from_db()

        plan = PlanDestrezas.objects.last()
        assert plan.name == 'Plan de Destrezas1', 'Should create a Plan de '\
            'Destrezas'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan de destrezas created for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan de Destrezas is created.'

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""
        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.PlanDestrezasCreateView.as_view()(request)

        assert response.status_code == 200, 'Should return a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'
        assert 'alert-danger' in str(response.content), \
            'Should return an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.PlanDestrezasCreateView.as_view()(request)
        assert response.status_code == 200, 'Should return a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'
        assert 'alert-danger' in str(response.content), \
            'Should return an error message'


class TestPlanDestrezasUpdateView(PlanDestrezasTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=self.plan_destrezas.pk, slug=self.plan_destrezas.slug)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=self.plan_destrezas.pk, slug=self.plan_destrezas.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get_when_user_doesnt_own_plan(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=self.another_plan.pk, slug=self.another_plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_destrezas_list')

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=self.another_plan.pk, slug=self.another_plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_destrezas_list')

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=self.plan_destrezas.pk, slug=self.plan_destrezas.slug)
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
        self.assertContains(response, 'id="id_destrezas"')
        self.assertContains(response, 'id="id_criterios_evaluacion"')
        self.assertContains(response, 'id="id_indicadores"')
        self.assertContains(response, 'name="periodos"')
        self.assertContains(response, 'name="semana_inicio"')
        self.assertContains(response, 'name="ejes_transversales"')
        self.assertContains(response, 'name="estrategias_metodologicas"')
        self.assertContains(response, 'name="recursos"')
        self.assertContains(response, 'name="actividades_evaluacion"')
        self.assertContains(response, 'name="necesidad_adaptacion"')
        self.assertContains(response, 'name="adaptacion_curricular"')
        self.assertContains(response, 'name="aprobado_por"')
        self.assertContains(response, 'name="revisado_por"')

    def test_post_success(self):
        """Prueba la actualización de planes de destreza"""
        assert self.plan_destrezas.name != 'Plan de Destrezas1', \
            'El plan inicialmente tiene un nombre diferente'
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_destrezas_update', kwargs={
            'pk': self.plan_destrezas.pk, 'slug': self.plan_destrezas.slug})
        response = self.client.post(url, self.data, follow=True)
        assert response.status_code == 200, 'Should return a success response'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Destrezas actualizado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_destrezas_list'))

        self.plan_destrezas.refresh_from_db()
        assert self.plan_destrezas.name == 'Plan de Destrezas1', \
            'Debe actualizar el plan de destreza'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan de destrezas updated for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan de Destrezas is updated.'

    def test_invalid_plan(self):
        """Tests the view when sending invalid data about a plan"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises 404 Error
        with pytest.raises(Http404):
            views.PlanDestrezasUpdateView.as_view()(request, pk=1, slug='test')

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""

        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=self.plan_destrezas.pk, slug=self.plan_destrezas.slug)

        assert response.status_code == 200, 'Should return a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'
        assert 'alert-danger' in str(response.content), \
            'Should return an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        plan = mixer.blend(PlanDestrezas)
        request = RequestFactory().post('/', data={})
        request.user = self.user
        response = views.PlanDestrezasUpdateView.as_view()(
            request, pk=plan.pk, slug=plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_destrezas_list')


class TestPlanDestrezasDeleteView(PlanDestrezasTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PlanDestrezasDeleteView.as_view()(
            request,
            pk=self.plan_destrezas.pk
        )
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = views.PlanDestrezasDeleteView.as_view()(
            request,
            pk=self.plan_destrezas.pk
        )
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.PlanDestrezasDeleteView.as_view()(
            request,
            pk=self.another_plan.pk
        )
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_destrezas_list')
        # It should still exist
        self.plan_destrezas.refresh_from_db()

    def test_get(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanDestrezasDeleteView.as_view()(
            request,
            pk=self.plan_destrezas.pk
        )
        assert response.status_code == 405, \
            'Should return a not allowed response'

    def test_delete_success(self):
        """Tests when a successful class plan is deleted"""
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_destrezas_delete', kwargs={'pk':
                      self.plan_destrezas.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Destrezas eliminado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_destrezas_list'))

        # The instances should no longer exist in database
        with pytest.raises(PlanDestrezas.DoesNotExist):
            PlanDestrezas.objects.get(pk=self.plan_destrezas.pk)


class TestPlanDestrezasDuplicateView(PlanDestrezasTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PlanDestrezasDuplicateView.as_view()(
            request, pk=self.plan_destrezas.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = views.PlanDestrezasDuplicateView.as_view()(
            request, pk=self.plan_destrezas.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.PlanDestrezasDuplicateView.as_view()(
            request, pk=self.plan_destrezas.pk)
        assert response.status_code == 405, \
            'Should return a not allowed response'

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.PlanDestrezasDuplicateView.as_view()(
            request, pk=self.another_plan.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_destrezas_list')
        copias = PlanDestrezas.objects.filter(name='{} (copia)'.format(
            self.another_plan.name))
        assert len(copias) == 0, 'Should be no copies'

    def test_success_plan_duplication(self):
        """Tests a plan has been successfuly duplicated"""

        self.plan_destrezas.objetivos.set(
            [self.objetivo_1, self.objetivo_2])
        self.plan_destrezas.objetivos_generales.set(
            [self.general_1, self.general_2])
        self.plan_destrezas.destrezas.set(
            [self.destreza_1, self.destreza_2])
        self.plan_destrezas.criterios_evaluacion.set(
            [self.criterio_1, self.criterio_2])
        self.plan_destrezas.indicadores.set(
            [self.indicador_1, self.indicador_2])

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_destrezas_duplicate',
                      kwargs={'pk': self.plan_destrezas.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'

        # Test success message
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan de Destrezas duplicado '\
            'exitosamente.', 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_destrezas_list'))

        # Test plan de destreza
        plan_destrezas_new = PlanDestrezas.objects.last()

        assert self.plan_destrezas.pk != plan_destrezas_new.pk, \
            'Should be another instance'
        assert plan_destrezas_new.name == '{} (copia)'.format(
            self.plan_destrezas.name), 'Should have a new name'
        assert plan_destrezas_new.curso == self.plan_destrezas.curso, \
            'Should have the same property values'
        # Debe tener igual todos los campos many to many al original
        assert plan_destrezas_new.objetivos.first() == self.objetivo_1
        assert plan_destrezas_new.objetivos.last() == self.objetivo_2
        assert plan_destrezas_new.objetivos_generales.first() == self.general_1
        assert plan_destrezas_new.objetivos_generales.last() == self.general_2
        assert plan_destrezas_new.destrezas.first() == self.destreza_1
        assert plan_destrezas_new.destrezas.last() == self.destreza_2
        assert plan_destrezas_new.criterios_evaluacion.first() == self.criterio_1
        assert plan_destrezas_new.criterios_evaluacion.last() == self.criterio_2
        assert plan_destrezas_new.indicadores.first() == self.indicador_1
        assert plan_destrezas_new.indicadores.last() == self.indicador_2

        assert self.plan_destrezas.updated_at != \
            plan_destrezas_new.updated_at, \
            'The updated_at field should not be copied'

        # Test second duplication

        request = RequestFactory().post('/', {})
        request.user = self.user
        request = add_middleware_to_request(request)

        views.PlanDestrezasDuplicateView.as_view()(
            request,
            pk=self.plan_destrezas.pk
        )

        plan_destrezas_new = PlanDestrezas.objects.last()
        assert plan_destrezas_new.name == '{} (copia 2)'.format(
            self.plan_destrezas.name)
        assert plan_destrezas_new.curso == self.plan_destrezas.curso

        # Test third duplication

        views.PlanDestrezasDuplicateView.as_view()(
            request,
            pk=self.plan_destrezas.pk
        )

        plan_destrezas_new = PlanDestrezas.objects.last()
        assert plan_destrezas_new.name == '{} (copia 3)'.format(
            self.plan_destrezas.name)
        assert plan_destrezas_new.curso == self.plan_destrezas.curso
