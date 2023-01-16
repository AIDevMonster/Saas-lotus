# Generated by Django 4.0.5 on 2022-10-29 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0055_remove_historicalplanversion_usage_billing_type_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalplan",
            name="plan_duration",
            field=models.CharField(
                choices=[
                    ("monthly", "Monthly"),
                    ("quarterly", "Quarterly"),
                    ("yearly", "Yearly"),
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="plan_duration",
            field=models.CharField(
                choices=[
                    ("monthly", "Monthly"),
                    ("quarterly", "Quarterly"),
                    ("yearly", "Yearly"),
                ],
                max_length=40,
            ),
        ),
        migrations.CreateModel(
            name="PriceAdjustment",
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
                ("price_adjustment_name", models.CharField(max_length=200)),
                (
                    "price_adjustment_description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "price_adjustment_type",
                    models.CharField(
                        choices=[
                            ("percentage", "Percentage"),
                            ("fixed", "Fixed"),
                            ("price_override", "Price Override"),
                        ],
                        max_length=40,
                    ),
                ),
                (
                    "price_adjustment_amount",
                    models.DecimalField(
                        blank=True, decimal_places=10, max_digits=20, null=True
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="org_price_adjustments",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="historicalplanversion",
            name="price_adjustment",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.priceadjustment",
            ),
        ),
        migrations.AddField(
            model_name="planversion",
            name="price_adjustment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="metering_billing.priceadjustment",
            ),
        ),
    ]
