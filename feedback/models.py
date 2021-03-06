from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Help with min and max
# https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-
# a-numeric-field-in-a-django-model
class Testimonials(models.Model):
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name="reviews")
    reviewed_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])
    content = models.TextField(max_length=500)
    icon = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['reviewed_on']

    def __str__(self):
        return f"{self.reviewed_by.username} gave a rating of {self.rating}"
