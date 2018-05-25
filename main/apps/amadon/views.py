from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.urls import reverse
shirt = 19.99
sweater = 29.99
cup = 4.99
book = 49.99
total = 0
num = 0

def index(request):

    context = {
        'shirt': shirt,
        'sweater': sweater,
        'cup': cup,
        'book': book
    }
    return render(request, 'amadon/store.html', context)

def checkout(request):
    context = {
        'shirt': shirt,
        'sweater': sweater,
        'cup': cup,
        'book': book, 
        'price': request.session['price'],
        'total': request.session['total'],
        'index': request.session['index']
    }
    return render(request, 'amadon/checkout.html', context)

def buy(request):
    global total, num
    request.session['buy'] = request.POST['buy']
    if request.session['buy'] == 'shirt':
        request.session['price'] = shirt * int(request.POST['amount'])
        total = request.session['price'] + total
        request.session['total'] = total
        num = int(request.POST['amount']) + num
        request.session['index'] = num
    
    elif request.session['buy'] == 'sweater':
        request.session['price'] = sweater * int(request.POST['amount'])
        total = request.session['price'] + total
        request.session['total'] = total
        num = int(request.POST['amount']) + num
        request.session['index'] = num

    elif request.session['buy'] == 'cup':
        request.session['price'] = cup * int(request.POST['amount'])
        total = request.session['price'] + total
        request.session['total'] = total
        num = int(request.POST['amount']) + num
        request.session['index'] = num

    elif request.session['buy'] == 'book':
        request.session['price'] = book * int(request.POST['amount'])
        total = request.session['price'] + total
        request.session['total'] = total
        num = int(request.POST['amount']) + num
        request.session['index'] = num

        
    return redirect('/amadon/checkout')