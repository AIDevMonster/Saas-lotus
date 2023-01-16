# Generated by Django 4.0.5 on 2022-12-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "metering_billing",
            "0105_rename_pricing_unit_historicalinvoice_currency_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalorganization",
            name="webhooks_provisioned",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="organization",
            name="webhooks_provisioned",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="webhooktrigger",
            name="trigger_name",
            field=models.CharField(
                choices=[
                    ("invoice.created", "invoice.created"),
                    ("invoice.paid", "invoice.paid"),
                ],
                max_length=40,
            ),
        ),
    ]
