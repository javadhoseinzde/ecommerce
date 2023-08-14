from django.urls import path
from .views import IndexView, ProductDetail
app_name = "shop"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("detail/<int:pk>", ProductDetail.as_view(), name="detail")
]