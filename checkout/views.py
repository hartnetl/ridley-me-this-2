from django.shortcuts import render
from .forms import CheckoutForm


def checkout(request):
    """ A view to return the checkout page """

    context = {}
    context['form']=CheckoutForm()

    return render(request, 'checkout/checkout.html', context)


def order_summary(request):
    """ A view to return a summary of the basket for the checkout page """

    return render(request, 'checkout/order_summary.html')
