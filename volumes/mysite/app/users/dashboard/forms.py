from django import forms
from app.users.models import ProductReturnModel

class ProductReturnForm(forms.ModelForm):
    class Meta:
        model = ProductReturnModel
        fields = "__all__"