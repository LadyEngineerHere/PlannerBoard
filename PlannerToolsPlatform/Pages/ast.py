import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import callback
import dash_bootstrap_components as dbc  # Import Bootstrap components
import time


# Layout for the AST page
layout = html.Div([
    html.H1("AST Tool"),
    
    # Bootstrap Button to run the AST Dash app or executable
    dbc.Button("Run AST Dash App", id="run-btn", n_clicks=0, color="primary", className="mr-2"),
    
    # Placeholder for embedding the AST Dash app
    html.Div(id="dash-embed", children="AST Dash app will display here."),
    
    # Hidden div to store the URL and manage redirects
    dcc.Location(id="url", refresh=True),
])


