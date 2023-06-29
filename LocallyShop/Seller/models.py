from django.db import models
from django.contrib.auth.models import User
from Core.models import Category
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance.User.username,instance.category.Title,filename)


class Product(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Title = models.CharField(max_length=255,null=True)
    Description = models.TextField(null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Qty = models.PositiveSmallIntegerField(null=True)
    Price = models.PositiveBigIntegerField(null=True)
    Image = models.ImageField(upload_to=user_directory_path,null=True)
    Size = models.CharField(max_length=255,blank=True,null=True)