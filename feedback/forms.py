from django import forms
from .models import Testimonials


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        exclude = ['reviewed_by']
