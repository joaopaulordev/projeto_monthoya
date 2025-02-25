# Generated by Django 5.0.7 on 2025-02-22 23:15

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=600, null=True)),
                ('isHomepage', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 22, 20, 15, 2, 601004), null=True),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 22, 20, 15, 2, 598792), null=True),
        ),
        migrations.AlterField(
            model_name='imovelcontato',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 22, 20, 15, 2, 600551), null=True),
        ),
        migrations.AddField(
            model_name='imovel',
            name='bairro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.bairro'),
        ),
    ]
