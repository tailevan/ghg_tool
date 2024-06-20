from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import Inventory_Year_Form, Refrigerant_Form, Electricity_Form, Commute_Form, Water_Form, Wastewater_Form, Material_Form, Disposal_Form, Travel_Form, Flight_Form, Accommodation_Form, Freighting_Form
from .models import Inventory_Year, Refrigerant, Electricity, Commute, Water, Wastewater, Material, Disposal, Travel, Flight, Accommodation, Freighting
from .models import Refrigerant_EF, Electricity_EF, Material_EF, Disposal_EF, Travel_EF, Flight_EF, Freighting_EF
from .utils import calculate_emission_refrigerant, calculate_emission_electricity, calculate_emission_commute, calculate_emission_water, calculate_emission_wastewater, calculate_emission_material, calculate_emission_disposal, calculate_emission_travel, calculate_emission_flight, calculate_emission_accommodation, calculate_emission_freighting
# from .dashboard import create_dashboard
import pandas as pd
############################################################################### 
# Scope 1 - Refrigerant 

def scope1(request):
    if request.method == 'POST':
        refrigerant = Refrigerant_Form(request.POST, prefix='refrigerant')

        if refrigerant.is_valid():
            quantity = refrigerant.cleaned_data['quantity']
            capacity = refrigerant.cleaned_data['capacity']
            refrigerant_ef = Refrigerant_EF.objects.get(type=refrigerant.cleaned_data['type']).emission_factor
            emissions = calculate_emission_refrigerant(quantity, capacity, refrigerant_ef)
            
            refrigerant = refrigerant.save(commit=False)
            refrigerant.emission = emissions
            refrigerant.save()
            return redirect('scope1')
    refrigerant = Refrigerant_Form(prefix='refrigerant')
    refrigerants = Refrigerant.objects.all()
    context_refrigerant = {'refrigerant': refrigerant, 'refrigerants': refrigerants}
    return render(request, 'ghg_inventory/scope1.html', context_refrigerant)

class RefrigerantUpdateView(UpdateView):
    model = Refrigerant
    fields = ['inventory_year', 'type', 'quantity', 'capacity']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('scope1')

class RefrigerantDeleteView(DeleteView):
    model = Refrigerant
    success_url = reverse_lazy('scope1')



############################################################################### 
def scope2(request):
    if request.method == 'POST':
        electricity = Electricity_Form(request.POST, prefix='electricity')

        if electricity.is_valid(): 
            consumption = electricity.cleaned_data['consumption']
            electricity_ef = Electricity_EF.objects.get().emission_factor
            emissions = calculate_emission_electricity(consumption, electricity_ef)
            
            electricity = electricity.save(commit=False)
            electricity.emission = emissions
            electricity.save()
            return redirect('scope2')
    electricity = Electricity_Form(prefix='electricity')
    electricities = Electricity.objects.all()
    context_electricity = {'electricity': electricity, 'electricities': electricities}
    return render(request, 'ghg_inventory/scope2.html',context_electricity)

