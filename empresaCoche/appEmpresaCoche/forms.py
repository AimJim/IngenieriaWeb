from django import forms
from django.core.exceptions import ValidationError

class SearchCar(forms.Form):
    carSelect = forms.IntegerField(required=True)

    def clean_select(self):
        data = self.cleaned_data['carSelect']

        return data

    
