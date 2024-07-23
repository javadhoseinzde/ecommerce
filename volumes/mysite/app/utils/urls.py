from django.urls import path
from .views import ContactUsFormView, AboutUs, BugBountyFormView, Privacy, PaymentMethod, ReturnProduct, ShippingMethod

urlpatterns = [
    path("contact_us/", ContactUsFormView.as_view(), name="contact-us"),
    path("about-us/", AboutUs.as_view(), name="about-us"),
    path("report/", BugBountyFormView.as_view(), name="bug-bounty"),
    path("privacy/", Privacy.as_view(), name="privacy"),
    path("payment-method/", PaymentMethod.as_view(), name="payment-method"),
    path("product-return", ReturnProduct.as_view(), name="product-return"),
    path("shipping-product", ShippingMethod.as_view(), name="shipping-product"),
]
