from django.urls import reverse, resolve
from asistente import views


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

    def test_premium(self):
        path = reverse('premium')
        view = resolve(path)
        assert view.func.view_class == views.PremiumTemplateView, \
            'Should resolve to the view PremiumTemplateView'
