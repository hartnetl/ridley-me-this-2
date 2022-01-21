from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from orders.models import Order


def order_history(request, order_number):
    # get the order
    order = get_object_or_404(Order, order_number=order_number)

    # Add message to tell user they're looking at a past order confirmation
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        # add the variable from_profile to check in that template if the user got there via the order history view
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Create a new instance of the user profile form using the post data
        # and tell it the instance we're updating is the profile we've just
        # retrieved above.
        form = UserProfileForm(request.POST, instance=profile)
        # Then if the form is valid, save it and add a success message.
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

