from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.urls import reverse
submission = 0
def index(request):
    return render(request, 'surveys/index.html')

def result(request):
    content = {
            "name":request.session['name'],
            "loc":request.session['loc'],
            "lang": request.session['lang'],
            "comment": request.session['comment'],
            "sub": request.session['sub']
        }
    return render(request, 'surveys/result.html', content)

def submit(request):
    global submission
    submission += 1
    if request.method == 'POST':
        request.session['sub'] = submission
        request.session['name'] = request.POST['name']
        request.session['loc'] = request.POST['loc']
        request.session['lang'] = request.POST.get('lang', False)
        request.session['comment'] = request.POST.get('comment', False)
       
        return redirect('/result')
    else:
        return redirect('/')