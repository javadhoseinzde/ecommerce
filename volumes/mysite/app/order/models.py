from django.db import models
from app.common.models import BaseModel
from app.users.models import MyUser
from app.shop.models import Product, Variants
# Create your models here.

class Order(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f"Order {self.id}"
    

class OrderItem(BaseModel):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    variants = models.ForeignKey(Variants,
                                related_name="order_items",
                                on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    

    
