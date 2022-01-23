from django import forms
from .models import Testimonials, admin_comments


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        exclude = ['reviewed_by']


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = admin_comments
#         fields = '__all__'
