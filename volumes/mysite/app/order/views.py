from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect ,HttpResponse
from .forms import OrderForm
from app.cart.models import ShopCart
from django.views.generic import ListView, View
from django.contrib import messages
from .models import Order, OrderItem
from .query import create_order
from app.users.models import MyUser


def order_view(request):
	user = request.user
	query = ShopCart.objects.filter(user=user)
	total = 0
	for q in query:
		total +=  int(q.sums())
		print(q.product.title)
		print(q.quantity)
	print(total)
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid:
			form.save()

	else:
		form = OrderForm()
	return render(request, "order/order_form.html", {"form":form, "total":total})


class OrderView(ListView):
	template_name = "order/order.html"

	def get_queryset(self) -> QuerySet[Any]:
		user = self.request.user
		query = ShopCart.objects.filter(user=user)
		total = 0
		for q in query:
			total +=  int(q.sums())
		return total
	

class OrderFormView(View):
	def post(self,request):
		user = self.request.user
		get_user = MyUser.objects.get(mobile=user)
		print(f"user id {get_user.id}")
		first_name = self.request.POST.get("first_name")
		last_name = self.request.POST.get("last_name")
		email = self.request.POST.get("email")
		address = self.request.POST.get("address")
		postal_code = self.request.POST.get("postal_code")
		city = self.request.POST.get("city")
		query = create_order(first_name, last_name, email, address, postal_code, city,user)
		print(f"form id {query.id}")
		create_cart = ShopCart.objects.filter(user=user)
		#in bayad toye payment bashe
		for i in create_cart:
			print("in for")
			OrderItem.objects.create(order=query, product_id=i.product.id, price=i.product.price, quantity=i.quantity)
			i.delete()
		if query:
			messages.success(request,"به سبد خرید اضافه شد")
		else:
			messages.error(request, "در ثبت نظر شما مشکلی پیش آمده لطقا مججد امتحان کنید")
			   
		return redirect("order:pay", query.id)
	

def payment(request, id):
	query = Order.objects.filter(id=id).update(paid=True)
	# for i in create_cart:
	# 	print("in for")
	# 	OrderItem.objects.create(order=query, product_id=i.product.id, price=i.product.price, quantity=i.quantity)
	# 	i.delete()
	return HttpResponse("PARDAKHT SHOD")

