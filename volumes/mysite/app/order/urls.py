from django.urls import path
from .views import order_view, OrderView, OrderFormView, payment

app_name = "order"

urlpatterns = [
    path("form", order_view),
    path("forms/", OrderView.as_view(), name="form"),
    path("create_order", OrderFormView.as_view(), name="create_order"),
    path("payment/<int:id>", payment, name="pay")
]