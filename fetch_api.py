import time
from datetime import datetime, timedelta

import pandas as pd
import requests

from utils import save_df_to_csv


def fetch_data_from_api(country_list:list, pollutants_list:list, days_to_fetch:30, max_page=10):
    
    date_to = datetime.now() 
    print(date_to)
    date_from = date_to - timedelta(days=days_to_fetch)
    #
    date_to = date_to.isoformat()
    date_from = date_from.isoformat()

    df = pd.DataFrame()
    # Loop over countries and pollutants and make API requests
    for page in range(1, max_page):
        print("---------------------------------------------------------------------------")
        print(f"Getting page {page}")
        print("---------------------------------------------------------------------------\n")

        url = f"https://api.openaq.org/v2/measurements?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-29T15%3A10%3A00%2B00%3A00&limit=100&page={page}&offset=0&    sort=desc&radius=1000&order_by=datetime"

        for country in country_list:
            print("---------------------------------------------------------------------------")
            print(f"Country fectched {country}")
            print("---------------------------------------------------------------------------\n")
            for pollutant in pollutants_list:
                print(f"Fetching {pollutant}...")
                
                params = {
                    "country": country,
                    "date_from": date_from,
                    "date_to": date_to,
                    "parameter": pollutant,
                    "limit": 1000  # increase this number if needed
                }
                # Initialize a flag for whether the request was successful
                success = False
                
                # Try the request up to 5 times
                for i in range(5):
                    response = requests.get(url, params=params)
                    # If the request was successful, break out of the retry loop
                    if response.status_code == 200:
                        print(f"SUCCESS -> {url}")
                        success = True
                        break
                    else:
                        print(f"Request failed for country {country} and pollutant {pollutant}. Status code: {response.status_code}. Retry number: {i+1}.")
                        # Wait for 1 second before trying again
                        time.sleep(1)
                # If the request was successful after all retries, add the data to the DataFrame
                if success:
                    data = response.json()
                    df_temp = pd.DataFrame(data['results'])
                    print(f"[SUCCES] --> Fetch df of shape {df_temp.shape}")
                    df = pd.concat([df, df_temp])
                else:
                    print(f"Failed to fetch data for country {country} and pollutant {pollutant} after 5 retries.")
                    
    save_df_to_csv(df, f"df_pages_{max_page}.csv")
            