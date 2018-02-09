# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-09 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_activity_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='activities', to='engine.Collection'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='collection',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='engine.Collection'),
        ),
    ]
