import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

CATEGORY_CHOICES = (
    ('Reptiles', 'Reptiles'),
    ('Canidae', 'Canidae'),
    ('Amphibians', 'Amphibians'),
    ('Inverts', 'Inverts'),
    ('Marsupials', 'Marsupials')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Pet(models.Model):
    NAME_MAX_LENGTH = 30
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    scientificName = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    type = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    careDetails = models.TextField()
    orders = models.IntegerField(default=0)
    date_added = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='pet_images', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pet, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("exotic_bay:type:pet", kwargs={
            'slug': self.slug
        })

    def get_remove_from_basket_url(self):
        return reverse("exotic_bay:remove-from-basket", kwargs={
            'slug': self.slug
        })

    def is_new(self):
        date_added = self.date_added
        today = datetime.date.today()
        new_period = datetime.timedelta(weeks=4)
        zero = datetime.timedelta(days=0)

        last_month = today - new_period
        return new_period >= (date_added - last_month) >= zero


class PetOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.pet.name}"

    def get_total_pet_price(self):
        return self.quantity * self.pet.price

    def get_final_price(self):
        return self.get_total_pet_price()


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    pets = models.ManyToManyField(PetOrder)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for pet_order in self.pets.all():
            total += pet_order.get_final_price()
        return total


class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return self.user.username


class License(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    license = models.FileField(upload_to='licenses/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s {self.pet.name} license"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
