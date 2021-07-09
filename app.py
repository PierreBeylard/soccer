
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import db
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

from dash.dependencies import Input, Output

import plotly.io as pio

from whitenoise import WhiteNoise

server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="static/") #Pour pouvoir accéder au fichier statics/assets/style.css sinon ça marche pas

# génération des df, et des figures

df_total_goal_by_rainfall = db.get_total_goals_by_rainfall() #1
df_total_goal_by_temperature = db.get_total_goals_by_temperature() #2

df_mean_goal_by_rainfall = db.get_mean_goals_by_rainfall() #1
df_mean_goal_by_temperature = db.get_mean_goals_by_temperature() #2


df_total_teams_goal_by_rainfall = db.get_total_teams_goals_by_rainfall()#3
df_total_teams_goal_by_temperature = db.get_total_teams_goals_by_temperature()#4

df_mean_teams_goal_by_rainfall = db.get_mean_teams_goals_by_rainfall()#3
df_mean_teams_goal_by_temperature = db.get_mean_teams_goals_by_temperature()#4




fig_total_goal_by_rainfall = px.bar(df_total_goal_by_rainfall, x="rainfall", y="total_goal",template="plotly_dark") #1

fig_total_goal_by_temperature = px.bar(df_total_goal_by_temperature, x="temperature", y="total_goal",template="plotly_dark") #2

fig_total_teams_goal_by_rainfall = px.scatter(df_total_teams_goal_by_rainfall, x="rainfall", y="total_goals", color="name",template="plotly_dark")#3

fig_total_teams_goal_by_temperature = px.scatter(df_total_teams_goal_by_temperature, x="temperature", y="total_goals", color="name",template="plotly_dark"  )#4


#-----------------------------------------------------------------------------------------------------------------------------------------------------------#


#Création du layout

app.layout = html.Div(children=[
    html.H1(children='Temperature and rainfall influence over goals in football matches',style = {'color':'#ebeaed',  'margin': '0px 0px 0px 300px '}),

    html.H2(children='''
Global Viz''',style={'color':'#cfcbce',  'margin': '50px 0px 15px 815px '}),
    html.Div(
    dbc.Row([
    
        dbc.Col([
            dcc.Dropdown(
                id='dropdown_rainfall',
                options=[
                    {'label': 'Total', 'value': 'Total'},
                    {'label': 'Mean', 'value': 'Mean'},               
                    ],
                value = 'Total',
                ),

            dcc.Graph(
                id='total_goals_by_rainfall',
                figure=fig_total_goal_by_rainfall
            )  #1     
              
            
        ]), 
    
        dbc.Col([
            dcc.Dropdown(
                id='dropdown_temperature',
                options=[
                    {'label': 'Total', 'value': 'Total'},
                    {'label': 'Mean', 'value': 'Mean'},                   
                    ],
                value = 'Total',
                ),

            dcc.Graph(
            id='total_goals_by_temperature',
            figure=fig_total_goal_by_temperature
            )  #2

            
         
        ]) 
        
    ])
    ),
    
    html.H2(children='''By teams Viz''',style={'color':'#cfcbce',  'margin': '50px 0px 15px 815px '}),

    html.Div(
    dbc.Row([
    
        dbc.Col([

             dcc.Dropdown(
                id='dropdown_rainfall2',
                options=[
                    {'label': 'Total', 'value': 'Total'},
                    {'label': 'Mean', 'value': 'Mean'},                   
                    ],
                value = 'Total',
                ),

            dcc.Graph(
            id='total_teams_goals_by_rainfall',
            figure=fig_total_teams_goal_by_rainfall 
            ),    #3
              
            
        ]), 
    
        dbc.Col([
            
            dcc.Dropdown(
                id='dropdown_temperature2',
                options=[
                    {'label': 'Total', 'value': 'Total'},
                    {'label': 'Mean', 'value': 'Mean'},                   
                    ],
                value = 'Total',
                ),

            dcc.Graph(
            id='total_teams_goals_by_temperature',
            figure=fig_total_teams_goal_by_temperature 
            ),       

        ])
    ])
    )

],style={"background-color":"#1d1c23"})


#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
#Callbacks 


# Graph 1 / Call Back 1

@app.callback(
    Output('total_goals_by_rainfall', 'figure'),
    Input('dropdown_rainfall', 'value'),
)
def update_graph(value):
    if value == "Mean":
        fig = px.bar(df_mean_goal_by_rainfall, x="rainfall", y="mean_goal",template="plotly_dark")

    else:
        fig = px.bar(df_total_goal_by_rainfall, x="rainfall", y="total_goal",template="plotly_dark")

    return fig

# Graph 2 / Call Back 2

@app.callback(
    Output('total_goals_by_temperature', 'figure'),
    Input('dropdown_temperature', 'value'),
)
def update_graph(value):
    if value == "Mean":
        fig = px.bar(df_mean_goal_by_temperature, x="temperature", y="mean_goal",template="plotly_dark")

    else:
        fig = px.bar(df_total_goal_by_temperature, x="temperature", y="total_goal",template="plotly_dark")

    return fig


# Graph 3 / Call Back 3

@app.callback(
    Output('total_teams_goals_by_rainfall', 'figure'),
    Input('dropdown_rainfall2', 'value'),
)
def update_graph(value):
    if value == "Mean":
        fig = px.scatter(df_mean_teams_goal_by_rainfall, x="rainfall", y="mean_goals", color='name',template="plotly_dark")

    else:
        fig = px.scatter(df_total_teams_goal_by_rainfall, x="rainfall", y="total_goals", color='name',template="plotly_dark")

    return fig

# Graph 4 / Call Back 4

@app.callback(
    Output('total_teams_goals_by_temperature', 'figure'),
    Input('dropdown_temperature2', 'value'),
)
def update_graph(value):
    if value == "Mean":
        fig = px.scatter(df_mean_teams_goal_by_temperature, x="temperature", y="mean_goals", color= 'name',template="plotly_dark")

    else:
        fig = px.scatter(df_total_teams_goal_by_temperature, x="temperature", y="total_goals", color= 'name',template="plotly_dark")

    return fig




if __name__ == '__main__':
    app.run_server(debug=True)