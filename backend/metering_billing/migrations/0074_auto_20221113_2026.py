# Generated by Django 4.0.5 on 2022-11-13 20:26

from django.db import migrations

from metering_billing.utils.enums import BATCH_ROUNDING_TYPE, PRICE_TIER_TYPE


def migrate_plancomponetns_to_price_tiers(apps, schema_editor):
    PlanComponent = apps.get_model("metering_billing", "PlanComponent")
    PriceTier = apps.get_model("metering_billing", "PriceTier")
    PlanVersion = apps.get_model("metering_billing", "PlanVersion")

    for pv in PlanVersion.objects.all().prefetch_related("components"):
        for pc in pv.components.all():
            new_pc = PlanComponent.objects.create(
                billable_metric=pc.billable_metric,
                plan_version=pv,
            )
            starting_point = 0
            if pc.free_metric_units and pc.free_metric_units > 0:
                PriceTier.objects.create(
                    plan_component=new_pc,
                    metric_units_per_batch=pc.free_metric_units,
                    type=PRICE_TIER_TYPE.FREE,
                    range_start=0,
                    range_end=pc.free_metric_units,
                )
                starting_point = pc.free_metric_units
            price_tier_dict = {
                "plan_component": new_pc,
                "type": PRICE_TIER_TYPE.PER_UNIT,
                "range_start": starting_point,
                "cost_per_batch": pc.cost_per_batch,
                "metric_units_per_batch": pc.metric_units_per_batch,
                "batch_rounding_type": BATCH_ROUNDING_TYPE.NO_ROUNDING,
                "range_end": None,
            }
            if pc.max_metric_units and pc.max_metric_units > 0:
                price_tier_dict["range_end"] = pc.max_metric_units
            PriceTier.objects.create(**price_tier_dict)
    PlanComponent.objects.filter(plan_version__isnull=True).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0073_plancomponent_plan_version_and_more"),
    ]

    operations = [
        migrations.RunPython(migrate_plancomponetns_to_price_tiers),
    ]
