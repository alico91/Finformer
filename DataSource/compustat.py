from requests import post as requests_post, get as requests_get
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

import sys

token = 'c3d6ae558ebb249d6e27ca7ca456685d29cf87a6'
headers = {
    'Authorization': 'Token c3d6ae558ebb249d6e27ca7ca456685d29cf87a6',
}


def fetch_all_data(api_url, iter, headers, params, data=[]):
    response = requests_get(api_url,headers=headers,params=params)
    response.raise_for_status()  # Raise exception for bad status codes
    
    # Append the data from the current response
    data.extend(response.json()['results'])
    
    # If there's a next page, recursively call the function with the next URL
    next_url = response.json().get('next')
    if next_url:
        fetch_all_data(next_url, iter-1, headers, params, data)
    
    return data



def getParameter(symbol, metric, N, startDate = "2000-01-01", endDate = "2024-01-01"):

    headers = {
        'Authorization': 'Token c3d6ae558ebb249d6e27ca7ca456685d29cf87a6',
    }


    params = {
        'limit' : 99,
        'tic__startswith': symbol,
        'datadate__gte': startDate,
        'datadate__lte': endDate,
    }

    api_url = "https://wrds-api.wharton.upenn.edu/data/comp.fundq/"

    df = fetch_all_data(api_url, np.ceil(N/99), headers, params)    
    dff = pd.DataFrame.from_dict(df)[['datadate',metric]]

    dff = dff[dff.astype(str).ne('None').all(1) & dff[metric] != 0.000]
    dff['datadate'] = pd.to_datetime(dff['datadate'].values)
    dff = dff.sort_values(by='datadate')
    dff[metric] = pd.to_numeric(dff[metric].values)
    print(dff)
    fig = px.line(dff, x="datadate", y=metric)
    fig.write_image("DataSource/OutputTest/img.jpeg")



    
# getParameter('AAPL','revtq', N=1000)