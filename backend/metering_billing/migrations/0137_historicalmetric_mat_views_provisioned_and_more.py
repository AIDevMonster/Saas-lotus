# Generated by Django 4.0.5 on 2023-01-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0136_remove_metric_unique_org_event_name_metric_type_and_other_fields_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmetric',
            name='mat_views_provisioned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='metric',
            name='mat_views_provisioned',
            field=models.BooleanField(default=False),
        ),
    ]
