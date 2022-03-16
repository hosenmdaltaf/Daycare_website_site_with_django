from django.shortcuts import render
# import requests
# import json

from classes.models import Services
from contactapp.models import Contact

from classes.sms import smsapi

def homepage(request):
    services= Services.objects.all()
    homeservices= Services.objects.all()[:3]

    if request.method == "POST": 
        data = request.POST
        if data['Servicesname'] != 'none':
            Servicesname = Services.objects.get(id=data['Servicesname'])
        else:
            Servicesname = None
        name = request.POST.get("name")
        message = request.POST.get("message")
        phonenumber = request.POST.get("phonenumber") 
        Contact.objects.create(name=name,message=message,phonenumber=phonenumber,Servicesname=Servicesname)
        msg = f"""
        name: {name}.
        message: {message}. 
        phonenumber: {phonenumber}. 
        Servicesname: {Servicesname}
        """
        receiver = '+8801880871297'
        sms_status = smsapi(receiver, msg)
        return render(request,'global/thankyou.html')
    return render(request,'classes/homepage.html',{'services':services,'homeservices':homeservices})


def classes(request):
    classes = Services.objects.all()
    return render(request,'classes/class.html' ,{'classes':classes})


def servicesDetailView(request,pk):
    object= Services.objects.get(pk=pk)
    latest = Services.objects.all()[:2]
    services= Services.objects.all()

    if request.method == "POST":
        data = request.POST
        if data['Servicesname'] != 'none':
            Servicesname = Services.objects.get(id=data['Servicesname'])
        else:
            Servicesname = None
        name = request.POST.get("name")
        message = request.POST.get("message")
        phonenumber = request.POST.get("phonenumber") 
    
        Contact.objects.create(name=name,message=message,phonenumber=phonenumber,Servicesname=Servicesname)
        # smsapi(receiver,'my msg')
        # msg = f"name:{name},message:{message},phonenumber:{phonenumber},Servicesname:{Servicesname}"
        msg = f"""
        name: {name}.
        message: {message}. 
        phonenumber: {phonenumber}. 
        Servicesname: {Servicesname}
        """
        receiver = '+8801880871297'
        sms_status = smsapi(receiver, msg)
        
        return render(request,'global/thankyou.html')
    return render(request,'classes/classdetail.html',{'object':object,'latest':latest,'services':services})
    
