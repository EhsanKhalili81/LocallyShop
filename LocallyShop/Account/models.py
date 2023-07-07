from django.db import models
from django.contrib.auth.models import User
from extensions.utlis import Jalali_Converter
from django.utils import timezone

class Userinformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    tel = models.PositiveBigIntegerField(blank=True,null=True)
    is_seller = models.BooleanField(default=False)
    kodeposti = models.PositiveBigIntegerField(blank=True,null=True)

class SellerRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    workspacename = models.CharField(max_length=255)
    workspacetel = models.PositiveBigIntegerField()
    kodeposti = models.PositiveBigIntegerField()
    address = models.TextField(max_length=500)
    describe = models.TextField(max_length=750)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def Jpublish(self):
        return Jalali_Converter(self.date_created)
    