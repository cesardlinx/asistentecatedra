from unittest.mock import patch
import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.messages import get_messages
from django.contrib.sites.models import Site
from django.core import mail
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from testfixtures import LogCapture
from accounts import views
from accounts.forms import PhotoForm, SignupForm

from .conftest import (clean_test_files,
                       create_test_image,
                       add_middleware_to_request)

pytestmark = pytest.mark.django_db
User = get_user_model()


class SignupTestCase(TestCase):
    """
    TestCase general con todos los datos de un usuario de prueba
    """
    def setUp(self):
        self.logger = LogCapture()

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

    def tearDown(self):
        # stopping log capture
        self.logger.uninstall()


class AuthTestCase(TestCase):
    """TestCase general con los dátos básicos para crear un usuario"""

    def setUp(self):
        self.logger = LogCapture()

        self.user = User.objects.create_user(
            email='tester@tester.com',
            password='P455w0rd_testing',
            first_name='David',
            last_name='Padilla',
            institution='Colegio Benalcazar'
        )

    def tearDown(self):
        # stopping log capture
        self.logger.uninstall()


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
    def test_form_valid(self, mock_recaptcha):
        """
        Test for user creation and authentication
        """
        # Mocking recaptcha
        mock_recaptcha.return_value = True

        response = self.client.post(self.url, self.data, follow=True)
        user = User.objects.last()

        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1, 'There should be one message'
        assert 'Exito!, un email ha sido enviado a tu correo para que '\
               'verifiques tu cuenta.' == messages[0].message, \
               'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'There should be a success message.'
        self.assertRedirects(response, reverse('planificaciones'))
        assert User.objects.exists() is True, 'Should create a user'
        user = User.objects.last()
        assert user.first_name == 'David',  \
            "The user's first name should be David"
        assert user.email_confirmed is False, \
            "Email shouldn't be confirmed"
        assert len(mail.outbox) == 1, 'Should exist an email in outbox'
        user = response.context.get('user')
        assert user.is_authenticated is True, \
            'User should be authenticated'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Confirmation email sent to {}'.format(user.email) \
            in str(self.logger), 'Log from confirmation sending'

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
        assert ('reCAPTCHA no válido. Por favor intente de nuevo recargando '
                'la página.') == messages[0].message, \
            'Should return error message'
        assert messages[0].tags == 'alert-danger', \
            'There should be an error message.'

        assert 'ERROR' in str(self.logger), 'Should return an error log'
        assert 'reCAPTCHA invalid error.' in str(self.logger), \
            'Error Log from reCAPTCHA error'

    @patch("accounts.views.CheckRecaptchaMixin.is_recaptcha_valid",
           autospec=True)
    def test_form_invalid(self, mock_recaptcha):
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


