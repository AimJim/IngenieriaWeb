from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render, loader, get_object_or_404

from .models import Car,Location, Transmission, Marca
from .forms import PersonalDetail


carValue = -1

def index(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas}
    return render(request, "index.html", context)

def car(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas}
    
    return render(request, 'car.html', context)

def about(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas}
    return render(request, "about.html", context)

def booking(request):

    if(request.method == "POST"):
        carSearch = request.POST['carSelect']
        print(carSearch)
    else:
        carSearch = '1'
    try:
        carSearch = int(carSearch)
    except:
        carSearch = 1
    
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas , 'selectedCar':carSearch}
    return render(request, "booking.html", context)

def contact(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'marcas': marcas}
    return render(request, "contact.html", context)

def detail(request):
    
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas}
    return render(request, "detail.html", context)

def service(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'marcas': marcas}
    return render(request, "service.html", context)

def team(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'marcas': marcas}
    return render(request, "team.html", context)

def testimonial(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    marcas = get_list_or_404(Marca.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'marcas': marcas}
    return render(request, "testimonial.html", context)

