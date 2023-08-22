from django.shortcuts import render, redirect, get_list_or_404
from .models import ShopCart
from app.shop.models import Product
from django.views.generic import View, ListView
from django.contrib import messages


def get_cart(user):
	return get_list_or_404(ShopCart, user=user)


def add_cart(user,product, quantity):
    return ShopCart.objects.create(
	    user = user ,
        product_id = product, 
        quantity = quantity
    )

def delete_cart(user,id):
	return ShopCart.objects.filter(user=user,
				 id=id).delete()

def update_cart(user, id, quantity):
	return ShopCart.objects.filter(user=user,
				 id=id).update(quantity=quantity)


#ADD PRODUCT TO CART
class AddToCart(View):
	def post(self,request, id):
		user = self.request.user
		# product = self.request.POST.get("product")
		quantity = self.request.POST.get("quantity")

		query = add_cart(product=id,quantity=quantity, user=user)
		get_id = Product.objects.get(id=id)
		if query:
			messages.success(request,"به سبد خرید اضافه شد")
		else:
			messages.error(request, "در ثبت نظر شما مشکلی پیش آمده لطقا مججد امتحان کنید")

		return redirect('shop:detail', get_id.id)
	

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
		for i in quer:
			total +=  int(i.sums())
		queryset = {
			"query": get_cart(user),
			"total": total,
		}
		return queryset


