from django.db import models
from django.conf import settings
from django.shortcuts import reverse

SPECIES = [
        ('logger', 'Loggerhead'),
        ('green', 'Green'),
        ('leather', 'Leatherback'),
        ('flat', 'Flatback'),
        ('hawks', 'Hawksbill'),
        ('olive', 'Olive Ridley'),
        ("kemp", "Kemp's Ridley"),
    ]


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    # programmatic name
    name = models.CharField(max_length=254)
    # front end name
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sku = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    species = models.CharField(choices=SPECIES, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_product", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=True)
    auto_date = models.DateTimeField()
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username
