import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def split_features_target(df):
    X = df[['temperatura']]
    y = df['vendas']
    return X, y
