from django.contrib import admin

from exotic_bay.models import Pet, PetOrder, Order, License, Payment, Address, UserProfile


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'shipping_address',
        'billing_address',
        'payment'
    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment'
    ]
    list_filter = [
        'ordered',
        'being_delivered',
        'received', ]
    search_fields = [
        'user__username',
        'ref_code'
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'postcode',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'postcode']


admin.site.register(Pet)
admin.site.register(PetOrder)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(License)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)