# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160501_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='photo',
            field=models.ImageField(default='', upload_to='./faces/'),
            preserve_default=False,
        ),
    ]
