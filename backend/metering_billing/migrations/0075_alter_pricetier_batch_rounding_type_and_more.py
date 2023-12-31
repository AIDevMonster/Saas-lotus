# Generated by Django 4.0.5 on 2022-11-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0074_auto_20221113_2026"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pricetier",
            name="batch_rounding_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("round_up", "Round Up"),
                    ("round_down", "Round Down"),
                    ("round_nearest", "Round Nearest"),
                    ("no_rounding", "No Rounding"),
                ],
                default="no_rounding",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="pricetier",
            name="metric_units_per_batch",
            field=models.DecimalField(
                blank=True, decimal_places=10, default=1.0, max_digits=20, null=True
            ),
        ),
    ]
