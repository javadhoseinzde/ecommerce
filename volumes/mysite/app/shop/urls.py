from django.urls import path
from .views import IndexView, ProductDetail, ProductList, product_detail, ajaxcolor
app_name = "shop"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("detail/<int:pk>", ProductDetail.as_view(), name="detail1"),
    path("product-list", ProductList.as_view(), name="product-list"),
    path("details/<int:id>/<slug:slug>", product_detail, name="detail"),
    path("ajax",ajaxcolor, name="ajax")
]