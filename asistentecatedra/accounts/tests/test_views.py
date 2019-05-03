import os
from unittest.mock import patch

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
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
from PIL import Image

from accounts import views
from accounts.forms import SignupForm

pytestmark = pytest.mark.django_db
User = get_user_model()


def add_middleware_to_request(request):
    """
    Función para agregar middleware a un request creado con RequestFactory
    """
    # Add session middleware
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()

    # Add messages middleware
    messages = FallbackStorage(request)
    request._messages = messages
    return request


class SignupTestCase(TestCase):
    """
    TestCase general con todos los datos de un usuario de prueba
    """
    def setUp(self):
        self.data = {
            'first_name': 'David',
            'last_name': 'Padilla',
            'password1': 'P455w0rd_testing',
            'password2': 'P455w0rd_testing',
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
        """
        Test para probar los campos en el contenido del correo electrónico
        """
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
        """Pruebas al recibir un link válido de confirmación de correo"""
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed yet'
        response = self.client.get(self.confirm_url, follow=True)
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
        """
        Pruebas al recibir un link de confirmación de correo con un
        token inválido.
        """
        assert self.user.email_confirmed is False, \
            'At the begining, the email should not be confirmed'
        # Invalidates the token
        self.user.set_password('New_password_2')
        self.user.save()
        response = self.client.get(self.confirm_url, follow=True)
        assert response.status_code == 200, \
            'The view should be callable by Anonymous user'
        self.user.refresh_from_db()
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed'

    def test_invalid_confirmation_data(self):
        """
        Pruebas al recibir un link de confirmación de correo con un
        uid inválido.
        """
        confirm_url = reverse(
            'confirm_email', kwargs={'uidb64': 123456, 'token': self.token})
        response = self.client.get(confirm_url, follow=True)
        assert response.status_code == 200, \
            'The view should be callable by Anonymous user'
        self.user.refresh_from_db()
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed'
        self.assertContains(
            response, 'Error. El enlace no es válido o ha expirado')


class TestProfileView(TestCase):
    """Tests para la vista de Perfil de usuario"""

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = User.objects.create_user(
            first_name='David',
            last_name='Padilla',
            email='tester@tester.com',
            password='P455w0rd_testing',
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

        self.client.login(email=self.user.email, password='P455w0rd_testing')

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
    """TestCase general con los dátos básicos para crear un usuario"""
    def setUp(self):
        self.data = {
            'email': 'tester@tester.com',
            'password': 'P455w0rd_testing'
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
        """Test para probar que un usuario puede cerrar sesión"""
        user = User.objects.create_user(
            email=self.data['email'],
            password=self.data['password']
        )

        login_result = self.client.login(username=user.email,
                                         password='P455w0rd_testing')
        assert login_result is True, 'User should be logged'
        response = self.client.get(reverse('logout'))
        session_user = response.wsgi_request.user
        assert session_user.is_authenticated is False
        self.assertRedirects(response, reverse('home'))


# PASSWORD RESET TESTS
class TestPasswordResetView(TestCase):
    """
    Tests the view that resets the user's password when the user has
    forgoten it
    """
    def setUp(self):
        self.url = reverse('password_reset')

    def test_get(self):
        """Test access to view by anonymous"""
        url = reverse('password_reset')
        response = self.client.get(url)
        assert response.status_code == 405, \
            'Should not be callable by get method'

    def test_post_success(self):
        """Test cuando el email de un usuario existente es enviado a la
        vista Password Reset
        """
        User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing'
        )
        data = {
            'email': 'tester@tester.com',
        }
        response = self.client.post(self.url, data, follow=True)
        messages = list(response.context.get('messages'))
        self.assertRedirects(response, reverse('login'))
        assert len(mail.outbox) == 1, 'Should exist an email in outbox'
        assert len(messages) == 1, 'Should exist a message'
        assert messages[0].tags == 'alert-success',\
            'Should return a success message'
        assert messages[0].message == 'Un mensaje ha sido enviado '\
                                      'a tu correo para que reestablezcas '\
                                      'tu contraseña.', \
                                      'Should return a success message'

    def test_post_invalid(self):
        """Test cuando un email perteneciente a ningún usuario es enviado a
        la vista Password Reset
        """
        data = {
            'email': 'david@tester.com'
        }
        response = self.client.post(self.url, data, follow=True)
        password_reset_form = response.context.get('reset_form')
        assert isinstance(password_reset_form, PasswordResetForm), \
            'Should return an instance of PasswordResetForm'
        assert response.context.get('view') is not None
        # print(response.context)
        self.assertRedirects(response, reverse('login'))
        messages = list(response.context.get('messages'))
        assert len(mail.outbox) == 0, 'Should not exist an email in outbox'
        assert len(messages) == 1, 'Should exist a message'
        assert messages[0].tags == 'alert-danger',\
            'Should return an error message'
        assert messages[0].message == 'La cuenta de correo que has escrito '\
                                      'es incorrecta, verifica tus datos.', \
                                      'Should return an error message'


class TestPasswordResetConfirmView(TestCase):
    """
    Tests para probar la vista de confirmación de reset de contraseña
    """
    def setUp(self):
        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing'
        )
        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)
        self.url = reverse('password_reset_confirm', kwargs={
            'uidb64': self.uid,
            'token': self.token
        })

    def test_get_success(self):
        """Sending a valid token and coded id"""
        response = self.client.get(self.url, follow=True)
        form = response.context.get('form')
        assert isinstance(form, SetPasswordForm)
        assert response.status_code == 200, 'Should be successful'
        assert response.context.get('validlink') is True, \
            'Path should be accepted as a valid link'
        assert len(response.redirect_chain) == 1, \
            'Should redirect to set password view'
        assert response.templates[0].name == \
            'accounts/password_reset_confirm.html'
        self.assertContains(response, 'name="new_password1"')
        self.assertContains(response, 'name="new_password2"')

    def test_get_invalid(self):
        """Sending a invalid token and user id"""
        self.user.set_password('p455w0rd_2')  # Invalidates the token
        self.user.save()
        response = self.client.get(self.url, follow=True)
        form = response.context.get('form')
        assert form is None, 'There should be no form'
        assert response.status_code == 200, 'Should return to same page'
        assert len(response.redirect_chain) == 0, \
            'Should not redirect to set password view'
        self.assertContains(
            response,
            '''<p>
            El enlace de restablecimiento de contraseña no es válido,
            seguramente porque ya ha sido usado antes.
            </p>
            ''',
            html=True
        ), 'Should show an error message'
        password_reset_url = reverse('password_reset')
        # Should contain a link to the password reset view
        self.assertContains(response, 'href="{}"'.format(password_reset_url))

    def test_post_success(self):
        """Tests when user sends new password"""
        session = self.client.session
        session['_password_reset_token'] = self.token
        session.save()

        url = reverse('password_reset_confirm', kwargs={
            'uidb64': self.uid,
            'token': 'set-password'
        })

        data = {
            'new_password1': 'P455w0rd_2',
            'new_password2': 'P455w0rd_2',
        }

        response = self.client.post(url, data, follow=True)
        self.assertRedirects(response, reverse('planificaciones'))
        user_session = response.context.get('user')
        assert user_session.is_authenticated is True, \
            'The user should be authenticated'
        assert response.status_code == 200, \
            'The login call should be successful'
        self.user.refresh_from_db()
        assert self.user.check_password('P455w0rd_2') is True, \
            'Password should have changed to the new one'
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be one message'
        assert messages[0].tags == 'alert-success', \
            'There should be one success message'
        assert messages[0].message == 'Tu contraseña ha sido cambiada ' \
                                      'exitosamente.', \
                                      'There should be one success message'

    def test_post_invalid(self):
        """Tests when user sends new password invalid data"""
        session = self.client.session
        session['_password_reset_token'] = self.token
        session.save()

        url = reverse('password_reset_confirm', kwargs={
            'uidb64': self.uid,
            'token': 'set-password'
        })

        data = {
            'new_password1': 'P455w0rd_2',
            'new_password2': 'P455w0rd_',
        }

        response = self.client.post(url, data)
        assert response.status_code == 200, 'Should return same page'
        form = response.context.get('form')
        self.assertTrue(form.errors)


