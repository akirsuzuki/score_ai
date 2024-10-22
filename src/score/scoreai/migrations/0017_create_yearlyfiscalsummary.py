# Generated by Django 5.0.4 on 2024-09-23 00:30

import django.core.validators
import django.db.models.deletion
import scoreai.models
import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0016_create_firmcompany'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firmcompany',
            options={},
        ),
        migrations.CreateModel(
            name='YearlyFiscalSummary',
            fields=[
                ('id', models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)], verbose_name='年')),
                ('version', models.IntegerField(default=1, verbose_name='バージョン')),
                # ('monthly_data', scoreai.models.MonthlyData(default=dict)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearly_fiscal_summaries', to='scoreai.company')),
            ],
            options={
                'verbose_name': '年次決算情報',
                'verbose_name_plural': '年次決算情報',
                'unique_together': {('company', 'year', 'version')},
            },
        ),
        migrations.DeleteModel(
            name='MonthlyRevenue',
        ),
    ]
