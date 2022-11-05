#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:41:11 2022

@author: craigrupp
"""

# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Performance Dashboard', style={'textAlign':'center', 'color':'#503D36', 'font-size':30}),
                                html.Div(["Input Year", dcc.Input(id='input-year', value='2010', type='number', style={'height':'35px', 'font-size':20}),], 
                                style={'font-size':30}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])

# The core idea of this application is to get year as user input and update the dashboard in real-time. 
# We will be using callback function

# Callback decorator
@app.callback(Output(component_id='line-plot', component_property='figure'), 
        Input(component_id='input-year', component_property='value'))

# Add computation to callback function / return graph
def get_graph(entered_year):
    # Select Data based on the entered_year
    df_year = airline_data[airline_data['Year'] == int(entered_year)]

    # Groupby Month for Entered Year and Get Average Delay Time
    avg_dly = df_year.groupby('Month')['ArrDelay'].mean().reset_index()

    # Create Figure
    fig = go.Figure(data=go.Scatter(x=avg_dly['Month'], y=avg_dly['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='Average Delay')
    return fig 

# Run app 
if __name__ == '__main__':
    app.run_server() 