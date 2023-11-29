import pandas as pd

df = pd.read_csv('python\pandas_lib\cleaning.csv')

#get all totals 
dftotal = df.sum()

#Statistics for each column (excluding NaN values)
dfmean = df.mean(axis = 0)

#Round to 2 decimal places
print(dfmean.round(2))
