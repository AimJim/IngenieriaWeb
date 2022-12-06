from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    img_url = models.CharField(max_length=512)
    descripcion = models.CharField(max_length=1024)
    def __str__(self) -> str:
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    img_url = models.CharField(max_length=512)
    descripcion = models.CharField(max_length=1024)
    def __str__(self) -> str:
        return self.nombre


class Car(models.Model):
    nombre= models.CharField(max_length=100)
    km=models.IntegerField()
    anyoF=models.IntegerField()
    potencia=models.IntegerField()
    img_url=models.CharField(max_length=512)
    precio=models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    
    


    def __str__(self) -> str:
        return self.nombre


class Transmission(models.Model):
    carID = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    transmissionIDs = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.carID.__str__() + " - " + self.transmissionIDs.__str__()

class Location(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre




