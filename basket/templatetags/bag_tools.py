from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    ''' Calculate the subtotal for products '''
    return price * quantity
