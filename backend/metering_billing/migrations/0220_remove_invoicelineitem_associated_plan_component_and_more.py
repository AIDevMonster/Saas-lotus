# Generated by Django 4.0.5 on 2023-03-02 19:53

import uuid

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0219_plancomponent_invoicing_interval_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoicelineitem",
            name="billing_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("in_arrears", "In Arrears"),
                    ("intermediate", "Intermediate"),
                    ("in_advance", "In Advance"),
                    ("one_time", "One Time"),
                ],
                max_length=40,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="BillingRecord",
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
                    "billing_record_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        help_text="The start of when this service started being provided."
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        help_text="The date this service stopped being provided."
                    ),
                ),
                (
                    "unadjusted_duration_microseconds",
                    models.BigIntegerField(
                        help_text="The duration of this service in microseconds, if it had been of its full intended length without considering anchoring + intermediate periods.",
                        null=True,
                    ),
                ),
                (
                    "invoicing_dates",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.DateTimeField(), default=list, size=None
                    ),
                ),
                ("next_invoicing_date", models.DateTimeField()),
                ("fully_billed", models.BooleanField(default=False)),
                (
                    "billing_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_records",
                        to="metering_billing.planversion",
                    ),
                ),
                (
                    "component",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_records",
                        to="metering_billing.plancomponent",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_records",
                        to="metering_billing.customer",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_records",
                        to="metering_billing.organization",
                    ),
                ),
                (
                    "recurring_charge",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_records",
                        to="metering_billing.recurringcharge",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_records",
                        to="metering_billing.subscriptionrecord",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="invoicelineitem",
            name="associated_billing_record",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="line_items",
                to="metering_billing.billingrecord",
            ),
        ),
        migrations.AddConstraint(
            model_name="billingrecord",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("component__isnull", True),
                    ("recurring_charge__isnull", True),
                    _connector="OR",
                ),
                name="only_one_of_component_or_recurring_charge",
            ),
        ),
        migrations.AddConstraint(
            model_name="billingrecord",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("component__isnull", False),
                    models.Q(
                        ("recurring_charge__isnull", False),
                        ("unadjusted_duration_microseconds__isnull", False),
                    ),
                    _connector="OR",
                ),
                name="recurring_charge_requires_unadjusted_duration",
            ),
        ),
    ]
