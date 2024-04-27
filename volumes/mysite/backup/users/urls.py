from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .dashboard.views import Dashboard
urlpatterns = [
	# path('login/', views.mobile_login, name="mobile_login"),
	path("register/", views.register_view, name="register_view"),
	path("verify/", views.verify ,name="verify"),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("dashboard/", Dashboard.as_view(), name="dashboard")
]