from django.shortcuts import render
from django.views import generic, View
from .models import Testimonials


class TestimonialView(generic.ListView):
    model = Testimonials
    template_name = 'feedback/testimonials.html'
    paginate_by = 6
