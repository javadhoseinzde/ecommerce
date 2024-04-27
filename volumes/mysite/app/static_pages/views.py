from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutUs(TemplateView):
    template_name = "static_pages/about_us.html"
