from django.urls import path
from .views import AddToCart, CartList, DeleteCart, UpdateCart

app_name = "cart"

urlpatterns = [
    path("", CartList.as_view(), name="cart-list"),
    path("add/<int:id>/", AddToCart.as_view(), name="add"),
    path("delete/<int:id>/", DeleteCart.as_view(), name="delete"),
    path("update/<int:id>/", UpdateCart.as_view(), name="update"),


]