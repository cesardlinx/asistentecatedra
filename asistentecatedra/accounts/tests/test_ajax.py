import pytest
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from accounts import views
pytestmark = pytest.mark.django_db

User = get_user_model()


class TestUniqueEmailValidatorView(TestCase):
    def setUp(self):
        self.user = mixer.blend(User, email='tester@tester.com')

    def test_not_ajax(self):
        request = RequestFactory().post('/',
                                        {'email': 'tester@tester.com'})
        request.user = AnonymousUser()
        response = views.unique_email_validator(request)
        self.assertContains(response, 'false')

    def test_email_exists(self):
        request = RequestFactory().post('/',
                                        {'email': 'tester@tester.com'},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = views.unique_email_validator(request)
        self.assertContains(response, 'false')

    def test_email_no_exists(self):
        request = RequestFactory().post('/',
                                        {'email': 'david@tester.com'},
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request.user = AnonymousUser()
        response = views.unique_email_validator(request)
        self.assertContains(response, 'true')
