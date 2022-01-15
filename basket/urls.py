from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<item_id>/', views.adjust_basket, name='adjust_basket'),
    path('remove/<item_id>/', views.remove_from_basket, name='remove_from_basket'),
    # path('add/<slug>/', views.add_to_basket, name='add_to_basket'),
    # path('delete/<slug>/', views.delete_product_from_basket, name='remove_from_basket'),
    # path('remove/<slug>/', views.decrease_quantity, name='reduce_quantity'),
    # path('increase/<slug>/', views.increase_quantity, name='increase_quantity'),
]
