# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='access',
            field=models.CharField(default='User', max_length=10),
        ),
    ]
