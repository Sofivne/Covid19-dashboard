from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#171B26",
    "color": "white"
}

sidebar = html.Div(
    [
        html.H2("COVID-19 Dashboard", className="display-6"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Top Countries Deaths", href="/top-countries-deaths", active="exact"),
                dbc.NavLink("Cases vs Deaths", href="/cases-vs-deaths", active="exact"),
                dbc.NavLink("Countries Comparison Map", href="/countries-comparison-map", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Div(
            [
                html.Hr(className="lead"),
                html.P("Author: Mahamoud", className="lead"),
            ]
        ),
    ],
    style=SIDEBAR_STYLE,
)


