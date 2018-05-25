from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request! for blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder for creating a new blog post"
    return HttpResponse(response)
def create(request):
	return redirect("/")


def number(request, number):
    response = "This is blog " + number
    return HttpResponse(response)

def edit(request, number):
    response = "edit blog number  " + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect(index)