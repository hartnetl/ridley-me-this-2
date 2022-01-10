from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from orders.models import Product, OrderItem, Order


class ViewBasket(TemplateView):
    model = OrderItem
    template_name = "basket/view_basket.html"


def add_to_basket(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.create(item=product)
    # check that the user hasn't already completed this order
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        # it exists so we're updating the order
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)

    return redirect("view_product", kwargs={'slug': slug})
