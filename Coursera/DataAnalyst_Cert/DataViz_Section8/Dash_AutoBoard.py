import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update

app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the automobiles data into pandas dataframe
auto_data =  pd.read_csv('automobileEDA.csv', encoding = "ISO-8859-1")
print(auto_data.head(2))

#Layout Section of Dash
app.layout = html.Div(
    children=[
        html.H1('Car Automobile Components', style={'textAlign':'center', 'color':'#503D36', 'font-size':24}),
        # Next Div Level
        html.Div([
            # Inner Division for adding dropdown helper text 
            html.Div(
                html.H2('Drive Wheels Type : ', style={'margin-right':'2em'}) # don't see a need for a comma here
            ),
            # Inner Division
            dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label':'Rear Wheel Drive', 'value':'rwd'},
                    {'label':'Front Wheel Drive', 'value':'fwd'},
                    {'label':'Four Wheel Drive', 'value':'4wd'}
                ],
                value='rwd'
            ),
            html.Div([
                html.Div([], id='plot1'),
                html.Div([], id='plot2')
            ], style={'display':'flex'}) # another comma at the eol here in template and unsure if needed
        ])
    ]
)



# Place to add @app.callback Decorator
# The inputs and outputs of our application's interface are described declaratively as the arguments of @app.callback decorator.
# Dash - inputs/outputs of app are properties of a particular components
# In this example, our input is the value property of the component that has the ID demo-dropdown
# Our layout has 2 outputs so we need to create 2 output components.
# Here, the component property will be children as we have created empty division and passing in dcc.Graph (figure) after computation.
# TASK 3E
@app.callback(
    [
        Output(component_id='plot1', component_property='children'),
        Output(component_id='plot2', component_property='children')
    ],
    Input(component_id='demo-dropdown', component_property='value')
)
# Place to define the callback function .
# Whenever an input property changes, the function that the callback decorator wraps will get called automatically.
# TASK 3F
def display_selected_drive_charts(value):
    # Subset dataframe to selected drive wheels value from dropdown
    filtered_df = auto_data[auto_data['drive-wheels'] == value].groupby(['drive-wheels', 'body-style'], as_index=False)['price'].mean()
    filtered_df = filtered_df
    fig1 = px.pie(filtered_df, values='price', names='body-style', title='Pie Chart')
    fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')
    return [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ]


if __name__ == '__main__':
    app.run_server()