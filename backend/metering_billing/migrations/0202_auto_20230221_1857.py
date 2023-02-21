# Generated by Django 4.0.5 on 2023-02-21 18:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0201_auto_20230221_0345"),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION insert_metric(
                p_organization_id integer,
                p_cust_id text,
                p_event_name text,
                p_time_created timestamp with time zone,
                p_properties jsonb,
                p_idempotency_id text
            ) RETURNS VOID AS $$ DECLARE 
            
            uuidv5_event_name uuid;
            uuidv5_idempotency_id uuid;
            uuidv5_customer_id uuid;

            BEGIN 
            
            uuidv5_customer_id := uuid_generate_v5(
                'D1337E57-E6A0-4650-B1C3-D6487AFFB8CA' :: uuid,
                p_cust_id
            );

            uuidv5_event_name := uuid_generate_v5(
                '843D7005-63DE-4B72-B731-77E2866DCCFF' :: uuid,
                p_event_name
            );

            uuidv5_idempotency_id := uuid_generate_v5(
                '904C0FFB-7005-414E-9B7D-8E3C5DDE266D' :: uuid,
                p_idempotency_id
            );

            INSERT INTO
                metering_billing_idempotencecheck (
                    organization_id,
                    time_created,
                    uuidv5_idempotency_id
                )
            VALUES
                (
                    p_organization_id,
                    p_time_created,
                    uuidv5_idempotency_id
                ) ON CONFLICT DO NOTHING;

            IF FOUND THEN
            INSERT INTO
                metering_billing_usageevent (
                    organization_id,
                    cust_id,
                    uuidv5_customer_id,
                    event_name,
                    uuidv5_event_name,
                    idempotency_id,
                    uuidv5_idempotency_id,
                    properties,
                    time_created,
                    inserted_at
                )
            VALUES
                (
                    p_organization_id,
                    p_cust_id,
                    uuidv5_customer_id,
                    p_event_name,
                    uuidv5_event_name,
                    p_idempotency_id,
                    uuidv5_idempotency_id,
                    p_properties,
                    p_time_created,
                    CURRENT_TIMESTAMP
                );

            END IF;

            END;

            $$ LANGUAGE plpgsql;
            """,
            reverse_sql="DROP FUNCTION IF EXISTS insert_metric(p_organization_id integer, p_cust_id text, p_event_name text, p_time_created timestamp, p_properties jsonb, p_idempotency_id text);",
        ),
        migrations.RunSQL(
            """ALTER TABLE metering_billing_idempotencecheck DROP CONSTRAINT IF EXISTS metering_billing_idempot_uuidv5_idempotency_id_262f86d2_uniq;""",
        ),
    ]
