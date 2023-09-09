from django.urls import path
from .api import ProductViewSet
from rest_framework import routers



router = routers.SimpleRouter()

router.register("product", ProductViewSet, basename="product"),
router.register("product/<int:pk>", ProductViewSet, basename="product"),
urlpatterns = router.urls


