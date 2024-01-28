import numpy as np
import pandas as pd
import requests
from io import StringIO
import json

APIkey = 'IJE3GxCR4zy2Clp7SDMYsQ'

version = 'v1'


def getCompanies():
    pd.set_option('display.max_columns', None)
    
    url = 'https://api.usfundamentals.com/v1/indicators/xbrl?indicators=NetIncomeLoss&frequency=q&period_type=yq&companies=1418091&token=' + APIkey
    r = requests.get(url)
    df = pd.read_csv(StringIO(r.text.strip()))
    print(df)
