import os
from base64 import urlsafe_b64encode

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import (LoginView, PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from mixer.backend.django import mixer
from PIL import Image
from accounts.forms import SignupForm

from accounts import views

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestSignupView(TestCase):
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
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password1"')
        self.assertContains(response, 'name="password2"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="first_name"')
        self.assertContains(response, 'name="last_name"')
        self.assertContains(response, 'name="institution"')
        self.assertContains(response, 'name="institution_logo"')

    def test_post_success(self):
        """
        Test for user creation and authentication
        """

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
            'username': 'tester',
            'password1': 'p455w0rd',
            'password2': 'p455w0rd',
            'email': 'tester@tester.com',
            'first_name': 'David',
            'last_name': 'Padilla',
            'institution': 'Colegio Benalcázar',
            'institution_logo': image
        }

        url = reverse('signup')
        response = self.client.post(url, data)

        # Image removal
        os.remove('media/test_image.png')

        user = User.objects.last()

        self.assertRedirects(response, reverse('planificaciones'))
        assert response.status_code == 302, \
            'Should redirect to planificaciones'
        assert User.objects.exists() is True, 'Should create a user'
        user = User.objects.last()
        assert 'logos/test_image_' in user.profile.institution_logo.name, \
            'User should have an institution logo'
        assert user.username == 'tester',  \
            "The user's username should be tester"
        # Authentication testing
        response = self.client.get(reverse('home'))
        user = response.context.get('user')
        assert user.is_authenticated is True, \
            'User should be authenticated'

    def test_optional_fields(self):
        data = {
            'username': 'tester',
            'password1': 'p455w0rd',
            'password2': 'p455w0rd',
            'email': 'tester@tester.com',
        }

        url = reverse('signup')
        self.client.post(url, data)

        user = User.objects.last()
        assert user.username == 'tester', 'Should create a user'
        assert str(user.profile) == 'tester', 'Should have a profile'
        assert user.profile.institution == ''

    def test_post_invalid(self):
        """Test for invalid data in signup"""
        url = reverse('signup')
        response = self.client.post(url, {})
        form = response.context.get('form')
        assert response.status_code == 200, \
            'Should not redirect'
        assert form.errors is not None, \
            'The form should have errors'
        assert User.objects.exists() is False, \
            'The view should not create a user'


class TestProfileView:
    """Tests para la vista de Perfil de usuario"""

    def setUp(self):
        """Creates data for testing and user"""
        super().setUp()
        self.user = mixer.blend(User)

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
        response = views.ProfileView.as_view()(request)
        assert response.status_code == 200, 'Authenticated user can access'
        # Campos en el template (Template Testing)
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password1"')
        self.assertContains(response, 'name="password2"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="first_name"')
        self.assertContains(response, 'name="last_name"')
        self.assertContains(response, 'name="institution"')
        self.assertContains(response, 'name="institution_logo"')


class TestLoginView:
    """Tests para la vista de Login"""
    def test_get(self):
        """Test access to view by anonymous"""
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = LoginView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anonymous'
        assert response.template_name == 'accounts/login.html'


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
        uid = urlsafe_b64encode(force_bytes(user.pk)).decode()
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
        uid = urlsafe_b64encode(force_bytes(user.pk)).decode()
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
