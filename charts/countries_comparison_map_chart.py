# countries_comparison_map_chart.py
import plotly.express as px
import pandas as pd
from data_processing import df

def generate_country_graph(filtered_data, selected_country: str):
    """
        Génère un graphique à barres montrant le nombre total de cas dans un pays sélectionné au fil du temps.

        Args :
            filtered_data (DataFrame) : Les données filtrées contenant les cas de COVID-19.
            selected_country (str) : Le nom du pays sélectionné.

        returns :
            fig (plotly.graph_objs.Figure) : Le graphique à barres généré.
    """
    fig = px.bar(filtered_data, x='Date_reported', y='Cumulative_cases',
                 labels={'Cumulative_cases': 'Total Cases'},
                 title=f'Total Cases in {selected_country}')
    fig.layout.template = 'plotly_dark'

    return fig