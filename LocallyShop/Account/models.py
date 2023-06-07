from django.db import models
from django.contrib.auth.models import User

class Userinformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    tel = models.PositiveBigIntegerField(blank=True,null=True)
    is_seller = models.BooleanField(default=False)
    kodeposti = models.PositiveBigIntegerField(blank=True,null=True)

