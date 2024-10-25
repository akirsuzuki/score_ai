# Generated by Django 5.0.4 on 2024-10-01 10:51

import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0035_fiscalsummary_year_accumulated_depreciation'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiscalsummary_year',
            name='other_intangible_assets',
            field=models.IntegerField(default=0, verbose_name='その他の無形固定資産（千円）'),
        ),
        migrations.AddField(
            model_name='fiscalsummary_year',
            name='total_intangible_assets',
            field=models.IntegerField(default=0, verbose_name='無形固定資産合計（千円）'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='goodwill',
            field=models.IntegerField(default=0, verbose_name='のれん（千円）'),
        ),
    ]
