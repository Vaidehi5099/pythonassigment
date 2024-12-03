import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset (adjust path as per your file location)
df = pd.read_csv(r"C:\Users\rushi\AppData\Local\Temp\1aefb953-e9a8-4d06-8c8e-d500158f2a17_Waste_Management_System_A_Comprehensive_Approach.zip.a17\vaidehipython\detaset\historical_emissions.csv")

# Preprocessing: melt the dataset to long format for easier plotting
df_melted = df.melt(id_vars=["Country", "Sector", "Gas"], var_name="Year", value_name="Emissions")

# Convert 'Year' to integer
df_melted["Year"] = pd.to_numeric(df_melted["Year"], errors='coerce')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the figures for the dashboard

# 1. Bar Chart: CO2 Emissions by Country and Sector for the latest year
latest_year = df_melted["Year"].max()
df_latest_year = df_melted[df_melted["Year"] == latest_year]
fig1 = px.bar(df_latest_year, x='Country', y='Emissions', color='Sector', 
              title=f"CO2 Emissions by Country and Sector in {latest_year}")

# 2. Line Chart: CO2 Emissions Over Time by Country
fig2 = px.line(df_melted, x='Year', y='Emissions', color='Country', title="CO2 Emissions Over Time by Country")

# Create the layout for the dashboard
app.layout = html.Div(children=[
    html.H1("CO2 Emissions Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for selecting a country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df_melted['Country'].unique()],
        value='USA',  # Default value
        style={'width': '48%', 'margin': '10px'}
    ),
    
    html.Div(children=[
        dcc.Graph(figure=fig1),
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    html.Div(children=[
        dcc.Graph(figure=fig2),
    ], style={'width': '48%', 'display': 'inline-block'}),
])

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
