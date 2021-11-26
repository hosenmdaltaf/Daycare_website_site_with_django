from django.db import models


# Category as a services

class Services(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image=models.ImageField(upload_to='post_images', blank=True, null=True)
    out = models.DateTimeField(null=True, help_text="When childfinish there class")
    _in = models.DateTimeField(null=True, help_text="When childstart there class")
    childagestart=models.CharField(max_length=2,null=True, help_text="When childagestart there class")
    childagefinish=models.CharField(max_length=2,null=True, help_text="When childagefinish there class")


    def duration(self):
        return self.out - self._in

    # def agelimit(self):
    #     return str(self.childagestart) - str(self.childagefinish)

    def __str__(self):
        return str(self.title)
