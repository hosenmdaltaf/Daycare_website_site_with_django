from django.urls import path
from .import views
from contactapp.views import ContactCreateView


app_name='contactapp'

urlpatterns = [
    path('add/', ContactCreateView.as_view(), name='author-add'),
    path('contactus/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
 
]
      
