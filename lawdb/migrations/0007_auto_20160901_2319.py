# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-02 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawdb', '0006_auto_20160901_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courtassignment',
            name='end_date',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='courtassignment',
            name='start_date',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]