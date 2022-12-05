from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from .models import Location

class PersonalDetail(forms.Form):
    firtsName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    mobile = forms.IntegerField(max_value=1000000000)

class BookingDetail(forms.Form):
    pickLocation = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    dropLocation = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    pickUpDate = forms.DateField()
    pickUpTime = forms.TimeField()
    #Adultos y niños necesitamos?¿
    request = forms.CharField(max_length=512)


    
