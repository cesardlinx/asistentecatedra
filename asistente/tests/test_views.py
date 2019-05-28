from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer
from stripe.error import CardError

from accounts.models import Subscription
from accounts.tests.conftest import clean_test_files
from asistente import views
from planificaciones.models.asignatura import Asignatura
from planificaciones.models.curso import Curso

from .conftest import add_middleware_to_request

pytestmark = pytest.mark.django_db

User = get_user_model()


class TestHomeView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.HomeTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/home.html' in \
            response.template_name, \
            'Home template should be rendered in the view'


class TestBibliotecaView(TestCase):
    def setUp(self):
        """Response creation"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        self.response = views.BibliotecaListView.as_view()(request)

    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        assert self.response.status_code == 200, \
            'Should be callable by anonymous'
        assert 'asistente/biblioteca.html' in \
            self.response.template_name, \
            'Premium template should be rendered in the view'

    def test_get(self):
        curso = mixer.blend(Curso, name="2° EGB")
        asignatura = mixer.blend(Asignatura, name='Matemática')
        libro = mixer.blend('asistente.Libro', asignatura=asignatura,
                            curso=curso)
        self.assertContains(self.response, libro.curso)

    def tearDown(self):
        clean_test_files()


class TestAyudaView(TestCase):
    def setUp(self):
        """Response Creation"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        self.response = views.AyudaListView.as_view()(request)

    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        assert self.response.status_code == 200, \
            'Should be callable by anonymous'
        assert 'asistente/ayuda.html' in \
            self.response.template_name, \
            'Ayuda template should be rendered in the view'

    def test_get(self):
        pregunta = mixer.blend('asistente.Pregunta')
        self.assertContains(self.response, pregunta.question)
        self.assertContains(self.response, pregunta.answer)


class TestPremiumView:
    def test_anonymous(self):
        """Tests that an anonymous user can access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.PremiumTemplateView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert 'asistente/premium.html' in \
            response.template_name, \
            'Premium template should be rendered in the view'


class TestCheckoutView(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)
        self.request = RequestFactory().get('/')
        self.plan = mixer.blend('accounts.Plan')

        self.mock_stripe = patch('asistente.views.stripe.Subscription')
        self.stripe_subscription = self.mock_stripe.start()
        self.stripe_subscription.create.return_value = {'id': '123456'}

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        self.request.user = AnonymousUser()
        response = views.CheckoutView.as_view()(self.request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that the view can be callable by a user"""
        self.request.user = self.user
        response = views.CheckoutView.as_view()(self.request)
        assert response.status_code == 200, \
            'Should be callable by the authenticated user'

    def test_post_success(self):
        """Test when all data are valid for checkout"""
        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
            'plan_id': self.plan.pk,
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request)
        assert response.status_code == 302, 'Should return a redirection'
        subscription = Subscription.objects.all()[0]
        assert subscription.user == self.user, \
            'The user should be related with the subscription'
        assert subscription.stripe_subscription_id == '123456', \
            'The subscription should have an id'
        assert subscription.active is True, \
            'The subscription should be active'
        self.user.refresh_from_db()
        assert self.user.active_plan == self.plan, \
            'The user now is subscripted to the plan'

    def test_invalid_plan_id(self):
        """Test when an invalid plan id is given"""
        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
            'plan_id': 'invalid-id',
        })
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request)
        assert 'Error. Los datos no son correctos o han sido alterados.' in \
            str(response.content), 'A message should be displayed'

        assert 'alert-danger' in str(response.content), \
            'It should display an error message'

    def test_invalid_card(self):
        """Test when an invalid card is entered (stripe CardError)"""
        self.stripe_subscription.create.side_effect = CardError('Error', 2, 2)

        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
            'plan_id': self.plan.pk,
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request)

        assert 'Error. La tarjeta de crédito ingresada no es válida.' in \
            str(response.content.decode("utf-8")
                ), 'A message should be displayed'

        assert 'alert-danger' in str(response.content), \
            'It should display an error message'

    @patch('asistente.views.delete_subscription_from_stripe')
    def test_change_subscription(self, mock_stripe_delete):
        """Tests an authenticated user can change his subscription"""

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MONTHLY')
        yearly_plan = mixer.blend('accounts.Plan', plan_type='YEARLY')

        before_subscription = mixer.blend(
            'accounts.Subscription',
            plan=monthly_plan,
            user=self.user,
            stripe_subscription_id='456789',
            active=True
        )

        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
            'plan_id': yearly_plan.pk,
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request)

        assert response.status_code == 302, \
            'Response should send a redirection'
        assert self.user.subscriptions.filter(active=True).count() == 1
        active_subscription = self.user.subscriptions.get(active=True)
        assert active_subscription != before_subscription
        assert self.user.active_plan == yearly_plan
        mock_stripe_delete.assert_called_once_with('456789')

    def test_change_subscription_when_no_previous_plan(self):
        """
        Tests a subscription change when there is no previous active plan
        """

        monthly_plan = mixer.blend('accounts.Plan', plan_type='MONTHLY')

        request = RequestFactory().post('/', {
            'stripeToken': 'some-token',
            'plan_id': monthly_plan.pk,
        })

        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.CheckoutView.as_view()(request)

        assert response.status_code == 302, \
            'Response should return an ok status'
        assert self.user.subscriptions.filter(active=True).count() == 1
        assert self.user.active_plan == monthly_plan