class TestSendConfirmationView(AuthTestCase):
    """
    Caso de prueba para probar el correo electrónico enviado al usuario
    independiente del registro para que este pueda verificar su email.
    """
    def setUp(self):
        super().setUp()
        self.url = reverse('send_confirmation')

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.send_confirmation_view(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_can_access_only_through_get(self):
        """Tests the view can't be access by a get method"""
        request = RequestFactory().head('/')
        request.user = self.user
        request = add_middleware_to_request(request)
        response = views.send_confirmation_view(request)
        assert response.status_code == 405, 'Method should not be allowed'

    def test_user_sent_confirmation_email(self):
        """
        Tests user sends a confirmation email
        """
        self.client.login(email=self.user.email, password='P455w0rd_testing')
        response = self.client.get(
            self.url,
            follow=True
        )
        messages = list(response.context.get('messages'))
        assert ('Un mensaje ha sido enviado a tu correo para que '
                'verifiques tu cuenta.') == messages[0].message
        assert len(mail.outbox) == 1, 'Should send the email'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Confirmation email sent to {}'.format(self.user.email) \
            in str(self.logger), 'Log from confirmation sending'

    def test_user_has_email_already_confirmed(self):
        """
        Tests that when a user has already confirmed his email
        no email is send
        """
        self.user.email_confirmed = True
        self.user.save()
        self.user.refresh_from_db()

        self.client.login(email=self.user.email, password='P455w0rd_testing')
        response = self.client.get(
            self.url,
            follow=True
        )
        messages = list(response.context.get('messages'))
        assert 'Su cuenta ya está verificada' == messages[0].message
        assert len(mail.outbox) == 0, 'Should not send the email'


class TestConfirmationEmail(SignupTestCase):
    """
    Caso de prueba para probar el correo electrónico enviado al usuario
    luego del registro para que este pueda verificar su email.
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
        site.domain = settings.DOMAIN
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


class TestConfirmEmailView(SignupTestCase):
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
            'confirm_email',
            kwargs={'uidb64': self.uid, 'token': self.token})

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

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'Email address: {} successfuly confirmed.'\
            .format(self.user.email) in str(self.logger),\
            'Should return a log with the email that was confirmed'

    def test_invalid_token_confirmation(self):
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

        assert 'ERROR' in str(self.logger), 'Should return an error log'
        assert "Email address can't be confirmed." in str(self.logger),\
            'Should return a log with the email that cannot be confirmed'

    def test_invalid_uid_confirmation(self):
        """
        Pruebas al recibir un link de confirmación de correo con un
        uid inválido.
        """
        confirm_url = reverse(
            'confirm_email',
            kwargs={'uidb64': 123456, 'token': self.token})
        response = self.client.get(confirm_url, follow=True)
        assert response.status_code == 200, \
            'The view should be callable by Anonymous user'
        self.user.refresh_from_db()
        assert self.user.email_confirmed is False, \
            'The user should not have the email confirmed'
        self.assertContains(
            response, 'Error. El enlace no es válido o ha expirado')

        assert 'ERROR' in str(self.logger), 'Should return an error log'
        assert "Email address can't be confirmed" in str(self.logger),\
            'Should return a log with the email that cannot be confirmed'


class TestExistsEmailValidator(AuthTestCase):
    """
    Caso de prueba para probar la vista que comprueba si existe el email
    de un usuario en la base de datos
    """
    def setUp(self):
        super().setUp()
        self.url = reverse('ajax_unique_email_validator')

    def test_post_access_only(self):
        """Solo se puede acceder a la vista mediante método post"""
        request = RequestFactory().get('/')
        response = views.exists_email_validator(request)
        assert response.status_code == 405, 'Not Allowed Method'

    def test_false_if_not_requested_through_ajax(self):
        """Si el request no viene mediante ajax retorna false"""
        request = RequestFactory().post('/', {'email': 'tester@tester.com'})
        response = views.exists_email_validator(request)
        assert response.status_code == 200
        assert response.content.decode("utf-8") == 'false'

    def test_user_exists(self):
        """Test cuando un usuario existe"""
        request = RequestFactory().post(
            '/',
            {'email': 'tester@tester.com'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        response = views.exists_email_validator(request)
        assert response.status_code == 200
        assert response.content.decode("utf-8") == 'true'

    def test_user_doesnt_exists(self):
        """Test cuando un usuario no existe"""
        request = RequestFactory().post(
            '/',
            {'email': 'asistente@tester.com'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        response = views.exists_email_validator(request)
        assert response.status_code == 200
        assert response.content.decode("utf-8") == 'false'


class TestProfileView(AuthTestCase):
    """Tests para la vista de Perfil de usuario"""

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.ProfileView.as_view()(request,
                                               pk=self.user.pk,
                                               slug=self.user.slug)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """Tests that an authenticated user can access the view"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.ProfileView.as_view()(request,
                                               pk=self.user.pk,
                                               slug=self.user.slug)
        assert response.status_code == 200, 'Authenticated user can access'
        photo_form = response.context_data.get('view').photo_form()
        assert isinstance(photo_form, PhotoForm), \
            'Should return an instance of the form for uploading a user photo'
        # Campos en el template (Template Testing)
        self.assertContains(response, 'name="first_name"')
        self.assertContains(response, 'name="last_name"')
        self.assertContains(response, 'name="institution"')
        self.assertContains(response, 'name="institution_logo"')

    def test_post_success(self):
        """Tests that user can update his data"""

        # Image creation
        image = create_test_image('test_logo.jpg', (300, 400))

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

        assert self.user.institution_logo.name is None

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
        assert self.user.institution_logo.name is not None

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'User {} has updated his data successfuly.'\
            .format(self.user.email) in str(self.logger),\
            'Should return a log with the user email that has updated his data'

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

    def tearDown(self):
        """Method to make the image removal when necesary"""
        clean_test_files()
        self.logger.uninstall()


