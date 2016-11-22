# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Matiere', '0002_auto_20161113_1717'),
        ('Etudiant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.IntegerField()),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Etudiant.Etu')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Matiere.Matiere')),
            ],
        ),
    ]