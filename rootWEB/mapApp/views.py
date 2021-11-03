import chardet
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

zerowaste_df = pd.read_csv('zerowaste_fin_utf8.txt', encoding='UTF-8')
zerowaste_df = zerowaste_df.replace(np.NaN , 0)

veganfood_df = pd.read_csv('veganfood_fin.csv', encoding='UTF-8')
veganfood_df = veganfood_df.replace(np.NaN , 0)

# About page - main page
def about(request) :
    print('mapApp about index ~ ')
    return render(request , 'map/about.html')

# Map page
def map(request) :
    print('mapApp map index ~ ')
    return render(request , 'map/map.html')

def zerowaste(request) :
    print('mapApp zerowaste index ~')
    # print(zerowaste_df.head(5))
    # print(zerowaste_df['상호명'])

    zerowasteList = []
    for idx in zerowaste_df.index :
        zerowasteList.append({
            'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
            'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
            'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
            'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
            'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
            'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
            'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
            'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
            'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
            'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() # numpy
        })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('zerowasteList complete!!')
    print(zerowasteList[0])

    return JsonResponse(zerowasteList, safe=False)

# Login page
def login(request) :
    print('mapApp login index ~ ')
    return render(request , 'map/login.html')

def logout(request) :
    return redirect('main')

def join(request) :
    return redirect('main')

def registerForm(request) :
    return render(request , 'map/join.html')

# Board page
def board(request) :
    print('mapApp index ~ ')
    return render(request , 'map/board.html')


# def register(request) :
#     print('mapApp index ~ ')
#     return render(request , 'map/register.html')

