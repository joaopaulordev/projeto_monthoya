# Generated by Django 5.0.7 on 2025-02-22 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_contato_data_criacao_alter_imovel_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 22, 15, 42, 44, 212592), null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 22, 15, 42, 44, 210564), null=True),
        ),
        migrations.AlterField(
            model_name='imovelcontato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 22, 15, 42, 44, 212166), null=True),
        ),
    ]
