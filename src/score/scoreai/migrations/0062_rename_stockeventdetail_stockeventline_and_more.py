# Generated by Django 5.0.4 on 2024-10-22 22:17

import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0061_alter_company_id_alter_debt_id_alter_firm_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockEventDetail',
            new_name='StockEventLine',
        ),

    ]
