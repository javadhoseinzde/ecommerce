from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Product

class ProductSiteMap(Sitemap):
	changefreq = 'weekly'

	priority = 0.9
	protocol = 'http'


	def items(self):
		return Product.objects.filter(status='True')

	def location(self,obj):
		#return '/details/%s' % (obj.id) % "/" % (obj.slug)
		return f"/details/{obj.id}/{obj.slug}"
