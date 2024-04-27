from django.contrib import admin
from .models import MyUser, ProductReturnModel
# Register your models here.
admin.site.register(MyUser)

class ProductReturnAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
admin.site.register(ProductReturnModel, ProductReturnAdmin)