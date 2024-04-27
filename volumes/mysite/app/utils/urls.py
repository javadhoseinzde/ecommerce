from django.urls import path
from .views import ContactUsFormView, AboutUs, BugBountyFormView, Privacy

urlpatterns = [
    path("contact_us/", ContactUsFormView.as_view(), name="contact-us"),
    path("about-us/", AboutUs.as_view(), name="about-us"),
    path("report/", BugBountyFormView.as_view(), name="bug-bounty"),
    path("privacy/", Privacy.as_view(), name="privacy"),

]