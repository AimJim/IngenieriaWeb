from django import forms

class SearchCar(forms.Form):
    carSelect = forms.IntegerField(required=True)

    
