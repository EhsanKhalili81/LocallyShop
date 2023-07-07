from django.db import models
from django.contrib.auth.models import User
from Core.models import Category
from extensions.utlis import Jalali_Converter
from django.utils import timezone
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance.User.username,instance.category.Title,filename)


class Product(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    Title = models.CharField(max_length=255,default=None)
    Description = models.TextField(default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    Qty = models.PositiveSmallIntegerField(default=None)
    Price = models.PositiveBigIntegerField(default=None)
    Image = models.ImageField(upload_to=user_directory_path,default=None)
    Size = models.CharField(max_length=255,default=None)
    date_created = models.DateTimeField(default=timezone.now)

    def Jpublish(self):
        return Jalali_Converter(self.date_created)