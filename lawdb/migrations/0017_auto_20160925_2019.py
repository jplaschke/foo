# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawdb', '0016_auto_20160919_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='section',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]