import numpy as np
import pandas as pd
import requests
import pprint

class AlphaVantage:
    def __init__(self, APIkey) -> None:
        self.APIkey = APIkey
        pass


    class FundamentalData:

        def __init__(self, alphaVantage) -> None:
            self.APIkey = alphaVantage.APIkey
            
            pass

        class IncomeStatement:

            def __init__(self, fundamentalData, symbol) -> None:
                self.APIkey = fundamentalData.APIkey
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

            def __init__(self, fundamentalData, symbol) -> None:
                self.function = 'BALANCE_SHEET'
                self.APIkey = fundamentalData.APIkey
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()
            
            def getAnnualReports(self):
                return pd.DataFrame.from_dict(self.data['annualReports'])
            
            def getQuarterlyReports(self):
                return pd.DataFrame.from_dict(self.data['quarterlyReports'])

        class CashFlow:

            def __init__(self, fundamentalData, symbol) -> None:
                self.function = 'CASH_FLOW'
                self.APIkey = fundamentalData.APIkey
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()
            
            def getAnnualReports(self):
                return pd.DataFrame.from_dict(self.data['annualReports'])
            
            def getQuarterlyReports(self):
                return pd.DataFrame.from_dict(self.data['quarterlyReports'])

        class Earnings:

            def __init__(self, fundamentalData, symbol) -> None:
                self.function = 'EARNINGS'
                self.APIkey = fundamentalData.APIkey
                self.symbol = symbol
                url = 'https://www.alphavantage.co/query?function=' + self.function + '&symbol=' + self.symbol + '&apikey=' + self.APIkey
                r = requests.get(url)
                self.data = r.json()
            
            def getAnnualEarnings(self):
                return pd.DataFrame.from_dict(self.data['annualEarnings'])
            
            def getQuarterlyEarnings(self):
                return pd.DataFrame.from_dict(self.data['quarterlyEarnings'])


