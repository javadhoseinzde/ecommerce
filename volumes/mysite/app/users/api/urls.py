from django.urls import path
from .api import UserViewSet

urlpatterns = [
    # ...
    path('login-with-otp/', UserViewSet.as_view(), name='login-with-otp'),
]