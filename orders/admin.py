from django.contrib import admin
from .models import Product, Order, OrderItem, Category


class OrderAdmin(admin.ModelAdmin):

    list_display = ('order_number', 'date_ordered', 'full_name', 'order_total')


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Category)
