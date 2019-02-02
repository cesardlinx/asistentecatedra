import os
from unittest.mock import patch

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import (LoginView, PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sites.models import Site
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from mixer.backend.django import mixer
from PIL import Image

from accounts import views
from accounts.forms import SignupForm

pytestmark = pytest.mark.django_db
User = get_user_model()


def add_middleware_to_request(request):
        # Add session middleware
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        # Add messages middleware
        messages = FallbackStorage(request)
        request._messages = messages
        return request


class SignupTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'David',
            'last_name': 'Padilla',
            'password1': 'P455w0rd',
            'password2': 'P455w0rd',
            'email': 'tester@tester.com',
            'institution': 'Colegio Benalcázar',
            'terms': True
        }
        self.url = reverse('signup')


class TestSignupView(SignupTestCase):
    """Tests para la vista de Signup"""

    def test_get(self):
        """Test access to view by anonymous"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.SignupView.as_view()(request)
        form = response.context_data.get('form')
        assert isinstance(form, SignupForm), \
            'The form should be instance of SignupForm'
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert response.template_name[0] == 'accounts/signup.html'
        # Campos en el template (Template Testing)
        self.assertContains(response, 'name="first_name"')
        self.assertContains(response, 'name="last_name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="password1"')
        self.assertContains(response, 'name="password2"')
        self.assertContains(response, 'name="institution"')
        self.assertContains(response, 'name="terms"')
        self.assertContains(response, 'name="g-recaptcha-response"')

    @patch("accounts.views.CheckRecaptchaMixin.is_recaptcha_valid",
           autospec=True)
    def test_post_success(self, mock_recaptcha):
        """
        Test for user creation and authentication
        """
        # Mocking recaptcha
        mock_recaptcha.return_value = True

        response = self.client.post(self.url, self.data, follow=True)
        user = User.objects.last()

        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1, 'There should be one message'
        assert 'Exito!, un mensaje ha sido enviado a tu correo para que '\
               'verifiques tu cuenta.' == messages[0].message, \
               'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'There should be a success message.'
        self.assertRedirects(response, reverse('planificaciones'))
        assert User.objects.exists() is True, 'Should create a user'
        user = User.objects.last()
        leading_part_of_email = user.email.split('@', 1)[0]
        derived_username = '{}_{}'.format(leading_part_of_email, user.pk)
        assert user.username == derived_username, \
            'Username creation should be derived from email'
        assert user.first_name == 'David',  \
            "The user's first name should be David"
        assert user.email_confirmed is False, \
            "Email shouldn't be confirmed"
        assert len(mail.outbox) == 1, 'Should exist an email in outbox'
        user = response.context.get('user')
        assert user.is_authenticated is True, \
            'User should be authenticated'

    @patch("accounts.views.CheckRecaptchaMixin.is_recaptcha_valid",
           autospec=True)
    def test_recaptcha_invalid(self, mock_recaptcha):
        """
        Test for signup when recaptcha is invalid
        """
        # Mocking recaptcha
        mock_recaptcha.return_value = False
        response = self.client.post(self.url, self.data)

        self.assertRedirects(response, self.url)
        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1, 'There should be one message'
        assert 'reCAPTCHA no válido. Por favor intente de nuevo.'\
               == messages[0].message, 'Should return error message'
        assert messages[0].tags == 'alert-danger', \
            'There should be an error message.'

    @patch("accounts.views.CheckRecaptchaMixin.is_recaptcha_valid",
           autospec=True)
    def test_post_invalid(self, mock_recaptcha):
        """Test for invalid data in signup"""
        # Mocking recaptcha
        mock_recaptcha.return_value = True
        response = self.client.post(self.url, {})

        form = response.context_data.get('form')

        # Errors
        errors = form.errors
        assert 'Este campo es obligatorio.' in errors.get('first_name')
        assert 'Este campo es obligatorio.' in errors.get('last_name')
        assert 'Este campo es obligatorio.' in errors.get('email')
        assert 'Este campo es obligatorio.' in errors.get('password1')
        assert 'Este campo es obligatorio.' in errors.get('password2')
        assert 'Este campo es obligatorio.' in errors.get('terms')
        assert 'Este campo es obligatorio.' in errors.get('institution')

        assert response.status_code == 200, \
            'Should not redirect'
        assert form.errors is not None, \
            'The form should have errors'
        assert User.objects.exists() is False, \
            'The view should not create a user'


class TestConfirmationEmail(SignupTestCase):
    """
    Caso de prueba para probar el correo electrónico enviado al usuario
    para que este pueda verificar su email.
    """
    @patch("accounts.views.CheckRecaptchaMixin.is_recaptcha_valid",
           autospec=True)
    def setUp(self, mock_recaptcha):
        """Obtención del correo"""

        super().setUp()

        # Mocking recaptcha
        mock_recaptcha.return_value = True

        # Site configuration
        site = Site.objects.get(pk=1)
        site.domain = 'localhost:8000'
        site.save()

        response = self.client.post(self.url, self.data)
        self.uid = response.context.get('uid')
        self.token = response.context.get('token')
        self.email = mail.outbox[0]

    def test_email_body(self):

        confirm_url = reverse('confirm_email', kwargs={
            'uidb64': self.uid,
            'token': self.token
        })

        assert confirm_url in self.email.body, \
            'Link for email confirmation should be in email body'
        assert settings.DOMAIN in self.email.body, \
            'Domain name should be in email body'
        assert 'David' in self.email.body, \
            'Name should be in email body'
        assert 'Asistente de Cátedra | Confirmar Correo Electrónico' in \
            self.email.subject, 'The subject of email'
        assert 'tester@tester.com' in self.email.to, \
            "The user's email should be in email's field TO "


class TestEmailConfirmationView(SignupTestCase):
    """
    Caso de prueba para probar la vista que confirma el correo electrónico
    del usuario.
    """
    @patch("accounts.views.CheckRecaptchaMixin.is_recaptcha_valid",
           autospec=True)
    def setUp(self, mock_recaptcha):
        """Obtención del uid y token"""
        super().setUp()

        # Mocking recaptcha
        mock_recaptcha.return_value = True

        response = self.client.post(self.url, self.data)
        self.user = User.objects.get(email='tester@tester.com')
        self.uid = response.context.get('uid')
        self.token = response.context.get('token')
        self.confirm_url = reverse(
            'confirm_email', kwargs={'uidb64': self.uid, 'token': self.token})

    def test_success_confirmation(self):
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed yet'
        response = self.client.get(self.confirm_url)
        assert response.status_code == 200, \
            'The view should be callable by Anonymous user'
        self.user.refresh_from_db()
        assert self.user.email_confirmed is True, \
            'The user should have his email confirmed now'
        response = self.client.get(reverse('home'))
        user = response.context.get('user')
        assert user.is_authenticated is True, \
            'The user should be authenticated'

    def test_invalid_confirmation(self):
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed yet'
        # Invalidates the token
        self.user.set_password('New_password_2')
        response = self.client.get(self.confirm_url)
        assert response.status_code == 200, \
            'The view should be callable by Anonymous user'
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed'


class TestProfileView(TestCase):
    """Tests para la vista de Perfil de usuario"""

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = User.objects.create_user(
            first_name='David',
            last_name='Padilla',
            email='tester@tester.com',
            password='P455w0rd',
            institution='Colegio Benalcazar'
        )

    def tearDown(self):
        """Method to make the image removal when necesary"""
        if os.path.isfile('media/test_image.png'):
            os.remove('media/test_image.png')

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.ProfileView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.ProfileView.as_view()(request,
                                               pk=self.user.pk,
                                               slug=self.user.slug)
        assert response.status_code == 200, 'Authenticated user can access'
        # Campos en el template (Template Testing)
        self.assertContains(response, 'name="first_name"')
        self.assertContains(response, 'name="last_name"')
        self.assertContains(response, 'name="institution"')
        self.assertContains(response, 'name="institution_logo"')

    def test_post_success(self):
        """Tests that user can update his data"""

        # Image creation
        img = Image.new('RGB', (60, 30), color=(73, 109, 137))
        img.save('media/test_image.png')

        img = open('media/test_image.png', 'rb')
        img_content = img.read()

        image = SimpleUploadedFile(
            name='test_image.png',
            content=img_content,
            content_type='image/jpeg'
        )
        img.close()

        # Data sending
        data = {
            'first_name': 'Bruno',
            'institution_logo': image
        }

        self.client.login(email=self.user, password='P455w0rd')

        url = reverse('profile', kwargs={
            'pk': self.user.pk,
            'slug': self.user.slug
        })
        response = self.client.post(url, data)

        assert response.status_code == 302, 'Should redirect to same page'
        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1, 'There should be a message'
        assert 'Sus datos han sido modificados con éxito.' \
            == messages[0].message
        assert 'alert-success' == messages[0].tags, \
            'There should be a success message'
        self.user.refresh_from_db()
        assert self.user.last_name == 'Padilla', \
            'The data untouched must remain the same'
        assert self.user.first_name == 'Bruno', \
            'First name should have changed'
        assert 'logos/test_image' in str(self.user.institution_logo)

    def test_post_invalid(self):
        request = RequestFactory().post('/', data={'first_name': ''})
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.ProfileView.as_view()(request,
                                               pk=self.user.pk,
                                               slug=self.user.slug)

        assert response.status_code == 302, 'Should redirect to same page'
        assert self.user.first_name == 'David', \
            "Should not have change user's data"


class AuthTestCase(TestCase):
    def setUp(self):
        self.data = {
            'email': 'tester@tester.com',
            'password': 'P455w0rd'
        }


class TestLoginView(AuthTestCase):
    """Tests para la vista de Login"""

    def test_get(self):
        """Test access to view by anonymous"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        request = add_middleware_to_request(request)
        response = LoginView.as_view(
            template_name='accounts/login.html')(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert response.template_name[0] == 'accounts/login.html'
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_post_success(self):
        """Test if login has been successful"""
        user = User.objects.create_user(
            email=self.data['email'],
            password=self.data['password']
        )
        data = {
            'username': self.data['email'],
            'password': self.data['password']
        }
        url = reverse('login')
        response = self.client.post(url, data, follow=True)
        planificaciones_url = reverse('planificaciones')

        self.assertRedirects(response, planificaciones_url)
        user_session = response.wsgi_request.user
        assert user_session.is_authenticated is True, \
            'User should be authenticated'
        assert user_session.email == user.email, \
            'The session data should be the same as the database data'

    def test_post_invalid(self):
        """Test if data has been invalid"""
        data = {
            'username': 'usuario',
            'password': 'C0ntr4553ñ4'
        }
        url = reverse('login')
        response = self.client.post(url, data)

        assert response.status_code == 200, 'Should return to same page'
        user_session = response.context.get('user')
        assert user_session.is_authenticated is False,\
            'User should not be authenticated'


class TestLogoutView(AuthTestCase):
    def test_get(self):
        user = User.objects.create_user(
            email=self.data['email'],
            password=self.data['password']
        )

        login_result = self.client.login(username=user.email,
                                         password='P455w0rd')
        assert login_result is True, 'User should be logged'
        response = self.client.get(reverse('logout'))
        session_user = response.wsgi_request.user
        assert session_user.is_authenticated is False
        self.assertRedirects(response, reverse('home'))


# PASSWORD RESET TESTS
class TestPasswordResetView:
    """
    Tests the view that resets the user's password when the user has
    forgoten it
    """
    def test_get(self):
        """Test access to view by anonymous"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PasswordResetView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert response.template_name == 'accounts/password_reset.html'

    def test_post_success(self):
        """Email de usuario existente enviado a la vista Password Reset"""
        mixer.blend(User, email='tester@tester.com')
        data = {
            'email': 'tester@tester.com'
        }
        request = RequestFactory().post('/', data=data)
        request.user = AnonymousUser()
        response = PasswordResetView.as_view()(request)
        assert response.status_code == 302, \
            'Should redirect to password reset done'
        assert len(mail.outbox) == 1, 'Should exist an email in outbox'

    def test_post_invalid(self):
        """Email perteneciente a ningún usuario enviado a Password Reset"""
        data = {
            'email': 'david@tester.com'
        }
        request = RequestFactory().post('/', data=data)
        request.user = AnonymousUser()
        response = PasswordResetView.as_view()(request)
        assert response.status_code == 302, \
            'Should redirect to password reset done'
        assert len(mail.outbox) == 0, 'Should not exist an email in outbox'


class TestPasswordResetDoneView:
    def test_get(self):
        """Test access to view by anonymous"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PasswordResetDoneView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert response.template_name == 'accounts/password_reset_done.html'


class TestPasswordResetConfirmView(TestCase):
    def test_get_success(self):
        """Sending a valid token and coded id"""
        user = mixer.blend(User)
        password_before = user.password
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        token = default_token_generator.make_token(user)
        data = {
            'uidb64': uid,
            'token': token
        }
        request = RequestFactory().get('/', data)
        request.user = AnonymousUser()
        response = PasswordResetConfirmView.as_view()(request)
        assert response.status_code == 200, 'Should be successful'
        assert password_before != user.password

    def test_get_invalid(self):
        """Sending a invalid token and user id"""
        user = mixer.blend(User, password='p455w0rd')
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        token = default_token_generator.make_token(user)
        data = {
            'uidb64': uid,
            'token': token
        }
        user.set_password('p455w0rd_2')  # Invalidates the token
        request = RequestFactory().get('/', data)
        request.user = AnonymousUser()
        response = PasswordResetConfirmView.as_view()(request)
        assert response.status_code == 200, 'Should show the page'
        self.assertContains(response, 'invalid password reset link'), \
            'Should show an error message'
        password_reset_url = reverse('password_reset')
        # Should contain a link to the password reset view
        self.assertContiains(response, 'href="{}"'.format(password_reset_url))


class TestPasswordResetCompleteView:
    def test_get(self):
        """Test access to view by anonymous"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PasswordResetCompleteView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert response.template_name == \
            'accounts/password_reset_complete.html'


class TestPasswordResetEmail(TestCase):
    def setUp(self):
        """Obtención del email"""
        mixer.blend(User, email='tester@tester.com', username='tester')
        data = {
            'email': 'tester@tester.com'
        }
        request = RequestFactory().post('/', data=data)
        request.user = AnonymousUser()
        self.response = PasswordResetView.as_view()(request)
        self.email = mail.outbox[0]

    def test_email_body(self):
        context = self.response.context_data
        token = context.get('token')
        uid = context.get('uid')
        password_reset_confirm_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        assert password_reset_confirm_url in self.email.body, \
            'Link to password reset confirm should be in email body'
        assert 'tester' in self.email.body, \
            'Username should be in email body'
        assert 'tester@tester.com' in self.email.body, \
            'Email should be in email body'
        assert 'Asistente de Cátedra | PASSWORD RESET' in self.email.subject, \
            'The subject of email'
        assert ['tester@tester.com', ] in self.email.to, \
            "The user's email should be in email's field TO "


# PASSWORD CHANGE TESTS
class TestPasswordChangeView(TestCase):
    """
    Tests the view that changes the user's password when
    authenticated
    """
    def setUp(self):
        self.user = mixer.blend(User, password='p455w0rd')

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PasswordChangeView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PasswordChangeView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'

    def test_post_success(self):
        data = {
            'old_password': 'p455w0rd',
            'new_password': 'p455w0rd_2',
            'new_password_confirmation': 'p455w0rd_2'
        }
        request = RequestFactory().post('/', data=data)
        request.user = self.user
        response = views.plan_clase_create(request)
        assert response.status_code == 302, \
            'Should redirect to password change done'
        self.user.refresh_from_db()
        assert self.user.check_password('p455w0rd_2') is True, \
            'The password should have changed for the new one'

    def test_post_invalid(self):
        data = {
            'old_password': 'p455w0rd',
            'new_password': 'p455w0rd_2',
            'new_password_confirmation': 'p455w0rd_2'
        }
        request = RequestFactory().post('/', data=data)
        request.user = self.user
        response = views.plan_clase_create(request)
        assert response.status_code == 302, \
            'Should redirect to password change done'
        self.user.refresh_from_db()
        assert self.user.check_password('p455w0rd_2') is True, \
            'The password should have changed for the new one'


class TestPasswordChangeDoneView(TestCase):
    """
    Tests the view that is showed when the password has changed
    """
    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = PasswordChangeDoneView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = PasswordChangeDoneView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        # Should show the password change done template
        assert response.template_name == 'accounts/password_change_done.html'
