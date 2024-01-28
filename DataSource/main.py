import numpy as np
import pandas as pd
from alphavantage import AlphaVantage
from compustat import getParameter
import usfundamentals 
import sys

### Data Source from Alpha Vantage

AV = AlphaVantage()
FD = AV.FundamentalData()

symbol = 'AAPL'

incomeStatement = FD.IncomeStatement(symbol)
balanceSheet = FD.BalanceSheet(symbol)
cashFlow = FD.CashFlow(symbol)
earnings = FD.Earnings(symbol)


print(incomeStatement.getAnnualReports())
print(incomeStatement.getQuarterlyReports())

print(balanceSheet.getAnnualReports())
print(balanceSheet.getQuarterlyReports())

print(cashFlow.getAnnualReports())
print(cashFlow.getQuarterlyReports())

print(earnings.getAnnualEarnings())
print(earnings.getQuarterlyEarnings())

### Data Source from Compustat / Capital IQ (WRDS)

symbol = 'AAPL'
metric = 'revtq'
N = 1000 #max datapoints
startDate = "2000-01-01"
endDate = "2024-01-01"

getParameter(symbol, metric, N, startDate, endDate)


