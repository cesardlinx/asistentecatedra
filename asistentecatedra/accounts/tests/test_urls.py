import pytest
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import resolve, reverse
from accounts import views
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestAccountsUrls:
    def test_signup(self):
        path = reverse('signup')
        view = resolve(path)
        assert view.func.view_class == views.SignupView, \
            'Should resolve to the Signup View'

    def test_profile(self):
        user = mixer.blend(User)
        path = reverse('profile', kwargs={'pk': user.pk, 'slug': user.slug})
        view = resolve(path)
        assert view.func.view_class == views.ProfileView, \
            'Should resolve to the Profile View'

    def test_login(self):
        path = reverse('login')
        view = resolve(path)
        assert view.func.view_class == LoginView, \
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
        assert view.func.view_class == PasswordResetView, \
            'Should resolve to the PasswordReset View'

    def test_password_reset_done(self):
        path = reverse('password_reset_done')
        view = resolve(path)
        assert view.func.view_class == PasswordResetDoneView, \
            'Should resolve to the PasswordResetDone View'

    def test_password_reset_confirm(self):
        path = reverse('password_reset_confirm')
        view = resolve(path)
        assert view.func.view_class == PasswordResetConfirmView, \
            'Should resolve to the PasswordResetConfirm View'

    def test_password_reset_complete(self):
        path = reverse('password_reset_complete')
        view = resolve(path)
        assert view.func.view_class == PasswordResetCompleteView, \
            'Should resolve to the PasswordResetComplete View'

    # Password Change
    def test_password_change(self):
        path = reverse('password_change')
        view = resolve(path)
        assert view.func.view_class == PasswordChangeView, \
            'Should resolve to the PasswordChange View'

    def test_password_change_done(self):
        path = reverse('password_change_done')
        view = resolve(path)
        assert view.func.view_class == PasswordChangeDoneView, \
            'Should resolve to the PasswordChangeDone View'

    def test_unique_email_validator(self):
        path = reverse('ajax_unique_email_validator')
        view = resolve(path)
        assert view.func == views.unique_email_validator, \
            'Should resolve to the unique_email_validator View'
