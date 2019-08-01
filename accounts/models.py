from datetime import datetime
from io import BytesIO

import stripe
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.core.validators import (FileExtensionValidator, MaxValueValidator,
                                    MinLengthValidator)
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from PIL import Image

from accounts.helpers import get_logo_path, get_photo_path

from .validators import validate_alpha

stripe.api_key = settings.STRIPE_SECRET_KEY


class Plan(models.Model):
    """Tipo de plan al que el usuario se subscribe."""
    FREE = 'GRATIS'
    MONTHLY = 'MENSUAL'
    YEARLY = 'ANUAL'
    PERPETUAL = 'PAGO ÚNICO'
    PLAN_CHOICES = (
        (PERPETUAL, 'Perpetual'),
        (YEARLY, 'Yearly'),
        (MONTHLY, 'Monthly'),
        (FREE, 'Free'),
    )
    slug = models.SlugField()
    plan_type = models.CharField(
        choices=PLAN_CHOICES,
        default=FREE,
        max_length=30
    )
    price = models.PositiveIntegerField(validators=[
                                        MaxValueValidator(100000)])
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

    def get_absolute_url(self):
        """Defines the absolute url for plans, which is the checkout view"""
        if self.plan_type != 'GRATIS':
            return reverse('checkout',
                           kwargs={'plan_id': self.pk, 'plan_slug': self.slug})

    @property
    def real_price(self):
        return self.price / 100


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
        extra_fields.setdefault('is_premium', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_premium') is not True:
            raise ValueError('Superuser must have is_premium=True.')

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
    photo = models.ImageField(
        upload_to=get_photo_path,
        verbose_name='foto',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(
            ('gif', 'bmp', 'jpeg', 'jpg', 'png'))]
    )
    email = models.EmailField(_('email'), unique=True)
    institution = models.CharField(max_length=100, null=True)
    institution_logo = models.ImageField(
        upload_to=get_logo_path,
        verbose_name='logo de la institución',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(
            ('gif', 'bmp', 'jpeg', 'jpg', 'png'))]
    )
    allow_notifications = models.BooleanField(default=True)
    email_confirmed = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=40)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    plans = models.ManyToManyField(Plan, through='Subscription')
    is_premium = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # required when create a superuser
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        """
        Creates the user's slug, and modifies the institution logo and
        photo before saving
        """
        # User slug
        complete_name = '{0} {1}'.format(self.first_name, self.last_name)
        self.slug = slugify(complete_name)

        self.username = self.email  # The username equals the email

        if self.institution_logo:
            # Converting imagefield to pil image
            logo = Image.open(self.institution_logo)
            maxsize = (150, 150)
            logo.thumbnail(maxsize, Image.ANTIALIAS)

            # Converting pil image to imagefield
            # Binary stream
            stream = BytesIO()
            try:
                # Saving file
                # saves modified file to binary stream
                logo.save(stream, format=logo.format)

                # Deletes previous logo
                this = User.objects.get(id=self.id)
                if this.institution_logo != self.institution_logo:
                    this.institution_logo.delete(save=False)

                    # creates the image field from modified image in stream
                    self.institution_logo.save(self.institution_logo.name,
                                               File(stream), save=False)
            except IOError:
                pass
            finally:
                stream.close()

        if self.photo:
            # Deletes previous photo
            this = User.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)

        if not self.stripe_customer_id:
            new_customer_id = stripe.Customer.create(email=self.email)
            self.stripe_customer_id = new_customer_id.get('id')

        # Saves in database
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Defines the absolute url for users which is the profile view"""
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.slug})

    def cancel_active_subscription(self):
        # deactivates current active subscription if exists
        active_subscription = self.active_subscription
        if active_subscription:
            active_subscription.cancel_subscription()

            # refunds the ammount for the days left to finish the period
            next_billing_date = active_subscription.next_billing_date
            last_billing_date = active_subscription.last_billing_date
            today = datetime.now()
            days_left = abs((next_billing_date - today).days)
            total_days = abs((next_billing_date - last_billing_date).days)
            amount_day = active_subscription.plan.price / total_days
            amount = round(days_left * amount_day)

            stripe.Refund.create(
                charge=active_subscription.stripe_charge_id,
                amount=amount,
            )

        try:
            # Gets the subscription to free plan if exists
            free_subscription = Subscription.objects.get(
                plan__plan_type='GRATIS', user=self)

            if free_subscription:
                # activates previous free subscription
                free_subscription.active = True
                free_subscription.save()

        except Subscription.DoesNotExist:
            try:
                # gets the free plan if exists
                free_plan = Plan.objects.get(plan_type="GRATIS")
            except Plan.DoesNotExist:
                # if free plan does not exist, creates a new one
                free_plan = Plan.objects.create(plan_type="GRATIS", price=0.00)

            # user subscribes to free plan
            Subscription.objects.create_subscription(
                self,
                free_plan,
            )

    def soft_delete(self):
        """Soft deletes user (sets is_active to False)"""
        self.is_active = False
        self.save()

    @property
    def full_name(self):
        """Gets the user's full name"""
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def get_logo(self):
        """
        Gets the logo url if exists, otherwise takes the default logo
        """
        if not self.institution_logo:
            url = static('img/defaults/default-school-logo.png')
            return url
        else:
            return self.institution_logo.url

    @property
    def get_photo(self):
        """
        Gets the photo url if exists, otherwise takes the default photo
        """
        if not self.photo:
            url = static('img/defaults/user.png')
            return url
        else:
            return self.photo.url

    @property
    def active_subscription(self):
        """
        Gets the user's active subscription
        """
        try:
            active_subscription = self.subscriptions.get(active=True)
            return active_subscription
        except Subscription.DoesNotExist:
            return False
        except Exception:
            return False

    @property
    def active_plan(self):
        """
        Gets the user's active plan
        """
        try:
            active_subscription = self.subscriptions.get(active=True)
            return active_subscription.plan
        except Subscription.DoesNotExist:
            return False
        except Exception:
            return False


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user_create(sender, instance, created, **kwargs):
    """Señal que agrega el plan GRATIS a un usuario recién creado"""
    try:
        if not instance.active_subscription:
            free_plan = None
            try:
                free_plan = Plan.objects.get(plan_type='GRATIS')
            except Plan.DoesNotExist:
                # if free plan does not exist, creates a new one
                free_plan = Plan.objects.create(plan_type="GRATIS", price=0.00)

            Subscription.objects.create_subscription(
                instance,
                free_plan,
            )
    except Plan.DoesNotExist:
        pass
    except Exception:
        pass


