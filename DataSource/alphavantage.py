import numpy as np
import pandas as pd
import requests
import pprint

APIkey = 'PJCB1PM5LO1IW14L'

class AlphaVantage:
    def __init__(self) -> None:
        pass


    class FundamentalData:

        def __init__(self) -> None:            
            pass

        class IncomeStatement:

            def __init__(self, symbol) -> None:
                self.APIkey = APIkey
                self.function = 'INCOME_STATEMENT'
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()

            
            def getAnnualReports(self):
                return pd.DataFrame.from_dict(self.data['annualReports'])
            
            def getQuarterlyReports(self):
                return pd.DataFrame.from_dict(self.data['quarterlyReports'])
        
        class BalanceSheet:

            def __init__(self, symbol) -> None:
                self.function = 'BALANCE_SHEET'
                self.APIkey = APIkey
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()
            
            def getAnnualReports(self):
                return pd.DataFrame.from_dict(self.data['annualReports'])
            
            def getQuarterlyReports(self):
                return pd.DataFrame.from_dict(self.data['quarterlyReports'])

        class CashFlow:

            def __init__(self, symbol) -> None:
                self.function = 'CASH_FLOW'
                self.APIkey = APIkey
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()
            
            def getAnnualReports(self):
                return pd.DataFrame.from_dict(self.data['annualReports'])
            
            def getQuarterlyReports(self):
                return pd.DataFrame.from_dict(self.data['quarterlyReports'])

        class Earnings:

            def __init__(self, symbol) -> None:
                self.function = 'EARNINGS'
                self.APIkey = APIkey
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()
            
            def getAnnualEarnings(self):
                return pd.DataFrame.from_dict(self.data['annualEarnings'])
            
            def getQuarterlyEarnings(self):
                return pd.DataFrame.from_dict(self.data['quarterlyEarnings'])


