from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView
from app.order.models import OrderItem
from app.comments.models import Comments
from .forms import ProductReturnForm
from django.views.generic import View


class Dashboard(ListView):
    template_name = "user/dashboard/index.html"
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        queryset = {
            "order_item_bool": OrderItem.objects.filter(order__user=user).exists(),
            "order_item": OrderItem.objects.filter(order__user=user, order__paid=True)[:4],
            "comment": Comments.objects.filter(user=user)[:3]
        }
        return queryset
    


class PurchasedProductsView(ListView):
    template_name = "user/dashboard/purchased_product.html"

    def get_queryset(self):
        user = self.request.user
        queryset = OrderItem.objects.filter(order__user=user, order__paid =True )
        return queryset

class CommentListView(ListView):
    template_name = "user/dashboard/comment_list.html"

    def get_queryset(self):
        user = self.request.user
        queryset = Comments.objects.filter(user=user)
        return queryset


class ProductReturnForm(FormView):
    form_class = ProductReturnForm
    template_name = "user/dashboard/product-return-form.html"
    success_url = "/"


class ProductReturnView(FormView):
    pass

class UserInfoView(UpdateView):
    pass