from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from .validators import validate_alpha


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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.plan_type)
        super().save(*args, **kwargs)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given name, email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular User with the given email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model."""
    slug = models.SlugField()
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        validators=[MinLengthValidator(3), validate_alpha],
        null=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        validators=[MinLengthValidator(3), validate_alpha],
        null=True
    )
    email = models.EmailField(_('email'), unique=True)
    institution = models.CharField(max_length=100, null=True)
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
        related_name='users',
        on_delete=models.SET_NULL,
        null=True
    )
    stripe_customer_id = models.CharField(max_length=40)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # required when create a superuser
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        complete_name = '{0} {1}'.format(self.first_name, self.last_name)
        self.slug = slugify(complete_name)
        super().save(*args, **kwargs)


class Subscription(models.Model):
    """
    Subscripción del usuario a la que pertenecen todos los datos del pago
    por medio de Stripe

    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Subscription."""

        db_table = 'subscripciones'
        verbose_name_plural = 'subscripciones'

    def __str__(self):
        """Unicode representation of Subscription."""
        return self.user.username
