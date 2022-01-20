import uuid
import datetime
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models import Sum
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from datetime import timedelta
from profiles.models import UserProfile

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


class TurtleSpecies(models.Model):
    class Meta:
        verbose_name_plural = 'Species'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=False, blank=False)
    title = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    # species = models.CharField(choices=SPECIES, max_length=10, null=True, blank=True)
    # sponsored_status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_product", kwargs={
            'slug': self.slug
        })

    def get_add_to_basket_url(self):
        return reverse("add_to_basket", kwargs={
            'slug': self.slug
        })

    def get_remove_from_basket_url(self):
        return reverse("remove_from_basket", kwargs={
            'slug': self.slug
        })


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Choose country *', null=False, blank=False, max_length=100)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # text field that will contain the original shopping bag that created it
    original_basket = models.TextField(null=False, blank=False, default='')
    # character field that will contain the unique stripe payment intent id
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        This generated a string of 32 numbers
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.orderitems.aggregate(Sum('orderitem_total'))['orderitem_total__sum'] or 0
        self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
        # return self.grand_total

    # override default save method 
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            # If the current order doesn't have an order number, one is assigned
            self.order_number = self._generate_order_number()
        # then execute original save method
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, editable=False)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

    # def get_total_item_price(self):
    #     return self.quantity * self.item.price

    # def get_grand_total(self):
    #     return self.get_total_item_price()

    def save(self, *args, **kwargs):
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


# code credit 
# https://stackoverflow.com/questions/2199013/how-can-my-django-model-datefield-add-30-days-to-the-provided-value/2199371
def get_sponsorship_end():
    return datetime.date.today() + timedelta(days=365)


class Turtles(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='turtle', null=True)
    sponsored_status = models.BooleanField(default=False, null=False, blank=False)
    species = models.CharField(choices=SPECIES, max_length=10, null=False, blank=False)
    name = models.CharField(max_length=50)
    sponsorship_start = models.DateField(auto_now_add=True)
    sponsorship_end = models.DateField(default=get_sponsorship_end)
    turtle_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    tagged_in = CountryField(blank_label='Choose country', max_length=100)
    current_location = models.ImageField(null=True, blank=True)

    # species = models.ForeignKey('TurtleSpecies', on_delete=models.CASCADE)
