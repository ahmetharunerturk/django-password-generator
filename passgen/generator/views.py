from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')

    chars =list('qwertyuıopğüssdfghjklşizxcvbnmöç')
    if(uppercase):
        chars.extend('QWERTYUIOPĞASDFGHJKLŞİZXCVBNMÖÇ')
    if(numbers):
        chars.extend('1234567890')
    if(symbols):
        chars.extend('>£#$½{%/()=<>:;')

    thepass = ''

    for i in range(length):
        thepass += random.choice(chars)




    return render(request, 'generator/password.html', {'password': thepass})