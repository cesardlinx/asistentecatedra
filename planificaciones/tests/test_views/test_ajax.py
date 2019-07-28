import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from planificaciones.tests.planificaciones_testcase import \
    PlanificacionesTestCase

from planificaciones.views.ajax_views import (
    LoadCursosView, LoadDestrezasView,
    LoadObjetivosView, LoadUnidadesView)

pytestmark = pytest.mark.django_db


class TestLoadCursosView(PlanificacionesTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = LoadCursosView.as_view()(request, template='checklist')
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = LoadCursosView.as_view()(request, template='checklist')
        assert response.status_code == 200, 'Authenticated user can access'
        assert response.content == b'', 'Response should be empty'

    def test_failed_when_bad_template_name(self):
        """
        Tests that when there is a bad template name
        will return an empty response
        """
        request = RequestFactory().get('/',
                                       {'asignatura': self.asignatura.id},
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.user
        response = LoadCursosView.as_view()(request, template='bad')
        assert response.status_code == 200, 'Authenticated user can access'
        assert response.content == b'', 'Response should be empty'

    def test_success_when_checklist_template(self):
        """
        Tests that an authenticated user can access the view and
        the inputs are checkboxes
        """
        request = RequestFactory().get('/',
                                       {'asignatura': self.asignatura.id},
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.user
        response = LoadCursosView.as_view()(request, template='checklist')
        assert response.status_code == 200, 'Authenticated user can access'
        # The template should contain checkboxes
        self.assertContains(response, '<input type="checkbox" name="cursos"')
        self.assertContains(
            response, 'value="{}"'.format(self.curso_1.id))
        self.assertContains(
            response, 'value="{}"'.format(self.curso_2.id))

    def test_success_when_select_template(self):
        """
        Tests that an authenticated user can access the view and
        the field is a select input
        """
        request = RequestFactory().get('/',
                                       {'asignatura': self.asignatura.id},
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = self.user
        response = LoadCursosView.as_view()(request, template='select')
        assert response.status_code == 200, 'Authenticated user can access'
        # The template should contain the options
        self.assertContains(response,
                            '<option value="{}"'.format(self.curso_1.id))
        self.assertContains(response,
                            '<option value="{}"'.format(self.curso_2.id))
        self.assertContains(
            response, 'value="{}"'.format(self.curso_1.id))
        self.assertContains(
            response, 'value="{}"'.format(self.curso_2.id))


class TestLoadUnidadesView(PlanificacionesTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = LoadUnidadesView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = LoadUnidadesView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert response.content == b'', 'Response should be empty'

    def test_success(self):
        """
        Tests that an authenticated user can access the view
        """
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'curso': self.curso_1.id
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadUnidadesView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, 'value="{}"'.format(self.unidad_1.id))


class TestLoadObjetivosView(PlanificacionesTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/',
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = LoadObjetivosView.as_view()(request, option='curso')
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = LoadObjetivosView.as_view()(request, option='curso')
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(response, '{\\"allowed\\": false}')

    def test_failed_when_bad_option(self):
        """
        Tests that when there is a bad option
        will return an empty response
        """
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'cursos[]': [self.curso_1.id, self.curso_2.id]
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadObjetivosView.as_view()(request, option='bad')
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(response, '{\\"allowed\\": false}')

    def test_success_when_option_is_area(self):
        """
        Tests when the option is area, should search objectives by area
        """
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadObjetivosView.as_view()(request, option='area')
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, self.general_1.codigo)

    def test_success_when_option_is_curso(self):
        """
        Tests when the option is curso, should search objectives by course
        """
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'cursos[]': [self.curso_1.id, self.curso_2.id]
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadObjetivosView.as_view()(request, option='curso')
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, self.objetivo_1.codigo)
        self.assertContains(
            response, self.objetivo_2.codigo)
        self.assertContains(
            response, self.general_1.codigo)

    def test_success_when_option_is_unidad(self):
        """
        Tests when the option is unidad, should search objectives by unit
        """
        request = RequestFactory().get(
            '/',
            {
                'unidad': self.unidad_1.id,
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadObjetivosView.as_view()(request, option='unidad')
        assert response.status_code == 200, 'Authenticated user can access'
        self.assertContains(
            response, self.objetivo_1.codigo)
        self.assertContains(
            response, self.objetivo_2.codigo)
        self.assertContains(
            response, self.general_1.codigo)


class TestLoadDestrezasView(PlanificacionesTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/', {'formset_name': 'somename'},
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = LoadDestrezasView.as_view()(request, template='checklist')
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_not_ajax(self):
        request = RequestFactory().get('/', {'formset_name': 'somename'})
        request.user = self.user
        response = LoadDestrezasView.as_view()(request, template='checklist')
        assert response.status_code == 200, 'Authenticated user can access'
        assert response.content == b'', 'Response should be empty'

    def test_failed_when_bad_template(self):
        """
        Tests that when there is a bad template name
        will return an empty response
        """
        request = RequestFactory().get('/', {'formset_name': 'somename'})
        request.user = self.user
        response = LoadDestrezasView.as_view()(request, template='checklist')
        assert response.status_code == 200, 'Authenticated user can access'
        assert response.content == b'', 'Response should be empty'

    def test_success_when_template_is_checklist(self):
        """
        Tests that an authenticated user can access the view and
        the inputs are checkboxes
        """
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'cursos[]': self.curso_1.id,
                'numero_fila': 0,
                'formset_name': 'somename'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadDestrezasView.as_view()(request, template='checklist')
        assert response.status_code == 200, 'Authenticated user can access'
        # The template should contain checkboxes
        self.assertContains(response,
                            '<input type="checkbox"')
        self.assertContains(response,
                            ' name="somename-0-destrezas"')
        self.assertContains(
            response, self.destreza_1.codigo)

    def test_success_when_template_is_select(self):
        """
        Tests that an authenticated user can access the view and
        the inputs are checkboxes
        """
        request = RequestFactory().get(
            '/',
            {
                'asignatura': self.asignatura.id,
                'curso': self.curso_1.id,
                'formset_name': 'somename'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        request.user = self.user
        response = LoadDestrezasView.as_view()(request, template='select')
        assert response.status_code == 200, 'Authenticated user can access'
        # The template should contain the options
        self.assertContains(response,
                            '<option value="{}"'.format(self.destreza_1.id))
        self.assertContains(response,
                            '<option value="{}"'.format(self.destreza_2.id))
        self.assertContains(
            response, self.destreza_1.codigo)
        self.assertContains(
            response, self.destreza_2.codigo)
