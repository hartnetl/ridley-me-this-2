from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsView.as_view(), name='products'),
    # path('<slug>/', views.ProductDetailView.as_view(), name='view_product'),
    path('<int:product_id>/', views.ProductDetailView.as_view(), name='view_product'),
    path('<add/', views.add_product, name='add_product'),
]
