from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import ProductForm


class productsView(ListView):
    model = Product
    template_name = "orders/view_products.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "orders/product_detail.html"


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'orders/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)