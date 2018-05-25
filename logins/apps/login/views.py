# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
import  re
import bcrypt
from models import users

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def register(request):
    return render(request, 'login/register.html')

def add(request):
    if request.method == "POST":
        errors = users.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(register)
        else:
            print "doing this stuff now"
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            users.objects.create(email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hash1)
            messages.error(request, 'Registration successful')
            #do stuff here
            return redirect(index)

def login(request):
    user = users.objects.filter(email=request.POST['email'])
    if request.method == 'POST':
            if request.POST['email'] == user[0].email:
                if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()) == False:
                    messages.error(request, 'password was invalid please try again')
                else:
                    return redirect(dashboard)
            else:
                messages.error(request, 'Invalid email address')
                return redirect(index)
    return redirect(index)

def dashboard(request):
    return render(request, 'login/dashboard.html')