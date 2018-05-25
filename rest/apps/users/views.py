from django.shortcuts import render, HttpResponse, redirect
import md5, re
from models import user
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
  # the index function is called when root is visited

 
def index(request):
    context = {
      'users': user.objects.all()
    }
    return render(request, 'users/index.html', context)

def add_user(request):
    return render(request, 'users/adduser.html')

def create(request):
    name = request.POST['name']
    email = request.POST['email']

    if len(name) < 1:
        print 'name to short'
        return redirect(add_user)
    elif len(email) < 1 or not EMAIL_REGEX.match(email):
        print 'wrong email'
        return redirect(add_user)
    else:
        user.objects.create(full_name=name, email=email)

    return redirect(index)

def show(request):
    context = {
      'users': user.objects.all(),
      'num': int(request.GET['id'])
    }
    return render(request, 'users/show.html', context)

def edit(request):
  context = {
      'users': user.objects.all(),
      'num': int(request.GET['id'])
  }
  print request.GET['id']
  print user.objects.get(id=request.GET['id']).id
  return render(request, 'users/edituser.html', context)

def destroy(request):
  num= request.POST['id']
  user.objects.get(id=num).delete()
  return redirect('/')

def update(request):
  num= request.POST['id']
  person = user.objects.get(id=num)
  person.full_name = request.POST['name']
  person.email = request.POST['email']
  person.save()

  return redirect('/')