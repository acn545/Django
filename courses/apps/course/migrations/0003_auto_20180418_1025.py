# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20180418_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='desc',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desc',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course.courses'),
        ),
    ]
