from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestimonialView.as_view(), name='testimonials'),
    path('add_testimonial/', views.CreateTestimonial.as_view(), name='add_testimonial'),
]
