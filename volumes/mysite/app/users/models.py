from django.db import models
from django.contrib.auth.models import AbstractUser
from app.users.myusermanager import MyUserManager
from app.shop.models import Product

class MyUser(AbstractUser):
	username = None
	mobile = models.CharField(max_length=11, unique=True)
	otp = models.PositiveIntegerField(blank=True, null=True)
	otp_create_time = models.DateTimeField(auto_now=True)

	objects = MyUserManager()

	USERNAME_FIELD = 'mobile'
	REQUIRED_FIELDS = []

	backend = 'app.users.mybackend.ModelBackend'




class ProductReturnModel(models.Model):
	RETERN_LEVEL = [
		("دیده نشده","دیده نشده"),
		("در حال بررسی","در حال بررسی"),
		("تایید شده تماس میگیریم","تایید شده تماس میگیریم"),
	]
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	description = models.TextField()
	status = models.CharField(max_length=100, choices=RETERN_LEVEL)
	image = models.ImageField(upload_to="ProductReturn", null=True)
	image1 = models.ImageField(upload_to="ProductReturn", null=True)
	image2 = models.ImageField(upload_to="ProductReturn", null=True)


