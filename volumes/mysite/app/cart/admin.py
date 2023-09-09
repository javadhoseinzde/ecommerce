from django.contrib import admin
from .models import ShopCart
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity"]

admin.site.register(ShopCart,ShopCartAdmin)