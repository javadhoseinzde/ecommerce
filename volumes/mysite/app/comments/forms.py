from django.forms import ModelForm
from .models import Comments

class CommnetForm(ModelForm):
    class Meta:
        model = Comments

        fields = ("content",)

