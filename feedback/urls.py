from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestimonialView.as_view(), name='testimonials'),
    path('add_testimonial/', views.CreateTestimonial.as_view(), name='add_testimonial'),
    # path('<testimonial_id>/edit/', views.EditTestimonial.as_view(), name='edit_testimonial'),
    path('edit/<testimonial_id>', views.edit_testimonial, name='edit_testimonial'),
]
