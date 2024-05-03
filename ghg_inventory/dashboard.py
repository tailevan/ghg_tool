import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc, html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import plotly.graph_objs as go
import pandas as pd

# app = DjangoDash('dashboard')  
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css']

app = DjangoDash('dashboard', external_stylesheets=external_stylesheets)

def create_dashboard(years, refrigerants_df, electricities_df, commutes_df, waters_df, wastewaters_df, materials_df, disposals_df, travels_df, flights_df, accommodations_df, freightings_df, scope3_emission_df):

    scope1_emission = refrigerants_df.groupby('inventory_year__year')['emission'].sum()
    scope2_emission = electricities_df.groupby('inventory_year__year')['emission'].sum()
    scope3_emission = scope3_emission_df['emission']

    # scope1_df = refrigerants_df
    # scope2_df = electricities_df
    # scope3_df = scope3_emission_df

    series_list = [scope1_emission, scope2_emission, scope3_emission]
    total_emission = series_list[0]

    for series in series_list[1:]:
        total_emission = total_emission.add(series, fill_value=0)
    total_emission_df = pd.DataFrame({
        'year': total_emission.index,
        'emission': total_emission.values
    })
    dropdown_year = dcc.Dropdown(
        id='dropdown-year',
        options=[{'label': year, 'value': year} for year in years],
        value = years[0]
    )
    



    gauge_chart = dcc.Graph(
        id='gauge_chart',
        figure=go.Figure(),
        style={'width': '400px', 'height': '300px'}
    )

    treemap_figure = dcc.Graph(
        id='treemap_figure',
        figure=go.Figure(
            go.Treemap(
                labels=['Scope 1', 'Scope 2', 'Scope 3'],
                parents=['', '', ''],
                values=[50, 100, 150],
                textinfo='label+value',
                marker=dict(
                    colors=['#1f77b4', '#ff7f0e', '#2ca02c'],
                    line=dict(width=2)
                )
            )
        ),
        style={'width': '900px', 'height': '800px'}
    )


    group_bar_chart = dcc.Graph(
        id='bar-chart',
        figure=go.Figure(
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
                    # y=commutes_df.groupby('inventory_year__year')['emission'].sum(),
                    y = scope3_emission_df['emission'],
                    name='Scope 3'
                ),
                # go.Line(
                #     x = list(years),
                #     y = total_emission_df['emission'] ,
                #     name='Total Emission'
                # ),
                go.Scatter(
                    x = list(years),
                    y = total_emission_df['emission'],
                    mode = 'lines+markers',
                    name='Total Emission'
                ),
            ],
            layout=go.Layout(
                title='Scope of Emission by Year',
                xaxis={'title': 'Year'},
                yaxis={'title': 'Emission'}
            )
        )
    )
    @app.callback(
        [Output('gauge-chart', 'figure'),Output('treemap', 'figure')],
        [Input('dropdown-year', 'value')]
    )
    def update_charts(selected_year):
        refrigerant_emission = refrigerants_df[refrigerants_df['inventory_year__year'] == selected_year]['emission'].sum()
        electricity_emission = electricities_df[electricities_df['inventory_year__year'] == selected_year]['emission'].sum()
        commute_emission = commutes_df[commutes_df['inventory_year__year'] == selected_year]['emission'].sum()
        water_emission = waters_df[waters_df['inventory_year__year'] == selected_year]['emission'].sum()
        wastewater_emission = wastewaters_df[wastewaters_df['inventory_year__year'] == selected_year]['emission'].sum()
        material_emission = materials_df[materials_df['inventory_year__year'] == selected_year]['emission'].sum()
        disposal_emission = disposals_df[disposals_df['inventory_year__year'] == selected_year]['emission'].sum()
        travel_emission = travels_df[travels_df['inventory_year__year'] == selected_year]['emission'].sum()
        flight_emission = flights_df[flights_df['inventory_year__year'] == selected_year]['emission'].sum()
        accommodation_emission = accommodations_df[accommodations_df['inventory_year__year'] == selected_year]['emission'].sum()
        freighting_emission = freightings_df[freightings_df['inventory_year__year'] == selected_year]['emission'].sum()


        # total_emission = filtered['emission'].sum()
        total_emission = refrigerant_emission + electricity_emission + commute_emission + water_emission + wastewater_emission + material_emission + disposal_emission + travel_emission + flight_emission + accommodation_emission + freighting_emission
        # Create gauge chart figure
        gauge_chart_figure = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=total_emission,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': 'Total Emission (tonne of CO2e)'}
            )
        )

        scope1_emission = refrigerants_df[refrigerants_df['inventory_year__year'] == selected_year]['emission'].sum()
        scope2_emission = electricities_df[electricities_df['inventory_year__year'] == selected_year]['emission'].sum()
        scope3_emission = commute_emission + water_emission + wastewater_emission + material_emission + disposal_emission + travel_emission + flight_emission + accommodation_emission + freighting_emission

        labels = ["Scope 1", "Scope 2", "Scope 3", "Commute", "Water", "Wastewater", "Material", "Disposal", "Travel", "Flight", "Accommodation", "Freighting"]
        parents = ["", "", "", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3"]
        values = [scope1_emission, scope2_emission, scope3_emission, commute_emission, water_emission, wastewater_emission, material_emission, disposal_emission, travel_emission, flight_emission, accommodation_emission, freighting_emission]

        treemap_figure = go.Figure(
            go.Treemap(
                labels=labels,
                parents=parents,
                values=values,
                textinfo='label+value',
                marker=dict(
                    colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e'],
                    line=dict(width=2)
                ),
                branchvalues='total'
            )
        )
        


        return gauge_chart_figure, treemap_figure


# Layout of the dashboard
    app.layout = html.Div([
        html.Div([
            html.Label('Select Year'),
            dropdown_year,
        ]),
        gauge_chart,
        group_bar_chart,
        treemap_figure,
    ], style={'height': '100vh'})    
    return app
