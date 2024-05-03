from django.contrib import admin
from .models import Inventory_Year, Refrigerant, Electricity, Commute, Water, Wastewater, Material, Disposal, Travel, Flight, Accommodation, Freighting
from .models import Refrigerant_EF, Electricity_EF, Material_EF, Disposal_EF, Travel_EF, Flight_EF, Freighting_EF

# input database
admin.site.register(Inventory_Year)
admin.site.register(Refrigerant)
admin.site.register(Electricity)
admin.site.register(Commute)
admin.site.register(Water)
admin.site.register(Wastewater)
admin.site.register(Material)
admin.site.register(Disposal)
admin.site.register(Travel)
admin.site.register(Flight)
admin.site.register(Accommodation)
admin.site.register(Freighting)


# emission database
admin.site.register(Refrigerant_EF)
admin.site.register(Electricity_EF)
admin.site.register(Material_EF)
admin.site.register(Disposal_EF)
admin.site.register(Travel_EF)
admin.site.register(Flight_EF)
admin.site.register(Freighting_EF)