from django.shortcuts import render, redirect, get_list_or_404, HttpResponse
from .models import ShopCart
from app.shop.models import Product
from django.views.generic import View, ListView
from django.contrib import messages


def get_cart(user):
	a = ShopCart.objects.filter(user=user).exists()
	if a == False:
		return False

	else:
		# return get_list_or_404(ShopCart, user=user)
		return True

def add_cart(user,product, quantity, variant):
	return ShopCart.objects.create(
		user = user ,
		product_id = product, 
		quantity = quantity,
		variant_id = variant

	)

	

def delete_cart(user,id):
	return ShopCart.objects.filter(user=user,
				 id=id).delete()

def update_cart(user, id, quantity):
	try:
		return ShopCart.objects.filter(user=user,
					id=id).update(quantity=quantity)

	except:
		query = ShopCart.objects.get(user=user,id=id)
		quantity = query.quantity
		return ShopCart.objects.filter(user=user,
					id=id).update(quantity= quantity+1)

#ADD PRODUCT TO CART
class AddToCart(View):
	def post(self,request, id):
		user = self.request.user
		
		# product = self.request.POST.get("product")
		variant = self.request.POST.get("variant")
		print("_________##################$$$$$$$$$$$$$$$$$$$$$$$$$")
		print(variant)
		print("_________##################$$$$$$$$$$$$$$$$$$$$$$$$$")

		if ShopCart.objects.filter(product=id, user=user,variant_id=variant).exists():
			print("update")

			quan = ShopCart.objects.get(user=user,product=id, variant_id=variant)
			count = quan.quantity + 1
			query = ShopCart.objects.filter(product=id, user=user, variant_id=variant).update(quantity=count)
			# update_cart(user=user,id=id, quantity=quantity)
		else:
			query = add_cart(product=id,quantity="1", user=user, variant=variant)
		get_id = Product.objects.get(id=id)
		if query:
			messages.success(request,"به سبد خرید اضافه شد")
		else:
			messages.error(request, "در ثبت نظر شما مشکلی پیش آمده لطقا مججد امتحان کنید")

		return redirect('shop:detail', get_id.id, get_id.slug)
	

#DELETE PRODUCT FROM CART
class DeleteCart(View):
	def post(self,request, id):
		user = self.request.user


		query = delete_cart(id=id, user=user)

		if query:
			messages.success(request,"با موفقیت حذف شد")
		else:
			messages.error(request, "در ثبت نظر شما مشکلی پیش آمده لطقا مججد امتحان کنید")

		return redirect('cart:cart-list')
	

#UPDATE PRODUCT FROM CART
class UpdateCart(View):
	def post(self,request, id):
		user = self.request.user
		quantity = self.request.POST.get("quantity")
		print(20 * "*",quantity)

		query = update_cart(id=id, user=user, quantity=quantity)
		if query:
			messages.success(request,"با موفقیت اپدیت شد")
		else:
			messages.error(request, "در ثبت نظر شما مشکلی پیش آمده لطقا مججد امتحان کنید")

		return redirect('cart:cart-list')

class CartList(ListView):
	template_name = "cart/cart-list.html"
	def get_queryset(self):
		user = self.request.user

		quer = get_cart(user)
		total = 0


		if quer == True:
			query = ShopCart.objects.filter(user=user)
			print(query)
			total_discount = 0
			for i in query:

				total_dis =  i.product.calculate_discount() * i.quantity
				total_disc = int(i.variant.price) * i.quantity - total_dis
				total_discount += int(total_disc)
			print(total_discount)
			for i in query:
				total +=  int(i.sums())
			queryset = {
				"query": query,
				"total": total_discount,
			}
			return queryset
		
		else:
			queryset = {
				"total": total,
			}
			return queryset
