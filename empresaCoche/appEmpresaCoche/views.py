from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, loader, get_object_or_404

from .models import Car,Location, Transmission, Marca,Categoria
from .forms import PersonalDetail





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
        
        form = PersonalDetail(request.POST)
        if(form.is_valid()):
            
            name = form.cleaned_data['firstName']
            if(name == ""):
                PersonalDetail()
                return render(request, 'booking.html', context)
            
            lname = form.cleaned_data['lastName']
            if(lname == ""):
                PersonalDetail()
                return render(request, 'booking.html', context)
            
            email = form.cleaned_data['email']
            if(email == ""):
                PersonalDetail()
                return render(request, 'booking.html', context)

            pickUpL = form.cleaned_data['pickLocation']
            if(pickUpL == 0):
                PersonalDetail()
                return render(request, 'booking.html', context)

            dropL = form.cleaned_data['dropLocation']
            if(dropL == 0):
                PersonalDetail()
                return render(request, 'booking.html', context)

            puD = form.cleaned_data['pickUpDate']
            if(puD == ""):
                PersonalDetail()
                return render(request, 'booking.html', context)

            puT = form.cleaned_data['pickUpTime']
            if(puT == ""):
                PersonalDetail()
                return render(request, 'booking.html', context)

            request = form.cleaned_data['request']
            if(request == ""):
                PersonalDetail()
                return render(request, 'booking.html', context)

            
            #El mail no se manda ya que windows bloquea los sockets.
            f= open('Data_from_form.txt','a')
            f.write('Nombre: ' + name + ' Apellido: ' + lname + ' Email: ' + email + ' Punto de recogida: ' + pickUpL.__str__() + ' Punto de devuelta: ' + 
            dropL.__str__() + ' Fecha de recogida: ' + puD + ' Horario de recogida: ' + puT + ' Peticiones especiales: ' + request + '\n')
            f.close()
            
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
