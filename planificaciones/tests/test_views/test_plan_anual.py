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
from planificaciones.models.plan_anual import PlanAnual
from planificaciones.models.desarrollo_unidad import DesarrolloUnidad
from planificaciones.tests.planificaciones_testcase import \
    PlanificacionesTestCase

from planificaciones.views.plan_anual_views import (
     PlanAnualListView, PlanAnualCreateView, PlanAnualUpdateView,
     PlanAnualDeleteView, PlanAnualDuplicateView, PlanAnualPdfView)


User = get_user_model()
pytestmark = pytest.mark.django_db


class PlanAnualTestCase(PlanificacionesTestCase):
    def setUp(self):
        """Creates data for testing Planes Anual"""
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
            'name': 'Plan Anual1',
            'ano_lectivo': '2019-2020',
            'docentes': 'David Padilla',
            'asignatura': self.asignatura.id,
            'curso': self.curso_1.id,
            'paralelos': 'A y C',
            'carga_horaria': 20,
            'semanas_trabajo': 20,
            'semanas_imprevistos': 20,
            'objetivos_generales': [self.general_1.id, self.general_2.id],
            'objetivos_curso': [self.objetivo_1.id, self.objetivo_2.id],
            'objetivos_generales_curso': [
                self.general_1.id, self.general_2.id],
            'ejes_transversales': 'Lorem ipsum dolor sit amet.',
            'bibliografia': 'Lorem ipsum dolor sit amet.',
            'aprobado_por': 'Lorem ipsum dolor sit amet.',
            'revisado_por': 'Lorem ipsum dolor sit amet.',

            # Formset Elementos curriculares 1
            'desarrollo_unidades-TOTAL_FORMS': '2',
            'desarrollo_unidades-INITIAL_FORMS': '0',
            'desarrollo_unidades-MIN_NUM_FORMS': '0',
            'desarrollo_unidades-MAX_NUM_FORMS': '1000',
            'desarrollo_unidades-0-unidad': self.unidad_1.id,
            'desarrollo_unidades-0-objetivos': [
                self.objetivo_1.id, self.objetivo_2.id],
            'desarrollo_unidades-0-objetivos_generales': [
                self.general_1.id, self.general_2.id],
            'desarrollo_unidades-0-destrezas': [
                self.destreza_1.id, self.destreza_2.id],
            'desarrollo_unidades-0-orientaciones_metodologicas': 'lorem ipsum',
            'desarrollo_unidades-0-semanas': 8,

            'desarrollo_unidades-1-unidad': self.unidad_1.id,
            'desarrollo_unidades-1-objetivos': [
                self.objetivo_1.id, self.objetivo_2.id],
            'desarrollo_unidades-1-objetivos_generales': [
                self.general_1.id, self.general_2.id],
            'desarrollo_unidades-1-destrezas': [
                self.destreza_1.id, self.destreza_2.id],
            'desarrollo_unidades-1-orientaciones_metodologicas': 'lorem ipsum',
            'desarrollo_unidades-1-semanas': 2,
        }

        self.plan_anual = mixer.blend(PlanAnual, elaborado_por=self.user)

        another_user = mixer.blend(User, is_premium=True)
        self.another_plan = mixer.blend(PlanAnual, elaborado_por=another_user)

        self.common_user = mixer.blend(User)

    def tearDown(self):
        self.logger.uninstall()


