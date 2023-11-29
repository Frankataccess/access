import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('python/pandas/times.csv')

df["Date"] = pd.to_datetime(df['Date'])

df.plot(x="Date", y=["Duration","Calories"])

plt.show()