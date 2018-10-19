# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-17 03:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incubator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='孵化器名称')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='联系电话')),
                ('credit_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='统一社会信用代码')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '孵化器',
                'verbose_name_plural': '孵化器',
            },
        ),
    ]
