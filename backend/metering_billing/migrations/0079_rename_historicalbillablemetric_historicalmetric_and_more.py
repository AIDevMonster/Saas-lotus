# Generated by Django 4.0.5 on 2022-11-21 20:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0078_historicalorganization_organization_id_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HistoricalBillableMetric",
            new_name="HistoricalMetric",
        ),
        migrations.RenameModel(
            old_name="BillableMetric",
            new_name="Metric",
        ),
        migrations.AlterModelOptions(
            name="historicalmetric",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical metric",
            },
        ),
    ]
