import pandas as pd


def save_df_to_csv(df:pd.DataFrame, name:str) -> None:
    df.to_csv(name, index=False)