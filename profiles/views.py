from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    # POST REQUEST HANDLER 
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    # GET REQUEST HANDLER 
    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()
        template = 'profiles/profile.html'
        context = {
            'profile': profile,
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

    return render(request, template, context)
