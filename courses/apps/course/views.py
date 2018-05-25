# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import courses, desc
# Create your views here.

def index(request):
    context = {
      'courses': courses.objects.all(),
    }
    return render(request, 'course/index.html', context)

def confirm_POST(request):
    request.session['course'] = request.POST['hidden']
    return redirect(confirm_GET)

def confirm_GET(request):
    context ={
        'course': courses.objects.get(id= request.session['course'])
    }
    return render(request, 'course/delete.html', context)

def delete(request):
    courses.objects.get(id=request.session['course']).delete()
    return redirect('/')
    
def add(request):
    courses.objects.create(name=request.POST['name'])
    desc.objects.create(desc=request.POST['desc'])
    return redirect('/')
