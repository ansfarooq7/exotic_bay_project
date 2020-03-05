from django.urls import path
from exotic_bay import views

app_name = 'exotic_bay'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('success/', views.success, name='success'),
    path('<type>/<slug:pet_name_slug>/', views.pet_details, name='pet_details'),
    path('basket/', views.basket,name='basket'),
]