class TestPlanAnualListView(PlanAnualTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanAnualListView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanAnualListView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualListView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert 'planificaciones/planificacion_list.html' in \
            response.template_name, \
            'Template should be the one for listing planning'
        assert self.plan_anual.name in response.rendered_content, \
            'Should contain the yearly plan name'
        assert self.another_plan.name not in response.rendered_content, \
            'Should not contain others users plans'


class TestPlanAnualCreateView(PlanAnualTestCase):
    """Prueba la vista para la creación de planes anuales"""

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanAnualCreateView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanAnualCreateView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualCreateView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        # Tempĺate Testing
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="ano_lectivo"')
        self.assertContains(response, 'name="docentes"')
        self.assertContains(response, 'name="asignatura"')
        self.assertContains(response, 'name="curso"')
        self.assertContains(response, 'name="paralelos"')
        self.assertContains(response, 'name="carga_horaria"')
        self.assertContains(response, 'name="semanas_trabajo"')
        self.assertContains(response, 'name="semanas_imprevistos"')
        self.assertContains(response, 'id="id_objetivos_generales"')
        self.assertContains(response, 'id="id_objetivos_curso"')
        self.assertContains(response, 'id="id_objetivos_generales_curso"')
        self.assertContains(response, 'name="ejes_transversales"')
        self.assertContains(response, 'name="bibliografia"')
        self.assertContains(response, 'name="aprobado_por"')
        self.assertContains(response, 'name="revisado_por"')

        # The title should be Nuevo Plan Anual
        self.assertContains(response, 'Nuevo Plan Anual')

    def test_post_success(self):
        """Prueba la creación de planes anuales"""
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_anual_create')
        response = self.client.post(url, self.data, follow=True)
        assert response.status_code == 200, 'Should return a success response'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan Anual creado exitosamente.', \
            'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_anual_list'))

        self.plan_anual.refresh_from_db()

        plan = PlanAnual.objects.last()
        desarrollo_unidad = DesarrolloUnidad.objects.last()
        assert plan.name == 'Plan Anual1', 'Should create a Plan Anual'
        assert desarrollo_unidad.plan_anual == plan, \
            'el elemento curricular debe pertenecer al plan anual'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan anual created for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan Anual is created.'

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""
        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanAnualCreateView.as_view()(request)

        assert response.status_code == 200, 'Should get a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises ValidationError
        with pytest.raises(ValidationError):
            PlanAnualCreateView.as_view()(request)


class TestPlanAnualUpdateView(PlanAnualTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanAnualUpdateView.as_view()(
            request, pk=self.plan_anual.pk, slug=self.plan_anual.slug)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanAnualUpdateView.as_view()(
            request, pk=self.plan_anual.pk, slug=self.plan_anual.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get_when_user_doesnt_own_plan(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualUpdateView.as_view()(
            request, pk=self.another_plan.pk, slug=self.another_plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_anual_list')

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanAnualUpdateView.as_view()(
            request, pk=self.another_plan.pk, slug=self.another_plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_anual_list')

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        mixer.blend(DesarrolloUnidad, plan_anual=self.plan_anual)
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualUpdateView.as_view()(
            request, pk=self.plan_anual.pk, slug=self.plan_anual.slug)
        assert response.status_code == 200, 'Authenticated user can access'
        # Tempĺate Testing
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="ano_lectivo"')
        self.assertContains(response, 'name="docentes"')
        self.assertContains(response, 'name="asignatura"')
        self.assertContains(response, 'name="curso"')
        self.assertContains(response, 'name="paralelos"')
        self.assertContains(response, 'name="carga_horaria"')
        self.assertContains(response, 'name="semanas_trabajo"')
        self.assertContains(response, 'name="semanas_imprevistos"')
        self.assertContains(response, 'id="id_objetivos_generales"')
        self.assertContains(response, 'id="id_objetivos_curso"')
        self.assertContains(response, 'id="id_objetivos_generales_curso"')
        self.assertContains(response, 'name="ejes_transversales"')
        self.assertContains(response, 'name="bibliografia"')
        self.assertContains(response, 'name="aprobado_por"')
        self.assertContains(response, 'name="revisado_por"')

        # The title should be the planning name
        self.assertContains(response,
                            'Plan Anual: {}'.format(self.plan_anual.name))

    def test_post_success(self):
        """Prueba la actualización de planes anuales"""
        assert self.plan_anual.name != 'Plan Anual1', \
            'El plan inicialmente tiene un nombre diferente'
        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_anual_update', kwargs={
            'pk': self.plan_anual.pk, 'slug': self.plan_anual.slug})
        response = self.client.post(url, self.data, follow=True)
        assert response.status_code == 200, 'Should return a success response'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan Anual actualizado exitosamente.', \
            'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_anual_list'))

        self.plan_anual.refresh_from_db()
        assert self.plan_anual.name == 'Plan Anual1', \
            'Debe actualizar el plan anual'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Plan Anual updated for the user: {}.'.format(
            self.user.email) in str(self.logger), \
            'Log when a Plan Anual is updated.'

    def test_invalid_plan(self):
        """Tests the view when sending invalid data about a plan"""
        request = RequestFactory().post('/', data={})
        request.user = self.user
        # Invalid data raises 404 Error
        with pytest.raises(Http404):
            PlanAnualUpdateView.as_view()(request, pk=1, slug='test')

    def test_invalid_data(self):
        """Tests the view when sending invalid data"""

        self.data['name'] = ''

        request = RequestFactory().post('/', data=self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanAnualUpdateView.as_view()(
            request, pk=self.plan_anual.pk, slug=self.plan_anual.slug)

        assert response.status_code == 200, 'Should get a success response'
        assert 'Por favor corrija los campos resaltados en rojo.' \
            in str(response.content), 'Should have an error message'

    def test_empty_data(self):
        """Tests the view when sending empty data"""
        plan = mixer.blend(PlanAnual)
        request = RequestFactory().post('/', data={})
        request.user = self.user
        response = PlanAnualUpdateView.as_view()(
            request, pk=plan.pk, slug=plan.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_anual_list')


class TestPlanAnualDeleteView(PlanAnualTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanAnualDeleteView.as_view()(request,
                                                 pk=self.plan_anual.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanAnualDeleteView.as_view()(request,
                                                 pk=self.plan_anual.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanAnualDeleteView.as_view()(request,
                                                 pk=self.another_plan.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_anual_list')
        # It should still exist
        self.plan_anual.refresh_from_db()

    def test_get(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualDeleteView.as_view()(request,
                                                 pk=self.plan_anual.pk)
        assert response.status_code == 405, \
            'Should return a not allowed response'

    def test_delete_success(self):
        """Tests when a successful class plan is deleted"""
        desarrollo_unidad = mixer.blend(DesarrolloUnidad,
                                        plan_anual=self.plan_anual)

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_anual_delete', kwargs={'pk': self.plan_anual.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan Anual eliminado exitosamente.',\
            'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_anual_list'))

        # The instances should no longer exist in database
        with pytest.raises(PlanAnual.DoesNotExist):
            PlanAnual.objects.get(pk=self.plan_anual.pk)
        with pytest.raises(DesarrolloUnidad.DoesNotExist):
            DesarrolloUnidad.objects.get(pk=desarrollo_unidad.pk)


class TestPlanAnualDuplicateView(PlanAnualTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanAnualDuplicateView.as_view()(
            request, pk=self.plan_anual.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanAnualDuplicateView.as_view()(
            request, pk=self.plan_anual.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_get(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualDuplicateView.as_view()(
            request, pk=self.plan_anual.pk)
        assert response.status_code == 405, \
            'Should return a not allowed response'

    def test_post_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        request = add_middleware_to_request(request)
        response = PlanAnualDuplicateView.as_view()(
            request, pk=self.another_plan.pk)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == reverse('plan_anual_list')
        copias = PlanAnual.objects.filter(name='{} (copia)'.format(
            self.another_plan.name))
        assert len(copias) == 0, 'Should be no copies'

    def test_success_plan_duplication(self):
        """Tests a plan has been successfuly duplicated"""

        self.plan_anual.objetivos_curso.set([self.objetivo_1, self.objetivo_2])
        self.plan_anual.objetivos_generales_curso.set(
            [self.general_1, self.general_2])
        self.plan_anual.objetivos_generales.set(
            [self.general_1, self.general_2])

        desarrollo_unidad_1 = mixer.blend(DesarrolloUnidad,
                                          plan_anual=self.plan_anual,
                                          unidad=self.unidad_1)
        desarrollo_unidad_1.destrezas.set(
            [self.destreza_1, self.destreza_2])

        desarrollo_unidad_2 = mixer.blend(DesarrolloUnidad,
                                          plan_anual=self.plan_anual,
                                          unidad=self.unidad_2)
        desarrollo_unidad_2.destrezas.set(
            [self.destreza_1, self.destreza_2])

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_anual_duplicate',
                      kwargs={'pk': self.plan_anual.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'

        # Test success message
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'Should return one message'
        assert messages[0].message == 'Plan Anual duplicado exitosamente.',\
            'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'Should return a success message'
        self.assertRedirects(response, reverse('plan_anual_list'))

        # Test plan anual
        plan_anual_new = PlanAnual.objects.last()
        desarrollo_unidad_new = DesarrolloUnidad.objects.last()
        assert self.plan_anual.pk != plan_anual_new.pk, \
            'Should be another instance'
        assert plan_anual_new.name == '{} (copia)'.format(
            self.plan_anual.name), 'Should have a new name'
        assert plan_anual_new.curso == self.plan_anual.curso, \
            'Should have the same property values'
        # Debe tener igual todos los campos many to many al original
        assert plan_anual_new.objetivos_curso.first() == self.objetivo_1
        assert plan_anual_new.objetivos_curso.last() == self.objetivo_2
        assert plan_anual_new.objetivos_generales_curso.first() == \
            self.general_1
        assert plan_anual_new.objetivos_generales_curso.last() == \
            self.general_2
        assert plan_anual_new.objetivos_generales.first() == self.general_1
        assert plan_anual_new.objetivos_generales.last() == self.general_2

        assert self.plan_anual.updated_at != plan_anual_new.updated_at, \
            'The updated_at field should not be copied'

        # Tests elemento curricular
        desarrollo_unidad_new = plan_anual_new.desarrollo_unidades.first()

        assert desarrollo_unidad_new.pk != desarrollo_unidad_1.pk, \
            'Should be another instance'
        assert desarrollo_unidad_new.plan_anual == plan_anual_new
        assert desarrollo_unidad_new.unidad == \
            desarrollo_unidad_1.unidad

        # Debe tener igual todos los campos many to many
        # al desarrollo de unidad original
        assert desarrollo_unidad_new.destrezas.first() == self.destreza_1
        assert desarrollo_unidad_new.destrezas.last() == self.destreza_2

        # Test second duplication

        request = RequestFactory().post('/', {})
        request.user = self.user
        request = add_middleware_to_request(request)

        PlanAnualDuplicateView.as_view()(request,
                                         pk=self.plan_anual.pk)

        plan_anual_new = PlanAnual.objects.last()
        assert plan_anual_new.name == '{} (copia 2)'.format(
            self.plan_anual.name)
        assert plan_anual_new.curso == self.plan_anual.curso

        # Test third duplication

        PlanAnualDuplicateView.as_view()(request,
                                         pk=self.plan_anual.pk)

        plan_anual_new = PlanAnual.objects.last()
        assert plan_anual_new.name == '{} (copia 3)'.format(
            self.plan_anual.name)
        assert plan_anual_new.curso == self.plan_anual.curso

    def test_when_name_too_long(self):
        """Tests a plan with a name too long has been duplicated"""

        self.plan_anual.objetivos_curso.set([self.objetivo_1, self.objetivo_2])
        self.plan_anual.objetivos_generales_curso.set(
            [self.general_1, self.general_2])
        self.plan_anual.objetivos_generales.set(
            [self.general_1, self.general_2])

        self.plan_anual.name = \
            'lorem ipsum dolor.sit amet (copia) (cop... (copia)'
        self.plan_anual.save()

        desarrollo_unidad_1 = mixer.blend(DesarrolloUnidad,
                                          plan_anual=self.plan_anual,
                                          unidad=self.unidad_1)
        desarrollo_unidad_1.destrezas.set(
            [self.destreza_1, self.destreza_2])

        desarrollo_unidad_2 = mixer.blend(DesarrolloUnidad,
                                          plan_anual=self.plan_anual,
                                          unidad=self.unidad_2)
        desarrollo_unidad_2.destrezas.set(
            [self.destreza_1, self.destreza_2])

        self.client.login(username='tester@tester.com',
                          password='P455w0rd_testing',)
        url = reverse('plan_anual_duplicate',
                      kwargs={'pk': self.plan_anual.pk})
        response = self.client.post(url, {}, follow=True)

        assert response.status_code == 200, 'Should return a success code'


class TestPlanAnualPdfView(PlanAnualTestCase):
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanAnualPdfView.as_view()(
            request, pk=self.plan_anual.pk)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_premium(self):
        """Tests that only premium users can access"""
        request = RequestFactory().get('/')
        request.user = self.common_user
        response = PlanAnualPdfView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        assert reverse('planificaciones') == response.url, \
            'Should not be callable by a normal user'

    def test_when_user_doesnt_own_plan(self):
        request = RequestFactory().post('/', self.data)
        request.user = self.user
        response = PlanAnualPdfView.as_view()(
            request, pk=self.another_plan.pk)
        assert response.status_code == 405, 'Should return a Not Allowed'

    def test_get_pdf(self):
        """Tests that an authenticated user can't access by get method"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PlanAnualPdfView.as_view()(
            request, pk=self.plan_anual.pk)
        assert response.status_code == 200, \
            'Should return a not allowed response'
        assert response.template_name[0] == \
            'planificaciones/pdfs/plan_anual_pdf.html'
        assert response._headers.get(
            'content-type') == ('Content-Type', 'application/pdf'), \
            'Should return a pdf'
        assert self.plan_anual.name in response.rendered_content, \
            'Should show info about the "plan anual"'
