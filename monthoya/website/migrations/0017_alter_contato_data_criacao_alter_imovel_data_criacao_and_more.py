# Generated by Django 5.0.7 on 2025-02-21 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_contato_data_criacao_alter_imovel_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 21, 13, 45, 29, 812907), null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 21, 13, 45, 29, 808924), null=True),
        ),
        migrations.AlterField(
            model_name='imovelcontato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 21, 13, 45, 29, 812230), null=True),
        ),
    ]
