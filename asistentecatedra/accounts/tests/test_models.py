import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from accounts.models import Profile, Plan, Subscription
pytestmark = pytest.mark.django_db


class TestPlan:
    def test_model(self):
        plan = mixer.blend('accounts.Plan')
        assert isinstance(plan, Plan), 'Should be an instance of Plan'
        assert str(plan) == plan.plan_type, \
            "The string representation should be the plan's type"
        assert plan._meta.db_table == 'planes', \
            'The table should be named "planes"'
        assert plan._meta.verbose_name_plural == 'planes', \
            'The plural name should be "planes"'


class TestProfile:
    """Tests del modelo para perfil de usuario"""
    def test_model(self):
        user = User.objects.create_user(
            username='tester',
            email='tester@tester.com',
            password='p455w0rd'
        )
        profile = user.profile

        assert isinstance(profile, Profile), 'Should be an instance of Profile'
        assert isinstance(profile.user, User), \
            'Should be an instance of Profile'
        assert str(profile) == profile.user.username, \
            "The string representation should be the user's username"
        assert profile._meta.db_table == 'perfiles', \
            'The table should be named "areas"'
        assert profile._meta.verbose_name_plural == 'perfiles', \
            'The plural name should be "áreas"'


class TestSubscription:
    def test_model(self):
        user = mixer.blend('auth.User')
        subscription = mixer.blend('accounts.Subscription',
                                   profile=user.profile)
        assert isinstance(subscription, Subscription), \
            'Should be an instance of Subscription'
        assert str(subscription) == subscription.profile.user.username, \
            "The string representation should be the plan's type"
        assert subscription._meta.db_table == 'subscripciones', \
            'The table should be named "subscripciones"'
        assert subscription._meta.verbose_name_plural == 'subscripciones', \
            'The plural name should be "subscripciones"'
