# Generated by Django 4.0.5 on 2022-09-06 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0004_alter_invoice_status_alter_organization_stripe_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="payment_intent_id",
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
