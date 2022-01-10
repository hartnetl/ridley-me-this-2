from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsView.as_view(), name='products'),
    path('<slug>/', views.ProductDetailView.as_view(), name='view_product'),
]
