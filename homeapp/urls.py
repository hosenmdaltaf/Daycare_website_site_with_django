from django.urls import path

from . import views


app_name='homeapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),

]
      

      
