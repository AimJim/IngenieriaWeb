from django.urls import path
from . import views

#Meter todos los que vayamos a usar
urlpatterns = [
    path('', views.index, name='index'), 
]