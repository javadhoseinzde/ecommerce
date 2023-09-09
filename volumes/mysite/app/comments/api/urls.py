from django.urls import path
from .api import CommentViewSet
from rest_framework import routers



router = routers.SimpleRouter()

router.register("comment", CommentViewSet, basename="comment"),
router.register("comment/<int:pk>", CommentViewSet, basename="comment"),
urlpatterns = router.urls


