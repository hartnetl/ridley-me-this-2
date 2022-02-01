from django.contrib import admin
from .models import Product, Order, OrderItem, Category, Turtles


class OrderItemAdminInline(admin.TabularInline):
    # Allows us to add and edit line items in admin in the order model
    model = OrderItem
    readonly_fields = ('orderitem_total',)

class TurtlesAdmin(admin.StackedInline):
    model = Turtles

class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total',
                       'grand_total', 'original_basket', 'stripe_pid')

    fields = ('order_number','user_profile', 'date', 'full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'order_total', 'grand_total', 'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)


class ProductAdmin(admin.ModelAdmin):

    inlines = (TurtlesAdmin,)

    list_display = ('title', 'category', 'price', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(Turtles)
