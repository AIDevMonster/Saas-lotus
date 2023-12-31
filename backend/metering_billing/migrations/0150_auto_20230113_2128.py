# Generated by Django 4.0.5 on 2023-01-13 21:28

from django.db import migrations


def transfer_invoice_status(apps, schema_editor):
    Invoice = apps.get_model("metering_billing", "Invoice")
    for inv in Invoice.objects.all():
        if inv.payment_status_old == "draft":
            inv.payment_status = 1
        elif inv.payment_status_old == "voided":
            inv.payment_status = 2
        elif inv.payment_status_old == "paid":
            inv.payment_status = 3
        elif inv.payment_status_old == "unpaid":
            inv.payment_status = 4
        inv.save()


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0149_historicalinvoice_payment_status_and_more"),
    ]

    operations = [
        migrations.RunPython(
            transfer_invoice_status, reverse_code=migrations.RunPython.noop
        ),
    ]
