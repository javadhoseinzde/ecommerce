from ..models import Category
from django import template

register = template.Library()

@register.inclusion_tag("shop/partials/category_navbar.html")
def category_navbar():
	return {
		"category": Category.objects.filter(status=True)
	}


