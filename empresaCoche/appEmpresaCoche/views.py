from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, loader

def index(request):
    return render(request, "index.html")

def car(request):
    return render(request, "car.html")

def about(request):
    return render(request, "about.html")

def booking(request):
    return render(request, "booking.html")

def contact(request):
    return render(request, "contact.html")

def detail(request):
    return render(request, "detail.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")
