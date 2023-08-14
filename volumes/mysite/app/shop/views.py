from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView
# Create your views here.


def filter_product():
    return Product.objects.filter(status="True")

def get_product(pk):
    return get_object_or_404(Product, pk=pk, status="True")


class IndexView(ListView):
    template_name = "shop/index.html"

    def get_queryset(self):
        queryset = {
            "query": filter_product()
        }
        return queryset


class ProductDetail(DetailView):
    template_name = "shop/product-detail.html"


    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_product(pk)