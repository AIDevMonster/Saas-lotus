# Generated by Django 4.0.5 on 2022-09-18 21:15

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0010_alter_invoice_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billingplan",
            name="billing_plan_id",
            field=models.CharField(
                default=uuid.UUID("17aa5637-c1e8-4114-8228-3b076b5aee0d"),
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="billingplan",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
