import pandas as pd

df = pd.read_csv("python\pandas\counting_pandas.py")

#Count all values in all columns
print(df.apply(pd.value_counts))
