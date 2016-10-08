# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-01 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawdb', '0004_auto_20160901_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='court_type',
            field=models.CharField(choices=[('Fed', 'Trial'), ('State', 'Appellate')], max_length=5),
        ),
        migrations.AlterField(
            model_name='court',
            name='fed_or_state',
            field=models.CharField(choices=[('Fed', 'Federal'), ('State', 'State')], max_length=5),
        ),
        migrations.AlterField(
            model_name='court',
            name='lower_court',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='superior_court', to='lawdb.Court'),
        ),
        migrations.AlterField(
            model_name='court',
            name='upper_court',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inferior_court', to='lawdb.Court'),
        ),
    ]