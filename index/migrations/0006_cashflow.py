# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-09 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_profit'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(verbose_name='年份')),
                ('name', models.CharField(max_length=4)),
                ('value', models.FloatField()),
                ('companyInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.CompanyInfo', verbose_name='企业')),
            ],
        ),
    ]
