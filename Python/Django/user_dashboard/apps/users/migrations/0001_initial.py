# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0002_users_access'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages_Posted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_from', to='logreg.Users')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_to', to='logreg.Users')),
            ],
        ),
    ]
