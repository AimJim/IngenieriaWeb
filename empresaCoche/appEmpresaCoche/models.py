from django.db import models
class Car(models.Model):
    nombre= models.CharField(max_length=100)
    km=models.IntegerField()
    anyoF=models.IntegerField()
    potencia=models.IntegerField()
    img_url=models.URLField(max_length=512)

    def __str__(self) -> str:
        return self.nombre
class Location(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

# Create your models here.
