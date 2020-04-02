from django import forms
from django.contrib.auth.models import User

from exotic_bay.models import License, Pet


class BasketAddPetForm(forms.Form):
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class LicenseForm(forms.ModelForm):
    pet = forms.ModelChoiceField(queryset=Pet.objects.all(), empty_label=None)

    class Meta:
        model = License
        fields = ('pet', 'license',)
