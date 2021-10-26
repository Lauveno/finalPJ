
from django.contrib import admin
from django.urls import path
from mapApp import views

urlpatterns = [
    # http://127.0.0.1:8000/map/main
    path('main/' , views.index , name = "main") ,
    #user
    path('login/' , views.login , name = "login") ,
    path('logout/' , views.logout , name = "logout") ,
    path('join/' , views.join , name = "join") ,
    path('registerForm/' , views.registerForm , name = "registerForm") ,
    # news
    path('news/' , views.news , name = "news") ,
    # path('news_read/' , views.news_read , name = "news_read") ,
    # register
    path('register/' , views.register , name = "register") ,
]
