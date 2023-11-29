import pandas as pd

df = pd.read_csv('python\pandas\cleaning.csv')
df.drop_duplicates(inplace=True)

print(df.duplicated())
