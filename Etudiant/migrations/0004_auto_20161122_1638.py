# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Semestre', '0004_remove_semestre_moyenne'),
        ('Etudiant', '0003_etu_diplome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etu',
            name='diplome',
        ),
        migrations.AddField(
            model_name='etu',
            name='semestre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Semestre.Semestre'),
        ),
    ]
