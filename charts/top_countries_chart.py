import plotly.express as px
import pandas as pd
from data_processing import df

def generate_top_countries_death_chart():
    """
        Génère un graphique à barres des cinq pays ayant enregistré le plus grand nombre de décès liés au COVID-19.

        Returns:
        fig:
        Objet graphique Plotly Express.
        Un graphique à barres représentant les cinq pays ayant enregistré le plus grand nombre de décès liés au COVID-19.
    """
    total_deaths_by_country = df.groupby('Country')['Cumulative_deaths'].sum().reset_index()
    top_5_countries_deaths_largest = total_deaths_by_country.nlargest(5, 'Cumulative_deaths')

    fig = px.bar(top_5_countries_deaths_largest, x="Country", y="Cumulative_deaths",
                 color="Country", barmode="group", labels={'Cumulative_deaths': 'Total of death'}, title="Top 5 countries with the largest number of deaths")
    fig.layout.template = 'plotly_dark'
    return fig

top_countries_death_chart = generate_top_countries_death_chart()
