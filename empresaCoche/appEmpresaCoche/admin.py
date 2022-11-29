from django.contrib import admin
from .models import Car, Location, Categoria, Marca, Transmission
# Register your models here.

admin.site.register(Car)
admin.site.register(Location)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Transmission)
