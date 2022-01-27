from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('add/', views.AddProduct, name='add_product'),
    path('<slug>/', views.ProductDetailView.as_view(), name='view_product'),
    path('edit/<slug>/', views.EditProduct, name='edit_product'),
    path('delete/<slug>/', views.delete_product, name='delete_product'),
]
