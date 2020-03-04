from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from exotic_bay.forms import UserForm


def home(request):
    context_dict = {}

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/home.html', context=context_dict)

    # Render the response and send it back.
    return response


def contact_us(request):
    context_dict = {}

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'exotic_bay/contact_us.html', context=context_dict)

    # Render the response and send it back.
    return response


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


