from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Checkout.as_view(), name='checkout'),
    path('summary/', views.order_summary, name='order_summary'),
]
