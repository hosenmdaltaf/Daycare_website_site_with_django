
from django.shortcuts import render
from classes.models import Services,Slider,Gallery,Contact,Service_add
from classes.sms import smsapi

import requests

def homepage(request):
    sms_send = None
    # services= Services.objects.all()
    all_service =Service_add.objects.all()
    homeservices= Services.objects.all()[:3] 
    sliders=Slider.objects.all()

    if request.method == "POST":
        data = request.POST
        if data['Servicesname'] != 'none':
            Servicesname = Service_add.objects.get(id=data['Servicesname'])
        else:
            Servicesname = None
        name = request.POST.get("name")
        message = request.POST.get("message")
        phonenumber = request.POST.get("phonenumber") 
        nid = request.POST.get("nid") 
        Contact.objects.create(name=name,message=message,phonenumber=phonenumber,Servicesname=Servicesname,nid=nid)
        msg = f"""
        name: {name}.
        message: {message}. 
        phonenumber: {phonenumber}.
        NID Number: {nid}.  
        Servicesname: {Servicesname}
        """
        receiver = '01880871297'
        sms_send = smsapi(msg,receiver)
        return render(request,'global/thankyou.html')
    return render(request,'classes/homepage.html',{'homeservices':homeservices,'sliders':sliders,
    'all_service':all_service,'sms_send':sms_send})


def classes(request):
    classes = Services.objects.all()
    return render(request,'classes/class.html' ,{'classes':classes})


def servicesDetailView(request,pk):
    sms_send = None
    object= Services.objects.get(pk=pk)
    latest = Services.objects.all()[:2]
    all_service =Service_add.objects.all()

    if request.method == "POST":
        data = request.POST
        if data['Servicesname'] != 'none':
            Servicesname = Service_add.objects.get(id=data['Servicesname'])
        else:
            Servicesname = None
        name = request.POST.get("name")
        message = request.POST.get("message")
        phonenumber = request.POST.get("phonenumber") 
        nid = request.POST.get("nid") 
        Contact.objects.create(name=name,message=message,phonenumber=phonenumber,Servicesname=Servicesname,nid=nid)
        msg = f"""
        name: {name}.
        message: {message}. 
        phonenumber: {phonenumber}.
        NID Number: {nid}. 
        Servicesname: {Servicesname}
        """
        receiver = '01880871297'
        sms_send = smsapi(msg,receiver)
        
        return render(request,'global/thankyou.html')
    return render(request,'classes/classdetail.html',{'object':object,'latest':latest,'all_service':all_service,'sms_send':sms_send})


def contact(request,*args):
    sms_send = None
    all_service =Service_add.objects.all()
    
    if request.method == "POST":
        data = request.POST
        if data['Servicesname'] != 'none':
            Servicesname = Service_add.objects.get(id=data['Servicesname'])
        else:
            Servicesname = None
        name = request.POST.get("name")
        message = request.POST.get("message")
        phonenumber = request.POST.get("phonenumber") 
        nid = request.POST.get("nid") 
        Contact.objects.create(name=name,message=message,phonenumber=phonenumber,Servicesname=Servicesname,nid=nid)

        msg = f"""
        name: {name}.
        message: {message}. 
        phonenumber: {phonenumber}.
        NID Number: {nid}. 
        Servicesname: {Servicesname}
        """
        receiver = '01880871297'
        sms_send = smsapi(msg,receiver)
        return render(request,'global/thankyou.html')
    return render(request,"classes/contact.html",{'all_service':all_service,'sms_send':sms_send})


def about(request):
    return render(request,"classes/about.html")

def gallery(request):
   
    gallerys = Gallery.objects.all()  
    return render(request,'classes/gallery.html',{'gallerys':gallerys})
