from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CommnetForm
from app.shop.models import Product
from django.contrib import messages
from .query import add_comment




class AddComment(View):
	
	def post(self,request, id):
		user = self.request.user

		content = self.request.POST.get("contnet")

		query = add_comment(content, id, user)
		get_id = Product.objects.get(id=id)
		if query:
			messages.success(request, "کامنت شما با موفقیت ثبت شد")
		else:
			messages.error(request, "در ثبت نظر شما مشکلی پیش آمده لطقا مججد امتحان کنید")

		return redirect('shop:detail', get_id.id)