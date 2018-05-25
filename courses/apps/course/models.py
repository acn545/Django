# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class UserManager(models.Manager):
    def validate(self, request_data):
        valid  = True
        errors = []
        if len(request_data['name']) < 5:
            valid = False
            errors.append("Course name must be longer")
        if len(request_data['desc']) < 15:
            valid = False
            errors.append('description must be longer than 15 characters')
        return valid, errors

class courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add  = True)
    updated_at = models.DateTimeField(auto_now = True)


class desc(models.Model):
    desc = models.TextField(default="none")
    created_at = models.DateTimeField(auto_now_add  = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.OneToOneField(courses, primary_key=True, related_name='course')

