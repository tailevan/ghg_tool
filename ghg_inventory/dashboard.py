import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc, html
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from django.db.models import Sum



# app = DjangoDash('dashboard')  
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css']
app = DjangoDash('dashboard', external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div([
        html.Label('Select Year'),
        dcc.Dropdown(id='dropdown_year', value='2024'),
        html.Label('Total Emission (tonne of CO2e)'),
        dcc.Graph(id='gauge_chart'),
        
    ]),
    dcc.Graph(id='group_bar_chart'),
    dcc.Graph(id='treemap_chart'),
], style={'height': '100vh'})
# Layout of the dashboard


# Callback to populate the dropdown
@app.callback(
    Output('dropdown_year', 'options'),
    [Input('dropdown_year', 'value')]
)
def update_dropdown(selected_year):
    # Query the database for the years
    from .models import Inventory_Year
    years = Inventory_Year.objects.values_list('year', flat=True)
    # Create the dropdown options
    options = [{'label': year, 'value': year} for year in years]
    return options



@app.callback(
    Output('gauge_chart', 'figure'),
    [Input('dropdown_year', 'value')]
)
def update_gauge_chart(selected_year):
    # Query the database for the emissions
    
    from .models import Refrigerant, Electricity, Commute, Water, Wastewater, Material, Disposal, Travel, Flight, Accommodation, Freighting
    
    refrigerant_emission = Refrigerant.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    electricity_emission = Electricity.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    commute_emission = Commute.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    water_emission = Water.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    
    wastewater_emission = Wastewater.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    material_emission = Material.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    disposal_emission = Disposal.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    travel_emission = Travel.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    flight_emission = Flight.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    accommodation_emission = Accommodation.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0
    freighting_emission = Freighting.objects.filter(inventory_year__year=selected_year).aggregate(total_emission=Sum('emission'))['total_emission'] or 0.0

    total_emission = refrigerant_emission + electricity_emission + commute_emission + water_emission + wastewater_emission + material_emission + disposal_emission + travel_emission + flight_emission + accommodation_emission + freighting_emission
    
    
    gauge_chart = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=total_emission,
        )
    )
    return gauge_chart


# Group bar chart
@app.callback(    
    Output('group_bar_chart', 'figure'),
    [Input('dropdown_year', 'value')]
)
def update_group_bar_chart(selected_year):

    from .models import Inventory_Year, Refrigerant, Electricity, Commute, Water, Wastewater, Material, Disposal, Travel, Flight, Accommodation, Freighting

    
    refrigerants_df = pd.DataFrame(list(Refrigerant.objects.values('inventory_year__year', 'emission')))
    electricities_df = pd.DataFrame(list(Electricity.objects.values('inventory_year__year', 'emission')))
    commutes_df = pd.DataFrame(list(Commute.objects.values('inventory_year__year', 'emission')))
    waters_df = pd.DataFrame(list(Water.objects.values('inventory_year__year', 'emission')))
    wastewaters_df = pd.DataFrame(list(Wastewater.objects.values('inventory_year__year', 'emission')))
    materials_df = pd.DataFrame(list(Material.objects.values('inventory_year__year', 'emission')))
    disposals_df = pd.DataFrame(list(Disposal.objects.values('inventory_year__year', 'emission')))
    travels_df = pd.DataFrame(list(Travel.objects.values('inventory_year__year', 'emission')))
    flights_df = pd.DataFrame(list(Flight.objects.values('inventory_year__year', 'emission')))
    accommodations_df = pd.DataFrame(list(Accommodation.objects.values('inventory_year__year', 'emission')))
    freightings_df = pd.DataFrame(list(Freighting.objects.values('inventory_year__year', 'emission')))

    scope3_df = pd.concat([commutes_df, waters_df, wastewaters_df, materials_df, disposals_df, travels_df, flights_df, accommodations_df, freightings_df])

    total_emission = pd.concat([refrigerants_df, electricities_df, scope3_df])
    years = Inventory_Year.objects.values_list('year', flat=True)
    
    group_bar_chart = go.Figure(
        data=[
            go.Bar(
                x=list(years),
                y=refrigerants_df.groupby('inventory_year__year')['emission'].sum(),
                name='Scope 1'
            ),
            go.Bar(
                x=list(years),
                y=electricities_df.groupby('inventory_year__year')['emission'].sum(),
                name='Scope 2'
            ),
            go.Bar(
                x=list(years),
                y=scope3_df.groupby('inventory_year__year')['emission'].sum(),
                name='Scope 3'
            ),
            go.Scatter(
                x=list(years),
                y=total_emission.groupby('inventory_year__year')['emission'].sum(),
                name='Total Emission',
                mode='lines'
            ),
        ],
        layout=go.Layout(
            title='Scope of Emission by Year',
            xaxis={'title': 'Year'},
            yaxis={'title': 'Emission'}
        ),
    )
    # print(refrigerants_df)
    return group_bar_chart



