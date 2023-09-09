from .models import Product
from app.comments.models import Comments
from django.db import models
from django.shortcuts import render, get_object_or_404, get_list_or_404

def filter_product():
    return Product.objects.published()

def get_product(pk):
    return get_object_or_404(Product.objects.published(), pk=pk, status="True")


def get_comment(pk):
    status = Comments.objects.filter(status=True,product_id=pk).exists()

    if status == True:
        return get_list_or_404(Comments.objects.published(), product_id=pk)
    else:
        return "کامنتی وجود ندارد"
