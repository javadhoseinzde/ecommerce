from django.contrib import admin
from .models import Product, Color, Images, Variants
# Register your models here.
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Images)
admin.site.register(Variants)