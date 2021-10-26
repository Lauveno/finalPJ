
from django.contrib import admin
from django.urls import path
from mapApp import views

urlpatterns = [
    # http://127.0.0.1:8000/map/main
    path('main/' , views.index) ,
]
