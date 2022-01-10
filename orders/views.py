from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class productsView(ListView):
    model = Product
    template_name = "orders/view_products.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "orders/product_detail.html"
