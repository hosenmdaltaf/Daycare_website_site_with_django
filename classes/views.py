from django.shortcuts import render

from classes.models import Services

def classes(request):
    classes = Services.objects.all()
    return render(request,'classes/class.html' ,{'classes':classes})
