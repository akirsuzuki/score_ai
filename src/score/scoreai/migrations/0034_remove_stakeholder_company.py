# Generated by Django 5.0.4 on 2024-10-01 09:18

import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0033_add_stakeholder_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stakeholder',
            name='company',
        ),
    ]
