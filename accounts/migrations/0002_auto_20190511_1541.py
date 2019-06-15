from django.conf import settings
from django.db import migrations
from django.template.defaultfilters import slugify


def create_pĺans(apps, schema_editor):
    Plan = apps.get_model('accounts', 'Plan')
    Plan.objects.bulk_create([
        Plan(
            plan_type='GRATIS',
            price=0,
        ),
        Plan(
            plan_type='MENSUAL',
            price=499,
            stripe_plan_id=settings.STRIPE_MONTHLY_ID
        ),
        Plan(
            plan_type='ANUAL',
            price=6999,
            stripe_plan_id=settings.STRIPE_YEARLY_ID
        ),
        Plan(
            plan_type='PAGO ÚNICO',
            price=11976,
        ),
    ])

    plans = Plan.objects.all()
    for plan in plans:
        plan.slug = slugify(plan.plan_type)
        plan.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_pĺans,
                             reverse_code=migrations.RunPython.noop)
    ]
