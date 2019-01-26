from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Plan(models.Model):
    """Tipo de plan al que el usuario se subscribe."""
    PREMIUM = 'PRO'
    FREE = 'FREE'
    PLAN_CHOICES = (
        (PREMIUM, 'Premium'),
        (FREE, 'Free'),
    )
    slug = models.SlugField()
    plan_type = models.CharField(
        choices=PLAN_CHOICES,
        default=FREE,
        max_length=30
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stripe_plan_id = models.CharField(max_length=40)

    class Meta:
        """
        Definition of table's name and the plural verbose name
        """
        db_table = 'planes'
        verbose_name_plural = 'planes'

    def __str__(self):
        """Unicode representation of Plan."""
        return self.plan_type


class Profile(models.Model):
    """Model definition for User's Profile."""
    slug = models.SlugField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100, blank=True, null=True)
    institution_logo = models.ImageField(
        upload_to='logos/',
        verbose_name='logos',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'svg'])]
    )
    allow_notifications = models.BooleanField(default=True)
    email_confirmed = models.BooleanField(default=False)
    plan = models.ForeignKey(
        Plan,
        related_name='profiles',
        on_delete=models.SET_NULL,
        null=True
    )
    stripe_customer_id = models.CharField(max_length=40)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        """
        Definition of table's name and the plural verbose name
        """
        db_table = 'perfiles'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Creates a profile when user is created"""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Subscription(models.Model):
    """
    Subscripción del usuario a la que pertenecen todos los datos del pago
    por medio de Stripe

    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Subscription."""

        db_table = 'subscripciones'
        verbose_name_plural = 'subscripciones'

    def __str__(self):
        """Unicode representation of Subscription."""
        return self.profile.user.username



