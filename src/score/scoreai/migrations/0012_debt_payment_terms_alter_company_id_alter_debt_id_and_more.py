# Generated by Django 5.0.4 on 2024-05-31 22:39

import django.db.models.expressions
import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0011_alter_company_id_alter_debt_id_alter_firm_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='payment_terms',
            field=models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(models.F('principal'), '-', models.F('adjusted_amount_first')), '-', models.F('adjusted_amount_last')), '/', models.F('monthly_repayment')), output_field=models.IntegerField()),
        ),
    ]
