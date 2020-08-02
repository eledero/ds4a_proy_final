############################################
#Por favor tener en cuenta:
##Se deben instalar en el ambiente los paquetes
###conda install psutil
###conda install -c plotly plotly-orca
##Sin embargoo no es necesario importarlos en los .py
############################################


#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

#Dash Bootstrap Components
import dash_bootstrap_components as dbc 

#Data 
import math
import numpy as np
import datetime as dt
import pandas as pd
import json
import base64
import io
import dash_table

#Recall app
from app import app



###########################################################
#
#           APP LAYOUT:
#
###########################################################

#LOAD THE DIFFERENT FILES
from lib import title, pictures, upload

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [ 
      pictures.DS4A_Img,
      pictures.Line_Img,
      title.title_backgroung,
      title.title_text,
      title.texto1,
      title.texto2,
      title.texto3,
      title.texto4,
      title.texto5,
      upload.upload
    ]
)

 
    
###############################################   
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
#Load and modify the data that will be used in the app.
#################################################################




#############################################################
# LINE PLOT : Add sidebar interaction here
#############################################################



#############################################################
# PROFITS BY CATEGORY : Add sidebar interaction here
#############################################################



#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################



#############################################################
# MAP : Add interactions here
#############################################################

#MAP date interaction


#############################################################
#Grag and drop buttom interaction
#############################################################

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    df.columns=["Pagina","Probabilidad"]

    plt.figure(figsize=(10,10))
    
    fig = go.Figure(go.Bar(
            x=df["Probabilidad"],
            y=(df["Pagina"].astype(str)),
            orientation='h'))
    
    fig.update_layout(
    title={
        'text': "Páginas más probables",
        'y':0.8,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize=False,
    width=300,
    height=300,
    xaxis=dict(
        title_text="%Probabilidad",
        tickmode="array",
        titlefont=dict(size=15),
        ),
    yaxis=dict(
        title_text="Página",
        tickmode="array",
        titlefont=dict(size=15),
        tickformat=',d'
        ),
)
    ###############################################################
    #Inicio Parte nueva 20200729
    ###############################################################
    fig.write_image("assets/fig1.jpg")
    
    graph1=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("fig1.jpg"),
                    id="graph1-image",
                )
            ],className='graph1-style-image'
        )
    
    graph2=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("fig1.jpg"),
                    id="graph2-image",
                )
            ],className='graph2-style-image'
        )
    
    graph3=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("fig1.jpg"),
                    id="graph3-image",
                )
            ],className='graph3-style-image'
        )
    
    return html.Div(
                    [ 
                      graph1,
                      graph2,
                      graph3,
                    ]
                    )
    ###############################################################
    #Fin Parte nueva 20200729
    ###############################################################



@app.callback(Output('output-upload', 'children'),
              [Input('upload-file', 'contents')],
              [State('upload-file', 'filename'),
               State('upload-file', 'last_modified')])

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    
#############################################################
    
    
    

if __name__ == "__main__":
    app.run_server(debug=True)
