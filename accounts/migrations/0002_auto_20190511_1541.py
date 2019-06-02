from django.conf import settings
from django.db import migrations


def create_pĺans(apps, schema_editor):
    Plan = apps.get_model('accounts', 'Plan')
    Plan.objects.bulk_create([
        Plan(
            plan_type='GRATIS',
            price=0.00,
        ),
        Plan(
            plan_type='MENSUAL',
            price=4.99,
            stripe_plan_id=settings.STRIPE_MONTHLY_ID
        ),
        Plan(
            plan_type='ANUAL',
            price=69.99,
            stripe_plan_id=settings.STRIPE_YEARLY_ID
        ),
        Plan(
            plan_type='PAGO ÚNICO',
            price=199.99,
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
