import requests
import json
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from pandas import json_normalize
import sys

username = 'COLUMBIA_STU-1761374'
APIkey = '5enwUVv42cKodY1VRmQZChYlVtCVcA9k3WsdWDT9'

authorization = (username,APIkey)

### Fundamental API

fundamentals_endpoint = 'https://api.factset.com/content/factset-fundamentals/v2/fundamentals'
fundamentals_request={
  "ids": [
    "AAPL-US"
  ],
  "periodicity": "QTR",
  "fiscalPeriodStart": "2010-09-01",
  "fiscalPeriodEnd": "2023-03-01",
  "metrics": [
    "FF_PE",
    "FF_EPS"
  ],
  "currency": "USD",
 "updateType": "RP"
}

headers = {'Accept': 'application/json','Content-Type': 'application/json'}

fundamentals_post = json.dumps(fundamentals_request)
fundamentals_response = requests.post(url = fundamentals_endpoint, data=fundamentals_post, auth = authorization, headers = headers, verify= False )
print('HTTP Status: {}'.format(fundamentals_response.status_code))

fundamentals_data = json.loads(fundamentals_response.text)
print(fundamentals_data)




### Price API

prices_endpoint = 'https://api.factset.com/content/factset-prices/v1/prices'
prices_request ={
  "ids": [
    "IBM-US",
    "FDS-US"
  ],
  "startDate": "2019-01-01",
  "endDate": "2019-08-30",
  "frequency": "D",
  "calendar": "FIVEDAY",
  "currency": "LOCAL",
  "adjust": "SPLIT"
}
headers = {'Accept': 'application/json','Content-Type': 'application/json'}

prices_post = json.dumps(prices_request)
prices_response = requests.post(url = prices_endpoint, data=prices_post, auth = authorization, headers = headers, verify= False )
print('HTTP Status: {}'.format(prices_response.status_code))

prices_data = json.loads(prices_response.text)
print(prices_data)
