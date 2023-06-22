import ast

import pandas as pd


def save_df_to_csv(df:pd.DataFrame, name:str) -> None:
    df.to_csv(name, index=False)
    
    
def convert_to_datetime(df:pd.DataFrame, column:str = "date") -> pd.DataFrame:
    
    df[column] = df[column].map(lambda x: x['utc'])
    df[column] = pd.to_datetime(df[column])
    
    return df    

def generate_coordinate_columns(df):    
        
    df['latitude'] = df['coordinates'].map(lambda x: x['latitude'])
    df['longitude'] = df['coordinates'].map(lambda x: x['longitude'])
    
        