# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-11 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawdb', '0012_auto_20160908_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cite',
            name='cite_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cite',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]
