# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitee',
            name='coefficient',
            field=models.FloatField(null=True),
        ),
    ]