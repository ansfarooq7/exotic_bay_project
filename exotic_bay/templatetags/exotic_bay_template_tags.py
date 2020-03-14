from django import template

from exotic_bay.models import Basket

register = template.Library()


@register.filter
def basket_pet_count(user):
    if user.is_authenticated:
        qs = Basket.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].pets.count()
    return 0
