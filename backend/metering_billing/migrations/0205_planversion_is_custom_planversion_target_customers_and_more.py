# Generated by Django 4.0.5 on 2023-02-24 22:56

import metering_billing.utils.utils
from django.db import migrations, models


def transfer_custom_plans(apps, schema_editor):
    Plan = apps.get_model("metering_billing", "Plan")

    for plan in Plan.objects.filter(target_customer__isnull=False):
        parent_plan = plan.parent_plan
        num_versions_in_parent = parent_plan.versions.count()
        i = 1
        for version in plan.versions.all():
            version.version = num_versions_in_parent + i
            version.plan = parent_plan
            version.target_customers.add(plan.target_customer)
            version.is_custom = True
            version.save()
            i += 1
    Plan.objects.filter(target_customer__isnull=False).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0204_alter_idempotencecheck_time_created"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="plan",
            name="both_null_or_both_not_null",
        ),
        migrations.AddField(
            model_name="planversion",
            name="is_custom",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="planversion",
            name="target_customers",
            field=models.ManyToManyField(
                related_name="plan_versions", to="metering_billing.customer"
            ),
        ),
        migrations.AlterField(
            model_name="historicalplan",
            name="created_on",
            field=models.DateTimeField(default=metering_billing.utils.utils.now_utc),
        ),
        migrations.AlterField(
            model_name="plan",
            name="created_on",
            field=models.DateTimeField(default=metering_billing.utils.utils.now_utc),
        ),
        migrations.DeleteModel(
            name="HistoricalPlanVersion",
        ),
        migrations.RunPython(transfer_custom_plans),
    ]
