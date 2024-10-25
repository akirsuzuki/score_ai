# Generated by Django 5.0.4 on 2024-09-29 03:04

import django.contrib.auth.validators
import django.core.validators
import ulid.api.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreai', '0023_alter_user_options_fiscalsummary_year_capital_stock_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='consultant',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='financialinstitution',
            name='bank_category',
            field=models.CharField(choices=[('都市銀行', '都市銀行'), ('地方銀行', '地方銀行'), ('第二地銀協加盟行', '第二地銀協加盟行'), ('信金中央金庫', '信金中央金庫'), ('信用金庫', '信用金庫'), ('商工組合中央金庫', '商工組合中央金庫'), ('労働金庫連合会', '労働金庫連合会'), ('農林中央金庫', '農林中央金庫'), ('政府関係機関', '政府関係機関'), ('信用組合', '信用組合'), ('その他', 'その他')], default='地方銀行', max_length=50),
        ),
    ]
