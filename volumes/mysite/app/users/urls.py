from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .dashboard.views import Dashboard, PurchasedProductsView, CommentListView, ProductReturnForm

urlpatterns = [
	# path('login/', views.mobile_login, name="mobile_login"),
	path("dashboard/", Dashboard.as_view(), name="dashboard"),
	path("register", views.register_view, name="register_view"),
	path("verify/", views.verify ,name="verify"),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path("purchased-product/", PurchasedProductsView.as_view(), name="purchased-product"),
	path("comment-list/", CommentListView.as_view(), name="comment-list"),
	path("return-product/", ProductReturnForm.as_view(), name="return-product")

]
