from django.db import models
from django.contrib.auth.models import User

class Userinformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    tel = models.PositiveBigIntegerField()
    is_seller = models.BooleanField(default=False)
    kodeposti = models.PositiveBigIntegerField()

