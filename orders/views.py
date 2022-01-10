from django.shortcuts import render
from .models import Product


def view_products(request):
    context = {
        'products': Product.objects.all()
    }
    
    return render(request, "orders/view_products.html", context)
