from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
import uuid

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

    def get_add_to_basket_url(self):
        return reverse("add_to_basket", kwargs={
            'slug': self.slug
        })

    def get_remove_from_basket_url(self):
        return reverse("remove_from_basket", kwargs={
            'slug': self.slug
        })


class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    # ordered = models.BooleanField(default=False)
    # start_date = models.DateTimeField(auto_now=True)
    # date_ordered = models.DateTimeField()
    # items = models.ManyToManyField(OrderItem)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Choose country...', default='blank_label')
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        This generated a string of 32 numbers
        """
        return uuid.uuid4().hex.upper()

    # def get_total(self):
    #     self.order_total = 0
    #     for order_item in self.items.all():
    #         print('order items:')
    #         print(order_item)
    #         self.order_total += order_item.get_grand_total()
    #         print('order_total:')
    #         print(order_total)
    #         self.save()
    #     return self.order_total

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
        return f"{self.quantity} of {self.item.title}"

    # def get_total_item_price(self):
    #     return self.quantity * self.item.price

    # def get_grand_total(self):
    #     return self.get_total_item_price()

    def save(self, *args, **kwargs):
        self.orderitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)
