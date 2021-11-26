from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm


from django.views.generic.edit import CreateView
from contactapp.models import Contact

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name','message','phonenumber', 'Servicesname']
    template_name='homeapp/contactForm.html'

#   comments_form = ContactForm()   

#     if request.method == 'POST': 
#         comments_form = CommentForm(request.POST )  
#         if comments_form.is_valid(): 
#             comments_form.instance.created_by = request.user.profile
#             comment = comments_form.save(commit=False)
#             comment.post = details
#             comments_form.save() 
#             return redirect("user_feeds:articale-detail", id=post.id )  
#         else: 
#             comments_form = CommentForm() 

def contact(request):
    if request.method == "POST":
        contact_form =ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/thanks/')
        else:
            contact_form=ContactForm()

    return render(request,'contactapp/contact.html')


def about(request):
    return render(request,'contactapp/about.html')

def team(request):
    return render(request,'contactapp/team.html')