# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=20)),
                ('ruling', models.CharField(max_length=40)),
                ('decide_date', models.DateTimeField(verbose_name='date decided')),
                ('argue_date', models.DateTimeField(verbose_name='date argued')),
                ('docket', models.CharField(max_length=50)),
                ('plantiff', models.CharField(max_length=50)),
                ('defendant', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Case',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('chapter', models.CharField(max_length=10)),
                ('section', models.PositiveSmallIntegerField()),
                ('subtitle', models.CharField(max_length=10)),
                ('topic', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=80)),
                ('fed_or_state', models.CharField(choices=[('Fed', 'Federal'), ('State', 'State')], max_length=1)),
            ],
            options={
                'db_table': 'Code',
            },
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=200)),
                ('hierachy_level', models.PositiveSmallIntegerField()),
                ('fed_or_state', models.CharField(choices=[('Fed', 'Federal'), ('State', 'State')], max_length=1)),
                ('court_type', models.CharField(choices=[('Fed', 'Trial'), ('State', 'Appellate')], max_length=1)),
                ('lower_court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inferior_court', to='lawdb.Court')),
            ],
            options={
                'db_table': 'Court',
            },
        ),
        migrations.CreateModel(
            name='CourtAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='date stared')),
                ('end_date', models.DateTimeField(verbose_name='date ended')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.Court')),
            ],
            options={
                'db_table': 'CourtAssignment',
            },
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=25)),
                ('year_born', models.PositiveSmallIntegerField()),
                ('state_born', models.CharField(max_length=2)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'db_table': 'Judge',
            },
        ),
        migrations.CreateModel(
            name='LawSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'LawSchool',
            },
        ),
        migrations.CreateModel(
            name='LegalPrinciple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('definition', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'LegalPrinciple',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_plantiff', models.PositiveSmallIntegerField()),
                ('for_defendant', models.PositiveSmallIntegerField()),
                ('opinion_type', models.CharField(max_length=30)),
                ('judge', models.ManyToManyField(to='lawdb.Judge')),
                ('legal_principle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.LegalPrinciple')),
            ],
            options={
                'db_table': 'Opinion',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('abbreiviation', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'State',
            },
        ),
        migrations.AddField(
            model_name='judge',
            name='law_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.LawSchool'),
        ),
        migrations.AddField(
            model_name='courtassignment',
            name='judge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.Judge'),
        ),
        migrations.AddField(
            model_name='court',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.State'),
        ),
        migrations.AddField(
            model_name='court',
            name='upper_court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superior_court', to='lawdb.Court'),
        ),
        migrations.AddField(
            model_name='code',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.State'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_below_cite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_below_cite', to='lawdb.Opinion'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_court_below',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawdb.Court'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_opinion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_opinion', to='lawdb.Opinion'),
        ),
        migrations.AddField(
            model_name='case',
            name='citations',
            field=models.ManyToManyField(related_name='_case_citations_+', to='lawdb.Case'),
        ),
    ]
