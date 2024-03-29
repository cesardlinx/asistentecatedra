import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LogoutView
from django.urls import resolve, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from mixer.backend.django import mixer
from accounts import views

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestAccountsUrls(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)

    def test_signup(self):
        path = reverse('signup')
        view = resolve(path)
        assert view.func.view_class == views.SignupView, \
            'Should resolve to the Signup View'

    def test_send_confirmation(self):
        path = reverse('send_confirmation')
        view = resolve(path)
        assert view.func == views.send_confirmation_view, \
            'Should resolve to the send_confirmation_view View'

    def test_confirm_email(self):
        user = mixer.blend(User)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        path = reverse('confirm_email', kwargs={
            'uidb64': uid,
            'token': token
        })
        view = resolve(path)
        assert view.func == views.confirm_email_view, \
            'Should resolve to the confirm_email_view View'

    def test_profile(self):
        user = mixer.blend(User)
        path = reverse('profile', kwargs={'pk': user.pk, 'slug': user.slug})
        view = resolve(path)
        assert view.func.view_class == views.ProfileView, \
            'Should resolve to the Profile View'

    def test_photo_upload(self):
        path = reverse('photo_upload')
        view = resolve(path)
        assert view.func == views.photo_upload_view, \
            'Should resolve to the PhotoUpload View'

    def test_login(self):
        path = reverse('login')
        view = resolve(path)
        assert view.func.view_class == views.CustomLoginView, \
            'Should resolve to the Login View'

    def test_logout(self):
        path = reverse('logout')
        view = resolve(path)
        assert view.func.view_class == LogoutView, \
            'Should resolve to the Logout View'

    # Password reset
    def test_password_reset(self):
        path = reverse('password_reset')
        view = resolve(path)
        assert view.func.view_class == views.CustomPasswordResetView, \
            'Should resolve to the PasswordReset View'

    def test_password_reset_confirm(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        path = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        view = resolve(path)
        assert view.func.view_class == views.CustomPasswordResetConfirmView, \
            'Should resolve to the PasswordResetConfirm View'

    # Password Change
    def test_password_change(self):
        path = reverse('password_change')
        view = resolve(path)
        assert view.func.view_class == views.CustomPasswordChangeView, \
            'Should resolve to the PasswordChange View'

    # Ajax unique email validator
    def test_unique_email_validator(self):
        path = reverse('ajax_unique_email_validator')
        view = resolve(path)
        assert view.func == views.unique_email_validator, \
            'Should resolve to the unique_email_validator View'

    def test_user_delete(self):
        path = reverse('user_delete', kwargs={
            'pk': self.user.pk
        })
        view = resolve(path)
        assert view.func.view_class == views.UserDeleteView, \
            'Should return the UserDeleteView'
