# Generated by Django 4.0.5 on 2023-03-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0238_analysis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorganization',
            name='gen_cust_in_braintree_after_lotus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalorganization',
            name='gen_cust_in_stripe_after_lotus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalorganization',
            name='lotus_is_customer_source_for_salesforce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalorganization',
            name='payment_grace_period',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='organization',
            name='gen_cust_in_braintree_after_lotus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='gen_cust_in_stripe_after_lotus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='lotus_is_customer_source_for_salesforce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='payment_grace_period',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='organizationsetting',
            name='setting_name',
            field=models.CharField(choices=[('generate_customer_after_creating_in_lotus', 'Generate in Stripe after Lotus'), ('gen_cust_in_braintree_after_lotus', 'Generate in Braintree after Lotus'), ('payment_grace_period', 'Payment Grace Period'), ('crm_customer_source', 'CRM Customer Source')], max_length=64),
        ),
    ]