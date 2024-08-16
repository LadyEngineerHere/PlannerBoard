import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc, html  
from dash.dependencies import Input, Output, State
from Pages import dashboard, ast, admm, qtyr, support
import base64
import io
import pandas as pd
import time

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sidebar content
sidebar = html.Div(
    [
        # BMW logo and Planner Portal
        html.Div(
            [
                html.Img(src="/assets/images/bmw.png", style={"width": "20px", "height": "20px", "margin-right": "13px"}),
                html.H2("Planner Portal", className="display-4", style={"color": "white", "font-size": "15px"}),
                html.Img(src="/assets/images/ToggleSideBar.png", style={"width": "15px", "height": "15px", "margin-right": "10px","margin-top": "-5px"}, className="white-icons"),
            ],
            className="d-flex align-items-center justify-content-between p-3",
        ),
        html.Hr(style={"borderColor": "white"}),

        # Navigation links
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Img(src="/assets/images/Dashboard.png", style={"width": "15px", "height": "15px", "margin-right": "10px"}, className="white-icons"),
                        html.Span("Dashboard", style={"color": "lightgrey", "font-size": "11px"})
                    ],
                    href="/dashboard",
                    id="dashboard-link",
                    className="d-flex align-items-center p-2",
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/images/AST.png", style={"width": "15px", "height": "15px", "margin-right": "10px"}, className="white-icons"),
                        html.Span("AST", style={"color": "lightgrey", "font-size": "11px"})
                    ],
                    href="/ast",
                    id="ast-link",
                    className="d-flex align-items-center p-2",
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/images/ADMM.png", style={"width": "15px", "height": "15px", "margin-right": "10px"}, className="white-icons"),
                        html.Span("ADMM", style={"color": "lightgrey", "font-size": "11px"})
                    ],
                    href="/admm",
                    id="admm-link",
                    className="d-flex align-items-center p-2",
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/images/QTYR.png", style={"width": "15px", "height": "15px", "margin-right": "10px"}, className="white-icons"),
                        html.Span("QTYR", style={"color": "lightgrey", "font-size": "11px"})
                    ],
                    href="/qtyr",
                    id="qtyr-link",
                    className="d-flex align-items-center p-2",
                ),
                html.Hr(style={"borderColor": "white"}),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/images/Support.png", style={"width": "15px", "height": "15px", "margin-right": "10px"}, className="white-icons"),
                        html.Span("Support", style={"color": "lightgrey", "font-size": "11px"})
                    ],
                    href="/support",
                    id="support-link",
                    className="d-flex align-items-center p-2",
                ),
            ],
            vertical=True,
            pills=True,
            className="sidebar",
        ),
    ],
    style={
        "position": "fixed",
        "top": "0",
        "left": "0",
        "bottom": "0",
        "width": "200px",
        "padding": "15px",
        "backgroundColor": "#1c1c1c",
        "border-radius": "15px",
    },
)



# Main content placeholder
content = html.Div(id="page-content", style={"margin-left": "250px", "padding": "20px"})

# App layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callback to highlight active tab and display content
@app.callback(
    [
        Output("dashboard-link", "className"),
        Output("ast-link", "className"),
        Output("admm-link", "className"),
        Output("qtyr-link", "className"),
        Output("support-link", "className"),
        Output("page-content", "children"),
    ],
    [Input("url", "pathname")],
)
def display_page(pathname):
    if pathname == "/dashboard" or pathname == "/":
        return (
            "d-flex align-items-center p-2 tab-selected",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            dashboard.layout,
        )
    elif pathname == "/ast":
        return (
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2 tab-selected",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            ast.layout,
        )
    elif pathname == "/admm":
        return (
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2 tab-selected",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            admm.layout,
        )
    elif pathname == "/qtyr":
        return (
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2 tab-selected",
            "d-flex align-items-center p-2",
            qtyr.layout,
        )
    elif pathname == "/support":
        return (
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2 tab-selected",
            support.layout,
        )
    else:
        return (
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            "d-flex align-items-center p-2",
            html.H1("404 Page Not Found"),
        )
        



# Define callback to toggle modal visibility
@app.callback(
    dash.dependencies.Output("info-modal", "is_open"),
    [dash.dependencies.Input("info-button", "n_clicks"),
     dash.dependencies.Input("close-info", "n_clicks")],
    [dash.dependencies.State("info-modal", "is_open")]
)
def toggle_modal(info_clicks, close_clicks, is_open):
    if info_clicks or close_clicks:
        return not is_open
    return is_open



# Callback to trigger the AST Dash app (or executable)
@app.callback(
    [Output("run-btn", "style"),
     Output("dash-embed", "children"),
     Output("url", "href")],  # Output to control redirect in case iframe fails
    [Input("run-btn", "n_clicks")],
    [State("dash-embed", "children")]  # State to check if iframe worked
)
def run_ast_dash_app(n_clicks, dash_embed_children):
    if n_clicks > 0:
        try:
            # Add a delay to ensure the AST Dash app starts up (if needed)
            time.sleep(2)

            # Try to embed the AST Dash app using an iframe
            iframe = html.Iframe(src="http://127.0.0.1:8051", style={"width": "100%", "height": "600px"})

            # Check if the iframe was able to load content
            if "AST Dash app will display here" in dash_embed_children:
                # If iframe is not loading, redirect to new tab
                return {"display": "none"}, dash_embed_children, "http://127.0.0.1:8051"
            else:
                # Hide the button and display the iframe
                return {"display": "none"}, iframe, None

        except Exception as e:
            return {"display": "block"}, f"Error: {e}", None

    # Button remains visible if no clicks, no iframe shown
    return {"display": "block"}, "AST Dash app will display here.", None








if __name__ == "__main__":
    app.run_server(debug=True)




