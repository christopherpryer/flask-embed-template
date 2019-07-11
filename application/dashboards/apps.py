"""Create a Dash app within a Flask app."""
from pathlib import Path
from dash import Dash, callback_context
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly_express as pe
from .layout import html_layout
import logging, sys
from .control import Service


# logging configuration
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


EXTERNAL_STYLESHEETS = ['/static/dist/css/load.css',
                        '/static/dist/css/styles.css',
                        'https://fonts.googleapis.com/css?family=Lato',
                        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                        '/static/dist/css/bWLwgP.css',
                        '/static/dist/css/stylesheet-oil-and-gas.css',
                        '/static/dist/css/styles.css']
EXTERNAL_SCRIPTS = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']

def Add_Review_Dash(server):
    """Create a Dash app."""
    dash_app = Dash(server=server,
                    external_stylesheets=EXTERNAL_STYLESHEETS,
                    external_scripts=EXTERNAL_SCRIPTS,
                    routes_pathname_prefix='/review/')

    # Override the underlying HTML template
    dash_app.index_string = html_layout
    dash_app.config['suppress_callback_exceptions'] = True

    # Review Data Model Obj.
    service = Service('Review')

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div(
        children=html.Div(
            html.Div(
                service.get_dash_children(), className='container-fluid',
                style={'width': '100%'}
            ),
            className='content-wrapper'),
        id='dash-container'
    )

    service.init_callbacks(dash_app)

    return dash_app.server