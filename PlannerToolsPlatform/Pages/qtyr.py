import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

layout = html.Div([
    html.H1("Quantity Match Report Page"),
    
        # Info Modal Button
    html.Div([
        dbc.Button("Info", id="open-info-modal", color="info"),
        dbc.Modal([
            dbc.ModalHeader("Page Information"),
            dbc.ModalBody(html.Div([
                html.P("This page allows you to upload your parts list (BEMI) for comparison with existing inventory."),
                html.P("Upload BEMI List: Upload your initial parts list to generate a comparison report."),
                html.P("Upload BEMI Finalized List: After reviewing the report, upload your finalized list. Note: Only upload once."),
                html.P("Download Report: After generating the report, you can download it for your records.")
            ])),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-info-modal", className="ml-auto")
            ),
        ], id="info-modal", is_open=False),
    ], style={'margin-bottom': '20px'}),
    
    # Upload BEMI List Section
    html.H2("Upload BEMI List"),
    html.P("Upload your parts list to compare it with existing inventory and generate a report."),
    # Placeholder for the file upload component
     dbc.Button("Upload Bemi List", id="open-warning-modal3", color="primary"),
    html.Div(id='upload-bemi-section', children=[
        # Replace this comment with your file upload component, e.g., dcc.Upload()
    ]),

   

    # Generated Report Section
    html.H2("Generated Report"),
    html.P("After uploading your BEMI list, the report below will compare it with existing inventory."),
    # Placeholder for the report generation and display
    html.Div(id='report-section', children=[
        # Replace this comment with the logic to generate and display the report
    ]),
    
     # Download Report Button
    html.Div([
        dbc.Button("Download Report", id="download-report-button", color="primary"),
        # Placeholder for the download functionality
        html.Div(id='download-section')
    ], style={'margin-top': '20px'}),
    
    
     # Upload BEMI Finalized List with Warning Modal
    html.H2("Upload BEMI Finalized List"),
    html.P("Upload your finalized parts list after reviewing the generated report."),
    html.Div([
        dbc.Button("Upload Finalized List", id="open-warning-modal2", color="danger"),
        dbc.Modal([
            dbc.ModalHeader("Warning"),
            dbc.ModalBody(html.Div([
                html.P("Warning: Do not upload more than one list. This should be your finalized list."),
                html.P("Ensure that your final list is correct, as it will be stored in the qty database.")
            ], style={'color': 'red'})),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-warning-modal2", className="ml-auto")
            ),
        ], id="warning-modal2", is_open=False),
    ], style={'margin-bottom': '20px'}),
    # Placeholder for the final list upload component
    html.Div(id='upload-finalized-section', children=[
        # Replace this comment with your final submission component, e.g., dcc.Upload()
    ]),
])

