from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from orders.models import Product


def basket_contents(request):
    """
    This is a context processor.
    Its purpose is to make this dictionary available to all templates across
    the entire application
    """

    # List for the bag items to live
    basket_items = []
    # starting total
    total = 0
    # empty basket
    product_count = 0
    # Access the session's shopping bag
    basket = request.session.get('basket', {})

    # # For each item and quantity in bag
    for item_id, item_data in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    #     # execute this one if size is supplied
    #     else:
    #         product = get_object_or_404(Product, pk=item_id)
    #         # iterate through inner dictionary of items by size
    #         for size, quantity in item_data['items_by_size'].items():
    #             # increment items accordingly
    #             total += quantity * product.price
    #             product_count += quantity
    #             bag_items.append({
    #                 'item_id': item_id,
    #                 'quantity': quantity,
    #                 'product': product,
    #                 'size': size,
    #             })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
