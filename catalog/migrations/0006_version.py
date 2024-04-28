# Generated by Django 5.0.4 on 2024-04-27 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(choices=[('WNR', 'Зима'), ('SRG', 'Весна'), ('SMR', 'Лето'), ('ATN', 'Осень')], default='SMR', max_length=3, verbose_name='Сезон')),
                ('description', models.TextField(max_length=250, verbose_name='Описание сезона')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный сезон')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
