from django.db import models


# Category as a services

class Services(models.Model):
    title = models.CharField(max_length=200,help_text="write title about your service")
    content = models.TextField(help_text="write in detail about your service")
    image=models.ImageField(upload_to='post_images', blank=True, null=True)
    classtimestart = models.CharField(max_length=7,null=True, help_text="When childfinish there class")
    classtimefinish = models.CharField(max_length=7,null=True, help_text="When childstart there class")
    childagestart=models.CharField(max_length=2,null=True, help_text="When childagestart there class")
    childagefinish=models.CharField(max_length=2,null=True, help_text="When childagefinish there class")
    price = models.IntegerField(null=True,blank=True,help_text="class/service fee")
    durationofclass= models.IntegerField(null=True,blank=True,help_text="how long child stay in class in a day")
   
    def __str__(self):
        return str(self.title)
