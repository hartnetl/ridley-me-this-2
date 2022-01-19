from django.urls import path
from . import views

urlpatterns = [
    # path('', views.productsView.as_view(), name='products'),
    path('', views.products_view, name='products'),
    # path('add/', views.add_product, name='add_product'),
    # path('add/', views.AddProduct.as_view(), name='add_product'),
    path('add/', views.AddProduct, name='add_product'),
    path('<slug>/', views.ProductDetailView.as_view(), name='view_product'),
    path('edit/<slug>/', views.EditProduct, name='edit_product'),
    # path('edit/<slug>/', views.EditProduct.as_view(), name='edit_product'),
    path('delete/<slug>/', views.delete_product, name='delete_product'),
    # path('<int:product_id>/', views.ProductDetailView.as_view(), name='view_product'),
]
