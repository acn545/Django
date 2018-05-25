from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.urls import reverse
submission = 0
data = []
checks = []
colors = []
def index(request):
    content = {
        'data': request.session['data'],
        'check': request.session['check'],
        'color': request.session['color']
    }
    return render(request, 'session_words/index.html', content)

def add(request):
    if request.method == 'POST':
        request.session['word'] = request.POST['word']
        request.session['data'] = data
        request.session['data'].append(request.session['word'])
        request.session['checkbox'] = request.POST.get('checked', False)
        request.session['check'] = checks
        request.session['check'].append(request.session['checkbox'])
        request.session['color'] = colors
        print request.POST['color']
        request.session['color'].append(request.POST['color'])

        print checks
        print data
        print colors
        
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    del data[:]
    del checks[:]
    del colors[:]
    request.session['data'] = data
    request.session['color'] = colors
    request.session['check'] = checks
    return redirect('/')