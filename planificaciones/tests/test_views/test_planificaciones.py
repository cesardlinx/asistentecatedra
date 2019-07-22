import pytest

from planificaciones.views.planificaciones_view import \
    PlanificacionesTemplateView
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from planificaciones import views
from django.contrib.auth import get_user_model
User = get_user_model()


pytestmark = pytest.mark.django_db


class TestPlanificacionesTemplateView:

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PlanificacionesTemplateView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_auth_user(self):
        """Tests that an authenticated user can access the view"""
        user = mixer.blend(User)
        request = RequestFactory().get('/')
        request.user = user
        response = PlanificacionesTemplateView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert 'planificaciones/planificaciones.html' in \
            response.template_name, \
            'Product list template should be rendered in the view'
