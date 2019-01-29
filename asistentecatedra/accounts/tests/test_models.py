import pytest
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from accounts.models import Plan, Subscription
pytestmark = pytest.mark.django_db

User = get_user_model()


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


class TestUser:
    """Tests del modelo de usuario"""
    def test_model(self):
        user = mixer.blend(User)
        assert isinstance(user, User), 'Should be an instance of Profile'
        assert isinstance(user.plan, Plan), \
            'The plan field should be an instance of Plan'


class TestSubscription:
    def test_model(self):
        user = mixer.blend(User)
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
