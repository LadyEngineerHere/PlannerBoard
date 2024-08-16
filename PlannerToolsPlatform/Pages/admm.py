import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc



# Define the layout of the app
layout = html.Div([
    html.H1("ADM Manufacturer Match Report Page"),
    
    # Info Button and Modal
    dbc.Button("INFO", id="info-button", color="info", className="me-2"),
    dbc.Button("Upload Bemi List", id="upload-bemi-list", color="primary", className="upload-bemi-button"),
     
    dbc.Modal([
        dbc.ModalHeader("Info"),
        dbc.ModalBody(
            "This Tool is to Match the Manufacture on the Bemi List to the ones on the ADM list. "
            "Result will display match or no match. Additionally, this tool will take the BMW M number column "
            "and fill in the blanks with 'INPROCESSPARTS' for any blank entries."
        ),
        dbc.ModalFooter(
            dbc.Button("Close", id="close-info", className="ml-auto", n_clicks=0)
        )
    ], id="info-modal", is_open=False),
    
   

    
    # Centered Results Display
    html.Div(id="results-container", style={'textAlign': 'center', 'marginTop': '20px'}),
    
    # Download Buttons
    html.Div([
        dbc.Button("Download Report", id="download-report", color="secondary", className="me-2"),
        dbc.Button("Download ADM List", id="download-adm-list", color="secondary")
    ], style={'textAlign': 'center', 'marginTop': '20px'})
])





