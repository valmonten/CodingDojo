# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0009_auto_20171001_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels',
            name='creator',
            field=models.ForeignKey(default='Nathan', on_delete=django.db.models.deletion.CASCADE, related_name='travel', to='logreg.Users'),
        ),
    ]
