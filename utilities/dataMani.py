import pandas as pd


def read_data(columns):
    
    df = pd.read_csv("chances.csv")
    if len(columns) > 0:
        
        df = df[columns]
        return df
    
    else:
        return df