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


# help with count https://stackoverflow.com/questions/5439901/getting-a-count-of-objects-in-a-queryset-in-django
@register.simple_tag
def get_available_turtle_count():

    qs = Product.objects.all().filter(turtle__sponsored_status=False).count()
    return qs
    

@register.simple_tag
def get_sponsored_turtle_count():
    qs = Product.objects.all().filter(turtle__sponsored_status=True).count()
    return qs

