from django.shortcuts import render, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


# class TestimonialView(request):
#     testimonials = Testimonials.objects.all()

#     context = {
#         'testimonials': testimonials,
#     }

#     return render(request, 'feedback/testimonials.html', context)

