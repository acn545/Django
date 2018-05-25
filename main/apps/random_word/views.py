from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
num = 0
def index(request):
    global num
    num += 1
    context = {
  "random": get_random_string(length=14),
  "number": num
  }
    return render(request,'random_word/index.html', context)

def reset(request):
    global num
    num = 0
    context = {
        "numZero": num
    }
    return render(request, 'random_word/index.html', context)
