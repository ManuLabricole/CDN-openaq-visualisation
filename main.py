import ast

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

from fetch_api import fetch_data_from_api
from utils import (convert_to_datetime, generate_coordinate_columns,
                   save_df_to_csv)

country_codes = ["FR", "DE", "BE", "NL", "LU", "GB", "IE", "PT", "ES", "AT", "CH", "LI", "DK", "NO", "SE", "FI", "IS"]
pollutants = ["pm10", "pm25", "pm1"]

fetch = False

data_file = "df_pages_15.csv"

if fetch:
    fetch_data_from_api(country_list=country_codes, pollutants_list=pollutants, days_to_fetch=30, max_page=15)
else:
    print("Data already fetched")
    df = pd.read_csv(data_file)


# PREPROCESSING DATA

"""
We need to preprocess the data to make it usable for our dashboard
To do this we will create a new file called utils.py
This file will contain all the functions we need to preprocess the data
Then we will import this file in our main.py
And we will call the functions we need to preprocess the data
"""

print("[RUNNING] Preprocessing data")
df = convert_to_datetime(df, column="date")




# START PLOTLY APP


"""
First We need to create a ploty dashboard 
"""

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='data-table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    
