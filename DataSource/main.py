import numpy as np
import pandas as pd
from alphavantage import AlphaVantage


### Data Source from Alpha Vantage

AV = AlphaVantage()
FD = AV.FundamentalData()

symbol = 'IBM'

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




### Data Source from EODHD APIS


