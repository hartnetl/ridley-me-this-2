from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Testimonials
from .forms import TestimonialForm


class TestimonialView(generic.ListView):
    model = Testimonials
    template_name = 'feedback/testimonials.html'


class CreateTestimonial(LoginRequiredMixin, CreateView):
    model = Testimonials
    form_class = TestimonialForm
    template_name = 'feedback/add_testimonial.html'
    success_message = "Thank you for your feedback :)"

    def get_success_url(self):
        return reverse('testimonials')

    def form_valid(self, form):
        form.instance.reviewed_by = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)


class EditTestimonial(LoginRequiredMixin, UpdateView):
    model = Testimonials
    form_class = TestimonialForm
    template_name = 'feedback/edit_testimonial.html'

    def get_object(self, queryset=None):
        return Testimonials.objects.get(pk=self.request.GET.get('pk'))


@login_required
def edit_testimonial(request, testimonial_id):
    """ Edit a product in the store """

    test = get_object_or_404(Testimonials, pk=testimonial_id)

    if test.reviewed_by != request.user or not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('testimonials'))

    # post handler
    if request.method == 'POST':
        # instantiate a form using request.post and request.files using the
        # instance of the product gotten above
        form = TestimonialForm(request.POST, request.FILES, instance=test)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your testimonial!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to update product. Please ensure \
                the form is valid.')
    else:
        # display prefilled form
        form = TestimonialForm(instance=test)
        messages.info(request, 'You are editing your testimonial')

    template = 'feedback/edit_testimonial.html'
    context = {
        'form': form,
        'test': test,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):

    test = get_object_or_404(Testimonials, pk=testimonial_id)

    if test.reviewed_by != request.user or not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do that')
        return redirect(reverse('testimonials'))

    test.delete()
    messages.success(request, 'Deleted that testimonial')
    return redirect(reverse('testimonials'))
