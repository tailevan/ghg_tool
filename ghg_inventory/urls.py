from django.urls import path
from . import views

urlpatterns = [
    path('', views.scope1, name='ghg_input'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # scope 1 - refrigerant
    path('scope1/', views.scope1, name='scope1'),
    path('scope1/update/<int:pk>/', views.RefrigerantUpdateView.as_view(), name='refrigerant_update'),
    path('scope1/delete/<int:pk>/', views.RefrigerantDeleteView.as_view(), name='refrigerant_delete'),

    # scope 2 - electricity
    path('scope2/', views.scope2, name='scope2'),
    path('scope2/update/<int:pk>/', views.ElectricityUpdateView.as_view(), name='electricity_update'),
    path('scope2/delete/<int:pk>/', views.ElectricityDeleteView.as_view(), name='electricity_delete'),

    # scope 3 - commute
    path('scope3/', views.commute, name='scope3'),

    path('scope3/commute/', views.commute, name='commute'),
    path('scope3/commute/update/<int:pk>/', views.CommuteUpdateView.as_view(), name='commute_update'),
    path('scope3/commute/delete/<int:pk>/', views.CommuteDeleteView.as_view(), name='commute_delete'),
    
    # scope 3 - water
    path('scope3/water/', views.water, name='water'),
    path('scope3/water/update/<int:pk>/', views.WaterUpdateView.as_view(), name='water_update'),
    path('scope3/water/delete/<int:pk>/', views.WaterDeleteView.as_view(), name='water_delete'),
    # scope 3 - wastewater
    path('scope3/wastewater/', views.wastewater, name='wastewater'),
    path('scope3/wastewater/update/<int:pk>/', views.WastewaterUpdateView.as_view(), name='wastewater_update'),
    path('scope3/wastewater/delete/<int:pk>/', views.WastewaterDeleteView.as_view(), name='wastewater_delete'),


    # scope 3 - material
    path('scope3/material/', views.material, name='material'),
    path('scope3/material/update/<int:pk>/', views.MaterialUpdateView.as_view(), name='material_update'),
    path('scope3/material/delete/<int:pk>/', views.MaterialDeleteView.as_view(), name='material_delete'),


    # scope 3 - disposal
    path('scope3/disposal/', views.disposal, name='disposal'),
    path('scope3/disposal/update/<int:pk>/', views.DisposalUpdateView.as_view(), name='disposal_update'),
    path('scope3/disposal/delete/<int:pk>/', views.DisposalDeleteView.as_view(), name='disposal_delete'),

    # scope 3 - travel
    path('scope3/travel/', views.travel, name='travel'),
    path('scope3/travel/update/<int:pk>/', views.TravelUpdateView.as_view(), name='travel_update'),
    path('scope3/travel/delete/<int:pk>/', views.TravelDeleteView.as_view(), name='travel_delete'),

    # scope 3 - flight
    path('scope3/flight/', views.flight, name='flight'),
    path('scope3/flight/update/<int:pk>/', views.FlightUpdateView.as_view(), name='flight_update'),
    path('scope3/flight/delete/<int:pk>/', views.FlightDeleteView.as_view(), name='flight_delete'),
    
    # scope 3 - accommodation
    path('scope3/accommodation/', views.accommodation, name='accommodation'),
    path('scope3/accommodation/update/<int:pk>/', views.AccommodationUpdateView.as_view(), name='accommodation_update'),
    path('scope3/accommodation/delete/<int:pk>/', views.AccommodationDeleteView.as_view(), name='accommodation_delete'),
    
    # scope 3 - freighting
    path('scope3/freighting/', views.freighting, name='freighting'),
    path('scope3/freighting/update/<int:pk>/', views.FreightingUpdateView.as_view(), name='freighting_update'),
    path('scope3/freighting/delete/<int:pk>/', views.FreightingDeleteView.as_view(), name='freighting_delete'),

]