class TestPasswordResetEmail(TestCase):
    def setUp(self):
        """Obtención del email"""
        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='David',
            last_name='Padilla',
        )
        data = {
            'email': 'tester@tester.com',
        }
        url = reverse('password_reset')

        self.response = self.client.post(url, data)
        self.email = mail.outbox[0]

    def test_email_body(self):
        """
        Test que prueba los campos en el correo enviado para reset de
        contraseña.
        """
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_confirm_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        assert password_reset_confirm_url in self.email.body, \
            'Link to password reset confirm should be in email body'
        # assert 'David' in self.email.body, \
        #     'First name should be in email body'
        # assert 'Asistente de Cátedra | Restablecimiento de contraseña' \
        #     in self.email.subject, \
        #     'The subject of email'
        # assert 'tester@tester.com' in self.email.to, \
        #     "The user's email should be in email's field TO "


# PASSWORD CHANGE TESTS
class TestPasswordChangeView(TestCase):
    """
    Tests the view that changes the user's password when
    authenticated
    """
    def setUp(self):
        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing'
        )

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.CustomPasswordChangeView.as_view()(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.CustomPasswordChangeView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        assert 'accounts/password_change.html' in response.template_name, \
            'Template password change should be returned from view'
        assert 'name="old_password"' in response.rendered_content, \
            'Form should contain old_password field'
        assert 'name="new_password1"' in response.rendered_content, \
            'Form should contain new_password1 field'
        assert 'name="new_password2"' in response.rendered_content, \
            'Form should contain old_password2 field'

    def test_post_success(self):
        """
        Tests para probar el cambio exitoso de contraseña por parte de un
        usuario logeado
        """
        data = {
            'old_password': 'P455w0rd_testing',
            'new_password1': 'P455w0rd_2',
            'new_password2': 'P455w0rd_2'
        }
        url = reverse('password_change')
        self.client.login(email=self.user, password='P455w0rd_testing')
        response = self.client.post(url, data, follow=True)
        assert response.status_code == 200, \
            'We should get a successful redirection to planificaciones'
        self.assertRedirects(response, reverse('planificaciones'))
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be one message'
        assert messages[0].tags == 'alert-success', \
            'There should be one success message'
        assert messages[0].message == 'Tu contraseña ha sido cambiada ' \
                                      'exitosamente.', \
                                      'There should be one success message'
        self.user.refresh_from_db()
        assert self.user.check_password('P455w0rd_2') is True, \
            'The password should have changed for the new one'

    def test_post_invalid(self):
        """
        Tests cuando el usuario ingresa mal los datos de la contraseña en el
        formulario
        """
        data = {
            'old_password': 'P455w0rd_testing',
            'new_password1': 'P455w0rd_2',
            'new_password2': 'P455w0rd_3'
        }
        url = reverse('password_change')
        self.client.login(email=self.user, password='P455w0rd_testing')
        response = self.client.post(url, data)
        form = response.context.get('form')
        assert response.status_code == 200, \
            'Should go to same page'
        self.user.refresh_from_db()
        assert self.user.check_password('P455w0rd_testing') is True, \
            'The password should not have changed.'
        self.assertTrue(form.errors)  # Form has errors
