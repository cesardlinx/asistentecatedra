from io import BytesIO

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.core.validators import (FileExtensionValidator,
                                    MinLengthValidator)
from django.db import models
from django.template.defaultfilters import slugify
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image

from accounts.helpers import get_logo_path, get_photo_path

from .validators import validate_alpha


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
    modified_at = models.DateTimeField(auto_now=True, editable=False)
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

        # Saves in database
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Defines the absolute url for users which is the profile view"""
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.slug})

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

