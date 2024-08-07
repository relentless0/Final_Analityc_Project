import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import duckdb
from etl import get_data
import dash_bootstrap_components as dbc
from connector import set_connection
import plotly.graph_objects as go
from dash import dash_table

tab1_df = get_data('get_df1')
tab2_df = get_data('get_df2')

tab1_dd_year = dcc.Dropdown(
    id='tab1_dd_year',
    options=[{'label':x, 'value':x} for x in range(2008, 2017)],
    value=2012,
    style={'color':'black'})

tab2_dd_year = dcc.Dropdown(
    id='tab2_dd_year',
    options=[{'label':x, 'value':x} for x in range(2008, 2017)],
    value=2012,
    style={'color':'black'})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    
    dbc.Row([        
        dbc.Col([
            html.H1('Sport Database Visualization', style={'color':'blue'}) 
        ], style={'marginLeft':'-1px'}, width={'size':'auto'}),
    ], className='app-header'),
    dbc.Row([
        html.Div(tab1_dd_year)
    ], style={'marginTop':'20px'}), 
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='firstg'
            )
        ])
    ]),
    dbc.Row([
        html.Div(tab2_dd_year)
    ], style={'marginTop':'20px'}), 
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='secondg'
            )
        ])
    ])
])
    
@app.callback(
    Output(component_id='firstg', component_property='figure'),
    Input(component_id='tab1_dd_year', component_property='value')
)


def creat_tab(year):
    year_df = tab1_df[tab1_df['year'] == year]
    gif = px.bar(
        data_frame=year_df, x='country', y='count'
    )
    return gif

@app.callback(
    Output(component_id='secondg', component_property='figure'),
    Input(component_id='tab2_dd_year', component_property='value')
)


def creat_tab2(year):
    year_df = tab2_df[tab2_df['year'] == year]
    gif = px.bar(
        data_frame=year_df, x='team', y='count'
    )
    return gif

if __name__ == '__main__':
    app.run_server()