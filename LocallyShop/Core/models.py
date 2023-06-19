from django.db import models

# Create your models here.
def file_path(instance, filename):
    return '{0}/{1}'.format(instance.Title,filename)


class Category(models.Model):
    Title=models.CharField(max_length=100)
