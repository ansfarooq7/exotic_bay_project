import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from exotic_bay.forms import ContactForm, RegisterForm, BasketAddPetForm
from exotic_bay.models import Pet, PetOrder, Basket


def home(request):
    context_dict = {}
    context_dict['pets'] = Pet.objects.all()
    context_dict['recently_added'] = Pet.objects.filter(
        date_added__gte=datetime.date.today() - datetime.timedelta(days=1))

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/home.html', context=context_dict)

    # Render the response and send it back.
    return response


def pet_details(request, type, pet_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a pet name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        pet = Pet.objects.get(slug=pet_name_slug)

        context_dict['name'] = pet.name
        context_dict['scientificName'] = pet.scientificName
        context_dict['price'] = pet.price
        context_dict['type'] = pet.type
        context_dict['stock'] = pet.stock
        context_dict['description'] = pet.description
        context_dict['careDetails'] = pet.careDetails
        context_dict['image'] = pet.image
        context_dict['form'] = BasketAddPetForm

        # We also add the pet object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the pet exists.
        context_dict['pet'] = pet

    except Pet.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['pet'] = None

    # Go render the response and return it to the client.
    return render(request, 'exotic_bay/pet.html', context=context_dict)


def about(request):
    context_dict = {}

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/about.html', context=context_dict)

    # Render the response and send it back.
    return response


# def register(request):
#     registered = False
#
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#
#         if user_form.is_valid():
#             user = user_form.save()
#
#             user.set_password(user.password)
#             user.save()
#
#             profile.user = user
#
#             profile.save()
#
#             registered = True
#         else:
#             print(user_form.errors)
#     else:
#         user_form = UserForm()
#
#     return render(request, 'exotic_bay/register.html', context={'user_form': user_form, 'registered': registered})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(response, "exotic_bay/register.html", context={"form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('exotic_bay:home'))
            else:
                return HttpResponse("Your Exotic-Bay account is disabled.")
        else:
            print("Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'exotic_bay/login.html')


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('exotic_bay:home'))


def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['2384693A@student.gla.ac.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('exotic_bay:success')
    return render(request, 'exotic_bay/contact_us.html', {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')


def basket(request):
    context_dict = {}

    response = render(request, 'exotic_bay/basket.html', context=context_dict)

    return response


def watchlist(request):
    context_dict = {}

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/watchlist.html', context=context_dict)

    # Render the response and send it back.
    return response


@login_required
def add_to_basket(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    form = BasketAddPetForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity']
        pet_order, created = PetOrder.objects.get_or_create(
            pet=pet,
            user=request.user,
            ordered=False
        )
        basket_qs = Basket.objects.filter(user=request.user, ordered=False)
        if basket_qs.exists():
            basket = basket_qs[0]
            # check if the pet order is in the basket
            if basket.pets.filter(pet__slug=pet.slug).exists():
                pet_order.quantity += quantity
                pet_order.save()
                messages.info(request, "This pet's quantity was updated.")
                return redirect("exotic_bay:basket")
            else:
                basket.pets.add(pet_order)
                messages.info(request, "This pet was added to your basket.")
                return redirect("exotic_bay:basket")
        else:
            ordered_date = timezone.now()
            basket = Basket.objects.create(
                user=request.user, ordered_date=ordered_date)
            basket.pets.add(pet_order)
            messages.info(request, "This pet was added to your basket.")
            return redirect("exotic_bay:basket")
    return redirect('exotic_bay:basket')
