from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from orders.models import Product, OrderItem, Order


class ViewBasket(TemplateView):
    model = OrderItem
    template_name = "basket/view_basket.html"


def add_to_basket(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=product,
        user=request.user,
        ordered=False
    )
    # check that the user hasn't already completed this order
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
    # it exists so we're updating the order
        order = order_qs[0]
        # check if the order item is in the order
        # if it is, update the quantity
        if order.items.filter(item__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
        # if it isn't, add the item to the order
        else:
            order.items.add(order_item)
    else:
    # if it doesn't exist we create a new order
        date_ordered = timezone.now()
        order = Order.objects.create(
            user=request.user, date_ordered=date_ordered)
        order.items.add(order_item)

    return redirect("view_product", slug=slug)


def delete_product_from_basket(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=product.slug).exists():
            order_item = OrderItem.objects.filter(
                item=product,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
        else:
            # product doesn't exist in order
            return redirect("view_product", slug=slug)
    else:
        # order doesn't exist
        return redirect("view_product", slug=slug)

    return redirect("view_product", slug=slug)
