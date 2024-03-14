from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created_at', 'updated_at']
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]