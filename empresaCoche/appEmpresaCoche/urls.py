from django.urls import path
from . import views

#Meter todos los que vayamos a usar
urlpatterns = [
    path('', views.index, name='index'), 
    path('car', views.car, name='car'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('detail', views.detail, name='detail'),
    path('index', views.index, name='index'),
    path('service', views.service, name='service'),
    path('marcas/<int:id>', views.marcas, name='marcas'),
    path('categorias/<int:id>', views.categorias, name='categorias'),
    path('carRedirect/<int:id>', views.carRedirect, name='carRedirect'),
]