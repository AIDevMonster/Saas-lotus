# Generated by Django 4.0.5 on 2022-10-09 00:10

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0036_categoricalfilter_numericfilter_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billablemetric",
            name="billable_metric_name",
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=200),
        ),
    ]
