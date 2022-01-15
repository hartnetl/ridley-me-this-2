from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import CheckoutForm
from checkout.models import Address
from orders.models import Order


class Checkout(View):
    """ A view to return the checkout form page """
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout/checkout_form.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            print(self.request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                print('the form is valid')
                # shipping_address = form.cleaned_data.get('shipping_address')
                # shipping_address2 = form.cleaned_data.get('shipping_address2')
                # shipping_country = form.cleaned_data.get('shipping_country')
                # shipping_zip = form.cleaned_data.get('shipping_zip')
                billing_address = form.cleaned_data.get('billing_address')
                billing_address2 = form.cleaned_data.get('billing_address2')
                billing_country = form.cleaned_data.get('billing_country')
                billing_zip = form.cleaned_data.get('billing_zip')
                # payment_option = form.cleaned_data.get('payment_option')
                billing_address = Address(
                    user=self.request.user,
                    street_address=billing_address,
                    street_address2=billing_address2,
                    country=billing_country,
                    zip=billing_zip
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                return redirect('checkout')
            messages.warning(self.request, 'You have filled out the form incorrectly')
            return redirect('checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("basket")


def order_summary(request):
    """ A view to return a summary of the basket for the checkout page """

    return render(request, 'checkout/order_summary.html')


class PaymentView(View):
    """ A view to return the payment page """

    def get(self, *args, **kwargs):
        return render(self.request, 'checkout/payment.html')
