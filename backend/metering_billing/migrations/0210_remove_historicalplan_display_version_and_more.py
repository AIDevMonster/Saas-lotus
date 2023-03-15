# Generated by Django 4.0.5 on 2023-02-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0209_remove_historicalplan_addon_spec_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalplan',
            name='display_version',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='display_version',
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planversion',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalplan',
            name='plan_name',
            field=models.TextField(help_text='Name of the plan'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_name',
            field=models.TextField(help_text='Name of the plan'),
        ),
    ]
