# Generated by Django 5.0.4 on 2024-10-22 09:04

import django.core.validators
import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0058_alter_company_id_alter_debt_id_alter_firm_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='industryindicator',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='日本語ラベル'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='score_EBITDA_interest_bearing_debt_ratio',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='EBITDA有利子負債倍率'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='score_equity_ratio',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='自己資本比率'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='score_labor_productivity',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='労働生産性'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='score_operating_profit_margin',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='営業利益率'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='score_operating_working_capital_turnover_period',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='営業運転資本回転期間'),
        ),
        migrations.AlterField(
            model_name='fiscalsummary_year',
            name='score_sales_growth_rate',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='売上高増加率'),
        ),
        migrations.DeleteModel(
            name='StakeHolder',
        ),
    ]
