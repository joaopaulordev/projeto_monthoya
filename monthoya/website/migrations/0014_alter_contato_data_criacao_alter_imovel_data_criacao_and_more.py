# Generated by Django 5.0.7 on 2025-02-21 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_contato_data_criacao_alter_imovel_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 21, 13, 9, 51, 89571), null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 21, 13, 9, 51, 87481), null=True),
        ),
        migrations.AlterField(
            model_name='imovelcontato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 21, 13, 9, 51, 89131), null=True),
        ),
    ]
