# Generated by Django 2.2.1 on 2019-08-01 04:36

import accounts.helpers
import accounts.models
import accounts.validators
from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('slug', models.SlugField()),
                ('first_name', models.CharField(max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3), accounts.validators.validate_alpha], verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3), accounts.validators.validate_alpha], verbose_name='last name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=accounts.helpers.get_photo_path, validators=[django.core.validators.FileExtensionValidator(('gif', 'bmp', 'jpeg', 'jpg', 'png'))], verbose_name='foto')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('institution', models.CharField(max_length=100, null=True)),
                ('institution_logo', models.ImageField(blank=True, null=True, upload_to=accounts.helpers.get_logo_path, validators=[django.core.validators.FileExtensionValidator(('gif', 'bmp', 'jpeg', 'jpg', 'png'))], verbose_name='logo de la institución')),
                ('allow_notifications', models.BooleanField(default=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('stripe_customer_id', models.CharField(max_length=40)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_premium', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('plan_type', models.CharField(choices=[('PAGO ÚNICO', 'Perpetual'), ('ANUAL', 'Yearly'), ('MENSUAL', 'Monthly'), ('GRATIS', 'Free')], default='GRATIS', max_length=30)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100000)])),
                ('stripe_plan_id', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'planes',
                'db_table': 'planes',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=40, null=True)),
                ('stripe_charge_id', models.CharField(blank=True, max_length=40, null=True)),
                ('active', models.BooleanField(default=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='accounts.Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'subscripciones',
                'db_table': 'subscripciones',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='plans',
            field=models.ManyToManyField(through='accounts.Subscription', to='accounts.Plan'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
