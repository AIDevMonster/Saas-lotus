# Generated by Django 4.0.5 on 2023-02-26 22:54

from django.db import migrations


def fill_pricing_units(apps, schema_editor):
    PlanVersion = apps.get_model("metering_billing", "PlanVersion")
    for plan_version in PlanVersion.objects.filter(currency__isnull=True):
        plan_version.currency = plan_version.organization.currency
        plan_version.save()


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0217_remove_historicalsubscriptionrecord_last_billing_date_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(fill_pricing_units),
    ]
