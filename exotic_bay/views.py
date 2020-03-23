from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from exotic_bay.forms import ContactForm, BasketAddPetForm
from exotic_bay.models import Pet, PetOrder, Basket, Watchlist


def home(request):
    context_dict = {}
    context_dict['pets'] = Pet.objects.all()[:4]
    context_dict['recently_added'] = Pet.objects.all().order_by('-date_added')[:4]

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/home.html', context=context_dict)

    # Render the response and send it back.
    return response


def reptiles(request):
    context_dict = {}
    context_dict['reptiles'] = Pet.objects.filter(type='Reptiles')

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/reptiles.html', context=context_dict)

    # Render the response and send it back.
    return response


def canidae(request):
    context_dict = {}
    context_dict['canidae'] = Pet.objects.filter(type='Canidae')

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/canidae.html', context=context_dict)

    # Render the response and send it back.
    return response


def amphibians(request):
    context_dict = {}
    context_dict['amphibians'] = Pet.objects.filter(type='Amphibians')

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/amphibians.html', context=context_dict)

    # Render the response and send it back.
    return response


def inverts(request):
    context_dict = {}
    context_dict['inverts'] = Pet.objects.filter(type='Inverts')

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/inverts.html', context=context_dict)

    # Render the response and send it back.
    return response


def marsupials(request):
    context_dict = {}
    context_dict['marsupials'] = Pet.objects.filter(type='Marsupials')

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/marsupials.html', context=context_dict)

    # Render the response and send it back.
    return response


def searchMatch(query, item):
    if query in item.description.lower() or query in item.name.lower() or query in item.type.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allPets = []
    typePets = Pet.objects.values('type')
    types = {item['type'] for item in typePets}
    for type in types:
        tempPet = Pet.objects.filter(type=type)
        pet = [item for item in tempPet if searchMatch(query, item)]
        allPets.append(pet)
    context_dict = {'allPets': allPets}
    return render(request, 'exotic_bay/search.html', context_dict)


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
    response = render(request, 'exotic_bay/success.html')
    return response


def basket(request):
    try:
        pets = []
        petsInBasket = []
        basket = Basket.objects.get(user=request.user, ordered=False)

        for pet_order in basket.pets.all():
            petsInBasket.append(pet_order.pet)

        for pet in Pet.objects.all().order_by('orders'):
            if pet not in petsInBasket:
                pets.append(pet)

        context_dict = {
            'basket': basket,
            'alsoInterested': pets[:4]
        }
        response = render(request, 'exotic_bay/basket.html', context=context_dict)
        return response
    except ObjectDoesNotExist:
        messages.warning(request, "You do not have an active order")
        return redirect("/")


def watchlist(request):
    try:
        watchlist = Watchlist.objects.get(user=request.user)
        context_dict = {
            'watchlist': watchlist
        }
        response = render(request, 'exotic_bay/watchlist.html', context=context_dict)
        return response
    except ObjectDoesNotExist:
        messages.warning(request, "You do not have an active watchlist")
        return redirect("/")


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


@login_required
def remove_single_pet_from_basket(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    basket_qs = Basket.objects.filter(
        user=request.user,
        ordered=False
    )
    if basket_qs.exists():
        basket = basket_qs[0]
        # check if the pet order is in the basket
        if basket.pets.filter(pet__slug=pet.slug).exists():
            pet_order = PetOrder.objects.filter(
                pet=pet,
                user=request.user,
                ordered=False
            )[0]
            if pet_order.quantity > 1:
                pet_order.quantity -= 1
                pet_order.save()
            else:
                basket.pets.remove(pet_order)
            messages.info(request, "This pet quantity was updated.")
            return redirect("exotic_bay:basket")
        else:
            messages.info(request, "This pet was not in your basket")
            return redirect("exotic_bay:pet_details", type=pet.type, slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("exotic_bay:pet_details", type=pet.type, slug=slug)


@login_required
def add_single_pet_to_basket(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    basket_qs = Basket.objects.filter(
        user=request.user,
        ordered=False
    )
    if basket_qs.exists():
        basket = basket_qs[0]
        # check if the pet order is in the basket
        if basket.pets.filter(pet__slug=pet.slug).exists():
            pet_order = PetOrder.objects.filter(
                pet=pet,
                user=request.user,
                ordered=False
            )[0]
            if pet_order.quantity > 0:
                pet_order.quantity += 1
                pet_order.save()
            else:
                basket.pets.add(pet_order)
            messages.info(request, "This pet quantity was updated.")
            return redirect("exotic_bay:basket")
        else:
            messages.info(request, "This pet was not in your basket")
            return redirect("exotic_bay:pet_details", type=pet.type, slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("exotic_bay:pet_details", type=pet.type, slug=slug)


@login_required
def add_to_watchlist(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    watchlist_qs = Watchlist.objects.filter(user=request.user)
    if watchlist_qs.exists():
        watchlist = watchlist_qs[0]
        # check if the pet order is in the basket
        if watchlist.pets.filter(slug=pet.slug).exists():
            messages.info(request, "This pet is already in your watchlist.")
            return redirect("exotic_bay:watchlist")
        else:
            watchlist.pets.add(pet)
            messages.info(request, "This pet was added to your watchlist.")
            return redirect("exotic_bay:watchlist")
    else:
        watchlist = Watchlist.objects.create(
            user=request.user)
        watchlist.pets.add(pet)
        messages.info(request, "This pet was added to your watchlist.")
        return redirect("exotic_bay:watchlist")
    return redirect('exotic_bay:watchlist')


@login_required
def remove_from_watchlist(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    watchlist_qs = Watchlist.objects.filter(user=request.user)
    if watchlist_qs.exists():
        watchlist = watchlist_qs[0]
        # check if the pet order is in the basket
        if watchlist.pets.filter(slug=pet.slug).exists():
            watchlist.pets.remove(pet)
            messages.info(request, "This pet was removed from your watchlist.")
            return redirect("exotic_bay:watchlist")
        else:
            messages.info(request, "This pet was not in your watchlist.")
            return redirect("exotic_bay:pet_details", type=pet.type, slug=slug)
    else:
        messages.info(request, "You do not have an active watchlist.")
        return redirect("exotic_bay:pet_details", type=pet.type, slug=slug)
