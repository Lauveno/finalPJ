from django.shortcuts import render

# Create your views here.

def index(request) :
    print('mapApp index ~ ')
    return render(request , 'map/index.html')