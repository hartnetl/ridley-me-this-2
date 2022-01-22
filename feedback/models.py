from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Testimonials(models.Model):
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name="reviews")
    reviewed_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField(max_length=500)
    icon = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['reviewed_on']

    def __str__(self):
        return f"{self.reviewed_by.username} gave a rating of {self.rating}"


class admin_comments(models.Model):
    review = models.ForeignKey(Testimonials, on_delete=models.SET_NULL, related_name='comments', null=True)
    name = models.CharField(max_length=50)
    date_replied = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment} replied by {self.name}"
