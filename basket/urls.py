from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewBasket.as_view(), name='basket'),
    path('add/<slug>/', views.add_to_basket, name='add_to_basket'),
]
