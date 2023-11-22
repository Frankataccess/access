import pandas as pd

df = pd.read_csv("cleaning.csv")

new_df = df.dropna()
x = new_df["Calories"].mean()

new_df["Calories"].fillna(x, inplace=True)
new_df['Date'] = pd.to_datetime(new_df['Date'])  # Corrected line

print(new_df.to_string())