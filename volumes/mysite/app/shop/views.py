from typing import Any, Optional


from django.views.generic import ListView, DetailView

from .query import filter_product, get_product ,get_comment

class IndexView(ListView):
    template_name = "shop/index.html"

    def get_queryset(self):
        queryset = {
            "query": filter_product(),
        }
        return queryset


class ProductDetail(DetailView):
    template_name = "shop/product-detail.html"


    def get_object(self):
        pk = self.kwargs.get("pk")
        queryset = {
            "detail": get_product(pk),
            "comment": get_comment(pk),
        }
        return queryset
    
