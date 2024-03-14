from django.urls import path
from .views import CategoryFilter
app_name = "category"
urlpatterns = [
    path("category/<slug:slug>", CategoryFilter.as_view(), name="category-filter")
]