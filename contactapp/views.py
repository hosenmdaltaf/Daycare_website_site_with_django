from django.shortcuts import render

from contactapp.models import Contact
from classes.models import Services
from homeapp.models import Gallery

from classes.sms import smsapi


def contact(request):
  
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

        msg = f"""
        name: {name}.
        message: {message}. 
        phonenumber: {phonenumber}. 
        Servicesname: {Servicesname}
        """
        receiver = '+8801880871297'
        sms_status = smsapi(receiver, msg)
        return render(request,'homeapp/thankyou.html')
    return render(request,'contactapp/contact.html',{'services':services})


def about(request):
    return render(request,'contactapp/about.html')

def team(request):
    gallerys = Gallery.objects.all()
    return render(request,'contactapp/gallery.html',{'gallerys':gallerys})

