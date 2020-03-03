from django.urls import path
from exotic_bay import views

app_name = 'exotic_bay'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us, name='contact'),
    path('about/', views.about, name='about'),
]