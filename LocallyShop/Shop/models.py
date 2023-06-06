from django.db import models
from django.contrib.auth.models import User
from Seller.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sumprice = models.PositiveBigIntegerField()
    orderstatus = models.SmallIntegerField()


class Basket(models.Model):
    orderid = models.ForeignKey(Order,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.SmallIntegerField()
    price = models.PositiveBigIntegerField()
