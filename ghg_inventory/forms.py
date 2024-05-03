from django import forms
from .models import Inventory_Year, Refrigerant, Electricity, Commute, Water, Wastewater, Material, Disposal, Travel, Flight, Accommodation, Freighting
from django.utils import timezone

class Inventory_Year_Form(forms.ModelForm):
    class Meta:
        model = Inventory_Year 
        fields = '__all__'

class Refrigerant_Form(forms.ModelForm):
    class Meta:
        model = Refrigerant
        fields = ['inventory_year', 'type', 'quantity', 'capacity']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields.pop('emission')

class Electricity_Form(forms.ModelForm):
    class Meta:
        model = Electricity
        fields = ['inventory_year', 'consumption', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }


class Commute_Form(forms.ModelForm):
    class Meta:
        model = Commute
        fields = ['inventory_year', 'employee', 'distance', 'workdays']


class Water_Form(forms.ModelForm):
    class Meta:
        model = Water
        fields = ['inventory_year', 'consumption', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }

class Wastewater_Form(forms.ModelForm):
    class Meta:
        model = Wastewater
        fields = ['inventory_year', 'consumption', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }

class Material_Form(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['inventory_year', 'type', 'quantity'] 

class Disposal_Form(forms.ModelForm):
    class Meta:
        model = Disposal
        fields = ['inventory_year', 'type', 'quantity']

class Travel_Form(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['inventory_year', 'type', 'distance', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }

class Flight_Form(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['inventory_year', 'type','distance','passenger', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }

class Accommodation_Form(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['inventory_year', 'country',  'night', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }

class Freighting_Form(forms.ModelForm):
    class Meta:
        model = Freighting
        fields = ['inventory_year', 'vehicle', 'agent', 'distance', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }