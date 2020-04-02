from django.contrib import admin

from exotic_bay.models import Pet, PetOrder, Basket, License, UserProfile, Watchlist


class BasketAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
    ]
    list_display_links = [
        'user',
    ]
    list_filter = [
        'ordered',
        'being_delivered',
        'received', ]
    search_fields = [
        'user__username',
        'ref_code'
    ]


admin.site.register(Pet)
admin.site.register(PetOrder)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Watchlist)
admin.site.register(License)
admin.site.register(UserProfile)