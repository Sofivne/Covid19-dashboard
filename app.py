import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output 
from layouts.sidebar import sidebar
from layouts.content import content
from layouts.home import home
from charts.top_countries_chart import top_countries_death_chart
from charts.cases_vs_deaths_chart import cases_vs_deaths_chart
from charts.countries_comparison_map_chart import generate_country_graph
from data_processing import df

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, r"./assets/styles.css"], suppress_callback_exceptions=True)

store = dcc.Store(id='data-store', data=df.to_dict('records'))

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
    store
])

@app.callback(
    Output('country-graph', 'children'),
    [Input('country-dropdown', 'value')]
)
def display_country_graph(selected_country):
    filtered_data = df[df['Country'] == selected_country]
    fig = generate_country_graph(filtered_data, selected_country)

    return dcc.Graph(figure=fig)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname: str):
    """
        Renvoie le contenu de la page en fonction du chemin d'accès (URL) fourni.

        Args:
        pathname (str): Le chemin d'accès (URL) vers la page.

        Returns:
        html.Div:
            Un élément Div HTML contenant le contenu de la page correspondant au chemin d'accès (URL) fourni.
            Si le chemin d'accès est '/', renvoie le contenu de la page d'accueil.
            Si le chemin d'accès est '/top-countries-deaths', renvoie le graphique des pays ayant enregistré le plus de décès.
            Si le chemin d'accès est '/cases-vs-deaths', renvoie le graphique des cas par rapport aux décès.
            Si le chemin d'accès est '/countries-comparison-map', renvoie la carte de comparaison des pays.
            Si le chemin d'accès n'est pas reconnu, renvoie un message d'erreur 404.
    """
    if pathname == "/":
        return home
    elif pathname == "/top-countries-deaths":
         return html.Div([
        html.H1("Top Countries Deaths", className="text-h1"),  
        html.P("Le graphique suivant présente les cinq pays où le nombre de décès est le plus élevé."),
        dcc.Graph(id='top-countries-deaths', figure=top_countries_death_chart)
    ])
    elif pathname == "/cases-vs-deaths":
         return html.Div([
        html.H1("Cases vs Deaths", className="text-h1"), 
        html.P("Le graphique suivant est un nuage de points comparant les décès liés à COVID-19 aux cas liés à COVID-19."),
        dcc.Graph(id='cases-vs-deaths', figure=cases_vs_deaths_chart)
    ])
    elif pathname == "/countries-comparison-map":
         return html.Div([
            html.H1("Countries Comparison Map", className="text-h1"), 
            html.P("La carte suivante est une carte de dispersion géographique comparant les décès liés à COVID-19 de certains pays."),
            html.Div([
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': country, 'value': country} for country in ['-- Choisir un pays --','France', 'United States of America', 'Morocco', 'Thailand', 'Japan', 'Argentina']],
                    value='France'
                )
            ]),
            html.Div(id='country-graph')
        ])
    else:
        return html.Div([
            html.H1("404: Not found", className="text-danger"),
        ], className="p-3 bg-light rounded-3")




if __name__ == "__main__":
    app.run(debug=True)
