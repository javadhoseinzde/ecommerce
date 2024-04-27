from django.urls import path
from .views import AddComment
app_name = "comment"

urlpatterns = [
    path("comments/<int:id>", AddComment.as_view(), name="create-comment")
]