class ElectricityUpdateView(UpdateView):
    model = Electricity
    fields = ['inventory_year', 'consumption', 'date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('scope2')

class ElectricityDeleteView(DeleteView):
    model = Electricity
    success_url = reverse_lazy('scope2')

############################################################################### 
def scope3(request):   
    return render(request, 'ghg_inventory/scope3.html')

############################################################################### 
def commute(request):
    if request.method == 'POST':
        commute = Commute_Form(request.POST, prefix='commute')

        if commute.is_valid(): 
            distance = commute.cleaned_data['distance']
            workdays = commute.cleaned_data['workdays']
            emissions = calculate_emission_commute(distance, workdays)
            
            commute = commute.save(commit=False)
            commute.emission = emissions
            commute.save()
            return redirect('commute')
    commute = Commute_Form(prefix='commute')
    commutes = Commute.objects.all()
    context_commute = {'commute': commute, 'commutes': commutes}
    return render(request, 'ghg_inventory/scope3_commute.html', context_commute)

class CommuteUpdateView(UpdateView):
    model = Commute
    fields = ['inventory_year', 'employee', 'distance', 'workdays']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('commute')

class CommuteDeleteView(DeleteView):
    model = Commute
    success_url = reverse_lazy('commute')

############################################################################### 
def water(request):
    if request.method == 'POST':
        water = Water_Form(request.POST, prefix='water')

        if water.is_valid(): 
            consumption = water.cleaned_data['consumption']
            emissions = calculate_emission_water(consumption)

            water = water.save(commit=False)
            water.emission = emissions
            water.save()
            return redirect('water')
    water = Water_Form(prefix='water')
    waters = Water.objects.all()
    context_water = {'water': water, 'waters': waters}
    return render(request, 'ghg_inventory/scope3_water.html', context_water)

class WaterUpdateView(UpdateView):
    model = Water
    fields = ['inventory_year', 'consumption', 'date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('water')

class WaterDeleteView(DeleteView):
    model = Water
    success_url = reverse_lazy('water')

############################################################################### 
def wastewater(request):
    if request.method == 'POST':
        wastewater = Wastewater_Form(request.POST, prefix='wastewater')

        if wastewater.is_valid(): 
            consumption = wastewater.cleaned_data['consumption']
            emissions = calculate_emission_wastewater(consumption)

            wastewater = wastewater.save(commit=False)
            wastewater.emission = emissions
            wastewater.save()
            return redirect('wastewater')
        
    wastewater = Wastewater_Form(prefix='wastewater')
    wastewaters = Wastewater.objects.all()
    context_wastewater = {'wastewater': wastewater, 'wastewaters': wastewaters}
    return render(request, 'ghg_inventory/scope3_waste.html', context_wastewater)

class WastewaterUpdateView(UpdateView):
    model = Wastewater
    fields = ['inventory_year', 'consumption', 'date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('wastewater')

class WastewaterDeleteView(DeleteView):
    model = Wastewater 
    success_url = reverse_lazy('wastewater')

############################################################################### 
def material(request):
    if request.method == 'POST':
        material = Material_Form(request.POST, prefix='material')

        if material.is_valid():
            quantity = material.cleaned_data['quantity']
            material_ef = Material_EF.objects.get(type=material.cleaned_data['type']).emission_factor
            emissions = calculate_emission_material(quantity, material_ef)

            material = material.save(commit=False)
            material.emission = emissions
            
            material.save()
            return redirect('material')
    material = Material_Form(prefix='material')
    materials = Material.objects.all()
    context_material = {'material': material, 'materials': materials}
    return render(request, 'ghg_inventory/scope3_material.html', context_material)

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ['inventory_year', 'type', 'quantity']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('material')

class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('material')

############################################################################### 
def disposal(request):
    if request.method == 'POST':
        disposal = Disposal_Form(request.POST, prefix='disposal')

        if disposal.is_valid(): 
            quantity = disposal.cleaned_data['quantity']
            disposal_ef = Disposal_EF.objects.get(type=disposal.cleaned_data['type']).emission_factor
            emissions = calculate_emission_disposal(quantity, disposal_ef)

            disposal = disposal.save(commit=False)
            disposal.emission = emissions
            disposal.save()
            return redirect('disposal')
    disposal = Disposal_Form(prefix='disposal')
    disposals = Disposal.objects.all()
    context_disposal = {'disposal': disposal, 'disposals': disposals}
    return render(request, 'ghg_inventory/scope3_disposal.html', context_disposal)

class DisposalUpdateView(UpdateView):
    model = Disposal
    fields = ['inventory_year', 'type', 'quantity']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('disposal')

class DisposalDeleteView(DeleteView):
    model = Disposal
    success_url = reverse_lazy('disposal')

############################################################################### 
def travel(request):
    if request.method == 'POST':
        travel = Travel_Form(request.POST, prefix='travel')
    
        if travel.is_valid(): 
            distance = travel.cleaned_data['distance']
            travel_ef = Travel_EF.objects.get(type=travel.cleaned_data['type']).emission_factor
            emissions = calculate_emission_travel(distance, travel_ef)

            travel = travel.save(commit=False)
            travel.emission = emissions
            travel.save()
            return redirect('travel')
    travel = Travel_Form(prefix='travel')
    travels = Travel.objects.all()
    context_travel = {'travel': travel, 'travels': travels}
    return render(request, 'ghg_inventory/scope3_travel.html', context_travel)

class TravelUpdateView(UpdateView):
    model = Travel
    fields = ['inventory_year', 'type', 'distance']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('travel')

class TravelDeleteView(DeleteView):
    model = Travel
    success_url = reverse_lazy('travel')

############################################################################### 
def flight(request):
    if request.method == 'POST':
        flight = Flight_Form(request.POST, prefix='flight')

        if flight.is_valid(): 
            distance = flight.cleaned_data['distance']
            passenger = flight.cleaned_data['passenger']
            flight_ef = Flight_EF.objects.get(type=flight.cleaned_data['type']).emission_factor
            
            emissions = calculate_emission_flight(distance, passenger, flight_ef)
            flight = flight.save(commit=False)
            flight.emission = emissions
            flight.save()
            return redirect('flight')
    flight = Flight_Form(prefix='flight')
    flights = Flight.objects.all()
    context_flight = {'flight': flight, 'flights': flights}
    return render(request, 'ghg_inventory/scope3_flight.html', context_flight)

class FlightUpdateView(UpdateView):
    model = Flight
    fields = ['inventory_year', 'type', 'distance', 'passenger', 'date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('flight')

class FlightDeleteView(DeleteView):
    model = Flight
    success_url = reverse_lazy('flight')

############################################################################### 
def accommodation(request):
    if request.method == 'POST':
        accommodation = Accommodation_Form(request.POST, prefix='accommodation')

        if accommodation.is_valid(): 
            night = accommodation.cleaned_data['night']
            emissions = calculate_emission_accommodation(night)

            accommodation = accommodation.save(commit=False)
            accommodation.emission = emissions
            accommodation.save()
            return redirect('accommodation')
    accommodation = Accommodation_Form(prefix='accommodation')
    accommodations = Accommodation.objects.all()
    context_accommodation = {'accommodation': accommodation, 'accommodations': accommodations}
    return render(request, 'ghg_inventory/scope3_accommodation.html', context_accommodation)

class AccommodationUpdateView(UpdateView):
    model = Accommodation
    fields = ['inventory_year', 'country']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('accommodation')

class AccommodationDeleteView(DeleteView):
    model = Accommodation
    success_url = reverse_lazy('accommodation')


############################################################################### 
def freighting(request):
    if request.method == 'POST':
        freighting = Freighting_Form(request.POST, prefix='freighting')

        if freighting.is_valid(): 
            distance = freighting.cleaned_data['distance']
            freighting_ef = Freighting_EF.objects.get(vehicle=freighting.cleaned_data['vehicle']).emission_factor
            emissions = calculate_emission_freighting(distance, freighting_ef)

            freighting = freighting.save(commit=False)
            freighting.emission = emissions
            freighting.save()
            return redirect('freighting')
    freighting = Freighting_Form(prefix='freighting')
    freightings = Freighting.objects.all()
    context_freighting = {'freighting': freighting, 'freightings': freightings}
    return render(request, 'ghg_inventory/scope3_freighting.html', context_freighting)

class FreightingUpdateView(UpdateView):
    model = Freighting
    fields = ['inventory_year', 'vehicle', 'agent', 'distance', 'date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('freighting')

class FreightingDeleteView(DeleteView):
    model = Freighting
    success_url = reverse_lazy('freighting')


###############################################################################
# Dashboard
    
def dashboard(request):
    
    return render(request, 'ghg_inventory/dashboard.html')