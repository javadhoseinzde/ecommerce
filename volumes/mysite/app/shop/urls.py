from django.urls import path
from .views import IndexView, ProductDetail, ProductList, product_detail, ajaxcolor, google_site_verf, submit_enamad, payment_request, pay_verify, ProductDiscount, ProductUnavailable
app_name = "shop"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("detail/<int:pk>", ProductDetail.as_view(), name="detail1"),
    path("discount", ProductDiscount.as_view()),
    path("unavailable", ProductUnavailable.as_view()),
    path("product-list", ProductList.as_view(), name="product-list"),
    path("details/<int:id>/<slug:slug>", product_detail, name="detail"),
    path("ajax",ajaxcolor, name="ajax"),
    path("google-provided.html", google_site_verf),
    path("4569762.txt", submit_enamad),
    path("payment/<int:id>", payment_request, name="payment"),
    path("verify/payment/<int:id>/<str:amount>", pay_verify),
]
