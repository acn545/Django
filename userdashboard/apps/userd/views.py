# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import users, message, comment
from django.contrib import messages
import bcrypt
# Create your views here.

# app starts at the home page nooo matter what
def home(request):
    request.session['email'] = ""
    request.session['level'] = ''
    request.session['id'] = ''
    return render(request, 'userd/home.html')
#initial login screen, checks for session and loads dashboard if someone has previously loged in, shows login.html otherwise
def login(request):
    if request.session['email'] == "":
        return render(request, 'userd/login.html')
    
    else: 
        if request.session['level'] == '9':
            return redirect('/dashboard/admin')
        else: 
            return redirect('/dashboard')
#deals with the login informatio
def log_in(request):
        if request.method == 'POST':
            errors = users.objects.log_in(request.POST)
            if len(errors):
                for tag, errors in errors.iteritems():
                    messages.error(request, errors, extra_tags=tag)
                return redirect('/login')
            else:
                user = users.objects.filter(email=request.POST['email'])
                request.session['email'] = request.POST['email']
                request.session['id'] = user[0].id
                if user[0].user_level == '9':
                    request.session['level'] = '9'
                    return redirect('/dashboard/admin')
                else:
                    return redirect('/dashboard')
#renders dashboard for normal users
def dashboard(request):
    context = {
        'users': users.objects.all(),
    }
    return render(request, 'userd/dashboard.html', context)
#renders dashboard for admin users
def admin(request):
    context = {
        'users': users.objects.all(),
    }
    return render(request, 'userd/adminboard.html', context)
# renders the registration form
def registration(request):
    return render(request, 'userd/registrationform.html')
#validates information and updates sqlite tables
def register(request):
    if request.method == 'POST':
        errors = users.objects.registration_validator(request.POST)
        if len(errors):
            for tag, errors in errors.iteritems():
                messages.error(request, errors, extra_tags=tag)
                return redirect('/registration')
        else:
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            if len(users.objects.all()) == 0:
                users.objects.create(name=request.POST['name'], email=request.POST['email'], password=hash1, user_level = 9)
                messages.error(request, 'Registration complete, please login!')

            else:
                users.objects.create(name=request.POST['name'], email=request.POST['email'], password=hash1, user_level = 0)
                messages.error(request, 'Registration complete, please login!')
        return redirect('/login')
#shows the users information when there name on the dashboard is clicked
def userboard(request, id):
    context = {
        'user': users.objects.get(id = id),
        'poster': users.objects.get(id=request.session['id']),
        'message': message.objects.all(),
        'comment': comment.objects.all(),
    }
    return render(request,  'userd/userdashboard.html', context)
#creates a message on a users page and redirects back to that users page
def msg(request, id):
    user = users.objects.get(id=id)
    poster = users.objects.get(id=request.session['id'])
    this_msg = message.objects.create(text= request.POST['message'], posted_by = poster.id, users_id = user.id)

    
    return redirect('/dashboard')

def comments(request, id):
    msg = message.objects.get(id=id)
    poster = users.objects.get(id=request.session['id'])
    this_msg = comment.objects.create(text= request.POST['comment'], posted_by = poster.id, message_id = msg.id)
    return redirect('/dashboard')
    

