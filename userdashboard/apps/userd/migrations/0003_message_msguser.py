# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userd', '0002_auto_20180423_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='msgUser',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]