from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from exotic_bay.forms import UserForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from exotic_bay.models import Pet


def home(request):
    context_dict = {}

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


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_passsword(user.password)
            user.save()

            profile.user = user

            profile.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'exotic_bay/register.html', context={'user_form': user_form, 'registered': registered})


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

    response = render(request, 'exotic_bay/basket.html', context= context_dict)

    return response
