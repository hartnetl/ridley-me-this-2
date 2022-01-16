from django.contrib import admin
from .models import Product, Order, OrderItem, Category


class OrderItemAdminInline(admin.TabularInline):
    # Allows us to add and edit line items in admin in the order model
    model = OrderItem
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total',
                       'grand_total', 'original_basket', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)
admin.site.register(Category)
