from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.utils import timezone
from django.contrib import messages
from orders.models import Product, OrderItem, Order


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/view_basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.title} quantity to {basket[item_id]}')

    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.title} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)  
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed {product.titke} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
