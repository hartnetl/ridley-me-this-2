from django import template
from orders.models import Order, Product

register = template.Library()


@register.filter
def basket_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0


@register.simple_tag
def get_available_turtle_count():

    qs = Product.objects.all().filter(turtle__sponsored_status=False).count()
    q = Product.objects.all()
    print('ALL')
    print(q)
    print('QS-AVAILABLE')
    print(qs)
    return qs
    # return 0


@register.simple_tag
def get_sponsored_turtle_count():
    qs = Product.objects.all().filter(turtle__sponsored_status=True).count()
    q = Product.objects.all()
    print('ALL')
    print(q)
    print('QS-sponsored')
    print(qs)
    # if qs.exists():
    return qs
    # return 0
