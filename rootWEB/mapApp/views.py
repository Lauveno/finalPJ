from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request) :
    print('mapApp index ~ ')
    return render(request , 'map/index.html')

def login(request) :
    print('mapApp index ~ ')
    return render(request , 'map/login.html')

def logout(request) :
    return redirect('main')

def join(request) :
    return redirect('main')

def registerForm(request) :
    return render(request , 'map/join.html')


def news(request) :
    print('mapApp index ~ ')
    return render(request , 'map/news.html')


def register(request) :
    print('mapApp index ~ ')
    return render(request , 'map/register.html')

