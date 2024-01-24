import numpy as np
import pandas as pd
from process import AlphaVantage

APIkey = 'PJCB1PM5LO1IW14L'

DS = AlphaVantage(APIkey)
FD = DS.FundamentalData(DS)

symbol = 'IBM'

incomeStatement = FD.IncomeStatement(FD, symbol)
balanceSheet = FD.BalanceSheet(FD, symbol)
cashFlow = FD.CashFlow(FD, symbol)
earnings = FD.Earnings(FD, symbol)

print(incomeStatement.getAnnualReports())
print(incomeStatement.getQuarterlyReports())

print(balanceSheet.getAnnualReports())
print(balanceSheet.getQuarterlyReports())

print(cashFlow.getAnnualReports())
print(cashFlow.getQuarterlyReports())

print(earnings.getAnnualEarnings())
print(earnings.getQuarterlyEarnings())





