import plotly.express as px
import pandas as pd
from data_processing import df

def generate_cases_vs_deaths_chart():
    """
    Generates a scatter plot chart comparing the total cases and total deaths for each country.
    
    Returns:
        fig (plotly.graph_objs._figure.Figure): Scatter plot chart object.
    """
    grouped_data = df.groupby('Country').agg(
        Total_Cases=pd.NamedAgg(column='Cumulative_cases', aggfunc='max'),
        Total_Deaths=pd.NamedAgg(column='Cumulative_deaths', aggfunc='max'),
        New_Cases=pd.NamedAgg(column='New_cases', aggfunc='sum'),
        WHO_Region=pd.NamedAgg(column='WHO_region', aggfunc='first')
    ).reset_index()

    fig = px.scatter(grouped_data, x="Total_Cases", y="Total_Deaths",
                     size="New_Cases", color="WHO_Region", hover_name="Country",
                     log_x=True, size_max=60, title="Total Deaths vs Total Cases")
    fig.layout.template = 'plotly_dark'

    return fig

cases_vs_deaths_chart = generate_cases_vs_deaths_chart()