class SubscriptionManager(models.Manager):
    def create_subscription(self, user, plan, token='', *args, **kwargs):
        """
        Creates a user subscriprion depending on the token existance
        and the plan type
        """
        active_subscription = user.active_subscription

        if token:
            if plan.plan_type == 'PAGO ÚNICO':
                # Stripe subscription creation
                stripe.Customer.modify(
                    user.stripe_customer_id,
                    source=token
                )

                # Stripe payment
                stripe_charge = stripe.Charge.create(
                    customer=user.stripe_customer_id,
                    amount=plan.price,
                    currency='usd',
                    description='Plan {} | Asistente de Cátedra'
                    .format(plan.plan_type),
                )

                if stripe_charge:
                    # Database subscription creation
                    with transaction.atomic():
                        # Cancel previous subscriptions if any
                        if active_subscription:
                            active_subscription.cancel_subscription()
                        subscription = Subscription.objects.create(
                            user=user,
                            plan=plan,
                            stripe_charge_id=stripe_charge.id
                        )
                        return subscription
            else:
                # Stripe subscription creation
                stripe.Customer.modify(
                    user.stripe_customer_id,
                    source=token
                )

                stripe_subscription = stripe.Subscription.create(
                    customer=user.stripe_customer_id,
                    items=[
                        {
                            'plan': plan.stripe_plan_id
                        }
                    ]
                )
                if stripe_subscription:
                    # Database subscription creation
                    # If there is an active subscription delete subscription
                    # Stripe before saving the new subscription
                    with transaction.atomic():
                        if active_subscription:
                            active_subscription.cancel_subscription()
                        subscription = Subscription.objects.create(
                            user=user,
                            plan=plan,
                            stripe_subscription_id=stripe_subscription.id
                        )
                        return subscription
        else:
            if active_subscription:
                active_subscription.cancel_subscription()
            subscription = Subscription.objects.create(
                user=user,
                plan=plan,
            )
            return subscription


class Subscription(models.Model):
    """
    Subscripción del usuario a la que pertenecen todos los datos del pago
    por medio de Stripe

    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='subscriptions',
        on_delete=models.CASCADE,
    )
    plan = models.ForeignKey(
        Plan,
        related_name='subscriptions',
        on_delete=models.CASCADE,
    )
    stripe_subscription_id = models.CharField(max_length=40, null=True,
                                              blank=True)
    stripe_charge_id = models.CharField(max_length=40, null=True,
                                        blank=True)
    active = models.BooleanField(default=True)
    objects = SubscriptionManager()

    class Meta:
        """Meta definition for Subscription."""

        db_table = 'subscripciones'
        verbose_name_plural = 'subscripciones'

    def __str__(self):
        """Unicode representation of Subscription."""
        return self.user.username

    @property
    def created_date(self):
        if self.user.is_premium:
            subscription = stripe.Subscription.retrieve(
                self.stripe_subscription_id)
            return datetime.fromtimestamp(subscription.created)
        return self.user.date_joined

    @property
    def last_billing_date(self):
        if self.user.is_premium:
            subscription = stripe.Subscription.retrieve(
                self.stripe_subscription_id)
            return datetime.fromtimestamp(subscription.current_period_start)
        return False

    @property
    def next_billing_date(self):
        if self.user.is_premium:
            subscription = stripe.Subscription.retrieve(
                self.stripe_subscription_id)
            return datetime.fromtimestamp(subscription.current_period_end)
        return False

    def cancel_subscription(self):
        if self.stripe_subscription_id:
            subscription = stripe.Subscription.retrieve(
                self.stripe_subscription_id)
            subscription.delete()
        self.active = False
        self.save()
