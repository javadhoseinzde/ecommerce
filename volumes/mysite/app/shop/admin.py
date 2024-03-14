from django.contrib import admin
from .models import Product, Color, Images, Variants, Slider, description_image
# Register your models here.
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Images)
admin.site.register(Variants)
admin.site.register(Slider)
admin.site.register(description_image)