## Treemap chart

@app.callback(
    Output('treemap_chart', 'figure'),
    [Input('dropdown_year', 'value')]
)
def update_treemap_chart(selected_year):
    
    from .models import Inventory_Year, Refrigerant, Electricity, Commute, Water, Wastewater, Material, Disposal, Travel, Flight, Accommodation, Freighting

    
    scope1_df = pd.DataFrame(list(Refrigerant.objects.values('inventory_year__year', 'emission')))
    scope2_df= pd.DataFrame(list(Electricity.objects.values('inventory_year__year', 'emission')))

    commutes_df = pd.DataFrame(list(Commute.objects.values('inventory_year__year', 'emission')))
    waters_df = pd.DataFrame(list(Water.objects.values('inventory_year__year', 'emission')))
    wastewaters_df = pd.DataFrame(list(Wastewater.objects.values('inventory_year__year', 'emission')))
    materials_df = pd.DataFrame(list(Material.objects.values('inventory_year__year', 'emission')))
    disposals_df = pd.DataFrame(list(Disposal.objects.values('inventory_year__year', 'emission')))
    travels_df = pd.DataFrame(list(Travel.objects.values('inventory_year__year', 'emission')))
    flights_df = pd.DataFrame(list(Flight.objects.values('inventory_year__year', 'emission')))
    accommodations_df = pd.DataFrame(list(Accommodation.objects.values('inventory_year__year', 'emission')))
    freightings_df = pd.DataFrame(list(Freighting.objects.values('inventory_year__year', 'emission')))

    scope3_df = pd.concat([commutes_df, waters_df, wastewaters_df, materials_df, disposals_df, travels_df, flights_df, accommodations_df, freightings_df])

    
    # Calculate the total emission for each scope
    scope1_emission = scope1_df.groupby('inventory_year__year')['emission'].sum()
    scope2_emission = scope2_df.groupby('inventory_year__year')['emission'].sum()
    scope3_emission = scope3_df.groupby('inventory_year__year')['emission'].sum()

    # Create a dictionary to store the components of scope 3
    scope3_components = {
        'Commutes': commutes_df.groupby('inventory_year__year')['emission'].sum(),
        'Waters': waters_df.groupby('inventory_year__year')['emission'].sum(),
        'Wastewaters': wastewaters_df.groupby('inventory_year__year')['emission'].sum(),
        'Materials': materials_df.groupby('inventory_year__year')['emission'].sum(),
        'Disposals': disposals_df.groupby('inventory_year__year')['emission'].sum(),
        'Travels': travels_df.groupby('inventory_year__year')['emission'].sum(),
        'Flights': flights_df.groupby('inventory_year__year')['emission'].sum(),
        'Accommodations': accommodations_df.groupby('inventory_year__year')['emission'].sum(),
        'Freightings': freightings_df.groupby('inventory_year__year')['emission'].sum(),

        # Add more components here
    }

    # Create the treemap chart
    treemap_chart = go.Figure(
        go.Treemap(
            labels=['Scope 1', 'Scope 2', 'Scope 3'],
            parents=['', '', ''],
            values=[scope1_emission[selected_year], scope2_emission[selected_year], scope3_emission[selected_year]],
            textinfo='label+value',
            hovertemplate='Scope: %{label}<br>Total Emission: %{value}<extra></extra>',
            branchvalues='total',
            marker=dict(
                colors=['#1f77b4', '#ff7f0e', '#2ca02c'],
                line=dict(width=2)
            )
        )
    )

    # # # Add the components of scope 3 to the treemap chart
    # for component, emission in scope3_components.items():
    #     treemap_chart.add_trace(
    #         go.Treemap(
    #             labels=[component],
    #             parents=['Scope 3'],
    #             values=[emission[selected_year]],
    #             textinfo='label+value',
    #             hovertemplate='Component: %{label}<br>Emission: %{value}<extra></extra>',
    #             branchvalues='total',
    #             marker=dict(
    #                 colors=['#d62728'],
    #                 line=dict(width=2)
    #             )
    #         )
    #     )
    # # print(scope3_components)
    return treemap_chart