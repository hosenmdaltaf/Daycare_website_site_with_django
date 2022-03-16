from django.db import models

# Create your models here.
class Slider(models.Model):
    image=models.ImageField(default="img/banner/slider1.jpeg")

class Gallery(models.Model):
    image=models.ImageField(null=True,blank=True)  
