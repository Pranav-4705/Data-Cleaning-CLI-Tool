import pandas as pd

def clean_data(path):
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)
    df.ffill(inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
