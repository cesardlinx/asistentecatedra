from django.conf import settings
from django.db import migrations


def create_pĺans(apps, schema_editor):
    Plan = apps.get_model('accounts', 'Plan')
    Plan.objects.bulk_create([
        Plan(
            plan_type='FREE',
            price=0.00,
            stripe_plan_id=settings.STRIPE_FREE_ID
        ),
        Plan(
            plan_type='MONTHLY',
            price=4.99,
            stripe_plan_id=settings.STRIPE_MONTHLY_ID
        ),
        Plan(
            plan_type='YEARLY',
            price=69.99,
            stripe_plan_id=settings.STRIPE_YEARLY_ID
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_pĺans,
                             reverse_code=migrations.RunPython.noop)
    ]
