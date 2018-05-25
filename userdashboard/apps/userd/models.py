from __future__ import unicode_literals
from django.db import models
import  re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = 'Please enter a valid name'
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = 'Please enter a valid email'
        if len(postData['password']) < 8:
            errors['password'] = 'Please enter a password of atleast 8 characters'
        if postData['password'] != postData['cpassword']:
            errors['match'] = 'Passwords did not match please try again'
        return errors
    def log_in(self, postData):
        errors = {}
        user = users.objects.filter(email= postData['email'])
        print user.first()
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = 'Please enter a valid email'
        if str(user.first()) == 'None':
            errors['notfound'] = "Email not registered"
            return errors
        if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()) == False:
            errors['password'] = 'incorrect password'
        return errors

class users(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_level = models.CharField(max_length = 9)
    objects = UserManager()

class message(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.CharField(max_length = 255)
    posted_by = models.CharField(max_length = 255)
    objects = UserManager()
    users = models.ForeignKey(users, related_name='message')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class comment(models.Model):
    text = models.CharField(max_length = 255)
    objects = UserManager()
    posted_by = models.CharField(max_length = 255)
    message = models.ForeignKey(message, related_name='comment')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
