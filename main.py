from fetch_api import fetch_data_from_api

country_codes = ["FR", "DE", "BE", "NL", "LU", "GB", "IE", "PT", "ES", "AT", "CH", "LI", "DK", "NO", "SE", "FI", "IS"]
pollutants = ["pm10", "pm25", "pm1"]


fetch_data_from_api(country_list=country_codes, pollutants_list=pollutants, days_to_fetch=30, max_page=15)


# PREPROCESSING DATA

"""
Here we 
"""


# START PLOTLY APP

"""
First We need to create a ploty dashboard 
"""