import pytest
from django.urls import resolve, reverse
from mixer.backend.django import mixer
from asistente import views
pytestmark = pytest.mark.django_db


class TestAsistenteUrls:
    def test_home(self):
        path = reverse('home')
        view = resolve(path)
        assert view.func.view_class == views.HomeTemplateView, \
            'Should resolve to the view HomeTemplateView'

    def test_biblioteca(self):
        path = reverse('biblioteca')
        view = resolve(path)
        assert view.func.view_class == views.BibliotecaListView, \
            'Should resolve to the view BibliotecaListView'

    def test_ayuda(self):
        path = reverse('ayuda')
        view = resolve(path)
        assert view.func.view_class == views.AyudaListView, \
            'Should resolve to the view AyudaListView'

    def test_about(self):
        path = reverse('about')
        view = resolve(path)
        assert view.func.view_class == views.AboutTemplateView, \
            'Should resolve to the view AboutTemplateView'

    def test_condiciones(self):
        path = reverse('condiciones')
        view = resolve(path)
        assert view.func.view_class == views.CondicionesTemplateView, \
            'Should resolve to the view CondicionesTemplateView'

    def test_privacidad(self):
        path = reverse('privacidad')
        view = resolve(path)
        assert view.func.view_class == views.PrivacidadTemplateView, \
            'Should resolve to the view PrivacidadTemplateView'

    def test_cookies(self):
        path = reverse('cookies')
        view = resolve(path)
        assert view.func.view_class == views.CookiesTemplateView, \
            'Should resolve to the view CookiesTemplateView'

    def test_contact(self):
        path = reverse('contacto')
        view = resolve(path)
        assert view.func.view_class == views.ContactView, \
            'Should resolve to the view ContactView'

