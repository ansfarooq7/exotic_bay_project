from django.urls import path
from exotic_bay import views

app_name = 'exotic_bay'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact_us, name='Contact Us'),
    path('about/', views.about, name='about'),
]