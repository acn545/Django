# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class user(models.Model):
    full_name = models.name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)