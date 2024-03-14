from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .models import MyUser
# Create your views here.
from . import forms
from . import helper
from django.contrib import messages

def register_view(request):
	form = forms.RegisterForm
	if request.method == "POST":
		try:
			if "mobile" in request.POST:
				mobile = request.POST.get("mobile")
				user = MyUser.objects.get(mobile=mobile)
				#send otp
				otp = helper.get_random_otp()
				helper.send_otp(mobile, otp)
				#save otp
				print("OTP",otp)
				user.otp = otp
				user.save()
				request.session['user_mobile'] = user.mobile
				#redirect to verify		
				return HttpResponseRedirect(reverse('verify'))
		except MyUser.DoesNotExist:
			form = forms.RegisterForm(request.POST)
			if form.is_valid():
				user = form.save(commit=False)
				otp = helper.get_random_otp()
				# helper.send_otp(mobile, otp)
				# save otp
				print("OTP",otp)
				user.otp = otp
				user.is_active = False
				user.save()
				request.session['user_mobile'] = user.mobile
				return HttpResponseRedirect(reverse('verify'))

				#redirect to verify
	return render(request, "user/register.html", {'form':form})

def verify(request):
	try:
		mobile = request.session.get('user_mobile')
		user = MyUser.objects.get(mobile=mobile)
		print("user otp")
		print(user.otp)

		if request.method == "POST":
			otp = request.POST.get("otp")
			#check otp expiration
			if not helper.check_otp_expiration(user.mobile):
				messages.error(request, "OTP is expire pleasee try again")
				print("otp expire")
				return HttpResponseRedirect(reverse('verify'))


			if user.otp != int(otp):
				messages.error(request, "OTP is incorrect pleasee try again")
				print("otp is incorrect")
				return HttpResponseRedirect(reverse('verify'))
			else:
				user.is_active = True	
				user.save()
				
				login(request, user)
				return HttpResponseRedirect(reverse('shop:index'))
	except MyUser.DoesNotExist:
		print("MYUSER DOESNOTEXIST")
		messages.error(request, "Error accrded try again")
		return HttpResponseRedirect(reverse('register_view'))
	return render(request, 'user/verify.html', {'user':user})

# def mobile_login(request):
# 	if request.method == "POST":
# 		if "mobile" in request.POST:
# 			mobile = request.POST.get("mobile")
# 			print(mobile)
# 			user = MyUser.objects.get(mobile=mobile)
# 			login(request, user)
# 			return HttpResponseRedirect(reverse('dashboard'))
# 	return render(request, 'mobile_login.html')
# def dashboard(request):
# 	return render(request, "dashboard.html")

