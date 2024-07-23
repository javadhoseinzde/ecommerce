from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django import forms
from .models import ContactUs, BugBounty
# Create your views here.


class ContactUsFormView(FormView):

    class ContactUsForm(forms.ModelForm):
        class Meta:
            model = ContactUs
            fields = "__all__"
        
    template_name = "utils/contact_us.html"
    form_class = ContactUsForm
    success_url = "/"

    def form_valid(self, form):
        print("form valid")
        print(form)
        form.save()
        return super().form_valid(form)
    
class AboutUs(TemplateView):
    template_name = "utils/about-us.html"


class BugBountyFormView(FormView):
    class BugBountyForm(forms.ModelForm):
        class Meta:
            model = BugBounty
            fields = "__all__"

    template_name = "utils/bug-bounty.html"
    form_class = BugBountyForm
    success_url = "/"

    def form_valid(self, form):
        print("valid")
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("invalid")
        form.save()
        return super().form_invalid(form)
    
    
class Privacy(TemplateView):
    template_name = "utils/privacy.html"



class PaymentMethod(TemplateView):
    template_name = "utils/payment-method.html"


class ReturnProduct(TemplateView):
    template_name = "utils/return-product.html"


class ShippingMethod(TemplateView):
    template_name = "utils/shipping-method.html"
