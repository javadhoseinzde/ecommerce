from django.shortcuts import render
from app.shop.models import Product
from django.views.generic import ListView
# Create your views here.

class CategoryFilter(ListView):
    template_name = "shop/product-list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
