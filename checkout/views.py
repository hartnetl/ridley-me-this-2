from django.shortcuts import render
from .forms import CheckoutForm
from django.views.generic import View


class Checkout(View):
    """ A view to return the checkout page """
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print('the form is valid')
            return redirect('checkout')



def order_summary(request):
    """ A view to return a summary of the basket for the checkout page """

    return render(request, 'checkout/order_summary.html')
