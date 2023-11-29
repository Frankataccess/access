import pandas as pd


df = pd.read_csv('python\pandas\correlation.csv')

print(df.corr())