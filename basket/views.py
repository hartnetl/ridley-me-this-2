from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.utils import timezone
from django.contrib import messages
from orders.models import Product, OrderItem, Order

class ViewBasket(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order,
            }
            return render(self.request, 'basket/view_basket.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


@login_required
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
            return redirect("view_product", slug=slug)
    else:
    # if it doesn't exist we create a new order
        date_ordered = timezone.now()
        order = Order.objects.create(
            user=request.user, date_ordered=date_ordered)
        order.items.add(order_item)
        messages.success(request, f'Added {product.title} to your new basket')

    return redirect("view_product", slug=slug)


@login_required
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
            return redirect("view_product", slug=slug)

        else:
            messages.error(request, "This item wasn't in your cart")
            return redirect("view_product", slug=slug)
    else:
        messages.error(request, "You don't have an active order")
        return redirect("view_product", slug=slug)

    return redirect("view_product", slug=slug)


@login_required
def decrease_quantity(request, slug):
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
            order_item.quantity -= 1
            order_item.save()
            messages.success(request, f'Reduced quantity of {product.title} to {order_item.quantity}')
            return redirect("basket")

        else:
            messages.error(request, "This item wasn't in your cart")
            return redirect("view_product", slug=slug)
    else:
        messages.error(request, "You don't have an active order")
        return redirect("view_product", slug=slug)

    return redirect("view_product", slug=slug)
