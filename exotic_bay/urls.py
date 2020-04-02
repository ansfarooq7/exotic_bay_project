from django.urls import path

from exotic_bay import views

app_name = 'exotic_bay'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us, name='contact'),
    path('about/', views.about, name='about'),
    path('success/', views.success, name='success'),
    path('<type>/<slug:pet_name_slug>/', views.pet_details, name='pet_details'),
    path('basket/', views.basket, name='basket'),
    path('add-to-basket/<slug>', views.add_to_basket, name='add-to-basket'),
    path('remove-single-pet-from-basket/<slug>', views.remove_single_pet_from_basket,
         name='remove-single-pet-from-basket'),
    path('remove-pet-from-basket/<slug>', views.remove_pet_from_basket,
         name='remove-pet-from-basket'),
    path('add-single-pet-to-basket/<slug>', views.add_single_pet_to_basket,
         name='add-single-pet-to-basket'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('add-to-watchlist/<slug>', views.add_to_watchlist, name='add-to-watchlist'),
    path('remove-from-watchlist/<slug>', views.remove_from_watchlist, name='remove-from-watchlist'),
    path('delete-user-profile/', views.deactivate_user_view, name='delete-user-profile'),
    path('delete-user/', views.deactivate_user, name='delete-user'),
    path('search/', views.search, name='search'),
    path('reptiles/<sortBy>', views.reptiles, name='reptiles'),
    path('canidae/<sortBy>', views.canidae, name='canidae'),
    path('amphibians/<sortBy>', views.amphibians, name='amphibians'),
    path('inverts/<sortBy>', views.inverts, name='inverts'),
    path('marsupials/<sortBy>', views.marsupials, name='marsupials'),
    path('pets/<sortBy>', views.pets, name='pets'),
    path('license/', views.petLicense, name='license'),
]
