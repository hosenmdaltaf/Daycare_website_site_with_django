from django.db import models
from classes.models import Services

# Create your models here.
class Contact(models.Model):
    Servicesname = models.ForeignKey(Services,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField()
    phonenumber= models.CharField(max_length=13)

    def __str__(self):
        return str(self.name) + '------' + str(self.Servicesname)