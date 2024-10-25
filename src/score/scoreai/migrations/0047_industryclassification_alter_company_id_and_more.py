# Generated by Django 5.0.4 on 2024-10-17 11:43

import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0046_debt_is_rescheduled_alter_company_id_alter_debt_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='業界名')),
                ('code', models.CharField(max_length=7, unique=True, verbose_name='分類コード')),
                ('memo', models.TextField(blank=True, verbose_name='備考')),
            ],
        ),

    ]
