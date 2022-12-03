from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render, loader

from .models import Car,Location, Transmission
from .forms import SearchCar

carValue = -1

def index(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission}
    return render(request, "index.html", context)

def car(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission}

    return render(request, 'car.html', context)

def about(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission}
    return render(request, "about.html", context)

def booking(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission}
    return render(request, "booking.html", context)

def contact(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    context = {'localizaciones': localizaciones, 'coches': coches}
    return render(request, "contact.html", context)

def detail(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'selectedCar': carValue}
    return render(request, "detail.html", context)

def service(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    context = {'localizaciones': localizaciones, 'coches': coches}
    return render(request, "service.html", context)

def team(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    context = {'localizaciones': localizaciones, 'coches': coches}
    return render(request, "team.html", context)

def testimonial(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    context = {'localizaciones': localizaciones, 'coches': coches}
    return render(request, "testimonial.html", context)

