from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, loader, get_object_or_404

from .models import Car,Location, Transmission, Marca,Categoria
from .forms import PersonalDetail
from django.core.mail import send_mail




def carRedirect(request, id):
    carBusc = id

    print(carBusc)
    context = {'carS' : carBusc}

    return render(request, 'carRedirect.html', context)

def index(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    categorias = get_list_or_404(Categoria.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas, 'categorias':categorias}
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
    formulario1 = PersonalDetail()

    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas , 'selectedCar':carSearch, 'form1': formulario1}
    return render(request, "booking.html", context)

def personalDetail(request):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    transmission = get_list_or_404(Transmission.objects.all())
    marcas = get_list_or_404(Marca.objects.all())
    formulario1 = PersonalDetail()

    context = {'localizaciones': localizaciones, 'coches': coches, 'transmision':transmission, 'marcas': marcas , 'selectedCar': 1, 'form1':formulario1}

    if(request.method == "POST"):
        print('1. if')
        form = PersonalDetail(request.POST)
        if(form.is_valid() or True):
            print('2. if')
            name = form.cleaned_data['firstName']
            
            lname = form.cleaned_data['lastName']

            email = form.changed_data['email']

            pickUpL = form.cleaned_data['pickLocation']

            dropL = form.cleaned_data['dropLocation']

            puD = form.changed_data['pickUpDate']

            puT = form.changed_data['pickUpTime']

            request = form.changed_data['request']
            print('me 3,14ca el culo')
            send_mail('indss booking', ''+name+lname+email+pickUpL+dropL+puD+puT+request, 'eneko.hernando@gmail.com', ['aimar.jimenez@opendeusto.es'], fail_silently=False, )    
            return HttpResponseRedirect("index")
        else:
            PersonalDetail()
            return render(request, "booking.html", context)
    else: 
        PersonalDetail()
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

def marcas(request, id):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    marcas = get_list_or_404(Marca.objects.all())
    transmission = get_list_or_404(Transmission.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'marcas': marcas, 'transmision':transmission, 'selectedMarca' : id}
    return render(request, "marcas.html", context)

def categorias(request, id):
    localizaciones = get_list_or_404(Location.objects.order_by('nombre'))
    coches = get_list_or_404(Car.objects.order_by('nombre'))
    marcas = get_list_or_404(Marca.objects.all())
    transmission = get_list_or_404(Transmission.objects.all())
    categorias = get_list_or_404(Categoria.objects.all())
    context = {'localizaciones': localizaciones, 'coches': coches, 'marcas': marcas, 'transmision':transmission, 'categorias':categorias, 'selectedTran':id}
    return render(request, "categorias.html", context)

