# Generated by Django 5.0.4 on 2024-06-04 01:41

import django.db.models.deletion
import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0013_securedtype_debt_is_collateraled_debt_is_nodisplay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='secured_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scoreai.securedtype'),
            preserve_default=False,
        ),
    ]
