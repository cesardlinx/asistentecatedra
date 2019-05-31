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

    def test_premium(self):
        path = reverse('premium')
        view = resolve(path)
        assert view.func.view_class == views.PremiumTemplateView, \
            'Should resolve to the view PremiumTemplateView'

    def test_checkout(self):
        plan = mixer.blend('accounts.Plan', plan_type='MONTHLY')
        path = reverse('checkout',
                       kwargs={'plan_id': plan.pk, 'plan_slug': plan.slug})
        view = resolve(path)
        assert view.func.view_class == views.CheckoutView, \
            'Should resolve to the CheckoutView'

    def test_cancel_subscription(self):
        path = reverse('cancel_subscription')
        view = resolve(path)
        assert view.func == views.cancel_subscription_view, \
            'Should resolve to the cancel_subscription_view'
