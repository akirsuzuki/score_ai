# Generated by Django 5.0.4 on 2024-05-22 07:34

import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firm',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=12, primary_key=True, serialize=False),
        ),
    ]
