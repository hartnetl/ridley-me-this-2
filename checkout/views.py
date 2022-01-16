import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import OrderForm
from orders.models import Order
from basket.contexts import basket_contents


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(amount=stripe_total,
                                         currency=settings.STRIPE_CURRENCY,)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K1HPjFEToCWPRVclerd629oZ2GPMA7MZ35nvCP1MFMF3TOaGag82Zcnss3Yks7VrpnTs54aTBofqbdW71E4mX19009CY8EerJ',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)


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
