import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import OrderForm
from orders.models import Order, OrderItem, Product
from basket.contexts import basket_contents


def checkout(request):
    # stripe payment intent 
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # handle checkout post
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'country': request.POST['country'],
                'postcode': request.POST['postcode'],
                'town_or_city': request.POST['town_or_city'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
            }
        order_form = OrderForm(form_data)
        # If form is valid, save the order 
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your basket wasn't found in our database. "
                        "Please send us a message for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('basket'))
            # Did user want to save their info 
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # form wasn't valid 
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # request isn't POST (So it's get request)
        basket = request.session.get('basket', {})

        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        # set stripe secret keys 
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)

        # create empty instance of order form
        order_form = OrderForm()

        # message incase you forget to set secret key 
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
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
