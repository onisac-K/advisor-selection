# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160501_2103'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='advisor',
            name='introduction',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='research',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
