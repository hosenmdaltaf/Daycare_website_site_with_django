
from django.db import models

# Category as a services

class Services(models.Model):
    title = models.CharField(max_length=200,help_text="write title about your service")
    content = models.TextField(help_text="write in detail about your service")
    image=models.ImageField(upload_to='post_images', blank=True, null=True)
    classtimestart = models.CharField(max_length=7,blank=True, null=True, help_text="When childfinish there class")
    classtimefinish = models.CharField(max_length=7,blank=True, null=True, help_text="When childstart there class")
    childagestart=models.CharField(max_length=2,blank=True, null=True, help_text="When childagestart there class")
    childagefinish=models.CharField(max_length=2,blank=True, null=True, help_text="When childagefinish there class")
    price = models.IntegerField(null=True,blank=True,help_text="class/service fee")
    durationofclass= models.IntegerField(null=True,blank=True,help_text="how long child stay in class in a day")
   
    def __str__(self):
        return str(self.title)

class Slider(models.Model):
    image=models.ImageField(default="img/banner/slider1.jpeg")

class Gallery(models.Model):
    image=models.ImageField(null=True,blank=True)  


# CATEGORY_CHOICES = (
# ("HO", "Hostel"),
# ("HA", "Halfday"),
# ("FD", "Fullday"),
# ("AS", "After-school"),
# ("HD", "Holiday"),
# ("NS", "Night-stay"),)

class Service_add(models.Model):
    category = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.category)

class Contact(models.Model):
    Servicesname = models.ForeignKey(Service_add,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    phonenumber= models.CharField(max_length=13,null=True,blank=True)
    nid = models.CharField(max_length=14,null=True,blank=True )

    def __str__(self):
        return str(self.name) + '------' + str(self.Servicesname)

class Features(models.Model):
    icon = models.ImageField(upload_to='features_images', blank=True, null=True)
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
