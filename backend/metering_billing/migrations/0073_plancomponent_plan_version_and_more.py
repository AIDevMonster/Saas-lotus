# Generated by Django 4.0.5 on 2022-11-13 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0072_customer_payment_provider_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="plancomponent",
            name="plan_version",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plan_components",
                to="metering_billing.planversion",
            ),
        ),
        migrations.AlterField(
            model_name="plancomponent",
            name="billable_metric",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="metering_billing.billablemetric",
            ),
        ),
        migrations.CreateModel(
            name="PriceTier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("flat", "Flat"),
                            ("per_unit", "Per Unit"),
                            ("free", "Free"),
                        ],
                        max_length=10,
                    ),
                ),
                ("range_start", models.DecimalField(decimal_places=10, max_digits=20)),
                (
                    "range_end",
                    models.DecimalField(
                        blank=True, decimal_places=10, max_digits=20, null=True
                    ),
                ),
                (
                    "cost_per_batch",
                    models.DecimalField(
                        blank=True, decimal_places=10, max_digits=20, null=True
                    ),
                ),
                (
                    "metric_units_per_batch",
                    models.DecimalField(
                        blank=True, decimal_places=10, max_digits=20, null=True
                    ),
                ),
                (
                    "batch_rounding_type",
                    models.CharField(
                        choices=[
                            ("round_up", "Round Up"),
                            ("round_down", "Round Down"),
                            ("round_nearest", "Round Nearest"),
                            ("no_rounding", "No Rounding"),
                        ],
                        default="no_rounding",
                        max_length=20,
                    ),
                ),
                (
                    "plan_component",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tiers",
                        to="metering_billing.plancomponent",
                    ),
                ),
            ],
        ),
    ]
