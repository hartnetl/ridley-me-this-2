from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.utils import timezone
from django.contrib import messages
from orders.models import Product, OrderItem, Order

def view_basket(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/view_basket.html')
