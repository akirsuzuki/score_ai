# Generated by Django 5.0.4 on 2024-10-01 08:50

import django.db.models.deletion
import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0029_stakeholder_name_is_board_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreai.stakeholder_name'),
        ),
    ]
