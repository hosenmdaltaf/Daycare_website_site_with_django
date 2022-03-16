from django.urls import path

from . import views


app_name='classes'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('classes/', views.classes, name='classes'),
    path('<int:pk>/', views.servicesDetailView, name='services-detail'),
    # path('<int:pk>/', ServicesDetailView.as_view(), name='services-detail'),
]




      