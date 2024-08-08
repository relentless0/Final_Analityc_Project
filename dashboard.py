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
tab3_df = get_data('get_df3')


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

tab3_dd_team = dcc.Dropdown(
    id='tab3_dd_team',
    options=[{'label':x, 'value':x} for x in tab3_df['team']],
    value='FC Barcelona',
    style={'color':'black'})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(style={"margin":"25px"}, children=[
    
    dbc.Row([        
        dbc.Col([
            html.H1('Sport Database Visualization', style={'color':'white'}),
            html.H3('(2008-2016)', style={'marginLeft':'200px'}) 
        ], style={'marginLeft':'300px'}, width={'size':'auto'}),
    ], className='app-header'),
    dbc.Row([
        html.H4('Year:'),
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
        html.H4('Year:'),
        html.Div(tab2_dd_year)
    ], style={'marginTop':'20px'}), 
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='secondg'
            )
        ])
    ]),
    dbc.Row([
        html.H4('Team:'),
        html.Div(tab3_dd_team)
    ], style={'marginTop':'20px'}), 
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='thirdg'
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
        data_frame=year_df, x='country', y='count',
        template='plotly_dark'
    )
    return gif

@app.callback(
    Output(component_id='secondg', component_property='figure'),
    Input(component_id='tab2_dd_year', component_property='value')
)


def creat_tab2(year):
    year_df = tab2_df[tab2_df['year'] == year]
    gif = px.line(
        data_frame=year_df, x='team', y='count',
        template='plotly_dark'
    )
    return gif

@app.callback(
    Output(component_id='thirdg', component_property='figure'),
    Input(component_id='tab3_dd_team', component_property='value')
)


def creat_tab3(team):
    team_df = tab3_df[tab3_df['team'] == team]
    gif = px.bar(
        data_frame=team_df, x='year', y='count',
        template='plotly_dark'
    )
    return gif

if __name__ == '__main__':
    app.run_server()