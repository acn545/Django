# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =255)
    desc = models.TextField(default='none')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length =255)
    email = models.CharField(max_length = 255)
    notes = models.TextField(default='PlaceHolder')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    book = models.ManyToManyField(books, related_name = 'authors')

