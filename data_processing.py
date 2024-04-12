import pandas as pd


def preprocess_data() -> pd.DataFrame:
    df = pd.read_csv(r"./resources/WHO-COVID-19-global-data.csv")
    return df

df = preprocess_data()
