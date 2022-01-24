from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('learn', views.learn, name='learn'),
]
