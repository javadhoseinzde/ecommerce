from django.db import models
from app.common.models import BaseModel
from app.shop.models import Product, Variants
from app.users.models import MyUser
# Create your models here.
class ShopCart(BaseModel):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL,blank=True, null=True) # relation with varinat

    def sums(self):
        return self.product.price * self.quantity