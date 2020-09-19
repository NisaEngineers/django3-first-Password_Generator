from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Vutum Buri, Ador Kori</h1>')
    return render(request,'pass_gen\home.html')


def credit(request):
    #return HttpResponse('<h1>Vutum Buri, Ador Kori</h1>')
    return render(request, 'pass_gen\credit.html')



def password(request):
    characters = list('')
    length = int(request.GET.get('length'))
    
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstwxyz'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()+~"?|'))
    
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'pass_gen\password.html', {'password':thepassword})



    
