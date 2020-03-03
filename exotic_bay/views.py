from django.shortcuts import render
from django.http import HttpResponse


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
