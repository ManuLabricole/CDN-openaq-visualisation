import pandas as pd
import datetime
import timedelta

date_to = datetime.now()
date_from = date_to - timedelta(days=30)

date_to = date_to.isoformat()
date_from = date_from.isoformat()

country_codes = ["FR", "DE", "BE", "NL", "LU", "GB", "IE", "PT", "ES", "AT", "CH", "LI", "DK", "NO", "SE", "FI", "IS"]
pollutants = ["pm10", "pm25", "pm1"]

df = pd.DataFrame()
# Loop over countries and pollutants and make API requests
for page in range(1, 10):
    print("---------------------------------------------------------------------------")
    print(f"Getting page {page}")
    print("---------------------------------------------------------------------------\n")
    
    url = f"https://api.openaq.org/v2/measurements?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-29T15%3A10%3A00%2B00%3A00&limit=100&page={page}&offset=0&sort=desc&radius=1000&order_by=datetime"

    for country in country_codes:
        for pollutant in pollutants:
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
                df = pd.concat([df, df_temp])
            else:
                print(f"Failed to fetch data for country {country} and pollutant {pollutant} after 5 retries.")