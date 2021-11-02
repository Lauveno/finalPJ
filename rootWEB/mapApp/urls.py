
from django.contrib import admin
from django.urls import path
from mapApp import views

urlpatterns = [
    # http://127.0.0.1:8000/map/main
    path('main/' , views.about , name = "main") ,
    # map
    path('map/' , views.map , name = "map") ,
    path('zerowaste/' , views.zerowaste , name = "zerowaste") ,
    # user
    path('login/' , views.login , name = "login") ,
    path('logout/' , views.logout , name = "logout") ,
    path('join/' , views.join , name = "join") ,
    path('registerForm/' , views.registerForm , name = "registerForm") ,
    # board
    path('board/' , views.board , name = "board") ,
    # path('news_read/' , views.news_read , name = "news_read") ,
    # register
    # path('register/' , views.register , name = "register") ,


]
