from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib import messages
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
            messages.success(request, f'Updated quantity of {product.title} to {order_item.quantity}')
            order_item.save()
        # if it isn't, add the item to the order
        else:
            order.items.add(order_item)
            messages.success(request, f'Added {product.title} to your basket')
    else:
    # if it doesn't exist we create a new order
        date_ordered = timezone.now()
        order = Order.objects.create(
            user=request.user, date_ordered=date_ordered)
        order.items.add(order_item)
        messages.success(request, f'Added {product.title} to your new basket')

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
            messages.success(request, f'Removed {product.title} from your basket')

        else:
            messages.error(request, "This item wasn't in your cart")
            return redirect("view_product", slug=slug)
    else:
        # order doesn't exist
        return redirect("view_product", slug=slug)

    return redirect("view_product", slug=slug)
