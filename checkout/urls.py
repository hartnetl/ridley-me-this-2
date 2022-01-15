from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout.as_view(), name='checkout'),
    path('summary/', views.order_summary, name='order_summary'),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
]
