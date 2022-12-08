from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from .models import Location

class PersonalDetail(forms.Form):
    firstName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control p-4'}))
    lastName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control p-4'}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control p-4'}))
    mobile = forms.IntegerField(max_value=1000000000, widget=forms.NumberInput(attrs={'class': 'form-control p-4'}))
    pickLocation = forms.ModelChoiceField(queryset=Location.objects.all(),widget=forms.Select(attrs={'class': 'form-control px-4'}))
    dropLocation = forms.ModelChoiceField(queryset=Location.objects.all(),widget=forms.Select(attrs={'class': 'form-control px-4'}))
    pickUpDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control px-4'}))
    pickUpTime = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control px-4'}))
    request = forms.CharField(max_length=512, widget=forms.TextInput(attrs={'class': 'form-control px-4'}))
    