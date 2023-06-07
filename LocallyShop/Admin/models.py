from django.db import models
import datetime,os

# Create your models here.

def filepath(filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Slider(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    Image = models.ImageField(upload_to=filepath,null=True,blank=True)