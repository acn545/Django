from django.shortcuts import render, HttpResponse, redirect
from random import randrange
from time import gmtime, strftime
import datetime
  # the index function is called when root is visited
coins = 50
actions = []
def index(request):
      context = {
        'coins': request.session['coins'],
        'list': request.session['list'],
        'earned': request.session['ncoins'],
      }
      return render(request, 'ninjagold/index.html', context)

def money(request):
    global coins
    if coins <= 0:
      request.session['ncoins'] = 0
      request.session['list'].append('you have zero coins left - game over' + " " + str(datetime.datetime.now()))
      return redirect('/')

    elif request.POST['nam'] == 'cave' :
      request.session['ncoins'] = randrange(5, 10)
      coins += request.session['ncoins']
      request.session['coins'] = coins
      request.session['list'] = actions
      request.session['list'].append('Earned ' + " " +  str(request.session['ncoins']) + " " +  "from the Cave! " + " " + str(datetime.datetime.now()))
      print request.session['list']
      return redirect('/')

    elif request.POST['nam'] == 'house' :
      request.session['ncoins'] = randrange(2, 5)
      coins += request.session['ncoins']
      request.session['coins'] = coins
      request.session['list'] = actions
      request.session['list'].append('Earned ' + " " + str(request.session['ncoins']) + " " + "from the House! " + " " +  str(datetime.datetime.now()))
      print request.session['list']
      return redirect('/') 

    elif request.POST['nam'] == 'farm' :
      request.session['ncoins'] = randrange(10, 20)
      coins += request.session['ncoins']
      request.session['coins'] = coins
      request.session['list'] = actions
      request.session['list'].append('Earned ' + " " +  str(request.session['ncoins']) + " " + "from the farm! " + " " + str(datetime.datetime.now()))
      print request.session['list']
      return redirect('/')

    elif request.POST['nam'] == 'casino' :
      request.session['ncoins'] = randrange(-50, 50)
      coins += request.session['ncoins']
      request.session['coins'] = coins
      request.session['list'] = actions
      if request.session['ncoins'] >= 0:
        request.session['list'].append('Earned ' + " " +  str(request.session['ncoins']) + " " + "at the farm! " + " " + str(datetime.datetime.now()))
      else:
        request.session['list'].append('Lost ' + " " +  str(request.session['ncoins']) + " " + "at the farm! " + " " + str(datetime.datetime.now()))      
      return redirect('/') 
        
    else: 
        "DEBUG: save() GET method was called"
        return redirect('/')