from django.shortcuts import render


def checkout(request):
    """ A view to return the checkout page """

    return render(request, 'checkout/checkout.html')


def order_summary(request):
    """ A view to return a summary of the basket for the checkout page """

    return render(request, 'checkout/order_summary.html')
