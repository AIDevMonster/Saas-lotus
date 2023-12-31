# Generated by Django 4.0.5 on 2022-10-04 03:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0031_subscription_auto_renew_billing_plan_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subscription",
            old_name="subscription_uid",
            new_name="subscription_id",
        ),
        migrations.AlterUniqueTogether(
            name="subscription",
            unique_together={("organization", "subscription_id")},
        ),
    ]
