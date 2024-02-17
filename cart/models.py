from django.db import models
from shop.models import *
# Create your models here.
class cart_id(models.Model):
    c_id=models.CharField(max_length=250,unique=True)
    add_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.c_id

class Items(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart_id,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.prodt
    def total(self):
        return self.quantity*self.prodt.price