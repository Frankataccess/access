import pandas as pd

df = pd.read_csv('correlation.csv')

print(df.corr())