# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Semestre', '0002_semestre_diplome'),
    ]

    operations = [
        migrations.AddField(
            model_name='semestre',
            name='moyenne',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]