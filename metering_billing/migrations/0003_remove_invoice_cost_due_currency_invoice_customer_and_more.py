# Generated by Django 4.0.5 on 2022-08-16 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0002_rename_stripe_api_key_organization_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='cost_due_currency',
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='metering_billing.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='cost_due',
            field=models.IntegerField(default=0),
        ),
    ]
