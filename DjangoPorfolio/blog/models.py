from django.db import models
import datetime 

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300000)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField(datetime.date.today)
