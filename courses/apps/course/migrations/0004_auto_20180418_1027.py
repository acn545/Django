# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20180418_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desc',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
