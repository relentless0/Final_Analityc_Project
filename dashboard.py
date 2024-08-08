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
            html.H1('Football Database Visualization', style={'color':'white'}),
            html.H3('(2008-2016)', style={'marginLeft':'200px'}) 
        ], style={'marginLeft':'300px'}, width={'size':'auto'}),
    ], className='app-header'),
    dbc.Row([
        html.H4('Choose Year:'),
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
        html.H4('Choose Year:'),
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
        html.H4('Choose Team:'),
        html.Div(tab3_dd_team)
    ], style={'marginTop':'20px'}), 
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='thirdg'
            )
        ])
    ]),
    dbc.Row([
        html.H3('All Played Football Matches by Year:'),
        dbc.Col([
            dcc.Graph(
                id='fourthg'
            )
        ])
    ], style={'marginTop': '20px'})
])
    
@app.callback(
    Output(component_id='firstg', component_property='figure'),
    Input(component_id='tab1_dd_year', component_property='value')
)


def creat_tab(year):
    year_df = tab1_df[tab1_df['year'] == year]
    gif = px.bar(
        data_frame=year_df, x='country', y='count', title='Number of football matches played by contries by year:',
        template='plotly_dark'
    )
    gif.update_layout(
        title={
            'text': 'Number of football matches played by contries by year:',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 22}  
        },
        xaxis_title='Countries',
        yaxis_title='Number of Matches',
        xaxis_title_font=dict(size=18),  
        yaxis_title_font=dict(size=18)   
    )

    return gif

@app.callback(
    Output(component_id='secondg', component_property='figure'),
    Input(component_id='tab2_dd_year', component_property='value')
)


def creat_tab2(year):
    year_df = tab2_df[tab2_df['year'] == year]
    gif = px.line(
        data_frame=year_df, x='team', y='count', title='Number of matches played by football teams by year',
        template='plotly_dark'
    )
    gif.update_layout(
        title={
            'text': 'Number of matches played by football teams by year:',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 22}  
        },
        xaxis_title='Football Teams',
        yaxis_title='Number of Matches',
        xaxis_title_font=dict(size=18),  
        yaxis_title_font=dict(size=18)  
        )
    return gif

@app.callback(
    [Output(component_id='thirdg', component_property='figure'),
    Output(component_id='fourthg', component_property='figure')],
    Input(component_id='tab3_dd_team', component_property='value')
)


def creat_tabs3(team):
    team_df = tab3_df[tab3_df['team'] == team]
    thirdg_figure = px.bar(
        data_frame=team_df, x='year', y='count', title='Number of matches played by year of each football team',
        template='plotly_dark'
    )
    thirdg_figure.update_layout(
        title={
            'text': 'Number of matches played by year of each football team:',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 22}  
        },
        xaxis_title='Years',
        yaxis_title='Number of Matches',
        xaxis_title_font=dict(size=18),  
        yaxis_title_font=dict(size=18)  
        )

    all_data = tab3_df.groupby('year').agg({'count': 'sum'}).reset_index()
    fourthg_figure = px.bar(
        data_frame=all_data, x='year', y='count',
        template='plotly_dark'
    )
    fourthg_figure.update_layout(
        xaxis_title='Years',
        yaxis_title='Number of Matches',
        xaxis_title_font=dict(size=18),  
        yaxis_title_font=dict(size=18)
    )

    return thirdg_figure, fourthg_figure

if __name__ == '__main__':
    app.run_server()