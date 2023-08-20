from django.db import models
from app.users.models import MyUser
from app.common.models import BaseModel
from app.shop.models import Product

class Comments(BaseModel):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title + " " + self.user.mobile
    
    