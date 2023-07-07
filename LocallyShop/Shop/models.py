from django.db import models
from django.contrib.auth.models import User
from Seller.models import Product
from extensions.utlis import Jalali_Converter
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sumprice = models.PositiveBigIntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    orderstatus = models.SmallIntegerField(default=0)
        
    def Jpublish(self):
        return Jalali_Converter(self.date_created)


class Basket(models.Model):
    orderid = models.ForeignKey(Order,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    countp = models.SmallIntegerField()
    price = models.PositiveBigIntegerField()

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def Jpublish(self):
        return Jalali_Converter(self.date_created)



