from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('request/',views.GenerateGameView.as_view(), name = 'request_view'),

]