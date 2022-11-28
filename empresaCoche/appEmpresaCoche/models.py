from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

class Car(models.Model):
    nombre= models.CharField(max_length=100)
    km=models.IntegerField()
    anyoF=models.IntegerField()
    potencia=models.IntegerField()
    img_url=models.CharField(max_length=512)
    precio=models.IntegerField()
    

    def __str__(self) -> str:
        return self.nombre
class Location(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre



# Create your models here.