class TestPhotoUploadView(AuthTestCase):
    """Tests for the view for users photo uploading"""
    def setUp(self):
        super().setUp()
        self.img = create_test_image('test_photo.jpg', (300, 400))

    def test_anonymous(self):
        """Tests that an anonymous user cant access"""
        data = {
            'x': 0,
            'y': 0,
            'width': 50,
            'height': 60,
            'photo': self.img
        }
        request = RequestFactory().post('/', data=data)
        request.user = AnonymousUser()
        response = views.photo_upload_view(request)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_cant_access_by_get(self):
        """Test view can't be accessed by a get request"""
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.photo_upload_view(request)
        assert response.status_code == 405, \
            'should return method not allowed error when accessing through get'

    def test_photo_upload_success(self):
        """Test when data is valid"""
        data = {
            'x': 0,
            'y': 0,
            'width': 50,
            'height': 60,
            'photo': self.img
        }
        request = RequestFactory().post('/', data=data)
        request.user = self.user
        assert self.user.photo.name is None
        response = views.photo_upload_view(request)
        self.user.refresh_from_db()
        assert response.status_code == 302, 'Should redirect to same page'
        assert self.user.email == 'tester@tester.com', \
            'User data should remain the same'
        assert self.user.photo.name is not None

    def test_invalid_data(self):
        """Test when data sent is invalid"""
        url = reverse('photo_upload')
        self.client.login(email=self.user.email,
                          password='P455w0rd_testing')
        response = self.client.post(url, data={}, follow=True)
        messages = list(response.context.get('messages'))
        assert response.status_code == 200
        assert messages[0].message == \
            'Ha ocurrido un error al intentar subir la foto.', \
            'An error message should be displayed'
        assert messages[0].tags == 'alert-danger'

    def tearDown(self):
        clean_test_files()
        self.logger.uninstall()


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
        data = {
            'username': self.user.email,
            'password': 'P455w0rd_testing'
        }
        url = reverse('login')
        response = self.client.post(url, data, follow=True)
        planificaciones_url = reverse('planificaciones')

        self.assertRedirects(response, planificaciones_url)
        user_session = response.wsgi_request.user
        assert user_session.is_authenticated is True, \
            'User should be authenticated'
        assert user_session.email == self.user.email, \
            'The session data should be the same as the database data'

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'User {} has logged in successfuly.'\
            .format(user_session.email) in str(self.logger),\
            'Should return a log with the user email that has logged in'

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

        assert 'ERROR' in str(self.logger), 'Should return an error log'
        assert 'There has been a failed login.' in str(self.logger),\
            'Should return log informing the failed login'


class TestLogoutView(AuthTestCase):
    def test_get(self):
        """Test para probar que un usuario puede cerrar sesión"""

        login_result = self.client.login(username=self.user.email,
                                         password='P455w0rd_testing')
        assert login_result is True, 'User should be logged'
        response = self.client.get(reverse('logout'))
        session_user = response.wsgi_request.user
        assert session_user.is_authenticated is False
        self.assertRedirects(response, reverse('home'))


# PASSWORD RESET TESTS
class TestPasswordResetView(AuthTestCase):
    """
    Tests the view that resets the user's password when the user has
    forgoten it
    """
    def setUp(self):
        super().setUp()
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

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'A reset password email has been sent to the email {}.'\
            .format(self.user.email) in str(self.logger),\
            'Should return a log with the user email that has requested a '\
            'reset password email'

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

        assert 'ERROR' in str(self.logger), 'Should return an error log'
        assert 'Wrong user email in a reset pasword email request.' \
            in str(self.logger), 'Should return a log the error of ' \
            'requesting with a bad user email'


class TestPasswordResetConfirmView(AuthTestCase):
    """
    Tests para probar la vista de confirmación de reset de contraseña
    """
    def setUp(self):
        super().setUp()
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


class TestPasswordResetEmail(AuthTestCase):
    def setUp(self):
        """Obtención del email"""
        super().setUp()
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


# PASSWORD CHANGE TESTS
class TestPasswordChangeView(AuthTestCase):
    """
    Tests the view that changes the user's password when
    authenticated
    """
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

        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'The user {} has successfuly changed his password.'\
            .format(self.user.email) in str(self.logger),\
            'Should return a log with the user email that has requested a '\
            'password change'

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


# User soft delete view
class TestUserDeleteView(AuthTestCase):

    def test_anonymous(self):
        """Tests that an anonymous user can't access the view"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = views.UserDeleteView.as_view()(request,
                                                  pk=self.user.pk,
                                                  slug=self.user.slug)
        assert 'login' in response.url, 'Should not be callable by anonymous'

    def test_get(self):
        """
        Tests that with a get request returns a redirection to the register.
        """
        request = RequestFactory().get('/')
        request.user = self.user
        response = views.UserDeleteView.as_view()(request,
                                                  pk=self.user.pk,
                                                  slug=self.user.slug)
        assert response.status_code == 302, 'Should return a redirection'
        assert response.url == '/', 'Should redirect to home'

    def test_soft_delete(self):
        """
        Test that user soft delete works
        """

        self.client.login(
            username='tester@tester.com',
            password='P455w0rd_testing'
        )
        assert self.user.is_active is True, 'Should be active'
        url = reverse('user_delete', kwargs={
            'pk': self.user.pk
        })
        response = self.client.post(url, {}, follow=True)
        self.user.refresh_from_db()
        assert self.user.is_active is False, 'Should not be active'
        assert response.status_code == 200, \
            'Should return a successful response'
        # Should redirect to signup
        self.assertRedirects(response, reverse('signup'))
        # Messages
        messages = list(response.context.get('messages'))
        assert len(messages) == 1, 'There should be one message'
        assert 'Tu cuenta ha sido eliminada con éxito.' \
            == messages[0].message, 'Should return a success message'
        assert messages[0].tags == 'alert-success', \
            'There should be a success message.'
        # Logs
        assert 'INFO' in str(self.logger), 'Should return an info log'
        assert 'The user {} has successfuly deleted his/her account.'\
            .format(self.user.email) in str(self.logger),\
            'Should return a log with the user email that has requested an '\
            'account deletion'
